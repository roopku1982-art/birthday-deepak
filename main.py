from flask import Flask, render_template_string
import os

app = Flask(__name__)

# Aapke dost ki details
naam = "Deepak"
umar = 15

# Hamari beautiful website ka HTML, CSS aur Animation code
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Happy Birthday {{ name }}!</title>
    <style>
        body {
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            overflow: hidden;
            position: relative;
        }
        .card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
            text-align: center;
            max-width: 400px;
            color: white;
            z-index: 10;
        }
        h1 { color: #00ffff; font-size: 3rem; margin-bottom: 10px; text-shadow: 0 0 15px rgba(0, 255, 255, 0.6); }
        .msg { font-size: 1.3rem; color: #fffb00; font-style: italic; margin-bottom: 30px; }
        .btn {
            background: linear-gradient(45deg, #00c6ff, #0072ff);
            color: white;
            border: none;
            padding: 15px 35px;
            font-size: 1.2rem;
            border-radius: 50px;
            cursor: pointer;
            font-weight: bold;
            box-shadow: 0 5px 15px rgba(0, 198, 255, 0.4);
        }
        .overlay {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(15, 32, 39, 0.9); backdrop-filter: blur(8px);
            display: flex; justify-content: center; align-items: center;
            z-index: 100; opacity: 0; pointer-events: none; transition: all 0.5s ease;
        }
        .popup-box {
            background: linear-gradient(135deg, #1d2671, #c33764); border: 3px solid #00ffff;
            padding: 40px; border-radius: 20px; text-align: center; color: white;
            box-shadow: 0 0 50px rgba(0, 255, 255, 0.5); transform: scale(0) rotate(-20deg);
            transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }
        .overlay.active { opacity: 1; pointer-events: auto; }
        .overlay.active .popup-box { transform: scale(1) rotate(0deg); }
        .popup-box h2 { font-size: 2.5rem; color: #fffb00; margin: 0 0 15px 0; }
        .close-btn { background: #ffffff; color: #1d2671; border: none; padding: 10px 25px; font-size: 1rem; border-radius: 25px; cursor: pointer; margin-top: 20px; font-weight: bold; }
        .balloon {
            position: absolute; width: 40px; height: 50px;
            border-radius: 50% 50% 50% 50% / 40% 40% 60% 60%;
            bottom: -70px; opacity: 0.85; animation: floatUp 8s linear infinite;
        }
        .balloon::after { content: "▲"; color: inherit; font-size: 12px; position: absolute; bottom: -7px; left: 14px; }
        @keyframes floatUp {
            0% { transform: translateY(0) translateX(0) rotate(0deg); }
            50% { transform: translateY(-60vh) translateX(20px) rotate(10deg); }
            100% { transform: translateY(-120vh) translateX(-20px) rotate(30deg); }
        }
    </style>
</head>
<body>

    <audio id="bgMusic" loop preload="auto">
        <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mp3">
    </audio>

    <div id="balloon-zone"></div>

    <div class="card">
        <h1>🎉 {{ name }} 🎉</h1>
        <div class="msg">It is only for you</div>
        <button class="btn" onclick="startEverything()">Tap to Open 🎁</button>
    </div>

    <div class="overlay" id="popupOverlay">
        <div class="popup-box">
            <h2>🥳 HAPPY 15th BIRTHDAY! 🎉</h2>
            <p>🎈🎈🎈</p>
            <p>Bhai {{ name }}, tu {{ age }} saal ka ho gaya! Tera din ekdum dhansu aur kadak hona chahiye!</p>
            <p>Enjoy your day buddy! 🥂</p>
            <button class="close-btn" onclick="togglePopup(false)">Thank You! ❤️</button>
        </div>
    </div>

    <script>
        const music = document.getElementById('bgMusic');
        function startEverything() {
            music.volume = 1.0;
            music.currentTime = 0;
            music.play().catch(error => console.log(error));
            togglePopup(true);
        }
        function togglePopup(show) {
            const overlay = document.getElementById('popupOverlay');
            if(show) { overlay.classList.add('active'); } 
            else { overlay.classList.remove('active'); music.pause(); }
        }
        function launchBalloons() {
            const zone = document.getElementById('balloon-zone');
            const colors = ['#ff0055', '#00ffff', '#fffb00', '#ff00ff', '#00ff00', '#ff7b00', '#2ecc71', '#3498db'];
            for (let i = 0; i < 50; i++) {
                const b = document.createElement('div');
                b.className = 'balloon'; b.style.left = Math.random() * 100 + 'vw';
                const randomColor = colors[Math.floor(Math.random() * colors.length)];
                b.style.backgroundColor = randomColor; b.style.color = randomColor;
                b.style.animationDelay = Math.random() * 7 + 's';
                b.style.animationDuration = (Math.random() * 4 + 6) + 's';
                zone.appendChild(b);
            }
        }
        window.onload = launchBalloons;
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, name=naam, age=umar)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    

    
