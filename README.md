# 🐳 Dockerized Python Task Tracker

A minimal command-line task logging app built with Python — perfect for learning how to containerize a script and manage logging using Docker.

This project lets you enter tasks interactively, logs them with timestamps, and stores them in a log file (`log.txt`). It runs inside a Docker container, making it portable and isolated.

---

## 📦 Features

- ✅ Interactive CLI: Enter multiple tasks in a single session
- ✅ Auto-logging: Each task is timestamped and saved
- ✅ Dockerized: Runs in a consistent container environment
- ✅ .gitignore: Prevents committing `log.txt`, cache, and Python artifacts

---

## 🧱 Project Structure

```
.
├── app/
│   └── main.py            # Main Python script
├── Dockerfile             # Build instructions
├── .gitignore             # Files to exclude from Git
└── README.md              # This file
```

---

## 🚀 Quick Start

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Rahuljoshi07/docker-task-tracker.git
cd docker-task-tracker
```

### 2️⃣ Build the Docker image

```bash
docker build -t task-tracker .
```

### 3️⃣ Run the container

```bash
docker run -it task-tracker
```

### 📝 Usage Example

```text
📝 Enter your tasks (type 'exit' to finish):
> Fix Dockerfile bug
> Write README
> exit

✅ Tasks Logged:
1. Fix Dockerfile bug
2. Write README
```

---

## 🔧 Future Improvements

- 💾 Mount volumes to persist `log.txt` outside the container
- 🌐 Add a web-based interface for task input
- 📤 Push logs to a cloud storage service or database
- 🔍 Add search/filter functionality on tasks

---

## 📄 License

This project is created for learning purposes by **Rahul Joshi**.  
Feel free to explore and use the code.

---

👨‍💻 Made with ❤️ by [Rahul Joshi](https://github.com/Rahuljoshi07)
