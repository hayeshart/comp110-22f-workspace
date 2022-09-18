"""An example of a list utility algorithim."""

# Name: contains 
# Function with 2 parameters: 
# needle - what we're searching for 
# haystack - what we're searching through 
# Return type: bool
def contains(needle: str, haystack: list[str]) -> bool: 
    # Start from first index 
    i: int = 0
    # Loop through each index of list 
    while i < len(haystack):
        # Test if the item at this index is equal to needle 
        if haystack[i] == needle:
            #   Yes! Return true 
            return True
    i += 1
    # Return false
    return False
