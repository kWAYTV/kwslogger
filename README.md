# 📚 kwslogger: Your Custom Logging Solution! 🚀
Welcome to `kwslogger`, a tailored logging solution for Python developers who desire more color and style in their logs.

## 🌟 Features
- 🎨 Colorful logs to easily differentiate log types.
- 📅 Timestamped logs to understand when events occur.

## ⚙️ Installation
```bash
pip install kwslogger
```

## 🚀 Quick Start
```python
import kwslogger

# Create a logger instance
logger = kwslogger.Logger()
```
or
```python
from kwslogger import Logger as logger
```
then you can use it simply like this
```python
# Clear the console
logger.clear()

# Log a message
logger.info("I'm an info message!")
logger.success("I'm a success message!")
logger.warning("I'm a warning!")
logger.error("I'm an error!")
```

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/kWAYTV/kwslogger/issues).

## 💖 Support
If you like this project, please give it a ⭐️ and share it with your friends!

## 📄 License
This project is [MIT](https://opensource.org/licenses/MIT) licensed, [click here](LICENSE) to see the license file.

---

Thanks for choosing `kwslogger` for your logging needs!