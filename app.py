from flask import Flask, render_template, jsonify
from analysis.apriori_rules import get_rules_from_excel
from analysis.clustering import cluster_customers

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/rules")
def rules():
    return render_template("rules.html")

@app.route("/cluster")
def cluster():
    return render_template("clusters.html")

@app.route("/api/rules")
def api_rules():
    return jsonify(get_rules_from_excel("data/sales.xlsx"))

@app.route("/api/cluster")
def api_cluster():
    return jsonify(cluster_customers("data/customers.xlsx"))

if __name__ == "__main__":
    app.run(debug=True)
