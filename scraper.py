import sys
import requests
from bs4 import BeautifulSoup
import ollama
import urllib.parse
from datetime import datetime
import os

def extract_text_from_url(url):
    print(f"Fetching URL: {url}")
    try:
        # Some sites use strict anti-bot protections (like Cloudflare) that still block `requests`.
        # `cloudscraper` mimics a real browser environment more thoroughly to bypass these.
        import cloudscraper
        scraper = cloudscraper.create_scraper(browser={
            'browser': 'chrome',
            'platform': 'windows',
            'desktop': True
        })
        response = scraper.get(url, timeout=15)
        response.raise_for_status()
    except Exception as e:
        print(f"Error fetching URL: {e}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Remove script and style elements
    for script_or_style in soup(['script', 'style']):
        script_or_style.decompose()
        
    text = soup.get_text(separator=' ', strip=True)
    return text

def ask_ollama(context, question, model="phi3:mini"):
    print(f"Asking Ollama (Model: {model})...")
    
    # We ask the LLM specifically to write readable markdown
    prompt = f"""Context information is below.
---------------------
{context[:4000]}
---------------------
Given the context information, answer the following question: {question}

Please format your response as a well-structured, highly readable Markdown document. Use headings, bullet points, bold text, and clear formatting where appropriate to make it easy to understand for anyone."""
    
    try:
        response = ollama.chat(model=model, messages=[
            {
                'role': 'user',
                'content': prompt
            }
        ])
        return response['message']['content']
    except Exception as e:
        print(f"Error communicating with Ollama: {e}")
        return None

def save_to_markdown(url, question, answer, model_name):
    # Create a nice filename based on the domain and timestamp
    domain = urllib.parse.urlparse(url).netloc.replace("www.", "")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"report_{domain}_{timestamp}.md"
    
    # Clean up filename for any weird characters
    filename = "".join([c for c in filename if c.isalpha() or c.isdigit() or c in ('.', '_', '-')]).rstrip()
    
    content = f"""# Scraping Report

**Source URL:** [{url}]({url})
**Question:** {question}
**Model Used:** `{model_name}`
**Date:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

---

{answer}
"""
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"\n✅ Successfully saved a readable report to: {os.path.abspath(filename)}")
    except Exception as e:
        print(f"\n❌ Error saving to file: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python scraper.py <URL> <Question> [model_name]")
        print("Example: python scraper.py https://en.wikipedia.org/wiki/Web_scraping \"What is web scraping?\" phi3:mini")
        sys.exit(1)
        
    target_url = sys.argv[1]
    user_question = sys.argv[2]
    model_name = sys.argv[3] if len(sys.argv) > 3 else "phi3:mini"
    
    page_text = extract_text_from_url(target_url)
    if not page_text:
        sys.exit(1)
        
    print(f"Extracted {len(page_text)} characters of text.")
    
    answer = ask_ollama(page_text, user_question, model=model_name)
    if answer:
        print("\n--- Answer Preview ---")
        print(answer)
        print("----------------------")
        save_to_markdown(target_url, user_question, answer, model_name)
