import tkinter as tk
import recommendation
def handle_recommendation():
    # Retrieve the user's input from the entry widget
    seed_track_id = entry.get()

    # Authenticate with Spotify and generate recommendations
    sp = recommendation.authenticate_spotify()
    recommendations = recommendation.generate_recommendations(sp, seed_track_id)

    # Display the recommendations in the GUI
    recommendation_text.delete(1.0, tk.END)
    for idx, track in enumerate(recommendations):
        recommendation_text.insert(tk.END, f"Recommendation {idx + 1}: {track['name']} by {track['artists'][0]['name']}\n")

if __name__ == '__main__':
    # Create the main window
    window = tk.Tk()
    window.title("Spotify Recommendation System")

    # Create and place GUI elements
    label = tk.Label(window, text="Enter the ID of the track:")
    label.pack()

    entry = tk.Entry(window)
    entry.pack()

    button = tk.Button(window, text="Recommend", command=handle_recommendation)
    button.pack()

    recommendation_text = tk.Text(window, height=5, width=50)
    recommendation_text.pack()

    # Run the GUI main loop
    window.mainloop()
```
