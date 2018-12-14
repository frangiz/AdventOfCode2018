"""--- Day 14: Chocolate Charts ---"""


def part_a(puzzle_input):
    """
    Calculate the answer for part_a.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_a.

    """
    recipes_to_make = int(''.join(puzzle_input))
    elf_index_1 = 0
    elf_index_2 = 1
    recipies = [3, 7]
    while len(recipies) < recipes_to_make + 10:
        new_recipes = recipies[elf_index_1] + recipies[elf_index_2]
        if new_recipes >= 10:
            recipies.append(1)
            recipies.append(new_recipes - 10)
        else:
            recipies.append(new_recipes)
        elf_index_1 = (elf_index_1 + (recipies[elf_index_1] + 1)) % len(recipies)
        elf_index_2 = (elf_index_2 + (recipies[elf_index_2] + 1)) % len(recipies)
    return ''.join(map(str, recipies[recipes_to_make:recipes_to_make + 10]))


def part_b(puzzle_input):
    """
    Calculate the answer for part_b.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_b.

    """
    target = list(map(int, ''.join(puzzle_input)))
    elf_index_1 = 0
    elf_index_2 = 1
    recipies = [3, 7]
    while recipies[-len(target):] != target and recipies[-len(target) - 1: -1] != target:
        new_recipes = recipies[elf_index_1] + recipies[elf_index_2]
        if new_recipes >= 10:
            recipies.append(1)
            recipies.append(new_recipes - 10)
        else:
            recipies.append(new_recipes)
        elf_index_1 = (elf_index_1 + (recipies[elf_index_1] + 1)) % len(recipies)
        elf_index_2 = (elf_index_2 + (recipies[elf_index_2] + 1)) % len(recipies)
    if recipies[-len(target):] == target:
        return str(len(recipies) - len(target))
    else:
        return str(len(recipies) - len(target) - 1)


def solve(puzzle_input):
    """Returs the answer for both parts."""
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
