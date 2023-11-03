
function validateEmail(email) {
    if(email){
        const emailRegex = /^[^\s@]+@[^\s@]+\.[A-Za-z.]+$/;
        if (!emailRegex.test(email)) {
            return false;
        }else{
            return true;
        }
    }
    else{
        const emailField = document.getElementById('EmailID');
        const email = emailField.value;
        const emailRegex = /^[^\s@]+@[^\s@]+\.[A-Za-z.]+$/;
        var error=document.getElementById('emailerror');
        if (!emailRegex.test(email)) {
            error.innerHTML='**Invalid email format. Please enter a valid email address.**';
            emailField.focus();
            return false;
        }
        else{
            error.innerHTML='';
        }
        console.log('Sending email:', email);
        fetch('check_email', {
            method: 'POST',
            body: JSON.stringify({ 'email': email }), 
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken') 
            },
        })
        .then(response => {
            console.log('Response from server:', response);
            return response.json();
        }) 
        .then(data => {
            console.log('Data received:', data);
            if (data.exists === true) {
                error.innerHTML = '**Email already exists. Please choose another email.**';
                emailField.focus();
            } else {
                error.innerHTML = '';
            }
        })
        .catch(error => {
            alert('An error occurred while processing the request. Please try again later.');
            emailField.focus();
        });
        return true;
    }
}

function validateFirstName(name) {
    if(name){
        const regex = /^[A-Za-z ]{3,}$/;
        if (!regex.test(name)) {
            return false;
        }
        else{
            return true;
        }
    }
    else{
        const namefield = document.getElementById('FirstName');
        const value = namefield.value;
        const regex = /^[A-Za-z ]{3,}$/;
        var error=document.getElementById('FirstNameerror');
        if (!regex.test(value)) {
            error.innerHTML='**Invalid FirstName. Name should be more than 2 characters. Please enter only alphabetic characters.**'
            field.focus();
            return false;
        }
        else{
            error.innerHTML='';
        }
        return true;
    }
}

function validateLastName(name) {
    if(name){
        const regex = /^[A-Za-z ]+$/;
        if (!regex.test(name)) {
            return false;
        }
        else{
            return true;
        }
    }
    else{
        const field = document.getElementById('LastName');
        const value = field.value;
        const regex = /^[A-Za-z ]+$/;
        var error=document.getElementById('LastNameerror');
        if (!regex.test(value)) {
            error.innerHTML='**Invalid LastName. Please enter only alphabetic characters.**'
            field.focus();
            return false;
        }
        else{
            error.innerHTML='';
        }
        return true;
    }
}



function validateMobileNumber(mobile) {
    if(mobile){
        const regex = /^\d{10}$/;
        if (!regex.test(mobile)) {
            return false;
        }
        else{
            return true;
        }
    }
    else{
        const mobileNumberField = document.getElementById('MobileNumber');
        const mobileNumber = mobileNumberField.value;
        const regex = /^\d{10}$/;
        var error=document.getElementById('moberror');
        if (!regex.test(mobileNumber)) {
            error.innerHTML='**Invalid mobile number. Please enter a 10-digit numeric mobile number.**';
            mobileNumberField.focus();
            return false;
        }
        else{
            error.innerHTML='';
        }
        return true;
    }
}


function validateDateOfBirth(dob) {
    if(dob){
        const today = new Date();
        const selectedDate = new Date(dob);
        if (isNaN(selectedDate) || selectedDate > today) {
            return false;
        }
        else{
            return true;
        }
    }
    else{
        const dobField = document.getElementById('DOB');
        const dob = dobField.value;
        const today = new Date();
        const selectedDate = new Date(dob);
        var error=document.getElementById('doberror');
        if (isNaN(selectedDate) || selectedDate > today) {
            error.innerHTML='**Invalid date of birth. Please select a valid date.**';
            dobField.focus();
            return false;
        }
        else{
            error.innerHTML='';
        }
        return true;
    }
}

try{
    module.exports={
        validateEmail,
        validateFirstName,
        validateLastName,
        validateMobileNumber,
        validateDateOfBirth
    }
}
catch{
    
}


