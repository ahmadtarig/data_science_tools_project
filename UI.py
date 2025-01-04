import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

# Initialize the main window
root = tk.Tk()
root.title("Movice Gross Predictor")
root.attributes('-fullscreen', True)   # set window state as fullscreen

# get screen dimensions
screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()

# Initialze width and heigh
# 1- top bar 
top_bar_height = int(screen_height * 0.04)

# 2- left and right panel 
panel_height = screen_height - top_bar_height + 10 # left and right panel have same height

# left panel width (14 VW)
left_panel_width = int(screen_width * 0.14)

# right panel width (full width - left panel width)
right_panel_width = screen_width - left_panel_width 

# 3- left panel labels
Left_panel_labels_height = top_bar_height * 2


# Initialze defult font
defult_font = ("Sanserif", 12, "bold")  

# Initialize the colors
black_1 = '#171717'
black_2 = '#252525'



# create top bar 
top_bar = tk.Frame(root, height=top_bar_height, bg=black_1, bd=2)
top_bar.pack(fill="x", anchor="n")  



# create the left panel
left_panel = tk.Frame(root, height=panel_height, width=left_panel_width, bg=black_1)
left_panel.place(x=0, y=top_bar_height - 5, anchor="nw")  

# create left panel component (labels expected program steps)
# introduction label
left_panel_label_introduction = tk.Label(left_panel, text="Introduction", fg="white", bg=black_2, font=defult_font)
left_panel_label_introduction.place(x=0, y=Left_panel_labels_height, width=left_panel_width, height=50) 

# production label
left_panel_label_production_cost = tk.Label(left_panel, text="Budget", fg="white", bg=black_1, font=defult_font)
left_panel_label_production_cost.place(x=0, y=Left_panel_labels_height * 2, width=left_panel_width, height=50) 

# genre label
left_panel_label_genre = tk.Label(left_panel, text="Type", fg="white", bg=black_1, font=defult_font)
left_panel_label_genre.place(x=0, y=Left_panel_labels_height * 3, width=left_panel_width, height=50) 

# year label
left_panel_label_year = tk.Label(left_panel, text="Year", fg="white", bg=black_1, font=defult_font)
left_panel_label_year.place(x=0, y=Left_panel_labels_height * 4, width=left_panel_width, height=50) 

# prediction label
left_panel_label_prediction = tk.Label(left_panel, text="Prediction", fg="white", bg=black_1, font=defult_font)
left_panel_label_prediction.place(x=0, y=panel_height - int(Left_panel_labels_height *1.4), width=left_panel_width, height=50) 


# create right panel
right_panel = tk.Frame(root, height=panel_height, width=right_panel_width, bg=black_2, relief="solid", highlightthickness=0)
right_panel.place(x=screen_width , y=top_bar_height - 5, anchor="ne")  # Position it at the right side

# create right panels
# create frame for each label (Introduction, Budget, Type, Year, Prediction)
frame_introduction = tk.Frame(right_panel, height=panel_height, width=right_panel_width, bg=black_2)
frame_budget = tk.Frame(right_panel, height=panel_height, width=right_panel_width, bg=black_2)
frame_genre = tk.Frame(right_panel, height=panel_height, width=right_panel_width, bg=black_2)
frame_year = tk.Frame(right_panel, height=panel_height, width=right_panel_width, bg=black_2)
frame_prediction = tk.Frame(right_panel, height=panel_height, width=right_panel_width, bg=black_2)

# create title to each frame 
tk.Label(frame_introduction, text="Introduction", fg="white", bg=black_2, font=("Sanserif", 32, "bold")).place(relx=0.5, rely=0.1, anchor="center")
tk.Label(frame_budget, text="Movie Budget ", fg="white", bg=black_2, font=("Sanserif", 32, "bold")).place(relx=0.5, rely=0.1, anchor="center")
tk.Label(frame_genre, text="Movie Type", fg="white", bg=black_2, font=("Sanserif", 32, "bold")).place(relx=0.5, rely=0.1, anchor="center")
tk.Label(frame_year, text="Time", fg="white", bg=black_2, font=("Sanserif", 32, "bold")).place(relx=0.5, rely=0.1, anchor="center")
tk.Label(frame_prediction, text="Prediction Content", fg="white", bg=black_2, font=("Sanserif", 32, "bold")).place(relx=0.5, rely=0.1, anchor="center")

