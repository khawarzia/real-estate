$(document).ready(function()
    {
        $(document).on("click", ".fa-edit", function()

        {
            var i = $(this).attr("id").split("_");
            if(i[0] == "EditTourName")
            {
                $("#colFormLabelSm_tour_name_" + i[1] + "").removeAttr("readonly");
                $("#colFormLabelSm_tour_name_" + i[1] + "").removeClass("border-0");
            }
        });
    
      });

      $(document).ready(function () {

        $(document).on("click", ".fa-calendar-alt", function () {
            var i = $(this).attr("id");
            if (i == "cal_datepicker_0001") {
                $("#datepicker_0001").css("display", "block");
                $("#datepicker_0001_form").css("display", "block");
                $("#span_datepicker_0001").css("position", "relative");
                $("#span_datepicker_0001").css("top", "-22px");
                $("#cal_datepicker_0001").addClass("text-danger")
                
            }
        });

        $('#datepicker_0001').datepicker({
            uiLibrary: 'bootstrap4',
        });

    });

                                            function dateFunc(x) {

                                                $("#" + x + "_form").css("display", "none");
                                                $("#span_" + x + "").css("position", "relative");
                                                $("#span_" + x + "").css("top", "-22px");
                                                $("#span_" + x).html( '<i class="fas fa-calendar-alt fa-1x pr-1 text-secondary" id="cal_' + x + '"></i>'+ $("#" + x).val());

                                            }
        
                                            $(".list-group-item-action").hover(function(){
                                                var i = $(this).attr("id").split("_");
                                                if(i[0] == "list"){
                                                    $(this).addClass("text-danger");
                                                }
                                              });

                                              $(".list-group-item-action").mouseover(function(){
                                                var i = $(this).attr("id").split("_");
                                                if(i[0] == "list"){
                                                    $(this).addClass("text-danger");
                                                }
                                              });

                                              $(".list-group-item-action").mouseout(function(){
                                                var i = $(this).attr("id").split("_");
                                                if(i[0] == "list"){
                                                    $(this).removeClass("text-danger");
                                                }
                                              });