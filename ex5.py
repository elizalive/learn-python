name = 'Elizabeth C. Scheltens'
age = 28
feet = 5
inches_1 = feet * 12
inches_2 = 4
height_us = inches_1 + inches_2 # total inches
height_uk = height_us * 2.54 # centimeters
weight_us = 135 # lbs
weight_uk = weight_us * 0.453592 # kilograms
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "She's %d inches tall." % height_us
print "For all you Brits, that's %f centimeters." % height_uk
print "She's %d pounds, or %f kilograms, heavy." % (weight_us, weight_uk) 
print "Actually that's not too heavy."
print "She's got %s eyes and %s hair." % (eyes, hair)
print "Her teeth are usually %s depending on the coffee" % teeth

# THer line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height_us, weight_us, age + height_us + weight_us)