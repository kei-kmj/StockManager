import {useParams} from "@tanstack/react-router";
import {useEffect, useState} from "react";
import {fetchUserDetail, updateUser, UserDetailResponse, UserUpdateRequest} from "../../api/users";
import {UserForm} from "../../components/form/User";
import {useSaveHandler} from "../../components/useSaveHandler";

export const EditUser = () => {
  const {userId} = useParams({from: '/users/$userId/edit'});

  const [user, setUser] = useState<UserDetailResponse | undefined>()
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const loadUser = async () => {
      const userData = await fetchUserDetail(Number(userId))
      setUser(userData)
      setLoading(false)
    }
    loadUser()
  }, [userId])

  const handleSubmit = useSaveHandler(
    (values: UserUpdateRequest) => updateUser(Number(userId), values),
    {action: "保存"}
  )

  if (loading || !user) return <p>Loading...</p>;

  return <UserForm initialValues={user} onSubmit={handleSubmit}/>;
}
