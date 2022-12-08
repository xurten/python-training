# Tip 7 Use enumarate instead of range method

flavor_list = ['vanilla', 'chocolate', 'hazelnut', 'strawberry']


# normal iteration
def bad_iterate():
    for i in range(len(flavor_list)):
        flavor = flavor_list[i]
        print(f'{i + 1}: {flavor}')


# better iteration
def good_iteration():
    for i, flavor in enumerate(flavor_list, 0):
        print(f'{i + 1}: {flavor}')


bad_iterate()
good_iteration()
