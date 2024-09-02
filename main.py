from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os
import json

# Initialize OpenAI API with your API key
openai.api_key = os.getenv("OPENAI_API_KEY")  # Load this from environment variables or set it directly.

app = FastAPI()

# Pydantic model for the state coverage request
class StateCoverageRequest(BaseModel):
    carriers: list

# Function to call the OpenAI Chat API to generate US state coverage data for carriers
def get_us_state_coverage(carriers):
    prompt = f"""Generate coverage data for the following carriers across US states: {', '.join(carriers)}.
    For each carrier and state, provide a coverage score between 0 and 1.
    
    Return the data as a JSON string with this structure:
    {{
        "UPS": {{"Alabama": 0.85, "Alaska": 0.72, ...}},
        "FedEx": {{"Alabama": 0.88, "Alaska": 0.75, ...}},
        ...
    }}
    """

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates realistic shipping carrier data."},
            {"role": "user", "content": prompt}
        ]
    )

    return json.loads(response.choices[0].message.content)

@app.post("/state-coverage-comparison/")
async def state_coverage_comparison(request: StateCoverageRequest):
    # Call the function to get the US state coverage data
    coverage_data = get_us_state_coverage(request.carriers)
    
    # Return the response data
    return coverage_data

@app.get("/")
def read_root():
    return {"message": "Welcome to the State Coverage Comparison API!"}
