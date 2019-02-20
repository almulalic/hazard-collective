class Page:
	def __init__(self, name, url, html):
		self.name=name
		self.url=url
		self.html=html

class Website:
	def __init__(self, name, home_page=Page("home", "/home", "index.html")):
		self.name=name
		self.pages=[home_page]
	def add_pages(self, pages):
		for page in pages:
			self.pages.append(page)