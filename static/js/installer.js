var origin = window.location.origin;

$(function(){
  $("form").submit(function(){
    if(ga){
      console.log("ga present");
      var info = $(this).serialize().split("&");
      var version = info[0].split("=")[1];
      console.log(version);
      var packages = [];
      ga('send', 'event', 'install_version', version.replace("_", ""));
      info.slice(1).forEach(function(i){
        console.log(i);
        ga('send', 'event', 'install_package', i.split("=")[1]);
      });
    }
    var url = origin + "/get_installer?" + $(this).serialize();
    var command = "sudo apt-get install curl; curl '" + url + "' | sudo bash";
    $("#command-row pre").empty();
    $("#command-row pre").append(command);
    $("#command-row").show();
    return false;
  });
})
