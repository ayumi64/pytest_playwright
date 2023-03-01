from screenpy_playwright import Target

URL = "https://bing.com/"


QUERY_INPUT = Target.the("query input").located_by("input[name=\"q\"]")
SERRCH_BUTTON = Target.the("search button").located_by("[aria-label=\"搜索网页\"] svg")
BING_PAGE_TITLE = Target.the("bing title").located_by("title")