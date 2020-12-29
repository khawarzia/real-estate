function submitfunc(){
    var h = false;
    var a = document.getElementById('span_datepicker_0001').innerText;
    var b = document.getElementById('span_datepicker_0002').innerText;
    var c = document.getElementById('span_datepicker_0003').innerText;
    document.getElementById('datepicker_0001').value = a;
    document.getElementById('datepicker_0002').value = b;
    document.getElementById('datepicker_0003').value = c;
    if (a[0] != 'P' ){
        var d = document.getElementById('exampleFormControlSelect1_1').value;
        var e = document.getElementById('exampleFormControlSelect1_2').value;
        var f = document.getElementById('exampleFormControlSelect1_3').value;
        if (d[6] != 'P' || e[6] != 'P' || f[6] != 'P'){
            if (checking2()){
                if (checking3()){
                    $('#submitmodal').modal('show');
                    h = true;
                    setTimeout(function(){
                    document.getElementById('requestform').submit();},4000);
                }
                else{
                    document.getElementById('errortextmessage').innerText = 'Please pick a time for the third date.'
                    $('#nosubmitmodal').modal('show');
                    return;
                }
            }
            else{
                document.getElementById('errortextmessage').innerText = 'Please pick a time for the second date.'
                $('#nosubmitmodal').modal('show');
                return;
            }
        }
        else{
            document.getElementById('errortextmessage').innerText = 'Please select one time for the first date.'
            $('#nosubmitmodal').modal('show');
            return;
        }
    }
    if ( b[0] != 'P' ){
        var d = document.getElementById('exampleFormControlSelect2_1').value;
        var e = document.getElementById('exampleFormControlSelect2_2').value;
        var f = document.getElementById('exampleFormControlSelect2_3').value;
        if (d[6] != 'P' || e[6] != 'P' || f[6] != 'P'){
            if (checking3()){
                $('#submitmodal').modal('show');
                h = true;
                setTimeout(function(){
                document.getElementById('requestform').submit();},4000);
            }
            else{
                document.getElementById('errortextmessage').innerText = 'Please pick a time for the third date.'
                $('#nosubmitmodal').modal('show');
                return;
            }
        }
        else{
            document.getElementById('errortextmessage').innerText = 'Please pick a time for the second date.'
            $('#nosubmitmodal').modal('show');
            return;
        }
    }
    if (c[0] != 'P'){
        var d = document.getElementById('exampleFormControlSelect3_1').value;
        var e = document.getElementById('exampleFormControlSelect3_2').value;
        var f = document.getElementById('exampleFormControlSelect3_3').value;
        if(checking3()){
            if (d[6] != 'P' || e[6] != 'P' || f[6] != 'P'){
                if (checking3()){
                    $('#submitmodal').modal('show');
                    h = true;
                    setTimeout(function(){
                    document.getElementById('requestform').submit();},4000);
                }
                else{
                    document.getElementById('errortextmessage').innerText = 'Please pick a time for the third date.'
                    $('#nosubmitmodal').modal('show');
                    return;
                }
            }
            else{
                document.getElementById('errortextmessage').innerText = 'Please pick a time for the third date.'
                $('#nosubmitmodal').modal('show');
                return;
            }
        }
        else{
            document.getElementById('errortextmessage').innerText = 'Please pick a third date'
            $('#nosubmitmodal').modal('show');
            return;
        }
        
    }
  
    else{
        if (h == false){
            document.getElementById('errortextmessage').innerText = 'Please select at least one date.'
            $('#nosubmitmodal').modal('show');
        }
    }
}

function checking2(){
    var b = document.getElementById('span_datepicker_0002').innerText;
    if (b[0] == 'P'){
        var d = document.getElementById('exampleFormControlSelect2_1').value;
        var e = document.getElementById('exampleFormControlSelect2_2').value;
        var f = document.getElementById('exampleFormControlSelect2_3').value;
        if (d[6] != 'P' || e[6] != 'P' || f[6] != 'P'){
            return false;
        }
        else{
            return true;
        }
    }
    else{
        var d = document.getElementById('exampleFormControlSelect2_1').value;
        var e = document.getElementById('exampleFormControlSelect2_2').value;
        var f = document.getElementById('exampleFormControlSelect2_3').value;
        if (d[6] != 'P' || e[6] != 'P' || f[6] != 'P'){
            return true;
        }
        else{
            return false;
        }
    }
}

