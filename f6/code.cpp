#include <iostream>

using namespace std;

int main(){

    int prev, current, res = 0;
    string read;
    bool first = true;

    while(getline(cin, read, ',')) {
        current = stoi(read);
        if (first) first = false;
        else if (current > prev) res++;
        prev = current;
    }

    cout << res << endl;

    return 0;
}