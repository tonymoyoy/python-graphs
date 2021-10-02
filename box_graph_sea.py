import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd

# Variables
source = 'metrics.xlsx'

# Import from an excel file
metrics = pd.read_excel(source, sheet_name='box')

# Graph parameters
sb.set_theme(style="darkgrid")
sb.set_palette('colorblind')
sb.boxplot(data=metrics)
sb.swarmplot(data=metrics, color=".25")


# Plot Titles
plt.title('End to End Duration')
plt.xlabel('Month')
plt.ylabel('Days')

# Save to file
plt.savefig('box_graph_sea.png')