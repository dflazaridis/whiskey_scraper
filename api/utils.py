from dataclasses import dataclass


@dataclass()
class Route:
    path: str
    methods: list[str]


BOTTLE_ROUTES = {
    # Create => POST
    'create': Route('/', ['POST']),

    # - List => GET /
    'list': Route('/', ['GET']),

    # - Get  => GET /{whiskey_bottle_id}
    'get': Route('/<bottle_id>', ['GET']),

    # Update => PUT
    'update': Route('/<bottle_id>', ['PUT']),

    # Delete => DELETE
    'delete': Route('/<bottle_id>', ['DELETE']),
}
