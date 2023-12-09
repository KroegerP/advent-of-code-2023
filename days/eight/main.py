from functools import reduce
from math import gcd
import sys


sys.setrecursionlimit(100000)


class Node:
    name: str = None
    r: str = None
    l: str = None

    def __init__(self, _name: str, r_l_pair: tuple[str, str]) -> None:
        self.name = _name
        self.l = r_l_pair[0]
        self.r = r_l_pair[1]


class NodeList:
    nodes: list[Node] = None
    pattern: str = None
    cur_direction_idx = 0
    dest: str = "Z"

    def __init__(self, _pattern: str, node_list: list[Node]) -> None:
        self.nodes = node_list
        self.pattern = _pattern

    def increment_cur_idx(self):
        if self.cur_direction_idx == (len(self.pattern) - 1):
            self.cur_direction_idx = 0
        else:
            self.cur_direction_idx += 1

    def go_to_dest(self, cur_node_name, step_count=0):
        next_node = next(n for n in self.nodes if n.name == cur_node_name)
        if next_node.name[-1] == self.dest:
            return step_count
        else:
            step_count += 1
            print(next_node.name)
            if self.pattern[self.cur_direction_idx] == "L":
                self.increment_cur_idx()
                return self.go_to_dest(next_node.l, step_count)
            else:
                self.increment_cur_idx()
                return self.go_to_dest(next_node.r, step_count)

    def go_to_dest_list(self, cur_node_names: list[str], step_count=0):
        next_nodes = []

        for name in cur_node_names:
            next_node = None

            for node in self.nodes:
                # print(f"Node List:")
                # print(node)
                # [print(n.name) for n in nodes if n.name[-1] == name]
                # next_node = next([n.name for n in nodes if n.name[-1] == name])
                print(f"Looking for {name}: {node.name}")
                if node.name[-1] == name and node in temp_list:
                    print(f"Found Node: {node.name}")
                    next_node = node
                    temp_list.remove(node)
                    break

            next_nodes.append(next_node)

        # next_nodes = [
        #     next([n for [name for name in n] in self.node_lists if name.name == n_node_name])
        #     for n_node_name in cur_node_names
        # ]
        print("Next Nodes")
        [print(f"{n.name}") for n in next_nodes]
        if all(next_node.name[2] == self.dest for next_node in next_nodes):
            return step_count
        else:
            step_count += 1
            if self.pattern[self.cur_direction_idx] == "L":
                self.increment_cur_idx()
                return self.go_to_dest_list(
                    [next_node.l[-1] for next_node in next_nodes], step_count
                )
            else:
                self.increment_cur_idx()
                return self.go_to_dest_list(
                    [next_node.r[-1] for next_node in next_nodes], step_count
                )


def PartOne(file_contents: list[str]):
    pattern = file_contents[0].strip()

    nodes = []

    for line in file_contents[2:]:
        name = line.split("=")[0].strip()
        str_pair = line.split("=")[-1].strip()

        tup_pair = str_pair.replace("(", "").replace(")", "").split(", ")

        nodes.append(Node(name, tup_pair))

    [print(f"{n.name}: L: {n.l}, R: {n.r}") for n in nodes]

    node_list = NodeList(_pattern=pattern, node_list=nodes)

    result = node_list.go_to_dest("AAA")

    print(result)

    return result


class NodeListList:
    node_lists: list[list[Node]] = None
    pattern: str = None
    cur_direction_idx = 0
    dest: str = "Z"

    def __init__(self, _pattern: str, node_lists: list[Node]) -> None:
        self.node_lists = node_lists
        self.pattern = _pattern

    def increment_cur_idx(self):
        if self.cur_direction_idx == (len(self.pattern) - 1):
            self.cur_direction_idx = 0
        else:
            self.cur_direction_idx += 1

    def go_to_dest_list(self, cur_node_names: list[str], step_count=0):
        next_nodes = []
        zipped_stuff = zip(self.node_lists, cur_node_names)
        for node_list, name in zipped_stuff:
            print(f"Node List:")
            [print(n.name) for n in node_list]
            next_node = None
            for node in node_list:
                print(f"Looking for {name}: {node.name}")
                if node.name[2] == name:
                    next_node = node
                    break

            next_nodes.append(next_node)

        # next_nodes = [
        #     next([n for [name for name in n] in self.node_lists if name.name == n_node_name])
        #     for n_node_name in cur_node_names
        # ]
        print("Next Nodes")
        print(next_nodes)
        if all(next_node.name[2] == self.dest for next_node in next_nodes):
            return step_count
        else:
            step_count += 1
            if self.pattern[self.cur_direction_idx] == "L":
                self.increment_cur_idx()
                return self.go_to_dest_list(
                    [next_node.l[-1] for next_node in next_nodes], step_count
                )
            else:
                self.increment_cur_idx()
                return self.go_to_dest_list(
                    [next_node.r[-1] for next_node in next_nodes], step_count
                )


def PartTwoOld(file_contents: list[str]):
    pattern = file_contents[0].strip()

    str_nodes = []

    for line in file_contents[2:]:
        name = line.split("=")[0].strip()
        str_pair = line.split("=")[-1].strip()

        tup_pair = [name] + str_pair.replace("(", "").replace(")", "").split(", ")

        str_nodes.append(tup_pair)

    print(str_nodes)

    node_groups = set([n[0][:-1] for n in str_nodes])

    node_lists = []

    # for group in list(node_groups):
    #     print(f"Group {group}")
    #     node_list = [
    #         Node(_name=n[0], r_l_pair=n[1:]) for n in str_nodes if n[0][:-1] == group
    #     ]

    #     if group != "XX":
    #         node_lists.append(node_list)

    #         [print(n.name) for n in node_list]

    node_list = [Node(_name=n[0], r_l_pair=n[1:]) for n in str_nodes]

    num_paths = len([n for n in node_list if n.name[-1] == "A"])

    class_obj = NodeList(node_list=node_list, _pattern=pattern)

    init_input = ["A"] * num_paths

    print(init_input)

    result = class_obj.go_to_dest_list(init_input)

    print(result)

    return result


def PartTwo(file_contents: list[str]):
    pattern = file_contents[0].strip()

    nodes: list[Node] = []

    for line in file_contents[2:]:
        name = line.split("=")[0].strip()
        str_pair = line.split("=")[-1].strip()

        tup_pair = str_pair.replace("(", "").replace(")", "").split(", ")

        nodes.append(Node(name, tup_pair))

    [print(f"{n.name}: L: {n.l}, R: {n.r}") for n in nodes]

    node_list = NodeList(_pattern=pattern, node_list=nodes)

    starting_nodes = [n for n in nodes if n.name[-1] == "A"]

    res = []

    for starting in starting_nodes:
        result = node_list.go_to_dest(starting.name)

        print(f"Period: {result}")

        res.append(result)

    print(res)

    lcm = reduce(lambda x, y: x * y // gcd(x, y), res)

    print(lcm)

    return result
