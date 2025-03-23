import { createRouter } from '@tanstack/react-router'
import { RootRoute } from './RootRoute'
import {createUserRoute, editUserRoute, usersIndexRoute, usersRoutes} from "./pages/users/UsersRoutes";


const routeTree = RootRoute.addChildren([
    usersRoutes.addChildren([
        usersIndexRoute,
        createUserRoute,
        editUserRoute
    ])
])


export const router = createRouter({routeTree})

declare module '@tanstack/react-router' {
  interface Register {
    router: typeof router
  }
}