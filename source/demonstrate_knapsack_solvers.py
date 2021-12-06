from typing import List
from typing import Tuple


class Item(object):

    def __init__(self, n, v, w):
        """Construct an instance of the Item class."""
        # TODO: Add this source code segment by consulting the book

    def get_name(self) -> str:
        """Access the name of an Item."""
        # TODO: Add this source code segment by consulting the book

    def get_value(self) -> int:
        """Access the value of an Item."""
        # TODO: Add this source code segment by consulting the book

    def get_weight(self) -> int:
        """Access the weight of an Item."""
        # TODO: Add this source code segment by consulting the book

    def __repr__(self) -> str:
        """Produce a textual representation of the Item."""
        # TODO: Add this source code segment by consulting the book


def value(item: Item) -> int:
    """Return the value for a specific item."""
    # TODO: Add this source code segment by consulting the book


def weight_inverse(item: Item) -> float:
    """Return the inverse of the weight for a specific item."""
    # TODO: Add this source code segment by consulting the book


def density(item: Item) -> float:
    """Return the density of the item."""
    # TODO: Add this source code segment by consulting the book


def greedy(items: List[Item], max_weight: int, key_function) -> Tuple[List[Item], float]:
    """Perform the greedy algorithm for items, a maximum weight of a knapsack, and an objective function."""
    # TODO: Add this source code segment by consulting the book


def build_items() -> List[Item]:
    """Create an instance of a 0/1 knapsack using instances of the Item class."""
    # NOTE: You are welcome to try the program with a different instance of the
    # 0/1 Knapsack solver than the one provided in the book. However, make sure that when
    # you have your final submission you are using the same example as in Figure 14-1.
    names = ["Clock", "Painting", "Radio", "Vase", "Book", "Computer"]
    values = [175, 90, 20, 50, 10, 200]
    weights = [10, 9, 4, 2, 1, 20]
    items: List[Item] = []
    for i in range(len(values)):
        items.append(Item(names[i], values[i], weights[i]))
    return items


def powerset(s: List[Item]):
    """Generate the powerset of a list of items."""
    # Reference:
    # https://stackoverflow.com/questions/1482308/how-to-get-all-subsets-of-a-set-powerset
    # TODO: Consult the provided reference (or other online references)
    # and add in a function that can create the powerset of the list of items.
    # TODO: Make sure that you confirm that the function is producing the
    # correct output for the instance of the 0/1 Knapsack problem in Figure 14-1


def exhaustive_enumeration(pset, max_weight, get_value, get_weight):
    """Run an exhaustive enumeration algorithm to find best combination."""
    # TODO: Provide an implementation of this function by consulting the book


def run_exhaustive_enumeration(max_weight=20):
    """Use the exhaustive enumeration algorithm for a problem instance."""
    items = build_items()
    print("Generating the powerset of all items!")
    pset = powerset(items)
    print()
    print("Using exhaustive enumeration to fill a knapsack of size", max_weight)
    taken, value = exhaustive_enumeration(pset, max_weight, Item.get_value, Item.get_weight)
    print("Total value of items taken is", value)
    for item in taken:
        print("  ", item)


def run_greedy(items: List[Item], max_weight: int, key_function) -> None:
    """Run the greedy algorithm and display the result."""
    taken, value = greedy(items, max_weight, key_function)
    print("Total value of items taken is", value)
    for item in taken:
        print("  ", item)


def run_all_greedy(max_weight=20) -> None:
    """Run all greedy algorithm with all possible objective functions."""
    print("Running all of the knapsack solvers!")
    print()
    items = build_items()
    print("Using greedy-by-value to fill knapsack of size", max_weight)
    run_greedy(items, max_weight, value)
    print()
    print("Using greedy-by-weight to fill knapsack of size", max_weight)
    run_greedy(items, max_weight, weight_inverse)
    print()
    print("Using greedy-by-density to fill knapsack of size", max_weight)
    run_greedy(items, max_weight, density)
    print()


if __name__ == "__main__":
    # TODO: run the greedy algorithm and display its output
    # TODO: run the exhaustive enumeration algorithm and display its output
