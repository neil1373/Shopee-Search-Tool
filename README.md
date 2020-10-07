# Exploring Shopee API

## Notice
* For Search feature, we use shopee api v1.
* For fetching item info, we use shopee api v2.

## Filter features

1. **(mandatory)** Keyword
2. number of maximum listing items
3. items location (Taiwan <code>-1</code> or Abroad <code>-2</code>)
4. ratings ( $>=n$ )
5. seller type
    * 優選賣家 （<code>boolean</code>）
	* 商城賣家 （<code>boolean</code>）

## Object "product"

* name
* price
* weblink
* photo_count
* photolinks (<code>list</code>)
* Average Rating
* Rating Counts (<code>list, [total, 1, 2, 3, 4, 5]</code>)

## Execution

1. execute $ python3 main.py in command line.
2. Open browser, and type "localhost:8080" in the URL field.
3. Press Enter and it will go to the homepage of the tool.

