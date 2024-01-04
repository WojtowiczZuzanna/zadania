from ebook import eBook

ebook1 = eBook("The Fellowship of the Ring", "J.J.R Tolkien", 15, 151)
ebook2 = eBook("Two Tower", "J.J.R Tolkien", 34, 453)

ebook1.open()
ebook1.status()
ebook1.read()
ebook1.status()
ebook1.close()
ebook1.status()

print( "\n")

ebook2.open()
ebook2.status()
ebook2.read()
ebook2.status()
ebook2.close()
ebook2.status()
