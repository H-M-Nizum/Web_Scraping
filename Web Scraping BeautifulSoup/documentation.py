#############################################################################################
################################ Navigating the tree ########################################
#############################################################################################

#############################################################################################
################################ Searching the tree #########################################
#############################################################################################

"""
 1. find() 
 2. find_all()
 3. A regular expression
 4. True
 5. A fuction
 6. A list
 7. find_all(name, attrs, recursive, string, limit, **kwargs)
 8. Searching by CSS class
 9. The limit argument
 10. find(name, attrs, recursive, string, **kwargs)
 11. find_parents(name, attrs, string, limit, **kwargs)
 12. find_parent(name, attrs, string, **kwargs)
 13. find_next_siblings(name, attrs, string, limit, **kwargs)
 14. find_next_sibling(name, attrs, string, limit, **kwargs)
 15. find_previous_siblings(name, attrs, string, limit, **kwargs)
 16. find_previous_sibling(name, attrs, string, **kwargs)
 17. find_all_next(name, attrs, string, limit, **kwargs)
 18. find_next(name, attrs, string, **kwargs)
 19. find_all_previous(name, attrs, string, limit, **kwargs)
 20. find_previous(name, attrs, string, **kwargs)
 21. CSS selectors through the .css property

"""

#############################################################################################
################################ Modifying the tree# ########################################
#############################################################################################
"""
1. Changing tag names and attributes (tag.name = "blockquote" tag['class'] = 'verybold')
2. Modifying .string (tag.string = "New link text.")
3. append()  - (<a>Foo</a>  a.append("Bar") # <a>FooBar</a>)
4. extend() - (<a>Soup</a>   a.extend(["'s", " ", "on"]) # <a>Soup's on</a>)
5. NavigableString() and .new_tag()  - (<b>Hello</b>  tag.append(NavigableString(" there")) # <b>Hello there.</b>) if you want create new tag new_tag = soup.new_tag("a", href="http://www.example.com"))
6. insert(), insert_before() and insert_after()
7. .clear() removes the contents of a tag:
8. .extract() removes a tag or string from the tree. It returns the tag or string that was extracted
9. .decompose() removes a tag from the tree, then completely destroys it and its contents:
10. .replace_with() extracts a tag or string from the tree, then replaces it with one or more tags or strings of your choice:
11. .wrap() wraps an element in the Tag object you specify. It returns the new wrapper:
12. .unwrap() is the opposite of wrap(). It replaces a tag with whatever’s inside that tag. It’s good for stripping out markup:
13. .smooth() to clean up the parse tree by consolidating adjacent strings:


"""

# ============================= Quick start Beautifulsoup =================================== #


# Html file or web page html source code
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>

"""

# ##import Beautifulsoup and print all html file using prettify for indentation.
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify())

# ##Here are some simple ways to navigate that data structure:

# #parse any single tag using tag name
# print(soup.title)
# print(soup.p)

# #parse innertext in a first tag
# print(soup.title.string)
# print(soup.a.string)

# #parse imediate first parent tag name
# print(soup.a.parent)
# print(soup.a.parent.name)

# #parse first tag class name
# print(soup.p['class'])

# #parse all tag element in a same tag name. provide in a list iteam
# print(soup.find_all('p'))
# print(soup.find_all('a'))
# print(soup.find('a')) # parse single iteam

# # parse a iteam depent on id
# print(soup.find(id = 'link3'))

# #One common task is extracting all the URLs found within a page’s <a> tags:
# for i in soup.find_all('a'):
#     print(i.get('href'))

# #extracting all the text from a page:
# print(soup.get_text())



# ============================= Details about Beautifulsoup =================================== #

"""
# Kinds of objects
    Beautiful Soup transforms a complex HTML document into a complex tree of Python objects. But you will only ever have to deal with about four kinds of objects: Tag, NavigableString, BeautifulSoup, and Comment. These objects represent the HTML elements that comprise the page.
