from sys import argv

script, filename = argv

print "We are going to erase %r." % filename
print "If you don't want that, hit CTRL-C(^C)."
print "If you do want that, hit RETURN"

raw_input('?')

print "Opening the file..."

target = open(filename, 'a')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you three lines."

line1= raw_input("line 1:")
line2= raw_input("line 2:")
line3= raw_input("line 3:")

print "I'm going to write these to the file."

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')










