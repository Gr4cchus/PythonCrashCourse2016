from collections import OrderedDict

programming_words = OrderedDict()

programming_words['dictionary'] = 'is a collection of key-value pairs.'
programming_words['conditional test'] = 'is an expression that can be evaluated as true or false.'
programming_words['loop'] = 'works through an object interactively'
programming_words['something'] = 'blah blah blah'

for key, value in programming_words.items():
    print(key + ":", value)
# print("Dictionary" + ":", programming_words['dictionary'],
#       "\nConditional test:", programming_words['conditional test'],
#       "\nLoop:", programming_words['loop'])
