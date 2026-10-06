import fs from 'fs';
import {feature} from 'topojson-client';
import {geoContains, geoBounds} from 'd3-geo';
const topo=JSON.parse(fs.readFileSync('node_modules/world-atlas/countries-50m.json'));
const fc=feature(topo,topo.objects.countries).features;
const mem={764:'THA',156:'CHN',410:'KOR',458:'MYS',702:'SGP',344:'HKG',704:'VNM',360:'IDN',608:'PHL',96:'BRN',158:'TWN',604:'PER',152:'CHL',484:'MEX',598:'PNG',554:'NZL',392:'JPN',36:'AUS',643:'RUS'};
const feats=fc.map(f=>({f,b:geoBounds(f),id:+f.id}));
const LON0=30, LON1=300, LAT0=72, LAT1=-56, STEP=1.5;
const cols=Math.round((LON1-LON0)/STEP), rows=Math.round((LAT0-LAT1)/STEP);
let out=[];
for(let r=0;r<rows;r++){ const lat=LAT0-r*STEP-STEP/2;
 for(let c=0;c<cols;c++){ let lon=LON0+c*STEP+STEP/2; let L=lon>180?lon-360:lon;
  for(const {f,b,id} of feats){
    const [[x0,y0],[x1,y1]]=b; if(lat<y0-1||lat>y1+1)continue;
    if(x0<=x1){ if(L<x0-1||L>x1+1)continue }
    if(geoContains(f,[L,lat])){ const m=mem[id]; out.push([c,r, m? (m==='RUS'?2:1):0]); break; }
  }
 }}
// encode: per dot 3 chars? use compact arrays
const enc=out.map(([c,r,t])=>String.fromCharCode(48+Math.floor(c/64),48+c%64,48+r,48+t)).join('');
fs.writeFileSync('dots.txt',JSON.stringify({cols,rows,LON0,LAT0,STEP,n:out.length,d:enc}));
console.log(cols,rows,out.length, enc.length);
