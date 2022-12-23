function welcome_message(){
    document.getElementById("word_of_welcome").style.display = 'inline'};

function reflection_message(){
    document.getElementById("ask").style.display = 'none';
    document.getElementById("gp_reflection").style.display = 'inline'}; 

function message_of_meanness(){
    document.getElementById("gp_reply2").style.display = 'inline'};

function rude_message(){
    document.getElementById("gp_reply1").style.display = 'inline'};

function response_quotas_reached(){
    document.getElementById("ask").style.display = 'none';
    document.getElementById('quotas').style.display = 'inline'};
 
function random_grandpy_answer(){
    var list_answers = ['gp_reply3', 'gp_reply4', 'gp_reply5', 'gp_reply6', 'gp_reply7'];
    var random_choice = Math.floor(Math.random()*list_answers.length);
    document.getElementById(list_answers[random_choice]).style.display = 'inline'; 
    document.getElementById("ask").style.display = 'none';
    document.getElementById('answer').style.display = 'inline'
    document.getElementById('other').style.display = 'inline'};

function incomprehension_message(){
    document.getElementById('comprehension').style.display = 'inline'};

function beginning_of_fatigue(){
    document.getElementById('overstrain').style.display = 'inline';
    document.getElementById("ask").style.display = 'none';
    document.getElementById('answer').style.display = 'inline':
    document.getElementById('other').style.display = 'inline'}:

//document.getElementById("question").text = "";
//document.getElementById("answer").style.display = 'none';
//document.getElementById("other").style.display = 'none';
