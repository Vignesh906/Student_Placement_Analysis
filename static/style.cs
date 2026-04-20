body {
    margin: 0;
    font-family: Arial;
    background: linear-gradient(135deg, #667eea, #764ba2);
}

.main {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

.card {
    background: white;
    padding: 25px;
    border-radius: 12px;
    width: 600px;
    text-align: center;
}

.grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
}

input, select {
    padding: 10px;
    border-radius: 6px;
    border: 1px solid #ccc;
}

button {
    margin-top: 15px;
    padding: 12px;
    width: 100%;
    border: none;
    background: #667eea;
    color: white;
    border-radius: 8px;
}

.progress-bar {
    background: #ddd;
    border-radius: 10px;
    margin-top: 10px;
}

.progress {
    height: 25px;
    width: 0%;
    color: white;
    text-align: center;
    line-height: 25px;
}