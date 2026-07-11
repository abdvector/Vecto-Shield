import numpy as np
from src.config import NUM_DRONES
class SwarmSimulator:
    def __init__(self, targets, origin):
        self.targets = np.array(targets)
        self.pos = np.array([origin for _ in range(NUM_DRONES)]) + np.random.normal(0, 0.005, (NUM_DRONES, 2))
        self.vel = np.zeros((NUM_DRONES, 2))
    def simulate(self, steps=100):
        frames, dists = [], []
        pbest = self.pos.copy()
        pbest_val = np.full(NUM_DRONES, float('inf'))
        assigned_targets = np.array([self.targets[i % len(self.targets)] for i in range(NUM_DRONES)])
        for _ in range(steps):
            r1, r2 = np.random.rand(NUM_DRONES, 2), np.random.rand(NUM_DRONES, 2)
            # Tuned for slower, smoother geographic convergence
            self.vel = (0.85 * self.vel) + (0.1 * r1 * (pbest - self.pos)) + (0.15 * r2 * (assigned_targets - self.pos))
            self.pos += self.vel * 0.1
            dist = np.linalg.norm(self.pos - assigned_targets, axis=1)
            improved = dist < pbest_val
            pbest[improved], pbest_val[improved] = self.pos[improved], dist[improved]
            frames.append(self.pos.copy())
            dists.append(np.mean(dist))
        return frames, dists
