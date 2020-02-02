def two_fer(name="you"):
    #return "One for {}, and one for me".format(name)
    return f'One for {name} and one for me'


one=two_fer()
two=two_fer('Elise')

print(one,two)