// import cookies from "js-cookie"

const iTools = {
    //显示全局遮罩
    showLoadMask(){

    },

    hideLoadMask(){

    },

    showError(title: string = "", msg: string = ""){
        alert(`${title}: ${msg}`)
    },

    processApiError(title: string, res: (string | {msg: string}) = {msg: ""}){
        if ("string" == typeof res){
            res = {msg: res}
        }
        this.showError(title, res.msg)
    }
}

export default iTools;

