var inputsRy = {
  sliderWidth: 250,
  minRange: +50,
  maxRange: +210, 
  outputWidth:30, // output width
  thumbWidth: 20, // thumb width
  thumbBorderWidth: 5,
  trackHeight: 4,
  theValue: [80, 160] // theValue[0] < theValue[1]
};
var isDragging0 = false;
var isDragging1 = false;

var range = inputsRy.maxRange - inputsRy.minRange;
var rangeK = inputsRy.sliderWidth / range;
var container = document.querySelector(".container");
var thumbRealWidth = inputsRy.thumbWidth + 2 * inputsRy.thumbBorderWidth;

// styles
var slider = document.querySelector(".slider");
slider.style.height = inputsRy.trackHeight + "px";
slider.style.width = inputsRy.sliderWidth + "px";
slider.style.paddingLeft = (inputsRy.theValue[0] - inputsRy.minRange) * rangeK + "px";
slider.style.paddingRight = inputsRy.sliderWidth - inputsRy.theValue[1] * rangeK + "px";

var track = document.querySelector(".track");
track.style.width = inputsRy.theValue[1] * rangeK - inputsRy.theValue[0] * rangeK + "px";

var thumbs = document.querySelectorAll(".thumb");
for (var i = 0; i < thumbs.length; i++) {

  thumbs[i].style.width = thumbs[i].style.height = inputsRy.thumbWidth + "px";
  // console.log(inputsRy.thumbWidth + "px");
  thumbs[i].style.borderWidth = inputsRy.thumbBorderWidth + "px";
  thumbs[i].style.top = -(inputsRy.thumbWidth / 2 + inputsRy.thumbBorderWidth - inputsRy.trackHeight / 2) + "px";
  thumbs[i].style.left = (inputsRy.theValue[i] - inputsRy.minRange) * rangeK - (thumbRealWidth / 2)  + "px";

}
var outputs = document.querySelectorAll(".output");
for (var i = 0; i < outputs.length; i++) {
  // console.log(thumbs[i])
  outputs[i].style.width = outputs[i].style.height = outputs[i].style.lineHeight = outputs[i].style.left = inputsRy.outputWidth + "px";
  outputs[i].style.top = -(Math.sqrt(2 * inputsRy.outputWidth * inputsRy.outputWidth) + inputsRy.thumbWidth / 2 - inputsRy.trackHeight / 2) + 10 + "px";
  outputs[i].style.left = (inputsRy.theValue[i] - inputsRy.minRange) * rangeK - inputsRy.outputWidth / 2 + "px";
  if (inputsRy.theValue[i] >=inputsRy.minRange &&  inputsRy.theValue[i] <=inputsRy.minRange + 23)
      {
        inputsRy.theValue[i] = 1;
      }
      else if (inputsRy.theValue[i] >= (inputsRy.minRange + 23)  &&  inputsRy.theValue[i] <= ( inputsRy.minRange + 2*23))
      {
        inputsRy.theValue[i] = 2;
      }
      else if (inputsRy.theValue[i] >= (inputsRy.minRange + 2*23)  &&  inputsRy.theValue[i] <= ( inputsRy.minRange + 3*23))
      {
        inputsRy.theValue[i] = 3;
      }
      else if (inputsRy.theValue[i] >= (inputsRy.minRange + 3*23)  &&  inputsRy.theValue[i] <= ( inputsRy.minRange + 4*23))
      {
        inputsRy.theValue[i] = 4;
      }
      else if (inputsRy.theValue[i] >= (inputsRy.minRange + 4*23)  &&  inputsRy.theValue[i] <= ( inputsRy.minRange + 5*23))
      {
        inputsRy.theValue[i] = 5;
      }
      else if (inputsRy.theValue[i] >= (inputsRy.minRange + 5*23)  &&  inputsRy.theValue[i] <= ( inputsRy.minRange + 6*23))
      {
        inputsRy.theValue[i] = 6;
      }
      else if (inputsRy.theValue[i] >= (inputsRy.minRange + 6*23)  &&  theValue0 <= ( inputsRy.minRange + 7*23))
      {
        inputsRy.theValue[i] = 7;
      }
  outputs[i].innerHTML = "<p>" + inputsRy.theValue[i] + "+</p>";
}

//events

thumbs[0].addEventListener("mousedown", function(evt) {
  isDragging0 = true;
}, false);
thumbs[1].addEventListener("mousedown", function(evt) {
  isDragging1 = true;
}, false);
container.addEventListener("mouseup", function(evt) {
  isDragging0 = false;
  isDragging1 = false;
}, false);
container.addEventListener("mouseout", function(evt) {
  isDragging0 = false;
  isDragging1 = false;
}, false);

