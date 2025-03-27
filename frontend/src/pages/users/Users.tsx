import {useEffect, useState} from "react";
import type {components} from '../../api/types'
import {fetchUsers} from "../../api/users";
import type {ColumnsType} from 'antd/es/table'
import {Table} from "antd";
import {Link} from "@tanstack/react-router";

type User = components['schemas']['UserCommon'];

export const Users = () => {
    const [users, setUsers] = useState<User[]>([])
    const [loading, setLoading] = useState(true)

    useEffect(() => {
        const load = async () => {
            const data = await fetchUsers()

            if (data) setUsers(data)
            setLoading(false)
        }
        load()
    }, [])

    const columns: ColumnsType<User> = [
        {
            title: 'ユーザーID',
            dataIndex: 'id',
            key: 'id',
        },
        {
            title: 'ニックネーム',
            dataIndex: 'nickname',
            key: 'nickname',
            render: (_text, record) => (
                <Link to="/users/$userId" params={{userId: record.id.toString()}}>
                    {record.nickname}
                </Link>)
        },
        {
            title: 'メールアドレス',
            dataIndex: 'email',
            key: 'email',
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
            <h2 className="text-lg font-bold mb-4">ユーザー一覧</h2>
            <Table<User>
                columns={columns}
                dataSource={users}
                loading={loading}
                rowKey="id"
                pagination={{pageSize: 10}}
            />
        </div>
    );
}