# create description to each frame 
tk.Label(frame_introduction, text="Introduction", fg="white", bg=black_2, font=("Sanserif", 32, "bold")).place(relx=0.5, rely=0.1, anchor="center")

# For the "Introduction" frame
tk.Label(frame_introduction, 
          text="\tThis program leverages historical movie data from The Movie Database (TMDb) API to predict the world gross of a movie."
               "By analyzing factors such as the production budget, genre, and release year, the program estimates how well a movie will perform in global markets."
               "The model uses a machine learning approach to derive these predictions, based on patterns observed in movies similar to the one you're interested in."
               "Through the user-friendly interface, you can input the movie's expected budget, genre, and release year, and instantly receive a prediction of the movie's worldwide earnings."
               "The goal of this tool is to assist filmmakers, producers, and anyone in the entertainment industry in making more informed decisions about a movie's financial potential.\n\n\n"
               "Key Features:\n\n"
               "1. Production Budget Input: Provide an estimate of the movie's budget to assess the potential return on investment.\n\n"
               "2. Genre Selection: Choose the movie's genre to factor in the popularity and trends of specific categories (e.g., Action, Comedy, Drama).\n\n"
               "3. Release Year Input: Set the release year to evaluate how the timing of the movie might influence its performance, factoring in seasonal trends and historical data.\n\n"
               "4. World Gross Prediction: Receive an estimate of the global earnings based on the provided data and predictive modeling.\n\n\n\n"
               "The model is trained on data sourced from The Movie Database (TMDb) API, which provides rich metadata on movies, including financial information, to support these predictions.",
          fg="white", bg=black_2, font=("Sanserif", 12), wraplength=800, justify="left").place(relx=0.5, rely=0.48, anchor="center")

# for the "Budget" frame
tk.Label(frame_budget, text="Expected Budget", fg="white", bg=black_2, font=("Sanserif", 32, "bold")).place(relx=0.5, rely=0.1, anchor="center")
tk.Label(frame_budget, text="Here, you will input the movie's expected production budget. The budget is a key factor in predicting the financial success of a movie.", wraplength=800, fg="white", bg=black_2, font=("Sanserif", 12)).place(relx=0.5, rely=0.2, anchor="center")
tk.Label(frame_budget, text="Enter expected budget (Min: 119.0 million, Max: 460 million)", fg="white", bg=black_2, font=("Sanserif", 12), wraplength=800, justify="left").place(relx=0.5, rely=0.4, anchor="center")
budget_entry = ctk.CTkEntry(frame_budget, font=("Sanserif", 14), corner_radius=12, fg_color=black_1, width=600, height=50, border_width=0)
budget_entry.place(relx=0.5, rely=0.5, anchor="center")
feedback_label = tk.Label(frame_budget, fg="white", bg=black_2, font=("Sanserif", 14))

# function to check budget value if valid or not and print feedback
def check_budget(budget_value):
    try:
        budget = float(budget_value)  # Convert the input to a float
        if 119.0 <= budget <= 460000000:
            feedback_label.config(text=f"Valid budget: {budget:.2f} million", fg="green")
            return True
        else:
            feedback_label.config(text="Budget is out of range. Please enter a valid budget.", fg="red")
    except ValueError:
        feedback_label.config(text="Invalid input. Please enter a valid numeric budget.", fg="red")
    feedback_label.place(relx=0.5, rely=0.6, anchor="center")
    return False

# for the "Genre" frame
tk.Label(frame_genre, text="Expected Type", fg="white", bg=black_2, font=("Sanserif", 32, "bold")).place(relx=0.5, rely=0.1, anchor="center")
tk.Label(frame_genre, text="Select the genre of the movie. Different genres have different trends in terms of audience appeal and financial performance.", fg="white", wraplength=800, bg=black_2, font=("Sanserif", 12)).place(relx=0.5, rely=0.2, anchor="center")

# list of genres
movie_genres = ['Action', 'Romance', 'Animation', 'Adventure', 'Drama', 'Crime',
                'Horror', 'Comedy', 'Thriller', 'TV Movie', 'Science Fiction',
                'War', 'Family', 'Fantasy', 'Documentary', 'History', 'Mystery',
                'Western', 'Music']

# Create ComboBox for selecting the genre
genre_combo = ctk.CTkComboBox(frame_genre, fg_color=black_1, values=movie_genres, font=("Sanserif", 14), width=400, height=40, corner_radius=10)
genre_combo.place(relx=0.5, rely=0.4, anchor="center")

