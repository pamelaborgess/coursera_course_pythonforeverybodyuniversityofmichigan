#exemplo 1
def thing():
    print('hello')
    
print('there')

#exemplo 2
def func(x):
    print(x)
    
func(10)
func(20)

#exemplo 3
def stuff():
    print('hello')
    return
    print('world')
    
stuff()

#exemplo 4
def greet(lang):
    if lang == 'es':
        return 'hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'hello'

print(greet('fr'), 'Michael')

#exemplo 5
def addtwo(a,b):
    added = a + b
    return a

x = addtwo(2,7)
print(x)
