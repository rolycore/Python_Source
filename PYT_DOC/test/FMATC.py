import cv2



image = imread("region18.jpg")

#Mat gray(image.rows, image.cols, CV_8UC1)

for (int i = 0; i < image.rows; i++):

    for (size_t j = 0; j < image.cols; j++):

        Vec3b pixel = image.at<Vec3b>(i, j)
        uchar B = pixel[0]
        uchar G = pixel[1]
        uchar R = pixel[2]

        gray.at<uchar>(i, j) = (B + G + R) / 3
    
