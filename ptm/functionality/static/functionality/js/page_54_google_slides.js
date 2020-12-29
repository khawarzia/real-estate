$(document).ready( function()
    {
        
        // Event Handler to close a list...
        $(document).on("click", ".close", function()
        {
            var i = $(this).attr("id").split("_");
            // console.log(i);
            if(i[0] == "close")
            {
                $("#list_" + i[1] + "").css("display","none");
            }
        });

    });
    
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
                // console.log($(this).attr("class"));
                $(this).addClass(" is-valid");
            }
        });

        // Event Handler To click on edit button for Tour Name...
        $(document).on("click", ".fa-edit", function () {
            var i = $(this).attr("id");
            // console.log(i);
            if (i == "editTitleTour") {
                $("#tourNameDisplay").css("display", "none");
                $("#editTitleTour").css("display", "none");
                $("#tourNameInput").css("display", "block");
            }
        });

        // Event handler for date pick in coulmn no 1
        $(document).on("click", ".fa-calendar-alt", function () {
            var i = $(this).attr("id");
            if (i == "date_0001") {
                $("#datepicker_0001").css("display", "block");
                $("#datepicker_0001_form").css("display", "block");
            }
            else if (i == "date_0002") {
                $("#datepicker_0002").css("display", "block");
                $("#datepicker_0002_form").css("display", "block");
            }
            else if (i == "date_0003") {
                $("#datepicker_0003").css("display", "block");
                $("#datepicker_0003_form").css("display", "block");
            }
        });

        $('#datepicker_0001').datepicker({
            uiLibrary: 'bootstrap4'
        });

        $('#datepicker_0002').datepicker({
            uiLibrary: 'bootstrap4'
        });

        $('#datepicker_0003').datepicker({
            uiLibrary: 'bootstrap4'
        });

        // $(document).load($('#exampleModalCenterError').modal('show'));
        $(document).load($('#exampleModalCenterSuccess').modal('show'));

    });