function checking3(){
    var b = document.getElementById('span_datepicker_0003').innerText;
    if (b[0] == 'P'){
        var d = document.getElementById('exampleFormControlSelect3_1').value;
        var e = document.getElementById('exampleFormControlSelect3_2').value;
        var f = document.getElementById('exampleFormControlSelect3_3').value;
        if (d[6] != 'P' || e[6] != 'P' || f[6] != 'P'){
            return false;
        }
        else{
            return true;
        }
    }
    else{
        var d = document.getElementById('exampleFormControlSelect3_1').value;
        var e = document.getElementById('exampleFormControlSelect3_2').value;
        var f = document.getElementById('exampleFormControlSelect3_3').value;
        if (d[6] != 'P' || e[6] != 'P' || f[6] != 'P'){
            return false;
        }
        else{
            return true;
        }
    }
}


        $(document).ready(function () {

            // Event Handler to close a list...
            $(document).on("click", ".close", function () {
                var i = $(this).attr("id").split("_");
                // console.log(i);
                if (i[0] == "close") {
                    $("#list_" + i[1] + "").css("display", "none");
                }
            });

            // Event Handler To Enter Tour Name
            $(document).on("click", ".form-control", function () {
                var i = $(this).attr("id");
                // console.log(i);
                if (i == "tourNameInput") {
                }
            });

            // Event Handler To click on edit button for Tour Name...
            $(document).on("click", ".fa-edit", function () {
                var i = $(this).attr("id");
                // console.log(i);
                if (i == "editTitleTour") {
                    $("#tourNameDisplay, #editTitleTour").hide();
                    // $("#editTitleTour").css("display", "none");
                    $("#tourNameInput").css("display", "block");
                    $("#tournametick").css("opacity", "1");
                    
                }
            });

            $(document).on("click", ".fa-check", function () {
                var i = $(this).attr("id");
                // console.log(i);
                if (i == "tournametick") {
                    $("#tourNameDisplay").css("display", "block");
                    $("#editTitleTour").css("display", "block");
                    $("#tourNameInput").css("display", "none");
                    $("#tournametick").css("opacity", "0");
                    document.getElementById('tourNameDisplay').innerHTML = document.getElementById('tourNameInput').value + '<i class="fas fa-edit text-secondary pl-1" id="editTitleTour"></i>';
                }
            });

            // Event handler for date pick in coulmn no 1
            $(document).on("click", ".fa-calendar-alt", function () {
                var i = $(this).attr("id");
                if (i == "cal_datepicker_0001") {
                    $("#datepicker_0001").css("display", "block");
                    $("#datepicker_0001_form").css("display", "block");
                    $("#span_datepicker_0001").css("position", "relative");
                    $("#span_datepicker_0001").css("top", "-22px");
                    $("#cal_datepicker_0001").addClass("text-danger");
                }
                else if (i == "cal_datepicker_0002") {
                    $("#datepicker_0002").css("display", "block");
                    $("#datepicker_0002_form").css("display", "block");
                    $("#span_datepicker_0002").css("position", "relative");
                    $("#span_datepicker_0002").css("top", "-22px");
                    $("#cal_datepicker_0002").addClass("text-danger");
                }
                else if (i == "cal_datepicker_0003") {
                    $("#datepicker_0003").css("display", "block");
                    $("#datepicker_0003_form").css("display", "block");
                    $("#span_datepicker_0003").css("position", "relative");
                    $("#span_datepicker_0003").css("top", "-22px");
                    $("#cal_datepicker_0003").addClass("text-danger");
                    
                }
            });

            var today;
            today = new Date(new Date().getFullYear(), new Date().getMonth(), new Date().getDate()+1);

            $('#datepicker_0001').datepicker({
                uiLibrary: 'bootstrap4',
                minDate: today
            });

            $('#datepicker_0002').datepicker({
                uiLibrary: 'bootstrap4',
                minDate: today
            });

            $('#datepicker_0003').datepicker({
                uiLibrary: 'bootstrap4',
                minDate: today
            });

        });
    
    function dateFunc(x) 
    {
        $("#" + x + "_form").css("display", "none");
        $("#span_" + x + "").css("position", "relative");
        $("#span_" + x + "").css("top", "-22px");
        $("#span_" + x).html($("#" + x).val() + '<i class="fas fa-calendar-alt fa-1x " id="cal_' + x + '"></i>');
    }

    $('.dropdown-menu li').on('click', function() {
        var getValue = $(this).text();
        $('.dropdown-select').text(getValue);
    });