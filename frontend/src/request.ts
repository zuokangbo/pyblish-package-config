import type {AxiosRequestConfig, AxiosInstance, AxiosResponse} from "axios"
import axios from "axios"
import { get } from "lodash"

import SysCfg from "../config"
import Tools from "./tools"

export interface IResponse<T = any> {
    code: number;
    data: T;
    msg: string;
}

export interface AxiosRequestConExt extends AxiosRequestConfig {
    reqParams?: AxiosRequestConExt;
    showLoading?: boolean; // 是否显示loading提示
    bIsNeedCachePrevent?: boolean; // 是否加上防止缓存的cp随即苏
    bIsNeedJsonStringify?: boolean; // 是否需要json string
    bIsNeedQsstringify?: boolean; // 是否需要qs.stringify
    force401ToLogin?: boolean; // 遇到401是否强制跳转到登录界面


}

axios.defaults.headers.head["Content-Type"] = "application/json;chartset=utf-8"

let timerLoading: ReturnType<typeof setTimeout>;
const axiosInstance: AxiosInstance = axios.create({
    baseURL: SysCfg.getConfig<string>("baseUrl"),
    timeout: 10000
})

// 定义每次请求响应处理
axiosInstance.interceptors.response.use((res: AxiosResponse) => {
    clearTimeout(timerLoading)
    Tools.hideLoadMask()

    const {status, data, config} = res;
    const {reqParams = {}} = config as AxiosRequestConExt;
    const {force401ToLogin = false} = reqParams;

    // http 200状态码
    if (200 == status){
        if (data){
            if (401 == data.code && force401ToLogin){
                // 跳转到login页面
                SysCfg.redirectToLogin()
                return
            } else if (data.code >= 400 && data.code <= 404 || data.code == 500){
                return Promise.reject(data)
            }
        }

        return data
    } else {
        return Promise.reject(data)
    }

}, (error) => {
    clearTimeout(timerLoading)
    Tools.hideLoadMask()

    let {message = "Request Error", response } = error;

    const stErrMsg = get(response, "data.msg", message);
    return Promise.reject({msg:stErrMsg})
})

// 常用的请求方法
const getMethods: string[] = ["GET", "POST", "PUT", "DELETE"]
type IAjaxMethod = "get" | "post" | "put" | "delete"
type IFnAjaxMethodHandler = <T = any>(reqParams: AxiosRequestConExt) => Promise<IResponse<T>>;

// 绑定多种请求类型方法
const iAllMethods: {[key in IAjaxMethod]: IFnAjaxMethodHandler} = {} as any;

getMethods.map(method => {
    const fnHandler: IFnAjaxMethodHandler = <T = any>(reqParams: AxiosRequestConExt | string): Promise<IResponse<T>> => {
        if ("GET" == method){
            if ("string" === typeof reqParams){
                reqParams = {
                    url: reqParams,
                    params: ""
                }
            }
        }
        return Ajax.request<T>(method, reqParams as AxiosRequestConExt)
    }
    iAllMethods[method.toLocaleLowerCase() as IAjaxMethod] = fnHandler
})


const Ajax = {
    ...iAllMethods,
    request<T = any>(method: string, reqParams: AxiosRequestConExt): Promise<IResponse<T>> {
        let {
            url,
            params,
            headers = {},
            timeout,
            showLoading = true,
            bIsNeedCachePrevent,
            bIsNeedJsonStringify,
            bIsNeedQsstringify,
            force401ToLogin
        } = reqParams

        if (showLoading !== false){
            clearTimeout(timerLoading)
            timerLoading = setTimeout(() => {
                Tools.showLoadMask()
            }, 200)
        }

        // json.stringify
        bIsNeedJsonStringify && (params = JSON.stringify(params))

        const iSendReqParams: AxiosRequestConExt = {
            reqParams,
            url,
            method: (getMethods.indexOf(method) > -1 ? method: "GET"),
            [method === "GET" ? "params" : "data"]: params,
            headers: Object.assign({}, headers)
        }

        timeout && (iSendReqParams.timeout = timeout)
        return axiosInstance.request(iSendReqParams)
    }
}

export type IAjax = typeof Ajax;

export default Ajax

