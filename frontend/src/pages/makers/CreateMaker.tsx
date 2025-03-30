
import {useSaveHandler} from "../../components/useSaveHandler";
import {createMaker} from "../../api/makers";
import {MakerForm} from "../../components/form/Maker";


export const CreateMaker = () => {
    const handleSubmit = useSaveHandler(
      createMaker,
      {action: "登録", redirectTo: "/makers"}
    );

    return <MakerForm onSubmit={handleSubmit}/>
}