import json
import numpy as np
import pandas as pd

with open("data.json", "r") as d:
    data = json.load(d)

store = np.array(["Movie1", "Movie1","Movie1","Movie1","Movie1","Movie1","Movie1","Movie1","Movie1","Movie1","Movie1","Movie1","Movie1","Movie1","Movie1","Movie1","Movie1","Movie1","Movie1","Movie1","Movie1","Movie1","Movie1","Movie1","Movie1"])

Storage = pd.DataFrame(data, index= store)

print (Storage.loc["Movie1"])