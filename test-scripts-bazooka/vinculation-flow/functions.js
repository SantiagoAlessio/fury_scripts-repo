function obtainCode(requestParams, response, context, ee, next){
    let uri = JSON.parse(response.body).return_uri

    let code = uri.split("code=")[1].split("&")[0]
    context.vars.validationCode = code
    next()
}

module.exports = {
    obtainCode: obtainCode
}