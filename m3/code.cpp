#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#include <bitset>

using namespace std;

#define MAX_PROVIDERS 10000

typedef vector<int> vi;
typedef pair<int, int> pair_ints;

vector<pair_ints> providers;

bool decreasing(int a, int b) {
    return a > b;
}

bool cheaper_n_bigger(pair_ints a, pair_ints b) {
    // first -> cost
    // second -> max_weight

    if (a.first == b.first) return a.second > b.second;
    return a.first < b.first;
}

int main() {

    int n,m;
    int weight;
    int cost;
    int res;
    bool impossible;

    vi routes;
    bitset<MAX_PROVIDERS> used;

    while(cin >> n >> m) {
        used.reset();
        routes.clear();
        providers.clear();
        impossible = false;
        res = 0;

        while(n--){
            cin >> weight;
            routes.push_back(weight);
        }
        while(m--){
            cin >> cost >> weight;
            providers.push_back(make_pair(cost, weight));
        }

        sort(routes.begin(), routes.end(), decreasing);
        sort(providers.begin(), providers.end(), cheaper_n_bigger);

        for(auto p: providers) {
            cout << p.first << " " << p.second << endl;
        }

        for(int w : routes) {
            int pos = 0;
            while(!impossible) {
                if (!used[pos] && providers[pos].second >= w) break; 
                if (++pos == providers.size()) impossible = true; 
            }
            if (impossible) break;
            used[pos].flip();
            res += providers[pos].first;
            cout <<w << " "<< providers[pos].first << " " << providers[pos].second << endl;
        }

        if(impossible) cout << "Imposible" << endl;
        else cout << res << endl;
    }

    return 0;
}