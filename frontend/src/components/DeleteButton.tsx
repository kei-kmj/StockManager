import {Button, message, Popconfirm} from "antd";
import {useRouter} from "@tanstack/react-router";


type DeleteButtonProps = {
  deleteFunction: (id: number) => Promise<void>
  id: number
  redirectTo: string
}

export const DeleteButton = ({
                               deleteFunction,
                               id,
                               redirectTo
                             }: DeleteButtonProps) => {
  const router = useRouter()

  const onDeleteConfirm = async () => {

    try {
      await deleteFunction(id)
      message.success('削除しました');
      router.navigate({to: redirectTo});
    } catch (error) {
      message.error('削除できませんでした');
      console.error(error);
    }
  }
  return (
    <Popconfirm
      title="本当に削除しますか？"
      description="この操作は元に戻せません"
      onConfirm={onDeleteConfirm}
      okText="削除"
      cancelText="キャンセル"
      okButtonProps={{
        style: {
          backgroundColor: '#697A24',
          borderColor: '#697A24',
          color: '#fff',
        },
      }}>
      <Button
        style={{
          borderColor: '#697A24',
          color: '#697A24'
        }}
      >
        削除
      </Button>
    </Popconfirm>
  )

}