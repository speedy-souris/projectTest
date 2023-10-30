function invisible_element(id_element) {
  document.getElementById(id_element).classList.remove("d-block");
  document.getElementById(id_element).classList.add("d-none");
}

function visible_element(id_element) {
  document.getElementById(id_element).classList.remove("d-none");
  document.getElementById(id_element).classList.add("d-block");
}

function welcome_message() {
  invisible_element("gp_reflection");
  visible_element("ask");
  document.getElementById("question").value = "";
  visible_element("word_of_welcome");
}

function reflection_message() {
  invisible_element("comprehension");
  invisible_element("gp_reply1");
  invisible_element("gp_reply2");
  invisible_element("gp_reply3");
  invisible_element("gp_reply4");
  invisible_element("gp_reply5");
  invisible_element("gp_reply6");
  invisible_element("gp_reply7");
  invisible_element("ask");
  visible_element("gp_reflection");
}

function message_of_meanness() {
  invisible_element("gp_reflection");
  invisible_element("gp_reply1");
  invisible_element("gp_reply2");
  invisible_element("comprehension");
  document.getElementById("question").value = "";
  visible_element("ask");
  visible_element("gp_reply2");
}

function rude_message() {
  invisible_element("gp_reflection");
  invisible_element("gp_reply1");
  invisible_element("gp_reply2");
  invisible_element("comprehension");
  document.getElementById("question").value = "";
  visible_element("ask");
  visible_element("gp_reply1");
}

function response_quotas_reached() {
  invisible_element("gp_reflection");
  invisible_element("gp_reply1");
  invisible_element("gp_reply2");
  invisible_element("gp_reply3");
  invisible_element("gp_reply4");
  invisible_element("gp_reply5");
  invisible_element("gp_reply6");
  invisible_element("gp_reply7");
  invisible_element("ask");
  visible_element("quotas");
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
  invisible_element("gp_reflection");
  invisible_element("word_of_welcome");
  invisible_element("comprehension");
  invisible_element("gp_reply1");
  invisible_element("gp_reply2");
  invisible_element("gp_reply3");
  invisible_element("gp_reply4");
  invisible_element("gp_reply5");
  invisible_element("gp_reply6");
  invisible_element("gp_reply7");
  visible_element(list_answers[random_choice]);
  invisible_element("ask");
  visible_element("answer");
  visible_element("other");
}

function incomprehension_message() {
  invisible_element("gp_reflection");
  invisible_element("comprehension");
  invisible_element("gp_reply1");
  invisible_element("gp_reply2");
  invisible_element("gp_reply3");
  invisible_element("gp_reply4");
  invisible_element("gp_reply5");
  invisible_element("gp_reply6");
  invisible_element("gp_reply7");
  document.getElementById("question").value = "";
  visible_element("ask");
  visible_element("comprehension");
}

function beginning_of_fatigue() {
  invisible_element("gp_reflection");
  visible_element("overstrain");
  invisible_element("ask");
  visible_element("answer");
  visible_element("other");
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
