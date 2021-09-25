# Day 19 - Intermediate - Instances, State and Higher Order Functions

[turtle.listen](https://docs.python.org/3/library/turtle.html#turtle.listen)

## Higher Order Functions

可以跟其他Function一起工作的Function，被稱為高階Function

```
def add(n1, n2):
    return n1 + n2

def subract(n1, n2):
    return n1 - n2
    
def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2    

# Higher Order Functions
def calculator(2, 3, func):
    return func(2, 3)

result = calculator(2, 3, add)
print(result)
```