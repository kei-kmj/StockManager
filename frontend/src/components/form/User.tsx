import {Form, Input} from 'antd';
import {SaveButton} from "../SaveButton";
import {UserCreateRequest, UserUpdateRequest} from "../../api/users";

type UserFormProps = {
  initialValues?:UserCreateRequest | UserUpdateRequest
  onSubmit: (values: UserCreateRequest | UserUpdateRequest) => void;
};

export const UserForm = ({initialValues, onSubmit}: UserFormProps) => {
  const [form] = Form.useForm();

  return (<>
      <h2>ユーザー情報編集</h2>
      <Form
        form={form}
        layout="vertical"
        initialValues={initialValues}
        onFinish={onSubmit}
      >
        <Form.Item
          name="name"
          label="ユーザー名"
          rules={[{required: true, message: 'ユーザー名を入力してください'}]}
        >
          <Input/>
        </Form.Item>

        <Form.Item
          name="nickname"
          label="ニックネーム"
          rules={[{required: true, message: 'ニックネームを入力してください'}]}
        >
          <Input/>
        </Form.Item>

        <Form.Item
          name="email"
          label="メールアドレス"
          rules={[{required: true, message: 'メールアドレスを入力してください'}]}
        >
          <Input/>
        </Form.Item>

        <Form.Item>
          <SaveButton/>
        </Form.Item>
      </Form></>
  );
};
