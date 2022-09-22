#include <iostream>
using namespace std; 
void part1() {
    int age;
    cout << "Please enter your age:" << endl;
    cin >> age;
    if (age == 13) {
        cout << "Too young. Go Away." << endl;
    } else if (age < 18) {
        cout << "Please get parent permission." << endl;
    } else if (age > 40) {
        cout << "This will be run in 8-bit mode for nostalgia!" << endl;
    } else {
        cout << "welcome to the game!" << endl;
    }
}

// part 2:

void part2() { 
    char choice = 'a';
    while (choice != 'q') {
        cout << endl << endl << "Press a to count up to 10, b to count down by 2s, and q to quit." << endl;
        cin >> choice;

        switch (choice) {
        case 'a':
            for (int i = 0; i <= 10; i++)
                cout << i << " ";
            break;
        case 'b':
            for (int i = 20; i > 0; i -= 2)
                cout << i << " ";
            break;
        case 'q':
            cout << "goodbye!" << endl;
        }
    }
}

int main() {
    part1();
    part2();
}