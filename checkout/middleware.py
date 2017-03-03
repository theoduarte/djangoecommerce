# coding=utf-8

def cart_item_middleware(get_response):

    def middleware(request):
        #print('antes da resposta')
        session_key = request.session.session_key
        response = get_response(request)
        #print('depois da resposta')
        if session_key != request.session.session_key:
            CartItem.objects.filter(cart_key=session_key).update(
                cart_key=request.session.session_key
            )
        return response

    return middleware
