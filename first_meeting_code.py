import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Xs = np.load("Datasets/kryptonite-9-X.npy")
Ys = np.load("Datasets/kryptonite-9-y.npy")
df_x = pd.DataFrame(Xs)
df_y = pd.DataFrame(Ys)
# correlation = np.corrcoef(Xs, rowvar=False, y=Ys)

# # print(correlation)

# df_x[0].apply(lambda x: 0 if x < 0.5 else 1)

for c in df_x.columns:
    df_x[c] = df_x[c].apply(lambda x: 0 if x < 0.5 else 1)

df_x.hist()

# plt.matshow(correlation)
plt.show()



# print(df.head())