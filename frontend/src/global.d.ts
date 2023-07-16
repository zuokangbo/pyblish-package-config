import type {IAjax} from "./request"

declare global {
    const Ajax: IAjax
    interface Window{
        Ajax: IAjax
    }

}

export {}

