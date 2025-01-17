import math
import random

WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 20
MAX_POWER = 30
FRICTION = 0.995
BULLET_SPEED = 15

def player_script(cannon_pos, ball_pos, power_bullet_count, precision_bullet_count, ball_vel):
    cannon_x, cannon_y = cannon_pos
    # Calculate angle and power (example logic)
    # target_x, target_y = WIDTH // 2, HEIGHT // 2
    target_x, target_y = ball_pos
    not_shooting = False
    angle = 0 #implement your logic here
    power = 30
    bullet_type = random.choice(["power", "precision"])
    if not_shooting:
        return None
    return (angle, power, bullet_type)