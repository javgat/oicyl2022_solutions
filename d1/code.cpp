#include <iostream>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <vector>

#define INF 999999  // int bigger than max clients

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vii;

int P, C, N;
string id;
unordered_map<string, vi> orders;
unordered_set<string> indexed;
vii adj_list(1001);
vi distances(1001, INF);
vi visited(1001, 0);

void read_input() {
    cin >> P;
    while (P--) {
        cin >> id;
        orders[id] = {0};
        indexed.insert(id);
    }

    cin >> C;
    for (int client_id = 1; client_id <= C; client_id++) {
        cin >> N;
        while (N--) {
            cin >> id;
            if (indexed.find(id) == indexed.end()) {
                indexed.insert(id);
                orders[id] = {};
            }
            orders[id].push_back(client_id);
        }
    }

    indexed.clear();
}

void dijkstra(int start) {
    distances[start] = 0;
    priority_queue<pair<int, int>> pq;
    pq.push(make_pair(0, start));
    while (true) {

        int node = pq.top().second;
        pq.pop();
        
        if(node == -1) break;

        visited[node] = 1;
        for (int n : adj_list[node]) {
            if (!visited[n] && distances[n] <= distances[node] + 1) {
                distances[n] = distances[node] + 1;
                pq.push(make_pair(-distances[n], n));
            }
        }
    } 
}

int main() {
    read_input();
    for (pair<string, vi> pair_relations : orders) {
        vi relations = pair_relations.second;
        for (int i = 0; i < relations.size() - 1; i++) {
            for (int j = i + 1; j < relations.size(); j++) {
                if (relations[i] == relations[j]) continue;
                adj_list[relations[i]].push_back(relations[j]);
                adj_list[relations[j]].push_back(relations[i]);
            }
        }
    }
    
    dijkstra(0);

    for (int i=1; i <= C; i++) {
        if(distances[i] == INF) cout << -1 << endl;
        else cout << distances[i] << endl;
    }
    
    return 0;
}