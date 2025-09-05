from flask import Flask, render_template, request
import pyshorteners

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    
    shortened_url = None
    if request.method == "POST":
        url = request.form.get("url")
        if url:
            try:
                shortener_obj = pyshorteners.Shortener()
                shortened_url = shortener_obj.tinyurl.short(url)
            except Exception as e:
                # Handle potential errors with the shortener service
                shortened_url = f"Error: Could not shorten URL. {e}"
        else:
            shortened_url = "Error: Please provide a valid URL."

    return render_template("index.html", shortened_url=shortened_url)

if __name__ == "__main__":
    app.run(debug=True)