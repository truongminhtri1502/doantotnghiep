import streamlit as st
from streamlit.components.v1 import html
import time
from pyngrok import ngrok
import subprocess
import time
import requests
import os

st.title("ĐỒ ÁN TỐT NGHIỆP")

def start_node_red(node_red_dir=".node-red"):
    """
    Start Node-RED from the specified .node-red directory.
    Returns the subprocess.Popen object or None if it fails.
    """
    try:
        # Ensure Node-RED is installed
        subprocess.run(["node-red", "--version"], check=True, capture_output=True, text=True)
        # Start Node-RED with the user directory
        cmd = ["node-red", "--userDir", node_red_dir]
        node_red_process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd=os.path.expanduser(node_red_dir)  # Set working directory to .node-red
        )
        st.write(node_red_process)

        # Wait briefly to ensure Node-RED starts
        time.sleep(3)
        # Check if Node-RED is running by accessing its web interface
        response = requests.get("http://localhost:1880", timeout=5)
        if response.status_code == 200:
            st.success("Node-RED started successfully!")
            return node_red_process
        else:
            st.error("Node-RED failed to start.")
            return None
    except FileNotFoundError:
        st.error("Node-RED is not installed. Install it with 'npm install -g node-red'.")
        return None
    except subprocess.CalledProcessError as e:
        st.error(f"Error checking Node-RED: {e.stderr}")
        return None
    except requests.RequestException as e:
        st.error(f"Failed to connect to Node-RED: {e}")
        return None
    
node_red_process = start_node_red()


global public_url
def run():
    ngrok.set_auth_token("2zsz2SxGP86gxDTO8ZXeD49UFiE_3Qt4k3LttMs9HyRJENKcg")  # Replace with your token
    ngrok_tunnel = ngrok.connect(addr="1880", proto="http", bind_tls=True)
    public_url = ngrok_tunnel.public_url + "/ui"
    st.write(f"Streamlit app is running at: {public_url}")
    #time.sleep̣̣̣̣(5)

    #iframe_code = f"""
    #<iframe src="{public_url}" width="100%" height="1280px" style="border:none;"></iframe>
    #"""
    #html(iframe_code, height=600)

def stop(public_url):
    ngrok.disconnect(public_url)
    ngrok.kill()

st.button("Chạy server", on_click=run, key="start")
##st.button("Dừng server", on_click=stop(public_url=""), key="stop")



