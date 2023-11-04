import tkinter as tk
from mahaNLP.autocomplete import TextGenerator
from PIL import Image, ImageTk
def generate_word_completion():
    text = entry_word_completion.get()
    num_predictions = int(entry_num_predictions_word.get())
    predictions = model.next_word(text, num_of_predictions=num_predictions)
    result_word_completion.set(predictions)

def generate_sentence_completion():
    text = entry_sentence_completion.get()
    num_predictions = int(entry_num_predictions_sentence.get())
    predictions = model.complete_sentence(text, num_of_predictions=num_predictions)
    result_sentence_completion.set(predictions)

# Create the main window
root = tk.Tk()
root.title("Marathi Text Generation")

# Initialize the TextGenerator
model = TextGenerator()

# Set the window size
window_width = 800
window_height = 600
root.geometry(f"{window_width}x{window_height}")

# Set the background color to light grey
root.configure(bg="light grey")

# Load the logo image
logo_image = Image.open("MARATHI Maitri.jpg")  # Replace with your logo image path
logo_photo = ImageTk.PhotoImage(logo_image)

# Create a label for the logo
logo_label = tk.Label(root, image=logo_photo, bg="light grey")
logo_label.image = logo_photo  # Prevent image from being garbage collected
logo_label.pack()

# Stylish heading
heading_label = tk.Label(root, text="Marathi Maitri", font=("Arial", 24, "bold"), bg="light grey", fg="black")
heading_label.pack()

# Add space between the heading and the sections
space_label = tk.Label(root, text="", bg="light grey", height=2)
space_label.pack()

# Word Completion Section
frame_word_completion = tk.Frame(root, bg="beige")
frame_word_completion.pack()

label_word_completion = tk.Label(frame_word_completion, text="Enter text for word completion:", bg="beige")
label_word_completion.pack()

entry_word_completion = tk.Entry(frame_word_completion)
entry_word_completion.pack(fill=tk.BOTH, expand=True)

label_num_predictions_word = tk.Label(frame_word_completion, text="Number of predictions:", bg="beige")
label_num_predictions_word.pack()

entry_num_predictions_word = tk.Entry(frame_word_completion)
entry_num_predictions_word.pack(fill=tk.BOTH, expand=True)

result_word_completion = tk.StringVar()
label_result_word_completion = tk.Label(frame_word_completion, textvariable=result_word_completion, bg="beige")
label_result_word_completion.pack(fill=tk.BOTH, expand=True)

button_word_completion = tk.Button(frame_word_completion, text="Generate Word Completion", command=generate_word_completion, bg="blue", fg="white")
button_word_completion.pack()

# Add space between the sections
space_label2 = tk.Label(root, text="", bg="light grey", height=2)
space_label2.pack()

# Sentence Completion Section
frame_sentence_completion = tk.Frame(root, bg="light pink")
frame_sentence_completion.pack()

label_sentence_completion = tk.Label(frame_sentence_completion, text="Enter text for sentence completion:", bg="light pink")
label_sentence_completion.pack()

entry_sentence_completion = tk.Entry(frame_sentence_completion)
entry_sentence_completion.pack(fill=tk.BOTH, expand=True)

label_num_predictions_sentence = tk.Label(frame_sentence_completion, text="Number of predictions:", bg="light pink")
label_num_predictions_sentence.pack()

entry_num_predictions_sentence = tk.Entry(frame_sentence_completion)
entry_num_predictions_sentence.pack(fill=tk.BOTH, expand=True)

result_sentence_completion = tk.StringVar()
label_result_sentence_completion = tk.Label(frame_sentence_completion, textvariable=result_sentence_completion, bg="light pink")
label_result_sentence_completion.pack(fill=tk.BOTH, expand=True)

button_sentence_completion = tk.Button(frame_sentence_completion, text="Generate Sentence Completion", command=generate_sentence_completion, bg="green", fg="white")
button_sentence_completion.pack()

root.mainloop()
