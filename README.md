# PulseMesh

### Async Multi-API Intelligence Engine

Analyze multiple APIs concurrently and get a unified result.

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?logo=streamlit)](https://streamlit.io/)

## Overview

PulseMesh is an asynchronous API intelligence engine built with Python. It sends requests to multiple APIs concurrently, handles individual request failures, and aggregates the results into a unified response.

The project combines a FastAPI backend with an interactive Streamlit frontend.

## Features

- Concurrent API requests using asyncio and aiohttp.
- Timeout and retry handling for individual API requests.
- Normalized responses containing success status, HTTP status, data, and error details.
- Unified result aggregation with total, successful, and failed request counts.
- Interactive dashboard built with Streamlit.
- REST API powered by FastAPI.
- Cloud-hosted backend deployed on Render.

## Architecture

```text
Streamlit Frontend
        |
        | HTTP POST /analyze
        v
FastAPI Backend
        |
        v
Asynchronous API Engine
        |
        +---- API 1
        +---- API 2
        +---- API 3
        +---- API N
        |
        v
Result Aggregator
        |
        v
Unified JSON Response
        |
        v
Streamlit Dashboard
```

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| FastAPI | Backend REST API |
| Uvicorn | ASGI server |
| asyncio | Asynchronous execution |
| aiohttp | Asynchronous HTTP requests |
| Streamlit | Interactive frontend |
| Requests | Frontend-to-backend HTTP communication |
| Pydantic | Request validation |
| Render | Backend hosting |

## Live Backend

**Base URL:** https://pulse-ai-xkbk.onrender.com

- [FastAPI interactive documentation](https://pulse-ai-xkbk.onrender.com/docs)
- [OpenAPI schema](https://pulse-ai-xkbk.onrender.com/openapi.json)

The backend is deployed on Render. The Streamlit frontend must also be deployed and connected before the complete application is publicly accessible through a single app URL.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/pulsemesh.git
cd pulsemesh
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows using Git Bash:

```bash
source .venv/Scripts/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

## Run Locally

### Start the FastAPI backend

Open the first terminal in the project root:

```bash
uvicorn backend.main:app --reload
```

API documentation:

http://127.0.0.1:8000/docs

### Start the Streamlit frontend

Open a second terminal in the project root:

```bash
streamlit run frontend/app.py
```

Open the application:

http://localhost:8501

Both services must be running during local development.

## API Usage

### Endpoint

```http
POST /analyze
Content-Type: application/json
```

### Example request

```json
{
  "urls": [
    "https://jsonplaceholder.typicode.com/todos/1",
    "https://httpbin.org/status/404"
  ]
}
```

### Response structure

```json
{
  "total": 2,
  "successful": 1,
  "failed": 1,
  "results": [
    {
      "success": true,
      "status": 200,
      "data": {
        "userId": 1,
        "id": 1,
        "title": "delectus aut autem",
        "completed": false
      },
      "error": null
    },
    {
      "success": false,
      "status": 404,
      "data": null,
      "error": "HTTP request failed"
    }
  ]
}
```

This is an illustrative response. Actual results depend on the external APIs and network conditions.

## Deployment

### Backend on Render

The FastAPI backend is deployed on Render.

Start command:

```bash
uvicorn backend.main:app --host 0.0.0.0 --port $PORT
```

### Frontend on Streamlit Community Cloud

Configure the following environment variable in the deployed Streamlit app's settings:

```text
PULSEMESH_API_URL=https://pulse-ai-xkbk.onrender.com
```

The frontend uses this value to send requests to the hosted backend.

## Error Handling

PulseMesh is designed to handle:

- Individual API request failures.
- HTTP error responses.
- Request timeouts and retries.
- Backend connection failures.
- Unexpected backend responses.

External API availability, network conditions, and hosting limits may affect results.


**PulseMesh — Multiple APIs. One unified result.**
