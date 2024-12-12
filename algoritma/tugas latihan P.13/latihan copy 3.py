print("\n")
print("Dictionary operations: Add & delete key-value pair, and check existence of key")
capitals = {"Indonesia":"Jakarta", "Italy":"Rome"}
capitals["Japan"] = "Tokyo"
print(capitals) 

capitals["Indonesia"] = "Penajam Paser Utara"
print(capitals) 

del capitals["Italy"]
print(capitals)

print("Indonesia" in capitals)
print("France" in capitals) 
print("\n")