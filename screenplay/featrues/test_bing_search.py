from screenpy import given, then, when
from screenpy.actions import SeeAllOf
from screenpy.resolutions import ContainsTheText, IsEqualTo
from screenpy_playwright.actions import Click, Enter
from screenpy_playwright.questions import Number, Text
from ..tasks.bing_open import OpenPage
from ..tasks.search_task_click import BingSearch

from ..userinterface.bing_s import QUERY_INPUT, SERRCH_BUTTON
from ..userinterface.bing_sr import RESULT_PAGE_TITLE

from ..user_types import StandardUser

def test_bing_search(Swalter):
    # given(Swalter).was_able_to(BingSearch.perform_as(Swalter, Swalter, "Swalter"))
    given(Swalter).was_able_to(OpenPage.perform_as(Swalter, Swalter))
    when(Swalter).attempts_to(
        Click.on_the(QUERY_INPUT),
        Enter.the_text("PlayWright").into_the(QUERY_INPUT),
        Click.on_the(SERRCH_BUTTON),
    )

    then(Swalter).should(
        SeeAllOf.the(
            # (GetSearchResult(), ContainsTheText("PlayWright")),
            (
                Text.of_the(RESULT_PAGE_TITLE),
                ContainsTheText("PlayWright")
            ),
        )
    )
    import time
    time.sleep(5)