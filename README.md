# Bundle para conseguir metadata de Animes de forma Local
Para instalar este plugin se debe copiar el bundle a la carpeta
Plugins de Plex,
Este plugin lo modifique de uno usado para musica y la verdad no lo he actualizado desde entonces, hasta ahora no parece tener problemas

No lo he probado con los ultimos cambios realizados por Plex

Instalación:<br/>
* Ir a la carpeta Library/Application Support/Plex Media Server/Plug-ins/ en mi caso en ubuntu se encuentra en ../var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Plug-ins<br/>
* Remover cualquier version antigua que se encuentre en esa carpeta (rm -r AnimeMeta.bundle).<br/>
* Descargar el Bundle mas reciente.<br/>
* Descomprimirlo pues al descargar de git deberia estar como ZIP, ingresar dentro de la carpeta AnimeMeta.bundle-master, dentro de la carpeta deberia haber un archivo README.md y AnimeMeta.bundle.<br/> 
![ezgif com-gif-maker](https://user-images.githubusercontent.com/60912834/94304762-742b2680-ff46-11ea-99f9-440e77b31ebe.gif)<br/> 
* Mover AnimeMeta.bundle a la carpeta Plug-ins.<br/>
* Reiniciar tu plex media server (service plexmediaserver restart para linux).<br/>
Uso:<br/>
* Ir a Settings -> Server -> Agents -> Movies/TV Shows (Ajustes --> Agentes --> Programas).<br/> 
<img width="1090" alt="Screen Shot 2020-09-25 at 15 36 19" src="https://user-images.githubusercontent.com/60912834/94304186-7a6cd300-ff45-11ea-9eab-c2e87b0455ca.png"><br/> 
* Activar el plugin y ordenarlo segun preferencia.<br/> 
<img width="1088" alt="Screen Shot 2020-09-25 at 15 56 03" src="https://user-images.githubusercontent.com/60912834/94305700-fe27bf00-ff47-11ea-9e89-81f338bd2614.png"><br/> 
* Refrescar tu libreria (o Pelicula/serie individual).<br/> 
<img width="738" alt="Screen Shot 2020-09-25 at 15 56 29" src="https://user-images.githubusercontent.com/60912834/94305821-362f0200-ff48-11ea-96c1-6b7f8da527e9.png"><br/>
* Luego asegurarse de tener los resumenes en la carpeta general con el nombre summary.txt<br/> 
<img src="https://aws1.discourse-cdn.com/plex/original/3X/e/e/ee0298e6c3ce6b6cb4ba00b62861a9a0c0f24271.png"><br/> 
* Finalmente actualizar los metadatos de toda la libreria o de la serie en especifico<br/> 
<img width="516" alt="Screen Shot 2020-09-25 at 16 02 00" src="https://user-images.githubusercontent.com/60912834/94305971-8017e800-ff48-11ea-8edd-4a5ef1f513e1.png"><br/> 
