# Book CRUD API (Flask)

Simple CRUD API for `Book` with fields: `id`, `book_name`, `author`, `publisher`.

Run locally:

```powershell
python -m pip install -r requirements.txt
python app.py
```

Endpoints:
- `GET /books` — list all books
- `POST /books` — create book (JSON: `book_name`, `author`, `publisher`)
- `GET /books/<id>` — get book
- `PUT /books/<id>` — update book (JSON: `book_name`, `author`, `publisher`)
- `DELETE /books/<id>` — delete book

Example create:

```powershell
# PowerShell (recommended)
Invoke-RestMethod -Uri 'http://127.0.0.1:5000/books' -Method Post `
	-Body (@{book_name='1984'; author='George Orwell'; publisher='Secker & Warburg'} | ConvertTo-Json) `
	-ContentType 'application/json'
```

```powershell
# Using curl.exe with a payload file (works from PowerShell)
@'
{"book_name":"1984","author":"George Orwell","publisher":"Secker & Warburg"}
'@ > payload.json
& curl.exe -X POST "http://127.0.0.1:5000/books" -H "Content-Type: application/json" --data-binary "@payload.json"
```
