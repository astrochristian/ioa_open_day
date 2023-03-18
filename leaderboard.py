import eel
import pandas as pd
# Initialiase eel
eel.init("web")


@eel.expose
def get_scores():
    # Function to get scoreboard
    # Open csv file
    df = pd.read_csv("scoreboard.csv")

    # Load columns as python lists
    names = df["name"].to_list()
    score = df["score_tot"].to_list()

    # Pass data back as string JSON object
    json_string = '{"names":%s, "scores":%s}' % (names, score)

    # Make sure all quotes are double
    json_string = json_string.replace("'", '"')

    return json_string


# Start eel
eel.start("index.html", mode="chrome_app")
