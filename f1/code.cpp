#include <iostream>

using namespace std;

int main(){

    int altura, anchura, profundidad;
    int minimo, maximo, medio;

    cin >> altura >> anchura >> profundidad;

    minimo = min(min(altura, anchura), profundidad);
    maximo = max(max(altura, anchura), profundidad);
    medio = altura + anchura + profundidad - minimo - maximo;

    if (maximo <= 20 && medio <= 12 && minimo <= 4) cout << "A" << endl;
    else if (maximo <= 40 && medio <= 20 && minimo <= 10) cout << "B" << endl;
    else if (maximo <= 80 && medio <= 40 && minimo <= 40) cout << "C" << endl;
    else if (maximo <= 150 && medio <= 75 && minimo <= 60) cout << "D" << endl;
    else cout << "E" << endl;

    return 0;
}