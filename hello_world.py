# 1. TASK: print "Hello World"
print( "Hello World" )
# 2. print "Hello Noelle!" with the name in a variable
name = "Bryce"
print( "Hello", name )	# with a comma
print( "Hello " + name )	# with a +
# 3. print "Hello 42!" with the number in a variable
num = 42
print( "Hello", num )	# with a comma
print( "Hello " + str(num) )	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print( "I love to eat {} and {}".format(fave_food1.title(), fave_food2.upper())) # with .format()
print( f"I love to eat {fave_food1} and {fave_food2}" ) # with an f string

if fave_food2.isalnum():
    print("fave_food2 variable is a string.")
    print( f"I love to eat {fave_food1} and {fave_food2}" ) # with an f string