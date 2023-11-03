# 📚 kwslogger: Your Custom Logging Solution! 🚀
Welcome to `kwslogger`, a tailored logging solution for Python developers who desire more color and style in their logs.

## 🌟 Features
- 🎨 Colorful logs to easily differentiate log types.
- 📅 Timestamped logs to understand when events occur.

## ⚙️ Installation
```bash
pip install kwslogger
```

## 🚀 Usage

Normal logs for your tools
```python
from kwslogger import Logger

# Create a logger instance
logger = Logger(debug=True) # Default debug: False, if this is False, the debug prints won't print.

# Clear the console
logger.clear()

# Log a message
logger.welcome("I'm a welcome message!")
logger.info("I'm an info message!")
logger.debug("I'm a debug message!")
logger.success("I'm a success message!")
logger.warning("I'm a warning!")
logger.error("I'm an error!")
logger.input("I'm an input message!")
logger.ratelimit("I'm a rate limit message!")
```

Animated Sleeps
```python
from kwslogger import Logger

# Create a logger instance
logger = Logger(debug=True)

logger.sleep("Waiting for 1 second...", 1)
```

Run functions while you showing the spinner
```python
from kwslogger import Logger

# Create a logger instance
logger = Logger(debug=True)

def test_func(number1, number2):
    answer = number1 + number2
    return answer

result = logger.run_with_spinner(test_func, "Calculating...", 1, 1)
print(str(result) + " (Func returned)")
```

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/kWAYTV/kwslogger/issues).

## 💖 Support
If you like this project, please give it a ⭐️ and share it with your friends!

## 📄 License
This project is [MIT](https://opensource.org/licenses/MIT) licensed, [click here](LICENSE) to see the license file.

---

Thanks for choosing `kwslogger` for your logging needs!