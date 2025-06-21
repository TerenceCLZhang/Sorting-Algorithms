import pygame
import pygame_menu as pm
import sys
from visualizer import visualize
from constants import WIDTH, HEIGHT, CAPTION, FPS, COLORS


class Visualizer:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(CAPTION)
        self.clock = pygame.time.Clock()

        # Fonts
        self.font_name = pygame.font.match_font(
            "Courier New") or pygame.font.get_default_font()
        self.fonts = {
            "title": pygame.font.Font(self.font_name, 35),
            "regular": pygame.font.Font(self.font_name, 20),
        }

        self.state_manager = StateManager("main_menu")
        self.main_menu = MainMenu(self.screen, self.state_manager, self.fonts)

        self.states = {
            "main_menu": self.main_menu,
        }

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            self.states[self.state_manager.get_state()].run()

            pygame.display.update()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()


class StateManager:
    def __init__(self, current_state):
        self.current_state = current_state

    def get_state(self):
        return self.current_state

    def set_state(self, new_state):
        self.current_state = new_state


class Scene:
    def __init__(self, display, state_manager, fonts):
        self.display = display
        self.state_manager = state_manager
        self.fonts = fonts

    def run(self):
        pass


class MainMenu(Scene):
    def __init__(self, display, state_manager, fonts):
        super().__init__(display, state_manager, fonts)

    def run(self):
        text_title = self.fonts["title"].render(
            "Sorting Algorithm Visualizer", True, COLORS["regular"])
        textbox_title = text_title.get_rect(topleft=(10, 10))
        self.display.blit(text_title, textbox_title)

        text_label_algorithm = self.fonts["regular"].render(
            "Choose an algorithm:", True, COLORS["regular"])
        textbox_text_label_algorithm = text_label_algorithm.get_rect(
            topleft=(10, 65))
        self.display.blit(text_label_algorithm, textbox_text_label_algorithm)


if __name__ == "__main__":
    # visualize("comb", n=100)
    visualiser = Visualizer()
    visualiser.run()
