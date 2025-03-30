import {createRootRoute} from '@tanstack/react-router'
import {Outlet} from '@tanstack/react-router'
import {Header} from "antd/es/layout/layout";
import {Footer} from "antd/lib/layout/layout";
import {TopMenu} from "./pages/TopMenu";
import {Layout} from "antd";

export const RootRoute = createRootRoute({

  component: () => (
    <Layout style={{minHeight: '100vh', width: '100%'}}>
      {/* ヘッダー */}
      <Header style={{background: '#f0f2f5', padding: '0 16px', height: '6vh'}}>
        <div className="w-full text-right">
          <span className="mr-5">📢 今月の月次締めは3月31日です</span>
          <span className="mr-5">👤 Keiko</span>
          <span className="mr-5">設定</span>
          <span className="ml-5">ヘルプ</span>
        </div>
      </Header>

      <Header style={{background: '#fff', padding: 0, height: 'auto'}}>
        <TopMenu/>
      </Header>

      <Layout.Content style={{flex: 1, padding: '24px 16px'}}>
        <Outlet/>
      </Layout.Content>

      <Footer style={{height: '10vh', textAlign: 'center'}}>
        © 2025 SlackStock 🦥 — Managed with 💙 by KamijoInfomationServices
      </Footer>
    </Layout>
  )
})
