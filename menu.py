import pygame

from additional_functions.button import Button
from additional_functions.board import run
from additional_functions.settings import settings_run


class Menu:
    def __init__(self):
        self.main_font = 'additional_functions/fonts/main.ttf'
        pass

    def run(self):
        pygame.init()
        size = width, height = 700, 500
        # screen — холст, на котором нужно рисовать:
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption('Меню')
        clock = pygame.time.Clock()
        buttons_group = pygame.sprite.Group()
        screen.fill(pygame.color.Color('white'))

        main_text = self.text(self.main_font, 50, 'Шашки Онлайн', 'black')

        print(main_text)
        # создание кнопок
        texts = {i[0]: i[1] for i in enumerate(['Играть', 'Настройки'])}
        buttons = {}
        for i in range(1, len(texts) + 1):
            text = self.text(self.main_font, 50, texts[i - 1], '#c15c0f')
            btn = Button(200, 100 * i, 70, 300, text, '#a04c0b', screen, buttons_group)
            buttons[btn] = texts[i - 1]

        running = True
        while running:
            size = width, height = 700, 500
            screen = pygame.display.set_mode(size)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for but in buttons:
                            if but.onclick(event.pos):
                                text_btn = buttons[but]
                                if text_btn == 'Играть':
                                    run()
                                elif text_btn == 'Настройки':
                                    settings_run()
                    elif event.button == 3:
                        pass

            screen.fill(pygame.color.Color('white'))
            screen.blit(main_text, (width // 2 - (main_text.get_size()[0] // 2), 20))
            buttons_group.draw(screen)
            buttons_group.update()

            pygame.display.flip()

    def text(self, font, size, text, color):
        font = pygame.font.Font(font, size)
        return font.render(text, True, color)


if __name__ == '__main__':
    menu = Menu()
    menu.run()
