import 'antd/dist/reset.css';
import {useParams} from '@tanstack/react-router';
import {deleteMaker, fetchMakerDetail} from '../../api/makers';
import {useEffect, useState} from "react";
import type {components} from "../../api/types";
import {Descriptions, Spin} from "antd";
import {DeleteButton} from "../../components/DeleteButton";
import {EditButton} from "../../components/EditButton";

type Maker = components['schemas']['MakerCommon'];

export const ShowMaker = () => {
  const {makerId} = useParams({from: '/makers/$makerId'});
  const [maker, setMaker] = useState<Maker | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const load = async () => {
      const data = await fetchMakerDetail(Number(makerId));
      if (data) setMaker(data);
      setLoading(false);
    };
    load();
  }, [makerId]);

  if (loading || !maker) {
    return (<Spin spinning={loading} tip="読み込み中...">
      <Descriptions bordered column={1}>
      </Descriptions>
    </Spin>)
  }

  return (<>
      <div>
        <h2 className="text-xl font-bold mb-4">{maker.name} の詳細</h2>
        <Descriptions bordered column={1}>
          <Descriptions.Item label="ID">{maker.id}</Descriptions.Item>
          <Descriptions.Item label="名前">{maker.name}</Descriptions.Item>
          <Descriptions.Item label="登録日時">{maker.created_at.slice(0, 10)}</Descriptions.Item>
        </Descriptions>
      </div>
      <div className="mt-4 flex justify-center gap-2">
        <EditButton to="/makers/$makerId/edit" params={{makerId: maker.id}} />
        <DeleteButton deleteFunction={deleteMaker} id={maker.id} redirectTo="/makers"/>
      </div>

    </>
  );
};