container.addEventListener("mousemove", function(evt) {
  var mousePos = oMousePos(this, evt);
  var theValue0 = (isDragging0) ? Math.round(mousePos.x / rangeK) + inputsRy.minRange : inputsRy.theValue[0];
  // console.log(theValue0);
  var theValue1 = (isDragging1) ? Math.round(mousePos.x / rangeK) + inputsRy.minRange : inputsRy.theValue[1];

  if (isDragging0) {

    if (theValue0 < theValue1 - (thumbRealWidth / 2) &&
      theValue0 >= inputsRy.minRange) {
      inputsRy.theValue[0] = theValue0;
      thumbs[0].style.left = (theValue0 - inputsRy.minRange) * rangeK - (thumbRealWidth / 2) + "px";
      outputs[0].style.left = (theValue0 - inputsRy.minRange) * rangeK - inputsRy.outputWidth / 2 + "px";
      if (theValue0 >=inputsRy.minRange &&  theValue0 <=inputsRy.minRange + 23)
      {
        theValue0 = 1;
      }
      else if (theValue0 >= (inputsRy.minRange + 23)  &&  theValue0 <= ( inputsRy.minRange + 2*23))
      {
        theValue0 = 2;
      }
      else if (theValue0 >= (inputsRy.minRange + 2*23)  &&  theValue0 <= ( inputsRy.minRange + 3*23))
      {
        theValue0 = 3;
      }
      else if (theValue0 >= (inputsRy.minRange + 3*23)  &&  theValue0 <= ( inputsRy.minRange + 4*23))
      {
        theValue0 = 4;
      }
      else if (theValue0 >= (inputsRy.minRange + 4*23)  &&  theValue0 <= ( inputsRy.minRange + 5*23))
      {
        theValue0 = 5;
      }
      else if (theValue0 >= (inputsRy.minRange + 5*23)  &&  theValue0 <= ( inputsRy.minRange + 6*23))
      {
        theValue0 = 6;
      }
      else if (theValue0 >= (inputsRy.minRange + 6*23)  &&  theValue0 <= ( inputsRy.minRange + 7*23))
      {
        theValue0 = 7;
      }
      outputs[0].innerHTML = "<p>" + theValue0 + "+</p>";
      slider.style.paddingLeft = (theValue0 - inputsRy.minRange) * rangeK + "px";
      track.style.width = (theValue1 - theValue0) * rangeK + "px";

    }
  } else if (isDragging1) {

    if (theValue1 > theValue0 + (thumbRealWidth / 2) &&
      theValue1 <= inputsRy.maxRange) {
          var i = 0;
      inputsRy.theValue[1] = theValue1;
      thumbs[1].style.left = (theValue1 - inputsRy.minRange) * rangeK - (thumbRealWidth / 2) + "px";
      outputs[1].style.left = (theValue1 - inputsRy.minRange) * rangeK - inputsRy.outputWidth / 2 + "px";
      if (theValue1 >=inputsRy.minRange &&  theValue1 <=inputsRy.minRange + 23)
      {
        i  = 1;
      }
      else if (theValue1 >= (inputsRy.minRange + 23)  &&  theValue1 <= ( inputsRy.minRange + 2*23))
      {
         i  = 2;
      }
      else if (theValue1 >= (inputsRy.minRange + 2*23)  &&  theValue1 <= ( inputsRy.minRange + 3*23))
      {
         i  = 3;
      }
      else if (theValue1 >= (inputsRy.minRange + 3*23)  &&  theValue1 <= ( inputsRy.minRange + 4*23))
      {
         i  = 4;
      }
      else if (theValue1 >= (inputsRy.minRange + 4*23)  &&  theValue1 <= ( inputsRy.minRange + 5*23))
      {
         i  = 5;
      }
      else if (theValue1 >= (inputsRy.minRange + 5*23)  &&  theValue1 <= ( inputsRy.minRange + 6*23))
      {
         i  = 6;
      }
      else if (theValue1 >= (inputsRy.minRange + 6*23)  &&  theValue0 <= ( inputsRy.minRange + 7*23))
      {
         i  = 7;
      }
      outputs[1].innerHTML = "<p>" + i + "+</p>";
      slider.style.paddingRight = (inputsRy.maxRange - theValue1) * rangeK + "px";
      track.style.width = (theValue1 - theValue0) * rangeK + "px";

    }
  }

}, false);

// helpers

function oMousePos(elmt, evt) {
  var ClientRect = elmt.getBoundingClientRect();
  return { //objeto
    x: Math.round(evt.clientX - ClientRect.left),
    y: Math.round(evt.clientY - ClientRect.top)
  }
}

