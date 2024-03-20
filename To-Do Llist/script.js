function addTask() {
    var taskInput = document.getElementById("taskInput");
    var taskText = taskInput.value.trim();
    if (taskText !== "") {
        var taskList = document.getElementById("taskList");
        var li = document.createElement("li");
        var editInput = document.createElement("input");
        editInput.type = "text";
        editInput.className = "edit-input";
        editInput.value = taskText;
        li.appendChild(editInput);
        var editBtn = document.createElement("button");
        editBtn.innerHTML = "Edit";
        editBtn.className = "edit-btn";
        editBtn.onclick = function() {
            editTask(this);
        };
        li.appendChild(editBtn);
        var deleteBtn = document.createElement("button");
        deleteBtn.innerHTML = "Delete";
        deleteBtn.className = "delete-btn";
        deleteBtn.onclick = function() {
            deleteTask(this);
        };
        li.appendChild(deleteBtn);
        taskList.appendChild(li);
        taskInput.value = "";
    } else {
        alert("Please enter a task!");
    }
}

function deleteTask(btn) {
    btn.parentNode.remove();
}

function editTask(btn) {
    var li = btn.parentNode;
    var editInput = li.querySelector(".edit-input");
    var taskText = editInput.value.trim();
    if (taskText !== "") {
        li.childNodes[0].nodeValue = taskText;
    } else {
        alert("Please enter a task!");
    }
}
