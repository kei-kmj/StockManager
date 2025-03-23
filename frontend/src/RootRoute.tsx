import { createRootRoute } from '@tanstack/react-router'
import { Outlet } from '@tanstack/react-router'
import {App} from "./App";

export const RootRoute = createRootRoute({
    component: () => (
        <><div>
            <App />
            <Outlet />
        </div></>
    )
})