class Publication:
	def __init__(self, name: str) -> None:
		self._name = name
	
	def print_info(self):
		print(f"Name: {self._name}")

class Book(Publication):
	def __init__(self, name: str, writer: str, pages_amount: int) -> None:
		Publication.__init__(self, name)
		self._writer = writer
		self._pages_amount = pages_amount
	
	def print_info(self):
		super().print_info()
		print(f"Writer: {self._writer}")
		print(f"Pages: {self._pages_amount}")

class Magazine(Publication):
	def __init__(self, name: str, publisher: str) -> None:
		Publication.__init__(self, name)
		self._publisher = publisher
	
	def print_info(self):
		super().print_info()
		print(f"Publisher: {self._publisher}")

def main():
	magazine = Magazine("Aku Ankka", "Aki Hyyppä")
	book = Book("Hytti n:o 6", "Rosa Liksom", 200)

	magazine.print_info()
	book.print_info()

main()