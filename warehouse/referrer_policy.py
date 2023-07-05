import typing

from pyramid.request import Request


def referrer_policy_tween_factory(
    handler: typing.Callable[[Request], Response], registry: typing.Any
) -> typing.Callable[[Request], Response]:
    """Returns the tween function that adds a Referrer-Policy header to the response.

    :param handler: The next tween or handler in the pyramid middleware chain.
    :param registry: The application registry.
    :return: The tween function that adds the Referrer-Policy header to the response.
    """

    def referrer_policy_tween(request: Request) -> Response:
        """Adds a Referrer-Policy header to the response.

        :param request: The pyramid request.
        :return: The response with the added Referrer-Policy header.
        """
        response = handler(request)
        response.headers["Referrer-Policy"] = "origin-when-cross-origin"
        return response

    return referrer_policy_tween


def includeme(config):
    config.add_tween("warehouse.referrer_policy.referrer_policy_tween_factory")
