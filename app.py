import streamlit as st
from streamlit.components.v1 import html

# URL of the service running on another port
other_service_url = "http://localhost:1880/ui"

# Embed the content using an iframe
iframe_code = f"""
<iframe src="{other_service_url}" width="100%" height="1280px" style="border:none;"></iframe>
"""
html(iframe_code, height=600)