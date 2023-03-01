from ..userinterface.bing_s import QUERY_INPUT, SERRCH_BUTTON, URL
from ..userinterface.bing_sr import RESULT_PAGE_TITLE

from ..user_types import User
from screenpy import Actor
from screenpy_playwright.actions import Click, Enter, Visit
from screenpy.pacing import beat



class BingSearch:
    
    @staticmethod
    def for_text(search_query: str) -> "BingSearch":
        """Supply the text to search GitHub for."""
        return BingSearch(search_query)

    # @staticmethod
    # def as_(user: User) -> "OpenPage":
    #     """Log in as a predefined user."""
    #     return BingSearch(user)

    @beat('{} searches GitHub for "{search_query}"')
    def perform_as(self, the_actor: Actor) -> None:
        """Direct the actor to log in."""
        the_actor.attempts_to(
            Enter.the_text(self.search_query).into_the(QUERY_INPUT),
            Click.on_the(SERRCH_BUTTON)
            # Wait.for_the(RESULT_PAGE_TITLE),
        )
        # return


    def __init__(self, search_query: str) -> None:
        self.search_query = search_query
