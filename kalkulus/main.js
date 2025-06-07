// main.js
// Menampilkan Kurva 3D berdasarkan Input
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.set(3, 3, 5);
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);
const controls = new THREE.OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;

// Input panjang dan lebar grid
const gridSizeInput = document.createElement("input");
gridSizeInput.type = "number";
gridSizeInput.value = 10;
gridSizeInput.min = 1;
gridSizeInput.style.position = "absolute";
gridSizeInput.style.top = "10px";
gridSizeInput.style.left = "10px";
document.body.appendChild(gridSizeInput);

gridSizeInput.addEventListener("change", updateGrid);

let gridHelper;
function updateGrid() {
    if (gridHelper) scene.remove(gridHelper);
    const size = parseFloat(gridSizeInput.value);
    gridHelper = new THREE.GridHelper(size, size * 2);
    scene.add(gridHelper);
    addNumberLabels(size);
}
updateGrid();

const axesHelper = new THREE.AxesHelper(5);
scene.add(axesHelper);
const light = new THREE.PointLight(0xffffff, 1, 100);
light.position.set(5, 5, 5);
scene.add(light);

// Menambahkan angka di tiap kotak grid
function addNumberLabels(size) {
    scene.children = scene.children.filter(child => !(child instanceof THREE.Sprite));
    
    for (let i = -size; i <= size; i += 1) {
        addLabel(i.toString(), { x: i, y: 0, z: 0 }, "white");
        addLabel(i.toString(), { x: 0, y: i, z: 0 }, "white");
    }
    
    for (let i = -size; i <= size; i += 0.1) {
        if (i % 1 !== 0) {
            addLabel(i.toFixed(1), { x: i, y: 0, z: 0 }, "gray", 0.3);
            addLabel(i.toFixed(1), { x: 0, y: i, z: 0 }, "gray", 0.3);
        }
    }
}

function addLabel(text, position, color, scale = 0.5) {
    const canvas = document.createElement("canvas");
    const ctx = canvas.getContext("2d");
    canvas.width = 256;
    canvas.height = 256;
    
    ctx.fillStyle = color;
    ctx.font = "40px Arial";
    ctx.fillText(text, 100, 150);
    
    const texture = new THREE.CanvasTexture(canvas);
    const material = new THREE.SpriteMaterial({ map: texture });
    const sprite = new THREE.Sprite(material);
    sprite.scale.set(scale, scale, scale);
    sprite.position.set(position.x, position.y, position.z);
    scene.add(sprite);
}

const data = JSON.parse(localStorage.getItem("polynomialData"));
if (data) {
    const points = [];
    const step = (parseFloat(data.x_max) - parseFloat(data.x_min)) / parseInt(data.jumlah_titik);
    for (let x = parseFloat(data.x_min); x <= parseFloat(data.x_max); x += step) {
        let y = 0;
        if (data.fungsi === "linear") {
            y = parseFloat(data.a) * x + parseFloat(data.b);
        } else if (data.fungsi === "kuadratik") {
            y = parseFloat(data.a) * x * x + parseFloat(data.b) * x + parseFloat(data.c);
        } else if (data.fungsi === "kubik") {
            y = parseFloat(data.a) * x * x * x + parseFloat(data.b) * x * x + parseFloat(data.c) * x + parseFloat(data.d);
        }
        points.push(new THREE.Vector2(x, y));
    }
    if (points.length > 1) {
        const geometry = new THREE.LatheGeometry(points, 50);
        const material = new THREE.MeshBasicMaterial({ color: 0x00ff00, wireframe: true });
        const curveMesh = new THREE.Mesh(geometry, material);
        scene.add(curveMesh);
    }
}



function animate() {
    requestAnimationFrame(animate);
    controls.update();
    renderer.render(scene, camera);
}
animate();
