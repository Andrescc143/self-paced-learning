const botOptions = ["Rock", "Papper", "Scissors"];


function runGame(userOption) {
    const botChoice = botOptions[Math.floor(Math.random() * botOptions.length)];

    if (userOption == botChoice) {
        console.log(`It's a tie ! User: ${userOption} vs Bot: ${botChoice}`)
    }
    else if (
        (userOption == "Rock" && botChoice == "Scissors")
        || (userOption == "Paper" && botChoice == "Rock")
        || (userOption == "Scissors" && botChoice == "Paper")
        ) {
        console.log(`User win ! User: ${userOption} vs Bot: ${botChoice}`)
    }
    else {
        console.log(`Bot win ! User: ${userOption} vs Bot: ${botChoice}`)
    }
}


console.log("Let's play !");
var userInput = "Rock";

runGame(userInput);