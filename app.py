import streamlit as st
from streamlit.components.v1 import html
import time
from pyngrok import ngrok

ngrok.set_auth_token("2zsz2SxGP86gxDTO8ZXeD49UFiE_3Qt4k3LttMs9HyRJENKcg")  # Replace with your token
ngrok_tunnel = ngrok.connect(addr="1880", proto="http", bind_tls=True)
public_url = ngrok_tunnel.public_url
print(f"Streamlit app is running at: {public_url}")

iframe_code = f"""
<iframe src="{public_url}" width="100%" height="1280px" style="border:none;"></iframe>
"""
html(iframe_code, height=600)



