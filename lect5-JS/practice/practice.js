// Greeting
function hello() {
	const greeting = document.querySelector("#hello");
	if (greeting.innerHTML === "Good Buy!") {
		greeting.innerHTML = "Hello!"
	} else {
		greeting.innerHTML = "Good Buy!"
	}
}

// Counter
// Look for the counter in the local storage
if (!localStorage.getItem('counter')) {
	// If there is no => create it
	localStorage.setItem('counter', 0);
}

function count() {
	let counter = localStorage.getItem('counter');
	counter++;

	document.querySelector("#counter").innerHTML = `Counter is now ${counter}.`

	localStorage.setItem('counter', counter);

	if (counter % 10 === 0) {
		alert(`${counter}!`);
	}
}

// Run all the functions when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
	// Greeting
	document.querySelector("#hello").onclick = hello;

	// Counter
	document.querySelector('#count').onclick = count;

	// Rest-timer
	let time = 0;
	function timer() {
		// Run the timer
		time++;
		// Put time indicator into the DOM element
		document.querySelector('#resttime').innerHTML = time;
		// Reset if there is an action on page
		document.onclick = () => time = 0;
	}
	let interval = setInterval(timer, 1000);
	// Stop timer
	function stop() {
		clearInterval(interval);
	}
	document.querySelector('a').onclick = stop;

	// Greeting by name
	document.querySelector('form').onsubmit = () => {
		let name = document.querySelector('#name').value;
		// Capitalize the name
		name = name.charAt(0).toUpperCase() + name.slice(1);
		alert(`Hello, ${name}`);
	}

	// Colors
	// Get an array of buttons
	// For each button (i) add event handler:
	// On click we take data from the dataset property of the button and apply it to the style of the header h1
	document.querySelectorAll('.colors').forEach(i =>
		i.onclick = () => {
			document.querySelector('h1').style.color = i.dataset.color;
		});

	// Dropdown colors
	document.querySelector('select').onchange = function() {
		document.querySelector('h1').style.color = this.value;
	}
});