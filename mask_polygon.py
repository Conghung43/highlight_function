# Block for testing autolable based on detected color then clasify
# frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
# # frame = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
# objects_collection = []
# for mask_layer in mask_layers:
#     if len(objects_collection) == 0:
#         objects_collection = frame[np.where(mask_layer.mask == 1)]
#     else:
#         objects_collection = np.concatenate((objects_collection , frame[np.where(mask_layer.mask == 1)]), axis = 0)
#     print(mask_layer.area())
# f =  open('dummy_data/objects_collection.npy', 'wb') 
# np.save(f, objects_collection)
# f.close()
# cv2.imwrite('dummy_data/objects_collection.jpg',frame )
# print(np.mean(objects_collection))
#Done block
