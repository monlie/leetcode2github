// ==UserScript==
// @name         leetcode2github
// @namespace    http://codes.monlab.top/l2g
// @version      0.0.1
// @description  Uploads your codes from leetcode to github automatically.
// @author       monlie
// @match        *://leetcode-cn.com/submissions/detail/*
// @require      https://cdn.bootcss.com/jquery/1.10.2/jquery.min.js
// @grant        GM_addStyle
// @icon         https://s1.ax1x.com/2018/05/27/Ch30OK.png
// ==/UserScript==
// 可是我真的不会写前端orz

(function() {
    GM_addStyle('#upload-code-btn{position:relative; left:74%}');

    function get_codes() {
        var code = "";
        $("div.ace_line").each(function (i, line) {
            code += ($(line).text()) + '\n';
        });
        var host = "https://leetcode-cn.com";
        var name = $("a.inline-wrap").text();
        var url = host + $("a.inline-wrap").attr("href");
        var language = $("#result_language").text();
        var time = $("#result_runtime").text();
        var user = $(".username").find("b").first().text();
        return {"url": url, "name": name, "language": language, "time": time, "user": user, "code": code}
    }

    var upload_btn_html = '<div class="pull-middle">';
    upload_btn_html += '<button id="upload-code-btn" class="btn btn-primary">&nbsp;&nbsp;上传代码&nbsp;&nbsp;</button>';
    upload_btn_html += '</div>';

    var upload_info_html = '<div class="pull-m">上传状态：<span id="upload_info">未上传</span></div>'

    var pos = $('#edit-code-btn').parent().parent();
    pos.append(upload_btn_html);
    pos.append(upload_info_html);
    var upload_btn = $('#upload-code-btn');
    var upload_info = $('#upload_info');
    upload_info.css('color', '#9a9a9a');

    $(function () {
        $('#upload-code-btn').click(function () {
            var info = get_codes();
            $.post("URL",                  // replace URL with the real url of your server
                   info, function (data, status) {
                   upload_info.text(data.data);
                   upload_info.css('color', 'green');
                   upload_btn.attr("disabled", true);
            });
        });
    });
})();
