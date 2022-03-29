from book_class import Book


class Booklist():
	def __init__(self):
		"""Initialize the empty book list"""
		

	def add(self, title, author):
		"""Add a Book object with the given title and author to the book list"""
		book = Book(title, author)
		self.booklist.append(book)

	def count_books(self):
		"""Return the number of books currently in the booklist"""
		return len(self.book_list)
	

	def remove_title(self, title):
		"""Remove a book from the book list"""
		for book in self.book_list:
			if book.title == title:
				self.book_list.remove(book)

	def display_titles(self):
		"""Print out all titles currently in the book list"""
		for book in self.book_list:
			print(book.title)

	def is_empty(self):
		"""Return True if the book list is empty, False if not"""
		if self.book_list:
			return True
		else:
			return False
