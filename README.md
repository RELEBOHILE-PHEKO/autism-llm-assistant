# 🧩 Early Autism Screening Guidance Chatbot

A domain-specific LLM assistant fine-tuned to provide educational guidance on early autism screening, developmental milestones, and support resources for caregivers, teachers, and healthcare workers.

> **⚠️ MEDICAL DISCLAIMER**: This is an educational tool only. It does **NOT** provide medical diagnoses. Always consult licensed healthcare professionals for concerns about child development.

---

## 📋 Project Overview

- **Model**: `google/gemma-2b-it` (Gemma 2B Instruct)
- **Fine-tuning Method**: QLoRA (4-bit quantization + LoRA adapters)
- **Dataset**: ~890 synthetic instruction-response pairs covering autism screening topics
- **Framework**: HuggingFace Transformers + PEFT + TRL + BitsAndBytes
- **Deployment**: Gradio web interface
- **Hardware**: Optimized for free-tier Google Colab/Kaggle (T4 GPU, ~15GB VRAM)

---

## 🚀 Quick Start

### 1. **Generate the Dataset**

```bash
python create_dataset.py
```

This creates `data/autism_screening_guidance.jsonl` with ~890 instruction-response examples covering:
- Early autism signs
- Speech and language delays
- Sensory sensitivities
- Developmental milestones
- Screening tools (M-CHAT-R)
- Myths vs facts
- Support strategies for parents and educators

### 2. **Fine-tune the Model** (Google Colab/Kaggle)

1. Open [`finetune-llm.ipynb`](finetune-llm.ipynb) in Google Colab or Kaggle
2. **Runtime → Change runtime type → GPU** (T4 recommended, ~15GB VRAM)
3. Run all cells sequentially
4. The notebook will:
   - Clone this repository
   - Generate the dataset
   - Load Gemma-2B-IT with 4-bit quantization
   - Apply LoRA adapters (rank-8, alpha-16)
   - Fine-tune for 2 epochs (~30-40 minutes on T4)
   - Save the model to `autism_guidance_gemma_2b/`

**Note**: You'll need a HuggingFace token with access to Gemma models. Get one at [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens).

### 3. **Run the Chatbot Locally**

After fine-tuning, download the `autism_guidance_gemma_2b/` folder and run:

```bash
pip install -r requirements.txt
python app.py
```

The Gradio interface will launch at `http://localhost:7860`.

---

## 📂 Repository Structure

```
autism-llm-assistant/
├── finetune-llm.ipynb          # Main fine-tuning notebook (Colab/Kaggle)
├── create_dataset.py           # Dataset generation script
├── app.py                      # Gradio chatbot UI
├── requirements.txt            # Python dependencies
├── data/
│   └── autism_screening_guidance.jsonl  # Generated dataset
├── autism_guidance_gemma_2b/   # Fine-tuned model (created after training)
│   ├── adapter_config.json
│   ├── adapter_model.safetensors
│   ├── tokenizer.json
│   └── ...
├── README.md                   # This file
├── REPORT.md                   # Technical report
├── SUBMISSION.md               # Assignment submission notes
└── QUICK_REFERENCE.txt         # Quick tips
```

---

## 🎯 Features

### ✅ Domain Expertise
- Trained on 890+ expert-level Q&A pairs
- Covers early signs, screening tools, milestones, myths vs facts
- Provides age-appropriate guidance (infants, toddlers, preschoolers)

### 🛡️ Safety Guardrails
1. **Banned Phrases**: Blocks harmful misinformation (e.g., "vaccines cause autism")
2. **Domain Filtering**: Redirects off-topic questions back to autism/child development
3. **Medical Disclaimer**: Appended to every response

### 🎨 User-Friendly Interface
- Multi-turn conversation history
- Pre-loaded example questions
- Links to authoritative resources (CDC, M-CHAT, Autism Speaks)
- Clean, accessible Gradio UI

---

## 📊 Dataset Details

**Format**: JSONL with `instruction`, `input`, `output` fields

**Topics** (10 categories, ~90 examples each):
1. Early autism signs (social, communication, behavioral)
2. Speech and language delays
3. Sensory processing differences
4. Repetitive behaviors and restricted interests
5. Developmental milestones (0-5 years)
6. Screening tools (M-CHAT-R, ASQ)
7. Myths and facts about autism
8. When to seek professional evaluation
9. Support strategies for parents/caregivers
10. Educational accommodations for teachers

**Safety**:
- All responses include a medical disclaimer
- 10 out-of-domain examples teach polite refusals
- Guardrails prevent diagnostic claims

---

## 🔧 Technical Details

