import {createRouter} from '@tanstack/react-router'
import {RootRoute} from './RootRoute'
import {createUserRoute, editUserRoute, showUserRoute, usersIndexRoute, usersRoutes} from "./pages/users/UsersRoutes";
import {
  createMakerRoute,
  editMakerRoute,
  makersIndexRoute,
  makersRoutes,
  showMakerRoute
} from "./pages/makers/MakersRoutes";


const routeTree = RootRoute.addChildren([
  usersRoutes.addChildren([
    usersIndexRoute,
    createUserRoute,
    showUserRoute,
    editUserRoute,
  ]),
  makersRoutes.addChildren([
    makersIndexRoute,
    createMakerRoute,
    showMakerRoute,
    editMakerRoute

  ])
])


export const router = createRouter({routeTree})

declare module '@tanstack/react-router' {
  interface Register {
    router: typeof router
  }
}