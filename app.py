from flask import Flask, render_template, request
import pyshorteners

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    shortened_url = None
    if request.method == "POST":
        url = request.form.get("url")
        service = request.form.get("service_provider")  # Get selected service

        if url:
            try:
                shortener_obj = pyshorteners.Shortener()
                if service == "tinyurl":
                    shortened_url = shortener_obj.tinyurl.short(url)
                elif service == "isgd":
                    shortened_url = shortener_obj.isgd.short(url)
                elif service == "dagd":
                    shortened_url = shortener_obj.dagd.short(url)
                elif service == "osdb":
                    shortened_url = shortener_obj.osdb.short(url)
                else:
                    shortened_url = shortener_obj.tinyurl.short(url)  # Default
            except Exception as e:
                shortened_url = f"Error: Could not shorten URL. {e}"
        else:
            shortened_url = "Error: Please provide a valid URL."

    return render_template("index.html", shortened_url=shortened_url)

if __name__ == "__main__":
    app.run(debug=True)
