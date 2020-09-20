$(document).ready(function(){
    $("#btn").click(function(){
        var files = document.getElementById('file').files[0];
        if (files.size > 5120000)
        {
            $("#imfo").text("你上传的文件超过5M啦");
            return false;
        }
    })
})