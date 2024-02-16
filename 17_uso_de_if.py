#or si uno de los dos es verdad entonces es verdad
#and ambos tienen que ser verdad para ser verdad
#not() cambia de True a False y viceversa

is_male = False
is_tall = True
if is_male and is_tall:
    print("Eres un hombre alto")
elif is_male and not(is_tall):
    print("Eres hombre pero no alto")
elif not(is_male) and is_tall:
    print("No eres hombre pero si alto")
else:
    print("No eres un hombre y no eres alto")