# Day 30 - Errors, Exceptions and JSON Data: Improving the Password

## Errors, Exceptions

* try:

Something that might cause an exception

* except:

Do this if there was an exception

* else:

Dothis if there were no exceptions 

* finally:

Do this no matter what happens

[day-30-end](https://replit.com/@appbrewery/day-30-end#main.py)

```python
#Exception Handling

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    raise TypeError("This is an error that I made up.")

#BMI Example

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)
```

[day-30-1-exercise](https://replit.com/@appbrewery/day-30-1-exercise)


[day-30-2-exercise](https://replit.com/@appbrewery/day-30-2-exercise)

## JSON Data

[JSON encoder and decoder](https://docs.python.org/3/library/json.html)


Write:

json.dump()

Read:

json.load()

Update:

json.update()


## Improving the Password