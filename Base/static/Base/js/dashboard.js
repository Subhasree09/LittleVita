document.getElementById('childForm').addEventListener('submit', function (event) {
    event.preventDefault();
    // // var childId = document.getElementById('childId').value;
    var childName = document.getElementById('childName').value;
    var dob = document.getElementById('dob').value;
    var childAge = document.getElementById('childage').value;
    // console.log('Child ID:', childId);
    console.log('Child Name:', childName);
    console.log('Date of Birth:', dob);
    console.log('ChildAge:', childAge);
    $('#addChildModal').modal('hide');
});