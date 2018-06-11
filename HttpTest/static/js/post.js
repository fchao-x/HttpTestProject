//Content-type选择后，生成的设置页面
function content_type(x){

	$("#body_config").remove();

	var html_app_x_www_form_urlencoded = '<div id="body_config"><button type="button" onclick="add_random_parameter();">添加随机参数</button> <button type="button" onclick="add_specified_parameter();">添加指定参数</button></div>';
	
	if(x == "application/x-www-form-urlencoded"){
		$("#content_type").after(html_app_x_www_form_urlencoded);
	};
	
};

var n=0;
//添加随机参数
function add_random_parameter(){

	n++;
	var html_random_parameter = '<div id="para_' + n + '" func="add_random_parameter">Name长度: <input type="number" id="para_name_' + n + '" name="para_name_' + n + '" />Value长度: <input type="number" id="para_value_' + n + '" name="para_value_' + n + '" />参数个数: <input type="number" id="para_no_' + n + '" name="para_no_' + n + '" /><button type="button" onclick="delete_this_line(' + n + ');">删除</button></div>';
	$("#body_config").append(html_random_parameter);	

};

//添加指定参数
function add_specified_parameter(){

	n++;
	var html_specified_parameter = '<div id="para_' + n + '" func="add_specified_parameter">Name值: <input type="text" id="para_name_' + n + '" name="para_name_' + n + '" />Value值: <input type="text" id="para_value_' + n + '" name="para_value_' + n + '" /><button type="button" onclick="delete_this_line(' + n + ');">删除</button></div>';
	$("#body_config").append(html_specified_parameter);
	
}

//删除当前行
function delete_this_line(x){

	$("#para_" + x).remove()

};

//生成参数
function get_paras(){

	var paras = '';
	var div_len = $("#body_config").contents("div").length;

	//div为0, 没有添加任何参数
	if(div_len==0){
		paras = '';
	} else {	
		for(var i=0; i<div_len; i++){
			var n = $("#body_config").contents("div").eq(i).attr("id").substr(5)
			if(i==0){
				paras += get_para_sub(n);
			} else {
				paras += '&' + get_para_sub(n);
			};			
		};
	};

	var html_request_content = '<div id="request_content_para"><p>' + paras + '</p></div>';
	$('#request_content_para').remove();
	$("#request_content").after(html_request_content);

};

//生成参数
function get_para_sub(x){

	var para = '';
	var func = $("#para_" + x).attr("func");
	var para_name = $("#para_name_" + x).val();
	var para_value = $("#para_value_" + x).val();

	if(func == "add_random_parameter"){
		var para_no = Number($("#para_no_" + x).val());
		for(var i=0; i<para_no; i++){
			if(i==0){
				para += get_random_string(para_name) + '=';
				para += get_random_string(para_value);
			} else {
				para += '&' + get_random_string(para_name) + '=';
				para += get_random_string(para_value);
			};		
		};
	} else {
		para += para_name + '=';
		para += para_value;
	};
	
	return para;
};

//生成随机字符串
function get_random_string(len){

	var random_string = ''
	var chars='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
	var max_pos = chars.length;

	for(var i=0; i<len; i++){
		random_string += chars.charAt(Math.floor(Math.random() * max_pos));
	};
	
	return random_string;

};

