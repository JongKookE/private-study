const images = ["0.jpg", "1.jpg", "2.jpg"];

const chosen_image = images[Math.floor(Math.random() * images.length)];

const bg_image = document.createElement("img");

bg_image.src = `img/${chosen_image}`;

document.body.appendChild(bg_image);