#include <iostream>
#include <vector>

using namespace std;

int main(){

    int total_size, N, value, weight;
    cin >> total_size >> N;

    vector<int> benefits(total_size+1, 0);

    int current = 0;
    while (N--) {
        cin >> weight >> value;
        for (int i = total_size - weight; i >= 0; i--){
            if (benefits[i+weight] < benefits[i] + value) {
                benefits[i+weight] = benefits[i] + value;
            }
        }
    }

    cout << benefits[total_size] << endl;

    return 0;
}