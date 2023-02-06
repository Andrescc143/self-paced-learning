function CarConstructor (brand, model){
    this.brand = brand;
    this.model = model;
    this.details = function(){
        return `This car is a ${this.brand}, which model is ${this.model}`;
    }

}

var newCar = new CarConstructor("Volvo", 2023);
console.log(newCar.details());