import {useParams} from "@tanstack/react-router";
import {useEffect, useState} from "react";
import {fetchMakerDetail, updateMaker, MakerDetailResponse, MakerUpdateRequest} from "../../api/makers";
import {MakerForm} from "../../components/form/Maker";
import {useSaveHandler} from "../../components/useSaveHandler";

export const EditMaker = () => {
  const {makerId} = useParams({from: '/makers/$makerId/edit'});

  const [maker, setMaker] = useState<MakerDetailResponse | undefined>()
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const loadMaker = async () => {
      const makerData = await fetchMakerDetail(Number(makerId))
      setMaker(makerData)
      setLoading(false)
    }
    loadMaker()
  }, [makerId])

  const handleSubmit = useSaveHandler(
    (values: MakerUpdateRequest) => updateMaker(Number(makerId), values),
    {action: "保存",
    redirectTo: "/makers"}
  )

  if (loading || !maker) return <p>Loading...</p>;

  return <MakerForm initialValues={maker} onSubmit={handleSubmit}/>;
}
