const passwordBox = document.getElementById("password");
const length = 12;

const uppperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const lowerCase = "abcdefghijklmnopqrstuvwxyz";
const numbers = "0123456789";
const allChars = uppperCase + lowerCase + numbers;

function generatePassword() {
  let password = "";
  password += uppperCase[Math.floor(Math.random() * uppperCase.length)];
  password += lowerCase[Math.floor(Math.random() * lowerCase.length)];
  password += numbers[Math.floor(Math.random() * numbers.length)];
  password += uppperCase[Math.floor(Math.random() * uppperCase.length)];

  while (length > password.length) {
    password += allChars[Math.floor(Math.random() * allChars.length)];
  }
  passwordBox.value = password;
}

function copyPass() {
  passwordBox.select();
  document.execCommand("copy");
}
