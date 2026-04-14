# 💬 Streamlit Chat App

## 📌 Overview

The **Streamlit Chat App** is a simple multi-user messaging application built using **Python and Streamlit**.
It allows users to send messages, view chat history, and interact with others in real time using a shared CSV file as storage.

---

## 🚀 Features

* ✅ Multi-user chat system
* ✅ Username-based messaging
* ✅ Real-time message display (auto-refresh every 5 seconds)
* ✅ Stores chat history in a CSV file
* ✅ Displays latest messages first
* ✅ Simple and clean user interface

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* OS module
* Datetime module

---

## 📂 Project Structure

```id="9m3a1k"
project_folder/
│
├── app.py            # Main Streamlit chat application
├── chat_data.csv     # Stores chat messages (auto-created)
└── README.md         # Project documentation
```

---

## ⚙️ Installation & Setup

### 1. Install Required Libraries

Run the following command:

```id="jv7r2c"
pip install streamlit pandas
```

---

### 2. Run the Application

Navigate to the project folder and run:

```id="8nq6rx"
streamlit run app.py
```

---

### 3. Open in Browser

The app will automatically open at:

```id="d6y3lp"
http://localhost:8501
```

---

## 🔧 How It Works

### 🔹 User Login

* Users enter a username before sending messages
* Messages are tagged with the username

---

### 🔹 Sending Messages

* Users type a message and click the **Send** button
* The message is saved along with:

  * Username
  * Timestamp

---

### 🔹 Data Storage

* Messages are stored in a CSV file (`chat_data.csv`)
* If the file exists, new messages are appended
* Otherwise, a new file is created automatically

---

### 🔹 Display Chat

* All messages are displayed on the screen
* Latest messages appear at the top
* Each message shows:

  * Username
  * Time
  * Message

---

### 🔹 Auto Refresh

* The app refreshes every **5 seconds**
* Ensures near real-time chat updates

---

## 📊 Example Output

```
User1 (12:30:10): Hello!
User2 (12:30:15): Hi there!
```

---

## ⚠️ Limitations

* Not a real-time server (uses file storage)
* No authentication system
* Not suitable for large-scale applications
* Possible delay due to refresh interval

---

## 🔥 Future Improvements

* Add user authentication (login/signup)
* Use database (SQLite / Firebase) instead of CSV
* Add emojis and media sharing
* Improve UI with chat bubbles
* Deploy online for global access

---

## 👨‍💻 Author

**Swarang Yende**
