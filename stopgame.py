import random
import time

import pygame


WIDTH, HEIGHT = 760, 460
FPS = 60

BG = (22, 24, 28)
PANEL = (36, 40, 46)
TEXT = (240, 244, 248)
SUBTEXT = (170, 180, 192)
GREEN = (46, 196, 130)
RED = (230, 92, 92)
BLUE = (75, 132, 255)

TOLERANCE = 0.30


def make_round():
	target = random.uniform(3.0, 8.0)
	return target


def draw_text(screen, text, font, color, x, y):
	surface = font.render(text, True, color)
	screen.blit(surface, (x, y))


def draw_button(screen, rect, label, font, color):
	pygame.draw.rect(screen, color, rect, border_radius=10)
	pygame.draw.rect(screen, (0, 0, 0), rect, width=2, border_radius=10)
	text_surface = font.render(label, True, (255, 255, 255))
	screen.blit(text_surface, text_surface.get_rect(center=rect.center))


def main():
	pygame.init()
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Stop The Timer - Pygame")
	clock = pygame.time.Clock()

	title_font = pygame.font.SysFont("Segoe UI", 36, bold=True)
	font = pygame.font.SysFont("Segoe UI", 26)
	small_font = pygame.font.SysFont("Segoe UI", 22)

	start_button = pygame.Rect(130, 350, 200, 60)
	stop_button = pygame.Rect(430, 350, 200, 60)

	total_score = 0
	round_number = 1
	target = make_round()
	running_timer = False
	start_time = 0.0
	elapsed = 0.0
	result_text = "Press START to begin"
	result_color = SUBTEXT

	game_running = True
	while game_running:
		clock.tick(FPS)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_running = False

			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				if start_button.collidepoint(event.pos) and not running_timer:
					if elapsed > 0:
						round_number += 1
						target = make_round()
						elapsed = 0.0
					start_time = time.perf_counter()
					running_timer = True
					result_text = "Timer running... click STOP"
					result_color = SUBTEXT

				if stop_button.collidepoint(event.pos) and running_timer:
					elapsed = time.perf_counter() - start_time
					running_timer = False

					delta = abs(elapsed - target)
					if delta <= TOLERANCE:
						round_score = max(0, int((TOLERANCE - delta) * 1000))
						total_score += round_score
						result_text = f"Great! +{round_score} points"
						result_color = GREEN
					else:
						result_text = "Missed target time"
						result_color = RED

		current_time = time.perf_counter() - start_time if running_timer else elapsed

		screen.fill(BG)
		pygame.draw.rect(screen, PANEL, (40, 40, 680, 280), border_radius=16)

		draw_text(screen, "Stop The Timer", title_font, TEXT, 250, 52)
		draw_text(screen, f"Round: {round_number}", small_font, SUBTEXT, 70, 118)
		draw_text(screen, f"Score: {total_score}", small_font, SUBTEXT, 570, 118)
		draw_text(
			screen,
			f"Target: {target:.2f}s",
			font,
			TEXT,
			280,
			165,
		)
		if running_timer:
			draw_text(screen, "Timer: ???", title_font, BLUE, 250, 215)
		else:
			draw_text(screen, f"Timer: {current_time:.3f}s", title_font, BLUE, 240, 215)
		draw_text(screen, result_text, small_font, result_color, 235, 285)

		draw_button(screen, start_button, "START", font, GREEN)
		draw_button(screen, stop_button, "STOP", font, RED)

		pygame.display.flip()

	pygame.quit()


if __name__ == "__main__":
	main()
