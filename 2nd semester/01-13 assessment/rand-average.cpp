#include <random>
#include <iostream>
#include <ctime>
#include <windows.h>
using namespace std;

int main() {
    srand(time(NULL));

    int number;
    float sum = 0;
    float n = 0;

    while (number != 75) {
        number = (rand() % 50) + 50;

        sum += number;
        n++;

        cout << number << endl;
    }
    cout << "average: " << sum / n;
    Beep(4000, 15000);
}
