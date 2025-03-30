import {useEffect, useState} from "react";
import type {components} from '../../api/types'
import {fetchMakers} from "../../api/makers";
import type {ColumnsType} from 'antd/es/table'
import {Table} from "antd";
import {Link} from "@tanstack/react-router";

type Maker = components['schemas']['MakerCommon'];

export const Makers = () => {
    const [makers, setMakers] = useState<Maker[]>([])
    const [loading, setLoading] = useState(true)

    useEffect(() => {
        const load = async () => {
            const data = await fetchMakers()

            if (data) setMakers(data)
            setLoading(false)
        }
        load()
    }, [])

    const columns: ColumnsType<Maker> = [
        {
            title: 'メーカーID',
            dataIndex: 'id',
            key: 'id',
        },
        {
            title: 'メーカー名',
            dataIndex: 'name',
            key: 'name',
            render: (_text, record) => (
                <Link to="/makers/$makerId" params={{makerId: record.id.toString()}}>
                    {record.name}
                </Link>)
        },
        {
            title: '登録日時',
            dataIndex: 'created_at',
            key: 'created_at',
            render: (text: string) => text.slice(0, 10)
        },
    ];

    return (
        <div>
            <h2 className="text-lg font-bold mb-4">メーカー一覧</h2>
            <Table<Maker>
                columns={columns}
                dataSource={makers}
                loading={loading}
                rowKey="id"
                pagination={{pageSize: 10}}
            />
        </div>
    );
}