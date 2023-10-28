function invisible_element(id_element) {
  document.getElementById(id_element).classList.remove("d-block");
  document.getElementById(id_element).classList.add("d-none");
}

function welcome_message() {
  document.getElementById("gp_reflection").style.display = "none";
  document.getElementById("ask").style.display = "inline";
  document.getElementById("question").value = "";
  document.getElementById("word_of_welcome").style.display = "inline";
}

function reflection_message() {
  document.getElementById("word_of_welcome").style.display = "none";
  document.getElementById("comprehension").style.display = "none";
  document.getElementById("gp_reply1").style.display = "none";
  document.getElementById("gp_reply2").style.display = "none";
  document.getElementById("gp_reply3").style.display = "none";
  document.getElementById("gp_reply4").style.display = "none";
  document.getElementById("gp_reply5").style.display = "none";
  document.getElementById("gp_reply6").style.display = "none";
  document.getElementById("gp_reply7").style.display = "none";
  document.getElementById("ask").style.display = "none";
  document.getElementById("gp_reflection").style.display = "inline";
}

function message_of_meanness() {
  document.getElementById("gp_reflection").style.display = "none";
  document.getElementById("gp_reply1").style.display = "none";
  document.getElementById("gp_reply2").style.display = "none";
  document.getElementById("comprehension").style.display = "none";
  document.getElementById("question").value = "";
  document.getElementById("ask").style.display = "inline";
  document.getElementById("gp_reply2").style.display = "inline";
}

function rude_message() {
  document.getElementById("gp_reflection").style.display = "none";
  document.getElementById("gp_reply1").style.display = "none";
  document.getElementById("gp_reply2").style.display = "none";
  document.getElementById("comprehension").style.display = "none";
  document.getElementById("question").value = "";
  document.getElementById("ask").style.display = "inline";
  document.getElementById("gp_reply1").style.display = "inline";
}

function response_quotas_reached() {
  document.getElementById("gp_reflection").style.display = "none";
  document.getElementById("gp_reply1").style.display = "none";
  document.getElementById("gp_reply2").style.display = "none";
  document.getElementById("gp_reply3").style.display = "none";
  document.getElementById("gp_reply4").style.display = "none";
  document.getElementById("gp_reply5").style.display = "none";
  document.getElementById("gp_reply6").style.display = "none";
  document.getElementById("gp_reply7").style.display = "none";
  document.getElementById("ask").style.display = "none";
  document.getElementById("quotas").style.display = "inline";
}

function random_grandpy_answer() {
  const list_answers = [
    "gp_reply3",
    "gp_reply4",
    "gp_reply5",
    "gp_reply6",
    "gp_reply7",
  ];
  var random_choice = Math.floor(Math.random() * list_answers.length);
  document.getElementById("gp_reflection").style.display = "none";
  document.getElementById("word_of_welcome").style.display = "none";
  document.getElementById("comprehension").style.display = "none";
  document.getElementById("gp_reply1").style.display = "none";
  document.getElementById("gp_reply2").style.display = "none";
  document.getElementById("gp_reply3").style.display = "none";
  document.getElementById("gp_reply4").style.display = "none";
  document.getElementById("gp_reply5").style.display = "none";
  document.getElementById("gp_reply6").style.display = "none";
  document.getElementById("gp_reply7").style.display = "none";
  document.getElementById(list_answers[random_choice]).style.display = "inline";
  document.getElementById("ask").style.display = "none";
  document.getElementById("answer").style.display = "inline";
  document.getElementById("other").style.display = "inline";
}

function incomprehension_message() {
  document.getElementById("gp_reflection").style.display = "none";
  document.getElementById("comprehension").style.display = "none";
  document.getElementById("gp_reply1").style.display = "none";
  document.getElementById("gp_reply2").style.display = "none";
  document.getElementById("gp_reply3").style.display = "none";
  document.getElementById("gp_reply4").style.display = "none";
  document.getElementById("gp_reply5").style.display = "none";
  document.getElementById("gp_reply6").style.display = "none";
  document.getElementById("gp_reply7").style.display = "none";
  document.getElementById("question").value = "";
  document.getElementById("ask").style.display = "inline";
  document.getElementById("comprehension").style.display = "inline";
}

function beginning_of_fatigue() {
  document.getElementById("gp_reflection").style.display = "none";
  document.getElementById("overstrain").style.display = "inline";
  document.getElementById("ask").style.display = "none";
  document.getElementById("answer").style.display = "inline";
  document.getElementById("other").style.display = "inline";
}

function wikipedia_response_display(code_grandpy) {
  var wiki_display = code_grandpy.history;
  document.getElementById("history").innerHTML = wiki_display;
}

function googleMap_static_response_display(code_grandpy) {
  var static_map_display = code_grandpy.map;
  document.getElementById("map").src =
    "data:image/png;base64," + static_map_display;
}

function apis_response_display(code_grandpy) {
  document.getElementById("address").textContent =
    "la réponse a la question : " + code_grandpy.address + " ?";
  wikipedia_response_display(code_grandpy);
  googleMap_static_response_display(code_grandpy);
}

function answer_gp(code_grandpy) {
  switch (code_grandpy.grandpy_status_code) {
    case "benevolent":
      welcome_message();
      break;
    case "tired":
      beginning_of_fatigue();
      apis_response_display(code_grandpy);
      break;
    case "mannerless":
      rude_message();
      break;
    case "disrespectful":
      message_of_meanness();
      break;
    case "incomprehension":
      incomprehension_message();
      break;
    case "response":
      random_grandpy_answer();
      apis_response_display(code_grandpy);
      break;
    case "exhausted":
      response_quotas_reached();
  }
}

const send_request = document.getElementById("submit2");
send_request.addEventListener("submit", function (e) {
  reflection_message();
  fetch("/index/2/" + document.getElementById("question").value)
    .then(function (res) {
      if (res.ok) {
        return res.json();
      }
    })
    .then(function (value) {
      answer_gp(value);
    })
    .catch(function (err) {
      console.log("Une erreur est levé");
      console.log(err);
    });
  e.preventDefault();
});
