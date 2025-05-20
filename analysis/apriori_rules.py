import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

def get_rules_from_excel(filepath):
    df = pd.read_excel(filepath)
    basket = df.groupby(["交易編號", "商品名稱"])["數量"].sum().unstack().fillna(0)
    basket = basket > 0  # bool 型資料
    frequent_items = apriori(basket, min_support=0.05, use_colnames=True)
    rules = association_rules(frequent_items, metric="lift", min_threshold=1.0)

    def convert(row):
        return {
            "antecedents": list(row["antecedents"]),
            "consequents": list(row["consequents"]),
            "support": row["support"],
            "confidence": row["confidence"],
            "lift": row["lift"]
        }

    return [convert(r) for _, r in rules.head(20).iterrows()]
