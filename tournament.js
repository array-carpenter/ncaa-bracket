const teams = ["UConn", "Stetson", "FAU", "Northwestern", "San Diego St", "UAB", "Auburn", "Yale",
               "BYU", "Duquesne", "Illinois", "Morehead St", "Washington St", "Drake", "Iowa State", "S Dakota St",
               "North Carolina", "HOW/WAG", "Mississippi St", "Michigan St", "Saint Mary's", "Grand Canyon", "Alabama", "Charleston",
               "Clemson", "New Mexico", "Baylor", "Colgate", "Dayton", "Nevada", "Arizona", "Long Beach St",
               "Houston", "Longwood", "Nebraska", "Texas A&M", "Wisconsin", "James Madison", "Duke", "Vermont",
               "Texas Tech", "NC State", "Kentucky", "Oakland", "Florida", "BOIS/COL", "Marquette", "Western Kentucky",
               "Purdue", "MTST/GRAM", "Utah State", "TCU", "Gonzaga", "McNeese", "Kansas", "Samford",
               "South Carolina", "Oregon", "Creighton", "Akron", "Texas", "UVA/CSU", "Tennessee", "St. Peter's"];

function simulateGame(team1, team2) {
    return Math.random() < 0.5 ? team1 : team2;
}

function simulateRound(teams) {
    let winners = [];
    for (let i = 0; i < teams.length; i += 2) {
        const winner = simulateGame(teams[i], teams[i + 1]);
        winners.push(winner);
    }
    return winners;
}

function startTournament() {
    let currentTeams = [...teams]; // Clone the original array
    const roundNames = ["Second Round", "Round of 32", "Sweet 16", "Elite 8", "Final 4", "Championship"];
    let resultsElement = document.getElementById("tournamentResults");
    resultsElement.innerHTML = ''; // Clear previous results

    for (let i = 0; i < roundNames.length; i++) {
        let roundResults = `<div class="card mt-3">
                                <div class="card-header">
                                    ${roundNames[i]}
                                </div>
                                <div class="card-body">`;

        currentTeams = simulateRound(currentTeams);
        currentTeams.forEach((team, index) => {
            roundResults += `<p class="card-text">Game ${index + 1} winner: ${team}</p>`;
        });

        roundResults += `    </div>
                          </div>`;
        resultsElement.innerHTML += roundResults;
        if (currentTeams.length === 1) break; // If it's the final winner
    }

    resultsElement.innerHTML += `<div class="mt-4 alert alert-success" role="alert">
                                    <h4 class="alert-heading">Tournament Winner!</h4>
                                    <p>Your Randomized 2024 NCAA Men's Tournament Winner is: ${currentTeams[0]}</p>
                                  </div>`;
}

