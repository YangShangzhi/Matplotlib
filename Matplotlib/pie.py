import matplotlib.pyplot as plt
import numpy as np

man = 71351
woman = 68187
man_perc = man / (man+woman)
woman_perc = woman / (man+woman)

fig_label = ['man','woman']
fig_color = ['blue','orange']

paches, fonts, texts = plt.pie([man_perc,woman_perc],labels=fig_label,colors=fig_color,
        explode=(0,0.05), autopct='%0.1f%%')

# text in the pie figure
for text in texts:
    text.set_color("white")

# text in the figure
for font in fonts+texts:
    font.set_fontsize(20)

plt.show()