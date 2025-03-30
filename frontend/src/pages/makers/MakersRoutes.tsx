import {createRoute, Outlet} from '@tanstack/react-router'
import { RootRoute } from '../../RootRoute'
import {Makers} from "./Makers";
import {CreateMaker} from "./CreateMaker";
import {EditMaker} from "./EditMaker";
import {ShowMaker} from "./ShowMaker";

export const makersRoutes = createRoute(
    {
        getParentRoute: () => RootRoute,
        path: 'makers',
        component: () => <Outlet />
    }
)

export const makersIndexRoute = createRoute({
  getParentRoute: () => makersRoutes,
  path: '/',
  component: Makers,
})

export const createMakerRoute = createRoute({
    getParentRoute: () => makersRoutes,
    path: 'new',
    component: CreateMaker
})

export const showMakerRoute = createRoute({
    getParentRoute: () => makersRoutes,
    path: '$makerId',
    component: ShowMaker
})

export const editMakerRoute = createRoute({
    getParentRoute: () => makersRoutes,
    path: '$makerId/edit',
    component: EditMaker
})