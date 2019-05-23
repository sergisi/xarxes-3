import sys
with open(sys.argv[1], 'r') as f:
    print('\\begin{table}[!h]\n\\centering\n\\begin{tabular}{|c|c|c|}\n\\hline')
    for line in f:
        camps = line.split('&')
        print(' &'.join(camps), end='\\\\\n')
        print('\\hline')
    print('\\end{tabular}\n\\caption{·}\n\\label{·}\n\\end{table}')
