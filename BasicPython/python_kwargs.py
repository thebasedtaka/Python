#for key value pairs
def sum_of(**kwargs):
    sum = 0
    for _, v in kwargs.items():
        sum += v 
    return round(sum,2)

print(sum_of(coffee=2.99, cake=4.55, juice=2.53))