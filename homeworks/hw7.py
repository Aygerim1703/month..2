import sqlite3


def create_table(conn):
    conn.execute('''CREATE TABLE IF NOT EXISTS books
                    (
                        id
                        INTEGER
                        PRIMARY
                        KEY
                        AUTOINCREMENT,
                        name
                        TEXT,
                        author
                        TEXT,
                        publication_year
                        INTEGER,
                        genre
                        TEXT,
                        number_of_pages
                        INTEGER,
                        number_of_copies
                        INTEGER
                    )''')
    conn.commit()


def insert_books(conn):
    books = [
        ("Война и мир", "Лев Толстой", 1869, "Роман", 1225, 5),
        ("Преступление и наказание", "Фёдор Достоевский", 1866, "Роман", 671, 3),
        ("Мастер и Маргарита", "Михаил Булгаков", 1967, "Роман", 470, 4),
        ("Отцы и дети", "Иван Тургенев", 1862, "Роман", 340, 2),
        ("Евгений Онегин", "Александр Пушкин", 1833, "Роман в стихах", 200, 6),
        ("Анна Каренина", "Лев Толстой", 1878, "Роман", 864, 3),
        ("Идиот", "Фёдор Достоевский", 1869, "Роман", 600, 2),
        ("Мёртвые души", "Николай Гоголь", 1842, "Поэма", 352, 5),
        ("Чайка", "Антон Чехов", 1896, "Пьеса", 150, 4),
        ("Белая гвардия", "Михаил Булгаков", 1925, "Роман", 320, 2),
    ]

    conn.executemany('''INSERT INTO books
                        (name, author, publication_year, genre, number_of_pages, number_of_copies)
                        VALUES (?, ?, ?, ?, ?, ?)''', books)
    conn.commit()


def delete_book(conn, book_name):
    conn.execute("DELETE FROM books WHERE name = ?", (book_name,))
    conn.commit()

if __name__ == "__main__":
    conn = sqlite3.connect('data.db')

    create_table(conn)
    insert_books(conn)
    delete_book(conn, "Чайка")

    conn.close()