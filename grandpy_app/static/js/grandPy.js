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
    document.getElementById('answer').style.display = 'inline';
    document.getElementById('other').style.display = 'inline'};

function incomprehension_message(){
    document.getElementById('comprehension').style.display = 'inline'};

function beginning_of_fatigue(){
    document.getElementById('overstrain').style.display = 'inline';
    document.getElementById("ask").style.display = 'none';
    document.getElementById('answer').style.display = 'inline';
    document.getElementById('other').style.display = 'inline'};
    
var data_send = {
    'grandpy_response_quotas': false,
    'nb_incivility': 0,
    'nb_indecency': 0,
    'nb_incomprehension': 0,
    'nb_request': 0,
 
    'incr_request': function(){
        this.nb_request += 1 
        if (this.nb_request == 5){
            return beginning_of_fatigue()}
        else{
            return random_grandpy_answer()}},
 
    'incr_incivility': function(){
        this.nb_incivility += 1
        if (this.nb_incivility >= 3){
            this.nb_incivility = 3
            this.grandpy_response_quotas = true
            return response_quotas_reached}
        else{
            return message_of_meanness()}},

    'incr_indecency': function(){
        this.nb_indecency += 1
        if (this.nb_indecency >= 3){
            this.nb_indecency = 3
            this.grandpy_response_quotas = true
            return response_quotas_reached}
        else{
            return rude_message()}},

    'incr_incomprehension': function(){
        this.nb_incomprehension += 1
        if (this.nb_incomprehension >= 3){
            this.nb_incomprehension = 3
            this.grandpy_response_quotas = true
            return response_quotas_reached}
        else{
            return incomprehension_message()}}
}

var response_json = JSON.parse(data_send)
if (!response_json['grandpy_response_quotas'] ){
    if (response_json['nb_incivility'] == 0 || (response_json['nb_incivility']< 3){
        data_send.incr_request()}
    else{
        data_send.incr_incility()}
        
    if (response_json['nb_indecency'] == 0) || (response_json['nb_indecency'] < 3){
        data_send.incr_request()}
    else{
        data_send.incr_indecency()}
        
    if (response_json['nb_incomprehension'] == 0) || 
        (response_json['nb_incomprehension']< 3){
        data_send.incr_request()}
    else{
        data_send.incr_incomprehensuion()}        
}
//document.getElementById("question").text = "";
//document.getElementById("answer").style.display = 'none';
//document.getElementById("other").style.display = 'none';
