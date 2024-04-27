import { Component, ViewChild } from '@angular/core';
import { Expense } from '../dto/expense';
import { ExpenseService } from '../service/expense-service';
import { MatButtonModule } from '@angular/material/button';
import {MatTable, MatTableModule} from '@angular/material/table';

@Component({
  selector: 'app-home-page',
  standalone: true,
  imports: [MatButtonModule, MatTableModule],
  templateUrl: './home-page.component.html',
  styleUrl: './home-page.component.css'
})
export class HomePageComponent  {

  @ViewChild(MatTable) table: MatTable<Expense>;
  expenseData: Expense[];
  displayedColumns = ['title', 'amount', 'date'];

  constructor(private readonly expenseService: ExpenseService) {};

  ngOnInit() {
    this.expenseService.getAllExpenseRows().subscribe(response => this.expenseData = response.data);
    this.table.renderRows();
  }

}
