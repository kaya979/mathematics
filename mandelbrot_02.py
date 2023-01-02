# “A Mandelbrot set marks the set of points in the complex plane such that the corresponding 
# Julia set is connected and not computable. 
# The Mandelbrot set is the set obtained from
#  the recurrence relation, Z_(n) = Z²_(n-1) + c, where, Z_(0) = c. where c is a complex number” 
# — Wolfram Mathworld.

# The colors in a Mandelbrot set represents the iterations at which that complex number diverges to
#  infinity (we can use here some threshold instead of infinity). 
# Generally, the black color is for numbers that converge to zero 
# (here we can use some maximum iteration limit under which if the number is not greater than the 
# threshold value we assume it is converging to zero) and that's all in a Mandelbrot set (not really).





import matplotlib.pyplot as plt
import numpy as np

def get_iter(c:complex, thresh:int =4, max_steps:int =25) -> int:
    # Z_(n) = (Z_(n-1))^2 + c
    # Z_(0) = c
    z=c
    i=1
    while i<max_steps and (z*z.conjugate()).real<thresh:
        z=z*z +c
        i+=1
    return i

# The above code is used to find if a complex number diverges under max_steps and if it does then when



def plotter(n, thresh, max_steps=25):
    mx = 2.48 / (n-1)
    my = 2.26 / (n-1)
    mapper = lambda x,y: (mx*x - 2, my*y - 1.13)
    img=np.full((n,n), 255)
    for x in range(n):
        for y in range(n):
            it = get_iter(complex(*mapper(x,y)), thresh=thresh, max_steps=max_steps)
            img[y][x] = 255 - it
    return img


# Line 37: Maps the image coordinate to the real-valued number in the range [-2,0.47] for x and in the range [-1.12,1.12] for y (with a margin of 0.01 on all sides),
#  which will be used to make complex numbers. 
# Because it is known that the set is bounded with “The left-most extent of the set ends with the spike at x = -2, and the right side extends out to approximately x = 0.47. 
# The top and bottom are at approximately y = ± 1.12, respectively” — fractalus.

# Line 38: Creates a Numpy array of shape N*N, to store the pixel values of Mandelbrot Set.

# Line 39–41: We loop through all pixels coordinates, using two loops, and calculate the pixel value for that coordinate (it is really the iteration value).

# Line 42-43: put the pixel value in the image. I used “img[y][x]=255-it” because more iterations mean heading toward brack color. 
# (I don’t know why does the image gets rotated -90 degree, but I rotated it 90 degrees by using “img[y][x]=255-it” instead of using “img[x][y]=255-it”) and returned the image “img”.


n=1000
img = plotter(n, thresh=4, max_steps=50)
plt.imshow(img, cmap="plasma")
plt.axis("off")
plt.show()

# The above code creates an image.

