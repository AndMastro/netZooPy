import pytest
import os
from netZooPy.panda.panda import Panda
import pandas as pd
import numpy as np

def test_panda():
    #print(os.getcwd())
    print('Start Panda run ...')
    ppi            ='tests/ToyData/ToyPPIData.txt'
    motif          ='tests/ToyData/ToyMotifData.txt'
    expression_data='tests/ToyData/ToyExpressionData.txt'
    lioness_file   =''
    rm_missing     = False
    output_file    ='travis_test_panda.txt'
    gt_file        ='tests/panda/test_panda.txt'

    #1. Vanilla panda
    panda_obj      = Panda(expression_data, motif, ppi, save_tmp=False, remove_missing=rm_missing,
                      keep_expression_matrix=bool(lioness_file))
    panda_obj.save_panda_results(output_file)
    res=pd.read_csv(output_file, sep=' ', header=None)
    gt =pd.read_csv(gt_file, sep=' ', header=None)
    #assert(gt.equals(round(res,3)))
    pd.testing.assert_frame_equal(res,gt,check_less_precise=False,check_exact=False)

    #2. with argument values
    rm_missing= False
    panda_obj = Panda(expression_data, motif, ppi, save_tmp=True, remove_missing=rm_missing,
                      keep_expression_matrix=True, save_memory=True)
    panda_obj.save_panda_results(output_file)
    res =pd.read_csv(output_file, sep=' ', header=None)
    assert(np.allclose(gt.iloc[:,3],res.transpose().values.flatten()))
    print('Test panda passed was successful!')

    #3. From command line
    #os.system('python3 run_panda.py -e ./tests/ToyData/ToyExpressionData.txt -m ./tests/ToyData/ToyMotifData.txt -p ./tests/ToyData/ToyPPIData.txt -o test_panda.txt -q output_panda.txt')
    #res2 =pd.read_csv(output_file, sep=' ', header=None)
    #pd.testing.assert_frame_equal(res,res2,check_less_precise=False,check_exact=False)
