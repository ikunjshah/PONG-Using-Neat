# PyPong: AI-Driven Ping Pong Game

![PyPong Demo](demo.gif)

PyPong is a classic ping pong game implemented using the Pygame library in Python. What sets PyPong apart is its AI opponent, powered by the NEAT (NeuroEvolution of Augmenting Topologies) framework, which learns and adapts to your gameplay style. Play against the AI, challenge yourself, and witness the AI evolve and improve over time.

## Features

- Classic ping pong gameplay with intuitive controls.
- AI opponent that utilizes the NEAT framework to learn and adapt to your gameplay.
- Smooth and visually pleasing graphics powered by Pygame.
- Option to play against a friend or challenge the AI to a match.
- Real-time game statistics and fitness scores for AI evaluation.

## Getting Started

1. Clone this repository to your local machine using `git clone https://github.com/ikunjshah/PONG-Using-Neat.git`
2. Install the required dependencies using `pip install -r requirements.txt`
3. Run the game using `python main.py`

## How It Works

The AI in PyPong is powered by the NEAT framework, which uses evolutionary algorithms to train neural networks. Here's how it works:

1. Multiple neural networks, representing different AI players, are created with varying structures.
2. These networks are evaluated by playing the game against each other and human players.
3. The AI players that perform well are selected to reproduce, creating the next generation of networks.
4. Over generations, the neural networks evolve and improve their performance in the game.

## Contributing

Contributions are welcome! If you find any bugs or have ideas for enhancements, feel free to open an issue or submit a pull request. Make sure to follow the [code of conduct](CODE_OF_CONDUCT.md).

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- Pygame: [https://www.pygame.org/](https://www.pygame.org/)
- NEAT: [https://neat-python.readthedocs.io/en/latest/](https://neat-python.readthedocs.io/en/latest/)
