import { Component } from '@angular/core';
import { Product } from './product.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.sass']
})
export class AppComponent {
  name = 'Camilo';
  age = 25;
  btnDisable = true;
  person = {
    name: "Andrés",
    age: 25
  };
  box = {
    width: 100,
    height: 100,
    background: 'red'
  }
  register = {
    username: '',
    email: '',
    password: ''
  }
  nameList: string[] = ["Camilo"];
  nameTyped = "";

  image = "assets/kratos.png";

  products: Product[] = [
    {
      name: "Car",
      price: 450000,
      img: "assets/car.avif"
    },
    {
      name: "TV",
      price: 34000,
      img: "assets/tv.jpg"
    },
    {
      name: "PS5",
      price: 3100,
      img: "assets/ps5.jpg"
    },
    {
      name: "Iphone",
      price: 8000,
      img: "assets/iphone.jpg"
    },
    {
      name: "Air conditioner",
      price: 7800,
      img: "assets/ac.jpg"
    }
  ]

  pushName(){
    if (!this.nameList.includes(this.nameTyped)){
      this.nameList.push(this.nameTyped);
      this.nameTyped = "";
    }
  };

  popName(index: number){
    this.nameList.splice(index, 1);
  }


  toggleButton (){
    this.btnDisable = !this.btnDisable;
  };

  onScroll(event: Event) {
    const element = event.target as HTMLElement;
    console.log(element.scrollTop);
  };

  changeName(event: Event){
    const element = event.target as HTMLInputElement;
    this.name = element.value;
  }
  onRegister(){
    console.log(this.register);
  }
}
