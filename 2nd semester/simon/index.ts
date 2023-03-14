const colors = ["red", "green", "blue", "yellow"]

function main() {

	let sequence = [colors[Math.random()]]

	let waiting = true
	let running = true
	// while (running) {
		

		// while (waiting) {} // wait until a button is pressed
	// }
	setInterval(addColor.bind(addColor, sequence), 1000)

	// sequence.push(colors[getRandomInt(0, 4)])
	// displaySequence(sequence)

	// addColor(sequence)
}

function addColor(sequence) {
	sequence.push(colors[getRandomInt(0, 4)])

	displaySequence(sequence)
}

// taken from MDN docs
function getRandomInt(min, max) {
	min = Math.ceil(min)
	max = Math.floor(max)
	return Math.floor(Math.random() * (max - min) + min)
}

function displaySequence(sequence, time = 1000, index = 0) {
	const red = document.getElementById("red")
	const green = document.getElementById("green")
	const blue = document.getElementById("blue")
	const yellow = document.getElementById("yellow")

	red.style.backgroundColor = '#db6962'
	green.style.backgroundColor = '#85ad58'
	blue.style.backgroundColor = '#6991d5'
	yellow.style.backgroundColor = '#cca738'

	for (let i = index; i < sequence.length; i++) {
		const item = sequence[i];
		switch (item) {
			case "red":
				red.style.backgroundColor = '#ffffff'
				setTimeout(() => {
					displaySequence(sequence, time, index + 1)
				}, time)
				break
			case "green":
				green.style.backgroundColor = '#ffffff'
				setTimeout(() => {
					displaySequence(sequence, time, index + 1)
				}, time)
				break
			case "blue":
				blue.style.backgroundColor = '#ffffff'
				setTimeout(() => {
					displaySequence(sequence, time, index + 1)
				}, time)
				break
			case "yellow":
				yellow.style.backgroundColor = '#ffffff'
				setTimeout(() => {
					displaySequence(sequence, time, index + 1)
				}, time)
				break
		}	
	}
}

function wait(secs) {
	const start = Date.now()
	while (Date.now() - start < secs * 100) {}
}