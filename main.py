import sys
import pygame
import time
import random
import os
import numpy as np

pygame.init()

color1 = (128, 128, 128)
color2 = (200, 200, 200)
block_color = {
    0: (205, 193, 180),
    2: (204, 255, 255),
    4: (0, 204, 255),
    8: (204, 255, 204),
    16: (153, 204, 255),
    32: (51, 153, 255),
    64: (0, 102, 204),
    128: (204, 255, 255),
    256: (153, 153, 255),
    512: (0, 204, 255),
    1024: (204, 255, 255),
    2048: (51, 204, 204),
    4096: (204, 255, 204),
    8192: (204, 255, 204),
    16384: (204, 255, 204),
    32768: (204, 255, 204)
}
num_color = {
    0: (205, 193, 180),
    2: (220, 220, 220),
    4: (220, 220, 220),
    8: (220, 220, 220),
    16: (220, 220, 220),
    32: (220, 220, 220),
    64: (220, 220, 220),
    128: (220, 220, 220),
    256: (220, 220, 220),
    512: (220, 220, 220),
    1024: (220, 220, 220),
    2048: (220, 220, 220),
    4096: (220, 220, 220),
    8192: (220, 220, 220),
    16384: (220, 220, 220),
    32768: (220, 220, 220)
}


class _2048:
    def __init__(self):
        self.step_sum = 0
        self.matrix = np.array([[0, 0, 0, 0],
                                [0, 0, 0, 0],
                                [0, 0, 0, 0],
                                [0, 0, 0, 0]])
        self.score = 0
        self.screen_image = pygame.display.set_mode((420, 640))
        self.title_text = ''
        self.score_text = ''
        self.score_text2 = ''
        self.text = ''
        self.success = False
        self.game_over = False
        self.add_num = True

    def start_game(self):
        pygame.init()
        pygame.display.set_caption('2048')

        self.screen_image.fill((220, 220, 220))

    def screen_setting(self):
        pygame.font.get_fonts()
        self.title_text = pygame.font.SysFont('宋体', 61, True)  # 填充标题文字
        title_text = self.title_text.render('~2048~', True, (205, 193, 180))
        self.screen_image.blit(title_text, (125, 10))

        pygame.draw.rect(self.screen_image, (220, 220, 220), (250, 45, 180, 120))
        self.score_text = pygame.font.SysFont('幼圆', 30, True)  # 填充分数文字
        self.score_text2 = pygame.font.SysFont('幼圆', 28, True)
        score_text = self.score_text.render('分 数:', True, (0, 0, 0))
        self.screen_image.blit(score_text, (220, 50))

        game_score = self.score_text2.render(str(self.score), True, (205, 195, 100))  # 填充分数
        self.screen_image.blit(game_score, (330, 50))

        for i in range(4):  # 填充背景方块
            for j in range(4):
                x = j * 80 + (j + 1) * 10
                y = i * 80 + (i + 1) * 10
                pygame.draw.rect(self.screen_image, block_color[int(self.matrix[i][j])], (x + 10, y + 105, 85, 85),
                                 border_radius=10)

                if self.matrix[i][j] < 10:  # 填充字体
                    self.text = pygame.font.SysFont('幼圆', 46, True)
                    num_text = self.text.render(str(self.matrix[i][j]), True, num_color[self.matrix[i][j]])
                    self.screen_image.blit(num_text, (x + 35, y + 120))
                elif self.matrix[i][j] < 100:
                    self.text = pygame.font.SysFont('幼圆', 40, True)
                    num_text = self.text.render(str(self.matrix[i][j]), True, num_color[self.matrix[i][j]])
                    self.screen_image.blit(num_text, (x + 25, y + 120))
                elif self.matrix[i][j] < 1000:
                    self.text = pygame.font.SysFont('幼圆', 34, True)
                    num_text = self.text.render(str(self.matrix[i][j]), True, num_color[self.matrix[i][j]])
                    self.screen_image.blit(num_text, (x + 15, y + 120))
                else:
                    self.text = pygame.font.SysFont('幼圆', 28, True)
                    num_text = self.text.render(str(self.matrix[i][j]), True, num_color[self.matrix[i][j]])
                    self.screen_image.blit(num_text, (x + 6, y + 120))

    def init_game(self):
        self.score = 0
        self.game_over = False
        self.success = False
        self.step_sum = 0
        self.matrix = np.array([[0, 0, 0, 0],
                                [0, 0, 0, 0],
                                [0, 0, 0, 0],
                                [0, 0, 0, 0]])
        for i in range(2):
            self.add_num = True
            self.create_num()

    def create_num(self):
        list1 = []
        for i in range(4):
            for j in range(4):
                if self.matrix[i][j] == 0:
                    list1.append([i, j])
        if list1 and self.add_num:
            value = 4 if random.randint(0, 6) % 3 == 0 else 2
            x, y = random.sample(list1, 1)[0]
            self.matrix[x][y] = value
            self.add_num = False

    def move_up(self):
        for j in range(4):
            k = 0
            for i in range(1, 4):
                if self.matrix[i][j] > 0:
                    if self.matrix[i][j] == self.matrix[k][j]:
                        self.score += self.matrix[k][j] * 2
                        self.matrix[k][j] *= 2
                        self.matrix[i][j] = 0
                        k += 1
                        self.add_num = True
                    elif self.matrix[k][j] == 0:
                        self.matrix[k][j] = self.matrix[i][j]
                        self.matrix[i][j] = 0
                        self.add_num = True
                    else:
                        k += 1
                        if self.matrix[k][j] == 0:
                            self.matrix[k][j] = self.matrix[i][j]
                            self.matrix[i][j] = 0
                            self.add_num = True
        self.step_sum += 1

    def move_down(self):
        for j in range(4):
            k = 3
            for i in range(2, -1, -1):
                if self.matrix[i][j] > 0:
                    if self.matrix[i][j] == self.matrix[k][j]:
                        self.score += self.matrix[i][j] * 2
                        self.matrix[k][j] *= 2
                        self.matrix[i][j] = 0
                        k -= 1
                        self.add_num = True
                    elif self.matrix[k][j] == 0:
                        self.matrix[k][j] = self.matrix[i][j]
                        self.matrix[i][j] = 0
                        self.add_num = True
                    else:
                        k -= 1
                        if self.matrix[k][j] == 0:
                            self.matrix[k][j] = self.matrix[i][j]
                            self.matrix[i][j] = 0
                            self.add_num = True
        self.step_sum += 1

    def move_left(self):
        self.matrix = self.matrix.T
        self.move_up()
        self.matrix = self.matrix.T

    def move_right(self):
        self.matrix = self.matrix.T
        self.move_down()
        self.matrix = self.matrix.T

    def judge_success(self):
        for i in range(4):
            for j in range(4):
                if self.matrix[i][j] == 32768:
                    self.success = True
                    return True
        return False

    def print_game_over(self):
        over_font = pygame.font.SysFont("simsunnsimsun", 60, True)
        str_text = over_font.render('Game Over!', True, (255, 255, 255))
        self.screen_image.blit(str_text, (45, 520))

    def judge_fail(self):
        for i in range(4):
            for j in range(4):
                if self.matrix[i][j] == 0:
                    return False
        for i in range(3):
            for j in range(3):
                if self.matrix[i][j] == self.matrix[i][j + 1]:
                    return False
                elif self.matrix[i][j] == self.matrix[i + 1][j]:
                    return False
            if self.matrix[3][i] == self.matrix[3][i + 1]:
                return False
            elif self.matrix[i][3] == self.matrix[i + 1][3]:
                return False
        self.game_over = True
        return True

    def print_success(self):
        success_font = pygame.font.SysFont("simsunnsimsun", 60, True)
        str_text = success_font.render('Successful!', True, (178, 34, 34))
        self.screen_image.blit(str_text, (50, 520))


