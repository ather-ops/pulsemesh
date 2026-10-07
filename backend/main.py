from fastapi import FastAPI
from pydantic import BaseModel
from backend.api_client import fetch_multiple, aggregate_results

app = FastAPI()
class URLRequest(BaseModel):
    urls: list[str]


@app.post("/analyze")
async def analyze(request: URLRequest):
   response = await fetch_multiple(request.urls)
   summary = aggregate_results(response)
   return summary
