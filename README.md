# Early Autism Screening Guidance Chatbot

Fine-tuning **TinyLlama 1.1B** with **LoRA** to create an early autism screening guidance chatbot for caregivers, teachers, and community health workers.

> **Important:** This chatbot does **not** diagnose autism. It provides guidance, raises awareness, and encourages professional screening.

---

## Project Overview

| Item | Details |
|------|---------|
| **Domain** | Healthcare / Child Development |
| **Base Model** | TinyLlama 1.1B Chat |
| **Method** | LoRA + 4-bit quantization |
| **Dataset** | 800–900 instruction examples (JSONL) |
| **Target Users** | Caregivers, teachers, community health workers |

---

## Repository Structure

```
autism-llm-assistant-1/
├── finetune_llm.ipynb      # Colab/Kaggle fine-tuning notebook
├── create_dataset.py       # Generates instruction dataset (JSONL)
├── data/
│   └── autism_screening_guidance.jsonl
├── app.py                  # Gradio UI (run after fine-tuning)
└── README.md
```

---

## Quick Start

### 1. Generate the Dataset

```bash
python create_dataset.py
```

Creates `data/autism_screening_guidance.jsonl` (~890 examples).

### 2. Fine-tune (Colab / Kaggle)

1. Open `finetune_llm.ipynb` in Google Colab or Kaggle.
2. **Runtime → Change runtime type → GPU** (T4 recommended).
3. Upload the repo (or clone) and run all cells.
4. Ensure `data/autism_screening_guidance.jsonl` and `create_dataset.py` are present.

### 3. Run the Gradio UI

```bash
pip install gradio
python app.py
```

---

## Dataset

- **Format:** JSONL with `instruction`, `input`, `output`
- **Topics:** Early autism signs, speech delay, sensory sensitivities, repetitive behaviors, social challenges, myths vs facts, when to seek screening, guidance for parents/teachers
- **Safety:** All domain responses include a disclaimer: *"This is not a diagnosis. Please consult a healthcare professional."*
- **Out-of-domain:** 10 examples with polite refusals

---

## Training Configuration

| Setting | Value |
|---------|-------|
| Batch size | 2 |
| Gradient accumulation | 8 |
| Learning rate | 2e-5 |
| Epochs | 2 |
| LoRA r | 8 |
| LoRA alpha | 16 |
| Max sequence length | 512 |

---

## Evaluation

- **Quantitative:** BLEU, ROUGE-L, perplexity  
- **Qualitative:** Base vs fine-tuned output comparison  
- **Experiments table:** Learning rate, batch size, epochs, GPU RAM, loss (for report)

---

## Requirements

- Python 3.8+
- GPU (8GB+ VRAM; T4 works on free Colab)
- `transformers`, `datasets`, `peft`, `accelerate`, `bitsandbytes`, `trl`, `gradio`

---

## License & Ethics

- For **academic and educational use** only.
- Not a substitute for professional medical or developmental evaluation.
- Designed to be supportive and culturally sensitive.
- Always encourages consultation with healthcare professionals.
