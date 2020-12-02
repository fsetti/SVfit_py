import ROOT
from ROOT import gROOT

gROOT.ProcessLine(".L libTauAnalysisClassicSVfit.so")
gROOT.ProcessLine(".L libTauAnalysisSVfitTF.so")

# or
#gROOT.ProcessLine(".L /home/users/fsetti/CMSSW_9_4_4/lib/slc6_amd64_gcc700/libTauAnalysisClassicSVfit.so")
#gROOT.ProcessLine(".L /home/users/fsetti/CMSSW_9_4_4/lib/slc6_amd64_gcc700/libTauAnalysisSVfitTF.so")

gROOT.ProcessLine(".L SVfit_py.cc+")

diTau_mass = ROOT.SVfit_mass( parameters )