"""

### ================================= Tag ==================================
## The most important methods of a tag are for accessing its name and attributes. 

soup1 = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')
tag = soup1.b
# print(tag)
# print(tag.name)

# change a tag’s name
tag.name = 'beauty'
# print(tag)

## Can access a tag’s attributes by treating the tag like a dictionary:
soup2 = BeautifulSoup('<b id="boldest">bold</b>', 'html.parser')
tag2 = soup2.b
# print(tag2)
# print(tag2.string)
# print(tag2['id']) # access id name

# # You can access the dictionary of attributes directly as .attrs:
# print(tag2.attrs)
# print(tag2.attrs.keys())
# print(tag2.attrs.values())

## You can add, remove, and modify a tag’s attributes. Again, this is done by treating the tag as a dictionary:

tag2['id'] = 'veryboldest'
# print(tag2)
# print(tag2['id'])

# add new attributes
tag2['newid'] = 'soBoldest'
# print(tag2)

# delete attributes
del tag2['newid']
# print(tag2)

# access or get attribute
# print(tag2['newid']) #KeyError: 'newid'
# print(tag2.get('newid')) #None

#### ======================================= Multi-valued attributes ==============================

# ## Beautiful Soup stores the value(s) of a multi-valued attribute as a list:
# # single class
css_soup = BeautifulSoup('<h1 class="first">Class attribute is a multi-valued attributes</h1>', 'html.parser').h1
# print(css_soup['class']) 
# # multiple class
css_soup1 = BeautifulSoup('<h1 class="first second third">Class attribute is a multi-valued attributes</h1>', 'html.parser').h1
# print(css_soup1['class'])

# # change multivalue class name
css_soup1['class'] = ['index', 'first', 'second']
# print(css_soup1)

"""
 If an attribute looks like it has more than one value, but its not a multi-valued attribute as defined by any version of the HTML standard, Beautiful Soup stores it as a simple string:
 You can force all attributes to be stored as strings by passing multi_valued_attributes=None as a keyword argument into the BeautifulSoup constructor:
"""

id_soup = BeautifulSoup('<p id="my id"></p>', 'html.parser')
# print(id_soup.p['id']) # 'my id'
no_list_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html.parser', multi_valued_attributes=None)
# print(no_list_soup.p['class']) # 'body strikeout'

# # You can use get_attribute_list to always return the value in a list container, whether it’s a string or multi-valued attribute value:
# print(id_soup.p.get_attribute_list('id')) # ["my id"]



# ## ============================= class bs4.NavigableString ============================ ##
""" 
    A tag can contain strings as pieces of text. Beautiful Soup uses the NavigableString class to contain these pieces of text. 
    A NavigableString is just like a Python Unicode string, I can convert a NavigableString to a Unicode string with str:
    You can’t edit a string in place, but you can replace one string with another, using replace_with():
"""
NavigableStringsoup = BeautifulSoup('<p class="boldest">Extremely bold</p>', 'html.parser')
# print(NavigableStringsoup.p)
# print(NavigableStringsoup.p.string)
# print(type(NavigableStringsoup.p.string)) #<class 'bs4.element.NavigableString'>
unicode_str = str(NavigableStringsoup.p.string)
# print(unicode_str)
# print(type(unicode_str)) #<class 'str'>

NavigableStringsoup.p.string.replace_with("Replace previous string")
# print(NavigableStringsoup.p.string)


# ## =========================== class bs4.Comment ==================##
"""
The Comment object is just a special type of NavigableString:
"""
comment_soup = BeautifulSoup("<b><!--Hey, buddy. Want to buy a used parser?--></b>", 'html.parser')
comment = comment_soup.b.string
# print(comment)
# print(type(comment)) # <class 'bs4.element.Comment'>



# ### =============================== Navigating the tree =====================================###
"""
Move from one part of a document to another. There are sevarel way -
    1. Going Down
    2. Going Up
    3. Going sideways
    4. Going back and forth

"""


html_doc3 = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup3 = BeautifulSoup(html_doc3, 'html.parser')
# print(soup3.prettify())

# ## 1. Going Down -----------------------------------------------------------------
""" Tags may contain strings and more tags. These elements are the tag’s children. Beautiful Soup provides a lot of different attributes for navigating and iterating over a tag’s children. """
    # #Navigating using tag names (using find() method)
# print(soup3.find('head'))
# print(soup3.head)
# print(soup3.title)
# print(soup3.h6) # return None if this tag is not exist
# print(soup3.find('h5')) # return None if this tag is not exist

# print(soup3.body.p) # This code gets the first <b> tag beneath the <body> tag:
# print(soup3.find('a')) # Gives only the first tag by that name:

## List of element
# print(soup3.find_all('a')) # If you need to get all the <a> tags, you can use find_all()

    ## # .contents and .children
soup3_head = soup3.head
# print(soup3_head)
# print(soup3_head.contents) # list of child element
# print(soup3_head.contents[0]) # First element
# print(soup3_head.contents[0].contents) # list of First element childrean
# print(soup3_head.contents[0].contents[0]) # First element First childrean

""" Instead of getting them as a list, you can iterate over a tag’s children using the .children generator: """

title_tag = soup3_head.contents[0]
for child in title_tag.children:
    # print(child)
    pass

""" If a tag’s only child is another tag, and that tag has a .string, then the parent tag is considered to have the same .string as its child: """

# print(soup3_head.contents) # [<title>The Dormouse's story</title>]
# print(soup3_head.string) # 'The Dormouse's story'


    # ## .strings and stripped_strings
""" 
If there’s more than one thing inside a tag, you can still look at just the strings. Use the .strings generator to see all descendant strings:
Newlines and spaces that separate tags are also strings. You can remove extra whitespace by using the .stripped_strings generator instead: Here, strings consisting entirely of whitespace are ignored, and whitespace at the beginning and end of strings is removed.
 """

# print("------------------- Normal string -------------------------")
# for string in soup3.strings:
#     print(string)
# print("-------------------------- Nomal string using repr---------------------")
# for string in soup3.strings:
#     print(repr(string))
# print("-------------------------- Stripped_string using repr---------------------")
# for string in soup3.stripped_strings:
#     print(repr(string))



# ## 1. Going up -----------------------------------------------------------------

"""
.parent
You can access an elements parent with the .parent attribute. the <head> tag is the parent of the <title> tag:

