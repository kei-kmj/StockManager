import { UserForm } from "../../components/form/User";
import {createUser} from "../../api/users";
import {useSaveHandler} from "../../components/useSaveHandler";


export const CreateUser = () => {
    const handleSubmit = useSaveHandler(
      createUser,
      {action: "登録", redirectTo: "/users"}
    );

    return <UserForm onSubmit={handleSubmit}/>
}