# Auto generated configuration file
# using:
# Revision: 1.19
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v
# with command line options: MinBias_8TeV_cfi --conditions auto:startup -s GEN,SIM --datatier GEN-SIM -n 10
# --relval 9000,300 --eventcontent RAWSIM --io MinBias.io --python MinBias.py --no_exec --fileout minbias.root

import FWCore.ParameterSet.Config as cms

process = cms.Process("SIM")

# Import of standard configurations
process.load("Configuration.StandardSequences.Services_cff")
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Configuration.EventContent.EventContent_cff")
process.load("SimGeneral.MixingModule.mixNoPU_cfi")
process.load("Configuration.StandardSequences.GeometryRecoDB_cff")
process.load("Configuration.Geometry.GeometrySimDB_cff")
process.load("Configuration.StandardSequences.MagneticField_38T_cff")
process.load("Configuration.StandardSequences.Generator_cff")
process.load("IOMC.EventVertexGenerators.VtxSmearedRealistic8TeVCollision_cfi")
process.load("GeneratorInterface.Core.genFilterSummary_cff")
process.load("Configuration.StandardSequences.SimIdeal_cff")
process.load("Configuration.StandardSequences.EndOfProcess_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")

process.maxEvents = cms.untracked.PSet(input=cms.untracked.int32(10))

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet()
process.options.numberOfThreads = cms.untracked.uint32(4)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version=cms.untracked.string("$Revision: 1.19 $"),
    annotation=cms.untracked.string("MinBias_8TeV_cfi nevts:10"),
    name=cms.untracked.string("Applications"),
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions = cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag

process.GlobalTag = GlobalTag(process.GlobalTag, "auto:startup", "")

process.generator = cms.EDFilter(
    "Pythia6GeneratorFilter",
    pythiaPylistVerbosity=cms.untracked.int32(0),
    filterEfficiency=cms.untracked.double(1.0),
    pythiaHepMCVerbosity=cms.untracked.bool(False),
    comEnergy=cms.double(8000.0),
    maxEventsToPrint=cms.untracked.int32(0),
    PythiaParameters=cms.PSet(
        pythiaUESettings=cms.vstring(
            "MSTU(21)=1     ! Check on possible errors during program execution",
            "MSTJ(22)=2     ! Decay those unstable particles",
            "PARJ(71)=10 .  ! for which ctau  10 mm",
            "MSTP(33)=0     ! no K factors in hard cross sections",
            "MSTP(2)=1      ! which order running alphaS",
            "MSTP(51)=10042 ! structure function chosen (external PDF CTEQ6L1)",
            "MSTP(52)=2     ! work with LHAPDF",
            "PARP(82)=1.921 ! pt cutoff for multiparton interactions",
            "PARP(89)=1800. ! sqrts for which PARP82 is set",
            "PARP(90)=0.227 ! Multiple interactions: rescaling power",
            "MSTP(95)=6     ! CR (color reconnection parameters)",
            "PARP(77)=1.016 ! CR",
            "PARP(78)=0.538 ! CR",
            "PARP(80)=0.1   ! Prob. colored parton from BBR",
            "PARP(83)=0.356 ! Multiple interactions: matter distribution parameter",
            "PARP(84)=0.651 ! Multiple interactions: matter distribution parameter",
            "PARP(62)=1.025 ! ISR cutoff",
            "MSTP(91)=1     ! Gaussian primordial kT",
            "PARP(93)=10.0  ! primordial kT-max",
            "MSTP(81)=21    ! multiple parton interactions 1 is Pythia default",
            "MSTP(82)=4     ! Defines the multi-parton model",
        ),
        processParameters=cms.vstring(
            "MSEL=0         ! User defined processes",
            "MSUB(11)=1     ! Min bias process",
            "MSUB(12)=1     ! Min bias process",
            "MSUB(13)=1     ! Min bias process",
            "MSUB(28)=1     ! Min bias process",
            "MSUB(53)=1     ! Min bias process",
            "MSUB(68)=1     ! Min bias process",
            "MSUB(92)=1     ! Min bias process, single diffractive",
            "MSUB(93)=1     ! Min bias process, single diffractive",
            "MSUB(94)=1     ! Min bias process, double diffractive",
            "MSUB(95)=1     ! Min bias process",
        ),
        parameterSets=cms.vstring("pythiaUESettings", "processParameters"),
    ),
)

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)

# Schedule definition
process.schedule = cms.Schedule(
    process.generation_step,
    process.genfiltersummary_step,
    process.simulation_step,
    process.endjob_step,
)

# Filter all path with the production filter sequence
for path in process.paths:
    getattr(process, path)._seq = process.generator * getattr(process, path)._seq
