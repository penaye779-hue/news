import django
import os

# --- Setup Django environment ---
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# --- Step 1: Populate sample data if empty ---
if Author.objects.count() == 0:
    print("No data found. Populating sample data...")
    
    # Authors
    author1 = Author.objects.create(name="J.K. Rowling")
    author2 = Author.objects.create(name="George R.R. Martin")

    # Books
    book1 = Book.objects.create(title="Harry Potter and the Sorcerer's Stone", author=author1)
    book2 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", author=author1)
    book3 = Book.objects.create(title="A Game of Thrones", author=author2)

    # Libraries
    library1 = Library.objects.create(name="Central Library")
    library2 = Library.objects.create(name="Community Library")

    # ManyToMany relationships
    library1.books.add(book1, book3)
    library2.books.add(book2)

    # Librarians (OneToOne)
    librarian1 = Librarian.objects.create(name="Alice", library=library1)
    librarian2 = Librarian.objects.create(name="Bob", library=library2)
    
    print("Sample data populated.\n")
else:
    print("Existing data found. Running queries...\n")

# --- Step 2: Queries ---

# 1️⃣ Query all books by a specific author
author_name = "J.K. Rowling"
try:
    author = Author.objects.get(name=author_name)
    print(f"Books by {author.name}:")
    for book in author.books.all():
        print(f"- {book.title}")
except Author.DoesNotExist:
    print(f"No author found with name '{author_name}'")

# 2️⃣ List all books in a library
library_name = "Central Library"
try:
    library = Library.objects.get(name=library_name)
    print(f"\nBooks in {library.name}:")
    for book in library.books.all():
        print(f"- {book.title}")
except Library.DoesNotExist:
    print(f"No library found with name '{library_name}'")

# 3️⃣ Retrieve the librarian for a library
try:
    librarian = library.librarian
    print(f"\nLibrarian of {library.name}: {librarian.name}")
except Librarian.DoesNotExist:
    print(f"No librarian assigned to {library.name}")
