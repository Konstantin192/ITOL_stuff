function add_task() {
    var task_list = document.querySelector("#task_list");
    var task_input = document.querySelector("#task_input").value;
    var task = document.createElement("li");
    var task_name = document.createTextNode(task_input);

    task.appendChild(task_name);
    task_list.appendChild(task);

    document.querySelector("#task_input").value = "";
}

function remove_task(task) {
    // task.remove();
    // console.log(Array.prototype.indexOf.call(task_list.childNodes, task));

    var tasks = task.parentNode.childNodes;
    var count = 0;

    for(let task_index = 0; task_index < tasks.length; task_index++) {
        if (task === tasks[task_index]) break;
        if (tasks[task_index].toString() !== '[object Text]') count++;
    }

    task.parentNode.removeChild(task);
}

// document.querySelector("#task_submit").onclick = add_task();
// document.querySelector("#task_submit").addEventListener("click", add_task());