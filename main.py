from flask import *
import shopee_fetch
import constant_file

#建立flask物件(習慣上通常取名為 app)
app = Flask(__name__)

#home(search) page
@app.route("/", methods = ['GET', 'POST'])
def home():
	return render_template("searchPage.html")

#search results page
@app.route("/keyword=<keyword>&item_num=<item_num>&locations=<locations>&ratingFilter=<ratingFilter>", methods = ['GET', 'POST'])
def keywordSearchResults(keyword, item_num, locations, ratingFilter):
	if locations == "Taiwan":
		locations = -1
	else:
		locations = -2
	item_list = shopee_fetch.getAllItems(keyword = keyword, n_items = int(item_num), locations = locations, ratingFilter = ratingFilter)
	return render_template("keywordSearchResults.html", item_list = item_list)

#item info page
@app.route("/searchItemByKeyword/itemId=<itemId>&shopId=<shopId>", methods = ['GET', 'POST'])
def searchItemByKeyword(itemId, shopId):
	
	item = shopee_fetch.getItemInfo(itemId, shopId)
	return render_template("itemInfo.html", item = item)

if __name__ == "__main__":
	app.run(debug = True, host = "0.0.0.0", port = 8080)
