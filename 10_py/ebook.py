class eBook():
    def __init__(self, title, author, number_of_pages, current_pg_nb, is_open = False):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages #number of read pages
        self.current_pg_nb = current_pg_nb
        self.is_open = is_open

    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False

    def status(self):
        if self.is_open == True:
            print(f"Title: {self.title}, Author: {self.author}, Current page: {self.current_pg_nb}, Pages read: {self.number_of_pages}")
        else:
            print("Error")
        
    def read(self):
        if self.is_open == True:
            self.current_pg_nb += self.number_of_pages
            print(self.current_pg_nb)