// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt

window.get_product_list = function() {
	// $(".more-btn .btn").click(function() {
	// 	window.get_product_list()
	// });

	if(window.start==undefined) {
		throw "product list not initialized (no start)"
	}
	var ds_name = window.location.href.split("?")[1]
	var ds_name = window.location.href.split("?")[1]

	// window.render_product_list('sam')
	href_args=window.getParams()
	url = `/api/method/sbk_crm.custom_methods.verify_otp?user=${href_args.user}&&otp=${href_args.otp}`
	console.log(url)
	$.ajax({
		url: url,
		// url: "/api/method/delivery_management.api.api.get_single_delivery?name=DSCH00078",
		type: 'GET',
		dataType: 'json',
		success: function (data, textStatus, xhr) {
			console.log(data)
			window.render_product_list(data.message || []);
			console.log("successw3!!");
		},
		error: function (data, textStatus, xhr) {
			console.log("Failure!!");
		}
	});

}

window.render_product_list = function(data) {
	console.log(data)
	var table = $("#search-list .table");
	html = data
	if(data=='success'){
		html=`<div class="alert alert-success" role="alert"> This is a success alert—check it</div>`
	}
	else{
		html=`<div class="alert alert-danger" role="alert"> This is a failed alert—check it</div>`

	}
	// $("#delivery_details").append(JSON.stringify(data));
	$("#delivery_details").append(html);


	window.start += (data.length || 0);
}

window.getParams = function (url) {
	var params = {};
	var parser = document.createElement('a');
	parser.href = window.location.href;
	var query = parser.search.substring(1);
	var vars = query.split('&');
	for (var i = 0; i < vars.length; i++) {
		var pair = vars[i].split('=');
		params[pair[0]] = decodeURIComponent(pair[1]);
	}
	return params;
};
