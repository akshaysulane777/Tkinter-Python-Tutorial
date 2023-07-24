import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk
import numpy as np

def open_file_1():
    file_path_1 = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
    if file_path_1:
        global image_1, cv_image_1
        image_1 = Image.open(file_path_1)
        image_1 = image_1.resize((300, 300))  # Resize the image to display in the GUI
        cv_image_1 = np.array(image_1)
        photo_1 = ImageTk.PhotoImage(image_1)
        image_label_1.config(image=photo_1)
        image_label_1.image = photo_1

def open_file_2():
    file_path_2 = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
    if file_path_2:
        global image_2, cv_image_2
        image_2 = Image.open(file_path_2)
        image_2 = image_2.resize((300, 300))  # Resize the image to display in the GUI
        cv_image_2 = np.array(image_2)
        photo_2 = ImageTk.PhotoImage(image_2)
        image_label_2.config(image=photo_2)
        image_label_2.image = photo_2

def compare_images():
    if cv_image_1 is not None and cv_image_2 is not None:
        gray_image_1 = cv2.cvtColor(cv_image_1, cv2.COLOR_RGB2GRAY)
        gray_image_2 = cv2.cvtColor(cv_image_2, cv2.COLOR_RGB2GRAY)

        # Calculate histograms
        hist_1, _ = np.histogram(gray_image_1.flatten(), bins=256, range=[0, 256])
        hist_2, _ = np.histogram(gray_image_2.flatten(), bins=256, range=[0, 256])

        # Convert histograms to CV_32F
        hist_1 = hist_1.astype(np.float32)
        hist_2 = hist_2.astype(np.float32)

        # Calculate histogram comparison using Chi-Squared distance
        chi_squared_distance = cv2.compareHist(hist_1, hist_2, cv2.HISTCMP_CHISQR)

        similarity_threshold = 3000  # Set the threshold value

        if chi_squared_distance < similarity_threshold:
            result_label.config(text="The images are similar.")
        else:
            result_label.config(text="The images are different.")

# Create the main application window
root = tk.Tk()
root.title("Image Comparison")

# Create buttons to select the first and second image files
select_button_1 = tk.Button(root, text="Select Image 1", command=open_file_1)
select_button_1.pack(pady=10)

select_button_2 = tk.Button(root, text="Select Image 2", command=open_file_2)
select_button_2.pack(pady=10)

# Create a button to compare the images
compare_button = tk.Button(root, text="Compare", command=compare_images)
compare_button.pack(pady=10)

# Create labels to display the selected images
image_label_1 = tk.Label(root)
image_label_1.pack(side=tk.LEFT, padx=10)

image_label_2 = tk.Label(root)
image_label_2.pack(side=tk.LEFT, padx=10)

# Create a label to display the result
result_label = tk.Label(root, text="Comparison result will appear here.")
result_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()

