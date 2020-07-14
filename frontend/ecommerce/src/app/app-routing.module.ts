import { NgModule, Component } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { LoginComponent } from './login/login.component';
import { PerfilComponent } from './perfil/perfil.component';

import { NavbarComponent } from './navbar/navbar.component';
import { ComprasComponent } from './compras/compras.component';

import{ InicioComponent } from './inicio/inicio.component'
import{ FooterComponent } from './footer/footer.component'

const routes: Routes = [
  {path: 'login', component: LoginComponent },
  {path: 'perfil', component: PerfilComponent},
  {path: 'compras',  component: ComprasComponent },
  {path: 'inicio',component: InicioComponent},
  {path: 'footer',component: FooterComponent}

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
