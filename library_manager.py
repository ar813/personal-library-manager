import json # Import JSON module to work with JSON files
import os # Import OS module to check if file exists

file = "library.json" # Define the filename for storing library data

# Check if the library file exists
if os.path.exists(file):
    try:
        # Try to open the file and load the existing data
        with open(file, "r") as f:
            library = json.load(f)
    except json.JSONDecodeError:
        # If file is empty or has an error, start with an empty list
        library = []
else:
    # If file doesn't exist, initialize an empty list
    library = []

print("\nWelcome to your Personal Library Manager!")

# Infinite loop to keep the program running until user exits
while True:
    # Display menu options
    print("\n1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")

    # Get user input and handle invalid input
    try:
        user_choice = int(input("\nEnter your choice: "))
    except ValueError:
        print("\nInvalid input. Please enter a number between 1 and 6.")
        continue

    if user_choice == 1:
        # Adding a new book
        book_title = input("\nEnter the title of the book: ").lower().strip()
        book_author = input("Enter the author of the book: ").lower().strip()
        
        # Get publication year and handle invalid input
        try:
            publication_year = int(input("Enter the publication year: "))
        except ValueError:
            print("\nInvalid year. Please enter a numeric value.")
            continue
        
        genre = input("Enter the genre: ").lower().strip()
        is_read = input("Have you read this book? (yes/no): ").strip().lower() == "yes"

        # Store book details in a dictionary and add it to the list
        library.append({
            "title": book_title,
            "author": book_author,
            "publication_year": publication_year,
            "genre": genre,
            "is_read": is_read
        })
        
        # Save updated library data to file
        with open(file, "w") as f:
            json.dump(library, f, indent=4)

        print(f"\nBook '{book_title}' added successfully!") 

    elif user_choice == 2:
        # Removing a book
        book_title = input("Enter the title of the book to remove: ").lower()
        
        found = False
        for book in library:
            if book["title"] == book_title:
                library.remove(book)
                print(f"\nBook '{book_title}' removed successfully!")
                
                # Save the updated library data after removal
                with open(file, "w") as f:
                    json.dump(library, f, indent=4)
                found = True
                break
        if not found:
            print(f"\nBook '{book_title}' not found in your library.")
            
    elif user_choice == 3:
        # Searching for a book
        print("\nSearch by:")
        print("1. Title")
        print("2. Author")
        
        # Get search choice and handle invalid input
        try:
            search_choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("\nInvalid input. Please enter 1 or 2.")
            continue
        
        if search_choice == 1:
            # Search by title
            book_title = input("Enter the title of the book: ").lower()
            for search in library:
                if search["title"] == book_title:
                    print(f"\nBook found: {search['title'].capitalize()} by {search['author'].capitalize()} ({search['publication_year']}) - {search['genre']} - {'Read' if search['is_read'] == True else 'Not Read'}")
                    break
            else:
                print(f"\nBook '{book_title}' not found in your library.")
        
        elif search_choice == 2:
            # Search by author
            book_author = input("Enter the author of the book: ").lower()
            
            found = False
            for search in library:
                if search["author"] == book_author:
                    print(f"\nBook found: {search['title'].capitalize()} by {search['author'].capitalize()} ({search['publication_year']}) - {search['genre']} - {'Read' if search['is_read'] == True else 'Not Read'}")
                    found = True
                    break
            if not found:
                print(f"\nAuthor '{book_author}' not found in your library.")
                
    elif user_choice == 4:
        # Displaying all books
        if not library:
            print("\nYour library is empty.")
        else:
            print("\nYour Library:")
            for index, book in enumerate(library, start=1):
                print(f"{index}. {book['title'].capitalize()} by {book['author'].capitalize()} ({book['publication_year']}) - {book['genre']} - {'Read' if book['is_read'] == True else 'Not Read'}")

    elif user_choice == 5:
        # Displaying library statistics
        total_books = len(library)
        if total_books == 0:
            print("\nNo books in your library yet!")
            continue
        
        read_books = 0
        for checking_is_read in library:
            if checking_is_read['is_read'] == True:
                read_books += 1
                
        unread_books = total_books - read_books
        read_percentage = (read_books / total_books) * 100
        unread_percentage = (unread_books / total_books) * 100
        
        # Displaying statistics
        print(f"\nLibrary Statistics:")
        print(f"Total books: {total_books}")
        print(f"Books read: {read_books}")
        print(f"Books not read: {unread_books}")
        print(f"\nPercentage of books read: {read_percentage:.2f}%")
        print(f"Percentage of books not read: {unread_percentage:.2f}%")
        
    elif user_choice == 6:
        # Exit program and save library to file
        print("\nLibrary saved to file. Goodbye!")
        with open(file, "w") as f:
            json.dump(library, f, indent=4)
        break
            
    else:
        # Handle invalid menu selection
        print("\nInvalid input. Please enter a number between 1 and 6.")
        