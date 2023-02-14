function welcome_message(){
    console.log("je suis ici")
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
    const list_answers = ['gp_reply3', 'gp_reply4', 'gp_reply5', 'gp_reply6', 'gp_reply7'];
    var random_choice = Math.floor(Math.random()*list_answers.length);
    document.getElementById('gp_reply3').style.display = 'none';
    document.getElementById('gp_reply4').style.display = 'none';
    document.getElementById('gp_reply5').style.display = 'none';
    document.getElementById('gp_reply6').style.display = 'none';
    document.getElementById('gp_reply7').style.display = 'none';
    document.getElementById(list_answers[random_choice]).style.display = 'inline'; 
    document.getElementById("ask").style.display = 'none';
    document.getElementById('answer').style.display = 'inline';
    document.getElementById('other').style.display = 'inline'};

function incomprehension_message(){
    document.getElementById('comprehension').style.display = 'inline'};

function beginning_of_fatigue(){
    document.getElementById('overstrain').style.display = 'inline';
    document.getElementById("ask").style.display = 'none';
    document.getElementById('answer').style.display = 'inline';
    document.getElementById('other').style.display = 'inline'};
    

function gp_answer(grandpy_code){
    //~ var response_json = JSON.parse(grandpy_code);
    var response_json = grandpy_code
    switch(grandpy_code){
        case 'home':
            welcome_message();
            break;
        case 'tired':
            beginning_of_fatigue();
            break;
        case 'mannerless':
            rude_message();
            break;
        case 'disrespectful':
            message_of_meanness();
            break;
        case 'incomprehension':
            incomprehension_message();
            break;
        case 'response':
            random_grandpy_answer();
            break;
        default :
            response_quotas_reached();}
}

const send_request = document.getElementById('submit2');
send_request.addEventListener('submit', function(e){
    fetch("/index/2/" + document.getElementById('question').value) 
    .then(function(res){
        if (res.ok){
            return res.json();}
    })
    .then(function(value){
        gp_answer(value);
    })
    .catch(function(err){
        console.log('Une erreur est levé');
        console.log(err);})
    e.preventDefault();
});

//document.getElementById("question").text = "";
//document.getElementById("answer").style.display = 'none';
//document.getElementById("other").style.display = 'none';
