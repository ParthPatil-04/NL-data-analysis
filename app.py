from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)
df = pd.read_csv("sample_data/sales.csv")  # Sample dataset

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        query = request.form.get("nl_query").lower()

        # Simple keyword matching (mock logic)
        if "average sales by category" in query:
            result = df.groupby("Category")["Sales"].mean().reset_index().to_html(index=False)
        elif "total sales" in query:
            result = f"<p>Total Sales: {df['Sales'].sum()}</p>"
        else:
            result = "<p>Query not recognized. Try 'average sales by category'.</p>"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

