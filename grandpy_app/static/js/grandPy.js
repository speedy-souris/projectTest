// function that deactivates the display of the HTML element
function invisible_element(id_element) {
  document.getElementById(id_element).classList.remove("d-block");
  document.getElementById(id_element).classList.add("d-none");
}

// function that reactivates the display of the HTML element
function visible_element(id_element) {
  document.getElementById(id_element).classList.remove("d-none");
  document.getElementById(id_element).classList.add("d-block");
}

//~ // function that displays the welcome message
function welcome_message() {
  invisible_element("gp_reflection");
  visible_element("ask");
  document.getElementById("question").value = "";
  visible_element("word_of_welcome");
}

// function that displays grandPy thinking
function reflection_message() {
  invisible_element("gp_reply3");
  invisible_element("gp_reply4");
  invisible_element("gp_reply5");
  invisible_element("gp_reply6");
  invisible_element("gp_reply7");
  invisible_element("ask");
  visible_element("gp_reflection");
}

// function that displays grandPy's response to meanness
function message_of_meanness() {
  invisible_element("gp_reflection");
  invisible_element("gp_reply1");
  invisible_element("gp_reply2");
  invisible_element("comprehension");
  document.getElementById("question").value = "";
  visible_element("ask");
  visible_element("gp_reply2");
}

//~ //  function that displays grandPy's response to rudeness
function rude_message() {
  invisible_element("gp_reflection");
  invisible_element("gp_reply1");
  invisible_element("gp_reply2");
  invisible_element("comprehension");
  document.getElementById("question").value = "";
  visible_element("ask");
  visible_element("gp_reply1");
}

/* additional option for project 13
 * function that displays grandPy's answer to the tenth question
*/
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

//  function that displays a random response from grandPy 
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
  invisible_element("gp_reply1");
  invisible_element("gp_reply2");
  invisible_element("gp_reply3");
  invisible_element("gp_reply4");
  invisible_element("gp_reply5");
  invisible_element("gp_reply6");
  invisible_element("gp_reply7");
  invisible_element("character_description")
  visible_element(list_answers[random_choice]);
  invisible_element("ask");
  visible_element("answer");
  visible_element("other");
}

// function that displays a response from grandPy about not understanding the question
function incomprehension_message() {
  //~ invisible_element("gp_reflection");
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

/* additional option for project 13
 * function that displays a response from grandPy who is tired
*/
function beginning_of_fatigue() {
  invisible_element("gp_reflection");
  visible_element("overstrain");
  invisible_element("ask");
  visible_element("answer");
  visible_element("other");
}

// function that displays the result of the wikipedia API
function wikipedia_response_display(code_grandpy) {
  var wiki_display = code_grandpy.history;
  document.getElementById("history").innerHTML = wiki_display;
}

// function that displays the static map from the googleMap API
function googleMap_static_response_display(code_grandpy) {
  var static_map_display = code_grandpy.map;
  document.getElementById("map").src =
    "data:image/png;base64," + static_map_display;
}

// function that displays all results from all googleMap and wikepedia APIs
function apis_response_display(code_grandpy) {
  document.getElementById("address").textContent =
    "la réponse a la question : " + code_grandpy.address + " ?";
  wikipedia_response_display(code_grandpy);
  googleMap_static_response_display(code_grandpy);
}

/* additional option for project 13
 * function that displays responses according to GrandPy status
 */
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

// function linking server and client (flask)
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
