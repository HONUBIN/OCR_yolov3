from PIL import Image
import numpy as np
import math

def dot(vector1, vector2, crop_param):
    for i in range(0, crop_param):
        for j in range(0, crop_param):
            vector_sum = vector1[i][j][0] * vector2[i][j][0] + vector1[i][j][1] * vector2[i][j][1] + vector2[i][j][2] * vector2[i][j][2]
    return vector_sum

def cosine_compare(vector1, vector2, crop_param): #changed
    similarity_param = 0.8
    dot_product = dot(vector1, vector2, crop_param)
    vector1_scale = math.sqrt(dot(vector1, vector1, crop_param))
    vector2_scale = math.sqrt(dot(vector2, vector2, crop_param))
    similarity = dot_product / (vector1_scale * vector2_scale)
    print("cosin_similarity : ", similarity)

    if similarity > similarity_param:
        return True
    else :
        return False


def image_parse(crop_param, img):
    #image = Image.open(src)
    resized_image = img.resize((200,200))
    #resized_image.save(dst)
    # crop_param = 2
    vector = np.zeros((crop_param, crop_param, 3))
    crop_len = 200/crop_param
    for i in range(0, crop_param):
        for j in range(0, crop_param):
            crop_image = resized_image.crop((crop_len * i, crop_len * j, crop_len * (i+1), crop_len * (j+1)))
            #crop_image.save(str(i)+str(j)+'test.jpg')
            rgb_crop_image = get_color(crop_image)
            vector[i][j][0] = rgb_crop_image[0]
            vector[i][j][1] = rgb_crop_image[1]
            vector[i][j][2] = rgb_crop_image[2]
    return vector


def get_color(image, convert = False):
    colors = image.getcolors(image.size[0] * image.size[1])
    i = 0
    c = [0,0,0]
    for (count, color) in colors:
        if True:
            i = i + count
            for a in range(count):
                if convert:
                    c[2] += color[0]
                    c[1] += color[1]
                    c[0] += color[2]
                else:
                    c[0] += color[0]
                    c[1] += color[1]
                    c[2] += color[2]
    if i == 0:
        return (0,0,0)
    else:
        c[0] = c[0] // i
        c[1] = c[1] // i
        c[2] = c[2] // i
    c=tuple(c)

    #print('avg_color: ', c)
    return c