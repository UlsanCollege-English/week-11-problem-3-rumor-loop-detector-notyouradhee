"""
HW03 — Rumor Loop Detector (Cycle in Undirected Graph)

Implement:
- has_cycle(graph)
- find_cycle(graph)
"""

def has_cycle(graph):
    """Return True if the undirected graph has any cycle; else False."""
    visited = set()

    def dfs(u, parent):
        visited.add(u)
        for v in graph.get(u, []):
            if v == u:
                return True
            if v not in visited:
                if dfs(v, u):
                    return True
            elif v != parent:
                return True
        return False

    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True
    return False


def find_cycle(graph):
    """Return a list of nodes forming a simple cycle where first == last.
    If no cycle, return None.

    Note:
    - Use DFS and a parent map.
    - Self-loop counts: return [u, u].
    """
    visited = set()
    parent = {}

    def build_cycle(u, v):
        path_u = [u]
        path_v = [v]
        pu = parent.get(u)
        pv = parent.get(v)
        while pu is not None:
            path_u.append(pu)
            pu = parent.get(pu)
        while pv is not None:
            path_v.append(pv)
            pv = parent.get(pv)
        set_u = set(path_u)
        meet = None
        for x in path_v:
            if x in set_u:
                meet = x
                break
        cu = path_u[:path_u.index(meet)+1]
        cv = path_v[:path_v.index(meet)+1]
        cv.reverse()
        cycle = cu + cv[1:]
        cycle.append(cycle[0])
        return cycle

    def dfs(u, p):
        visited.add(u)
        parent[u] = p
        for v in graph.get(u, []):
            if v == u:
                return [u, u]
            if v not in visited:
                c = dfs(v, u)
                if c is not None:
                    return c
            elif v != p:
                return build_cycle(u, v)
        return None

    for node in graph:
        if node not in visited:
            c = dfs(node, None)
            if c is not None:
                return c
    return None
