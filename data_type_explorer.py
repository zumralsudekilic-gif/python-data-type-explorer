print("=================================")
print("     PYTHON DATA TYPE EXPLORER")
print("=================================")

data = [25, 3.14, "Zümral", True]

print("\nData in the list:")
print(data)

index=int(input("\nEnter an index (0-3): "))

print("Selected value:", data[index])
print("Data type:", type(data[index]))
if type(data[index]) == int:
    print("This is an integer (int).")
elif type(data[index]) == float:
    print("This is a float.")
elif type(data[index]) == str:
    print("This is a string (str).")
elif type(data[index]) == bool:
    print("This is a boolean (bool).")

except IndexError:
    print("Error: Invalid index!")

except ValueError:
    print("Error: Please enter a number!")


