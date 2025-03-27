import {createRoute, Outlet} from '@tanstack/react-router'
import { RootRoute } from '../../RootRoute'
import {Users} from "./Users";
import {CreateUser} from "./CreateUser";
import {EditUser} from "./EditUser";
import {ShowUser} from "./ShowUser";

export const usersRoutes = createRoute(
    {
        getParentRoute: () => RootRoute,
        path: 'users',
        component: () => <Outlet />
    }
)

export const usersIndexRoute = createRoute({
  getParentRoute: () => usersRoutes,
  path: '/',
  component: Users,
})

export const createUserRoute = createRoute({
    getParentRoute: () => usersRoutes,
    path: 'new',
    component: CreateUser
})

export const showUserRoute = createRoute({
    getParentRoute: () => usersRoutes,
    path: '$userId',
    component: ShowUser
})

export const editUserRoute = createRoute({
    getParentRoute: () => usersRoutes,
    path: '$userId/edit',
    component: EditUser
})