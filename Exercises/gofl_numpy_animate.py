import matplotlib.pyplot as plt
from matplotlib import animation


def _animate(self, *args):
    # This is the callback function used by the
    # matlibplot.animation.FuncAnimation function.  It is responsible
    # for advanccing the game, and then setting the array for the image.
    # The requirements for the callback are that it must return a tuple
    # of 1 element containing the AxisImage object.
    if (self.rows <= 30 and self.cols <= 80):
      self.print_grid()
    self.next_move()
    self.im.set_array(self.grid)
    return (self.im,)


def play(self):
    # Plays Conways' game of life and uses matplotlib to create an
    # animation of the changes in the grid.

    # First create a Figure object.  The Figure object contains all of
    # the plot elements.
    fig = plt.figure()

    # Create an AxisImage object using the imshow object. An AxisImage
    # object uses an array of points to represent pixels in an image.
    # Ee can use our numpy created grid to represent our pixels.  The colors
    # of the pixels are managed by the cmap argument.  Anything with a value
    # of zero is background and anything with a value of one is the
    # forground. Anything with a value between 0 and 1 is some gradient
    # value between the colors. In our case we only use 1 and zero..
    self.im = plt.imshow(self.grid, animated=True)

    # To get the image to be animated we have to create a FuncAnimation
    # object.  It receives as the Figure object, and the name of a function
    # that it will call each step of the animation.  The number of
    # miliseconds between each step of the animation is also given.
    anim = animation.FuncAnimation(fig, self._animate, interval=1)

    # Start the show!
    plt.show()
