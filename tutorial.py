import pygame
from pong import Game
import neat
import os
import pickle

class PongGame:
    def __init__(self, window, width, height):
        self.game = Game(window, width, height)
        self.ball = self.game.ball
        self.left_paddle = self.game.left_paddle
        self.right_paddle = self.game.right_paddle
    
    def test_ai(self, genome, config):
        net = neat.nn.FeedForwardNetwork.create(genome, config) 
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(60)
            self.game.width, self.game.height = 700, 500
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.game.move_paddle(left=True, up=True)
            elif keys[pygame.K_s]:
                self.game.move_paddle(left=True, up=False)

            output = net.activate((self.right_paddle.y, self.ball.y, abs(self.right_paddle.x - self.ball.x)))
            decision = output.index(max(output))
            if decision == 0:
                pass
            if decision == 1:
                self.game.move_paddle(left=False, up=True)
            else:
                self.game.move_paddle(left=False, up=False)

            game_info = self.game.loop()
            print(game_info.left_score, game_info.right_score)
            self.game.loop()
            self.game.draw(True, False)
            pygame.display.update() 

            if game_info.left_score >= 10 or game_info.right_score >= 10 or game_info.left_hits > 50:
                #print which player won in the game window  
                pygame.font.init()
                font = pygame.font.SysFont(None, 50, (255, 255, 255))
                if game_info.left_score >= 10:
                    text = font.render("Left Player Wins!", True, (255, 255, 255))
                elif game_info.right_score >= 10:
                    text = font.render("Right Player Wins!", True, (255, 255, 255))
                #take some time to show the score
                text_rect = text.get_rect()
                text_rect.center = (self.game.width // 2, self.game.height // 2)
                self.game.window.blit(text, text_rect)
                pygame.display.update()
                pygame.time.delay(3000)
                break

        pygame.quit()

    def train_ai(self, genome1, genome2, config):
        net1 = neat.nn.FeedForwardNetwork.create(genome1, config)
        net2 = neat.nn.FeedForwardNetwork.create(genome2, config)

        run = True
        while run:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()
            output1 = net1.activate((self.left_paddle.y, self.ball.y, abs(self.left_paddle.x - self.ball.x)))
            decision1 = output1.index(max(output1))
            if decision1 ==0:
                pass
            if decision1 == 1:
                self.game.move_paddle(left=True, up=True) 
            else:
                self.game.move_paddle(left=True, up=False)

            output2 = net2.activate((self.right_paddle.y, self.ball.y, abs(self.right_paddle.x - self.ball.x)))
            decision2 = output2.index(max(output2))
            if decision2 == 0:
                pass
            if decision2 == 1:
                self.game.move_paddle(left=False, up=True)
            else:
                self.game.move_paddle(left=False, up=False)

            game_info = self.game.loop()

            self.game.draw()
            pygame.display.update()

            if game_info.left_score >= 1 or game_info.right_score >= 1 or game_info.left_hits > 50:
                break
    
        def calculate_fitness(self, genome1, genome2):
            genome1.fitness += game_info.left_hits
            genome2.fitness += game_info.right_hits



def eval_genomes(genomes, config):
    width, height = 700, 500
    window = pygame.display.set_mode((width, height))

    for i, (genome_id, genome1) in enumerate(genomes):
        if i == len(genomes) - 1:
            break
        genome1.fitness = 0 
        for genome_id2, genome2 in genomes[i+1:]:
            genome2.fitness = 0 if genome2.fitness is None else genome2.fitness
            game = PongGame(window, width, height)
            game.train_ai(genome1, genome2, config)


def run_neat(config):
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(1))

    winner = p.run(eval_genomes, 50)
    with open("best.pickle", "wb") as f:
        pickle.dump(winner, f)

def test_ai(config):
    width, height = 700, 500
    window = pygame.display.set_mode((width, height))
    with open("best.pickle", "rb") as f:
        winner = pickle.load(f)

    game = PongGame(window, width, height)
    game.test_ai(winner, config)

if __name__=="__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config.txt")
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)
    #run_neat(config)
    test_ai(config)