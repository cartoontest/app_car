<!DOCTYPE html>
<html>
<head>
    <title>CarSleep - Add Parking Market</title>
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <header>
        <h1>CarSleep</h1>
        <nav>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">About Us</a></li>
                <li><a href="#">Contact</a></li>
                <li><a href="/logout">Log out</a></li>
            </ul>
        </nav>
    </header>
php
Copy code
<main>
    <section class="add-parking-market">
        <h2>Add Parking Market</h2>
        <form action="{{ url_for('add_parking_market') }}" method="POST">
            <div class="form-group">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="address">Address:</label>
                <input type="text" id="address" name="address" required>
            </div>
            <div class="form-group">
                <label for="description">Description:</label>
                <textarea id="description" name="description" rows="5" required></textarea>
            </div>
            <div class="form-group">
                <label for="image">Image:</label>
                <input type="file" id="image" name="image">
            </div>
            <div class="form-group">
                <label for="lat">Latitude:</label>
                <input type="text" id="lat" name="lat" required>
            </div>
            <div class="form-group">
                <label for="lng">Longitude:</label>
                <input type="text" id="lng" name="lng" required>
            </div>
            <button type="submit" class="btn">Add Parking Market</button>
        </form>
    </section>
</main>
</body>
</html>