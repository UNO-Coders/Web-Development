from pipes import PIPE


string1 = "Hello"

#  METHOD 1

@PIPE
def add_string(prev, next):
    return f"{prev} {next}"

@PIPE
def count_chars(prev):
    return len(prev)

print(string1 | add_string("World") | add_string("!!!") | count_chars())

#  METHOD 2

def count_chars(prev):
    return len(prev)

print(string1 | PIPE(count_chars))