$(document).on('click', "#submit", function () {

    var queue = $('#queue').val();
    if (queue.length == 0) {
        alert('Queue is required');
        return;
    }
    var url_callback = $('#callback').val();
    if (url_callback.length == 0) {
        alert('Callback is required');
        return;
    }
    var topic = $('#topic').val();
    if (topic.length == 0) {
        alert('Topic is required');
        return;
    }

    const consumer = {
    topic: topic,
    url_callback: url_callback
    };
    
    // Create a JSON object with the consumer information
    const json = {
    consumer: consumer,
    queue: queue
    };
    
    // Print the JSON object to the console
    console.log(json);

    let json_string = JSON.stringify(json);
    console.log(json_string);
    $.ajax({
        method: 'POST',
        data: json_string,
        contentType: 'application/json',
        success: function (data) {
            console.log(data);
            console.log("Success Consumer");
            window.location = `/`
        },
        Error: function(data){
            console.log("error");
        },
        fail: function(data){
            console.log("fail");
        },
    });

})
