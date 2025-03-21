import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def describe_listing(listing_text):
    prompt = f"""
You are an expert Etsy seller and product analyst.

Given the following Etsy listing content, describe:
- Its style/aesthetic (e.g., boho, minimalist, gothic)
- Its likely target audience
- The overall vibe, mood, and product type

Listing:
\"\"\"
{listing_text}
\"\"\"

Return the analysis in 3–5 short bullet points.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    return response["choices"][0]["message"]["content"]


def reimagine_listing(listing_text, new_style):
    prompt = f"""
You are a creative product designer with an eye for trends.

Take the following Etsy listing and reimagine it in a new style:
- Maintain the core idea, but shift the aesthetic
- Use the requested style to inspire the tone, look, and description
- Create a new title and 3-sentence product description

Listing:
\"\"\"
{listing_text}
\"\"\"

New Style: {new_style}

Respond with:
- New Title:
- New Description:
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.85,
    )

    return response["choices"][0]["message"]["content"]
