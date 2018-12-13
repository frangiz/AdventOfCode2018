"""--- Day 13: Mine Cart Madness ---"""


class Cart():
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.turn = 0
        self.alive = True

    def __repr__(self):
        return "{}({!r})".format(self.__class__.__name__, self.__dict__)


def part_a(puzzle_input):
    """
    Calculate the answer for part_a.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_a.

    """
    tracks = [[a for a in line.rstrip('\n')] for line in puzzle_input]
    carts = []
    for y in range(len(tracks)):
        for x, c in enumerate(tracks[y]):
            if c == '<':
                carts.append(Cart(x, y, -1, 0))
            elif c == '>':
                carts.append(Cart(x, y, 1, 0))
            elif c == '^':
                carts.append(Cart(x, y, 0, -1))
            elif c == 'v':
                carts.append(Cart(x, y, 0, 1))
    while True:
        carts.sort(key=lambda c: (c.y, c.x))
        for cart in carts:
            cart.x = cart.x + cart.dx
            cart.y = cart.y + cart.dy
            got_collision = any(cart.x == c.x and cart.y == c.y and cart is not c for c in carts)
            if got_collision:
                return '{},{}'.format(cart.x, cart.y)
            if tracks[cart.y][cart.x] == '\\':
                cart.dx, cart.dy = cart.dy, cart.dx
            elif tracks[cart.y][cart.x] == '/':
                cart.dx, cart.dy = -cart.dy, -cart.dx
            elif tracks[cart.y][cart.x] == '+':
                if cart.turn == 0:
                    cart.dx, cart.dy = cart.dy, -cart.dx
                elif cart.turn == 1:
                    pass  # Just continue straight
                elif cart.turn == 2:
                    cart.dx, cart.dy = -cart.dy, cart.dx
                cart.turn = (cart.turn + 1) % 3

    return str(0)


def part_b(puzzle_input):
    """
    Calculate the answer for part_b.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_b.

    """
    tracks = [[a for a in line.rstrip('\n')] for line in puzzle_input]
    carts = []
    for y in range(len(tracks)):
        for x, c in enumerate(tracks[y]):
            if c == '<':
                carts.append(Cart(x, y, -1, 0))
            elif c == '>':
                carts.append(Cart(x, y, 1, 0))
            elif c == '^':
                carts.append(Cart(x, y, 0, -1))
            elif c == 'v':
                carts.append(Cart(x, y, 0, 1))
    while len(carts) > 1:
        carts.sort(key=lambda c: (c.y, c.x))
        for cart in carts:
            cart.x += cart.dx
            cart.y += cart.dy
            other_cart = next((c for c in carts if cart.x == c.x and cart.y == c.y and cart is not c and c.alive), None)
            if other_cart:
                cart.alive = False
                other_cart.alive = False
            if tracks[cart.y][cart.x] == '\\':
                cart.dx, cart.dy = cart.dy, cart.dx
            elif tracks[cart.y][cart.x] == '/':
                cart.dx, cart.dy = -cart.dy, -cart.dx
            elif tracks[cart.y][cart.x] == '+':
                if cart.turn == 0:
                    cart.dx, cart.dy = cart.dy, -cart.dx
                elif cart.turn == 1:
                    pass  # Just continue straight
                elif cart.turn == 2:
                    cart.dx, cart.dy = -cart.dy, cart.dx
                cart.turn = (cart.turn + 1) % 3
        carts = [c for c in carts if c.alive]
    if len(carts) == 1:
        return '{},{}'.format(carts[0].x, carts[0].y)
    return str(0)


def solve(puzzle_input):
    """Returs the answer for both parts."""
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