# Function to get the selected genre
def get_selected_genre():
    selected_genre = genre_combo.get()
    return selected_genre

# for the "Year" frame
tk.Label(frame_year, text="Release Year", fg="white", bg=black_2, font=("Sanserif", 32, "bold")).place(relx=0.5, rely=0.1, anchor="center")
tk.Label(frame_year, text="Select the year in which the movie was released. The year of release can influence its popularity and box office performance.", fg="white", wraplength=800, bg=black_2, font=("Sanserif", 12)).place(relx=0.5, rely=0.2, anchor="center")

# Convert the years into strings
movie_years = [str(int(year)) for year in sorted([2024., 2023., 2022., 1979., 2007., 2027., 2017., 2026., 1992.,
                                           2010., 2020., 2025., 2000., 2009., 2001., 2018., 2021., 2002.,
                                           2014., 1994., 2011., 1972., 2019., 2004., 1997., 2003., 2005.,
                                           2008., 2016., 2015., 1977., 2012., 2013., 1995., 1998., 1999.,
                                           2006., 1974., 1982., 1984., 1966., 1950., 1983., 1993., 1985.,
                                           1946., 1976., 1990., 1987., 1986., 1939., 1989., 1991., 1938.,
                                           1996., 1988., 1968., 1978., 1975.])]

# Create ComboBox for selecting the year
year_combo = ctk.CTkComboBox(frame_year, fg_color=black_1, values=movie_years, font=("Sanserif", 14), width=400, height=40, corner_radius=10)
year_combo.place(relx=0.5, rely=0.4, anchor="center")

# Function to get the selected year
def get_selected_year():
    selected_year = year_combo.get()
    return selected_year

def preprocess_genre(genre):
    # Assuming 'genre' is a string (like 'Action', 'Romance', etc.)
    genre_mapping = {
        'Action': 0, 'Romance': 1, 'Animation': 2, 'Adventure': 3, 'Drama': 4,
        'Crime': 5, 'Horror': 6, 'Comedy': 7, 'Thriller': 8, 'TV Movie': 9,
        'Science Fiction': 10, 'War': 11, 'Family': 12, 'Fantasy': 13, 
        'Documentary': 14, 'History': 15, 'Mystery': 16, 'Western': 17, 'Music': 18
    }
    return genre_mapping.get(genre, -1)  # Default to -1 if genre is not found

def simulate_prediction(budget, genre, year):
    # Get the current working directory
    current_directory = os.getcwd()

    # Define the path to your CSV file
    file_path = os.path.join(current_directory, 'cleaned_top-1000-movies.csv')

    try:
        data = pd.read_csv(file_path)
    except FileNotFoundError:
        output_label.configure(text="Something went wrong: couldn't find 'cleaned_top-1000-movies.csv' file", fg='red')
        return
    output_label.configure(text="The File 'cleaned_top-1000-movies.csv' was read successfully.\n", fg='green')
    

    # Feature columns and target
    X = data[['Production Cost', 'Genre Numeric', 'Year']]
    y = data['Worldwide Gross']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    genre_numeric = preprocess_genre(genre)

    # Prepare the input data for prediction
    input_data = pd.DataFrame({
        'Production Cost': [budget],
        'Genre Numeric': [genre_numeric],
        'Year': [year]
    })

    # Make the prediction
    prediction = model.predict(input_data)

    # Display the result
    output_label.configure(text=f"Predicted Worldwide Gross: ${prediction[0]:,.2f}", fg="green")


# for the "Prediction" frame
def predict_movie_gross():
    # Get the values from the other panels
    budget = float(budget_entry.get())
    genre = get_selected_genre()
    year = int(year_combo.get())
    
    predicted_gross = simulate_prediction(budget, genre, year)
    
    # Update the output label
    output_label.config(text=f"Prediction: {predicted_gross:.2f} million")

tk.Label(frame_prediction, text="PREDICTION WORLD GROSS", fg="white", bg=black_2, font=("Sanserif", 32, "bold")).place(relx=0.5, rely=0.1, anchor="center")
tk.Label(frame_prediction, text="Based on the input data (budget, genre, year), the model will predict the expected world gross for the movie, helping you forecast its financial success.", wraplength=800, fg="white", bg=black_2, font=("Sanserif", 12)).place(relx=0.5, rely=0.2, anchor="center")
predict_button = ctk.CTkButton(frame_prediction, text="Predict", font=("Sanserif", 14), width=150, height=40, corner_radius=10, fg_color=black_1, command=predict_movie_gross)
predict_button.place(relx=0.5, rely=0.3, anchor="center")
output_label = tk.Label(frame_prediction, fg="white", bg=black_2, font=("Sanserif", 12), width=40, height=2, wraplength=500)
output_label.place(relx=0.5, rely=0.7, anchor="center")


