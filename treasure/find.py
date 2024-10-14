from typing import List


def find_treasure(treasure_map: List[int], coins: int = 0) -> int:
    r = list()
    if len(treasure_map) == 0 or treasure_map is None:
        # something looks like f***ed
        raise Exception("Map is empty")
    if len(treasure_map) == 1:
        # we have found the treasure!
        return 0
    if coins == 2 and treasure_map == [3, 10, 9]:
        pass

    if treasure_map[0] < len(treasure_map):
        r.append(find_treasure(treasure_map[treasure_map[0]:], coins))

    if coins > 0:
        # * if coins available alter instructions
        if treasure_map[0] + 1 >= len(treasure_map):
            # firs validate if altered instruction is not beyond treasure
            pass
        else:
            # ** by adding one
            r.append(find_treasure(treasure_map[treasure_map[0] + 1:], coins - 1))

        if treasure_map[0] > 1 and treasure_map[0]-1 < len(treasure_map):
            # ** by substituting one if possible
            r.append(find_treasure(treasure_map[treasure_map[0] - 1:], coins - 1))

    if all(item is None for item in r):
        # No path to for the win
        return None

    return 1 + min([item for item in r if item is not None])


if __name__ == '__main__':
    print("run UT")
