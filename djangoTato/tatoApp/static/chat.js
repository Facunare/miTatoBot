function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
function sendMessage(event) {
  event.preventDefault();
  console.log("aca");
  var formMessage = new FormData(document.getElementById('formMessage'));

  fetch('../ask/', {
    method: 'POST',
    body: formMessage,
    headers: {
      'X-CSRFToken': getCookie('csrftoken'),
      'X-Requested-With': 'XMLHttpRequest'
    }
  })
    .then(function (res) {
      return res.json();
    })
    .then(function (data) {
      var message = data.mensaje;
      var respuesta = data.respuesta;
      const input = document.querySelector(".input");
      var messagesContainer = document.querySelector('.messages .msg');
      if (input.value !== "") {
        var messageElement = document.createElement('p');
        messageElement.style.color = "black";
        messageElement.textContent = message;
        messageElement.classList.add('question');

        var timestampElement = document.createElement('span');
        timestampElement.style.color = "black";
        timestampElement.textContent = getCurrentTime();
        messageElement.appendChild(timestampElement);

        messagesContainer.appendChild(messageElement);

        if (respuesta) {
          var responseElement = document.createElement('p');
          responseElement.textContent = respuesta;
          responseElement.classList.add('response');
          responseElement.style.color = "black";
          var responseTimestampElement = document.createElement('span');
          responseTimestampElement.textContent = getCurrentTime();
          responseElement.appendChild(responseTimestampElement);

          messagesContainer.appendChild(responseElement);
        }

        input.value = "";
      }

        // var deleteForm = document.createElement('form');
        // deleteForm.action = 'deleteChat/';
        // deleteForm.method = 'post';
        // deleteForm.classList.add('delete');

        // var deleteButton = document.createElement('button');
        // deleteButton.innerHTML = '<i class="bx bx-trash"></i>';

        // deleteForm.appendChild(deleteButton);
        // messagesContainer.appendChild(deleteForm);
        
      })
      .catch(function (error) {
        console.error('Error:', error);
      });
    }
    
      // function deleteMessages(event) {
      //   event.preventDefault();
    
      //   var deleteForm = new FormData(document.getElementById('deleteForm'));
      //   var form = document.getElementById('deleteForm')
      //   fetch('../deleteChat/', {
      //     method: 'POST',
      //     body: deleteForm,
      //     headers: {
      //       'X-CSRFToken': getCookie('csrftoken'),
      //       'X-Requested-With': 'XMLHttpRequest'
      //     }
      //   })
      //     .then(function (res) {
      //       return res.json();
      //     })
      //     .then(function (data) {
      //       console.log("HOLAAA")
      //       const messages = document.querySelectorAll('.message')
      //       for(let message of messages){
      //         message.remove()
      //       }
      //       form.style.display = "none"
    
      //       console.log('CSRF Token:', getCookie('csrftoken'));
      //     })
      //     .catch(function (error) {
      //       console.error('Error:', error);
      //     });
      // }




function getCurrentTime() {
    var now = new Date();
    var hours = now.getHours().toString().padStart(2, '0');
    var minutes = now.getMinutes().toString().padStart(2, '0');
    return hours + ':' + minutes;
  }