"""
Gradio UI for Autism Screening Guidance Chatbot.
Run after fine-tuning: python app.py
Loads the fine-tuned Gemma-2B-IT model from autism_guidance_gemma_2b/
"""

import gradio as gr
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from peft import PeftModel

MODEL_NAME = "google/gemma-2b-it"
ADAPTER_PATH = "autism_guidance_gemma_2b"
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Load tokenizer
print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(ADAPTER_PATH)
tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_side = 'right'

# Load base model with 4-bit quantization for efficiency
print("Loading base model...")
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type='nf4',
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_use_double_quant=True,
)

base = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    quantization_config=bnb_config,
    device_map="auto"
)

# Load LoRA adapter
print("Loading LoRA adapter...")
model = PeftModel.from_pretrained(base, ADAPTER_PATH)
model.eval()
print("✓ Model loaded successfully!")

# Safety guardrails
BANNED_PHRASES = [
    'vaccines cause autism',
    'cure autism',
    'diagnose my child',
    'autism is caused by bad parenting',
]

DOMAIN_KEYWORDS = [
    'autism', 'asd', 'child', 'toddler', 'infant', 'baby',
    'screening', 'development', 'speech', 'behavior', 'behaviour',
    'milestone', 'social', 'm-chat', 'sensory', 'eye contact', 'nonverbal',
]

DISCLAIMER = (
    '\n\n*General educational information only — '
    'not a medical diagnosis. Please consult a licensed healthcare professional.*'
)


def generate_response(question: str, max_new_tokens: int = 512) -> str:
    """Generate response using Gemma-2B-IT chat template."""
    prompt = (
        f'<start_of_turn>user\n{question}<end_of_turn>\n'
        f'<start_of_turn>model\n'
    )
    inputs = tokenizer(prompt, return_tensors='pt').to(model.device)
    
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            repetition_penalty=1.2,
            no_repeat_ngram_size=3,
            eos_token_id=tokenizer.eos_token_id,
            pad_token_id=tokenizer.pad_token_id,
            use_cache=True,
        )
    
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    parts = decoded.split('model\n')
    if len(parts) > 1:
        return parts[-1].strip()
    return decoded.strip()


def safe_chat(question: str) -> str:
    """Apply guardrails then generate response."""
    ql = question.lower()
    
    if any(phrase in ql for phrase in BANNED_PHRASES):
        return (
            'I cannot provide medical diagnoses or spread misinformation. '
            'Please consult a licensed healthcare professional or visit '
            'cdc.gov/autism for trusted resources.' + DISCLAIMER
        )
    
    if not any(kw in ql for kw in DOMAIN_KEYWORDS):
        return (
            'I am designed to help with early autism screening and child '
            'development guidance. Could you rephrase your question in '
            'that context?' + DISCLAIMER
        )
    
    return generate_response(question) + DISCLAIMER


EXAMPLE_QUESTIONS = [
    'What are early signs of autism in a 2-year-old?',
    'How is the M-CHAT-R screening tool used?',
    'My child does not respond to their name at 12 months.',
    'What developmental milestones should a toddler have by age 2?',
    'How can I support my child with autism at home?',
]


def respond(message: str, history: list) -> tuple:
    """Process user message and return updated conversation history."""
    if not message.strip():
        return '', history
    reply = safe_chat(message)
    history.append((message, reply))
    return '', history


with gr.Blocks(
    title='Early Autism Screening Guidance',
    theme=gr.themes.Soft(primary_hue='blue'),
) as demo:
    
    gr.Markdown(
        '# 🧩 Early Autism Screening Guidance Chatbot\n'
        '**Powered by Gemma-2B-IT fine-tuned with QLoRA**\n\n'
        '> **Medical Disclaimer:** General educational information only. '
        'Not a substitute for professional medical advice or diagnosis. '
        "Always consult a licensed healthcare provider about your child's development."
    )
    
    chatbot = gr.Chatbot(label='Conversation', height=500)
    msg_box = gr.Textbox(
        placeholder='Ask about early autism signs, milestones, screening tools...',
        label='Your question',
        lines=2,
    )
    
    with gr.Row():
        submit_btn = gr.Button('Send ➤', variant='primary')
        clear_btn = gr.Button('Clear conversation')
    
    gr.Examples(
        examples=EXAMPLE_QUESTIONS,
        inputs=msg_box,
        label='Example questions — click to use',
    )
    
    gr.Markdown(
        '---\n'
        '**Resources:** '
        '[CDC Autism Info](https://www.cdc.gov/autism) · '
        '[M-CHAT Screening](https://mchatscreen.com) · '
        '[Autism Speaks](https://www.autismspeaks.org)'
    )
    
    # Wire interactions
    submit_btn.click(respond, [msg_box, chatbot], [msg_box, chatbot])
    msg_box.submit(respond, [msg_box, chatbot], [msg_box, chatbot])
    clear_btn.click(lambda: ([], ''), None, [chatbot, msg_box])

if __name__ == "__main__":
    demo.launch()