var inputsRy = {
  sliderWidth: 250,
  minRange: +50,
  maxRange: +210, 
  outputWidth:30, // output width
  thumbWidth: 20, // thumb width
  thumbBorderWidth: 5,
  trackHeight: 4,
  theValue: [80, 160] // theValue[0] < theValue[1]
};
var isDragging0 = false;
var isDragging1 = false;

var range = inputsRy.maxRange - inputsRy.minRange;
var rangeK = inputsRy.sliderWidth / range;
var container = document.querySelector("#slider_Container_3");
var thumbRealWidth = inputsRy.thumbWidth + 2 * inputsRy.thumbBorderWidth;

// styles
var slider = document.querySelector(".slider_3");
slider.style.height = inputsRy.trackHeight + "px";
slider.style.width = inputsRy.sliderWidth + "px";
slider.style.paddingLeft = (inputsRy.theValue[0] - inputsRy.minRange) * rangeK + "px";
slider.style.paddingRight = inputsRy.sliderWidth - inputsRy.theValue[1] * rangeK + "px";

var track = document.querySelector(".track_3");
track.style.width = inputsRy.theValue[1] * rangeK - inputsRy.theValue[0] * rangeK + "px";

var thumbs = document.querySelectorAll(".thumb_3");
for (var i = 0; i < thumbs.length; i++) {

  thumbs[i].style.width = thumbs[i].style.height = inputsRy.thumbWidth + "px";
  // console.log(inputsRy.thumbWidth + "px");
  thumbs[i].style.borderWidth = inputsRy.thumbBorderWidth + "px";
  thumbs[i].style.top = -(inputsRy.thumbWidth / 2 + inputsRy.thumbBorderWidth - inputsRy.trackHeight / 2) + "px";
  thumbs[i].style.left = (inputsRy.theValue[i] - inputsRy.minRange) * rangeK - (thumbRealWidth / 2)  + "px";

}
var outputs = document.querySelectorAll(".output_3");
for (var i = 0; i < outputs.length; i++) {
  // console.log(thumbs[i])
  outputs[i].style.width = outputs[i].style.height = outputs[i].style.lineHeight = outputs[i].style.left = inputsRy.outputWidth + "px";
  outputs[i].style.top = -(Math.sqrt(2 * inputsRy.outputWidth * inputsRy.outputWidth) + inputsRy.thumbWidth / 2 - inputsRy.trackHeight / 2) + 10 + "px";
  outputs[i].style.left = (inputsRy.theValue[i] - inputsRy.minRange) * rangeK - inputsRy.outputWidth / 2 + "px";
  if (inputsRy.theValue[i] >=inputsRy.minRange &&  inputsRy.theValue[i] <=inputsRy.minRange + 23)
      {
        inputsRy.theValue[i] = 1960;
      }
      else if (inputsRy.theValue[i] >= (inputsRy.minRange + 23)  &&  inputsRy.theValue[i] <= ( inputsRy.minRange + 2*23))
      {
        inputsRy.theValue[i] = 1970;
      }
      else if (inputsRy.theValue[i] >= (inputsRy.minRange + 2*23)  &&  inputsRy.theValue[i] <= ( inputsRy.minRange + 3*23))
      {
        inputsRy.theValue[i] = 1980;
      }
      else if (inputsRy.theValue[i] >= (inputsRy.minRange + 3*23)  &&  inputsRy.theValue[i] <= ( inputsRy.minRange + 4*23))
      {
        inputsRy.theValue[i] = 1990;
      }
      else if (inputsRy.theValue[i] >= (inputsRy.minRange + 4*23)  &&  inputsRy.theValue[i] <= ( inputsRy.minRange + 5*23))
      {
        inputsRy.theValue[i] = 2000;
      }
      else if (inputsRy.theValue[i] >= (inputsRy.minRange + 5*23)  &&  inputsRy.theValue[i] <= ( inputsRy.minRange + 6*23))
      {
        inputsRy.theValue[i] = 2010;
      }
      else if (inputsRy.theValue[i] >= (inputsRy.minRange + 6*23)  &&  theValue0 <= ( inputsRy.minRange + 7*23))
      {
        inputsRy.theValue[i] = 2020;
      }
  outputs[i].innerHTML = "<p>" + inputsRy.theValue[i] + "</p>";
}

//events

thumbs[0].addEventListener("mousedown", function(evt) {
  isDragging0 = true;
}, false);
thumbs[1].addEventListener("mousedown", function(evt) {
  isDragging1 = true;
}, false);
container.addEventListener("mouseup", function(evt) {
  isDragging0 = false;
  isDragging1 = false;
}, false);
container.addEventListener("mouseout", function(evt) {
  isDragging0 = false;
  isDragging1 = false;
}, false);

