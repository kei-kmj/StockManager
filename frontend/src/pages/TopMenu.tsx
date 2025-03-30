import { Menu } from "antd";
import { useRouter } from "@tanstack/react-router";

export const TopMenu = () => {
  const router = useRouter();

  const handleMenuClick = (e: { key: string }) => {
    router.navigate({ to: e.key });
  };

  const items = [
    { key: "/inventory", label: "在庫登録" },
    { key: "/item", label: "アイテム" },
        {
      key: "maker",
      label: "メーカー",
      children: [
        { key: "/makers", label: "メーカー一覧" },
        { key: "/makers/new", label: "メーカー登録" },
      ],
    },
    { key: "/month", label: "月次確定" },
    {
      key: "user",
      label: "利用者",
      children: [
        { key: "/users", label: "利用者一覧" },
        { key: "/users/new", label: "利用者登録" },
      ],
    },
  ];

  return (
    <Menu mode="horizontal" items={items} onClick={handleMenuClick} />
  );
};
