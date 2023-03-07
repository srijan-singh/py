import numpy as np
height_list = [180, 215, 176, 150, 181, 209]
height_array = np.array(height_list)
height_array_m = height_array * 0.0254
print(height_array_m)