import pygame, random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
	def __init__(self, x: float, y: float, radius: float) -> None:
		super().__init__(x, y, radius)

	def draw(self, screen: pygame.Surface) -> None:
		pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

	def update(self, dt: float) -> None:
		self.position += (self.velocity * dt)

	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return

		log_event("asteroid_split")
		new_angle: float = random.uniform(20, 50)
		new_velocity1: pygame.Vector2 = self.velocity.rotate(new_angle) * 1.2
		new_velocity2: pygame.Vector2 = self.velocity.rotate(-1 * new_angle) * 1.2
		new_radius = self.radius - ASTEROID_MIN_RADIUS
		new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
		new_asteroid1.velocity = new_velocity1
		new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
		new_asteroid2.velocity = new_velocity2

