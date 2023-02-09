import { Component, Input, Output, EventEmitter, OnInit, OnChanges,
   SimpleChanges, AfterViewInit, OnDestroy, SimpleChange } from '@angular/core';

@Component({
  selector: 'app-img',
  templateUrl: './img.component.html',
  styleUrls: ['./img.component.scss']
})
export class ImgComponent {

  @Input() img: string = "";
  @Input() imgAlt: string = "";

  defaultImg: string = "./assets/default-img.png";

  imgError(){
    this.img = this.defaultImg;
  }

}

/*
  @Output() loaded = new EventEmitter<string>();
  @Input('img')
  set changeImg(img: string){
    this.img = img
    console.log("The image changed")
  };

  counter: number = 0;
  counterFunction: number = 0;

  constructor(){
    //before render
    //Avoid to run asynchronous tasks
    console.log('Constructor', 'imgValue => ', this.img)
  }


  ngOnInit(): void {
    //Before render. Asyn processes, fetch API, etc. It runs once.
    console.log('On Init')
    this.counterFunction = window.setInterval(() => {
      this.counter += 1;
      console.log("Running the setInterval method to increase the counter.");
    }, 1000);
    console.log(this.counterFunction);
  }

  ngOnChanges(changes: SimpleChanges): void {
      //Before render. It is in charge to update the Inputs.
      console.log('On changes.', 'Changes => ', changes);
  }

  ngAfterViewInit(): void {
      //After render. Here we can manage the children of this component.
      console.log('On AfterViewInit')
  }

  ngOnDestroy(): void {
    console.log('On Destroy');
    window.clearInterval(this.counterFunction);
  }

  imgLoaded(){
    console.log("Imagen loaded")
    this.loaded.emit(this.img);
  }
  */
