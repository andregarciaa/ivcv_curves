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


   #-------------------------------------------------------------------------------------------

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


   # primeros pasos lectura de los ficheros:
            readfileCV = open(ficherosIVCV[0],'rb') 
            readfileIV = open(ficherosIVCV[1],'rb')

            cont = 0
            while (readfileCV.readLine() != "BEGIN"):
                readfileCV.readLine()
                cont = cont+1
            # mostrar los valores en el documento (a partir de la linea "BEGIN":
            readfileCV.readLine(cont) 


   #------------------------------------------------------------------------------------------


   # PARTE 3: Generar plots 
      # importar liberia para hacer plots:
      import pylab as pl  
      # use pylab to plot x and y
      pl.plot(x, y)
	       	



   #--------------------------------BACKUP---------------------------------------------------


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
    """ WHAT THE FUNCTION DOES
        This function receives the directory containing the module folders with data
        and a list of the sensors which the user wants to plot.

    Parameters
    ----------
    module_path: str (string)
      Name of the module´s directory (raise para errores)
    sensor_number_list (array)
      Array con los nombres de los sensores dentro del module_path que queremos plotear

    Return
    ------
    ivfiles,cvfiles   
    """
    # funcion para ver contenido de un fichero. Importarlo:
    from os import listdir, path
    # importar funcion array:
    import array

    # pasar como input el directorio (tal cual entre comillas o un string). 
    # Devuelve array con los elementos que encuentra en el directorio
    directories = listdir(module_path)

    # si el directorio introducido esta vacio se lanza mensaje de error y se para el programa:
    if (directories == []):
        print("\033[1;35mERROR: The given directory is empty\033[1;m")
        # salir del programa: (otra opcion es: sys.exit(1))
        raise

    k = 0
    # array que guarda los ficheros con los datos IV y CV a plotear:
    plot_folder = []
    ficherosIVCV = []
    valuescv = []
    valuesiv = []

    # recorrer el array directories para quedarnos con las carpetas de los sensores dentro del 
    # modulo que se han pedido plotear (las carpetas contienen el fichero IV y CV). Para ello
    # se compara la terminacion con la lista de sensores que se paso como input:
    for fichero in directories:

        # split the name of the folders when finding a "_": (da 2 strings) Ex: "W5-B220_S2" (medidas pre-Andrea) 
        if (sensor_number_list[k] == fichero.split('_')[1]):
            # si la carpeta es una de la lista de sensores a plotear, se agrega a una nueva lista:
            plot_folder.append(fichero)
            # concatenar el directorio con el nombre del sensor, para entrar en la carpeta con la IV y CV:
            ficherosIVCV.append(listdir(os.path.join(module_path, sensor_number_list[k])))
            # guardar por separado IV y CV:
            valuescv.append(ficherosIVCV[k])
            valuesiv.append(ficherosIVCV[k+1])

        # or when finding a second "-": (da 3 strings)  Ex: "W5-B230-S2" (medidas Andrea)
        elif (sensor_number_list[k] == fichero.split('-')[2]):
            plot_folder.append(fichero)
            # concatenar el directorio con el nombre del sensor, para entrar en la carpeta con la IV y CV:
            ficherosIVCV.append(listdir(os.path.join(module_path, sensor_number_list[k])))
            # guardar por separado IV y CV:
            valuescv.append(ficherosIVCV[k])
            valuesiv.append(ficherosIVCV[k+1])

        else:
            print("\033[1;35mERROR: The requested sensor/s are not in the given directory\033[1;m")
            # salir del programa: (otra opcion es: sys.exit(1))
            raise
        k = k+1

    return valuescv, valuesiv

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
    

