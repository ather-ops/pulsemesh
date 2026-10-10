<p align="center"> <img src="https://raw.githubusercontent.com/ather-ops/pulsemesh/main/assets/pulsh%20ai%20cover.png" alt="Pulsh AI - Async Multi-API Intelligence Engine" width="100%"> </p> <h3 align="center">Async Multi-API Intelligence Engine</h3> <p align="center"> Send requests to many APIs at once and get one unified result. </p> <p align="center"> <b><a href="https://pulsh-mesh.streamlit.app/">Open the Live App</a></b> &nbsp;|&nbsp; <a href="https://pulse-ai-xkbk.onrender.com/docs">API Docs</a> </p>

## Overview

Pulsh AI is an asynchronous API intelligence engine built with Python. It calls multiple APIs concurrently, handles each request failure on its own, and combines everything into a single response.

A FastAPI backend does the work, and an interactive Streamlit dashboard shows the results.

---

## Features

- Concurrent API requests with asyncio and aiohttp
- Timeout and retry handling for each request
- Normalized responses with success status, HTTP status, data, and error details
- Unified results with total, successful, and failed request counts
- Interactive Streamlit dashboard
- REST API powered by FastAPI
- Backend hosted on Render, frontend on Streamlit Community Cloud

---

## Architecture

```mermaid
flowchart TD
    A[Streamlit Dashboard] -->|POST /analyze| B[FastAPI Backend]
    B --> C[Async API Engine]
    C --> D1[API 1]
    C --> D2[API 2]
    C --> D3[API N]
    D1 --> E[Result Aggregator]
    D2 --> E
    D3 --> E
    E --> F[Unified JSON Response]
    F --> A
```

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core language |
| FastAPI | Backend REST API |
| Uvicorn | ASGI server |
| asyncio + aiohttp | Concurrent HTTP requests |
| Pydantic | Request validation |
| Streamlit | Interactive frontend |
| Requests | Frontend-to-backend communication |
| Render | Backend hosting |

---

## Live Links

- **App:** [pulsh-mesh.streamlit.app](https://pulsh-mesh.streamlit.app/)
- **Backend:** [pulse-ai-xkbk.onrender.com](https://pulse-ai-xkbk.onrender.com)
- **Interactive API docs:** [/docs](https://pulse-ai-xkbk.onrender.com/docs)

---

## Error Handling

Pulsh AI is built to handle individual API failures, HTTP error responses, timeouts and retries, backend connection problems, and unexpected backend responses. Results depend on external API availability, network conditions, and hosting limits.

---

<p align="center"><b>Pulsh AI: Multiple APIs. One unified result.</b></p>
