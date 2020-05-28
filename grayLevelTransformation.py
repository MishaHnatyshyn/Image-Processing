from numpy import uint8

def clamp_image_bitmap_to_interval(image_bitmap_array, interval_start, interval_end):
    interval_range = interval_end - interval_start
    clamped_image = ((interval_range / 255) * image_bitmap_array + interval_start).astype(uint8)
    return clamped_image


# coefficient > 1 - return darker image
# coefficient = 1 - return same image
# coefficient < 1 && coefficient > 0  - return brighter image
def change_image_bitmap_darkness(image_bitmap_array, coefficient):
    darker_image = 255.0 * (image_bitmap_array / 255.0) ** coefficient
    return darker_image


