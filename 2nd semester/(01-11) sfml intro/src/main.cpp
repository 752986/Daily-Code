#include <SFML/Graphics.hpp>

int main() {
    sf::RenderWindow window(sf::VideoMode(800, 800), "SFML Circles");
    sf::CircleShape circle;

    while (window.isOpen()) {
        sf::Event e;
        while (window.pollEvent(e)) {
            if (e.type == sf::Event::Closed) {
                window.close();
            }
        }

        circle.setRadius(50);
        circle.setFillColor(sf::Color(200, 50, 50));
        circle.setPosition(400, 400);

        window.draw(circle);
        window.display();
    }
    
    return 0;
}