# Early Autism Screening Guidance Chatbot


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

#
