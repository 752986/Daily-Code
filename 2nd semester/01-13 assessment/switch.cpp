#include <iostream>
using namespace std;

int main() {
    bool quit = false;
    while (!quit) {
        char answer;
        cout << "press `d` for dog, `c` for cat, `b` for birb, `e` for eduardo, `q` to quit. \n> ";
        cin >> answer;

        switch (answer) {
        case 'd':
            cout << "woof!" << endl;
            break;
        case 'c':
            cout << "meow!" << endl;
            break;
        case 'b':
            cout << "tweet!" << endl;
            break;
        case 'e':
            cout << "python is cringe because you can't access random memory" << endl;
            break;
        case 'q':
            cout << "goodbye!" << endl;
            quit = true;
            break;
        default:
            cout << "sorry, that's not a valid response." << endl;
            break;
        }
    }
}
