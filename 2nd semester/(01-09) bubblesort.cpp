#include <vector>
#include <cstdio>
#include <random>
#include <ctime>
#include <chrono>
using namespace std;

template <typename T>
void bubbleSort(vector<T> &list) {
    bool swapped;
    int finished = 0;
    do {
        swapped = false;
        for (int i = 0; i < list.size() - 1 - finished; i++) {
            if (list[i] > list[i + 1]) {
                T temp = list[i + 1];
                list[i + 1] = list[i];
                list[i] = temp;

                swapped = true;
            }
        }
        finished ++;
    } while (swapped);
}

int main() {
    int length = 50000;
    auto a = vector<int>();
    a.reserve(100);
    srand(time(NULL));
    for (int i = 0; i < length; i++) {
        a.push_back(rand() % 100);
    }

    chrono::time_point<std::chrono::system_clock> start, end;
    start = chrono::system_clock::now();
    bubbleSort(a);
    end = chrono::system_clock::now();
    chrono::duration<double> elapsed_seconds = end - start;
    printf("%d elements, %f secs", length, elapsed_seconds);

    // for(auto num : a) {
    //     printf("%d\n", num);
    // }
}
