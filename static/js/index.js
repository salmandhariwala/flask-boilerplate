// execution start here : main function
var main_func = function() {

	// step 1
	console.log("dom loaded");

	// step 2
	$("#hello_world").html('hello world via jquery');

	// step 3 :sample post
	$.ajax({
		type:"POST",
		url:"/test/post", 
		headers:{ "Content-Type": "application/json" },
		data:JSON.stringify({"foo":"bar"}),
		success:function(data){
			console.log("success of post ");
			console.log(data);
		},
		error:function(data){
			console.log("fail * post request");
			console.log(data);
		},
		dataType: "json"
	});

	// step 4 : sample get
	$.ajax({
		type:"GET",
		url:"/test/get", 
		headers:{ "sampleheader1": "samplevalue1" },
		success:function(data){
			console.log("success of get ");
			console.log(data);
		},
		error:function(data){
			console.log("fail * get request");
			console.log(data);
		},
		dataType: "json"
	});

}


$(main_func);