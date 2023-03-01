from screenpy import Actor
from screenpy_playwright.actions import Click, Enter, Visit
from screenpy.pacing import beat
from .search_task_click import BingSearch

class OpenPage:
    """Log in with the supplied user or username/password combination.

    Examples::

        the_actor.attempts_to(LogIn.as_(StandardUser))

        the_actor.attempts_to(LogIn.using("username", "password"))
    """
    @staticmethod
    def open_page(URL) -> "OpenPage":
        """Supply the text to search GitHub for."""
        return OpenPage(URL)
     
    # @staticmethod
    # def for_text(search_query: str) -> "SearchGitHub":
    #     """Supply the text to search GitHub for."""
    #     return SearchGitHub(search_query)
    
    @beat('open page')
    def perform_as(self, the_actor: Actor, ) -> None:
        """Direct the actor to log in."""
        the_actor.attempts_to(
            Visit(self.URL)
        )
        return BingSearch(the_actor)
    
    def __init__(self, URL: str) -> None:
        self.URL = URL