container.addEventListener("mousemove", function(evt) {
  var mousePos = oMousePos(this, evt);
  var theValue0 = (isDragging0) ? Math.round(mousePos.x / rangeK) + inputsRy.minRange : inputsRy.theValue[0];
  // console.log(theValue0);
  var theValue1 = (isDragging1) ? Math.round(mousePos.x / rangeK) + inputsRy.minRange : inputsRy.theValue[1];

  if (isDragging0) {

    if (theValue0 < theValue1 - (thumbRealWidth / 2) &&
      theValue0 >= inputsRy.minRange) {
      inputsRy.theValue[0] = theValue0;
      thumbs[0].style.left = (theValue0 - inputsRy.minRange) * rangeK - (thumbRealWidth / 2) + "px";
      outputs[0].style.left = (theValue0 - inputsRy.minRange) * rangeK - inputsRy.outputWidth / 2 + "px";
      if (theValue0 >=inputsRy.minRange &&  theValue0 <=inputsRy.minRange + 23)
      {
        theValue0 = 1960;
      }
      else if (theValue0 >= (inputsRy.minRange + 23)  &&  theValue0 <= ( inputsRy.minRange + 2*23))
      {
        theValue0 = 1970;
      }
      else if (theValue0 >= (inputsRy.minRange + 2*23)  &&  theValue0 <= ( inputsRy.minRange + 3*23))
      {
        theValue0 = 1980;
      }
      else if (theValue0 >= (inputsRy.minRange + 3*23)  &&  theValue0 <= ( inputsRy.minRange + 4*23))
      {
        theValue0 = 1990;
      }
      else if (theValue0 >= (inputsRy.minRange + 4*23)  &&  theValue0 <= ( inputsRy.minRange + 5*23))
      {
        theValue0 = 2000;
      }
      else if (theValue0 >= (inputsRy.minRange + 5*23)  &&  theValue0 <= ( inputsRy.minRange + 6*23))
      {
        theValue0 = 2010;
      }
      else if (theValue0 >= (inputsRy.minRange + 6*23)  &&  theValue0 <= ( inputsRy.minRange + 7*23))
      {
        theValue0 = 2020;
      }
      outputs[0].innerHTML = "<p>" + theValue0 + "</p>";
      slider.style.paddingLeft = (theValue0 - inputsRy.minRange) * rangeK + "px";
      track.style.width = (theValue1 - theValue0) * rangeK + "px";

    }
  } else if (isDragging1) {

    if (theValue1 > theValue0 + (thumbRealWidth / 2) &&
      theValue1 <= inputsRy.maxRange) {
          var i = 0;
      inputsRy.theValue[1] = theValue1;
      thumbs[1].style.left = (theValue1 - inputsRy.minRange) * rangeK - (thumbRealWidth / 2) + "px";
      outputs[1].style.left = (theValue1 - inputsRy.minRange) * rangeK - inputsRy.outputWidth / 2 + "px";
      if (theValue1 >=inputsRy.minRange &&  theValue1 <=inputsRy.minRange + 23)
      {
        i  = 1960;
      }
      else if (theValue1 >= (inputsRy.minRange + 23)  &&  theValue1 <= ( inputsRy.minRange + 2*23))
      {
         i  = 1970;
      }
      else if (theValue1 >= (inputsRy.minRange + 2*23)  &&  theValue1 <= ( inputsRy.minRange + 3*23))
      {
         i  = 1980;
      }
      else if (theValue1 >= (inputsRy.minRange + 3*23)  &&  theValue1 <= ( inputsRy.minRange + 4*23))
      {
         i  = 1990;
      }
      else if (theValue1 >= (inputsRy.minRange + 4*23)  &&  theValue1 <= ( inputsRy.minRange + 5*23))
      {
         i  = 2000;
      }
      else if (theValue1 >= (inputsRy.minRange + 5*23)  &&  theValue1 <= ( inputsRy.minRange + 6*23))
      {
         i  = 2010;
      }
      else if (theValue1 >= (inputsRy.minRange + 6*23)  &&  theValue0 <= ( inputsRy.minRange + 7*23))
      {
         i  = 2020;
      }
      outputs[1].innerHTML = "<p>" + i + "</p>";
      slider.style.paddingRight = (inputsRy.maxRange - theValue1) * rangeK + "px";
      track.style.width = (theValue1 - theValue0) * rangeK + "px";

    }
  }

}, false);

// helpers

function oMousePos(elmt, evt) {
  var ClientRect = elmt.getBoundingClientRect();
  return { //objeto
    x: Math.round(evt.clientX - ClientRect.left),
    y: Math.round(evt.clientY - ClientRect.top)
  }
}

