import grayLevelTransformation
import neighborhoodProcessing
import edgeDetection
from numpy import array
from matplotlib import pyplot as plt
from PIL import Image

url = 'image.jpg'
im = array(Image.open(url).convert('L'))


def test(modified_img, modified_title):
    plt.figure(figsize=(50, 50))

    plt.subplot(1, 2, 1)
    plt.imshow(im, cmap='gray', vmin=0, vmax=255)
    plt.title('Original')

    plt.subplot(1, 2, 2)
    plt.imshow(modified_img, cmap='gray', vmin=0, vmax=255)
    plt.title(modified_title)

    plt.show()


clamped = grayLevelTransformation.clamp_image_bitmap_to_interval(im, 100, 200)
test(clamped, 'Clamped to interval 100-200')

darker = grayLevelTransformation.change_image_bitmap_darkness(im, 3)
test(darker, 'Darker with degree 3')

with_minimum_filter = neighborhoodProcessing.apply_minimum_filter_to_image(im)
test(with_minimum_filter, 'Minimum filter')

with_mean_filter = neighborhoodProcessing.apply_mean_filter_to_image(im)
test(with_mean_filter, 'Mean filter')

with_gaussian_filter = neighborhoodProcessing.apply_gaussian_filter_to_image(im)
test(with_gaussian_filter, 'Gaussian filter')

with_laplacian_edge_detection = edgeDetection.perform_laplacian_edge_detection(url)
test(with_laplacian_edge_detection, 'Laplacian edge-detection')
