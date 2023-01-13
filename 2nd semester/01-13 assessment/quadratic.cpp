#include <iostream>
#include <cmath>
using namespace std;

void quadratic(int a, int b, int c) {
    float sub = (-b - sqrtf((b * b) - (4 * a * c))) / (2 * a);
    float add = (-b + sqrtf((b * b) - (4 * a * c))) / (2 * a);

    if (isnan(sub)) {
        cout << "there are no real roots";
    } else if (sub == add) {
        cout << "the root is x = " << sub;
    } else {
        cout << "the roots are x = " << sub << " and x = " << add;
    }
}

int main() {
    int a, b, c;

    cout << "enter the a, b, and c parameters of `ax^2 + bx + c` \n> ";

    cin >> a;
    cin >> b;
    cin >> c;

    quadratic(a, b, c);
}
