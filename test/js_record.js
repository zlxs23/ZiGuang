// 这是学习 jQuery methods 记录
$ // 即 jQuery
// selector
$(selector).action();
$(document).ready(function() {}) == $(function() {});
$('p').hide();
$('p.cls').hide(); // class = 'cls''s p
$('p#id').hide(); // id = 'id''s p
$('*'); // select all element
$(this); // select current HTNL element
$('p:first'); // select the first <p> element
$('ul li:first'); // select the first <ul>'s the first <li> element
$('ul li:first-child'); // select all <ul>'s the first <li> element
$('[href]'); // select have href's element
$("a[target='_blank']"); // select all target's attr_value == _blank's <a> element
$("a[target!='_blank']"); // select all target's attr_value != _blank's <a> element
$(':button'); // select all type='button''s button element AND input element
$('re.even'); // select 偶数 位置 的 <tr> element
$('tr:odd'); // select 奇数 位置 的 <tr> element
// event
/*
	mouse's event: click, dblclick, mouseenter, mouseleave
	keyboard's event: keypress, keydown, keyup
	form's event: submit, change, focus, blur
	document/window's event: load, resize, scroll, unload
*/
// most DOM event has a equal jQuery method
$('p').click(); // click the <p> content
$('p').dblclick(); // double click the <p> content
$('#p1').mouseenter(); // when mouse cross the element
$('.p1').mouseleave(); // when mouse leave the element
$('.p1').mousedown(); // when mouse 移动到该元素上方，并按下
$('#p1').mouseup(); // when mouse 放松鼠标时
$('#p1').hover(); // 模拟 光标悬停 -- 当鼠标移动 ele 上方时触发一个事件，离开时触发另一个事件
$('input').focus(); // when 获得聚焦 焦点 发生 focus event
$('input').blur(); // when 失去焦点 发生 blur event