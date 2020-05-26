import random

import pygame

pygame.init()


class Bar:
    def __init__(self, x, y, height):
        self.x = x
        self.y = y
        self.height = height
        self.color = (255, 255, 255)


class Chart:
    def __init__(self, bars):
        self.bars = bars

    def add_bar(self, bar):
        self.bars.append(bar)

    def print_bars(self):
        arr = []
        for i in self.bars:
            arr.append(i.height)
        print(arr)

    def draw_chart(self, window):
        for bar in self.bars:
            pygame.draw.rect(window, bar.color, (bar.x, bar.y, 1000 / len(self.bars) - 1, -bar.height))

        pygame.draw.line(window, (255, 255, 255), (0, 400), (1000, 400))


def bubble_sort(window, chart):
    for i in range(len(chart.bars) - 1):
        for j in range(0, len(chart.bars) - i - 1):
            chart.bars[j].color = (0, 255, 0)
            chart.bars[j + 1].color = (255, 0, 0)
            if chart.bars[j].height > chart.bars[j + 1].height:
                chart.bars[j].height, chart.bars[j + 1].height = chart.bars[j + 1].height, chart.bars[j].height
            redraw_window(window, chart)
            pygame.time.wait(1)
            pygame.display.flip()
            chart.bars[j].color, chart.bars[j + 1].color = (255, 255, 255), (255, 255, 255)


def selection_sort(window, chart):
    for i in range(len(chart.bars)):
        min_index = i
        for j in range(i + 1, len(chart.bars)):
            if chart.bars[min_index].height > chart.bars[j].height:
                min_index = j

        chart.bars[i].color = (0, 255, 0)
        chart.bars[min_index].color = (255, 0, 0)
        chart.bars[i].height, chart.bars[min_index].height = chart.bars[min_index].height, chart.bars[i].height
        redraw_window(window, chart)
        pygame.time.wait(50)
        pygame.display.flip()

        chart.bars[i].color, chart.bars[min_index].color = (255, 255, 255), (255, 255, 255)


def insertion_sort(window, chart):
    for i in range(1, len(chart.bars)):
        key = chart.bars[i].height
        j = i - 1
        while j >= 0 and key < chart.bars[j].height:
            chart.bars[j + 1].height = chart.bars[j].height
            j -= 1
        chart.bars[j + 1].height = key

        chart.bars[j].color = (0, 255, 0)
        chart.bars[j + 1].color = (255, 0, 0)

        redraw_window(window, chart)
        pygame.time.wait(50)
        pygame.display.flip()
        chart.bars[j].color, chart.bars[j + 1].color = (255, 255, 255), (255, 255, 255)


def create_rand_bars(num_of_bars, window_width):
    arr = []
    x_coord = 5
    for i in range(num_of_bars):
        height = random.randint(0, 300)
        arr.append(Bar(x_coord, 400, height))
        x_coord += window_width / num_of_bars
    return arr


def redraw_window(window, chart):
    window.fill((0, 0, 0))
    chart.draw_chart(window)
    font = pygame.font.SysFont("Helvetica", 30)

    text = pygame.font.SysFont("Helvetica", 25).render("-10 Bars", 1, (255, 255, 255))
    window.blit(text, (200, 0))

    text = font.render("Randomize", 1, (255, 255, 255))
    window.blit(text, (450, 0))

    text = pygame.font.SysFont("Helvetica", 25).render("+10 Bars", 1, (255, 255, 255))
    window.blit(text, (700, 0))

    text = font.render("Selection Sort", 1, (255, 255, 255))
    window.blit(text, (200, 450))

    text = font.render("Bubble Sort", 1, (255, 255, 255))
    window.blit(text, (450, 450))

    text = font.render("Insertion Sort", 1, (255, 255, 255))
    window.blit(text, (700, 450))

def main():
    window = pygame.display.set_mode((1000, 500))
    pygame.display.set_caption("Algorithm Visualiser")
    run = True
    chart = Chart(create_rand_bars(50, 1000))
    num_of_bars = 50
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                print(position)
                if 450 < position[0] < 580 and 0 < position[1] < 30:
                    chart = Chart(create_rand_bars(num_of_bars, 1000))
                if 200 < position[0] < 360 and 450 < position[1] < 490:
                    selection_sort(window, chart)
                if 450 < position[0] < 600 and 450 < position[1] < 490:
                    bubble_sort(window, chart)
                if 700 < position[0] < 850 and 450 < position[1] < 490:
                    insertion_sort(window, chart)
                if 200 < position[0] < 280 and 0 < position[1] < 30:
                    num_of_bars -= 10
                    chart = Chart(create_rand_bars(num_of_bars, 1000))
                if 700 < position[0] < 780 and 0 < position[1] < 30:
                    num_of_bars += 10
                    chart = Chart(create_rand_bars(num_of_bars, 1000))
        redraw_window(window, chart)
        pygame.display.flip()


main()
