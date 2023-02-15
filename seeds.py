from models.author import Author
from models.book import Book 

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

author_repository.delete_all()
book_repository.delete_all()

author_1 = Author ("Donald", "Duck")
author_repository.save(author_1)
author_2 = Author ("Mickey", "Mouse")
author_repository.save(author_2)


book_1 = Book("For the love of Ducks", "Biography", "Disney", author_1)
book_repository.save(book_1)
book_2 = Book("A mouse's tale", "Biography", "Disney", author_2)
book_repository.save(book_2)


