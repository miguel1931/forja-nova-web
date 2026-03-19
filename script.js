const status = document.querySelectorAll('section ul li');
// Example dynamic behavior: highlight each status item one by one.
let idx = 0;
setInterval(() => {
  status.forEach((el, i) => el.style.opacity = i === idx ? '1' : '0.65');
  idx = (idx + 1) % status.length;
}, 2700);