var inputsRy = {
  sliderWidth: 250,
  minRange: +50,
  maxRange: +210, 
  outputWidth:30, // output width
  thumbWidth: 20, // thumb width
  thumbBorderWidth: 5,
  trackHeight: 4,
  theValue: [80, 160] // theValue[0] < theValue[1]
};
var isDragging0 = false;
var isDragging1 = false;

var range = inputsRy.maxRange - inputsRy.minRange;
var rangeK = inputsRy.sliderWidth / range;
var container = document.querySelector("#slider_Container_2");
var thumbRealWidth = inputsRy.thumbWidth + 2 * inputsRy.thumbBorderWidth;

// styles
var slider = document.querySelector(".slider_2");
slider.style.height = inputsRy.trackHeight + "px";
slider.style.width = inputsRy.sliderWidth + "px";
slider.style.paddingLeft = (inputsRy.theValue[0] - inputsRy.minRange) * rangeK + "px";
slider.style.paddingRight = inputsRy.sliderWidth - inputsRy.theValue[1] * rangeK + "px";

var track = document.querySelector(".track_2");
track.style.width = inputsRy.theValue[1] * rangeK - inputsRy.theValue[0] * rangeK + "px";

var thumbs = document.querySelectorAll(".thumb_2");
for (var i = 0; i < thumbs.length; i++) {

  thumbs[i].style.width = thumbs[i].style.height = inputsRy.thumbWidth + "px";
  // console.log(inputsRy.thumbWidth + "px");
  thumbs[i].style.borderWidth = inputsRy.thumbBorderWidth + "px";
  thumbs[i].style.top = -(inputsRy.thumbWidth / 2 + inputsRy.thumbBorderWidth - inputsRy.trackHeight / 2) + "px";
  thumbs[i].style.left = (inputsRy.theValue[i] - inputsRy.minRange) * rangeK - (thumbRealWidth / 2)  + "px";

}
var outputs = document.querySelectorAll(".output_2");
for (var i = 0; i < outputs.length; i++) {
  // console.log(thumbs[i])
  outputs[i].style.width = outputs[i].style.height = outputs[i].style.lineHeight = outputs[i].style.left = inputsRy.outputWidth + "px";
  outputs[i].style.top = -(Math.sqrt(2 * inputsRy.outputWidth * inputsRy.outputWidth) + inputsRy.thumbWidth / 2 - inputsRy.trackHeight / 2) + 10 + "px";
  outputs[i].style.left = (inputsRy.theValue[i] - inputsRy.minRange) * rangeK - inputsRy.outputWidth / 2 + "px";
  if (inputsRy.theValue[i] >=inputsRy.minRange &&  inputsRy.theValue[i] <=inputsRy.minRange + 23)
      {
        inputsRy.theValue[i] = 1;
      }
      else if (inputsRy.theValue[i] >= (inputsRy.minRange + 23)  &&  inputsRy.theValue[i] <= ( inputsRy.minRange + 2*23))
      {
        inputsRy.theValue[i] = 2;
      }
      else if (inputsRy.theValue[i] >= (inputsRy.minRange + 2*23)  &&  inputsRy.theValue[i] <= ( inputsRy.minRange + 3*23))
      {
        inputsRy.theValue[i] = 3;
      }
      else if (inputsRy.theValue[i] >= (inputsRy.minRange + 3*23)  &&  inputsRy.theValue[i] <= ( inputsRy.minRange + 4*23))
      {
        inputsRy.theValue[i] = 4;
      }
      else if (inputsRy.theValue[i] >= (inputsRy.minRange + 4*23)  &&  inputsRy.theValue[i] <= ( inputsRy.minRange + 5*23))
      {
        inputsRy.theValue[i] = 5;
      }
      else if (inputsRy.theValue[i] >= (inputsRy.minRange + 5*23)  &&  inputsRy.theValue[i] <= ( inputsRy.minRange + 6*23))
      {
        inputsRy.theValue[i] = 6;
      }
      else if (inputsRy.theValue[i] >= (inputsRy.minRange + 6*23)  &&  theValue0 <= ( inputsRy.minRange + 7*23))
      {
        inputsRy.theValue[i] = 7;
      }
  outputs[i].innerHTML = "<p>" + inputsRy.theValue[i] + "+</p>";
}

//events

thumbs[0].addEventListener("mousedown", function(evt) {
  isDragging0 = true;
}, false);
thumbs[1].addEventListener("mousedown", function(evt) {
  isDragging1 = true;
}, false);
container.addEventListener("mouseup", function(evt) {
  isDragging0 = false;
  isDragging1 = false;
}, false);
container.addEventListener("mouseout", function(evt) {
  isDragging0 = false;
  isDragging1 = false;
}, false);

