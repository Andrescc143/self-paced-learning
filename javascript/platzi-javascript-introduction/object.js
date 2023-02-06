var Car = {
    brand: "Volvo",
    model: 2023,
    details: function(){
        console.log(`My new car is a ${this.brand} which model is ${this.model}`);
    }
};


Car.details();