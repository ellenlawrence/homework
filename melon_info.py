"""Print out all the melons in our inventory."""


from melons import melons


def print_melon(melons):
    """Print each melon with corresponding attribute information."""


    for name, attributes in melons.items():
        print(name.upper())
        
        for attribute, value in attributes.items():
            print(f'{attribute}: {value}')
              

    return

print_melon(melons)



