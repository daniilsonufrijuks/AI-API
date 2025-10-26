import os
from pathlib import Path
import requests
from dotenv import load_dotenv
import json

# .env
env_path = Path(__file__).resolve().parents[1] / '.env'
load_dotenv(dotenv_path=env_path)

API_KEY = os.getenv('HUGGINGFACE_API_KEY')

# Izmantojam standarto API
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

headers = {"Authorization": f"Bearer {API_KEY}"}

# Teksts summārizācijai
TEXT = "The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (416 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct."

payload = {
    "inputs": TEXT,
    "parameters": {
        "max_length": 130,
        "min_length": 30,
        "do_sample": False
    }
}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()

def main():
    result = query(payload)
    # Summārizācijas modeļi atgriež atbildi ar 'summary_text'
    if isinstance(result, list) and result and 'summary_text' in result[0]:
        print("--- Modeļa kopsavilkums ---")
        print(result[0]['summary_text'].strip())
    elif isinstance(result, dict) and 'summary_text' in result:
        print("--- Modeļa kopsavilkums ---")
        print(result['summary_text'].strip())
    else:
        print("Nezināma atbildes forma:")
        print(json.dumps(result, indent=2, ensure_ascii=False))
        


if __name__ == '__main__':
    main()