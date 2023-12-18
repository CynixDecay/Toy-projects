const API_URL =
  "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=Example";

let imgbox = document.getElementById("img-box");
let qrImage = document.getElementById("qrImage");
let qrText = document.getElementById("qrText");

function generateQR() {
  if (qrText.value !== "") {
    qrImage.src =
      "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=" +
      qrText.value;
    imgbox.classList.add("show-img");
  } else {
    qrText.classList.add("error");
    setTimeout(() => {
      qrText.classList.remove("error");
    }, 1000);
  }
}
