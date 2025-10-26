# AI-API
AI API uzdevums RVT

# Hugging Face Python demo

Šis repo demonstrē:
- branch + PR ar uzdevuma pirmās puses izpildi;
- Python skriptu, kas izsauc Hugging Face API ar hard-coded promptu;
- drošu API atslēgas glabāšanu GitHub Secrets.


## Lietošana lokāli

```bash
git clone <repo-url>
cd {}
cp .env
# aizpildiet HUGGINGFACE_API_KEY
python -m pip install -r requirements.txt
python main.py