# function to switch to next frame
def show_next_frame(current_frame, next_frame):
    if current_frame == frame_budget and next_frame == frame_genre:
        # Check if the budget is valid
        if not check_budget(budget_entry.get()):
            return  # Don't proceed to next frame if the budget is invalid
            pass
        else:
            feedback_label.config(text="")  # Clear previous error message if valid

    # dictionary of labels corresponding to steps
    left_panel_labels = {
        frame_introduction: left_panel_label_introduction,
        frame_budget: left_panel_label_production_cost,
        frame_genre: left_panel_label_genre,
        frame_year: left_panel_label_year,
        frame_prediction: left_panel_label_prediction,
    }
    
    # reset all labels to the default style
    for label in left_panel_labels.values():
        label.config(bg=black_1, fg="white")
    
    # Highlight the label corresponding to the next frame
    if next_frame in left_panel_labels:
        left_panel_labels[next_frame].config(bg=black_2, fg="white")

    current_frame.place_forget()  # Hide the current frame
    next_frame.place(relx=0.5, rely=0.5, anchor="center")  # Show the next frame


def next_step(current_frame, next_frame):
    # create a CustomTkinter Button
    button = ctk.CTkButton(
        current_frame,
        text="Next Step > ",
        fg_color=black_2,
        hover_color="white",
        font=("Sanserif", 18, "bold"),
        text_color="white",  # Default text color
        command=lambda: show_next_frame(current_frame, next_frame),
        width=170,
        height=40,
        corner_radius=25
    )
    
    # change text color on hover
    def on_enter(event):
        button.configure(text_color=black_2, fg_color="white",)  # Set hover text color

    
    def on_leave(event):
        button.configure(text_color="white", fg_color=black_2,)  # Revert to default text color
    
    # bind hover events
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)
    
    # position the button towards the bottom right
    button.place(relx=0.9, rely=0.9, anchor="center")  # Adjust position as needed


def back_step(current_frame, previous_frame):
    # create a CustomTkinter Button for "Back"
    button = ctk.CTkButton(
        current_frame,
        text="< Back ",
        fg_color=black_2,
        hover_color="white",  # Background color on hover
        font=("Sanserif", 18, "bold"),
        text_color="white",  # Default text color
        command=lambda: show_next_frame(current_frame, previous_frame),
        width=170,
        height=40,
        corner_radius=25
    )
    # change text color on hover
    def on_enter(event):
        button.configure(text_color=black_2, fg_color="white",)  # Set hover text color

    
    def on_leave(event):
        button.configure(text_color="white", fg_color=black_2,)  # Revert to default text color

    # bind hover events
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

    # position the button towards the bottom left
    button.place(relx=0.1, rely=0.9, anchor="center")  # Adjust position as needed


# adding the "Next Step" button in the frames
next_step(frame_introduction, frame_budget)
next_step(frame_budget, frame_genre)
next_step(frame_genre, frame_year)
next_step(frame_year, frame_prediction)

# adding the "Back Step" button in the frames
back_step(frame_budget, frame_introduction)
back_step(frame_genre, frame_budget)
back_step(frame_year, frame_genre)
back_step(frame_prediction, frame_year)

# function to exit the program
def on_exit():
    root.quit()

# create and exit button
exit_button = tk.Button(top_bar, width=5, text="X", fg="white", bg=black_1, bd=0, font=("Arial",8, "bold"), command=on_exit)
exit_button.pack(side="right", padx=(0, 20), pady=0, fill="y")  

# function to change the button color when hovering over it
def on_enter(event):
    exit_button.config(bg="red")

# function to revert the button color when the mouse leaves
def on_leave(event):
    exit_button.config(bg=black_1)

# function to change the button color when clicked
def on_click(event):
    exit_button.config(bg="dark red")

# bind events for hover and click
exit_button.bind("<Enter>", on_enter)
exit_button.bind("<Leave>", on_leave)
exit_button.bind("<Button-1>", on_click)

frame_introduction.place(relx=0.5, rely=0.5, anchor="center")

# run the application
root.mainloop()
