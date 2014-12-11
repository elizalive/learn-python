# Sets variable x equal to the string 'There are (%d) types of people.'
# Looks for integer decimal with which to replace %d
# Replaces %d with 10
x = "There are %d types of people." % 10

# Sets the variable binary equal to the string 'binary'
binary = "binary"

# Sets the variable do_not equal to the string 'don't'
do_not = "don't"

# Sets variable y equal to the string 'Those who know (%s) and those who (%s).'
# Looks for strings with which to replace both instances of (%s)
# Replaces the first instance of %s with the variable binary
# replaces the second instance of %s with the variable do_not
y = "Those who know %s and those who %s." % (binary, do_not)

# Sets variable x equal to the string 'There are (%d) types of people.'
# Looks for integer decimal with which to replace %d
# Replaces %d with 10
# Displays text 'There are 10 types of people.'
print x

# Sets variable y equal to the string 'Those who know (%s) and those who (%s).'
# Looks for strings with which to replace both instances of (%s)
# Replaces the first instance of %s with the variable binary
# Replaces the second instance of %s with the variable do_not
# Displays text 'Those who know binary and those who don't.'
print y

# Sets variable x equal to the string 'There are (%d) types of people.'
# Looks for integer decimal with which to replace %d
# Replaces %d with 10
# Looks for string with which to replace %r
# Replaces %r with string 'There are 10 types of people.'
# Displays text 'I said: There are 10 types of people.'
print "I said: %r." % x

# Sets variable y equal to the string 'Those who know (%s) and those who (%s).'
# Looks for strings with which to replace both instances of (%s)
# Replaces the first instance of %s with the variable binary
# Replaces the second instance of %s with the variable do_not
# Looks for string with which to replace 
print "I also said: '%s'." % y

# Sets variable hilarious equal to Boolean False
hilarious = False

# Sets variable joke_evaluation equal to string 'Isn't that joke so funny! (%r)'
joke_evaluation = "Isn't that joke so funny?! %r"

# replaces joke_evaluation variable with string 'Isn't that joke so funny?! (%r)'
# Looks for string with which to replace %r
# Replaces %r with the value of the variable hilarious ('False')
# Displays text 'Isn't that joke so funny?! False'
print joke_evaluation % hilarious

# Sets variable w equal to the string 'This is the left side of...'
w = "This is the left side of..."

# Sets variable e equal to the string 'a string with a right side.'
e = "a string with a right side."

# Replaces variable w with string 'This is the left side of...'
# Replaces variable e with string 'a string with a right side.'
# Displays text 'This is the left side of...''a string with a right side.'
print w + e