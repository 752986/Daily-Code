#include <SFML/Graphics.hpp>

sf::RenderWindow window(sf::VideoMode(800, 800), "Trees"); //set up screen
sf::CircleShape circle;
sf::RectangleShape rect;

void tree(int x, int y) {
	sf::CircleShape circle;
	sf::RectangleShape rect;

	//trunk
	rect.setPosition(x + 45, y + 30);
	rect.setFillColor(sf::Color(100, 80, 0));
	rect.setSize(sf::Vector2f(20, 100));
	window.draw(rect);

	//left branch
	circle.setRadius(30);
	circle.setFillColor((sf::Color(0, 100, 80)));
	circle.setPosition(x, y + 30);
	window.draw(circle);

	//right branch
	circle.setRadius(30);
	circle.setFillColor((sf::Color(80, 100, 0)));
	circle.setPosition(x + 50, y + 30);
	window.draw(circle);

	//top branch
	circle.setRadius(30);
	circle.setFillColor((sf::Color(0, 100, 0)));
	circle.setPosition(x + 25, y);
	window.draw(circle);
}


int main()
{
	while (window.isOpen())//GAME LOOP--------------------------------
	{
		sf::Event event;
		while (window.pollEvent(event))
		{
			if (event.type == sf::Event::Closed)
				window.close();

		}

		//render section-------------------------------
		window.clear();

		for (int i = 0; i < 800; i += 100) {
			for (int j = 0; j < 800; j += 100) {
				tree(i + (j / 3), j);
			}
		}

		window.display(); //flip the buffer

	}//end game loop-------------------------------------------------



	return 0;
} //end main