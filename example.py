import ROOT
from ROOT import gROOT

gROOT.ProcessLine(".L /home/users/fsetti/CMSSW_10_2_9/lib/slc6_amd64_gcc700/libTauAnalysisClassicSVfit.so")
gROOT.ProcessLine(".L /home/users/fsetti/CMSSW_10_2_9/lib/slc6_amd64_gcc700/libTauAnalysisSVfitTF.so")
gROOT.ProcessLine(".L SVfit_py.cc+")

ROOT.SVfit_mass( parameters )
