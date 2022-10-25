# #question 25 example
# def f(a,b):
#     print(f"x,y are {x},{y}")
#     print(f"a,b are {a},{b}")
#     a=4
#     return 2*b
    
# x=2
# y=3
# y=f(12,5)
# print(f"y is {y}")


# def f(x,y):
#     # print(f"x: {x}, y: {y}")
#     print("inside the function")
#     print(f"x: {x} @{id(x)}, y: {y} @{id(y)}")
#     x = 5
#     # print(f"x: {x}, y: {y}")
#     print(f"x: {x} @{id(x)}, y: {y} @{id(y)} \n")
#     return 2*y

# x = 4
# y = 12
# print("\noutside the function, prior to function call")
# print(f"x: {x} @{id(x)}, y: {y} @{id(y)} \n")
# y = f(y,x)
# # print(f"x: {x}, y: {y}")
# print("outside the function, after the function ends")
# print(f"x: {x} @{id(x)}, y: {y} @{id(y)}")



# li = []

# li.append( int("42") )
# li.append( len(li) )
# li.append( type("42") )
# li.append( sorted([1,0,0,2]) )
# li.append( print("Hello World") )

# for i in li:
#     print(f"{i} of type {type(i)}")


def file_tester(file_in):
    open_file = open(file_in,'r')
    for line in open_file:
        print(line)
    open_file.close()

file_tester('words.txt')