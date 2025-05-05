#include <bits/stdc++.h>
using namespace std;

// Global (or static) variables to mirror your Python code.
static vector<vector<int>> graphAdj;         // Adjacency list
static vector<bool> visited;                 // Visited array
static vector<int> tin;                      // Discovery time (tin)
static vector<int> backEdgesStart;           // Mirrors back_edges_start in Python
static vector<int> backEdgesEnd;             // Mirrors back_edges_end in Python

static vector<pair<int,int>> bridges;        // List of bridges
static vector<pair<int,int>> treeEdges;      // List of tree edges
static vector<pair<int,int>> backEdges;      // List of back edges

static int timerVal = 0;                    // "timer" variable in Python

int dfs(int source, int parent) {
    // If we've already visited this node:
    if(visited[source]) {
        // Check for potential back edge
        if(parent != -1 && tin[source] < tin[parent]) {
            backEdgesEnd[source]++;
            backEdgesStart[parent]++;
            backEdges.push_back({parent, source});
        }
        // Return 0 so that we don’t affect higher recursion’s counts
        return 0;
    }

    // Assign discovery time and mark visited
    tin[source] = timerVal++;
    visited[source] = true;

    // If not the root of DFS, record a tree edge (source -> parent)
    if(parent != -1) {
        treeEdges.push_back({source, parent});
    }

    // Track back edges contributed by children
    int numBackEdges = 0;

    // Explore neighbors
    for(int v : graphAdj[source]) {
        if(v == parent) continue; 
        numBackEdges += dfs(v, source);
    }

    // Adjust for back edges discovered at this node
    numBackEdges += backEdgesStart[source];
    numBackEdges -= backEdgesEnd[source];

    // The Python code does an additional "timer += 1" here
    timerVal++;

    // If this is not root and we have no back edges, it's a bridge
    if(parent != -1 && numBackEdges == 0) {
        bridges.push_back({parent, source});
    }

    return numBackEdges;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    int caseIndex = 1;

    while(true) {
        cin >> n >> m;
        // Break if reading failed or if n = m = 0
        if(!cin || (n == 0 && m == 0)) {
            break;
        }

        // Resize data structures
        graphAdj.assign(n+1, {});
        visited.assign(n+1, false);
        tin.assign(n+1, -1);
        backEdgesStart.assign(n+1, 0);
        backEdgesEnd.assign(n+1, 0);

        // Clear global edge containers
        bridges.clear();
        treeEdges.clear();
        backEdges.clear();

        // Reset timer
        timerVal = 0;

        // Read edges
        for(int i = 0; i < m; i++) {
            int x, y;
            cin >> x >> y;
            graphAdj[x].push_back(y);
            graphAdj[y].push_back(x);
        }

        // Call DFS on unvisited nodes
        for(int u = 1; u <= n; u++) {
            if(!visited[u]) {
                dfs(u, -1);
            }
        }

        // Print results for this case
        cout << caseIndex++ << "\n\n";

        // Bridges (print both directions)
        for(auto &b : bridges) {
            cout << b.first << " " << b.second << "\n";
        }

        // Tree edges
        for(auto &te : treeEdges) {
            cout << te.first << " " << te.second << "\n";
        }

        // Back edges (note the print order: (v, u) in original code)
        for(auto &be : backEdges) {
            cout << be.second << " " << be.first << "\n";
        }

        // Print "#"
        cout << "#\n";
    }

    return 0;
}
