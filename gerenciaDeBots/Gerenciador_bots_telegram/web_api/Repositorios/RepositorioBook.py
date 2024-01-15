from Gerenciador_bots_telegram.web_api.models import Book
from datetime import date



new_book = Book(title="Example Book", author="Author Name", published_date=date.today())
new_book.save()
