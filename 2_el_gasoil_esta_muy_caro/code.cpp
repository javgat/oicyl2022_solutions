#include <iostream>

using namespace std;

int main(){

    double gas_price = 170;
    int kms, consumption;

    long long int res = 0;
    while(cin >> kms >> consumption) {
        res += kms * consumption; 
    }

    res = (long long int) res * gas_price / 100.0;
    cout << res << endl;    

    return 0;
}