"""

title_tag1 = soup3.title
# print(title_tag1) # # <title>The Dormouse's story</title>
# The title string itself has a parent: the <title> tag that contains it:
# print(title_tag1.parent) # <head><title>The Dormouse's story</title></head>

"""
.parents
You can iterate over all of an elements parents with .parents. This example uses .parents to travel from an <a> tag buried deep within the document, to the very top of the document:
"""

link_tag = soup3.a
# print(link_tag) # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
for parent in link_tag.parents:
    # print(parent.name)
    pass

    # p
    # body
    # html
    # [document]



# ## 1. Going sideways -----------------------------------------------------------------

sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></a>", 'html.parser')
# print(sibling_soup.prettify())

#   <a>
#       <b>
#           text1
#       </b>
#       <c>
#           text2
#       </c>
#   </a>

"""
The <b> tag and the <c> tag are at the same level: they are both direct children of the same tag. We call them siblings. When a document is pretty-printed, siblings show up at the same indentation level. 
"""



    # ## .next_sibling and .previous_sibling

"""
You can use .next_sibling and .previous_sibling to navigate between page elements that are on the same level of the parse tree:
The <b> tag has a .next_sibling, but no .previous_sibling, because theres nothing before the <b> tag on the same level of the tree. For the same reason, the <c> tag has a .previous_sibling but no .next_sibling:
"""
# print(sibling_soup.b.next_sibling) # <c>text2</c>
# print(sibling_soup.c.previous_sibling) # <b>text1</b>

# The strings “text1” and “text2” are not siblings, because they don’t have the same parent:
# print(sibling_soup.b.next_sibling.string.next_sibling) # None
# print(sibling_soup.c.previous_sibling.string.previous_sibling) # None



"""
.next_siblings and .previous_siblings
You can iterate over a tag’s siblings with .next_siblings or .previous_siblings:

"""
for sibling in soup3.a.next_siblings:
    # print(repr(sibling))
    pass

# print("--- previous ---")
for sibling in soup3.find(id="link3").previous_siblings:
    # print(repr(sibling))
    pass



# ## 1. Going back and forth -----------------------------------------------------------------




## ========================== Searching the tree ============================================

"""
 find() 
 find_all()
 A regular expression
 True
 A fuction
 A list
 find_all(name, attrs, recursive, string, limit, **kwargs)
 Searching by CSS class
 The limit argument
 find(name, attrs, recursive, string, **kwargs)
 find_parents(name, attrs, string, limit, **kwargs)
 find_parent(name, attrs, string, **kwargs)
 find_next_siblings(name, attrs, string, limit, **kwargs)
 find_next_sibling(name, attrs, string, limit, **kwargs)
 find_previous_siblings(name, attrs, string, limit, **kwargs)
 find_previous_sibling(name, attrs, string, **kwargs)
 find_all_next(name, attrs, string, limit, **kwargs)
 find_next(name, attrs, string, **kwargs)
 find_all_previous(name, attrs, string, limit, **kwargs)
 find_previous(name, attrs, string, **kwargs)
 CSS selectors through the .css property


"""

    # ##A regular expression
"""
If you pass in a regular expression object, Beautiful Soup will filter against 
that regular expression using its search() method. 
This code finds all the tags whose names start with the letter “b”; in this case, 
the <body> tag and the <b> tag:
"""
import re
for i in soup3.find_all(re.compile("^b")):
    # print(i.name)
    pass

""" This code finds all the tags whose names contain the letter t: """
for i in soup3.find_all(re.compile("t")):
    # print(i.name)
    pass

    # ## True
""" The value True matches every tag it can. This code finds all the tags in the document, but none of the text strings: """
for i in soup3.find_all(True):
    # print(i.name)
    pass

    # ## A function
""" If none of the other matches work for you, define a function that takes 
an element as its only argument. Pass this function into find_all() """ 
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')

    # ## A list
""" If you pass in a list, Beautiful Soup will finds all the <a> tags and all the <b> tags: """
# print(soup3.find_all(['a', 'b']))

    # ## Searching by CSS class
# print(soup3.find_all("a", class_="sister"))


    # ## The limit argument
# print(soup3.find_all('a', limit=2)) # print only two instance


    # ## find(name, attrs, recursive, string, **kwargs)
""" sometimes you only want to find one result.  If find_all() cant find anything, it returns an empty list. find() returns None:"""
soup.find('title')


