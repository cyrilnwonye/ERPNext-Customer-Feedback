var form = document.querySelector('form');
var data = new FormData(form);


let urlString = window.location.href;

let paramString = urlString.split('?')[1];
let queryString = new URLSearchParams(paramString);
for(let pair of queryString.entries()) {
    document.getElementById('delivery_note_number').value= pair[1];
}



    document.addEventListener('submit', function (event) {

    event.preventDefault();

    fetch('http://127.0.0.1:8020/api/method/customer_feedback.services.rest.get_customer_feedback', {
        method: 'POST',
        body: new FormData(event.target),
    }).then(function (response) {
        if (response.ok) {

            // document.getElementById("responseHead").innerHTML = response.message;
            // document.getElementById('responseBody').innerHTML = response.message;

            $(document).ready(function(){
                $("#myModal").modal('show');
            });

            return response.json();
        }
        return Promise.reject(response);
    }).then(function (data) {

        if(data.message == "Success"){
            document.getElementById('responseHead').innerHTML = "Success";
            document.getElementById('responseBody').innerHTML = "We have received your feedback. Thank you!";
        }else{
            document.getElementById('responseHead').innerHTML = "Message";
            document.getElementById('responseBody').innerHTML = "There was a problem submitting your feedback!";
        }
        

        console.log(data.message);

        

    }).catch(function (error) {
    console.warn(error);
        alert(error.message)
    });
});


function dismisModal(){
    $('#myModal').modal('hide');
    location.href = 'https://naragenergy.com';
}

