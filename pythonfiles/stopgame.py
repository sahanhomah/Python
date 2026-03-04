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
MAX_TURNS_PER_PLAYER = 5


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

	player_scores = [0, 0]
	player_turns = [0, 0]
	completed_turns = 0
	current_player = 0
	target = make_round()
	running_timer = False
	game_over = False
	start_time = 0.0
	elapsed = 0.0
	last_stopped_time = 0.0
	result_text = "Player 1: Press START to begin"
	result_color = SUBTEXT

	game_running = True
	while game_running:
		clock.tick(FPS)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_running = False

			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				if start_button.collidepoint(event.pos) and not running_timer and not game_over:
					elapsed = 0.0
					start_time = time.perf_counter()
					running_timer = True
					result_text = f"Player {current_player + 1}: Timer running... click STOP"
					result_color = SUBTEXT

				if stop_button.collidepoint(event.pos) and running_timer:
					elapsed = time.perf_counter() - start_time
					last_stopped_time = elapsed
					running_timer = False

					delta = abs(elapsed - target)
					if delta <= TOLERANCE:
						round_score = max(0, int((TOLERANCE - delta) * 1000))
						player_scores[current_player] += round_score
						result_text = f"Player {current_player + 1}: +{round_score} points"
						result_color = GREEN
					else:
						result_text = f"Player {current_player + 1}: Missed target time"
						result_color = RED

					completed_turns += 1
					player_turns[current_player] += 1
					if player_turns[0] >= MAX_TURNS_PER_PLAYER and player_turns[1] >= MAX_TURNS_PER_PLAYER:
						game_over = True
						if player_scores[0] > player_scores[1]:
							result_text = "Game Over: Player 1 wins!"
							result_color = GREEN
						elif player_scores[1] > player_scores[0]:
							result_text = "Game Over: Player 2 wins!"
							result_color = GREEN
						else:
							result_text = "Game Over: It's a tie!"
							result_color = BLUE
					else:
						current_player = 1 - current_player
						target = make_round()

		current_time = time.perf_counter() - start_time if running_timer else last_stopped_time

		screen.fill(BG)
		pygame.draw.rect(screen, PANEL, (40, 40, 680, 280), border_radius=16)

		draw_text(screen, "Stop The Timer", title_font, TEXT, 250, 52)
		draw_text(screen, f"Turn: {min(completed_turns + 1, MAX_TURNS_PER_PLAYER * 2)}/{MAX_TURNS_PER_PLAYER * 2}", small_font, SUBTEXT, 70, 118)
		draw_text(screen, f"Current: Player {current_player + 1}", small_font, SUBTEXT, 250, 118)
		draw_text(screen, f"P1: {player_scores[0]} ({player_turns[0]}/{MAX_TURNS_PER_PLAYER})", small_font, SUBTEXT, 470, 95)
		draw_text(screen, f"P2: {player_scores[1]} ({player_turns[1]}/{MAX_TURNS_PER_PLAYER})", small_font, SUBTEXT, 470, 125)
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

		start_color = SUBTEXT if game_over else GREEN
		draw_button(screen, start_button, "START", font, start_color)
		draw_button(screen, stop_button, "STOP", font, RED)

		pygame.display.flip()

	pygame.quit()


if __name__ == "__main__":
	main()
