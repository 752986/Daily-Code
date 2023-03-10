#include <iostream>
using namespace std;

class Pizza {
public:
    int toppings;
    bool isBaked;


    float getPrice() {
        return 10 + (2 * toppings);
    }

    void addTopping() {
        toppings += 1;
    }

    void bake() {
        isBaked = true;
    }
    
    void printInfo() {
        cout << "A " << (isBaked ? "baked" : "unbaked") << " pizza with " << toppings << " toppings. It's worth $" << getPrice() << "." << endl;
    }


    Pizza() {
        isBaked = false;
        toppings = 0.0;
    }
};

int main() {
    Pizza pizza = Pizza();
    cout << "base pizza: ";
    pizza.printInfo();
    pizza.addTopping();
    pizza.addTopping();
    pizza.bake();
    cout << "after toppings + bake: ";
    pizza.printInfo();
}