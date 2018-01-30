 # para ejecutar el script desde el terminal usando ./plotivcv.py (si no hay permiso, se pide con: chmod 777 plotivcv.py)
#! /usr/bin/python


   #-------------------------------------------------------------------------------------------

   # PARTE 2: Ficheros 
   # Cada fichero pertece a un pad distinto y contiene 4 subficheros pertenecientes a los cuatro sensores de dicho pad
   # Cada subfichero contiene dos archivos: uno con extension .iv y el otro con extension .cv
   # Encontrar y asociar los ficheros a representar.

    # recorrer el array con los nombres de los ficheros a plotear y para cada uno de ellos, hacer el plot:
    for fileName in ivfiles:
        # Leer el (path+nombre de fichero) separandolo en dos mediante el punto. Segunda parte = tipo de plot:
        plotType = fileName.split('.')[1]
        if (plotType==iv):
            ejeY = "i"
            titlePlot = "IV curve"
        else:
            ejeY = "v"
            titlePlot = "CV curve"

        # leer el fichero de datos: saltar el cabecero, despues de BEGIN empiezan los datos:
        while(open('fileName').readLine()!="BEGIN"):
            open('fileName').NextLine()

        open('fileName').NextLine()  # saltar la linea con el texto "BEGIN" (la siguiente es la primera con datos)

        # ir guardando el contenido de todas las lineas en el array ivdata:
        while((open('fileName').readLine()!= "")
            ivdata = open('fileName').readLine()

              """
        # primeros pasos lectura de los ficheros:
        readfileCV = open(ficherosIVCV[0],'rb') 
        readfileIV = open(ficherosIVCV[1],'rb')

        cont = 0
        while (readfileCV.readLine() != "BEGIN"):
            readfileCV.readLine()
            cont = cont+1
        # mostrar los valores en el documento (a partir de la linea "BEGIN":
        readfileCV.readLine(cont) 
             """
"""

   #------------------------------------------------------------------------------------------

   # PARTE 3: Generar plots 
      # importar liberia para hacer plots:
      import pylab as pl  
      # use pylab to plot x and y
      pl.plot(x, y)	       	

   #--------------------------------BACKUP---------------------------------------------------

    # Se podria implementar que el usuario eliga si quiere ver la IV, la CV o ambas (en la segunda parte):

    def plotIVCVcurves(fileName, whatPlot):
       print "hola"
       # PARTE 1: Argumentos de entrada
       if (whatPlot==0):   # Dibujar solo IVs
          print "Dibujar IV "
   
       elif(whatPlot==1):  # Dibujar solo CVs
          print "Dibujar CV"

       elif(whatPlot==2):  # Dibujar IVs y CVs
          print "Dibujar ambas"

    # ----------------------------

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
      Name of the module's directory
    sensor_number_list (array)
      Array with the names of the sensors inside the module_path which the user wants to plot

    Return
    Two arrays with the paths and names of the files which contain the data which is goint to be plotted
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

    # array que guarda los ficheros con los datos IV y CV a plotear:
    plot_folder = []
    ficherosIVCV = []
    cvfiles = []
    ivfiles = []
    # variable which checks if between 'sensor_number_list' and 'directories' were coincidences (not zero) or not (zero, so the requested sensor is not there)
    checker = 0
    
    # recorrer el array directories para quedarnos con las carpetas de los sensores dentro del 
    # modulo que se han pedido plotear (las carpetas contienen el fichero IV y CV). Para ello
    # se compara la terminacion con la lista de sensores que se paso como input:
    for fichero in directories:
        # cada fichero en el path introducido se compara con cada uno de los sensores de la lista a plotear:
        for k in range(0,len(sensor_number_list)):
            # split the name of the folders when finding a "_": (da 2 strings) Ex: "W5-B220_S2" (medidas pre-Andrea) 
            # or when finding a second "-": (da 3 strings)  Ex: "W5-B230-S2" (medidas Andrea)
            if (sensor_number_list[k] == fichero.split('_')[1] or sensor_number_list[k] == fichero.split('-')[2]):
                checker = 1
                # si la carpeta es una de la lista de sensores a plotear, se agrega a una nueva lista:
                plot_folder.append(fichero)
                # concatenar el directorio con el nombre del sensor, para entrar en la carpeta con la IV y CV:
                # allficherosIVCV contiene la lista de todos los iv y cv pedidos:
                allficherosIVCV.append(listdir(os.path.join(module_path, fichero)))
                # ficherosIVCV contiene solo los iv y cv del sensor que se esta guardando ahora:
                ficherosIVCV = listdir(os.path.join(module_path, fichero))

                # si se repitio varias veces la medida IV o CV para un sensor, (porque la primera medida se hizo mal o para comprobar que algo raro se repite siempre), se para el codigo:
                if (len(ficherosIVCV)>2):
                    print("\033[1;35mERROR: There are several IV or CV measurements done for the same sensor. Please leave just one of each type inside all the sensor folders.\033[1;m")
                    raise

                # guardar por separado los nombres de los ficheros IV y CV:
                cvfiles.append(ficherosIVCV[0])
                ivfiles.append(ficherosIVCV[1])

    if(checker == 0):
        print("\033[1;35mERROR: The requested sensor/s are not in the given directory\033[1;m")
        # salir del programa: (otra opcion es: sys.exit(1))
        raise
            
    return cvfiles, ivfiles

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
    # Obtain the list IV,CV files. First output of get_files is the cv data, and second the iv
    cvfiles,ivfiles = get_files(args.module_dir,args.sensor_number)
    # Read and parse the files
    # for each ivfiles, then parse the file and return the array of measures (I,V)
    ivdata = get_data(ivfiles)
    # for each cvfiles, then parse the file and return the array of measures (C,V)
    #.... 
    

