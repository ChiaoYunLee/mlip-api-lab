import json
import os
from typing import Any, Dict
from litellm import completion

# You can replace these with other models as needed but this is the one we suggest for this lab.
MODEL = "groq/llama-3.3-70b-versatile"

api_key = os.getenv("GROQ_API_KEY")

def get_itinerary(destination: str) -> Dict[str, Any]:
    """
    Returns a JSON-like dict with keys:
      - destination
      - price_range
      - ideal_visit_times
      - top_attractions
    """
    # implement litellm call here to generate a structured travel itinerary for the given destination

    # See https://docs.litellm.ai/docs/ for reference.

    data = completion(model = MODEL,
                      api_key = api_key,
                      response_format={ "type": "json_object" },
                      messages = 
                      [{
                          "content":f"""Generate a structured travel itinerary in JSON format for the destination: {destination}, with only the 
                                    following 4 keys: destination, price_range, ideal_visit_times, and top_attractions.""",
                          "role":"user"
                      }])
    return json.loads(data.choices[0].message.content) # type: dictionary
