function setup(){
 //   noCanvas();
	
	let speech = new p5.Speech();
	let speechRec = new p5.SpeechRec('en-IN', gotSpeech);
	let continuous = true;
	let interim = false;
	speechRec.start(continuous, interim);
	
	let bot = new RiveScript();
	bot.loadFile("brain/brain.rive", brainReady, brainError);

	function brainReady(){
		console.log('Chatbot Ready!');
		bot.sortReplies();
	}
	
	function brainError(){
		console.log('Chatbot Error!')
	}
	
	let button = select('#submit');
	let user_input = select('#user_input');
	let output = select('#output');
	
	button.mousePressed(chat);
	
	function gotSpeech() {
		if(speechRec.resultValue){
        	let input = speechRec.resultString;
	  		let reply = bot.reply("local-user", input);
			speech.speak(reply);
			output.html(reply);		
   		}
 	}

	
	function chat(){
		let input = user_input.value();
		let reply = bot.reply("local-user", input);
			speech.speak(reply);
			output.html(reply);
	}
	
	

}


