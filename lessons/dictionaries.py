"""Demonstrations of dictionary capabilities."""


# Declaring the type of a dictionary 
schools: dict[str, int]

# Initializing to an empty dictionary 
schools = dict()

# Set a key-value pairing in the dictionary 
schools["UNC"] = 19400
schools ["Duke"] = 6717
schools["NCSU"] = 26150

# Print a dictionary literal representation 
print(schools)

# Access avalue by its key -- "lookup" 
print(f"UNC has {schools['UNC']} students.")

# Remove a key-value pair from a dictionary
# by its key 
schools.pop("Duke")

# Test for existance of a key 
if "Duke" in schools: 
    print("Found the key 'Duke' in schools")
else: 
    print("No key 'Duke' in schools")

    # Update / Reassign a key-value pair 
    schools["UNC"] = 20000
    schools["NCSU"] += 200

print(schools)

# Demonstration of dictionary literals

#Empty dictionary literal
schools = {} # Same as dict()
print(schools)

#Alternatively, initialize key-values pairs 
schools = {
    "UNC": 19400,
    "Dukie": 6717,
    "NCSU": 26150
}
print(schools)

#What happens when a key does not exist 
# print(schools["UNCC"])

# Example looping over keys of a dict 
for key in schools: 
    print(f"Key: {key} -> Value: {schools[schools]}")