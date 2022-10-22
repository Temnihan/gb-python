my_text = input('введи пример: ')
print(' eval = ',eval(my_text))
my_text = my_text.replace(' ','')
# exec(f'print({my_text})')
def addition(data):
    d = data.split('+')
    sum = mult(d[0])
    if len(d)<2:
        return sum
    for i in range(1,len(d)):
        tmp = mult(d[i])
        sum += tmp
    return sum

def minus(data):
    d = data.split('-')
    res = addition(d[0])
    if len(d)<2:
        return res
    for i in range(1,len(d)):
        tmp = addition(d[i])
        res -= tmp
    return res

def divide (data):
    d = data.split('/')
    if len(d)<2:
        return int(d[0])

    d = list(map(float,d))
    res = d[0]
    for i in range(1,len(d)):
        res /= d[i]
    return res

def mult(data):
    # mlp = 1
    d = data.split('*')
    result = divide(d[0])
    if len(d)<2:
        return  result
    for i in range(1,len(d)):
        tmp = divide(d[i])
        result *= tmp
    return result


print(minus(my_text))