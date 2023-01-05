#include <iostream>
using namespace std;

int subtract(int a, int b) {
    return a - b;
}

int main() {
    int n1, n2;
    cout << "this took me 50 minutes to get running! thanks, microsoft!" << endl << "> ";
    cin >> n1;
    cin >> n2;
    cout << n1 << " - " << n2 << " = " << subtract(n1, n2) << endl;
}