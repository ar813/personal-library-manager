import os
import streamlit as st
from pymongo import MongoClient # pip install pymongo
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    st.error("❌ MONGO_URI not found. Please set it in your .env file.")
    st.stop()

# Connect to MongoDB
try:
    client = MongoClient(MONGO_URI)
    db = client["PersonalLibrary"]
    books_collection = db["books"]
except Exception as e:
    st.error(f"❌ MongoDB Connection Error: {e}")
    st.stop()

# Sidebar with styling
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2232/2232688.png", width=100)
st.sidebar.title("📚 Library Menu")
st.sidebar.markdown("---")
menu = ["🏠 Home", "📕 Add Book", "❌ Remove Book", "🔍 Search Book", "📚 Display All Books", "📊 Library Statistics"]
choice = st.sidebar.radio("Navigate", menu)
st.sidebar.markdown("---")
st.sidebar.write("📌 *Manage your personal book collection easily!* ✨")

if choice == "🏠 Home":
    st.title("📚 Welcome to Your Personal Library Manager!")
    st.markdown(
        """
        ### 📖 About This Application
        - Easily manage your personal book collection.
        - Add, remove, search, and track books you’ve read.
        - Get insightful library statistics.
        - Keep your book collection organized and accessible.
        
        🚀 *Start managing your library today!*
        """
    )

if choice == "📕 Add Book":
    st.subheader("📕 Add a Book")
    book_title = st.text_input("📕 Book Title").strip().lower()
    book_author = st.text_input("👨‍💼 Author").strip().lower()
    publication_year = st.number_input("📅 Publication Year", min_value=1000, max_value=9999)
    genre = st.text_input("🏷️ Genre").strip().lower()
    is_read = st.checkbox("📖 Have you read it?")
    
    if st.button("Add Book"):
        if book_title and book_author and publication_year and genre:
            book_data = {
                "title": book_title,
                "author": book_author,
                "publication_year": publication_year,
                "genre": genre,
                "is_read": is_read,
            }
            books_collection.insert_one(book_data)
            st.success(f"✅ Book '{book_title}' added successfully!")
        else:
            st.warning("⚠️ Please fill all fields.")

elif choice == "❌ Remove Book":
    st.subheader("❌ Remove a Book")
    book_title = st.text_input("❌ Enter the book title to remove").strip().lower()
    if st.button("Remove Book"):
        result = books_collection.delete_one({"title": book_title})
        if result.deleted_count > 0:
            st.success(f"✅ Book '{book_title}' removed successfully!")
        else:
            st.warning(f"⚠️ Book '{book_title}' not found.")

elif choice == "🔍 Search Book":
    st.subheader("🔍 Search for a Book")
    search_by = st.radio("Search by", ["Title", "Author"])
    search_query = st.text_input(f"Enter the {search_by.lower()}").strip().lower()
    
    if st.button("Search"):
        if search_by == "Title":
            book = books_collection.find_one({"title": search_query})
            if book:
                st.markdown(f"""
                **📌 Title:** {book['title'].capitalize()}  
                **👨‍💼 Author:** {book['author'].capitalize()}  
                **📅 Year:** {book['publication_year']}  
                **🏷️ Genre:** {book['genre'].capitalize()}  
                **📗 Status:** {"Read" if book['is_read'] else "Not Read"}
            """)
            else:
                st.warning(f"⚠️ Book '{search_query}' not found.")
        else:
            books = list(books_collection.find({"author": search_query}))
            if books:
                for book in books:
                    st.markdown(f"""
                    **📌 Title:** {book['title'].capitalize()}  
                    **👨‍💼 Author:** {book['author'].capitalize()}  
                    **📅 Year:** {book['publication_year']}  
                    **🏷️ Genre:** {book['genre'].capitalize()}  
                    **📗 Status:** {"Read" if book['is_read'] else "Not Read"}
                """)
            else:
                st.warning(f"⚠️ No books found by '{search_query}'.")

elif choice == "📚 Display All Books":
    st.subheader("📚 Your Library")
    books = list(books_collection.find())
    if books:
        for book in books:
            st.markdown(f"""
                **📌 Title:** {book['title'].capitalize()}  
                **👨‍💼 Author:** {book['author'].capitalize()}  
                **📅 Year:** {book['publication_year']}  
                **🏷️ Genre:** {book['genre'].capitalize()}  
                **📗 Status:** {"Read" if book['is_read'] else "Not Read"}
            """)
    else:
        st.warning("📭 Your library is empty.")

elif choice == "📊 Library Statistics":
    total_books = books_collection.count_documents({})
    if total_books == 0:
        st.warning("📭 No books in your library yet!")
    else:
        read_books = books_collection.count_documents({"is_read": True})
        unread_books = total_books - read_books
        read_percentage = (read_books / total_books) * 100
        unread_percentage = (unread_books / total_books) * 100
        
        st.markdown(f"""
            ### 📊 Library Statistics  
            - **📚 Total Books:** {total_books}  
            - **✅ Read Books:** {read_books}  
            - **📕 Unread Books:** {unread_books}  
            - **📖 Read Percentage:** {read_percentage:.2f}%  
            - **📕 Unread Percentage:** {unread_percentage:.2f}%  
            """)
