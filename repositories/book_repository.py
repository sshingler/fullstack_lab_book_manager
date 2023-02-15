from db.run_sql import run_sql
from models.author import Author 
from models.book import Book 
import repositories.author_repository as author_repository 

def delete_all():
    sql = "DELETE  FROM books"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def save(book):
    sql = "INSERT INTO books (title, genre, publisher, author_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [book.title, book.genre, book.publisher, book.author.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book  

def select(id):
    book = None
    sql = "SELECT * FROM books WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result=results[0]
        author = author_repository.select(result['author_id'])
        book = Book(result['title'], result['genre'], result['publisher'], author, result ['id'])
    return book 
    
def select_all():
    books = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = author_repository.select(row['author_id'])
        book = Book(row['title'], row['genre'], row['publisher'], author, row ['id'])
        books.append(book)
    return books

