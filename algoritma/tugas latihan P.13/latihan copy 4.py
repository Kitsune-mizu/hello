print("\n")
print("Dictionary operations: Length, update multiple key-value pairs, get all keys, and clear ")
capitals = {"Indonesia":"Jakarta", "Italy":"Rome"}
print(len(capitals)) 

y = {"Germany":"Berlin", "France":"Paris"}
capitals.update(y)
print(capitals) 

capitals_keys = list(capitals.keys())
print(capitals_keys) 

capitals.clear()
print(capitals) 
print("\n")
