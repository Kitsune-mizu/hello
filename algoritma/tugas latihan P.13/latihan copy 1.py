print("\n")
print("Creating dictionaries")
capitals = {"Indonesia":"Jakarta", "Italy":"Rome", "Germany":"Berlin"}
squares = {1:1, 2:4, 3:9}
print(squares) 
print(type(squares)) 
randoms = {1:"Bob", "17":False, "Blue":"Red"}
empty_dictionary = {}
print(type(empty_dictionary)) 
print("\n")

print("Creating dictionaries")
tuple_of_tuples = (
    ("Indonesia", "Jakarta"),
    ("Italy", "Rome"),
    ("Germany", "Berlin")
)
capitals = dict(tuple_of_tuples)
print(capitals)
print(randoms)

list_of_tuples = [
    ("Indonesia", "Jakarta"),
    ("Italy", "Rome"),
    ("Germany", "Berlin")
]
capitals = dict(list_of_tuples)
print(capitals) 
print(randoms)
print("\n")
