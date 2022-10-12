const input = document.querySelector("input");
const main = document.querySelector("main");
const btn = document.querySelector("button");
const code = document.querySelector(".qrcode");
const qrcodeimg = document.querySelector(".qrcode img");
btn.addEventListener("click", () => {
  const inputval = input.value;
  if (!inputval) return;
  qrcodeimg.src = ` https://api.qrserver.com/v1/create-qr-code/?size=170x170&data=${inputval} `;
  qrcodeimg.addEventListener("load", () => {
    // btn.innerHTML = "Generating QR Code....";
    code.style.display = "flex";
  });
});
