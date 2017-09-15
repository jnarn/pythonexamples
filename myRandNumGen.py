#Example of using modules. https://docs.python.org/2/library/random.html
#Import statement to call a module. It should available in the path or working directory.
import random
print(random.__file__) #checking the referred module file here
print('Random result: ' + str(random.randint(1,6))) #printing a random number between 1 to 6
