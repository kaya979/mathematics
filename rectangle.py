import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


fig, ax = plt.subplots()

ax.plot([0, 10],[0, 10])



ax.add_patch(Rectangle((1, 1), 2, 6))


plt.show()




# This code is a test file to see that matplotlib is working including outputting an image as named Figure_2.png, see files in the repo.