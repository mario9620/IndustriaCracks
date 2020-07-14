import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { LoginComponent } from './login/login.component';
import { PerfilComponent } from './perfil/perfil.component';

import { NavbarComponent } from './navbar/navbar.component';
import { ComprasComponent } from './compras/compras.component';

import{ InicioComponent } from './inicio/inicio.component'


const routes: Routes = [
  {path: 'login', component: LoginComponent },
  {path: 'perfil', component: PerfilComponent},
  {path: 'compras',  component: ComprasComponent },
  {path: 'inicio',component: InicioComponent}

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