def step_sum(game: _2048):
    smooth = 0
    sora = 0
    single = 0
    matrix = game.matrix
    for m in range(4):
        random_num = random.randint(1, 4)
        if random_num == 1:
            game.move_up()
        elif random_num == 2:
            game.move_down()
        elif random_num == 3:
            game.move_left()
        elif random_num == 4:
            game.move_right()
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 0:
                sora += 1
    for i in range(3):
        for j in range(3):
            smooth += (matrix[i][j + 1] - matrix[i][j])
            smooth += (matrix[i + 1][j] - matrix[i][j])
        smooth += (matrix[3][i + 1] - matrix[3][i])
        smooth += (matrix[i + 1][3] - matrix[i + 1][3])
    smooth *= (-1)
    for i in range(4):
        matrix = game.matrix
        if matrix[i][1] < 0:
            if matrix[i][2] < 0:
                if matrix[i][3] < 0:
                    if matrix[i][0] < 0:
                        single += 1
        if matrix[1][i] < 0:
            if matrix[2][i] < 0:
                if matrix[3][i] < 0:
                    if matrix[0][i] < 0:
                        single += 1
        if matrix[i][1] > 0:
            if matrix[i][2] > 0:
                if matrix[i][3] > 0:
                    if matrix[i][0] > 0:
                        single += 1
        if matrix[1][i] > 0:
            if matrix[2][i] > 0:
                if matrix[3][i] > 0:
                    if matrix[0][i] > 0:
                        single += 1
    return 20 * single + 20 * sora + 5 * smooth


