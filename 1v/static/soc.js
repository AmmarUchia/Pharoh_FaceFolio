let videoStream;
let video;
let canvas;
let recognizedNameDiv;
let recognizing = false;

async function toggleWebcam() {
    if (recognizing) {
        stopWebcam();
    } else {
        startWebcam();
    }
}

async function startWebcam() {
    try {
        await fetch('/load_encodings');

        videoStream = await navigator.mediaDevices.getUserMedia({ video: true });
        video = document.createElement('video');
        video.srcObject = videoStream;
        video.autoplay = true;

        // Get the specific section where you want to append the video
        const targetSection = document.getElementById('webcamContainer');

        // Append the video to the target section
        targetSection.appendChild(video);

        canvas = document.getElementById('webcamCanvas');
        //recognizedNameDiv = document.getElementById('recognizedName');

        setInterval(() => {
            captureAndRecognize();
        },100); // rec interval

        recognizing = true;
        document.querySelector('button').style.display = 'none';
    } catch (error) {
        console.error('Error accessing webcam:', error);
    }
}

function refreshPage() {
    location.reload();

}

function stopWebcam() {
    if (videoStream) {
        videoStream.getTracks().forEach(track => track.stop());
        video.remove();

        recognizing = false;
        document.querySelector('button').innerText = 'Start';
    }
}

async function captureAndRecognize() {
    if (!videoStream) {
        console.error('Webcam not started.');
        return;
    }

    const context = canvas.getContext('2d');
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    const imageData = canvas.toDataURL('image/jpeg');

    const response = await fetch('/recognize', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ image: imageData }),
    });

    const data = await response.json();

    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = '';

    data.forEach(person => {
        const nameParts = person.name.split('_');

        // Check if there are two parts
        if (nameParts.length === 2) {
            // Display the first part in "name:" element
            resultDiv.innerHTML += `<p>Name: ${nameParts[0]}</p>`;
            
            // Display the second part in "name2:" element
            resultDiv.innerHTML += `<p>Class: ${nameParts[1]}</p>`;
        } else {
            // Handle the case when the name format is unexpected
            resultDiv.innerHTML += `<p>Unexpected name format: ${person.name}</p>`;
        }

       //resultDiv.innerHTML += `<p>Name: ${person.name} </p>`;
        
        // Check if a name is recognized
        if (person.name) {
            // Stop the webcam
            stopWebcam();
            captureAndRecognize = false;
            recognizing = false;
            document.querySelector('button').style.display = 'none';
            //document.getElementById('stbty').style.display = 'none';
            // You can add additional actions here when a name is recognized
            // For example, display a message, redirect to another page, etc.



            // Example: Display a message
           // alert(`Name: ${nameParts[0]}Class: ${nameParts[1]} `);
            
        }
    });

    // Display recognized name under the canvas
    // recognizedNameDiv.innerHTML = data.length > 0 ? `CLASS: ${data[0].name}` : 'No match found';
}

document.addEventListener('DOMContentLoaded', initializeWebcam);
