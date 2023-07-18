import datetime

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
        self.borrower = None
        self.due_date = None

    def borrow(self, borrower, due_date):
        if self.available:
            self.available = False
            self.borrower = borrower
            self.due_date = due_date
            print(f"O livro '{self.title}' foi emprestado para {self.borrower} até {self.due_date}.")
        else:
            print(f"O livro '{self.title}' não está disponível no momento.")

    def return_book(self):
        if not self.available:
            self.available = True
            self.borrower = None
            self.due_date = None
            print(f"O livro '{self.title}' foi devolvido.")
        else:
            print(f"O livro '{self.title}' já está disponível.")

    def __str__(self):
        status = "Disponível" if self.available else f"Emprestado para {self.borrower} até {self.due_date}"
        return f"Título: {self.title}\nAutor: {self.author}\nISBN: {self.isbn}\nStatus: {status}\n"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"O livro '{book.title}' foi adicionado à biblioteca.")

    def find_books_by_title(self, title):
        found_books = []
        for book in self.books:
            if title.lower() in book.title.lower():
                found_books.append(book)
        return found_books

    def find_books_by_author(self, author):
        found_books = []
        for book in self.books:
            if author.lower() in book.author.lower():
                found_books.append(book)
        return found_books

    def display_books(self):
        if len(self.books) == 0:
            print("A biblioteca está vazia.")
        else:
            for book in self.books:
                print(book)

# Função principal do programa
def main():
    library = Library()

    while True:
        print("\n=== Sistema de Gerenciamento de Biblioteca ===")
        print("1. Adicionar Livro")
        print("2. Pesquisar Livros por Título")
        print("3. Pesquisar Livros por Autor")
        print("4. Mostrar Todos os Livros")
        print("5. Emprestar Livro")
        print("6. Devolver Livro")
        print("7. Sair")

        choice = input("Digite sua escolha (1-7): ")

        if choice == "1":
            title = input("Digite o título do livro: ")
            author = input("Digite o autor do livro: ")
            isbn = input("Digite o ISBN do livro: ")
            book = Book(title, author, isbn)
            library.add_book(book)
        elif choice == "2":
            search_title = input("Digite o título para pesquisar: ")
            found_books = library.find_books_by_title(search_title)
            if len(found_books) > 0:
                print("Livros encontrados:")
                for book in found_books:
                    print(book)
            else:
                print("Nenhum livro encontrado com o título especificado.")
        elif choice == "3":
            search_author = input("Digite o autor para pesquisar: ")
            found_books = library.find_books_by_author(search_author)
            if len(found_books) > 0:
                print("Livros encontrados:")
                for book in found_books:
                    print(book)
            else:
                print("Nenhum livro encontrado com o autor especificado.")
        elif choice == "4":
            library.display_books()
        elif choice == "5":
            title = input("Digite o título do livro para emprestar: ")
            borrower = input("Digite o nome do emprestador: ")
            due_date_str = input("Digite a data de devolução (formato: dd/mm/aaaa): ")
            due_date = datetime.datetime.strptime(due_date_str, "%d/%m/%Y")
            found_books = library.find_books_by_title(title)
            if len(found_books) > 0:
                book = found_books[0]
                book.borrow(borrower, due_date)
            else:
                print("Nenhum livro encontrado com o título especificado.")
        elif choice == "6":
            title = input("Digite o título do livro para devolver: ")
            found_books = library.find_books_by_title(title)
            if len(found_books) > 0:
                book = found_books[0]
                book.return_book()
            else:
                print("Nenhum livro encontrado com o título especificado.")
        elif choice == "7":
            break
        else:
            print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    main()
