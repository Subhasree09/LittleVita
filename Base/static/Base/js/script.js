console.log("Hello from script.js!");

// For the pop up message box

document.querySelector('.cancel-message').addEventListener('click', function () {
	var messageBox = document.querySelector('.message-box');
	messageBox.style.display = 'block'; // Show the message box
	messageBox.style.display = 'none';

});


setTimeout(function () {
	var messageBox = document.querySelector('.message-box');
	messageBox.style.display = 'block'; // Show the message box
	messageBox.style.display = 'none';
}, 3000);

// For the navbar to hide when scrolling down and show when scrolling up
let lastScrollTop = 0;
const navbar = document.querySelector('.navbar');

window.addEventListener('scroll', () => {
	const scrollTop = document.documentElement.scrollTop;
	if (scrollTop < lastScrollTop) {
		navbar.classList.remove('hide');
	} else {
		navbar.classList.add('hide');
	}
	lastScrollTop = scrollTop;
});