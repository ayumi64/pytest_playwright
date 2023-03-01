from screenpy import Actor, given, then, when
from screenpy.actions import SeeAllOf
from screenpy.resolutions import ContainsTheText, IsEqualTo
from screenpy_playwright.questions import Number, Text
from ..tasks.bing_open import OpenPage
from ..userinterface.bing_s import URL
from ..questions.bing_open import GetOpenResult

Swalter = Actor.named("Swalter")

def test_open_bing(Swalter):
    # given(Swalter).was_able_to(BingSearch.perform_as(Swalter, Swalter, "Swalter"))
    given(Swalter).was_able_to(OpenPage.open_page(URL))
    
    then(Swalter).should(
        
        SeeAllOf.the(
            (GetOpenResult(), ContainsTheText("必应")),
        )
    )
    import time
    time.sleep(5)