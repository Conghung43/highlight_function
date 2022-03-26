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


ax = plt.axes(projection ="3d")

image = cv2.imread('dummy_data/objects_collection.jpg')
f =  open('dummy_data/objects_collection.npy', 'rb')
objects_collection = np.load(f, allow_pickle=True)
objects_collection = np.array([objects_collection[index] for index in range(0, len(objects_collection),50)])
x,y,z = [objects_collection[:,0], 
                    objects_collection[:,1], 
                    objects_collection[:,2]]
print(len(objects_collection))
sctt = ax.scatter3D(x,y,z,
                    alpha = 0.8,
                    c = (x + y + z),
                    )
ax.set_xlim([0,255])
ax.set_ylim([0,255])
ax.set_zlim([0,255])
plt.show()
