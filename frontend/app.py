import streamlit as st
import requests
import os

# Backend URL configuration
API_BASE_URL = os.getenv(
    "PULSEMESH_API_URL",
    "https://pulse-ai-xkbk.onrender.com"
).rstrip("/")

# Page configuration
st.set_page_config(
    page_title="Pulse ai",
    page_icon="⚡",
    layout="wide"
)

# App header
st.title("⚡ Pulse ai")
st.subheader("Async Multi-API Intelligence Engine")
st.write(
    "Analyze multiple APIs concurrently and get a unified result."
)

# User input
urls = st.text_area(
    "Enter API URLs",
    placeholder="Enter one URL per line..."
)

# Analyze button
if st.button("Analyze URLs"):
    if not urls.strip():
        st.warning("First enter your URLs!")

    else:
        url_list = urls.split()

        try:
            with st.spinner("Pulse is analyzing your apis..."):
                response = requests.post(
                    f"{API_BASE_URL}/analyze",
                    json={"urls": url_list},
                    timeout=30
                )

                response.raise_for_status()
                result = response.json()

            # Summary metrics
            col1, col2, col3 = st.columns(3)

            col1.metric("Total APIs", result["total"])
            col2.metric("Success", result["successful"])
            col3.metric("Failed", result["failed"])

            # Individual API results
            for index, item in enumerate(
                result["results"], start=1
            ):
                st.subheader(f"API: {index}")

                if item["success"]:
                    st.success(
                        f"Request Successful — Status: {item['status']}"
                    )
                    st.json(item["data"])

                else:
                    st.error(
                        f"Request Failed — Status: {item['status']}"
                    )
                    st.write(item["error"])

        except requests.exceptions.Timeout:
            st.error(
                "The PulseMesh backend took too long to respond. "
                "Please try again."
            )

        except requests.exceptions.ConnectionError:
            st.error(
                "Could not connect to the Pulse ai backend. "
                "Make sure FastAPI is running or the deployed backend "
                "URL is configured correctly."
            )

        except requests.exceptions.RequestException as e:
            st.error(f"HTTP request failed: {e}")

        except (ValueError, KeyError) as e:
            st.error(f"Invalid response received from the backend: {e}")
