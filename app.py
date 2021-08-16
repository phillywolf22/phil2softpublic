from flask import Flask, render_template
from flask_assets import Bundle, Environment

app = Flask(__name__)

# Bundling src/main.css files into dist/main.css'
css = Bundle("src/main.css", output="dist/main.css", filters="postcss")

assets = Environment(app)
assets.register("main_css", css)
css.build()


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/page2")
def other():
    return render_template("index.html")


@app.route("/test")
def test():
    return render_template("test.html")


if __name__ == "__main__":
    app.run()
