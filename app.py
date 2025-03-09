from flask import Flask, render_template, request
from optimizer.performance import analyze_website
from optimizer.suggestions import optimization_tips

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    performance_data = None
    tips = None

    if request.method == "POST":
        url = request.form.get("url")
        if url:
            load_time = analyze_website(url)
            tips = optimization_tips(load_time)
            performance_data = {"url": url, "load_time": load_time}

    return render_template("index.html", performance_data=performance_data, tips=tips)

if __name__ == "__main__":
    app.run(debug=True)
