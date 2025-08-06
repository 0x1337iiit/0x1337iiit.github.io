---
layout: none
---
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Mission Briefing - 0x1337 CTF</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    html, body {
      margin: 0;
      padding: 0;
      font-family: 'Courier New', Courier, monospace;
      background: black;
      color: #00ffcc;
      overflow: hidden;
    }

    body.scrolling {
      overflow-y: auto;
    }

    .digital-rain {
      position: fixed;
      width: 100%;
      height: 100%;
      z-index: -1;
      overflow: hidden;
    }

    .rain-drop {
      position: absolute;
      color: #00ffcc;
      font-family: 'Courier New', monospace;
      font-size: 14px;
      opacity: 0.7;
      animation: fall linear infinite;
      text-shadow: 0 0 5px #00ffcc;
    }

    @keyframes fall {
      0% {
        transform: translateY(-100vh);
        opacity: 1;
      }
      100% {
        transform: translateY(100vh);
        opacity: 0;
      }
    }

    .scan-line {
      position: fixed;
      width: 100%;
      height: 2px;
      background: linear-gradient(90deg, transparent, #00ffcc, transparent);
      animation: scan 3s linear infinite;
      z-index: 1;
      opacity: 0.5;
    }

    @keyframes scan {
      0% { top: -2px; }
      100% { top: 100vh; }
    }

    .typing-container {
      padding: 5vw;
      font-size: 5vw;
      white-space: pre-line;
      line-height: 1.5;
      animation: fadeIn 1s ease-in-out, textGlitch 0.1s infinite;
      text-shadow: 0 0 10px #00ffcc;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(30px); }
      to { opacity: 1; transform: translateY(0); }
    }

    @keyframes textGlitch {
      0%, 98% { text-shadow: 0 0 10px #00ffcc; }
      99% { text-shadow: 2px 0 #ff0000, -2px 0 #0000ff, 0 0 10px #00ffcc; }
      100% { text-shadow: 0 0 10px #00ffcc; }
    }

    .poster {
      display: none;
      justify-content: center;
      align-items: center;
      height: 100vh;
      animation: zoomIn 1s ease-in;
    }

    .poster img {
      width: 90vw;
      max-width: 600px;
      border: 5px solid #00ffcc;
      border-radius: 10px;
    }

    @keyframes zoomIn {
      from { transform: scale(0.6); opacity: 0; }
      to { transform: scale(1); opacity: 1; }
    }

    .destruct {
      color: red;
      font-size: 7vw;
      text-align: center;
      margin-top: 20vh;
      animation: flicker 0.2s infinite;
    }

    @keyframes flicker {
      0%, 100% { opacity: 1; }
      50% { opacity: 0.2; }
    }

    @keyframes buttonGlow {
      from { 
        box-shadow: 0 0 10px #00ffcc, inset 0 0 10px rgba(0,255,204,0.1);
        text-shadow: 0 0 10px #00ffcc;
      }
      to { 
        box-shadow: 0 0 20px #00ffcc, inset 0 0 20px rgba(0,255,204,0.3);
        text-shadow: 0 0 20px #00ffcc;
      }
    }

    @media (min-width: 768px) {
      .typing-container {
        font-size: 2vw;
      }
      .destruct {
        font-size: 4vw;
      }
    }
  </style>
</head>
<body>

<audio id="bgMusic" loop>
  <source src="theme.mp3" type="audio/mpeg">
</audio>

<div class="digital-rain" id="digitalRain"></div>
<div class="scan-line"></div>

<div id="content" class="typing-container">
  <div id="startButton" style="position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); border: 2px solid #00ffcc; color: #00ffcc; padding: 20px 40px; border-radius: 10px; cursor: pointer; font-weight: bold; font-size: 18px; z-index: 1000; text-shadow: 0 0 10px #00ffcc; animation: buttonGlow 2s ease-in-out infinite alternate;">
    🎯 START MISSION BRIEFING
  </div>
</div>

<div id="poster" class="poster">
  <img src="poster.jpeg" alt="CTF Poster">
</div>

<script>
  const briefing = `
>> Your mission, should you choose to accept it:

Mr. Zuck, a rogue AI from Meta, has infiltrated our campus network. 
He's embedding secret exploits within everyday apps.

Your task? Infiltrate his fortress — code-named "The Gram".

> Challenge codename: Zuck CTF

>> Objective:
Find and exploit the vulnerabilities hidden within Zuck’s digital empire.

> Timeline: 6 August 9pm. The storm hits then.

Zuck has eyes everywhere. Trust no one.

This message will self-destruct in 10 seconds.

Good luck, hacker.
`;

  const contentEl = document.getElementById("content");
  const posterEl = document.getElementById("poster");
  const startButton = document.getElementById("startButton");
  const bgMusic = document.getElementById("bgMusic");

  // Digital rain effect
  function createDigitalRain() {
    const rainContainer = document.getElementById('digitalRain');
    const characters = '01アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン';
    
    for (let i = 0; i < 50; i++) {
      const drop = document.createElement('div');
      drop.className = 'rain-drop';
      drop.style.left = Math.random() * 100 + '%';
      drop.style.animationDuration = (Math.random() * 3 + 2) + 's';
      drop.style.animationDelay = Math.random() * 2 + 's';
      drop.textContent = characters[Math.floor(Math.random() * characters.length)];
      rainContainer.appendChild(drop);
      
      // Change character periodically
      setInterval(() => {
        drop.textContent = characters[Math.floor(Math.random() * characters.length)];
      }, 100);
    }
  }

  // Initialize digital rain
  createDigitalRain();

  let index = 0;

  function typeNextChar() {
    if (index < briefing.length) {
      contentEl.innerHTML += briefing.charAt(index);
      index++;
      window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });
      setTimeout(typeNextChar, 50);
    } else {
      setTimeout(() => {
        contentEl.innerHTML = '<div class="destruct">SELF DESTRUCT INITIATED</div>';
        setTimeout(() => {
          document.body.classList.add('scrolling');
          contentEl.style.display = 'none';
          posterEl.style.display = 'flex';
          localStorage.setItem('briefingShown', 'true');
        }, 3000);
      }, 2000);
    }
  }

  function startBriefing() {
    startButton.style.display = 'none';
    try {
      bgMusic.volume = 0.1; // soft hum
      bgMusic.play().catch(() => {
        console.warn("Autoplay blocked, waiting for user interaction");
      });
    } catch (e) {
      console.error("Audio playback error:", e);
    }
    typeNextChar();
  }

  if (startButton) {
    startButton.addEventListener('click', startBriefing);
  }

  window.onload = () => {
    if (localStorage.getItem('briefingShown')) {
      // Already viewed, show poster directly
      startButton.style.display = 'none';
      document.body.classList.add('scrolling');
      contentEl.style.display = 'none';
      posterEl.style.display = 'flex';
    } else {
      // Await user to start
      startButton.style.display = 'block';
    }
  };
</script>

</body>
</html>
