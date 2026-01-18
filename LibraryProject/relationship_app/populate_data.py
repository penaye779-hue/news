# relationship_app/populate_data.py
import django, os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Create authors, books, libraries, librarians only if they don't exist
author1, created = Author.objects.get_or_create(name="J.K. Rowling")
author2, created = Author.objects.get_or_create(name="George R.R. Martin")

book1, created = Book.objects.get_or_create(title="Harry Potter and the Sorcerer's Stone", author=author1)
book2, created = Book.objects.get_or_create(title="Harry Potter and the Chamber of Secrets", author=author1)
book3, created = Book.objects.get_or_create(title="A Game of Thrones", author=author2)

library1, created = Library.objects.get_or_create(name="Central Library")
library2, created = Library.objects.get_or_create(name="Community Library")

library1.books.add(book1, book3)
library2.books.add(book2)

librarian1, created = Librarian.objects.get_or_create(name="Alice", library=library1)
librarian2, created = Librarian.objects.get_or_create(name="Bob", library=library2)

print("Sample data populated successfully!")
