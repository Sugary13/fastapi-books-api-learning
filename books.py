from fastapi import FastAPI, Body, HTTPException

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'},
]

@app.get("/books/mybook")
async def read_all_books():
    return {'books': BOOKS}

@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book_title.casefold() == book.get('title', "").casefold():
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.get("/books/")
async def read_category_by_query(category: str):
    books_by_query = []
    for book in BOOKS:
        if category.casefold() == book.get('category', "").casefold():
            books_by_query.append(book)
    if not books_by_query:
        raise HTTPException(status_code=404, detail="Book not found")
    return {'books': books_by_query}

@app.get("/books/byauthor/")
async def read_book_by_author(author: str):
    books_by_author = []
    for book in BOOKS:
        if author.casefold() == book.get("author", "").casefold():
            books_by_author.append(book)
    if not books_by_author:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"books": books_by_author}


@app.get("/books/by_author_and_category/")
async def read_author_category_by_query(author: str, category: str):
    books_by_author = []
    for book in BOOKS:
        if author.casefold() == book.get('author', "").casefold() and \
            category.casefold() == book.get('category', "").casefold():
            books_by_author.append(book)

    return {'books': books_by_author}

@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
    return {"message": "Book created"}

@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i, book in enumerate(BOOKS):
        if BOOKS[i].get("title").casefold() == updated_book.get('title', "").casefold():
            BOOKS[i] = updated_book
            return {"message": "Book updated"}

    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i, book in enumerate(BOOKS):
        if BOOKS[i].get("title", "").casefold() == book_title.casefold():
            BOOKS.pop(i)
            return {"message": "Book deleted"}

    raise HTTPException(status_code=404, detail="Book not found")





