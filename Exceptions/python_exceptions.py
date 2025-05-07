def divide_by(a, b):
    return a / b

try: 
    ans = divide_by(40,"w")
except ZeroDivisionError as e:
    print("You have sinned", exec)
    print(e.__class__)
except Exception as e:
    print(e, "Something went Wrong")