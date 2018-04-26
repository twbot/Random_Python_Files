#!/usr/bin/env python3
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook


def main():
    image_file = cbook.get_sample_data('ada.png')
    image = plt.imread(image_file)
    plt.imshow(image)
    plt.axis('off')  # clear x- and y-axes
    plt.show()


if __name__ == '__main__':
	main()