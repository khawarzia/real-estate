

            function removefunc(){
                var a = document.getElementById('listid').value;
                var h = new XMLHttpRequest();
                h.open("GET","/unlink/"+a);
                h.send();
                alert('List has been unlinked');
            }
        
// ================================================================================

        $(document).ready(function()
        {
            $(document).on("mouseover", ".list-group-item-secondary", function()
            {
                // console.log($(this).attr("id"));
                $("#" + $(this).attr("id").split("_")[1] + "").css("color", "#dc3545");
            });

            $(document).on("mouseout", ".list-group-item-secondary", function()
            {
                // console.log($(this).attr("id"));
                $("#" + $(this).attr("id").split("_")[1] + "").css("color", "black");
            });
        });
        
        // ===================================================

// function e(a){
//             var b = document.getElementById(a).removeAttribute('readonly');
//             // var c = document.getElementById('savesubmit'+a).style = '';
//             // var input_id = $(this).attr("id");
//                 // var list_id = input_id.split("_")[1];
//                 $("#row" + a + "").css("border", "1px solid #dc3545");
//                 $("#circle_" + a + "").css("color", "red");
//                 $("#circle_" + a + "").addClass("text-danger");
//                 $("#share_" + a + "").css("color", "red");
//                 $("#share_" + a + "").addClass("text-danger");
//                 $("#edit_" + a + "").css("color", "red");
//                 $("#edit_" + a + "" ).removeClass("fa-edit");
//                 $("#edit_" + a + "").addClass("fa-check text-danger");
//                 $("#edit_" + a + "").click(function(){
//                     document.getElementById('form'+a).submit();
//                 })
                
//                 $("#" + a+ "").css("background-color", "white");
//                 $("#" + a + "").hover( function()
//                 {
//                     $("#" + a+ "").css("background-color", "white");
//                 });
                
//         }
        
// function e(a){
//     var b = document.getElementById(a).removeAttribute('readonly');
//     document.getElementById(a).focus();
//             console.log(a);
//     var val = document.getElementById(a).value; //store the value of the element
//     document.getElementById(a).value = ''; //clear the value of the element
//     document.getElementById(a).value = val; //set that value back.
//         // $("#row" + a + "").css("border", "1px solid #dc3545");
//         $('#editButton_'+a).attr('onclick','this.form.submit();');
//         $("#row_" + a + "").addClass("border border-danger");
//         // $(""+a+"" ).addClass("text-dark");
//         $("#circle_" + a + "").css("color", "#dc3545");
//         $("#circle_" + a + "").addClass("text-danger");
//         $("#share_" + a + "").css("color", "#dc3545");
//         $("#share_" + a + "").addClass("text-danger");
//         $("#copy_" + a + "").css("color", "#dc3545");
//         $("#copy_" + a + "").addClass("text-danger");
//         $("#edit_" + a + "").css("color", "#dc3545");
//         $("#edit_" + a + "" ).removeClass("fa-edit");
//         $("#edit_" + a + "").addClass("fa-check text-danger");
//         $("#" + a+ "").css("background-color", "white");
//         $("#tourRequestStatus_" + a + "").css("display" , "none");
//         $("#tourRequestCalendar_" + a + "").css("display" , "none");
//         $("#tourRequestDate_" + a + "").css("display" , "none");
//         $("#editButton_" + a + "").css("left" , "0px");
//         $("#remove_" + a + "").css("left" , "0px");
//         // console.log($("#" + a + "").attr("data-type"));margin-left: 92px;
//         if($("#" + a + "").attr("data-type")){
//             $("#" + a + "").css("width", "43.4%");
//             $("#editButton_" + a + "").css("margin-left" , "92px");
//         }
//         else{
//             $("#" + a + "").css("width", "70%");    
//         }
//         // $("#" + a + "").css("width", "92%");
//         $("#" + a + "").hover( function()
//         {
//             $("#" + a+ "").css("background-color", "white");
            
//         });                
//         $("#row_" + a + "").css("background-color", "white");

//         $("#row_" + a + "").hover( function()
//         {
//             $("#" + a+ "").css("background-color", "white");
//         });

//         // console.log("sdsdfd");
// }

// ============================================

