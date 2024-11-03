from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(_name_)
api = Api(app)

# Contoh data buku untuk keperluan pengujian
books = [
    {"id": 1, "title": "Belajar Python", "author": "John Doe", "year": 2021},
    {"id": 2, "title": "Pemrograman Web dengan Flask", "author": "Jane Smith", "year": 2022},
    {"id": 3, "title": "Data Science untuk Pemula", "author": "Michael Brown", "year": 2020},
    {"id": 4, "title": "Machine Learning Praktis", "author": "Lisa White", "year": 2023},
    {"id": 5, "title": "Pengenalan AI", "author": "Andrew Clark", "year": 2021},
    {"id": 6, "title": "Pemrograman dengan Java", "author": "Sarah Lee", "year": 2019},
    {"id": 7, "title": "Dasar-Dasar C++", "author": "Robert Wilson", "year": 2018},
    {"id": 8, "title": "Jaringan Komputer", "author": "Emily Davis", "year": 2020},
    {"id": 9, "title": "Basis Data Relasional", "author": "Chris Thompson", "year": 2021},
    {"id": 10, "title": "Pemrograman Android", "author": "Anna Scott", "year": 2019},
    {"id": 11, "title": "Algoritma dan Struktur Data", "author": "David Turner", "year": 2022},
    {"id": 12, "title": "Pemrograman Web Lanjutan", "author": "Kevin Ramirez", "year": 2021},
    {"id": 13, "title": "Cybersecurity Dasar", "author": "Sophia Martin", "year": 2023},
    {"id": 14, "title": "Cloud Computing", "author": "James Green", "year": 2022},
    {"id": 15, "title": "Pemrograman Python untuk Data Science", "author": "Laura Lopez", "year": 2023}
]

class BookList(Resource):
    def get(self):
        return {
            "error": False,
            "message": "success",
            "count": len(books),
            "books": books
        }

    def post(self):
        data = request.get_json()
        new_book = {
            "id": len(books) + 1,
            "title": data["title"],
            "author": data["author"],
            "year": data["year"]
        }
        books.append(new_book)
        return {"error": False, "message": "Book added successfully", "book": new_book}, 201

class BookDetail(Resource):
    def get(self, book_id):
        book = next((bk for bk in books if bk["id"] == book_id), None)
        if book:
            return {"error": False, "message": "success", "book": book}
        return {"error": True, "message": "Book not found"}, 404

    def put(self, book_id):
        data = request.get_json()
        book = next((bk for bk in books if bk["id"] == book_id), None)
        if book:
            book.update(data)
            return {"error": False, "message": "Book updated successfully", "book": book}
        return {"error": True, "message": "Book not found"}, 404

    def delete(self, book_id):
        global books
        books = [bk for bk in books if bk["id"] != book_id]
        return {"error": False, "message": "Book deleted successfully"}, 200

# Tambahkan resources ke API
api.add_resource(BookList, '/books')
api.add_resource(BookDetail, '/books/<int:book_id>')

if _name_ == "_main_":
    app.run(debug=True)