### Model Architecture
- **Base Model**: Gemma 2B Instruct (2.5B parameters)
- **Quantization**: 4-bit NormalFloat (nf4) via BitsAndBytes
- **LoRA Configuration**:
  - Rank (r): 8
  - Alpha: 16
  - Target modules: Q, K, V, O projections + MLP (gate, up, down)
  - Dropout: 0.05
  - Trainable parameters: ~19.6M (~0.8% of total)

### Training Configuration
- **Learning Rate**: 1e-5 (cosine LR scheduler)
- **Batch Size**: 1 per device
- **Gradient Accumulation**: 16 steps (effective batch 16)
- **Epochs**: 2
- **Precision**: BFloat16 mixed precision
- **Hardware**: NVIDIA T4 (15GB VRAM)
- **Training Time**: ~30-40 minutes

### Chat Template
Uses Gemma's official format:
```
<start_of_turn>user
{question}<end_of_turn>
<start_of_turn>model
{response}<end_of_turn>
```

---

## 📈 Evaluation Metrics

The notebook includes comprehensive evaluation:

1. **ROUGE-1/ROUGE-L**: Unigram and longest subsequence overlap
2. **BLEU**: N-gram precision
3. **Perplexity**: Model confidence on domain text
4. **Qualitative**: Side-by-side comparisons (base vs fine-tuned)
5. **Hyperparameter Experiments**: 3 runs with varying LR, LoRA rank, epochs

Typical improvements after fine-tuning:
- ROUGE-L: +40-60%
- BLEU: +50-80%
- Perplexity: 20-30% lower
- Qualitative: More specific, actionable, domain-appropriate responses

---

## 🎓 Use Cases

This chatbot is designed for:

✅ **Parents/Caregivers**: Learn early autism signs, when to seek screening  
✅ **Educators**: Understand classroom accommodations and support strategies  
✅ **Community Health Workers**: Provide evidence-based screening guidance  
✅ **Students/Researchers**: Educational resource on autism screening practices  

❌ **NOT for**:
- Medical diagnosis
- Treatment recommendations
- Replacing professional healthcare advice

---

## 🔐 Safety & Ethics

### Implemented Safeguards
1. **Medical Disclaimer**: Every response includes a clear notice
2. **Misinformation Blocking**: Banned phrases list (vaccines, cures, diagnoses)
3. **Domain Constraints**: Refuses unrelated questions politely
4. **Source Attribution**: Links to CDC, M-CHAT, Autism Speaks
5. **Supervised Deployment**: Intended for educational settings with human oversight

### Known Limitations
- Synthetic dataset (not clinically validated)
- May hallucinate specific facts (verify with authoritative sources)
- English-only
- Not suitable for crisis intervention or urgent medical decisions

---

## 📦 Installation & Requirements

### Python Dependencies
```bash
pip install -r requirements.txt
```

### Key Libraries
- `transformers>=4.36.0`
- `peft>=0.7.0`
- `bitsandbytes>=0.41.0`
- `trl>=0.7.0`
- `torch>=2.0.0`
- `gradio>=4.0.0`
- `datasets`, `accelerate`, `evaluate`, `nltk`, `sentencepiece`

### Hardware Requirements
- **Training**: NVIDIA GPU with 15GB+ VRAM (T4, V100, A100)
- **Inference**: GPU recommended (4-8GB VRAM) or CPU (slower)

---

## 🤝 Contributing

This is an educational project. Contributions welcome for:
- Dataset expansion (more diverse examples)
- Additional safety guardrails
- Multi-language support
- Improved evaluation metrics

Please ensure all contributions maintain the ethical guidelines and medical disclaimers.

---

## 📚 Resources

- **Autism Information**: [CDC Autism & Developmental Disabilities](https://www.cdc.gov/autism)
- **Screening Tool**: [M-CHAT-R Official Site](https://mchatscreen.com)
- **Support Organization**: [Autism Speaks](https://www.autismspeaks.org)
- **Model**: [Gemma on HuggingFace](https://huggingface.co/google/gemma-2b-it)

---

## 📄 License

This project is for educational purposes. The Gemma model is subject to its own license terms. Dataset and code are provided as-is for academic use.

---

## 👨‍💻 Author

**RELEBOHILE PHEKO**  
GitHub: [@RELEBOHILE-PHEKO](https://github.com/RELEBOHILE-PHEKO)

---

## 🙏 Acknowledgments

- **Google**: For releasing Gemma models
- **HuggingFace**: For transformers, PEFT, and TRL libraries
- **CDC & Autism Speaks**: For evidence-based screening guidance
- **Colab/Kaggle**: For free GPU access

---

**Last Updated**: February 2026
