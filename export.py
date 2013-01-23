
mkdir skiloyper
pgsql2shp -f ski_900913.shp -u turkompisen turkompisen "select osm_id, lit, piste_type, piste_grooming, way from planet_osm_line where piste_type='nordic' or route='ski'"
ogr2ogr -s_srs EPSG:900913 -t_srs EPSG:4326 skiloyper.shp ski_900913.shp
ogr2ogr -F "GPX" skiloyper.gpx skiloyper.shp
rm ski_900913*
mv skiloyper* skiloyper

mkdir stier
pgsql2shp -f blaamerka_sti_900913.shp -u turkompisen turkompisen "select osm_id, lit, way from planet_osm_line where trailblazed='yes' or marked_trail='blue'"
ogr2ogr -s_srs EPSG:900913 -t_srs EPSG:4326 blaamerka_sti.shp blaamerka_sti_900913.shp
ogr2ogr -F "GPX" blaamerka_sti.gpx blaamerka_sti.shp
rm blaamerka_sti_900913*

pgsql2shp -f alle_stier_900913.shp -u turkompisen turkompisen "select osm_id, lit, way from planet_osm_line where highway='path'"
ogr2ogr -s_srs EPSG:900913 -t_srs EPSG:4326 alle_stier.shp alle_stier_900913.shp
ogr2ogr -F "GPX" alle_stier.gpx alle_stier.shp
rm alle_stier_900913*
mv alle* blaamerka* stier