# Danh sách lưu các công việc dưới dạng dictionary
tasks = []

def add_task(task_name):
    """Thêm một công việc mới vào danh sách."""
    task = {'name': task_name, 'completed': False}
    tasks.append(task)
    print(f"Đã thêm công việc: '{task_name}'")

def list_tasks():
    """Liệt kê công việc kèm trạng thái hoàn thành [x] hoặc [ ]."""
    print("\n--- DANH SÁCH CÔNG VIỆC ---")
    if not tasks:
        print("Danh sách trống!")
    else:
        for index, task in enumerate(tasks, start=1):
            status = "x" if task['completed'] else " "
            print(f"{index}. [{status}] {task['name']}")
    print("---------------------------\n")

def complete_task(task_index):
    """Đánh dấu công việc hoàn thành dựa vào chỉ số."""
    actual_index = task_index - 1
    if 0 <= actual_index < len(tasks):
        tasks[actual_index]['completed'] = True
        print(f"Đã đánh dấu hoàn thành công việc số {task_index}!")
    else:
        print("Lỗi: Chỉ số công việc không hợp lệ!")

def delete_task(task_index):
    """Xóa một công việc khỏi danh sách dựa trên chỉ số."""
    actual_index = task_index - 1
    if 0 <= actual_index < len(tasks):
        removed_task = tasks.pop(actual_index)
        print(f"Đã xóa công việc: '{removed_task['name']}'")
    else:
        print("Lỗi: Chỉ số công việc cần xóa không hợp lệ!")

# --- Điểm bắt đầu của chương trình
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")
    add_task("Nộp bài tập cho giảng viên")
    
    # Thao tác thử các tính năng
    complete_task(1)
    delete_task(3)
    
    # Hiển thị danh sách cuối cùng
    list_tasks()