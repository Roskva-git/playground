//The temperature today in kelvin
const kelvin = 270;

//The temperature today in celcius will be 273 degrees less than in kelvin
const celsius = kelvin - 273;

//converts Celsius to Newton
let newton = celsius * (33/100);

//Rounds down Newton to the closest integer
newton = Math.floor(newton);

//Converts celsius to fahrenheit
let fahrenheit = celsius * (9/5) + 32;

//Rounds down to the closest integer
fahrenheit = Math.floor(fahrenheit);

console.log(`The temperature today is ${fahrenheit} degrees Fahrenheit.`);
console.log(`The temperature today is ${newton} degrees Newton.`);
