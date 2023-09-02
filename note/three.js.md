# three.js折腾记录
## 入门快。git clone后开nginx或fastapi,访问examples/*.html,成。
## npm/nodejs: 可以不用。
- 不过后期要在vscode中加入代码提示的话，需要在git目录中npm install three vite
## javascript模块化：
- html的modulemap中加cssbase
- html中<script type="module" src="cssjs.js"></script>
- cssbase.js中写常规框架
- cssjs.js中import {scene,camera,controls,renderer} from './cssbase.js',作init

## shadow
```javascript
renderer.shadowMap.enabled=true
light.castShadow=true; cube.castShadow=true; plane.receiveShadow=true;
```
- MeshBasicMaterial不产生shadow(不对光照产生任何反应)

## PlaneGeometry(x,y,segx,segy)
- planeg.rotateX(Math.PI/2)
```javascript
for(let i=0;i<planeg.attributes.position.count;i++)
  v.fromBufferAttribute(position,i)
  v.z += Math.random()
  position.setXYZ(i,v.x, v.y, v.z)
}
```
- planeg.toNonIndexed();
- planeg.attributes.position.needsUpdate = true;
- planeg.computeVertexNormals();//for shadow
