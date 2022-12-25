document.addEventListener('DOMContentLoaded', function() {

    document.addEventListener('click', event => {
        element = event.target;

        if (element.id.startsWith('status-')) {
            let employee_id = element.dataset.id

            element.addEventListener('change', () => {
                fetch(`edit_status/${employee_id}`, {
                    method: 'PUT',
                    body: JSON.stringify({
                        status: element.value
                    })
                })
            })
        }
    })
})