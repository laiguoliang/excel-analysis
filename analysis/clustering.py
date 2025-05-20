import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def cluster_customers(filepath):
    df = pd.read_excel(filepath)
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df[["年購買金額", "購買次數"]])
    kmeans = KMeans(n_clusters=3, random_state=0).fit(df_scaled)
    df["分群"] = kmeans.labels_
    return df.to_dict(orient="records")
