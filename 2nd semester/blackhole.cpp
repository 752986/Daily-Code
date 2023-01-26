#include <iostream>
using namespace std;

const double c = 2.998e8;
const double G = 6.674e-11;

double radius(double mass) {
    return (2*G*mass)/(c*c);
}

int main() {
    int mass;
    while (true) {
        cout << "gimmie mass uy wnat pls" << endl;
        cin >> mass;

        double result = radius(mass);
        cout << result << endl;
    }
}