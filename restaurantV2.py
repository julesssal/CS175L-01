#CS175L-01
#Julia Salerno
#restaurantV2

vegetarian = False
vegan = False
gluten_free = False
another_search = True

while another_search == True:
    response = str(input(" Is anyone in your party vegetarian? "))
    if response == "yes":
        vegetarian = True

    response = input(" Is anyone in your party vegan? ")
    if response == "yes":
        vegan = True

    response = input(" Is anyone in your party gluten free? ")
    if response == "yes":
        gluten_free = True

    print("Here are your restaurant choices:")
    if (not vegetarian) and (not vegan) and (not gluten_free):
        print("Joe's Gourmet Burgers")

    elif (not vegan) and (not gluten_free):
        print("Mama's Fine Italian")

    elif (not vegan):
        print("Main Street Pizza")
    print("Corner Cafe")
    print("Chef's Kitchen")

    res = str(input("Enter 'yes' if you would like to do another restaurant search (enter 'no' to end)"))
    if res =='yes':
        another_search = True
    else:
        another_search = False
