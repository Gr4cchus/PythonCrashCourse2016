import myprogram
print('\nimport module')
myprogram.display_message()

import myprogram as mn
print("\n import x as mp")
mn.display_message()

from myprogram import display_message
print('\n from x import function')
display_message()

from myprogram import display_message as fn
print('\n from x import function as fn')
fn()

from myprogram import *
display_message()
