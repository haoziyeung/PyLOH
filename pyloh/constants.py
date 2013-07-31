'''
Created on 2013-07-20

@author: Yi Li
'''
import numpy as np

BAF_N_MIN = 0.4
BAF_N_MAX = 0.6
BAF_T_MIN = 0.35
BAF_T_MAX = 0.65
LOH_FREC_MAX = 0.25
LOH_FREC_MIN = 0.15
SITES_NUM_MIN = 20
ERR = 0.01
EMPIRI_BAF = 0.485
EMPIRI_AAF = 1 - EMPIRI_BAF
PHI_INIT = 0.1
#ETA = 1.01
ETA = 1
BURN_IN = 30

GENOTYPES_NORMAL = ['AB']
GENOTYPES_TUMOR = ['NULL', 'A', 'B', 'AA', 'AB', 'BB', 'AAB', 'ABB', 'AABB']
GENOTYPES_TUMOR_NUM = len(GENOTYPES_TUMOR)
MU_N = [EMPIRI_BAF/(EMPIRI_BAF + EMPIRI_AAF)]
MU_T = [EMPIRI_BAF/(EMPIRI_BAF + EMPIRI_AAF), ERR, 1-ERR, ERR,
        EMPIRI_BAF/(EMPIRI_BAF + EMPIRI_AAF), 1-ERR,
        EMPIRI_BAF*1/(EMPIRI_BAF*1 + EMPIRI_AAF*2),
        EMPIRI_BAF*2/(EMPIRI_BAF*2 + EMPIRI_AAF*1),
        EMPIRI_BAF/(EMPIRI_BAF + EMPIRI_AAF)]
OMEGA = np.array([100, 400, 400, 2, 100, 2, 2, 2, 2])

CHROM_START = 0

CHROM_LIST = ['chr1', 'chr2', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7', 'chr8',
              'chr9', 'chr10', 'chr11', 'chr12', 'chr13', 'chr14', 'chr15',
              'chr16', 'chr17', 'chr18', 'chr19', 'chr20', 'chr21', 'chr22']

CHROM_LENS = [247249719, 242951149, 199501827, 191273063, 180857866, 170899992,
              158821424, 146274826, 140273252, 135374737, 134452384, 132349534,
              114142980, 106368585, 100338915, 88827254, 78774742, 76117153,
              63811651, 62435964, 46944323, 49691432]