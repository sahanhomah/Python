import os
import sqlite3
import tkinter as tk
from dataclasses import dataclass
from datetime import datetime
from tkinter import messagebox, ttk


@dataclass
class Task:
	task_id: int | None
	title: str
	description: str
	due_date: str
	priority: str
	status: str


class TaskRepository:
	def __init__(self, db_path: str) -> None:
		self.db_path = db_path
		self._initialize_db()

	def _connect(self) -> sqlite3.Connection:
		return sqlite3.connect(self.db_path)

	def _initialize_db(self) -> None:
		query = """
		CREATE TABLE IF NOT EXISTS tasks (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			title TEXT NOT NULL,
			description TEXT NOT NULL,
			due_date TEXT NOT NULL,
			priority TEXT NOT NULL,
			status TEXT NOT NULL
		)
		"""
		with self._connect() as conn:
			conn.execute(query)
			conn.commit()

	def add_task(self, task: Task) -> None:
		query = """
		INSERT INTO tasks (title, description, due_date, priority, status)
		VALUES (?, ?, ?, ?, ?)
		"""
		with self._connect() as conn:
			conn.execute(
				query,
				(task.title, task.description, task.due_date, task.priority, task.status),
			)
			conn.commit()

	def update_task(self, task: Task) -> None:
		query = """
		UPDATE tasks
		SET title = ?, description = ?, due_date = ?, priority = ?, status = ?
		WHERE id = ?
		"""
		with self._connect() as conn:
			conn.execute(
				query,
				(
					task.title,
					task.description,
					task.due_date,
					task.priority,
					task.status,
					task.task_id,
				),
			)
			conn.commit()

	def delete_task(self, task_id: int) -> None:
		with self._connect() as conn:
			conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
			conn.commit()

	def mark_completed(self, task_id: int) -> None:
		with self._connect() as conn:
			conn.execute("UPDATE tasks SET status = 'Completed' WHERE id = ?", (task_id,))
			conn.commit()

	def get_all_tasks(
		self,
		search_text: str = "",
		priority_filter: str = "All",
		status_filter: str = "All",
		sort_due_date: bool = False,
	) -> list[Task]:
		query = (
			"SELECT id, title, description, due_date, priority, status FROM tasks WHERE 1=1"
		)
		params: list[str] = []

		if search_text.strip():
			query += " AND title LIKE ?"
			params.append(f"%{search_text.strip()}%")

		if priority_filter != "All":
			query += " AND priority = ?"
			params.append(priority_filter)

		if status_filter != "All":
			query += " AND status = ?"
			params.append(status_filter)

		if sort_due_date:
			query += " ORDER BY due_date ASC"
		else:
			query += " ORDER BY id DESC"

		with self._connect() as conn:
			rows = conn.execute(query, tuple(params)).fetchall()

		return [
			Task(
				task_id=row[0],
				title=row[1],
				description=row[2],
				due_date=row[3],
				priority=row[4],
				status=row[5],
			)
			for row in rows
		]


class TaskController:
	PRIORITIES = {"Low", "Medium", "High"}
	STATUSES = {"Pending", "Completed"}

	def __init__(self, repository: TaskRepository) -> None:
		self.repository = repository

	def _validate_task(self, task: Task) -> None:
		if not task.title.strip():
			raise ValueError("Title is required.")

		if not task.description.strip():
			raise ValueError("Description is required.")

		try:
			datetime.strptime(task.due_date, "%Y-%m-%d")
		except ValueError as exc:
			raise ValueError("Due date must be in YYYY-MM-DD format.") from exc

		if task.priority not in self.PRIORITIES:
			raise ValueError("Priority must be Low, Medium, or High.")

		if task.status not in self.STATUSES:
			raise ValueError("Status must be Pending or Completed.")

	def create_task(self, title: str, description: str, due_date: str, priority: str, status: str) -> None:
		task = Task(
			task_id=None,
			title=title.strip(),
			description=description.strip(),
			due_date=due_date.strip(),
			priority=priority,
			status=status,
		)
		self._validate_task(task)
		self.repository.add_task(task)

	def edit_task(
		self,
		task_id: int,
		title: str,
		description: str,
		due_date: str,
		priority: str,
		status: str,
	) -> None:
		task = Task(
			task_id=task_id,
			title=title.strip(),
			description=description.strip(),
			due_date=due_date.strip(),
			priority=priority,
			status=status,
		)
		self._validate_task(task)
		self.repository.update_task(task)

	def remove_task(self, task_id: int) -> None:
		self.repository.delete_task(task_id)

	def complete_task(self, task_id: int) -> None:
		self.repository.mark_completed(task_id)

	def list_tasks(
		self,
		search_text: str = "",
		priority_filter: str = "All",
		status_filter: str = "All",
		sort_due_date: bool = False,
	) -> list[Task]:
		return self.repository.get_all_tasks(
			search_text=search_text,
			priority_filter=priority_filter,
			status_filter=status_filter,
			sort_due_date=sort_due_date,
		)


