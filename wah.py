side =  100
space = 1
Dsoil=  6
Dgravel= 1.5

A_Total=side**2
A_Sm_Box=   A_Total/4
A_Circ=     ((side/4)**2)*3.1415
A_Sm_Gar=   (A_Sm_Box-A_Circ)/4
A_Bg_Gar=   (A_Total-A_Circ*2-A_Sm_Box)
A_Flow  =   space**2
Num_Sm_Gar = int(A_Sm_Gar/A_Flow)
Num_Bg_Gar = int(A_Bg_Gar/A_Flow)
Total_Flow = (Num_Bg_Gar+Num_Sm_Gar)*4
Vol_Soil_Sm = A_Sm_Gar*Dsoil
Vol_Soil_Bg = A_Bg_Gar*Dsoil
Vol_Soil_Total = A_Sm_Gar*Dsoil*4+A_Bg_Gar*Dsoil*4
Vol_Grav = 3*A_Circ*Dgravel
print( Num_Sm_Gar, " Flowers in small flowerbed " )
print( Num_Bg_Gar, " Flowers in big flowerbed " )
print( Total_Flow, " Flowers in Total" )
print( (Vol_Soil_Sm*(1/27)), " Volume soil of small flowerbed in cubic yards " )
print( (Vol_Soil_Bg*(1/27)), " Volume soil of big flowerbed in cubic yards " )
print( (Vol_Soil_Total*(1/27)), " Volume of total soil in cubic yards " )
print( (Vol_Grav*(1/27)), " Volume of total gravel in cubic yards " )
