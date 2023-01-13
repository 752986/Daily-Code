#include <iostream>
using namespace std;

const float COST = 24.57f;

int main() {
    float answer;
    cout << "How much money do you have? \n> ";
    cin >> answer;

    if (answer < COST) {
        cout << "sorry, you cant afford eggs! have you considered theft?";
    } else if (answer == COST) {
        cout << "congratulations, you can (just barely) buy eggs!";
    } else {
        cout << "congratulations, you can buy eggs! your remaining balance is " << answer - COST;
    }
}