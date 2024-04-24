# output : 7th table 7 X 1,  7 X 10, 10values, fun call generator
# functional program [with functions, without classes]

def print_tables(num):
    for value in range(1,11):
        yield f"{num} X {value} = {num*value}" # generator object


if __name__ == "__main__":
    output = print_tables(7)
    print(output)