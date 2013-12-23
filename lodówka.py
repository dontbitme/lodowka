# -*- coding: utf-8 -*-
class Lodowka(object):
    
    def __init__(self):
        self.products = []
        self.temperature = None
        self.status = False  

    def find_products_index(self, product_name):
        for index in range(len(self.products)):
            if self.products[index].name == product_name:
                return index
            
    def add_product(self, product):
        index = self.find_products_index(product.name)
        if index != None:
            self.products[index].weight += product.weight
        else:
            self.products.append(product)

                

                     
    def delete_product(self, product_name):
        
        index = self.find_products_index(product_name)
        if index != None:
            self.products.remove(self.products[index])
        else:
            print "there is no product with this name.."
                    
                
                
            
            
        
            
            
            

     
           
            
    def show_products(self):
        print "------ PRODUCTS ------"
        for product in self.products:
            print '- ', product.name, product.price, product.weight, product.expiration_date
        print "----------------------"
        
    def turn_on(self):
        self.status = True
    
    def turn_off(self):
        self.status = False
    
    def show_status(self):
        return self.status
        
    def set_temp(self, temp):
        self.temperature = temp
    
    def show_temperature(self):
        return self.temperature
    
    def total_price(self):
        hajs = 0
        for x in self.products:
            hajs += x.price
        print hajs    
        
        
    def take_out(self, product):
        for a in self.products:
            if a.name == product.name:
                self.products.remove(a)
                print "Product " + a.name +" was taken out..."
            else:
                print "There is no product with this name..."
             
   
    def najwiecej(self):
        lis=[]
        for s in self.products:
            self.products.index(s.name)        #NIE ZROBI£EM


            
        
            
            


class Produkt(object):
    def __init__(self, name, price, weight, expiration_date):
        self.name = name
        self.price = price
        self.weight = weight
        self.expiration_date = expiration_date
        

p = Produkt('banan', 3, 0.5, '01.03.2013')
p1 = Produkt('jablko', 3, 0.5, '01.03.2013') 
p2 = Produkt('cytryna', 3, 0.5, '01.03.2013') 


l = Lodowka()
l.add_product(p)
l.add_product(p1)
l.add_product(p2)
l.show_products()
l.delete_product("banan")
l.show_products()