container.addEventListener("mousemove", function(evt) {
  var mousePos = oMousePos(this, evt);
  var theValue0 = (isDragging0) ? Math.round(mousePos.x / rangeK) + inputsRy.minRange : inputsRy.theValue[0];
  // console.log(theValue0);
  var theValue1 = (isDragging1) ? Math.round(mousePos.x / rangeK) + inputsRy.minRange : inputsRy.theValue[1];

  if (isDragging0) {

    if (theValue0 < theValue1 - (thumbRealWidth / 2) &&
      theValue0 >= inputsRy.minRange) {
      inputsRy.theValue[0] = theValue0;
      thumbs[0].style.left = (theValue0 - inputsRy.minRange) * rangeK - (thumbRealWidth / 2) + "px";
      outputs[0].style.left = (theValue0 - inputsRy.minRange) * rangeK - inputsRy.outputWidth / 2 + "px";
      if (theValue0 >=inputsRy.minRange &&  theValue0 <=inputsRy.minRange + 23)
      {
        theValue0 = 1;
      }
      else if (theValue0 >= (inputsRy.minRange + 23)  &&  theValue0 <= ( inputsRy.minRange + 2*23))
      {
        theValue0 = 2;
      }
      else if (theValue0 >= (inputsRy.minRange + 2*23)  &&  theValue0 <= ( inputsRy.minRange + 3*23))
      {
        theValue0 = 3;
      }
      else if (theValue0 >= (inputsRy.minRange + 3*23)  &&  theValue0 <= ( inputsRy.minRange + 4*23))
      {
        theValue0 = 4;
      }
      else if (theValue0 >= (inputsRy.minRange + 4*23)  &&  theValue0 <= ( inputsRy.minRange + 5*23))
      {
        theValue0 = 5;
      }
      else if (theValue0 >= (inputsRy.minRange + 5*23)  &&  theValue0 <= ( inputsRy.minRange + 6*23))
      {
        theValue0 = 6;
      }
      else if (theValue0 >= (inputsRy.minRange + 6*23)  &&  theValue0 <= ( inputsRy.minRange + 7*23))
      {
        theValue0 = 7;
      }
      outputs[0].innerHTML = "<p>" + theValue0 + "+</p>";
      slider.style.paddingLeft = (theValue0 - inputsRy.minRange) * rangeK + "px";
      track.style.width = (theValue1 - theValue0) * rangeK + "px";

    }
  } else if (isDragging1) {

    if (theValue1 > theValue0 + (thumbRealWidth / 2) &&
      theValue1 <= inputsRy.maxRange) {
          var i = 0;
      inputsRy.theValue[1] = theValue1;
      thumbs[1].style.left = (theValue1 - inputsRy.minRange) * rangeK - (thumbRealWidth / 2) + "px";
      outputs[1].style.left = (theValue1 - inputsRy.minRange) * rangeK - inputsRy.outputWidth / 2 + "px";
      if (theValue1 >=inputsRy.minRange &&  theValue1 <=inputsRy.minRange + 23)
      {
        i  = 1;
      }
      else if (theValue1 >= (inputsRy.minRange + 23)  &&  theValue1 <= ( inputsRy.minRange + 2*23))
      {
         i  = 2;
      }
      else if (theValue1 >= (inputsRy.minRange + 2*23)  &&  theValue1 <= ( inputsRy.minRange + 3*23))
      {
         i  = 3;
      }
      else if (theValue1 >= (inputsRy.minRange + 3*23)  &&  theValue1 <= ( inputsRy.minRange + 4*23))
      {
         i  = 4;
      }
      else if (theValue1 >= (inputsRy.minRange + 4*23)  &&  theValue1 <= ( inputsRy.minRange + 5*23))
      {
         i  = 5;
      }
      else if (theValue1 >= (inputsRy.minRange + 5*23)  &&  theValue1 <= ( inputsRy.minRange + 6*23))
      {
         i  = 6;
      }
      else if (theValue1 >= (inputsRy.minRange + 6*23)  &&  theValue0 <= ( inputsRy.minRange + 7*23))
      {
         i  = 7;
      }
      outputs[1].innerHTML = "<p>" + i + "+</p>";
      slider.style.paddingRight = (inputsRy.maxRange - theValue1) * rangeK + "px";
      track.style.width = (theValue1 - theValue0) * rangeK + "px";

    }
  }

}, false);

// helpers

function oMousePos(elmt, evt) {
  var ClientRect = elmt.getBoundingClientRect();
  return { //objeto
    x: Math.round(evt.clientX - ClientRect.left),
    y: Math.round(evt.clientY - ClientRect.top)
  }
}

