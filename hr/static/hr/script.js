document.addEventListener('DOMContentLoaded', function() {

    document.addEventListener('click', event => {
        element = event.target;

        // Update orientation status of employee
        if (element.id.startsWith('status-')) {
            let employee_id = element.dataset.id;

            element.addEventListener('change', () => {
                fetch(`edit_status/${employee_id}`, {
                    method: 'PUT',
                    body: JSON.stringify({
                        status: element.value
                    })
                })
            })
        }

        // Toogle done in task status
        if (element.id.startsWith('check-')) {
            ids = element.dataset.id;
            ids = ids.slice(1, -1).replaceAll('"', '').replace(/\s/g, '').split(',');
            employee_id = ids[0];
            template_id = ids[1];
            task_id     = ids[2];

            fetch(`/hr/check_done/${employee_id}/${task_id}`, {
                method: 'PUT'
            })

            document.querySelector(`#form-check-${employee_id}-${template_id}-${task_id}`).style.display = "none";
        }
    })
})