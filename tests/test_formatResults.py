import formatter
from bs4 import BeautifulSoup

def test_sortList():
    """
    Checks the sortList function
    """
    arr = [{"price":"$10"}, {"price":"$20"}, {"price":"$0"}]
    ansArr = [{"price":"$0"}, {"price":"$10"}, {"price":"$20"}]
    revAnsArr = [{"price":"$20"}, {"price":"$10"}, {"price":"$0"}]
    assert formatter.sortList(arr, "pr", False) == ansArr
    assert formatter.sortList(arr, "pr", True) == revAnsArr

def test_formatResults():
    """
    Checks the formatResults function
    """
    titles = [BeautifulSoup('<div class="someclass">title  </div>', "html.parser")]
    prices = [BeautifulSoup('<div class="someclass">$0.99  </div>', "html.parser")]
    links = []

    product = formatter.formatResult("example", titles, prices, links)
    ans = {"title":"title", "price":"$0.99", "website":"example"}
    print(product["website"], ans["website"])

    assert product["title"] == ans["title"] and product["price"] == ans["price"] and product["website"] == ans["website"]