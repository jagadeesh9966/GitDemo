'''itemsincart = 0
if itemsincart !=2:
    raise Exception("products cart count not matching")
if itemsincart !=2:
    pass
assert(itemsincart==2)
assert(itemsincart==0)'''

'''try:
    with open('filelog.txt','r') as reader:
        reader.read()
except:
    print("some how reached this block because there is failure in try block")
try:
    with open('filelog.txt','r')  as reader:
        reader.read()
except Exception as e:
    print(e)'''

try:
    with open('test.txt','r') as reader:
        reader.read()
except Exception as e:
    print(e)
finally:
    print("cleaning up resource")


