# Base Media class - parent class for all library items
class Media:
    def __init__(self, title, id_number, publication_year):
        self._title = title  # Protected attribute
        self._id_number = id_number  # Protected attribute
        self._publication_year = publication_year
        self._checked_out = False
        self._due_date = None
    
    @property
    def title(self):
        return self._title
    
    @property
    def id_number(self):
        return self._id_number
    
    @property
    def is_checked_out(self):
        return self._checked_out
    
    def check_out(self, due_date):
        if not self._checked_out:
            self._checked_out = True
            self._due_date = due_date
            return True
        return False
    
    def return_item(self):
        if self._checked_out:
            self._checked_out = False
            self._due_date = None
            return True
        return False
    
    def get_info(self):
        status = "Checked Out" if self._checked_out else "Available"
        info = f"Title: {self._title}, ID: {self._id_number}, Status: {status}"
        if self._checked_out:
            info += f", Due: {self._due_date}"
        return info


# Book class inherits from Media
class Book(Media):
    def __init__(self, title, id_number, publication_year, author, pages):
        # Call parent constructor
        super().__init__(title, id_number, publication_year)
        self.author = author
        self.pages = pages
    
    def get_info(self):
        basic_info = super().get_info()
        return f"{basic_info}, Author: {self.author}, Pages: {self.pages}"


# DVD class inherits from Media
class DVD(Media):
    def __init__(self, title, id_number, publication_year, director, runtime):
        super().__init__(title, id_number, publication_year)
        self.director = director
        self.runtime = runtime  # in minutes
    
    def get_info(self):
        basic_info = super().get_info()
        return f"{basic_info}, Director: {self.director}, Runtime: {self.runtime} min"


# AudioBook class - demonstrates multiple inheritance
class AudioBook(Book):
    def __init__(self, title, id_number, publication_year, author, narrator, length):
        super().__init__(title, id_number, publication_year, author, 0)  # No physical pages
        self.narrator = narrator
        self.length = length  # in minutes
    
    def get_info(self):
        # Using parent method but replacing some info
        basic_info = Media.get_info(self)  # Skip Book's get_info
        return f"{basic_info}, Author: {self.author}, Narrator: {self.narrator}, Length: {self.length} min"


# Example usage
if __name__ == "__main__":
    # Create instances of different media types
    book = Book("The Great Gatsby", "B12345", 1925, "F. Scott Fitzgerald", 180)
    dvd = DVD("Inception", "D98765", 2010, "Christopher Nolan", 148)
    audiobook = AudioBook("Dune", "A45678", 1965, "Frank Herbert", "Simon Vance", 840)
    
    # Test methods
    print(book.get_info())
    book.check_out("2025-05-01")
    print(book.get_info())
    
    print("\n" + dvd.get_info())
    
    print("\n" + audiobook.get_info())
    audiobook.check_out("2025-04-30")
    print(audiobook.get_info())
    audiobook.return_item()
    print(audiobook.get_info())