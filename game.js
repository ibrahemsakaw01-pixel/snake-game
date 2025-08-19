const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

let dx = 10;
let dy = 0;
let snake = [{ x: 200, y: 200 }];
let food = { x: 100, y: 100 };

document.addEventListener("keydown", changeDirection);

function drawSnake() {
  ctx.fillStyle = "lime";
  snake.forEach(part => ctx.fillRect(part.x, part.y, 10, 10));
}

function drawFood() {
  ctx.fillStyle = "red";
  ctx.fillRect(food.x, food.y, 10, 10);
}

function moveSnake() {
  const head = { x: snake[0].x + dx, y: snake[0].y + dy };
  snake.unshift(head);

  if (head.x === food.x && head.y === food.y) {
    generateFood();
  } else {
    snake.pop();
  }
}

function generateFood() {
  food.x = Math.floor(Math.random() * 40) * 10;
  food.y = Math.floor(Math.random() * 40) * 10;
}

function changeDirection(event) {
  const key = event.keyCode;
  if (key === 37 && dx === 0) { dx = -10; dy = 0; }
  else if (key === 38 && dy === 0) { dx = 0; dy = -10; }
  else if (key === 39 && dx === 0) { dx = 10; dy = 0; }
  else if (key === 40 && dy === 0) { dx = 0; dy = 10; }
}

/* دالة للتحكم باللمس */
function setDirection(dir) {
  if (dir === "up" && dy === 0) { dx = 0; dy = -10; }
  else if (dir === "down" && dy === 0) { dx = 0; dy = 10; }
  else if (dir === "left" && dx === 0) { dx = -10; dy = 0; }
  else if (dir === "right" && dx === 0) { dx = 10; dy = 0; }
}

function drawGame() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  drawFood();
  moveSnake();
  drawSnake();

  if (snake[0].x < 0 || snake[0].x >= canvas.width || snake[0].y < 0 || snake[0].y >= canvas.height) {
    alert("Game Over!");
    document.location.reload();
  }

  setTimeout(drawGame, 100);
}

drawGame();
