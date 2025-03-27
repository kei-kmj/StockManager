import {useRouter} from "@tanstack/react-router";
import {Button} from "antd";

type EditButtonProps = {
  to: string
  params: Record<string, number>
}

export const EditButton = ({to, params}: EditButtonProps) => {
  const router = useRouter()

  const handleClick = () => {
    router.navigate({to, params})
  }

  return (
    <Button
      style={{
        backgroundColor: '#697A24',
        borderColor: '#697A24',
        color: 'white',
      }}
      onClick={handleClick}
    >
      編集
    </Button>
  );


}