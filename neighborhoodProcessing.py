import scipy.ndimage
from numpy import ones


def apply_minimum_filter_to_image(image_bitmap, size=5):
    result_image = scipy.ndimage.filters.minimum_filter(
        image_bitmap,
        size,
        footprint=None,
        output=None,
        mode='reflect',
        cval=0.0,
        origin=0
    )
    return result_image


def apply_gaussian_filter_to_image(image_bitmap, sigma=2):
    result_image = scipy.ndimage.filters.gaussian_filter(
        image_bitmap,
        sigma,
        order=0,
        output=None,
        mode="reflect",
        cval=0.0,
        truncate=4.0
    )
    return result_image


def apply_mean_filter_to_image(image_bitmap):
    coefficient = ones((5, 5)) / 25
    result_image = scipy.ndimage.filters.convolve(image_bitmap, coefficient)
    return result_image
