# 0x04. AirBnB clone - Web framework

## Tasks

### 0. Hello Flask!
Write a script that starts a Flask web application:
- Your web application must be listening on `0.0.0.0`, port `5000`
- Routes:
  - `/`: display “Hello HBNB!”
- You must use the option `strict_slashes=False` in your route definition

### 1. HBNB
Write a script that starts a Flask web application:
- Your web application must be listening on `0.0.0.0`, port `5000`
- Routes:
  - `/`: display “Hello HBNB!”
  - `/hbnb` : display “HBNB”
- You must use the option `strict_slashes=False` in your route definition

### 2. C is fun!
Write a script that starts a Flask web application:
- Your web application must be listening on `0.0.0.0`, port `5000`
- Routes:
  - `/`: display “Hello HBNB!”
  - `/hbnb` : display “HBNB”
  - `/c/<text>`: display “C ” followed by the value of the `text` variable (replace underscore `_` symbols with a space )
- You must use the option `strict_slashes=False` in your route definition

### 3. Python is cool!
Write a script that starts a Flask web application:
- Your web application must be listening on `0.0.0.0`, port `5000`
- Routes:
  - `/`: display “Hello HBNB!”
  - `/hbnb` : display “HBNB”
  - `/c/<text>`: display “C ” followed by the value of the `text` variable (replace underscore `_` symbols with a space )
  - `/python/(<text>)`: display “Python ”, followed by the value of the `text` variable (replace underscore `_` symbols with a space )
    - The default value of `text` is “is cool”
- You must use the option `strict_slashes=False` in your route definition

### 4. Is it a number?
Write a script that starts a Flask web application:
- Your web application must be listening on `0.0.0.0`, port `5000`
- Routes:
  - `/`: display “Hello HBNB!”
  - `/hbnb` : display “HBNB”
  - `/c/<text>`: display “C ” followed by the value of the `text` variable (replace underscore `_` symbols with a space )
  - `/python/(<text>)`: display “Python ”, followed by the value of the `text` variable (replace underscore `_` symbols with a space )
    - The default value of `text` is “is cool”
  - `/number/<n>`: display “`n` is a number” only if `n` is an integer
- You must use the option `strict_slashes=False` in your route definition

### 5. Number template
Write a script that starts a Flask web application:
- Your web application must be listening on `0.0.0.0`, port `5000`
- Routes:
  - `/`: display “Hello HBNB!”
  - `/hbnb` : display “HBNB”
  - `/c/<text>`: display “C ” followed by the value of the `text` variable (replace underscore `_` symbols with a space )
  - `/python/(<text>)`: display “Python ”, followed by the value of the `text` variable (replace underscore `_` symbols with a space )
    - The default value of `text` is “is cool”
  - `/number/<n>`: display “`n` is a number” only if `n` is an integer
    - `h1` tag: “Number: `n`” inside the tag `body`
- You must use the option `strict_slashes=False` in your route definition