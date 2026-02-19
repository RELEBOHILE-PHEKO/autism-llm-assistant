"""
Gradio UI for Autism Screening Guidance Chatbot.
Run after fine-tuning: python app.py
Loads the fine-tuned model from autism_guidance_model/
"""

import gradio as gr
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
ADAPTER_PATH = "autism_guidance_model"
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Load base + LoRA
print("Loading model...")
base = AutoModelForCausalLM.from_pretrained(MODEL_NAME, device_map="auto", torch_dtype=torch.float16)
model = PeftModel.from_pretrained(base, ADAPTER_PATH)
tokenizer = AutoTokenizer.from_pretrained(ADAPTER_PATH)
model.eval()


def chat(question: str) -> str:
    prompt = f"<|user|>\n{question}\n<|assistant|>\n"
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    with torch.no_grad():
        out = model.generate(
            **inputs,
            max_new_tokens=256,
            temperature=0.7,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id,
        )
    text = tokenizer.decode(out[0], skip_special_tokens=True)
    if "<|assistant|>" in text:
        return text.split("<|assistant|>")[-1].strip()
    return text.strip()


with gr.Blocks(title="Autism Screening Guidance") as demo:
    gr.Markdown("""
    ## Early Autism Screening Guidance Chatbot
    For caregivers, teachers, and community health workers.
    **This is not a diagnosis. Please consult a healthcare professional.**
    """)
    inp = gr.Textbox(label="Your question", placeholder="e.g. What are early signs of autism in toddlers?")
    out = gr.Textbox(label="Response", lines=6)
    btn = gr.Button("Ask")
    btn.click(fn=chat, inputs=inp, outputs=out)
    gr.Examples(
        examples=[
            "What are early signs of autism in toddlers?",
            "When should I seek autism screening for my child?",
            "Is autism caused by vaccines?",
            "How can teachers support autistic students?",
        ],
        inputs=inp,
    )

if __name__ == "__main__":
    demo.launch()
