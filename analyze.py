import json
import os
from typing import Any, Dict
from litellm import completion

# You can replace these with other models as needed but this is the one we suggest for this lab.
MODEL = "groq/llama-3.3-70b-versatile"

api_key = os.getenv("GROQ_API_KEY")
schema = {
  "name": "itinerary_schema",
  "schema": {
      "type": "object",
      "properties": {
          "destination": {"type": "string"},
          "price_range": {"type": "string"},
          "ideal_visit_times": {"type": "array",
                                "items": {"type": "string"}},
          "top_attractions": {"type": "array",
                              "items": {"type": "string"}},
      },  
      "required": ["destination", "price_range", "ideal_visit_times", "top_attractions"],
}}

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
                      response_format={ "type": "json_schema", "json_schema": schema, "strict": True},
                      messages = 
                      [{
                          "content":f"""Generate a structured travel itinerary in JSON format for the destination: {destination}""",
                          "role":"user"
                      }])
    return json.loads(data.choices[0].message.content) # type: dictionary
