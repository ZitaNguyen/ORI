document.addEventListener('DOMContentLoaded', function() {

    let select = document.querySelector('#status');

    select.addEventListener('click', () => {
        // let firstOption = select.firstElementChild;
        // console.log(firstOption);
        // firstOption.getAttribute("hidden");
        // select.remove(0);
        // console.log(select);
        // console.log(select.options[3].value);
        // select.size = "3";
        // let statuses = ["upcoming", "current", "done"];
        // let current_status = select.options[0].value;

        // for (const status of statuses)
        // {
        //     if (current_status != status) {
        //         var option = document.createElement("option");
        //         option.value = status;
        //         option.text = status.charAt(0).toUpperCase() + status.slice(1);
        //         select.appendChild(option);
        //     }
        // }
        // console.log(select);
        // select.options[0].style.display = "none";
    })

    // document.querySelector('#status').addEventListener('click', event => {
    //     let current_status = event.target;
    //     let statuses = ["upcoming", "current", "done"];

    //     let select = document.createElement("select");
    //     select.className = "form-select";
    //     select.size = "3";

    //     for (const status of statuses)
    //     {
    //         var option = document.createElement("option");
    //         option.value = status;
    //         option.text = status.charAt(0).toUpperCase() + status.slice(1);
    //         select.appendChild(option);
    //     }

    //     current_status.innerHTML = '';
    //     current_status.appendChild(select);
    //     console.log(current_status);
    // })
})