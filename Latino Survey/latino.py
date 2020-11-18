import viztools as vt
import pewtools as pt
import pandas as pd
import pyreadstat
import matplotlib.pyplot as plt
import seaborn as sns

#################### IO ####################
# read sav file and create a dict for columns
df15, meta15 = pyreadstat.read_sav('latino2015.sav')
df18, meta18 = pyreadstat.read_sav('latino2018.sav')

