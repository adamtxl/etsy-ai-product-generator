# Etsy AI Product Generator

Generate AI-inspired Etsy product ideas from existing listings and remix them into new styles.

## Features

- Scrapes top Etsy product from Google Shopping
- Describes listing with AI
- Reimagines listing in a different aesthetic style

## How to Run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Visit `http://127.0.0.1:8000/generate?keyword=boho+mug&style=cyberpunk`