def step_study(game: _2048, n):
    sum = 0
    for i in range(n):
        x = game
        temp = step_sum(x)
        sum += temp
    return sum / n


def markov(game1: _2048, C=0.008):
    for m_event in pygame.event.get():
        if m_event.type == pygame.QUIT:
            sys.exit()
    while not game1.game_over or not game1.judge_success():
        for m_event in pygame.event.get():
            if m_event.type == pygame.QUIT:
                sys.exit()
        temp = game1
        temp.move_up()
        step_up = step_study(temp, 60)
        score_up = temp.score - game1.score
        value_up = step_up + C * score_up

        temp = game1
        temp.move_down()
        step_down = step_study(temp, 60)
        score_down = temp.score - game1.score
        value_down = step_down + C * score_down

        temp = game1
        temp.move_left()
        step_left = step_study(temp, 60)
        score_left = temp.score - game1.score
        value_left = step_left + C * score_left

        temp = game1
        temp.move_right()
        step_right = step_study(temp, 60)
        score_right = temp.score - game1.score
        value_right = step_left + C * score_right

        game_over_0 = game1.judge_fail()
        if game_over_0:
            game1.print_game_over()

        value_max = max(value_right, value_down, value_left, value_up)
        if value_max == value_up:
            game1.move_up()
        elif value_max == value_down:
            game1.move_down()
        elif value_max == value_left:
            game1.move_left()
        else:
            game1.move_right()
        mygame.screen_setting()
        is_success_0 = game1.judge_success()
        if is_success_0:
            game1.game_over = True
            game1.print_success()

        game1.create_num()
        pygame.display.flip()


while True:
    mygame = _2048()
    mygame.start_game()
    mygame.init_game()
    start_screen = pygame.display.set_mode((420, 640))
    start_image = pygame.image.load('./source/start_image.jpeg')
    start_screen.blit(start_image, (0, 0))
    start_title_text = pygame.font.SysFont('宋体', 80, True)  # 填充标题文字
    title_text = start_title_text.render('~2048~', True, (204, 204, 204))
    start_screen.blit(title_text, (75, 240))
    pygame.draw.rect(start_screen, (255, 255, 255), (100, 400, 285, 30))
    pygame.draw.rect(start_screen, (255, 255, 255), (100, 450, 285, 30))
    start_text = pygame.font.SysFont('幼圆', 20, True)
    people_text = start_text.render('print 1 start game', True, (0, 0, 0))
    start_screen.blit(people_text, (120, 405))
    computer_text = start_text.render('print 2 automatic game', True, (0, 0, 0))
    start_screen.blit(computer_text, (120, 455))
    pygame.display.update()
    my_keys_list = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if my_keys_list[pygame.K_1]:
        mygame.start_game()
        mygame.init_game()
        while True:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.K_ESCAPE:
                    mygame.init_game()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and mygame.judge_fail() == False:
                        mygame.move_up()
                    if event.key == pygame.K_DOWN and mygame.judge_fail() == False:
                        mygame.move_down()
                    if event.key == pygame.K_LEFT and mygame.judge_fail() == False:
                        mygame.move_left()
                    if event.key == pygame.K_RIGHT and mygame.judge_fail() == False:
                        mygame.move_right()
            mygame.screen_setting()
            mygame.create_num()
            game_over = mygame.judge_fail()
            if game_over:
                mygame.print_game_over()

            is_success = mygame.judge_success()
            if is_success:
                mygame.print_success()

            pygame.display.flip()
    elif my_keys_list[pygame.K_2]:
        mygame.start_game()
        mygame.init_game()
        while True:
            for m_event in pygame.event.get():
                if m_event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.update()
            markov(mygame)
            mygame.screen_setting()
            pygame.display.update()
