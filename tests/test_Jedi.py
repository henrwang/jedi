import pytest

import ase.io as io
from ase.vibrations.vibrations import VibrationsData
import numpy as np
import sys
sys.path.append('./')
from jedi.jedi import Jedi


class  TestJEDIHCN():
  
    @classmethod
    def setup_class(cls):

        mol=io.read('./tests/hcn/opt.json')
        mol2=io.read('./tests/hcn/dis.json')
        hessian=VibrationsData.read('./tests/hcn/modes.json')
        cls.hcn = Jedi(mol,mol2,hessian)
        cls.hcn.run()
        phessian=VibrationsData.from_2d(mol,np.loadtxt('./tests/hcn/parthess'),indices=[2,3,5,8,9,11])
        cls.phcn = Jedi(mol,mol2,phessian)
        cls.phcn.partial_analysis(indices=[2,3,5,8,9,11])


    def test_run(cls):
        '''Test if ERIMs are correct'''
        assert np.array_equal(cls.hcn.E_RIMs,np.loadtxt('./tests/hcn/ERIMs'))
    
    def test_partial(cls):
        '''Test if ERIMs are correct'''
        assert np.array_equal(cls.phcn.E_RIMs,np.loadtxt('./tests/hcn/pERIMs'))