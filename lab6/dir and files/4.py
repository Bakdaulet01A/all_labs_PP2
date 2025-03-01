with open(r"Example 4.txt", 'r') as fp:
    lines = len(fp.readlines())
    print('Total Number of lines:', lines)