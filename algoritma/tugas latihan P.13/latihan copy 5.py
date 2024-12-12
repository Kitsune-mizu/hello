print("\n")
print("Dictionary iterations ")
capitals = {"Indonesia":"Jakarta", "Italy":"Rome", "Germany":"Berlin"}
for country in capitals:
  print(country, "has capital" , capitals[country])
print("\n")

capitals = {"Indonesia":"Jakarta", "Italy":"Rome", "Germany":"Berlin"}
for country, capital in capitals.items():
  print(country, "has capital" , capital)
print("\n")

print("Dictionary iterations ")
x = {}
for i in range(1, 4):
  x[i] = i**3
print(x)
print("\n")
