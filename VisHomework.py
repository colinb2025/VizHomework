import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap

csv_file_path = "VisHomework/Top_Highest_Openings.csv"
df = pd.read_csv(csv_file_path)

#==========================================================================================================================================

mgm_movies = df[df['Distributor'].str.contains('Metro-Goldwyn-Mayer', case=False, na=False)]
gross = mgm_movies['Total Gross']
release = mgm_movies['Release']
plt.figure(figsize=(8, 5))
plt.scatter(release, gross, color='blue', alpha=0.5)
plt.title('Scatterplot of MGM Movie Gross Revenue')
plt.ylabel('Gross Revenue')
plt.xlabel('Title')
plt.xticks(rotation=45)
plt.grid(True)
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.3)
plt.show()

#==========================================================================================================================================

plt.figure(figsize=(8, 5))
df['Distributor'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Bar Plot of Quantity of Distributor Movies')
plt.xlabel('Distributor')
plt.ylabel('Frequency')
plt.grid(axis='y')
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.4)
plt.show()

#==========================================================================================================================================

df_subset = df.head(5)
cmap = get_cmap('tab10')

plt.figure(figsize=(10, 5))
for i, (index, row) in enumerate(df_subset.iterrows()):
    color = cmap(i)
    plt.plot(df_subset.loc[index, 'Date'], df_subset.loc[index, 'Opening'], marker='o', label=row['Release'] + ' Opening', color=color)

plt.title('Comparison of Opening Day Revenue')
plt.xlabel('Date')
plt.ylabel('Value')
plt.xticks(rotation=45)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.grid(True)
plt.subplots_adjust(left=0.08, right=0.5, top=0.9, bottom=0.3)
plt.show()