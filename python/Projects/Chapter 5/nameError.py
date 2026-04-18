s = spam()
s.here()

class spam():
    def here(self):
        print("yes" * 10)
       
# define the class and function before using it to not trigger the NameError