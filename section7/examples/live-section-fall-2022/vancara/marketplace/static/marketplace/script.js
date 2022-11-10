document.addEventListener('DOMContentLoaded', function() {
    // alert('hello');




    document.querySelectorAll('.edit').forEach(btn => {

        btn.addEventListener('click', function() {
            // alert(btn.dataset.vehicle);

            const vehicleId = btn.dataset.vehicle;

            const descr = document.querySelector(`.descr[data-vehicle="${vehicleId}"]`);


            const area = document.querySelector(`.area[data-vehicle="${vehicleId}"]`);

            area.innerHTML = descr.innerHTML;


        })

    })



})


fetch().then( data => {
    
    ... innerHTML  = data.content

)