import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


fig, ax = plt.subplots()

ax.plot([0, 10],[0, 10])



ax.add_patch(Rectangle((1, 1), 2, 6))


plt.show()
