# 1- save a product info added from a user
def addProduct(name, price):
    with open("products.txt", "a", encoding="utf-8") as file:
        file.write(f"name: {name}, price: {price}\n")


#addProduct("samsung s10", 3000)
#addProduct("samsung s11", 3500)

# 2- find and change
def find_and_change(file_name, old_word, new_word):
    with open(file_name, "r+", encoding="utf-8") as file:
        text = file.read()
        new_text = text.replace(old_word, new_word)
        file.seek(0)
        file.write(new_text)
        file.truncate()

find_and_change("products.txt", "samsung", "iphone")




    




