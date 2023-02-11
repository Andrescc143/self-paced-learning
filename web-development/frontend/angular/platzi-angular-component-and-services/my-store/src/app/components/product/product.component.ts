import { Component, Input, Output, EventEmitter } from '@angular/core';
import { IProduct } from 'src/app/models/product.model';

@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.scss']
})
export class ProductComponent {
  @Input() product: IProduct ={
    id: "",
    title: "",
    price: 0,
    image: "",
    description: "",
    category: ""
  }

  @Output() productAdded = new EventEmitter<IProduct>();

  onAddToCart(): void {
    this.productAdded.emit(this.product);
  }
}
