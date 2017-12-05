# para ejecutar el script desde el terminal usando ./plotivcv.py (si no hay permiso, se pide con: chmod 777 plotivcv.py)
#! /usr/bin/python

"""
def plotIVCVcurves(fileName, whatPlot):
   print "hola"
   # PARTE 1: Argumentos de entrada
   if (whatPlot==0):   # Dibujar solo IVs
      print "Dibujar IV "
   
   elif(whatPlot==1):  # Dibujar solo CVs
      print "Dibujar CV"

   elif(whatPlot==2):  # Dibujar IVs y CVs
      print "Dibujar ambas"


   #-------------------------------------------------------------------------------------------------------------------------

   # PARTE 2: Ficheros 
   # Cada fichero pertece a un pad distinto y contiene 4 subficheros pertenecientes a los cuatro sensores de dicho pad
   # Cada subfichero contiene dos archivos: uno con extension .iv y el otro con extension .cv
   # Encontrar y asociar los ficheros a representar.

   # Leer el nombre de fichero separandolo en dos mediante el punto. Segunda parte = tipo de plot:
   plotType = fileName.split('.')[1]

   if (plotType==iv):
      ejeY = "i"
      titlePlot = "IV curve"
   else:
      ejeY = "v"
      titlePlot = "CV curve"

   # leer el fichero de datos
   while(open('fileName').readLine()!="BEGIN"):
      open('fileName').NextLine()

   open('fileName').NextLine()  # saltar la linea con el texto "BEGIN" (la siguiente es la primera con datos)


   #-------------------------------------------------------------------------------------------------------------------------


   # PARTE 3: Generar plots 
      # importar liberia para hacer plots:
      import pylab as pl  
      # use pylab to plot x and y
      pl.plot(x, y)
	       	



   #---------------------------------------------------BACKUP----------------------------------------------------------------


    canvas = ROOT.TCanvas()
    # Pintar el ajuste calculado:
    ajuste.Draw()	 	        
    fitStatus = histo.Fit(ajuste, "SQ","", 1000,80000)
    mpv_down = ajuste.GetParameter(1)
    if not fitStatus.IsValid():
        print("\033[1;31mfailed fit: fit down\033[1;m")
    fitStatus = histo.Fit(ajuste, "SQ","", 10000,30000)
    mpv_up = ajuste.GetParameter(1)
    if not fitStatus.IsValid():
        print("\033[1;31mfailed fit: fit up\033[1;m")
    fitStatus = histo.Fit(ajuste, "SQ", "", 10000, 50000) # Ajustar el plot con el fit calculado y ajustar los limites del ajuste a posteriori
    mpv_nominal = ajuste.GetParameter(1)
    if not fitStatus.IsValid():
        print("\033[1;31mfailed fit: fit nominal\033[1;m")
    nom = "MPV: {0:.0f}#pm{1:.0f}".format(mpv_nominal, max(abs(mpv_nominal-mpv_down) , abs(mpv_up-mpv_nominal)))
    stringPlot = ROOT.TLatex()
    stringPlot.DrawLatexNDC(0.6,0.5,nom)

    #canvas.SaveAs("cluster_calibrated_charge_"+Nrun+".png")
    canvas.SaveAs("cluster_calibrated_charge_{0}.root".format(Nrun))

 """
def get_files(module_path,sensor_number_list):
    """WHAT THE FUNCTION DOES

    Parameters
    ----------
    module_path: str
      Name of the module´s directory (raise para errores
)
    Return
    ------
    ivfiles,cvfiles   
    """
    i=[]
    j=[]
    return i,j

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser(prog='plotivcv')
    # Argumento posicional:
    parser.add_argument('module_dir',help="Name of the module's directory"\
                          " which has several subdirectories with the data of each sensor inside the module")
    # Argumento opcional (tipo con la variable nargs, el + significa lista):
    parser.add_argument('-s', '--sensor-number', nargs="+", dest="sensor_number", help="Sensor subdirectory"\
                         " names inside the module_dir which are going to actually be plotted."\
                         " All the sensors in the module will be plotted if this argument is not used")
    # ejecucion del parser (lectura de los inputs del user):
    args = parser.parse_args()  
    print args.module_dir
    print args.sensor_number
    # Obtain the list IV,CV files, 
    ivfiles,cvfiles = get_files(args.module_dir,args.sensor_number)
    # Read and parse the files
    # for each ivfiles, then parse the file and return the array of measures (I,V)
    # for each cvfiles, then parse the file and return the array of measures (C,V)
    #.... 
    


