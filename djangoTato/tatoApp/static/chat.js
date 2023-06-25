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
    event.preventDefault()
    console.log("aca")
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
  
        var messagesContainer = document.querySelector('.messages .msg');
  
        var messageElement = document.createElement('p');
        messageElement.style.color = "black"
        messageElement.textContent = message;
        messageElement.classList.add('question');
        
        var timestampElement = document.createElement('span');
        timestampElement.style.color = "black"
        timestampElement.textContent = getCurrentTime();
        messageElement.appendChild(timestampElement);
        
        messagesContainer.appendChild(messageElement);
  
        if (respuesta) {
          var responseElement = document.createElement('p');
          responseElement.textContent = respuesta;
          responseElement.classList.add('response');
          responseElement.style.color = "black"
          var responseTimestampElement = document.createElement('span');
          responseTimestampElement.textContent = getCurrentTime();
          responseElement.appendChild(responseTimestampElement);
  
          messagesContainer.appendChild(responseElement);
        }
      })
      .catch(function (error) {
        console.error('Error:', error);
      });
  }
  
  function getCurrentTime() {
    var now = new Date();
    var hours = now.getHours().toString().padStart(2, '0');
    var minutes = now.getMinutes().toString().padStart(2, '0');
    return hours + ':' + minutes;
  }