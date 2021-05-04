# part 1
class Computer:
    def __init__(self, name, processor, ram, mfrYear):
        self.name = name
        self.processor = processor
        self.ram = ram  # gigabytes
        self.mfrYear = mfrYear

    def getAge(self):
        return f"{2021-self.mfrYear} year old"


myPc = Computer("myPc", "ryzen 5600", 16, 2020)
print(myPc.getAge())

# part 2
l = [5, 7, 77, 2, 5, 6, 7, 8, 50, 10, 1, 30, 54]


def squareList(l):
    result = []
    for item in l:
        result.append(item**2)
    return result


print(squareList(l))


# part 3
class inventory:
    def __init__(self, name, address, stock):
        self.name = name
        self.address = address
        self.stock = stock

    def addStock(self, item):
        self.stock.append(item)


class book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


stocklist = [
    book("Crying in H Mart", "Michelle Zauner", 22.95),
    book("Greenlights", "Matthew McConaughey", 23.99),
    book("On the House: A Washington Memoir", "John Boehner", 23.99),
    book(
        "The Code Breaker: Jennifer Doudna, Gene Editing, and the Future of the Human Race",
        "Walter Isaacson", 27.99),
    book("Think Again: The Power of Knowing What You Don't Know", "Adam Grant",
         21.99)
]

storeInventory = inventory("Barnes & Noble", "www.barnesandnoble.com",
                           stocklist)
