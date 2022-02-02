#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

typedef vector<int> vi;
typedef pair<int, string> dayNid;

vector<vector<dayNid>> q_orders(6);
int current_day = 1;

bool earlier_back(dayNid a, dayNid b) { return a.first >= b.first; }

int get_priority_of(int n) {
    if (q_orders[n].size() == 0) return -1;
    if (q_orders[n].back().first > current_day) return -1;
    return n + current_day - q_orders[n].back().first;
}

void select(int n, bool print_day) {
    string id = q_orders[n].back().second;
    q_orders[n].pop_back();
    if (print_day) cout << '#' << current_day << '\n';
    cout << id << '\n';
}

int main() {
    int N, C, D;
    string id;
    char P;

    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> C >> id >> D >> P;
        if (P != 'P') C--;  // start at 0
        q_orders[C].push_back(make_pair(D, id));
    }
    for (int i = 0; i < 6; i++) {
        stable_sort(q_orders[i].begin(), q_orders[i].end(), earlier_back);
    }
    int delivered = 0;
    int max_priority, index, current_priority;
    bool end = false;
    while (delivered < N && current_day <= 30) {
        for (int i = 0; i < 10; i++) {
            max_priority = -1;
            index = -1;
            for (int n = 0; n < 6; n++) {
                current_priority = get_priority_of(n);
                if (current_priority > max_priority) {
                    max_priority = current_priority;
                    index = n;
                }
            }
            if (index == -1) {
                break;
            }
            select(index, i == 0);
            delivered++;
        }
        current_day++;
    }
    cout << flush;

    return 0;
}