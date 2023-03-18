// Update scoreboard
function updateLeaderboard() {
    console.log("Updating Leaderboard");

    // Call python's get_scores function
    eel.get_scores()(function (response) {
        console.log(response)

        // Parse JSON string
        var json_response = JSON.parse(response);

        // Get scores and names
        var scores = json_response["scores"];
        var names = json_response["names"];

        var N_scores = scores.length;

        // Clear table html
        var table_html = "";

        // Populate leaderboard
        for (var i = 0; i < N_scores; i++) {
            // New row
            table_html += "<tr><td class='name row'>" + names[i] + "</td><td class='score row'>" + scores[i] + "</td></tr>";
        }

        // Update html
        document.getElementById("leaderboard_tbody").innerHTML = table_html;
    })
}

// Check leaderboard every 10 seconds and update scoreboard on html
updateLeaderboard()
setInterval(updateLeaderboard, 10 * 1000);