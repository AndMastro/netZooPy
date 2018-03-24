#!/usr/bin/env python
"""Run PANDA algorithm from the command line.

Usage:
  -h, --help: help
  -e, --expression: expression values
  -m, --motif: pair file of motif edges
  -p, --ppi: pair file of PPI edges
  -o, --out: output file
  Example:
  python run_puma.py -e ./ToyData/ToyExpressionData.txt -m ./ToyData/ToyMotifData.txt -p ./ToyData/ToyPPIData.txt -o test_puma.txt
"""
import sys
import getopt
import pypanda

def main(argv):
    #Create variables
    expression_data = None
    motif = None
    ppi = None
    output_file = "output_panda.txt"
    rm_missing = False
    # Get input options
    try:
        opts, args = getopt.getopt(argv, 'he:m:p:o:r', ['help', 'expression=', 'motif=', 'ppi=', 'out=', 'rm_missing'])
    except getopt.GetoptError:
        print(__doc__)
        sys.exit()
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print(__doc__)
            sys.exit()
        elif opt in ('-e', '--expression'):
            expression_data = arg
        elif opt in ('-m', '--motif'):
            motif = arg
        elif opt in ('-p', '--ppi'):
            ppi = arg
        elif opt in ('-o', '--out'):
            output_file = arg
        elif opt in ('-r', '--rm_missing'):
            rm_missing = arg

    #Check if required options are given
    print('Input data:')
    print('Expression:', expression_data)
    print('Motif data:', motif)
    print('PPI data:', ppi)
    if not expression_data and not motif and not ppi:
        print('Missing inputs!')
        print(__doc__)
        sys.exit()

    # Run PANDA
    print('Start Panda run ...')
    panda_obj = pypanda.Panda(expression_data, motif, ppi, save_tmp=True, remove_missing=rm_missing)
    #panda_obj = pypanda.Panda(expression_data, motif, None, save_tmp=True, remove_missing=rm_missing)
    #panda_obj = pypanda.Panda(None, motif, ppi, save_tmp=True, remove_missing=rm_missing)
    #panda_obj = pypanda.Panda(None, motif, None, save_tmp=True, remove_missing=rm_missing)
    #panda_obj = pypanda.Panda(expression_data, None, ppi, save_tmp=True, remove_missing=rm_missing)
    panda_obj.save_panda_results(output_file)
    panda_obj.top_network_plot(top=100, file='panda_top100genes.png')
    #indegree = panda_obj.return_panda_indegree()
    #outdegree = panda_obj.return_panda_outdegree()
    print('All done!')

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))



