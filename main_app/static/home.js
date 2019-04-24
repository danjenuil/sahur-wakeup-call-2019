$(document).ready(function() {
  $("#subscribeForm").on("submit", function(event) {
    event.preventDefault();
    let formData = {
      'name' : $('input[name=name]').val(),
      'email': $('input[name=email]').val(),
      'phone': $('input[name=phone]').val()
    };
    $.ajax({
      url: "/subscribe",
      method: "POST",
      data: formData,
      dataType: "json",
      success: function(response) {
        if ((response[0]['message'] == "OTP code has been sent") || (response[0]['message'] == "Pending confirmation")) {
          $("#otpform").prepend(`<input id='phoneNumberOtp' type='hidden' value='${$('input[name=phone]').val()}'>`);
          $("#otpPhoneNumber").append(`${$('input[name=name]').val()}`);
          $(".modal").addClass("is-active");
        } else {
          alert(response[0]['message']);
        }
      }
    });
  });

  $("#otpform").on("submit", function(event) {
    event.preventDefault();
    let formData = {
      'phone' : $("#phoneNumberOtp").val(),
      'otp' : $("#otpInput").val()
    };
    $.ajax({
      url: "/checkotp",
      method: "POST",
      data: formData,
      dataType: "json",
      success: function(response) {
        if (response[0]['message'] == "Valid OTP") {
          $(".modal-close").click();
          alert("You have succesfully subscribed to our wakeup call service!");
        } else {
          alert("Invalid OTP!");
        }
      }
    })
  });

  $(".modal-close").on("click", function(event) {
    $(".modal").removeClass("is-active");
    $("#otpPhoneNumber").empty();
    $("#phoneNumberOtp").detach();
  })
});


