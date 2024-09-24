const arrayContainer = document.getElementById('array-container');
let array = [];

function generateArray() {
    arrayContainer.innerHTML = '';
    array = [];
    for (let i = 0; i < 50; i++) {
        array.push(Math.floor(Math.random() * 100) + 1);
    }
    renderArray();
}

function renderArray() {
    arrayContainer.innerHTML = '';
    for (let i = 0; i < array.length; i++) {
        const bar = document.createElement('div');
        bar.classList.add('array-bar');
        bar.style.height = `${array[i]}%`;
        bar.style.width = '20px';
        arrayContainer.appendChild(bar);
    }
}

async function bubbleSort() {
    for (let i = 0; i < array.length - 1; i++) {
        for (let j = 0; j < array.length - i - 1; j++) {
            if (array[j] > array[j + 1]) {
                await swap(j, j + 1);
            }
        }
    }
}

async function selectionSort() {
    for (let i = 0; i < array.length; i++) {
        let minIndex = i;
        for (let j = i + 1; j < array.length; j++) {
            if (array[j] < array[minIndex]) {
                minIndex = j;
            }
        }
        await swap(i, minIndex);
    }
}

async function insertionSort() {
    for (let i = 1; i < array.length; i++) {
        let key = array[i];
        let j = i - 1;
        while (j >= 0 && array[j] > key) {
            await swap(j, j + 1, false);
            j = j - 1;
        }
        array[j + 1] = key;
        renderArray();
        await sleep(50);
    }
}

async function swap(i, j, update = true) {
    const bars = document.getElementsByClassName('array-bar');
    let temp = array[i];
    array[i] = array[j];
    array[j] = temp;

    if (update) {
        bars[i].style.height = `${array[i]}%`;
        bars[j].style.height = `${array[j]}%`;
    }
    await sleep(50);
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

generateArray();
