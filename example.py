import ROOT
import numpy as np
from ROOT import gROOT

gROOT.ProcessLine(".L libTauAnalysisClassicSVfit.so")
gROOT.ProcessLine(".L libTauAnalysisSVfitTF.so")

# or
#gROOT.ProcessLine(".L /home/users/fsetti/CMSSW_9_4_4/lib/slc6_amd64_gcc700/libTauAnalysisClassicSVfit.so")
#gROOT.ProcessLine(".L /home/users/fsetti/CMSSW_9_4_4/lib/slc6_amd64_gcc700/libTauAnalysisSVfitTF.so")

gROOT.ProcessLine(".L SVfit_py.cc+")

diTau_mass = ROOT.SVfit_mass( 11.7491,-51.9172, 787.352,-178.63,179.545, -1,0, 2,3, 33.7393,0.9409,-0.541458,0.51100e-3, 25.7322,0.618228,2.79362,0.13957 )
print ( ' di-tau mass: ' , diTau_mass )


diTau_p4 = ROOT.SVfit_ditau_p4( 11.7491,-51.9172, 787.352,-178.63,179.545, -1,0, 2,3, 33.7393,0.9409,-0.541458,0.51100e-3, 25.7322,0.618228,2.79362,0.13957 )
print ( ' diTau_p4 ' ,np.sqrt( diTau_p4[3] * diTau_p4[3] - diTau_p4[0] * diTau_p4[0] - diTau_p4[1] * diTau_p4[1] - diTau_p4[2] * diTau_p4[2] ) )


parts_p4 = ROOT.SVfit_all_p4( 11.7491,-51.9172, 787.352,-178.63,179.545, -1,0, 2,3, 33.7393,0.9409,-0.541458,0.51100e-3, 25.7322,0.618228,2.79362,0.13957 )
tt_p4 	= parts_p4[0]
tau1_p4 = np.array(parts_p4[1])
tau2_p4 = np.array(parts_p4[2])
tautau_p4 = tau1_p4 + tau2_p4
print ( ' tt_p4 ' , np.sqrt( tt_p4[3] * tt_p4[3] - tt_p4[0] * tt_p4[0] - tt_p4[1] * tt_p4[1] - tt_p4[2] * tt_p4[2] ) )
print ( ' tau1_p4 + tau2_p4 ' , np.sqrt( tautau_p4[3] * tautau_p4[3] - tautau_p4[0] * tautau_p4[0] - tautau_p4[1] * tautau_p4[1] - tautau_p4[2] * tautau_p4[2] ) )
