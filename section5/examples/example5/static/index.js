document.addEventListener('DOMContentLoaded', () => {

    document.querySelector('#form').onsubmit = () => {
        event.preventDefault();

        fetch("/list")
        //  ->  header+cookies+json  ....  
        .then(response => response.json())
        // json ({"items":["cs50","web50","mobile50","game50","test50"],"success":true}) ->
        .then(data => {
        // data = '{"items":["cs50","web50","mobile50","game50","test50"],
        //          "success":true}'


          // fetch select
          let opts = document.querySelector('#opts')

          // clear out any options for size just in case
          opts.innerHTML = null


          // Update the result div
          if (data.success) {
              //const contents = data.items;

              console.log(data) // TODO: remove this

              // better to use
              // emails.forEach(element => {
                
              //   });
              for (let i = 0, len = data.items.length; i < len; i++) {

                  // create element option
                  const option = document.createElement("option");

                  // add option into options text
                  option.text = data.items[i];

                  // add option to select object
                  opts.add(option, opts[i]);
              }

              // unselect option in dropdown
              opts.selectedIndex = -1;

          } else {
              document.querySelector('#result').innerHTML = 'There was an error.';
          }

          // THIS RUNS WHEN FETCH IS DONE COMPLETELY
          document.querySelector('#result').innerHTML = 'INSIDE IN THEN (RUNS AFTER THEN PROCESSED)';


        })  // FETCH/THEN ENDS HERE


        // THIS RUNS WHILE FETCH IS WAITING FOR SERVER RESPONSE
        document.querySelector('#result').innerHTML = 'OUT OF THEN (RUNS USUALLY BEFORE FETCH PROCESSED)';
    
    
    };

});


//<select class="form-control" id="opts" name="size" disabled>





// id =  100


// fetch(`/emails/${id}`, {
//   method: 'PUT',
//   body: JSON.stringify({
//       archived: true
//   })
// })
