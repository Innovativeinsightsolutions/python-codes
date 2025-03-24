<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portfolio</title>
    <style>
        /* Basic styling */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #333;
            color: white;
            padding: 1rem;
            text-align: center;
        }
        nav {
            display: flex;
            justify-content: center;
            background-color: #444;
        }
        nav a {
            color: white;
            text-decoration: none;
            padding: 1rem;
        }
        nav a:hover {
            background-color: #555;
        }
        section {
            padding: 2rem;
            text-align: center;
        }
        footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 1rem;
            position: fixed;
            bottom: 0;
            width: 100%;
        }
    </style>
</head>
<body>
    <header>
        <h1>My Portfolio</h1>
    </header>
    <nav>
        <a href="#about">About Me</a>
        <a href="#projects">Projects</a>
        <a href="#contact">Contact</a>
    </nav>
    <section id="about">
        <h2>About Me</h2>
        <p>Welcome to my portfolio! I am a [Your Profession] with a passion for [Your Interests].</p>
    </section>
    <section id="projects">
        <h2>Projects</h2>
        <p>Here are some of my recent projects:</p>
        <ul>
            <li>Project 1 - Description</li>
            <li>Project 2 - Description</li>
            <li>Project 3 - Description</li>
        </ul>
    </section>
    <section id="contact">
        <h2>Contact</h2>
        <p>Email: your.email@example.com</p>
        <p>Phone: +123456789</p>
    </section>
    <footer>
        <p>&copy; 2023 Your Name. All rights reserved.</p>
    </footer>
</body>
</html>
