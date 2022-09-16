function obtainCode(requestParams, response, context, ee, next){
    let uri = JSON.parse(response.body).return_uri

    let code = uri.split("code=")[1].split("&")[0]
    context.vars.validationCode = code
    if(response.statusCode === 500){
        console.log("error ", {url: response.url, body: JSON.parse(response.body)})
    }
    next()
}

function debugResponse(requestParams, response, context, ee, next){
    if(response.statusCode === 500){
        console.log("error ", {
            url: response.url,
            cardToek: context.vars.CardToken,
            body: JSON.parse(response.body)})
    }

    next()
}

module.exports = {
    obtainCode: obtainCode,
    debugResponse: debugResponse
}