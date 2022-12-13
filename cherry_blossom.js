// Get the canvas and its context
var canvas = document.getElementById("sky");
var context = canvas.getContext("2d");

// Set the canvas dimensions to match the window
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

// Define a function to create a new cherry blossom
function createBlossom() {
  // Randomize the blossom's starting position and size
  var x = Math.random() * canvas.width;
  var y = Math.random() * canvas.height;
  var size = Math.random() * 30 + 20;

  // Randomize the blossom's speed and direction
  var speedX = Math.random() * 2 - 1;
  var speedY = Math.random() * 2 + 1;

  // Create an object to represent the blossom
  var blossom = {
    x: x,
    y: y,
    size: size,
    speedX: speedX,
    speedY: speedY,
    update: function() {
      // Update the blossom's position
      this.x += this.speedX;
      this.y += this.speedY;

      // If the blossom goes off the bottom of the screen,
      // move it back to the top
      if (this.y > canvas.height) {
        this.x = Math.random() * canvas.width;
        this.y = 0;
      }
    },
    draw: function() {
      // Draw the blossom as a pink circle
      context.beginPath();
      context.arc(this.x, this.y, this.size, 0, Math.PI * 2);
      context.fillStyle = "pink";
      context.fill();
    }
  };

  return blossom;
}

// Create an array to store the blossom objects
var blossoms = [];

// Create a new blossom every 0.1 seconds
setInterval(function() {
  blossoms.push(createBlossom());
}, 100);

// Update and draw the blossoms every frame
function updateAndDraw() {
  // Clear the screen
  context.clearRect(0, 0, canvas.width, canvas.height);

  // Update and draw each blossom
  for (var i = 0; i < blossoms.length; i++) {
    blossoms[i].update();
    blossoms[i].draw();
  }

  // Request another frame
  requestAnimationFrame(updateAndDraw);
}

// Start the animation
updateAndDraw();
