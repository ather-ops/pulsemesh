import streamlit as st
import requests
st.set_page_config(
    page_title="PulseMesh",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ PulseMesh")
st.subheader("Async Multi-API Intelligence Engine")

st.write(
    "Analyze multiple APIs concurrently and get a unified result."
)

urls = st.text_area(
    "Enter API URLs",
    placeholder="Enter one URL per line..."
)
if st.button("Analyze urls"):
    url = urls.split()
    if not urls.strip():
        st.warning("First enter your url!")
    else:
        try:
            with st.spinner("pulsh is thinking..."):
                response = requests.post(
                    "http://127.0.0.1:8000/analyze",
                    json = {"urls": url}
                )
                result = response.json()
                col1, col2, col3, = st.columns(3)
                col1.metric("Total APIs", result["total"])
                col2.metric("Success", result["successful"])
                col3.metric("Failed", result["failed"])

                for index,something in enumerate(result["results"],start=1):
                    st.subheader(f"API:{index}")
                    if something["success"]:
                        st.write({
                            "status":something["status"],
                            "data":something["data"]
                        })
                    else:
                        st.write({
                            "status":something["status"],
                            "error":something["error"]
                        })
        except Exception as e:
            st.error("Something went wrong please try again!")
