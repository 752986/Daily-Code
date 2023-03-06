#include <iostream>
using namespace std;

enum class CarType { 
    Engine, 
    Tanker, 
    Box, 
    Passenger, 
    Caboose,
};

class Car {
public:
    int CarNumber;
    CarType cartype;
    Car* next;

    Car(int number, CarType type);
};

Car::Car(int number, CarType type) {
    CarNumber = number;
    cartype = type;
    next = nullptr;
}

class Train {
public:
    Car* head;

    Train();
    Train(Car* head);
    void addFront(Car* new_car);
    bool insert(Car* after, Car* new_car);
    void print();
};

Train::Train() {
    head = nullptr;
}

Train::Train(Car* front) {
    head = front;
}

/// @brief Makes `new_car` the new head of the linked list
/// @param new_car: The car that will become the new head
void Train::addFront(Car* new_car) {
    new_car->next = head;
    head = new_car;
}

/// @brief Inserts a new car in the middle of the list
/// @param after: The new car will be inserted after this one
/// @param new_car: The car to be inserted
/// @return Whether or not the car was inserted; if `after` is not in the train this returns false
bool Train::insert(Car* after, Car* new_car) {
    Car* current = head;
    while (current->next != nullptr && current != after) {
        current = current->next;
    }
    if (current == after) {
        Car* next_next = current->next;
        current->next = new_car;
        new_car->next = next_next;
        return true;
    } 
    // we reached the end without finding `after`
    return false;
}

/// @brief Prints the train to stdout
void Train::print() {
    Car* current = head;
    cout << "[" << endl;
    while (current != nullptr) {
        string car_type;
        switch (current->cartype) {
        case CarType::Engine:
            car_type = "Engine";
            break;
        case CarType::Tanker:
            car_type = "Tanker";
            break;
        case CarType::Box:
            car_type = "Box";
            break;
        case CarType::Passenger:
            car_type = "Passenger";
            break;
        case CarType::Caboose:
            car_type = "Caboose";
            break;
        }
        cout << "  " << car_type << endl;
        current = current->next;
    }
    cout << "]" << endl;
}


int main() {
    Car* box = new Car(36, CarType::Box);
    Car* tanker = new Car(10, CarType::Tanker);
    Train* train = new Train(box);
    train->addFront(tanker);
    train->addFront(new Car(3, CarType::Engine));
    train->insert(tanker, new Car(97, CarType::Passenger));
    train->insert(box, new Car(64, CarType::Caboose));
    train->print();
}

/* 
definitions:
`enum`: a way to name specific values of an int
`*`: "pointer to" or "dereference"
`**`: "double pointer"
`->`: "access from inside pointer"
`&`: "address of"
*/