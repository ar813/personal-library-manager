# Personal Library Manager

## 📖 Overview

The **Personal Library Manager** is a Streamlit-based web application that helps users manage their personal book collection. Users can add, remove, search, and track books they've read. It also provides insightful statistics about the library.

## 🚀 Features

- 📕 **Add Books** to your personal collection.
- ❌ **Remove Books** from your library.
- 🔍 **Search Books** by title or author.
- 📚 **Display All Books** in your collection.
- 📊 **View Library Statistics**, including read and unread books.

## 🛠️ Setting Up the Application

### 1️⃣ Create Required Files

Before running the application, create the following files:

- `library_manager.py` (This is where you write your application code.)
- `.env` (To store environment variables securely.)
- `requirements.txt` (To list the dependencies needed for the project.)

### 2️⃣ In `requirements.txt` file, we need this

```
streamlit
pymongo
python-dotenv
```

To install dependencies manually, run:

```sh
pip install streamlit pymongo python-dotenv
```

### 3️⃣ Set Up Environment Variables

Create a `.env` file and add your MongoDB connection string:

```
MONGO_URI = "your_mongodb_connection_string"
```

### 4️⃣ Run the Application

```sh
streamlit run library_manager.py
```

## 🗄️ Connecting to MongoDB

The application uses **MongoDB** to store book data. Follow these steps to set up MongoDB:

### Use MongoDB Atlas (Recommended):

1. **Create an Account & Cluster**

   - Sign up at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas/register).
   - Create a **free cluster** by following the setup wizard.

2. **Set Up Database Access**

   - Navigate to **Database Access** in the MongoDB Atlas dashboard.
   - Click **Add New Database User** and create a user with a **password**.
   - Set user roles to **Read and Write to Any Database**.

3. **Configure Network Access**

   - Go to **Network Access** and click **Add IP Address**.
   - Select **Allow Access from Anywhere** (`0.0.0.0/0`).

4. **Get Your Connection String**

   - Go to your cluster and click **Connect**.
   - Choose **Connect Your Application**.
   - Copy the **MongoDB connection string** and replace `<password>` with your created user’s password.
   - Update the `.env` file with this string.

## 🖥️ Deployment to Streamlit Cloud

### 1️⃣ Push Code to GitHub

### 2️⃣ Deploy on Streamlit Cloud

- Go to [Streamlit Cloud](https://share.streamlit.io/)
- Click **New App**
- Select your **GitHub repository**
- Set the **branch** and **main script** (`library_manager.py`)
- Add **secrets**:
  ```
  MONGO_URI = "your_mongodb_connection_string"
  ```
- Click **Deploy**

## 🔧 Troubleshooting

### ❌ `ModuleNotFoundError: No module named 'pymongo'`

Install missing dependency:

```sh
pip install pymongo
```

### ❌ `ServerSelectionTimeoutError`

- Ensure MongoDB is running.
- If using MongoDB Atlas, **whitelist your IP** (`0.0.0.0/0`).
- Verify **MONGO\_URI** in `.env`.

---

✨ Happy Reading! 📚

