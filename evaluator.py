import turingarena as ta
import networkx as nx
import random


def main():
    test_cases = [
        nx.complete_graph(8),
        star_with_extra_edges(14, 19),
        two_touching_cycles(10, 3),
        two_touching_cycles(5, 22),
    ]

    for g in test_cases:
        assert nx.is_connected(g)
        assert not nx.is_bipartite(g)

    solved_cases = sum(
        evaluate_test_case(g)
        for g in test_cases
    )

    print(f"You solved {solved_cases} cases out of {len(test_cases)}.")


def evaluate_test_case(g):
    print(f"Evaluating on graph with {g.order()} nodes and {g.size()} edges...")

    try:
        run_test_case(g)
    except ta.AlgorithmError as e:
        print("Test case failed:")
        print(e.message)
        return False
    else:
        print("Test case OK!")
        return True


def run_test_case(g):
    with ta.run_algorithm(ta.submission.source) as process:
        process.procedures.solve(
            g.order(),
            g.size(),
            [u for u, v in g.edges()],
            [v for u, v in g.edges()],
        )

        cycle_len = process.functions.length()

        process.check(cycle_len <= ta.parameters['longest_allowed_walk'], f"cycle too long")

        cycle = [
            process.functions.get_node(i)
            for i in range(cycle_len)
        ]

        print(f"Answer: {cycle}, checking...")

        for i in range(len(cycle)):
            u, v = cycle[i], cycle[(i+1)%len(cycle)]
            process.check(g.has_edge(u, v), f"there is no edge ({u}, {v})")
        process.check(len(cycle) % 2 == 1, f"not in state 'SLURP'")

def star_with_extra_edges(N, M):
    g = nx.star_graph(N)
    g.add_edges_from(random.sample(set(nx.non_edges(g)), M - len(g.edges())))
    return g


def two_touching_cycles(a, b):
    return nx.relabel_nodes(nx.compose(
        nx.cycle_graph(a),
        nx.relabel_nodes(nx.cycle_graph(b), lambda u: a + u - 1),
    ), {
        i: j
        for i, j in enumerate(random.sample(range(a+b-1), a+b-1))
    })


main()
