from time import sleep
import sys

'''
Ever wondered how to do the opposite behavior to "\n"?

Consider the ANSI escape codes:
    "\033[F" : move cursor to the beginning of the previous line
    "\033[A" : move cursor up one line
for more, see [Control Sequence Introducer commands](https://en.wikipedia.org/wiki/ANSI_escape_code#Control_Sequence_Introducer_commands)

In a terminal with short height, try num = 15
In a terminal with tall height, try num = 50
'''

num = 15
print("\n"*(num+3))
for ind in range(num):
    if ind < (num-1):
        sleep(5.0/num)
    sys.stdout.write("\033[F"*2)
    print("Printing in reverse" + "." * ind)
sys.stdout.write("\033[F"*4)