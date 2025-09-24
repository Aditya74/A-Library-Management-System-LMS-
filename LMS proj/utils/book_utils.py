# from assets.data import LMS          
# def taking_book(student):
#     print("\nAvailable Books:")
#     for book, info in LMS.get("BOOKS", {}).items():
#         print(f"{book} - {info['count']} copies")
    
#     book_name = input("Enter book name to borrow: ")
#     if book_name in LMS["BOOKS"] and LMS["BOOKS"][book_name]["count"] > 0:
#         LMS["BOOKS"][book_name]["count"] -= 1
#         student.setdefault("books", []).append(book_name)
#         print(f"You borrowed '{book_name}' successfully!")
#     else:
#         print(f"Book '{book_name}' is not available.")

# def return_book(student):
#     if "books" not in student or not student["books"]:
#         print("You have no books to return.")
#         return

#     print("Your borrowed books:", student["books"])
#     book_name = input("Enter book name to return: ")
#     if book_name in student["books"]:
#         student["books"].remove(book_name)
#         LMS["BOOKS"][book_name]["count"] += 1
#         print(f"You returned '{book_name}' successfully!")
#     else:
#         print(f"You did not borrow '{book_name}'.")

# def view_books(student):
#     books = student.get("books", [])
#     if books:
#         print("Your borrowed books:", books)
#     else:
#         print("You have no borrowed books.")

