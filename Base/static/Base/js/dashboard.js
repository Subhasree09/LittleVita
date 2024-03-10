document.getElementById('childForm').addEventListener('submit', function (event) {
    // event.preventDefault();
    // // var childId = document.getElementById('childId').value;
    var childName = document.getElementById('childName').value;
    var dob = document.getElementById('dob').value;
    // var childSex = document.getElementById('childage').value;
    // console.log('Child ID:', childId);
    console.log('Child Name:', childName);
    console.log('Date of Birth:', dob);
    // console.log('ChildAge:', childAge);
    $('#addChildModal').modal('hide');
});


// Add this JavaScript code to your existing scripts

document.getElementById('openFormBtn').addEventListener('click', function() {
    document.getElementById('popupFormContainer').style.display = 'block';
    document.querySelector('.overlay').style.display = 'block';
});

document.getElementById('closeFormBtn').addEventListener('click', function() {
    document.getElementById('popupFormContainer').style.display = 'none';
    document.querySelector('.overlay').style.display = 'none';
});

