
// For Property Images...

$('.carousel').carousel({
  interval: false,
  wrap:false
});

// For Search through Interested Dropdown...

$(document).ready(function(){
    $("#myInput").on("keyup", function() {
      var value = $(this).val().toLowerCase();
      $("#lists_buyers label").filter(function() {
        $(this).toggle($(this).text().toLowerCase().startsWith(value) || $(this).text().toLowerCase().indexOf(value) > -1)
      });
    });
  
  $("#myInput_2").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#lists_buyers label").filter(function() {
      $(this).toggle($(this).text().toLowerCase().startsWith(value) || $(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});

  $(document).ready(function () {

// mouseover event for a list element
$(document).on("mouseover", ".list-group-item-action", function () {
  // if ($(this).attr("id").indexOf("listHeading") >= 0)
  // {
    console.log($(this).attr("id"));
    $("#listHeading_" + $(this).attr("id").split("_")[1] + "").css("color", "#dc3545");
    $("#buttonImageA_" + $(this).attr("id").split("_")[1] + "").css("display", "block");
    $("#buttonImageB_" + $(this).attr("id").split("_")[1] + "").css("display", "block");
    $("#buttonImageC_" + $(this).attr("id").split("_")[1] + "").css("display", "block");
  // }
  
});

//   mouseout event for a list element
$(document).on("mouseout", ".list-group-item-action", function () {
  // if ($(this).attr("id").indexOf("listHeading") >= 0)
  // console.log($(this).attr("id"));
  {
    $("#listHeading_" + $(this).attr("id").split("_")[1] + "").css("color", "black");
    $("#buttonImageA_" + $(this).attr("id").split("_")[1] + "").css("display", "none");
    $("#buttonImageB_" + $(this).attr("id").split("_")[1] + "").css("display", "none");
    $("#buttonImageC_" + $(this).attr("id").split("_")[1] + "").css("display", "none");
  }

});

});  

// $(document).ready(function()
// {
//     $('#exampleModalCenter_0003').modal('show');
//     $(document).on('click', '.btn-secondary', function(){
//         // $("#" + $(this).attr("id")).button('toggle');
//         var i = $(this).attr("id").split("_");
//         // console.log($(this).attr("id"));
//         if(i[0] == "dropDown"){
//             if($("#exampleModalCenterSuccessfullyAddedExistingInterestList_" + i[1]).length == 0)
//             {
//                 $("#mainDiv").append('<div class="modal fade" id="exampleModalCenterSuccessfullyAddedExistingInterestList_'+i[1]+'" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true"><div class="modal-dialog modal-dialog-centered" role="document"><div class="modal-content"><div class="modal-header border-0"><button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button></div><div class="modal-body text-center"><h4 class="modal-title mx-auto text-center text-wrap font-weight-bold text-danger" id="exampleModalCenterTitle">Done!</h4><br><span class="text-dark font-weight-bold text-center mx-auto text-wrap" style="width:10px;">'+ $("#listHeading1").html() +', '+ $("#listHeading2").html() +'<br> has been added to <a href="#" class="text-danger">'+ $("#dropDown_"+ i[1]+" span").html() +'</a><br> for Buyer <a href="#" class="text-danger"> Janer</a></span><br><br><a class="text-danger font-weight-bold" href="#">Manage Interest Lists</a></div></div></div></div>');
//                 // $("#"+i+"").addClass('active');
//                 $("#exampleModalCenterSuccessfullyAddedExistingInterestList_"+ i[1]).modal('show');
//             }   
//             else{
//                 // $("#" + i).button('toggle');
//                 $("#exampleModalCenterSuccessfullyAddedExistingInterestList_"+ i[1]).modal('show');

//             }
//         }
//     });
// });

// Click Event on property list item to show property modal
$(document).ready(function()
{
    $(document).on("click", ".list-group-item-action", function()
    {
      // console.log($(this).attr("id"));
        var i = $(this).attr("id").split("_");
        if(i[0] == "lst")
        {
          elem = document.getElementById($(this).attr("id"));
          // console.log(elem);
          if($(elem).attr("data-target"))
          {
            var t = $(elem).attr("data-target");
            if($(t).length == 0)
            {
              
              // $("#header_Card").prepend('<div class="modal fade" id="exampleModalCenter_'+ i[1]+'" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true"> <div class="modal-dialog modal-dialog-centered" role="document"> <div class="modal-content"> <div class="modal-header border-0" style="background-color: #d8dce0;"> <button type="button" class="close" data-dismiss="modal" aria-label="Close"> <span aria-hidden="true">&times;</span> </button> </div> <div class="modal-body m-0 p-0" style="background-color: #d8dce0;"> <div class="container p-0 m-0 pt-0 pl-4 pr-4"> <div class="row p-0 m-0"> <div class="col-sm-7 p-0 m-0"> <div class="row p-0 m-0"> <div class="col p-0 m-0"> <span class="font-weight-bold" id="listHeading1">3180 Cortez Rd</span><br> <span class="font-weight-normal" id="listHeading2">Pebble Beach, CA 93953</span><br> <span class="font-weight-normal">Status <span class="font-weight-bold">Active</span><br> <span class="font-weight-normal">48 days on market</span><br> <span class="font-weight-normal">MLs#1234567890</span> </div> <div class="col"> <span class="font-weight-bold float-right" style="font-size: 26px;">3180 Cortez Rd</span><br><br> <span class="font-weight-bold float-right">14,000 sqft | 5 beds | 4 baths</span><br> </div> </div> <div class="row"> <div class="col"> <table class="table table-borderless"> <tbody> <tr> <td>Property Type</td> <td>Single Family</td> <td>Heating</td> <td>Forced Air</td> </tr> <tr> <td>Year Built</td> <td>1984</td> <td>Colling</td> <td>Central Forced Air</td> </tr> <tr> <td>Lot Size</td> <td>14,000 sqft</td><td>Fireplaces</td> <td>14,000 sqft</td> </tr> <tr> <td>Stories</td> <td>3</td> <td>Flooring</td> <td>Laminate</td> </tr> <tr> <td>Parking</td> <td>Attached</td> <td>Rof</td> <td> Tile</td> </tr> <tr> <td>Garage Spaces</td> <td>2</td> <td>Pool</td> <td>None</td></tr> </tbody> </table> </div> </div> <div class="row overflow-auto pl-3" style="height: 150px;"> Why painful the sixteen how minuter looking nor. Subject but why ten earnest husband imagine sixteen brandon. Are unpleasing occasional celebrated motionless unaffected conviction out. Evil make to no five they. Stuff at avoid of sense small fully it whose an. Ten scarcely distance moreover handsome age although. As when have find fine or said no mile. He in dispatched in imprudence dissimilar be possession unreserved insensible. She evil face fine calm have now. Separate screened he outweigh of distance landlord. Smile spoke total few great had never their too. Amongst moments do in arrived at my replied. Fat weddings servants but man believed prospect. Companions understood is as especially pianoforte connection introduced. Nay newspaper can sportsman are admitting gentleman belonging his. Is oppose no he summer lovers twenty in. Not his difficulty boisterous surrounded bed. Seems folly if in given scale. Sex contented dependent conveying advantage can use. </div> </div> <div class="col-lg-5"> <div id="carouselExampleControls" class="carousel slide" data-ride="carousel"> <ol class="carousel-indicators"> <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li> <li data-target="#carouselExampleIndicators" data-slide-to="1"></li> <li data-target="#carouselExampleIndicators" data-slide-to="2"></li></ol> <div class="carousel-inner"> <div class="carousel-item active"> <img src="download.jpg" class="d-block w-100" alt="..."> <span class="font-weight-bold text-center">Silicon Valley</span> </div> <div class="carousel-item"> <img src="download.jpg" class="d-block w-100" alt="..."> <span class="font-weight-bold">New York</span> </div> <div class="carousel-item"> <img src="download.jpg" class="d-block w-100" alt="..."> <span class="font-weight-bold">USA</span> </div> </div> <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev"> <span class="carousel-control-prev-icon" aria-hidden="true"></span> <span class="sr-only">Previous</span> </a> <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next"> <span class="carousel-control-next-icon" aria-hidden="true"></span> <span class="sr-only">Next</span> </a> </div> <div class="row mb-0 pb-0"> <div class="col-sm-4 mt-5 mb-0 pb-0 ml-0"> <div class="dropdown"> <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" style=" width:100px;"> Interested </button> <div class="dropdown-menu text-center" aria-labelledby="dropdownMenuButton"> <input class="form-control mb-2" id="myInput" type="text" placeholder="Search"> <li class="list-group-item list-group-item-action mb-1 bg-secondary text-white font-weight-normal" data-toggle="modal" data-target="#exampleModalCenterInterstList" id="newListModal_'+i[1]+'"> New Interest List</li> <div class="btn-group-toggle mt-1" data-toggle="buttons" style="width:100%; border-radius: 0;" id="lists_buyers"> <label class="btn btn-secondary " style="width:100%;border-radius: 0" id="dropDown_0001" data-toggle="modal" data-target="#exampleModalCenterSuccessfullyAddedExistingInterestList_0001"> <input type="checkbox" checked style="width:100%;border-radius: 0"> <span> Jane Doe</span> </label> </div> <div class="btn-group-toggle mt-1" data-toggle="buttons" style="width:100%; border-radius: 0;" id="lists_buyers"> <label class="btn btn-secondary" style="width:100%;border-radius: 0;" id="dropDown_0002" data-toggle="modal" data-target="#exampleModalCenterSuccessfullyAddedExistingInterestList_0002"> <input type="checkbox" checked style="width:100%;border-radius: 0"><span> List Network</span> </label> </div> <div class="btn-group-toggle mt-1" data-toggle="buttons" style="width:100%; border-radius: 0;" id="lists_buyers"> <label class="btn btn-secondary" style="width:100%;border-radius: 0" id="dropDown_'+ i[1]+'" data-toggle="modal" data-target="#exampleModalCenterSuccessfullyAddedExistingInterestList_'+ i[1]+'"> <input type="checkbox" checked style="width:100%;border-radius: 0"><span> List Fremont</span></label></div></div></div> </div><div class="col-sm-4 mt-5 mb-0 pb-0"><div class="dropdown"><button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton_2" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"style="width:100px;">Tour</button><div class="dropdown-menu text-center" aria-labelledby="dropdownMenuButton_2"><input class="form-control mb-2" id="myInput_2" type="text" placeholder="Search"><li class="list-group-item list-group-item-action mb-1 bg-secondary text-white font-weight-normal">New Interest List</li><div class="btn-group-toggle mt-1" data-toggle="buttons" style="width:100%; border-radius: 0;" id="lists_buyers"><label class="btn btn-secondary " style="width:100%;border-radius: 0" id="dropDown2_0001"><input type="checkbox" checked style="width:100%;border-radius: 0"> <span class="m-0 p-0">Jane Doe</span></label></div><div class="btn-group-toggle mt-1" data-toggle="buttons" style="width:100%; border-radius: 0;"id="lists_buyers"><label class="btn btn-secondary" style="width:100%;border-radius: 0;" id="dropDown2_0002"><input type="checkbox" checked style="width:100%;border-radius: 0"><span> ListNetwork</span></label></div><div class="btn-group-toggle mt-1" data-toggle="buttons" style="width:100%; border-radius: 0;" id="lists_buyers"><label class="btn btn-secondary" style="width:100%;border-radius: 0" id="dropDown2_'+i[1]+'"><input type="checkbox" checked style="width:100%;border-radius: 0"><span> ListFremont</span></label></div></div></div></div><div class="col-lg-4 mt-5 mb-0 pb-0"><div class="dropdown"><button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton_2"data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"style="width:100px;">Offer</button><div class="dropdown-menu text-center" aria-labelledby="dropdownMenuButton_2"><input class="form-control mb-2" id="myInput_2" type="text" placeholder="Search"> <li class="list-group-item list-group-item-action mb-1 bg-secondary text-white font-weight-normal">New Interest List</li><div class="btn-group-toggle mt-1" data-toggle="buttons" style="width:100%; border-radius: 0;" id="lists_buyers"><label class="btn btn-secondary " style="width:100%;border-radius: 0" id="dropDown2_0001"><input type="checkbox" checked style="width:100%;border-radius: 0"> <span class="m-0 p-0">Jane Doe</span></label></div><div class="btn-group-toggle mt-1" data-toggle="buttons" style="width:100%; border-radius: 0;"id="lists_buyers"><label class="btn btn-secondary" style="width:100%;border-radius: 0;" id="dropDown2_0002"><input type="checkbox" checked style="width:100%;border-radius: 0"><span> ListNetwork</span></label></div><div class="btn-group-toggle mt-1" data-toggle="buttons" style="width:100%; border-radius: 0;"id="lists_buyers"><label class="btn btn-secondary" style="width:100%;border-radius: 0" id="dropDown2_'+i[1] +'"><input type="checkbox" checked style="width:100%;border-radius: 0"><span> ListFremont</span></label></div></div></div></div></div><div class="row"><a class="text-center text-danger mx-auto" href="#">More Information</a></div></div></div></div></div></div></div></div>');              
              
              // $('#exampleModalCenterInterstList').css("height", "200px");
              // $('#exampleModalCenterInterstList').css("height", "200px");

              var z = $('#exampleModalCenter_' + i[1]+ '').css("z-index");
              // console.log(z);
              $('#exampleModalCenterInterstList').css("z-index", z+String("1"));
              $('#exampleModalCenter_' + i[1]+ '').modal('show');
            }
            else
            {
              // $('#exampleModalCenter_' + i[1]+ '').css("height", "100px");
              // $('#newListModal_' + i[1]+ '').css("height", "100px");
              // $('#exampleModalCenterInterstList').css("height", "100px");
              var z = $('#exampleModalCenter_' + i[1]+ '').css("z-index");
              // console.log(z);
              $('#exampleModalCenterInterstList').css("z-index", z+String("1"));
              $('#exampleModalCenter_' + i[1]+ '').modal('show');
            }
          }
        }
    });
});
// $("#pop_up_interest_list_review_satus_0001").click(function()
// {

// });

// In Popup moodel ... Popover template
$(document).ready(function () {
    $('[data-toggle="popover"]').popover(
        {
            title: "Interest List Review Legend",
            template: '<div class="popover bg-dark text-white" role="tooltip"><div class="arrow text-dark" ></div><h3 class="popover-header text-white bg-dark">Interest List Review Legend</h3><i class="fas fa-smile fa-2x ml-4" style="color: red;background-color: white; border-radius: 1.25rem;"></i><i class="fas fa-frown fa-2x ml-5" style="color: red;background-color: white; border-radius: 1.25rem;"></i><i class="fas fa-meh fa-2x ml-5" style="color: red;background-color: white; border-radius: 1.25rem;"></i><br><span class="pl-4">Like</span><span class="pl-5">Dislike</span><span class="pl-4">Not Sure</span></div>'
        }
    );
    // $("#exampleModalCenterSuccessfullyAddedInterestList").modal('show');

    // $('#exampleModalCenterSuccessfullyAddedInterestList').on('hidden.bs.modal', function (e) {
    //   // do something...
    // })
});
