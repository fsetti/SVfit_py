### SVfit_py

# Installation
SVfit_py requires the installation of [SVfit](https://github.com/SVfit/ClassicSVfit/tree/fastMTT_19_02_2019) (fastMTT_19_02_2019). Otherwise, the compiled libraries libTauAnalysisClassicSVfit.so and libTauAnalysisSVfitTF.so can be used instead.

# Running SVfit_py
Before running these scripts, make sure to set the environment as suggested in the SVfit instructions (e.g. cd ~/CMSSW_9_4_4/src ; cmsenv; cd -).
Once the installation of C++ SVfit is completed and the libraries libTauAnalysisClassicSVfit.so and libTauAnalysisSVfitTF.so are generated, they should be loaded in the python script along with the SVfit_py.cc script as shown in [example.py](https://github.com/fsetti/SVfit_py/blob/main/example.py).
