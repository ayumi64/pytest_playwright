from screenpy import Actor
from screenpy.pacing import beat
from screenpy_playwright.questions import Text

from ..userinterface.bing_sr import RESULT_PAGE_TITLE


class GetOpenResult:
    """Get the number in the badge on the shopping cart icon.

    Examples::

        the_actor.should(See.the(ShoppingCartBadgeNumber(), IsEqualTo(903)))
    """

    @beat("{} reads the number of items in their shopping cart.")
    def answered_by(self, the_actor: Actor) -> str:
        """Direct the actor to ask about the number of items in their cart."""
        return str(Text.of_the(RESULT_PAGE_TITLE).answered_by(the_actor))
