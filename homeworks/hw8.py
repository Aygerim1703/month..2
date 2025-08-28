import sqlite3

def create_tables(conn):

    conn.execute('''CREATE TABLE IF NOT EXISTS genres(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )''')


    conn.execute('''CREATE TABLE IF NOT EXISTS books(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        author TEXT NOT NULL,
        publication_year INTEGER,
        number_of_pages INTEGER,
        number_of_copies INTEGER,
        genre_id INTEGER,
        FOREIGN KEY (genre_id) REFERENCES genres(id)
    )''')

    conn.commit()

def insert_genres(conn):
    genres = [
        ("Роман",),
        ("Поэма",),
        ("Пьеса",),
        ("Фантастика",)
    ]
    conn.executemany("INSERT INTO genres (name) VALUES (?)", genres)
    conn.commit()

def insert_books(conn):
    books = [
        ("Война и мир", "Лев Толстой", 1869, 1225, 5, 1),
        ("Преступление и наказание", "Фёдор Достоевский", 1866, 671, 3, 1),
        ("Мастер и Маргарита", "Михаил Булгаков", 1967, 470, 4, 1),
        ("Евгений Онегин", "Александр Пушкин", 1833, 200, 6, 2),
        ("Мёртвые души", "Николай Гоголь", 1842, 352, 5, 2),
        ("Чайка", "Антон Чехов", 1896, 150, 4, 3),
        ("Белая гвардия", "Михаил Булгаков", 1925, 320, 2, 1),
        ("Пикник на обочине", "Стругацкие", 1972, 250, 3, 4),
    ]
    conn.executemany('''INSERT INTO books
        (name, author, publication_year, number_of_pages, number_of_copies, genre_id)
        VALUES (?, ?, ?, ?, ?, ?)''', books)
    conn.commit()

def get_books_with_genres(conn):
    cursor = conn.execute('''
        SELECT books.name, books.author, books.publication_year,
               genres.name AS genre, books.number_of_pages, books.number_of_copies
        FROM books
        JOIN genres ON books.genre_id = genres.id
    ''')
    rows = cursor.fetchall()


    print(f"{'Название книги':30} | {'Автор':20} | {'Год':6} | {'Жанр':12} | {'Страниц':8} | {'Копий':6}")
    print("-" * 95)


    for row in rows:
        name, author, year, genre, pages, copies = row
        print(f"{name[:30]:30} | {author[:20]:20} | {year:<6} | {genre[:12]:12} | {pages:<8} | {copies:<6}")

def export_books_to_txt(conn, filename="books.txt"):
    cursor = conn.execute('''
        SELECT books.name, books.author, books.publication_year,
               genres.name AS genre, books.number_of_pages, books.number_of_copies
        FROM books
        JOIN genres ON books.genre_id = genres.id
    ''')
    rows = cursor.fetchall()

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"{'Название книги':30} | {'Автор':20} | {'Год':6} | {'Жанр':12} | {'Страниц':8} | {'Копий':6}\n")
        f.write("-" * 95 + "\n")
        for row in rows:
            name, author, year, genre, pages, copies = row
            f.write(f"{name[:30]:30} | {author[:20]:20} | {year:<6} | {genre[:12]:12} | {pages:<8} | {copies:<6}\n")

    print(f"Данные успешно сохранены в {filename}")

if __name__ == "__main__":
    conn = sqlite3.connect("data.db")


    conn.execute("DROP TABLE IF EXISTS books")
    conn.execute("DROP TABLE IF EXISTS genres")

    create_tables(conn)
    insert_genres(conn)
    insert_books(conn)

    print("Книги с жанрами:")
    get_books_with_genres(conn)

    export_books_to_txt(conn)

    conn.close()