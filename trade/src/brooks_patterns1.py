lbl_body_doji = "doji"
lbl_body_bull = "branco"
lbl_body_bear = "preto"
lbl_tail_top = "top"
lbl_tail_bottom = "bottom"
lbl_tail_neutral = "neutral"
lbl_buy_pressure = "compra"
lbl_sell_pressure = "venda"

class BrooksPatterns1(object):

    body_doji_max = 10
    body_trend_min = 50
    
    def __init__(self, body, top, bottom, close, retracement):
        self.body = body
        self.top = top
        self.bottom = bottom
        self.close = close
        self.retracement = retracement
        self.body_pattern = self.__get_body_pattern()
        self.tail = self.__get_tail()
        self.pattern = self.__get_pattern()

    def __get_body_pattern(self):
        """ Padrão de corpo: alta/baixa/doji."""
        if abs(self.body) <= self.body_doji_max:
            return lbl_body_doji
        if self.body > 0:
            return lbl_body_bull
        if self.body < 0:
            return lbl_body_bear

    def __get_tail(self):
        """Sombra menor: top/bottom/neutral."""
        if self.top < self.bottom:
            return lbl_tail_top
        if self.bottom < self.top:
            return lbl_tail_bottom
        return lbl_tail_neutral

    def __get_pattern(self):
        """ Padrão de uma barra: careca/topo raspado, fundo raspado."""
        if self.__is_buy_pressure():
            return lbl_buy_pressure
        if self.__is_sell_pressure():
            return lbl_sell_pressure
        return ""
    
    def __is_topo_careca(self):
        """ Se for topo careca retorna true."""
        pass
    
    def __is_fundo_careca(self):
        """ Se for fundo careca retorna true."""
        pass
    
    def __is_careca(self):
        """ Se for careca retorna true."""
        pass
    
    def __is_buy_pressure(self):
        """ Se tiver pressão compradora retorna true."""
        if self.body < 0:
            return False
        if abs(self.body) < self.body_trend_min:
            return False
        if self.close < self.retracement:
            return False
        if abs(self.body) >= 80:
            return True
        #if self.bottom < self.top:
            #return False
        return True
    
    def __is_sell_pressure(self):
        """ Se tiver pressão vendedora retorna true."""
        if self.body > 0:
            return False
        if abs(self.body) < self.body_trend_min:
            return False
        if self.close > self.retracement:
            return False
        if abs(self.body) >= 80:
            return True
        #if self.top < self.bottom:
            #return False
        return True
        


