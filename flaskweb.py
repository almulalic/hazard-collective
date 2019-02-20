from website import Website, Page
from flask import Flask, render_template

ws=Website(name="Hazard Collective", home_page=Page("home", "/home", "index.html"))
ws.add_pages({
	Page("generic", "/generic", "generic.html"),
	Page("elements", "/elements", "elements.html")
	})

app = Flask(__name__)

@app.route(ws.pages[0].url)
def home():
	return render_template(ws.pages[0].html, website=ws, page=ws.pages[0])

@app.route(ws.pages[1].url)
def generic():
	return render_template(ws.pages[1].html, website=ws, page=ws.pages[1])

@app.route(ws.pages[2].url)
def elements():
	return render_template(ws.pages[2].html, website=ws, page=ws.pages[2])



if __name__ == "__main__":
	app.run(debug=True)
