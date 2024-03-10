console.log("Hello from script.js!");
// setTimeout(function() {
// 	var errorElement = document.querySelector('.error');
// 	if (errorElement) {
// 	  location.reload(true);
// 	}
//   }, 5000);
//   setTimeout(function(){
// 	var successElement=document.querySelector('.success');
// 	if(successElement){
// 	  location.reload(true);
// 	}
//   },5000);

document.querySelector('.cancel-message').addEventListener('click', function() {
    var messageBox = document.querySelector('.message-box');
    messageBox.style.display = 'block'; // Show the message box
	messageBox.style.display = 'none';
    
});

setTimeout(function(){
	var messageBox = document.querySelector('.message-box');
	messageBox.style.display = 'block'; // Show the message box
	messageBox.style.display = 'none';
},3000);