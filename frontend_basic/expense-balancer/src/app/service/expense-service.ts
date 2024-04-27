import { HttpClient } from "@angular/common/http";
import { environment } from "../constants/environment";
import { Injectable } from "@angular/core";
import { Expense } from "../dto/expense";
import { Observable, catchError, map } from 'rxjs';
import { ExpenseResponse } from "../dto/expense-response";

@Injectable({
    providedIn: 'root'
  })
export class ExpenseService {
    constructor(private httpClient: HttpClient) {}

    getAllExpenseRows(): Observable<ExpenseResponse> {
        return this.httpClient.get<ExpenseResponse>(environment.serverUrl + '/expense/getall').pipe();
    }
}