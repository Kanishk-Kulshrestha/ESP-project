const char MAIN_page[] PROGMEM = R"=====(
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Login Page</title>
  <style>
    .container {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }

    form {
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    input, button {
      margin: 5px;
      padding: 10px;
    }

    .error-message {
      color: red;
      margin-bottom: 10px;
    }

    .switch {
  position: relative;
  display: inline-block;
  width: 60px;
  height: 34px;
}

.switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #ccc;
  -webkit-transition: .4s;
  transition: .4s;
}

.slider:before {
  position: absolute;
  content: "";
  height: 26px;
  width: 26px;
  left: 4px;
  bottom: 4px;
  background-color: white;
  -webkit-transition: .4s;
  transition: .4s;
}

input:checked + .slider {
  background-color: #2196F3;
}

input:focus + .slider {
  box-shadow: 0 0 1px #2196F3;
}

input:checked + .slider:before {
  -webkit-transform: translateX(26px);
  -ms-transform: translateX(26px);
  transform: translateX(26px);
}

.slider.round {
  border-radius: 34px;
}

.slider.round:before {
  border-radius: 50%;
}

  </style>
</head>
<body>
  <div class="container">
    <form id="loginForm" onsubmit="checkCredentials(event)">
      <input type="text" id="username" placeholder="Username" required>
      <input type="password" id="password" placeholder="Password" required>
      <div id="errorMessage" class="error-message"></div>
      <button type="submit" id="loginBtn">Login</button>
    </form>
    
    <label class="switch" id="switch">
        <input type="checkbox" onclick="toggleSwitch()">
        <span class="slider round"></span>
      </label>

  </div>
  <script>

    function sendData(pos) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
        console.log(this.responseText);
        }
    };
    xhttp.open("GET", "setPOS?servoPOS="+pos, true);
    xhttp.send();
    }

    function toggleSwitch() {
        var switchElement = document.getElementById("switch");
        var isChecked = switchElement.querySelector("input").checked;
        if (isChecked) {
        console.log("Switch is ON");
        sendData(100);
        // Add actions to perform when switch is ON
        } else {
        console.log("Switch is OFF");
        sendData(0);
        // Add actions to perform when switch is OFF
        }
    }


    document.getElementById('switch').style.display = 'none';
    function checkCredentials(event) {
      event.preventDefault();

      const username = document.getElementById('username').value;
      const password = document.getElementById('password').value;

      if (username === 'admin' && password === 'password') {
        document.getElementById('loginForm').style.display = 'none';
        document.getElementById('switch').style.display = 'block';
        document.getElementById('errorMessage').innerText = 'Login Successful!';

      } else {
        document.getElementById('errorMessage').innerText = 'Invalid username or password';
      }
    }
  </script>
</body>
</html>
)=====";
