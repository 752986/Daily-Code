#include <vector>
#include <cstdio>
#include <random>
#include <ctime>
#include <chrono>
using namespace std;

template <typename T> // generics are weird in c++. also, I learned that the order of function declarations matters (no function hoisting)
void bubbleSort(vector<T> &list) {
    bool swapped;
    // "premature optimization is the root of all evil": the `finished` variable was added later, since I'm trying to make a functional program before I focus on speed
    int finished = 0; // remember how many elements have already been sorted, so we don't check them 
    do {
        swapped = false; // remember whether we made a change, so we don't keep going after the list is already sorted
        for (int i = 0; i < list.size() - 1 - finished; i++) {
            if (list[i] > list[i + 1]) { // if the two items are in the wrong order:
                // swap the two values:
                T temp = list[i + 1];
                list[i + 1] = list[i];
                list[i] = temp;

                swapped = true;
            }
        }
        finished ++;
    } while (swapped);
}

int main()
{
    // initialize our vector and fill it with random values:
    int length = 50000;
    auto a = vector<int>();
    a.reserve(100);
    srand(time(NULL));
    for (int i = 0; i < length; i++) {
        a.push_back(rand() % 100);
    }

    // time how long it took to sort and print the results:
    chrono::time_point<std::chrono::system_clock> start, end;
    start = chrono::system_clock::now();
    bubbleSort(a);
    end = chrono::system_clock::now();
    chrono::duration<double> elapsed_seconds = end - start;
    printf("%d elements, %f secs", length, elapsed_seconds);

    // print the sorted list:
    // for(auto num : a) {
    //     printf("%d\n", num);
    // }
}
