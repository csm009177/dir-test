import fs from 'fs'

function makedir(dir, count){
  for(let i=0; i<count; i++){
     let dirName = dir + i;
    if(!fs.existsSync(dirName)){
      fs.mkdirSync(dirName)
    }
  }
}

makedir("sungmin", 10)