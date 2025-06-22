import datetime

def log_task(task):
    with open("log.txt", "a") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp}: {task}\n")

if __name__ == "__main__":
    print("📝 Enter your tasks (type 'exit' to finish):")
    session_tasks = []
    while True:
        task = input("> ")
        if task.lower() == "exit":
            break
        log_task(task)
        session_tasks.append(task)
    
    print("\n✅ Tasks Logged:")
    for i, t in enumerate(session_tasks, 1):
        print(f"{i}. {t}")
