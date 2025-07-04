a = input().strip()

# Extract the last four characters and state code
pl = a[-4:]  # Last 4 characters of the input
s = a[:2]    # First 2 characters of the input (state code)

# Dictionary to map state codes
d = {"TN": "Tamilnadu", "KA": "Karnataka", "KL": "Kerala"}

# Print the corresponding state
if s in d:
    print(d[s])

# Check if the last 4 digits are "Fancy"
if pl == pl[0] * 4:  # All four digits are the same (e.g., 7777)
    print("Fancy")
elif pl in ["1234", "2345", "3456", "4567", "5678", "6789", "7890", "9876", "8765", "7654", "6543", "5432", "4321"]:
    print("Fancy")  # Consecutive increasing or decreasing numbers

elif pl[1] == pl[2] == pl[3]:  # Last 3 digits are the same
    print("Fancy")
else:
    print("Not Fancy")
