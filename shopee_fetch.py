import time
import requests
import json
from tqdm import tqdm   # 進度條，pip3 install tqdm
import constant_file

class product(object):
    name = 'name'
    price = 1
    weblink = 'weblink'
    photo_count = 0
    photolinks = []
    avg_rating = 4.0
    rating_count_list = [] #[total, 1, 2, 3, 4, 5]

def getAllItems(keyword, n_items = 30, minPrice = 1, maxPrice = 200000000, locations = '', ratingFilter = 3, preferred = False, officialMall = False):
    print(str.lower(str(preferred)))
    search_url = f'https://shopee.tw/api/v1/search_items/\
?by=relevancy\
&locations={locations}\
&keyword={keyword}\
&limit={n_items}\
&locations={locations}\
&ratingFilter={ratingFilter}\
&preferred={str.lower(str(preferred))}\
&officialMall={str.lower(str(officialMall))}'

    # print(search_url)

    search_result = requests.get(search_url, headers=constant_file.headers)
    search_data = json.loads(search_result.text)
    product_list = []

    for i in tqdm(range(n_items), desc = 'Processing search data...'):
        itemid = search_data['items'][i]['itemid']
        shopid = search_data['items'][i]['shopid']
        product_object = product()
        setattr(product_object, 'itemid', itemid)
        setattr(product_object, 'shopid', shopid)
        product_list.append(product_object)
    return product_list


def getItemInfo(itemid, shopid):
    product_object = product()
    product_url = f'https://shopee.tw/api/v2/item/get?itemid={itemid}&shopid={shopid}'
    product_info = requests.get(product_url, headers=constant_file.headers)
    
    product_data = json.loads(product_info.text)
    currency_unit = product_data['item']['coin_info']['spend_cash_unit']
    product_name = product_data['item']['name'].ljust(70)
    product_price = (product_data['item']['price'] / currency_unit)
    # print(product_name, product_price)

    setattr(product_object, 'name', product_name)
    setattr(product_object, 'price', product_price)

    product_weblink = f'https://shopee.tw/product/{shopid}/{itemid}'
    # print(product_weblink)
    setattr(product_object, 'weblink', product_weblink)

    product_photolinks = []
    product_photo_count = 0
    for photo_hash in product_data['item']['images']:
        product_photo_count += 1
        photo_link = f'https://cf.shopee.tw/file/{photo_hash}'
        # print('Photo\t'+photo_link)
        product_photolinks.append(photo_link)
    setattr(product_object, 'photo_count', product_photo_count)
    setattr(product_object, 'photolinks', product_photolinks)

    product_avg_rating = product_data['item']['item_rating']['rating_star']
    setattr(product_object, 'avg_rating', product_avg_rating)

    product_rating_count = product_data['item']['item_rating']['rating_count']
    setattr(product_object, 'rating_count_list', product_rating_count)
    
    time.sleep(0.15) # to avoid of being recognized as robot by shopee server
    return product_object
    
def main():
    # Testing functions
    product_list = getAllItems(keyword = 'iPhone 11', n_items = 40, locations = -1, ratingFilter = 4)
    print("product_list = ", product_list)
    print("itemid = ", product_list[0].itemid, "shopid = ", product_list[0].shopid)
    product_object = getItemInfo(product_list[0].itemid, product_list[0].shopid)
    print(product_object.name)

    # Simple Filters
    '''
    keyword: <str>
    n_items: <positive int>
    '''

    '''
    locations:
        -1 : Taiwan
        -2 : Abroad
    '''

    '''
    ratingFilter: <positive int>
    preferred = <bool> 蝦皮優選賣家
    officialMall = <bool> 蝦皮商城賣家
    '''

if __name__ == '__main__':
    main()