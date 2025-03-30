import {Form, Input} from 'antd';
import {SaveButton} from "../SaveButton";
import {MakerCreateRequest, MakerUpdateRequest} from "../../api/makers";

type MakerFormProps = {
  initialValues?:MakerCreateRequest | MakerUpdateRequest
  onSubmit: (values: MakerCreateRequest | MakerUpdateRequest) => void;
};

export const MakerForm = ({initialValues, onSubmit}: MakerFormProps) => {
  const [form] = Form.useForm();

  return (<>
      <h2>メーカー情報編集</h2>
      <Form
        form={form}
        layout="vertical"
        initialValues={initialValues}
        onFinish={onSubmit}
      >
        <Form.Item
          name="name"
          label="メーカー名"
          rules={[{required: true, message: 'ユーザー名を入力してください'}]}
        >
          <Input/>
        </Form.Item>

        <Form.Item>
          <SaveButton/>
        </Form.Item>
      </Form></>
  );
};
