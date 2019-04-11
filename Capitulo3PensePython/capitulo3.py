print(type(42))
print(int('32'))
print(int('Hello'))
print(int(3.99999))
print(int(-2.3))
print(float(32))
print(float('3.14159'))
print(str(32))
print(str(3.14159))
import math
math
<module 'math' (built-in)>
ratio = signal_power / noise_power
decibels = 10 * math.log10(ratio)
radians = 0.7
height = math.sin(radians)
degrees = 45
radians = degrees / 180.0 * math.pi
print(math.sin(radians))
print(math.sqrt(2) / 2.0)
x = math.sin(degrees / 360.0 * 2 * math.pi)
x = math.exp(math.log(x+1))
minutes = hours * 60 
hours * 60 = minutes  # errado
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")
def print_lyrics(): 
	print("I'm a lumberjack, and I'm okay.")
print(print_lyrics)
print(type(print_lyrics))
print_lyrics()
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
repeat_lyrics()
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
repeat_lyrics()
def print_twice(bruce):
    print(bruce)
    print(bruce)
print_twice('Spam')
print_twice(42)
print_twice(math.pi)
print_twice('Spam '*4)
print_twice(math.cos(math.pi))
michael = 'Eric, the half a bee.'
print_twice(michael)
def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)
line1 = 'Bing tiddle '
line2 = 'tiddle bang.'
cat_twice(line1, line2)
print(cat)
Traceback (innermost last):
  File "test.py", line 13, in __main__
    cat_twice(line1, line2)
  File "test.py", line 5, in cat_twice
    print_twice(cat)
  File "test.py", line 9, in print_twice
    print(cat)
x = math.cos(radians)
golden = (math.sqrt(5) + 1) / 2
math.sqrt(5)
result = print_twice('Bing')
print(result)
print(type(None))


