import pytest
import os
from netZooPy import otter
import pandas as pd
import numpy as np

def test_condor():
    print('Start Otter run ...')
    W       = 'tests/otter/W.csv'
    W       = pd.read_csv(W, header=None)
    W       = W.values
    C       = 'tests/otter/C.csv'
    C       = pd.read_csv(C, header=None)
    C       = C.values
    P       = 'tests/otter/P.csv'
    P       = pd.read_csv(P, header=None)
    P       = P.values
    gt_file = 'tests/otter/test_otter.csv'

    #1. Vanilla panda
    W  =otter.otter(W,P,C)
    gt =pd.read_csv(gt_file, header=None)
    W =pd.DataFrame(data=W)
    pd.testing.assert_frame_equal(W,gt,check_less_precise=False,check_exact=False)
