from book_class import Book


class Booklist():
	def __init__(self):
		"""Initialize the empty book list"""
		self.books = []


	def add(self, title, author):
		"""Add a Book object with the given title and author to the book list"""
		book_1 = Book(title, author)
		self.books.append(book_1)


	def count_books(self):
		"""Return the number of books currently in the booklist"""
		return (len(self.books))

	def remove_title(self, title):
		"""Remove a book from the book list"""
		for book in self.books:
			if book.title == title:
				self.books.remove(book)
			else:
				print("the title does not exist")
	

	def display_titles(self):
		"""Print out all titles currently in the book list"""
		# titles = []
		for book in self.books:
			# titles.append(book.title)
			print(book.title)
			
	def is_empty(self):
		"""Return True if the book list is empty, False if not"""
		if not self.books:
  			print("List is empty")
		else:
			print("List is NOT empty")



nyt_bestsellers = Booklist()

nyt_bestsellers.add("Python for Dummies","Tyler Langham")
nyt_bestsellers.add("Random for Dummies","Random Langham")

print(nyt_bestsellers.books)
nyt_bestsellers.display_titles()

nyt_bestsellers.is_empty()


# titles = []
# for book in nyt_bestsellers.books:
# 	titles.append(book.title)
# print(titles)
