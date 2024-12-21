import random  # impoting random module for generating random values
import string # importing string module for predefined character sets

def generate_key():  # definingfunction to generate eandom key
    # now have to create a pool of valid characters
    pool = string.ascii_letters + string.digits

    # randomly selecting 20 characters from the pool and joining them into string
    return ''.join(random.choices(pool,k=20))

# printing 20-chr random key
print(generate_key())