// =======// =======================================
                // $(document).on("mouseover", ".list-group-item-action", function()
                // {
                
                //    $("#" + $(this).attr("id").split("_")[1] + "").css("background-color", "white"); 
                //    $("#" + $(this).attr("id").split("_")[1] + "").css("color", "#dc3545"); 
                //    $("#row_" + $(this).attr("id").split("_")[1] + "").css("background-color", "white"); 
                // });
                // $(document).on("mouseout", ".list-group-item-action", function()
                // {
                    
                //     $("#" + $(this).attr("id").split("_")[1] + "").css("background-color", "rgb(240, 240, 240)"); 
                //     $("#" + $(this).attr("id").split("_")[1] + "").css("color", "black"); 
                //    $("#row_" + $(this).attr("id").split("_")[1] + "").css("background-color", "rgb(240, 240, 240)");
                // });
            // =============================================================

        function relocate(a){
            if (document.getElementById(a).hasAttribute('readonly') == true){
                window.location.href = '/show-tour/'+a;
            }
        }
        function deletelist(a){
            window.location.href = '/delete-tour/'+a;
        }
        $(document).ready(function () {
            var i = 1;

            // Mouseover event for remove...
            $(document).on('mouseover', '.fa-times-circle', function () {
                var button_id = $(this).attr("id");
                $("#" + button_id + "").css("color", "#dc3545");
            });

            // Mouseout event for remove...
            $(document).on('mouseout', '.fa-times-circle', function () {
                var button_id = $(this).attr("id");
                $("#" + button_id + "").css("color", "black");
            });

            // Mouse over for share ...
            $(document).on('mouseover', '.fa-share-square', function () {
                var button_id = $(this).attr("id");
                $("#" + button_id + "").css("color", "#dc3545");
            });

            // Mouseout event for share...
            $(document).on('mouseout', '.fa-share-square', function () {
                var button_id = $(this).attr("id");
                $("#" + button_id + "").css("color", "black");
            });

            // Mouse over for edit ...
            $(document).on('mouseover', '.fa-edit', function () {
                var button_id = $(this).attr("id");
                $("#" + button_id + "").css("color", "#dc3545");
            });

            // Mouseout event for edit...
            $(document).on('mouseout', '.fa-edit', function () {
                var button_id = $(this).attr("id");
                $("#" + button_id + "").css("color", "black");
            });

            // Mousein event for save...
            $(document).on('mouseover', '.fa-save', function () {
                var button_id = $(this).attr("id");
                $("#" + button_id + "").css("color", "#dc3545");
            });

            // Mouseout event for save...
            $(document).on('mouseout', '.fa-save', function () {
                var button_id = $(this).attr("id");
                $("#" + button_id + "").css("color", "black");
            });

            // Mousein event for copy...
            $(document).on('mouseover', '.fa-copy', function () {
                var button_id = $(this).attr("id");
                $("#" + button_id + "").css("color", "#dc3545");
            });

            // Mouseout event for copy...
            $(document).on('mouseout', '.fa-copy', function () {
                var button_id = $(this).attr("id");
                $("#" + button_id + "").css("color", "black");
            });

              // Mousein event for link...
              $(document).on('mouseover', '.fa-link', function () {
                var button_id = $(this).attr("id");
                $("#" + button_id + "").css("color", "#dc3545");
            });

            // Mouseout event for link...
            $(document).on('mouseout', '.fa-link', function () {
                var button_id = $(this).attr("id");
                $("#" + button_id + "").css("color", "black");
            });

            // Mousein event for unlink...
            $(document).on('mouseover', '.fa-unlink', function () {
                var button_id = $(this).attr("id");
                $("#" + button_id + "").css("color", "#dc3545");
            });

            // Mouseout event for unlink...
            $(document).on('mouseout', '.fa-unlink', function () {
                var button_id = $(this).attr("id");
                $("#" + button_id + "").css("color", "black");
            });

            // Click on Remove Button
            $(document).on('click', '.btn-dark', function () {
                var list_id = $(this).attr("id").split("_")[1];
                // $(this).css("background-color" , "red");
                // $(this).css("color" , "white");
                // console.log(button_id);
                // $('#row' + button_id + '').remove();
                if ($("#exampleModalCenter_" + list_id + "").length) {
                    // var A = 
                    // var res = '<p class="card-text text-center">Are you sure you want to delete</p><a class="alert-link text-center mx-auto" href="#">' + $("#lst" + list_id + "").html() + '</a> From your Interest List?'
                    $("#modelBody_" + list_id + "").html('<p class="card-text text-center">Are you sure you want to delete <br> <br><a class="alert-link mx-auto text-center" href="#">' + $("#"+list_id).value + '</a>?' + '<p class="card-text text-center" style="font-size:12px;">This action will delete the selected Tour and all properties within it.</p></p>');
                    $("#modelFooterButton_"+ list_id + "").html("Delete");
                    // $("#modelBody_" + list_id + "").html($("#row" + list_id + "").val());
                    // console.log($("#row" + list_id + "").html());
                    // $("#modelBody_" + list_id + "").html($("#row" + list_id + "").html());
                    $('#exampleModalCenter_' + list_id + '').modal('show');
                    
                }
                else {
                    
                    $("#dynamic_field").prepend('<div class="modal fade" id="exampleModalCenter_' + list_id + '" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true"><div class="modal-dialog modal-dialog-centered" role="document"><div class="modal-content"><div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-label="Close" id="modelClose_' + list_id + '"><span aria-hidden="true">&times;</span></button></div><div class="modal-body" id="modelBody_' + list_id + '"></div><div class="modal-footer"><button type="button" class="btn btn-danger mx-auto" onclick="deletelist('+list_id+')" id="modelFooterButton_'+ list_id+'"></button></div></div></div></div>');
                    // var res = 
                    $("#modelBody_" + list_id + "").html('<p class="card-text text-center">Are you sure you want to delete <br> <br><a class="alert-link mx-auto text-center" href="/show-tour/'+list_id+'">' + document.getElementById(list_id).value  + '</a> ?' + '<p class="card-text text-center" style="font-size:12px;">This action will delete the selected Tour and all properties within it.</p></p>');
                    $("#modelFooterButton_"+ list_id + "").html("Delete");
                    // console.log($("#row" + list_id + "").html());
                    // $("#modelBody_" + list_id + "").html($("#row" + list_id + "").html());
                    $('#exampleModalCenter_' + list_id + '').modal('show');
                }

            });

            // on click event for input:

            $(document).on('focus', ".form-control", function () {
                var input_id = $(this).attr("id");
                var list_id = input_id.split("_")[1];
                $("#row" + list_id + "").css("border", "1px solid #dc3545");
                $("#circle_" + list_id + "").css("color", "#dc3545");
                $("#share_" + list_id + "").css("color", "#dc3545");
                $("#edit_" + list_id + "").css("color", "#dc3545");
                $("#copy_" + list_id + "").css("color", "#dc3545");
                $("#link_" + list_id + "").css("color", "#dc3545");
                $("#" + list_id + "").css("background-color", "white");
            });

            $(document).on('click', ".form-control", function () {
                var input_id = $(this).attr("id");
                var list_id = input_id.split("_")[1];
                $("#row" + list_id + "").css("border", "1px solid #dc3545");
                $("#circle_" + list_id + "").css("color", "#dc3545");
                $("#share_" + list_id + "").css("color", "#dc3545");
                $("#edit_" + list_id + "").css("color", "#dc3545");
                $("#copy_" + list_id + "").css("color", "#dc3545");
                $("#link_" + list_id + "").css("color", "#dc3545");
                $("#" + list_id + "").css("background-color", "white");
            });

            $(document).on('focusin', ".form-control", function () {
                var input_id = $(this).attr("id");
                var list_id = input_id.split("_")[1];
                $("#row" + list_id + "").css("border", "1px solid #dc3545");
                $("#circle_" + list_id + "").css("color", "#dc3545");
                $("#share_" + list_id + "").css("color", "#dc3545");
                $("#edit_" + list_id + "").css("color", "#dc3545");
                $("#copy_" + list_id + "").css("color", "#dc3545");
                $("#link_" + list_id + "").css("color", "#dc3545");
                $("#" + list_id + "").css("background-color", "white");
            });

            $(document).on('focusout', ".form-control", function () {
                var input_id = $(this).attr("id");
                var list_id = input_id.split("_")[1];
                $("#row" + list_id + "").css("border", "1px solid rgba(0,0,0,.125)");
                $("#circle_" + list_id + "").css("color", "black");
                $("#share_" + list_id + "").css("color", "black");
                $("#edit_" + list_id + "").css("color", "black");
                $("#copy_" + list_id + "").css("color", "black");
                $("#link_" + list_id + "").css("color", "black");
                
            });

            // Click on Share Button
                // $("#share_" + list_id + "").css("color", "black");
                // $('#share_'+list_id+"").css("color", "red");
                // console.log(list_id);
                // $("#share_" + list_id + "").css("color", "red");
                
            // // Mouseout event for share...
            // $(document).on('mouseout', '.fa-share-square', function () {
            //     var button_id = $(this).attr("id");
            //     $("#" + button_id + "").css("color", "red");
            // });
            });

// ================================================================================
$(document).ready(function()
{
    $(document).on("click", ".btn-white", function()
    {
        var i = $(this).attr("id").split("_");
        if(i[0] == "linkButton"){
            $("#Name_"+ i[1] + "").css("display", "none");
            // $("#BuyerNameForm_"+ i[1] + "").css("display", "inline");
            $("#BuyerName_"+ i[1] + "").css("display", "inline");
        }
        // console.log(i);
    });
    // $("#exampleModalCenterBuyerReference88Slide").modal('show');
});
