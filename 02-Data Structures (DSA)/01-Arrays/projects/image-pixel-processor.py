class ImagePixelProcessor:
    """
    A flexible image processor that supports various kernel-based image filters and transformations. 
    This processor allows customized padding, filter sizes, and a variety of filters such as blur, sharpen, 
    edge detection, emboss, and custom user-defined filters. It also supports basic image transformations.
    """
    
    def __init__(self, image, padding_type='zero'):
        """
        Initializes the processor with the given image and padding configuration.

        Args:
            image (list[list[int]]): 2D array representing a grayscale image.
            padding_type (str): The type of padding to apply ('zero' or 'replicate'). Default is 'zero'.
        """
        self.image = image
        self.padding_type = padding_type  # Define padding type ('zero' or 'replicate')

    def apply_filter(self, kernel, padding=None):
        """
        Applies a given kernel to the image using convolution with customizable padding.

        Args:
            kernel (list[list[int]]): 2D array representing the kernel.
            padding (int, optional): The padding size to be added around the image. Defaults to None.

        Returns:
            list[list[int]]: The filtered image as a 2D array after applying the kernel.
        """
        rows, cols = len(self.image), len(self.image[0])
        k_rows, k_cols = len(kernel), len(kernel[0])
        pad = padding if padding is not None else k_rows // 2  # Padding size

        # Create a padded version of the image based on the selected padding type
        padded_image = self._apply_padding(self.image, rows, cols, k_rows, k_cols, pad)

        # Prepare an output image
        output = [[0] * cols for _ in range(rows)]

        # Perform convolution
        for i in range(rows):
            for j in range(cols):
                result = 0
                for ki in range(k_rows):
                    for kj in range(k_cols):
                        result += padded_image[i + ki][j + kj] * kernel[ki][kj]
                output[i][j] = min(max(result, 0), 255)  # Clamp to [0, 255]
        
        return output

    def _apply_padding(self, image, rows, cols, k_rows, k_cols, pad):
        """
        Applies the padding to the image, either using zero-padding or replicate-padding.
        
        Args:
            image (list[list[int]]): Original 2D image.
            rows (int): Number of rows in the image.
            cols (int): Number of columns in the image.
            k_rows (int): Kernel rows.
            k_cols (int): Kernel columns.
            pad (int): Padding size.

        Returns:
            list[list[int]]: Padded 2D image.
        """
        if self.padding_type == 'zero':
            # Zero padding: Add 0s around the image
            padded_image = [[0] * (cols + 2 * pad) for _ in range(rows + 2 * pad)]
        elif self.padding_type == 'replicate':
            # Replicate padding: Repeat the edge pixels
            padded_image = [[0] * (cols + 2 * pad) for _ in range(rows + 2 * pad)]
            for i in range(rows):
                for j in range(cols):
                    padded_image[i + pad][j + pad] = self.image[i][j]
            for i in range(pad):
                for j in range(cols):
                    padded_image[i][j + pad] = self.image[0][j]  # Replicate top row
                    padded_image[rows + pad + i][j + pad] = self.image[rows - 1][j]  # Replicate bottom row
            for i in range(pad):
                for j in range(rows + 2 * pad):
                    padded_image[j][i] = padded_image[j][pad]  # Replicate left column
                    padded_image[j][cols + pad + i] = padded_image[j][cols + pad - 1]  # Replicate right column
        else:
            raise ValueError("Unsupported padding type. Use 'zero' or 'replicate'.")
        return padded_image

    def print_image(self, image):
        """
        Prints the image as a grid of pixel values.

        Args:
            image (list[list[int]]): The 2D array representing the image.
        """
        for row in image:
            print(" ".join(f"{val:3}" for val in row))

    def blur(self, kernel_size=3):
        """
        Applies a blur filter to the image with customizable kernel size.

        Args:
            kernel_size (int): Size of the blur kernel. Default is 3 for a 3x3 kernel.

        Returns:
            list[list[int]]: The blurred image as a 2D array.
        """
        blur_kernel = [[1/(kernel_size**2)] * kernel_size for _ in range(kernel_size)]
        return self.apply_filter(blur_kernel)

    def sharpen(self):
        """
        Applies a sharpen filter to the image.

        Returns:
            list[list[int]]: The sharpened image as a 2D array.
        """
        sharpen_kernel = [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]  # Sharpen kernel
        return self.apply_filter(sharpen_kernel)

    def edge_detection(self):
        """
        Applies an edge detection filter to the image.

        Returns:
            list[list[int]]: The edge-detected image as a 2D array.
        """
        edge_detection_kernel = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]  # Edge detection kernel
        return self.apply_filter(edge_detection_kernel)

    def emboss(self):
        """
        Applies an emboss filter to the image.

        Returns:
            list[list[int]]: The embossed image as a 2D array.
        """
        emboss_kernel = [[-2, -1, 0], [-1, 1, 1], [0, 1, 2]]  # Emboss kernel
        return self.apply_filter(emboss_kernel)

    def sharpen_highpass(self):
        """
        Applies a high-pass sharpen filter to the image.

        Returns:
            list[list[int]]: The high-pass sharpened image as a 2D array.
        """
        highpass_kernel = [[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]  # High-pass filter kernel
        return self.apply_filter(highpass_kernel)

    def custom_filter(self, kernel):
        """
        Applies a custom user-defined filter to the image.

        Args:
            kernel (list[list[int]]): The user-defined kernel.

        Returns:
            list[list[int]]: The image filtered with the custom kernel.
        """
        return self.apply_filter(kernel)

    def rotate(self, angle):
        """
        Rotates the image by a given angle (clockwise).

        Args:
            angle (int): The angle by which to rotate the image.

        Returns:
            list[list[int]]: The rotated image as a 2D array.
        """
        import math
        # Convert angle to radians
        angle_rad = math.radians(angle)
        rows, cols = len(self.image), len(self.image[0])
        new_image = [[0] * cols for _ in range(rows)]
        
        center_x, center_y = cols // 2, rows // 2
        for i in range(rows):
            for j in range(cols):
                # Rotate each pixel
                new_x = int((j - center_x) * math.cos(angle_rad) - (i - center_y) * math.sin(angle_rad) + center_x)
                new_y = int((j - center_x) * math.sin(angle_rad) + (i - center_y) * math.cos(angle_rad) + center_y)
                if 0 <= new_x < cols and 0 <= new_y < rows:
                    new_image[new_y][new_x] = self.image[i][j]
        return new_image

    def flip(self, direction='horizontal'):
        """
        Flips the image either horizontally or vertically.

        Args:
            direction (str): 'horizontal' or 'vertical'. Default is 'horizontal'.

        Returns:
            list[list[int]]: The flipped image as a 2D array.
        """
        rows, cols = len(self.image), len(self.image[0])
        flipped_image = [[0] * cols for _ in range(rows)]
        
        if direction == 'horizontal':
            for i in range(rows):
                for j in range(cols):
                    flipped_image[i][cols - 1 - j] = self.image[i][j]
        elif direction == 'vertical':
            for i in range(rows):
                for j in range(cols):
                    flipped_image[rows - 1 - i][j] = self.image[i][j]
        else:
            raise ValueError("Direction must be 'horizontal' or 'vertical'.")
        
        return flipped_image

# Example Usage
if __name__ == "__main__":
    # Sample grayscale image (5x5)
    sample_image = [
        [10, 20, 30, 40, 50],
        [50, 60, 70, 80, 90],
        [90, 100, 110, 120, 130],
        [130, 140, 150, 160, 170],
        [170, 180, 190, 200, 210],
    ]

    # Initialize processor with replicate padding
    processor = ImagePixelProcessor(sample_image, padding_type='replicate')
    print("Original Image:")
    processor.print_image(sample_image)

    # Apply blur with custom kernel size
    blurred_image = processor.blur(kernel_size=3)
    print("\nBlurred Image:")
    processor.print_image(blurred_image)

    # Apply sharpen filter
    sharpened_image = processor.sharpen()
    print("\nSharpened Image:")
    processor.print_image(sharpened_image)

    # Apply edge detection
    edges_image = processor.edge_detection()
    print("\nEdge Detection Image:")
    processor.print_image(edges_image)

    # Apply emboss filter
    embossed_image = processor.emboss()
    print("\nEmbossed Image:")
    processor.print_image(embossed_image)

    # Flip image horizontally
    flipped_image = processor.flip(direction='horizontal')
    print("\nFlipped Image (Horizontal):")
    processor.print_image(flipped_image)

    # Rotate image by 90 degrees
    rotated_image = processor.rotate(90)
    print("\nRotated Image (90 degrees):")
    processor.print_image(rotated_image)
