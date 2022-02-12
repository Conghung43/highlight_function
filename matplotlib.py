import matplotlib.pyplot as plt
plt.scatter(pixel_list[:, 0], 
        pixel_list[:, 1],
        c = clustering.labels_,
        s=1, cmap='inferno')
plt.scatter(current_ps_pixel_data[:, 0], 
        current_ps_pixel_data[:, 1], 
        c = '#FF0000',
        s=1)
# plt.plot(first_array[:, 0][0],first_array[:, 1][0],marker="o", color="red")
# plt.show()
plt.pause(1)
plt.clf()
