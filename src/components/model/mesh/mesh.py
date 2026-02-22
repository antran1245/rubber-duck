import trimesh
import numpy as np
from OpenGL.GL import *


class Mesh:
    def __init__(self, path, scale=0.5):
        self.scale = scale

        scene = trimesh.load(path)

        if isinstance(scene, trimesh.Scene):
            self.mesh = trimesh.util.concatenate(scene.dump())
        else:
            self.mesh = scene

        self.vertices = np.array(self.mesh.vertices, np.float32)
        self.faces = np.array(self.mesh.faces, np.uint32)

        if (
            hasattr(self.mesh.visual, "vertex_colors")
            and len(self.mesh.visual.vertex_colors) > 0
        ):

            colors = self.mesh.visual.vertex_colors
            self.colors = colors[:, :3] / 255.0
        else:
            self.colors = None

    def draw(self):
        if self.vertices is None:
            return

        glPushMatrix()

        glScalef(self.scale, self.scale, self.scale)

        glBegin(GL_TRIANGLES)

        for face in self.faces:
            for i in face:

                if self.colors is not None:
                    c = self.colors[i]
                    glColor3f(float(c[0]), float(c[1]), float(c[2]))
                else:
                    glColor3f(0.8, 0.8, 0.8)

                v = self.vertices[i]
                glVertex3f(float(v[0]), float(v[1]), float(v[2]))

        glEnd()

        glPopMatrix()
