#!/usr/bin/perl

use LWP::UserAgent;

if (!$ARGV[0]) {


print q (

#+"-------------------------------------------------------------+"#
#    _____  .__                 ____._____.         .__.__      +"#
#   /  _  \ |  |               |    |__\_ |_________|__|  |     +"#
#  /  /_\  \|  |    ______     |    |  || __ \_  __ \  |  |     +"#
# /    |    \  |__ /_____/ /\__|    |  || \_\ \  | \/  |  |__   +"#
# \____|__  /____/         \________|__||___  /__|  |__|____/   +"#
#         \/                                \/                  +"#
#                                                               +"#
#                                 Admin_Finder versi  v.X-00.1  +"#
#+"-------------------------------------------------------------+"#

                  Admin_Finder versi v.X-00.1
         Tutorial seperti dibawah/Tutorials like this below 
            perl Admin_Finder.pl http://www.target.com
           --------------------------------------------
              [+]contact me : dexter666@live.com[+]    
                 [+]Coded by DexteR Al-jibril[+]
#+"-------------------------------------------------------------+"#
#    _____  .__                 ____._____.         .__.__      +"#
#   /  _  \ |  |               |    |__\_ |_________|__|  |     +"#
#  /  /_\  \|  |    ______     |    |  || __ \_  __ \  |  |     +"#
# /    |    \  |__ /_____/ /\__|    |  || \_\ \  | \/  |  |__   +"#
# \____|__  /____/         \________|__||___  /__|  |__|____/   +"#
#         \/                                \/                  +"#
#                                                               +"#
#                                 Admin_Finder versi  v.X-00.1  +"#
#+"-------------------------------------------------------------+"#
);

exit 1;

}

print q (


);

$target = $ARGV[0];

print("\n [-] Target: $target \n");

@paneles=('admin/','ADMIN/','paneldecontrol/','login/','adm/','cms/',
'admon/','ADMON/','administrador/','administrator/','admin/login.php',
'ADMIN/login.php','admin/home.php','admin/controlpanel.html','admin/controlpanel.php','admin.php',
'admin.html','admin/cp.php','admin/cp.html','cp.php','cp.html','controlpanel/','panelc/',
'administrator/index.php','administrator/login.html','administrator/login.php','administrator/account.html',
'administrator/account.php','administrator.php','administrator.html','login.php','login.html',
'modelsearch/login.php','moderator.php','moderator.html','moderator/login.php','moderator/login.html',
'moderator/admin.php','moderator/admin.html','moderator/','account.php','account.html','controlpanel/',
'admin/index.asp','admin/login.asp','admin/home.asp','admin/controlpanel.asp','admin.asp','admin/cp.asp',
'cp.asp','administrator/index.asp','administrator/login.asp','administrator/account.asp','administrator.asp',
'login.asp','modelsearch/login.asp','moderator.asp','moderator/login.asp','moderator/admin.asp','account.asp',
'controlpanel.asp','admincontrol.asp','adminpanel.asp','fileadmin/','fileadmin.php','fileadmin.asp',
'fileadmin.html','administration/','administration.php','administration.html','sysadmin.php','sysadmin.html',
'phpmyadmin/','myadmin/','sysadmin.asp','sysadmin/','ur-admin.asp','ur-admin.php','ur-admin.html','ur-admin/',
'Server.php','Server.html','Server.asp','Server/','wp-admin/','administr8.php','administr8.html',
'administr8/','administr8.asp','webadmin/','webadmin.php','webadmin.asp','webadmin.html','administratie/',
'admins/','admins.php','admins.asp','admins.html','administrivia/','Database_Administration/','WebAdmin/',
'sysadmins/','admin1/','system-administration/','administrators/','pgadmin/','directadmin/',
'staradmin/','ServerAdministrator/','SysAdmin/','administer/','sys-admin/','typo3/',
'panel/','cpanel/','cPanel/','cpanel_file/','platz_login/','rcLogin/','blogindex/',
'formslogin/','autologin/','support_login/','meta_login/','manuallogin/','simpleLogin/',
'loginflat/','utility_login/','showlogin/','memlogin/','members/','login-redirect/','sub-login/',
'wp-login/','login1/','dir-login/','login_db/','xlogin/','smblogin/','customer_login/',
'login-us/','acct_login/','admin_area/','bigadmin/','project-admins/','phppgadmin/','pureadmin/',
'sql-admin/','radmind/','openvpnadmin/','wizmysqladmin/','vadmind/','ezsqliteadmin/',
'hpwebjetadmin/','newsadmin/','adminpro/','Lotus_Domino_Admin/','bbadmin/','vmailadmin/',
'Indy_admin/','ccp14admin/','irc-macadmin/','banneradmin/','sshadmin/','phpldapadmin/','macadmin/',
'administratoraccounts/','admin4_account/','admin4_colon/','radmind-1/','Super-Admin/','AdminTools/',
'cmsadmin/','SysAdmin2/','globes_admin/','cadmins/','phpSQLiteAdmin/','navSiteAdmin/','server_admin_small/',
'logo_sysadmin/','server/','database_administration/','ADMIN/login.html','system_administration/','ss_vms_admin_sm/');

foreach $finder( @paneles) {
 $buscador = LWP::UserAgent->new() or die;
 $busqueda = $buscador->get($target."/".$finder);

 if ($busqueda->content =~ /username/ || $busqueda->content =~ /Username/ || $busqueda->content =~ /UserName/ ||
  $busqueda->content =~ /usuario/ || $busqueda->content =~ /Usuario/ ||
  $busqueda->content =~ /user/ || $busqueda->content =~ /User/ ||
  $busqueda->content =~ /password/ || $busqueda->content =~ /Password/ ||
  $busqueda->content =~ /contraseña/ || $busqueda->content =~ /Contraseña/ ||
  $busqueda->content =~ /senha/ || $busqueda->content =~ /Senha/ ||
  $busqueda->content =~ /pass/ || $busqueda->content =~ /Pass/ ||
  $busqueda->content =~ /pwd/ || $busqueda->content =~ /Pwd/
 ) {
  print("\n [+] scanner: $target/$finder \n\a");
 }
}

exit 1;
