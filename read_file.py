import os 

os.system('cls')
# r => read r+ => read and write
# w => write w+ => write and read
# a = append a+ => append and read
try :
    mode = input('enter a (r , r+ , w, w+, a, a+) : ')
    if mode not in ['a','a+','w','w+','r','r+']:
        raise ValueError('mode not is correct')
except ValueError as z:
    print(z)

path = rf"test.txt"

try :
    with open(file=path,mode=mode,encoding="utf-8") as file:
        if mode in ['r','r+']:
            b = file.read()
            file.seek(0)
            print(b)
            if mode == 'r+':
                file.write('123')
                file.seek(0)
                print(file.read())
        else :
            text = input('enter a text: ')
            file.write(text)
            file.seek(0)
            if mode == 'w+' or 'a+':
                print(file.read())
except Exception as z:
    print(z)

print('my name is mohammad')

