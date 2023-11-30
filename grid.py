from OpenGL.GL import glColor3f, glBegin, glEnd, glVertex3f, GL_LINES


class Grid:

    def __init__(self, **kwargs):
        self.margin = kwargs.get("margin", 0.25)
        self.size = kwargs.get("size", 3)
        self.cnt_of_lines = int(self.size / self.margin)

        self.rgb = (255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0)

    def draw(self):
        glBegin(GL_LINES)

        # Draw LineS
        glColor3f(0.2, 0.2, 0.2)

        for i in range(1, ((self.cnt_of_lines + 1) // 2)):
            # Y-lines
            glVertex3f(self.margin * i, self.size / 2, 0)
            glVertex3f(self.margin * i, -self.size / 2, 0)

            glVertex3f(-self.margin * i, self.size / 2, 0)
            glVertex3f(-self.margin * i, -self.size / 2, 0)

            # X-lines
            glVertex3f(self.size / 2, self.margin * i, 0)
            glVertex3f(-self.size / 2, self.margin * i, 0)
            
            glVertex3f(self.size / 2, -self.margin * i, 0)
            glVertex3f(-self.size / 2, -self.margin * i, 0)

        # Draw X-axis 
        glColor3f(0.8, 0, 0)
        glVertex3f(self.size / 2, 0, 0)
        glVertex3f(-self.size / 2, 0, 0)

        # Draw Y-axis
        glColor3f(0, 0.9, 0)
        glVertex3f(0, self.size / 2, 0)
        glVertex3f(0, -self.size / 2, 0)

        glEnd()
