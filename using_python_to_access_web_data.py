def sum_numbers_from_file():
    import re
    filename = input('Type the name of file, please:')
    handle = open(filename)
    numlist = list()
    for line in handle:
        line = line.rstrip()
        numbers = re.findall('([0-9]+)', line)
        if len(numbers) < 1: continue
        for element in numbers:
            numlist.append(float(element))
    return(sum(numlist))
    

print(sum_numbers_from_file())