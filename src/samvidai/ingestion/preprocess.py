import cv2

def preprocess_image(image_path: str) -> str:
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    img = cv2.GaussianBlur(img, (5, 5), 0)
    img = cv2.adaptiveThreshold(
        img, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11, 2
    )

    cv2.imwrite(image_path, img)
    return image_path
