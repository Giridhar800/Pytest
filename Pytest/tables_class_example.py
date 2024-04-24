# class program testing

class print_tables:
    def __init__(self,num):
        self.num = num
    
    def print_tables(self):
        f = open("output.txt",'w')
        for value in range(1,11):
            print(f"{self.num} X {value} = {self.num*value}", file=f)

if __name__ == "__main__":
    obj = print_tables(5)
    obj.print_tables()
