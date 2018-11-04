#include <vector>
#include <array>

using std::vector;
using std::array;

int N, M;
vector<vector<int>> adj;
vector<array<bool, 2>> visited;
vector<array<int, 2>> parent;
vector<int> cycle;

const int START = 0;

void dfs(int u, int s) {
    visited[u][s] = true;

    for(int v : adj[u]) {
        if(visited[v][!s]) continue;
        parent[v][!s] = u;
        dfs(v, !s);
    }
}

void solve(int N, int M, int *U, int *V) {
    ::N = N;
    ::M = M;

    adj.resize(N);
    visited.resize(N);
    parent.resize(N);

    for(int i = 0; i < M; i++) {
        int u = U[i];
        int v = V[i];
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    for(int u = 0; u < N; u++) {
        visited[u][0] = visited[u][1] = false;
    }

    dfs(START, 0);

    for(int u = START, s = 1; u != START || s != 0; u = parent[u][s], s = !s) {
        cycle.push_back(u);
    }
}

int length() {
    return cycle.size();
}

int get_node(int i) {
    return cycle[i];
}
