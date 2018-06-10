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
	var html_random_parameter = '<div id="para_' + n + '" func="add_random_parameter">参数个数: <input type="number" name="para_no_' + n + '" />Name长度: <input type="number" name="para_name_' + n + '" />Value长度: <input type="number" name="para_value_' + n + '" /><button type="button" onclick="delete_this_line(' + n + ');">删除</button></div>';
	$("#body_config").append(html_random_parameter);	

};

//添加指定参数
function add_specified_parameter(){

	n++;
	var html_specified_parameter = '<div id="para_' + n + '" func="add_specified_parameter">Name值: <input type="text" name="para_name_' + n + '" />Value值: <input type="text" name="para_value_' + n + '" /><button type="button" onclick="delete_this_line(' + n + ');">删除</button></div>';
	$("#body_config").append(html_specified_parameter);
	
}

//删除当前行
function delete_this_line(x){

	$("#para_" + x).remove()

};

//生成参数
function get_paras(){

	var paras = '';

	//n==0, 没有添加任何参数
	if(n==0){
		paras = '';
	} else {
		for(var i=1; i<=n; i++){
			if(i == 1){
				paras = paras + get_para_sub(i);
			} else {
				paras = '&' + get_para_sub(i);
			};			
		};
	};

	var html_request_content = '<div><p>' + paras + '</p></div>'
	$("#request_content").after(html_request_content)

};

//生成参数
function get_para_sub(n){

	var para = '';
	if($("#para_" + n).attr("func") == "add_random_parameter"){
		para = para + get_random_string($("#para_name_" + n).val()) + '=';
		para = para + get_random_string($("#para_value_" + n).val());
	} else {
		para = para + $("#para_name_" + n).val() + '=';
		para = para + $("#para_value_" + n).val();
	}
}

//生成随机字符串
function get_random_string(len){

	var random_string = ''
	var chars='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
	var max_pos = chars.length;

	for(i=0; i<len; i++){
		random_string += chars.charAt(Math.floor(Math.random() * max_pos));
	};

	return random_string;

};

