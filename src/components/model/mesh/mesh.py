import trimesh
import numpy as np
from OpenGL.GL import *


class Mesh:
    def __init__(self, path, scale=0.05):
        self.scale = scale

        scene = trimesh.load(path)

        if isinstance(scene, trimesh.Scene):
            self.mesh = trimesh.util.concatenate(scene.dump())
        else:
            self.mesh = scene

        self.vertices = np.array(self.mesh.vertices, np.float32)
        self.face = np.array(self.mesh.faces, np.uint32)

    def draw(self):
        if self.vertices is None:
            return

        glPushMatrix()

        glColor3f(0.9, 0.9, 0.9)

        glScalef(self.scale, self.scale, self.scale)

        glBegin(GL_TRIANGLES)

        for face in self.faces:
            for i in face:
                v = self.vertices[i]
                glVertex3f(v[0], v[1], v[2])

        glEnd()

        glPopMatrix()
