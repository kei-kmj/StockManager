import 'antd/dist/reset.css';
import {useParams} from '@tanstack/react-router';
import {deleteUser, fetchUserDetail} from '../../api/users';
import {useEffect, useState} from "react";
import type {components} from "../../api/types";
import {Descriptions, Spin} from "antd";
import {DeleteButton} from "../../components/DeleteButton";
import {EditButton} from "../../components/EditButton";

type User = components['schemas']['UserCommon'];

export const ShowUser = () => {
  const {userId} = useParams({from: '/users/$userId'});
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const load = async () => {
      const data = await fetchUserDetail(Number(userId));
      if (data) setUser(data);
      setLoading(false);
    };
    load();
  }, [userId]);

  if (loading || !user) {
    return (<Spin spinning={loading} tip="読み込み中...">
      <Descriptions bordered column={1}>
      </Descriptions>
    </Spin>)
  }

  return (<>
      <div>
        <h2 className="text-xl font-bold mb-4">{user.name} さんの詳細</h2>
        <Descriptions bordered column={1}>
          <Descriptions.Item label="ID">{user.id}</Descriptions.Item>
          <Descriptions.Item label="名前">{user.name}</Descriptions.Item>
          <Descriptions.Item label="ニックネーム">{user.nickname}</Descriptions.Item>
          <Descriptions.Item label="メールアドレス">{user.email}</Descriptions.Item>
          <Descriptions.Item label="登録日時">{user.created_at.slice(0, 10)}</Descriptions.Item>
        </Descriptions>
      </div>
      <div className="mt-4 flex justify-center gap-2">
        <EditButton to="/users/$userId/edit" params={{userId: user.id}} />
        <DeleteButton deleteFunction={deleteUser} id={user.id} redirectTo="/users"/>
      </div>

    </>
  );
};
