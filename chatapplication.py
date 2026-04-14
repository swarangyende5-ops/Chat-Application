import streamlit as st
import pandas as pd
import os
from datetime import datetime
import time

# File to store chat messages
CHAT_FILE = "chat_data.csv"

st.set_page_config(page_title="Chat App", layout="centered")

# ---------------- TITLE ----------------
st.title("💬 Streamlit Chat App")
st.write("Simple multi-user chat system")

# ---------------- USER LOGIN ----------------
username = st.text_input("Enter your username")

# ---------------- LOAD CHAT ----------------
def load_chat():
    if os.path.exists(CHAT_FILE):
        return pd.read_csv(CHAT_FILE)
    else:
        return pd.DataFrame(columns=["Time", "User", "Message"])

# ---------------- SAVE MESSAGE ----------------
def save_message(user, message):
    new_data = pd.DataFrame({
        "Time": [datetime.now().strftime("%H:%M:%S")],
        "User": [user],
        "Message": [message]
    })

    if os.path.exists(CHAT_FILE):
        old_data = pd.read_csv(CHAT_FILE)
        updated_data = pd.concat([old_data, new_data], ignore_index=True)
    else:
        updated_data = new_data

    updated_data.to_csv(CHAT_FILE, index=False)

# ---------------- INPUT MESSAGE ----------------
message = st.text_input("Type your message")

# ---------------- SEND BUTTON ----------------
if st.button("Send"):
    if username == "" or message == "":
        st.warning("Enter username and message")
    else:
        save_message(username, message)
        st.success("Message sent!")

# ---------------- DISPLAY CHAT ----------------
st.subheader("📨 Chat Messages")

chat_data = load_chat()

# Show latest messages first
if not chat_data.empty:
    chat_data = chat_data.iloc[::-1]

    for _, row in chat_data.iterrows():
        st.markdown(f"**{row['User']}** ({row['Time']}): {row['Message']}")
else:
    st.write("No messages yet...")

# ---------------- AUTO REFRESH ----------------
st.caption("🔄 Refreshing every 5 seconds...")

time.sleep(5)
st.rerun()