var inputsRy = {
  sliderWidth: 250,
  minRange: +50,
  maxRange: +210, 
  outputWidth:30, // output width
  thumbWidth: 20, // thumb width
  thumbBorderWidth: 5,
  trackHeight: 4,
  theValue: [80, 160] // theValue[0] < theValue[1]
};
var isDragging0 = false;
var isDragging1 = false;

var range = inputsRy.maxRange - inputsRy.minRange;
var rangeK = inputsRy.sliderWidth / range;
var container = document.querySelector(".container");
var thumbRealWidth = inputsRy.thumbWidth + 2 * inputsRy.thumbBorderWidth;

// styles
var slider = document.querySelector(".slider");
slider.style.height = inputsRy.trackHeight + "px";
slider.style.width = inputsRy.sliderWidth + "px";
slider.style.paddingLeft = (inputsRy.theValue[0] - inputsRy.minRange) * rangeK + "px";
slider.style.paddingRight = inputsRy.sliderWidth - inputsRy.theValue[1] * rangeK + "px";

var track = document.querySelector(".track");
track.style.width = inputsRy.theValue[1] * rangeK - inputsRy.theValue[0] * rangeK + "px";

var thumbs = document.querySelectorAll(".thumb");
for (var i = 0; i < thumbs.length; i++) {

  thumbs[i].style.width = thumbs[i].style.height = inputsRy.thumbWidth + "px";
  // console.log(inputsRy.thumbWidth + "px");
  thumbs[i].style.borderWidth = inputsRy.thumbBorderWidth + "px";
  thumbs[i].style.top = -(inputsRy.thumbWidth / 2 + inputsRy.thumbBorderWidth - inputsRy.trackHeight / 2) + "px";
  thumbs[i].style.left = (inputsRy.theValue[i] - inputsRy.minRange) * rangeK - (thumbRealWidth / 2)  + "px";

}
var outputs = document.querySelectorAll(".output");
for (var i = 0; i < outputs.length; i++) {
  // console.log(thumbs[i])
  outputs[i].style.width = outputs[i].style.height = outputs[i].style.lineHeight = outputs[i].style.left = inputsRy.outputWidth + "px";
  outputs[i].style.top = -(Math.sqrt(2 * inputsRy.outputWidth * inputsRy.outputWidth) + inputsRy.thumbWidth / 2 - inputsRy.trackHeight / 2) + 10 + "px";
  outputs[i].style.left = (inputsRy.theValue[i] - inputsRy.minRange) * rangeK - inputsRy.outputWidth / 2 + "px";
  if (inputsRy.theValue[i] >=inputsRy.minRange &&  inputsRy.theValue[i] <=inputsRy.minRange + 23)
      {
        inputsRy.theValue[i] = 1;
      }
      else if (inputsRy.theValue[i] >= (inputsRy.minRange + 23)  &&  inputsRy.theValue[i] <= ( inputsRy.minRange + 2*23))
      {
        inputsRy.theValue[i] = 2;
      }
      else if (inputsRy.theValue[i] >= (inputsRy.minRange + 2*23)  &&  inputsRy.theValue[i] <= ( inputsRy.minRange + 3*23))
      {
        inputsRy.theValue[i] = 3;
      }
      else if (inputsRy.theValue[i] >= (inputsRy.minRange + 3*23)  &&  inputsRy.theValue[i] <= ( inputsRy.minRange + 4*23))
      {
        inputsRy.theValue[i] = 4;
      }
      else if (inputsRy.theValue[i] >= (inputsRy.minRange + 4*23)  &&  inputsRy.theValue[i] <= ( inputsRy.minRange + 5*23))
      {
        inputsRy.theValue[i] = 5;
      }
      else if (inputsRy.theValue[i] >= (inputsRy.minRange + 5*23)  &&  inputsRy.theValue[i] <= ( inputsRy.minRange + 6*23))
      {
        inputsRy.theValue[i] = 6;
      }
      else if (inputsRy.theValue[i] >= (inputsRy.minRange + 6*23)  &&  theValue0 <= ( inputsRy.minRange + 7*23))
      {
        inputsRy.theValue[i] = 7;
      }
  outputs[i].innerHTML = "<p>" + inputsRy.theValue[i] + "+</p>";
}

//events

thumbs[0].addEventListener("mousedown", function(evt) {
  isDragging0 = true;
}, false);
thumbs[1].addEventListener("mousedown", function(evt) {
  isDragging1 = true;
}, false);
container.addEventListener("mouseup", function(evt) {
  isDragging0 = false;
  isDragging1 = false;
}, false);
container.addEventListener("mouseout", function(evt) {
  isDragging0 = false;
  isDragging1 = false;
}, false);

