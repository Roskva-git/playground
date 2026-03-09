let raceNumber = Math.floor(Math.random() * 1000);

const registeredEarly = true;

const runnersAge = 18;

if (registeredEarly && runnersAge > 18) {
 raceNumber += 1000;
 }

if (registeredEarly && runnersAge > 18) {
 console.log(`Welcome to the race. Your start time is 9:30 am and your race number is ${raceNumber}`);
 } else if (runnersAge > 18 && !registeredEarly) {
   console.log(`Welcome to the race. Your start time is 11:00 am and your race number is ${raceNumber}`);
 } else if (runnersAge < 18) {
   console.log(`Welcome to the race. Your start time is 12:30 pm and your race number is ${raceNumber}`);
 } else {
   console.log("Please go to the registration desk.");
 }
