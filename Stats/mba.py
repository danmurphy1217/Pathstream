from bs4 import BeautifulSoup
import requests as re
import nltk
import matplotlib.pyplot as plt
import seaborn as sns


url = "https://www.mbacrystalball.com/blog/2019/12/11/average-gpa-for-mba/"

html = re.get(url)
soup = BeautifulSoup(html.content , 'html.parser')
table_entries = soup.findAll('td')

colleges = soup.findAll('tr')

colleges_split = [str(r).split('>') for r in colleges]

gpa_vals = [str(gpa) for g in colleges_split for gpa in g if ('.' in str(gpa)) & ('-' not in str(gpa))]

final_gpa_vals = [str(v[:4]).replace('<', '').replace('-', '') for v in gpa_vals]

final_gpa_vals[4] =  final_gpa_vals[4][:3]


# print(final_gpa_vals)
plt.title('Histogram of MBA Average GPAs', fontsize = 18)
plt.ylabel('Frequency', fontsize = 13)

plt.xlabel('Average GPA', fontsize = 13)

sns.distplot(final_gpa_vals, bins = [3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8], hist=True, kde=False, color= (1, int(58/253), int(58/253)), hist_kws={
    'rwidth':0.85,
    'edgecolor':'black',
    'alpha':.77
})
plt.savefig('histogram')