container.addEventListener("mousemove", function(evt) {
  var mousePos = oMousePos(this, evt);
  var theValue0 = (isDragging0) ? Math.round(mousePos.x / rangeK) + inputsRy.minRange : inputsRy.theValue[0];
  // console.log(theValue0);
  var theValue1 = (isDragging1) ? Math.round(mousePos.x / rangeK) + inputsRy.minRange : inputsRy.theValue[1];

  if (isDragging0) {

    if (theValue0 < theValue1 - (thumbRealWidth / 2) &&
      theValue0 >= inputsRy.minRange) {
      inputsRy.theValue[0] = theValue0;
      thumbs[0].style.left = (theValue0 - inputsRy.minRange) * rangeK - (thumbRealWidth / 2) + "px";
      outputs[0].style.left = (theValue0 - inputsRy.minRange) * rangeK - inputsRy.outputWidth / 2 + "px";
      if (theValue0 >=inputsRy.minRange &&  theValue0 <=inputsRy.minRange + 23)
      {
        theValue0 = 1;
      }
      else if (theValue0 >= (inputsRy.minRange + 23)  &&  theValue0 <= ( inputsRy.minRange + 2*23))
      {
        theValue0 = 2;
      }
      else if (theValue0 >= (inputsRy.minRange + 2*23)  &&  theValue0 <= ( inputsRy.minRange + 3*23))
      {
        theValue0 = 3;
      }
      else if (theValue0 >= (inputsRy.minRange + 3*23)  &&  theValue0 <= ( inputsRy.minRange + 4*23))
      {
        theValue0 = 4;
      }
      else if (theValue0 >= (inputsRy.minRange + 4*23)  &&  theValue0 <= ( inputsRy.minRange + 5*23))
      {
        theValue0 = 5;
      }
      else if (theValue0 >= (inputsRy.minRange + 5*23)  &&  theValue0 <= ( inputsRy.minRange + 6*23))
      {
        theValue0 = 6;
      }
      else if (theValue0 >= (inputsRy.minRange + 6*23)  &&  theValue0 <= ( inputsRy.minRange + 7*23))
      {
        theValue0 = 7;
      }
      outputs[0].innerHTML = "<p>" + theValue0 + "+</p>";
      slider.style.paddingLeft = (theValue0 - inputsRy.minRange) * rangeK + "px";
      track.style.width = (theValue1 - theValue0) * rangeK + "px";

    }
  } else if (isDragging1) {

    if (theValue1 > theValue0 + (thumbRealWidth / 2) &&
      theValue1 <= inputsRy.maxRange) {
          var i = 0;
      inputsRy.theValue[1] = theValue1;
      thumbs[1].style.left = (theValue1 - inputsRy.minRange) * rangeK - (thumbRealWidth / 2) + "px";
      outputs[1].style.left = (theValue1 - inputsRy.minRange) * rangeK - inputsRy.outputWidth / 2 + "px";
      if (theValue1 >=inputsRy.minRange &&  theValue1 <=inputsRy.minRange + 23)
      {
        i  = 1;
      }
      else if (theValue1 >= (inputsRy.minRange + 23)  &&  theValue1 <= ( inputsRy.minRange + 2*23))
      {
         i  = 2;
      }
      else if (theValue1 >= (inputsRy.minRange + 2*23)  &&  theValue1 <= ( inputsRy.minRange + 3*23))
      {
         i  = 3;
      }
      else if (theValue1 >= (inputsRy.minRange + 3*23)  &&  theValue1 <= ( inputsRy.minRange + 4*23))
      {
         i  = 4;
      }
      else if (theValue1 >= (inputsRy.minRange + 4*23)  &&  theValue1 <= ( inputsRy.minRange + 5*23))
      {
         i  = 5;
      }
      else if (theValue1 >= (inputsRy.minRange + 5*23)  &&  theValue1 <= ( inputsRy.minRange + 6*23))
      {
         i  = 6;
      }
      else if (theValue1 >= (inputsRy.minRange + 6*23)  &&  theValue0 <= ( inputsRy.minRange + 7*23))
      {
         i  = 7;
      }
      outputs[1].innerHTML = "<p>" + i + "+</p>";
      slider.style.paddingRight = (inputsRy.maxRange - theValue1) * rangeK + "px";
      track.style.width = (theValue1 - theValue0) * rangeK + "px";

    }
  }

}, false);

// helpers

function oMousePos(elmt, evt) {
  var ClientRect = elmt.getBoundingClientRect();
  return { //objeto
    x: Math.round(evt.clientX - ClientRect.left),
    y: Math.round(evt.clientY - ClientRect.top)
  }
}
