import neurokit2 as nk
import matplotlib.pyplot as plt

nk.fractal_mandelbrot(show=True)


m = nk.fractal_mandelbrot(real_range=(-2, 0.75), imaginary_range=(-1.25, 1.25))
plt.imshow(m.T, cmap="viridis")
plt.axis("off")
plt.show()


# WORKS!!!!