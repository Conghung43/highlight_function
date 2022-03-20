import cv2

def write_image(dir, image_name, image):
    cv2.imwrite(f'{dir}/{image_name}.jpg', image)

def show_image(tab_name, image, is_iteration):
    cv2.imshow(tab_name, image)
    if is_iteration:
        cv2.waitKey(1)
    else:
        cv2.waitKey(0)

        
# Draw line from polygon
            #     for index, point in enumerate(polygons):
            #         if index >= len(polygons) - 1:
            #             vis_frame = cv2.line(vis_frame,tuple(point),tuple(polygons[0]),(0, 255, 0),1)
            #         else:
            #             vis_frame = cv2.line(vis_frame,tuple(point),tuple(polygons[index + 1]),(0, 255, 0),1)
