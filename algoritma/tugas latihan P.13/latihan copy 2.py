print("\n")
print("Dictionary operations: Retrieve the value of a key")
capitals = {"Indonesia":"Jakarta", "Italy":"Rome", "Germany":"Berlin"}
print(capitals["Italy"]) 
print(capitals["Indonesia"])

squares = {1:1, 2:4, 3:9}
print(squares[2]) 
print(squares[1]) 
print(squares[3]) 
print("\n")

print("Dictionary operations:Get the value of a key")
capitals = {"Indonesia":"Jakarta", "Italy":"Rome", "Germany":"Berlin"}
print(capitals.get("Italy")) 
print(capitals.get("Indonesia")) 

squares = {1:1, 2:4, 3:9}
print(squares.get(1)) 
print(squares.get(3))
print(squares.get(4)) 
print(squares.get(4, "Not available!")) 
print("\n")