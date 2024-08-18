ItemsInCart = 0
# Item will be added to cart
if ItemsInCart != 2:
    # raise Exception("Product card count not matching")
    pass

assert(ItemsInCart == 0)

try:
    with open('Filelog.txt', 'r') as reader:
        reader.read()
except:
    # customise failure message
    print("Some how I reached this block because there is failure in try block")

try:
    with open('Filelog.txt', 'r') as reader:
        reader.read()
except Exception as e:
    # Python specific failure message
    print(e)
finally:
    # write code to close/terminate/delete records in finally block
    print("cleaning the  records")

