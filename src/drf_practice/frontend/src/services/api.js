import axios from 'axios'
import store from '@/store'

/***
 * APIにアクセスするために共通で利用するクライアントを定義
 */
const api = axios.create({
    // 環境ごとに異なる値が自動的に設定される
    // 下記のように環境ごとに.envを作成し値を定義しておけばコードの出し分けが必要なくなる
    //   frontend/.env.production VUE_APP_ROOT_API = /api/v1/
    //   frontend/.env.development VUE_APP_ROOT_API = http://localhost/api/v1/
    baseURL: process.env.VUE_APP_ROOT_API,
    timeout: 5000,
    headers: {
        'Content-Type': 'application/json',
        'X-Requested-With': 'XMLHttpRequest'
    }
})

// 共通前処理
api.interceptors.request.use(function (config) {
    // メッセージをクリア
    store.dispatch('message/clearMessages')
    // 認証用トークンがあればリクエストヘッダに乗せる
    const token = localStorage.getItem('access')
    if (token) {
        config.headers.Authorization = 'JWT ' + token
        return config
    }
    return config
}, function (error) {
    return Promise.reject(error)
})

// 共通エラー処理
api.interceptors.response.use(function (response) {
    return response
}, function (error) {
    console.log('error.response=', error.response)
    const status = error.response ? error.response.status : 500

    // エラーの内容に応じてstoreのメッセージ更新
    let message
    if (status == 400) {
        // バリデーションNG
        let messages = [].concat.apply([], Object.values(error.response.data))
        store.dispatch('message/setWarningMessagees', { messages: messages })

    } else if (status === 401) {
        // 認証エラー
        const token = localStorage.getItem('access')
        if (token != null) {
            message = 'ログイン有効期限切れ'
        } else {
            message = '認証エラー'
        }
        store.dispatch('auth/logout')
        store.dispatch('message/setErrorMessage', { message: message })

    } else if (status === 403) {
        // 権限エラー
        message = '権限エラーです'
        store.dispatch('message/setErrorMessage', { message: message })

    } else {
        // その他エラー
        message = '想定外のエラーです'
        store.dispatch('message/setErrorMessage', { message: message })
    }
    return Promise.reject(error)
})

export default api