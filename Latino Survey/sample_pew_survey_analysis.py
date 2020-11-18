import viztools as vt
import pewtools as pt
import pandas as pd
import pyreadstat
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#################### IO ####################
# declare file
sf = 'latino2018.sav'

# read sav file and create a dict for columns
df, meta = pyreadstat.read_sav(sf)
question_dict = dict(zip(meta.column_names, meta.column_labels))

# wf = pt.weighted_frequency(df,meta,'qn3','weight')


#################### Easy Table ####################
# get slice of df, map the value labels and sort by labels (e.g. not by largest percentages)

# personal finance
qn12a = df['qn12a'].map(meta.value_labels['labels2']).value_counts(normalize=True).loc[meta.value_labels['labels2'].values()]
# print("Selected question: ", question_dict["qn12a"])
# print(qn12a)

#################### Matrix ####################
# look at crosstabs to differ by age group (weighted) 

question = 'qn14a'
demo = 'qn3'
crosstab = pt.quick_crosstab(df,meta,question,demo)
print(crosstab)



#################### plotting ####################

# heat map
fig, ax = plt.subplots()

im, cbar = vt.heatmap(crosstab.values, crosstab.axes[0], crosstab.axes[1], ax=ax,
                   cmap="PuRd", cbarlabel="percentage of surveyed")
texts = vt.annotate_heatmap(im, valfmt="{x:.1f} %")
plt.title("Trump Approval 2018")

fig.tight_layout()
plt.show()