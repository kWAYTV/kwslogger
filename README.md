# 📚 kwslogger: Your Custom Logging Solution! 🚀
Welcome to `kwslogger`, a tailored logging solution for Python developers who desire more color and style in their logs.
![Showcase](https://i.imgur.com/vyeT4DA.gif)

## 🌟 Features
- 🎨 Colorful logs to easily differentiate log types.
- 📅 Timestamped logs to understand when events occur.

## ⚙️ Installation
```bash
pip install kwslogger
```

## 🚀 Quick Start
First import the library:
```python
from kwslogger import Logger
```
then you can use it simply like this
```python
# Create a logger instance
logger = Logger(debug=True) # Default debug: False

# Clear the console
logger.clear()

# Log a message
logger.welcome("I'm a welcome message!")
logger.info("I'm an info message!")
logger.debug("I'm a debug message!")
logger.success("I'm a success message!")
logger.warning("I'm a warning!")
logger.error("I'm an error!")
logger.sleep("I'm a sleep message!")
logger.input("I'm an input message!")
logger.ratelimit("I'm a rate limit message!")

# Wait for 3 seconds using spinners
logger.spinner_wait("Waiting for 3 seconds...", 3)
```

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/kWAYTV/kwslogger/issues).

## 💖 Support
If you like this project, please give it a ⭐️ and share it with your friends!

## 📄 License
This project is [MIT](https://opensource.org/licenses/MIT) licensed, [click here](LICENSE) to see the license file.

---

Thanks for choosing `kwslogger` for your logging needs!
