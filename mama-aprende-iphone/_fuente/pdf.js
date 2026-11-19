// Genera los PDF para leer sin internet. Uso (desde la raíz del sitio, con un servidor en :8766):
//   node mama-aprende-iphone/_fuente/pdf.js
const {chromium}=require('playwright'); const fs=require('fs');
(async()=>{const b=await chromium.launch(); const p=await b.newPage();
  fs.mkdirSync('mama-aprende-iphone/pdf',{recursive:true});
  const n=fs.readdirSync('mama-aprende-iphone').filter(f=>/^leccion-\d+\.html$/.test(f)).length;
  for(let i=1;i<=n;i++){ await p.goto(`http://localhost:8766/mama-aprende-iphone/leccion-${i}.html`); await p.waitForTimeout(300);
    await p.pdf({path:`mama-aprende-iphone/pdf/leccion-${i}.pdf`,format:'Letter',printBackground:true,margin:{top:'14mm',bottom:'14mm',left:'12mm',right:'12mm'}}); }
  await b.close(); console.log('pdf',n);})();
