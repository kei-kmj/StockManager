import {useRouter} from "@tanstack/react-router";
import {message} from "antd";
import {ActionType} from "./types";


type SaveHandlerOptions = {
  action: ActionType
  redirectTo? :string
}

// ジェネリクス型 (Generics)
// 型を柔軟に扱えるようにする
export const useSaveHandler = <T, R>(
  saveFunction: (values: T) => Promise<R>,
  options?: SaveHandlerOptions
) => {
  const router = useRouter()

  return async (values: T) => {
    try {

      await saveFunction(values)

      if (options?.action) {
        message.success(`${options.action}しました`)
      }

      if (options?.redirectTo) {
        router.navigate({to: options.redirectTo})
      }
    }
    catch (error) {
      message.error(`${options?.action}できませんでした`)
      console.error(error)
    }
  }
}