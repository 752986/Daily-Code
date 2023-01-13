#define SDL_MAIN_HANDLED
#include <SDL2/SDL.h>

int main() {
    // sf::RenderWindow window(sf::VideoMode(800, 800), "SFML Circles");
    // sf::CircleShape circle;

    // while (window.isOpen()) {
    //     sf::Event e;
    //     while (window.pollEvent(e)) {
    //         if (e.type == sf::Event::Closed) {
    //             window.close();
    //         }
    //     }

    //     circle.setRadius(50);
    //     circle.setFillColor(sf::Color(200, 50, 50));
    //     circle.setPosition(400, 400);

    //     window.draw(circle);
    //     window.display();
    // }

    SDL_Window* window;
    SDL_Surface* surface;

    SDL_Init(SDL_INIT_VIDEO);

    window = SDL_CreateWindow("SDL Tutorial", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, 1200, 800, SDL_WINDOW_SHOWN);

    return 0;
}