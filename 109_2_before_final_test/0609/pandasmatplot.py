#%%
import requests
import json
import pandas as pd

import matplotlib.pyplot as plt

font = {"family": "DFKai-SB", "weight": "bold", "size": "12"}

plt.rc("font", **font)  # pass in the font dict as kwargs
plt.rc("axes", unicode_minus=False)


response = requests.get(
    "https://apis.youbike.com.tw/api/front/station/all?lang=tw&type=2"
)
a = json.loads(response.content)
df = pd.DataFrame.from_dict(a["retVal"])

# print(df.index)
# print(df)


tmp = df[df["area_code"] == "00"]
# print(ktmp)

stationtotal = tmp.groupby("status").count()[["area_code"]]
print(stationtotal)
# tt2 = stationtotal.sort_values(by="area_code")
# tt2["area_code"].plot.bar(title="高雄市區域", figsize=[10, 10])
# tt=stationtotal.sort_values(by='area_code')
# tt['area_code'].plot.pie(y="area_code",autopct = "%1.1f%%",figsize=[10,10])


#%%
