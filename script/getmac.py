import sys
with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        words = line.split()
        print('(eth.src == ' + words[1] +' || eth.dst == ' + words[1] + ') && ip')