class TaskManagerApp:
	def __init__(self, root: tk.Tk, controller: TaskController) -> None:
		self.root = root
		self.controller = controller
		self.selected_task_id: int | None = None

		self.root.title("Task Manager")
		self.root.geometry("980x600")
		self.root.minsize(900, 540)

		self._build_ui()
		self.refresh_table()

	def _build_ui(self) -> None:
		container = ttk.Frame(self.root, padding=12)
		container.pack(fill="both", expand=True)

		form_frame = ttk.LabelFrame(container, text="Task Details", padding=10)
		form_frame.pack(fill="x")

		ttk.Label(form_frame, text="Title").grid(row=0, column=0, sticky="w", padx=5, pady=5)
		self.title_var = tk.StringVar()
		ttk.Entry(form_frame, textvariable=self.title_var, width=40).grid(
			row=0, column=1, sticky="ew", padx=5, pady=5
		)

		ttk.Label(form_frame, text="Due Date (YYYY-MM-DD)").grid(
			row=0, column=2, sticky="w", padx=5, pady=5
		)
		self.due_date_var = tk.StringVar()
		ttk.Entry(form_frame, textvariable=self.due_date_var, width=20).grid(
			row=0, column=3, sticky="ew", padx=5, pady=5
		)

		ttk.Label(form_frame, text="Description").grid(row=1, column=0, sticky="nw", padx=5, pady=5)
		self.description_text = tk.Text(form_frame, height=4, width=50)
		self.description_text.grid(row=1, column=1, columnspan=3, sticky="ew", padx=5, pady=5)

		ttk.Label(form_frame, text="Priority").grid(row=2, column=0, sticky="w", padx=5, pady=5)
		self.priority_var = tk.StringVar(value="Medium")
		self.priority_box = ttk.Combobox(
			form_frame,
			textvariable=self.priority_var,
			values=["Low", "Medium", "High"],
			state="readonly",
			width=18,
		)
		self.priority_box.grid(row=2, column=1, sticky="w", padx=5, pady=5)

		ttk.Label(form_frame, text="Status").grid(row=2, column=2, sticky="w", padx=5, pady=5)
		self.status_var = tk.StringVar(value="Pending")
		self.status_box = ttk.Combobox(
			form_frame,
			textvariable=self.status_var,
			values=["Pending", "Completed"],
			state="readonly",
			width=18,
		)
		self.status_box.grid(row=2, column=3, sticky="w", padx=5, pady=5)

		form_frame.columnconfigure(1, weight=1)
		form_frame.columnconfigure(3, weight=1)

		action_frame = ttk.Frame(container, padding=(0, 10, 0, 10))
		action_frame.pack(fill="x")

		ttk.Button(action_frame, text="Add", command=self.add_task).pack(side="left", padx=4)
		ttk.Button(action_frame, text="Edit", command=self.edit_task).pack(side="left", padx=4)
		ttk.Button(action_frame, text="Delete", command=self.delete_task).pack(side="left", padx=4)
		ttk.Button(action_frame, text="Complete", command=self.complete_task).pack(
			side="left", padx=4
		)
		ttk.Button(action_frame, text="Clear", command=self.clear_form).pack(side="left", padx=4)

		filter_frame = ttk.LabelFrame(container, text="Search / Filter", padding=10)
		filter_frame.pack(fill="x")

		ttk.Label(filter_frame, text="Search Title").pack(side="left", padx=4)
		self.search_var = tk.StringVar()
		search_entry = ttk.Entry(filter_frame, textvariable=self.search_var, width=24)
		search_entry.pack(side="left", padx=4)
		search_entry.bind("<KeyRelease>", lambda _event: self.refresh_table())

		ttk.Label(filter_frame, text="Priority").pack(side="left", padx=4)
		self.priority_filter_var = tk.StringVar(value="All")
		priority_filter = ttk.Combobox(
			filter_frame,
			textvariable=self.priority_filter_var,
			values=["All", "Low", "Medium", "High"],
			state="readonly",
			width=10,
		)
		priority_filter.pack(side="left", padx=4)
		priority_filter.bind("<<ComboboxSelected>>", lambda _event: self.refresh_table())

		ttk.Label(filter_frame, text="Status").pack(side="left", padx=4)
		self.status_filter_var = tk.StringVar(value="All")
		status_filter = ttk.Combobox(
			filter_frame,
			textvariable=self.status_filter_var,
			values=["All", "Pending", "Completed"],
			state="readonly",
			width=10,
		)
		status_filter.pack(side="left", padx=4)
		status_filter.bind("<<ComboboxSelected>>", lambda _event: self.refresh_table())

		self.sort_due_var = tk.BooleanVar(value=False)
		ttk.Checkbutton(
			filter_frame,
			text="Sort by due date",
			variable=self.sort_due_var,
			command=self.refresh_table,
		).pack(side="left", padx=8)

		self.tree = ttk.Treeview(
			container,
			columns=("id", "title", "description", "due_date", "priority", "status"),
			show="headings",
		)
		self.tree.pack(fill="both", expand=True)

		self.tree.heading("id", text="ID")
		self.tree.heading("title", text="Title")
		self.tree.heading("description", text="Description")
		self.tree.heading("due_date", text="Due Date")
		self.tree.heading("priority", text="Priority")
		self.tree.heading("status", text="Status")

		self.tree.column("id", width=60, anchor="center")
		self.tree.column("title", width=180)
		self.tree.column("description", width=320)
		self.tree.column("due_date", width=120, anchor="center")
		self.tree.column("priority", width=100, anchor="center")
		self.tree.column("status", width=110, anchor="center")

		self.tree.bind("<<TreeviewSelect>>", self.on_select_task)

	def _read_form(self) -> tuple[str, str, str, str, str]:
		title = self.title_var.get()
		description = self.description_text.get("1.0", "end").strip()
		due_date = self.due_date_var.get()
		priority = self.priority_var.get()
		status = self.status_var.get()
		return title, description, due_date, priority, status

	def add_task(self) -> None:
		try:
			title, description, due_date, priority, status = self._read_form()
			self.controller.create_task(title, description, due_date, priority, status)
			self.refresh_table()
			self.clear_form()
			messagebox.showinfo("Success", "Task added successfully.")
		except ValueError as exc:
			messagebox.showwarning("Validation Error", str(exc))
		except sqlite3.Error as exc:
			messagebox.showerror("Database Error", f"Could not add task.\n{exc}")
		except Exception as exc:
			messagebox.showerror("Error", f"Unexpected error while adding task.\n{exc}")

	def edit_task(self) -> None:
		if self.selected_task_id is None:
			messagebox.showwarning("No Selection", "Select a task to edit.")
			return

		try:
			title, description, due_date, priority, status = self._read_form()
			self.controller.edit_task(
				self.selected_task_id,
				title,
				description,
				due_date,
				priority,
				status,
			)
			self.refresh_table()
			messagebox.showinfo("Success", "Task updated successfully.")
		except ValueError as exc:
			messagebox.showwarning("Validation Error", str(exc))
		except sqlite3.Error as exc:
			messagebox.showerror("Database Error", f"Could not update task.\n{exc}")
		except Exception as exc:
			messagebox.showerror("Error", f"Unexpected error while updating task.\n{exc}")

	def delete_task(self) -> None:
		if self.selected_task_id is None:
			messagebox.showwarning("No Selection", "Select a task to delete.")
			return

		confirmed = messagebox.askyesno("Confirm Delete", "Delete selected task?")
		if not confirmed:
			return

		try:
			self.controller.remove_task(self.selected_task_id)
			self.refresh_table()
			self.clear_form()
			messagebox.showinfo("Success", "Task deleted successfully.")
		except sqlite3.Error as exc:
			messagebox.showerror("Database Error", f"Could not delete task.\n{exc}")
		except Exception as exc:
			messagebox.showerror("Error", f"Unexpected error while deleting task.\n{exc}")

	def complete_task(self) -> None:
		if self.selected_task_id is None:
			messagebox.showwarning("No Selection", "Select a task to mark as completed.")
			return

		try:
			self.controller.complete_task(self.selected_task_id)
			self.refresh_table()
			self.status_var.set("Completed")
			messagebox.showinfo("Success", "Task marked as completed.")
		except sqlite3.Error as exc:
			messagebox.showerror("Database Error", f"Could not complete task.\n{exc}")
		except Exception as exc:
			messagebox.showerror("Error", f"Unexpected error while completing task.\n{exc}")

	def clear_form(self) -> None:
		self.selected_task_id = None
		self.title_var.set("")
		self.description_text.delete("1.0", "end")
		self.due_date_var.set("")
		self.priority_var.set("Medium")
		self.status_var.set("Pending")
		self.tree.selection_remove(self.tree.selection())

	def on_select_task(self, _event: tk.Event) -> None:
		selected = self.tree.selection()
		if not selected:
			return

		values = self.tree.item(selected[0], "values")
		self.selected_task_id = int(values[0])
		self.title_var.set(values[1])
		self.description_text.delete("1.0", "end")
		self.description_text.insert("1.0", values[2])
		self.due_date_var.set(values[3])
		self.priority_var.set(values[4])
		self.status_var.set(values[5])

	def refresh_table(self) -> None:
		for row in self.tree.get_children():
			self.tree.delete(row)

		tasks = self.controller.list_tasks(
			search_text=self.search_var.get(),
			priority_filter=self.priority_filter_var.get(),
			status_filter=self.status_filter_var.get(),
			sort_due_date=self.sort_due_var.get(),
		)

		for task in tasks:
			self.tree.insert(
				"",
				"end",
				values=(
					task.task_id,
					task.title,
					task.description,
					task.due_date,
					task.priority,
					task.status,
				),
			)


def main() -> None:
	base_dir = os.path.dirname(os.path.abspath(__file__))
	db_path = os.path.join(base_dir, "tasks.db")

	repository = TaskRepository(db_path)
	controller = TaskController(repository)

	root = tk.Tk()
	TaskManagerApp(root, controller)
	root.mainloop()


if __name__ == "__main__":
	main()
