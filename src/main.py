'''
A mega greeting module.
'''

from sam.greeting.greeter import Greeter as SamGreeter

greeter_list = [
    SamGreeter('Sam')
]

def main():
    for greeter in greeter_list:
        greeter.greet()


if __name__ == '__main__':
    main()