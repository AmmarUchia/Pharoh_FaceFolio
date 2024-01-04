from flask import Flask, render_template_string, request, jsonify
import cv2
import numpy as np
import face_recognition
import os
import base64
from io import BytesIO
from PIL import Image
import pickle  # Added for pickle support

app = Flask(__name__)

path = 'persons'
images = []
classNames = []
personsList = os.listdir(path)

for cl in personsList:
    #curPersonn = cv2.imread(f'{path}/{cl}')
    #images.append(curPersonn)
    classNames.append(os.path.splitext(cl)[0])

def findEncodeings(image):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

# Load face encodings from the pickle file
def loadFaceEncodings():
    with open('face_encodings.pickle', 'rb') as file:
        encodeListKnown = pickle.load(file)
    return encodeListKnown

encodeListKnown = loadFaceEncodings()
print('Face Encodings Loaded.')


@app.route('/')
def index():
    html_content=""" 




<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta content="width=device-width, initial-scale=1.0" name="viewport">

  <title>Impact Bootstrap Template - Index</title>
  <meta content="" name="description">
  <meta content="" name="keywords">

  <!-- Favicons -->
  <link href="{{ url_for('static', filename='favicon.png') }}" rel="icon">
  <link href="{{ url_for('static', filename='apple-touch-icon.png') }}" rel="apple-touch-icon">

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,600;1,700&family=Montserrat:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&family=Raleway:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&display=swap" rel="stylesheet">

  <!-- Vendor CSS Files -->
  <link href="{{ url_for('static', filename='bootstrap.min.css') }}" rel="stylesheet">
  <link href="{{ url_for('static', filename='bootstrap-icons.css') }}" rel="stylesheet">
  <link href="{{ url_for('static', filename='aos.css') }}" rel="stylesheet">
  <link href="{{ url_for('static', filename='glightbox.min.css') }}" rel="stylesheet">
  <link href="{{ url_for('static', filename='swiper-bundle.min.css') }}" rel="stylesheet">

  <!-- Template Main CSS File -->
  <link href="{{ url_for('static', filename='main.css') }}" rel="stylesheet">

  <!-- =======================================================
  * Template Name: Impact
  * Updated: Sep 18 2023 with Bootstrap v5.3.2
  * Template URL: https://bootstrapmade.com/impact-bootstrap-business-website-template/
  * Author: BootstrapMade.com
  * License: https://bootstrapmade.com/license/
  ======================================================== -->
</head>
<!-- ... Your existing HTML code ... -->

<!-- Include the JavaScript file -->


<body dir="">
  
    

  <header id="header" class="header d-flex align-items-center">

    <div class="container-fluid container-xl d-flex align-items-center justify-content-between">
      <a href="index.html" class="logo d-flex align-items-center">
        <!-- Uncomment the line below if you also wish to use an image logo -->
        <!-- <img src="assets/img/logo.png" alt=""> -->
        <h1>Phroh<span> _</span>Face-Folio<span>_</span></h1>
      </a>
      <nav id="navbar" class="navbar">
        <ul>
          <li><a href="#hero">Home</a></li>
          <li><a href="#about">About</a></li>
          <li><a href="#services">Services</a></li>
          <!-- <li><a href="#portfolio">Portfolio</a></li> -->
          <li><a href="#team">Team</a></li>

      </nav><!-- .navbar -->

      <i class="mobile-nav-toggle mobile-nav-show bi bi-list"></i>
      <i class="mobile-nav-toggle mobile-nav-hide d-none bi bi-x"></i>

    </div>
  </header><!-- End Header -->
  <!-- End Header -->

  <!-- ======= Hero Section ======= -->
  <section id="hero" class="hero">
    <div class="container position-relative">
      <div class="row gy-5" data-aos="fade-in">
        <div class="col-lg-6 order-2 order-lg-1 d-flex flex-column justify-content-center text-center text-lg-start">
          <h2>Welcome to <span>Phroh Face-Folio</span></h2>
          <p>Empowering Education: Faces Recognized, Connections Enhanced, Futures Transformed.</p>
          <div class="d-flex justify-content-center justify-content-lg-start">
            <a href="#try" class="btn-get-started">Try it</a>
            <!-- <a href="https://www.youtube.com/watch?v=LXb3EKWsInQ" class="glightbox btn-watch-video d-flex align-items-center"><i class="bi bi-play-circle"></i><span>Watch Video</span></a> -->
          </div>
        </div>
        <div class="col-lg-6 order-1 order-lg-2">
          <img src="{{ url_for('static', filename='hero-img.svg') }}" class="img-fluid" id="gh" alt="" data-aos="zoom-out" data-aos-delay="100">
        </div>
      </div>
    </div>


        </div>
      </div>
    </div>

    </div>
  </section>
  <!-- End Hero Section  -->

  <main id="main">

    <!-- ======= About Us Section ======= -->
    <section id="about" class="about">
      <div class="container" data-aos="fade-up">

        <div class="section-header">
          <h2>About Us</h2>
          <p>Embark on a transformative journey with Pharoh Face-Folio</p>
        </div>

        <div class="row gy-4">
          <div class="col-lg-6">
            <!-- <h3>Voluptatem dignissimos provident quasi corporis</h3> -->
            <img src="{{ url_for('static', filename='about.jpg') }}" class="img-fluid rounded-4 mb-4" style="margin-left: ;" alt="">
            <p>
              At the heart of Pharoh Face-Folio, our commitment is to seamlessly integrate facial recognition technology powered by AI into the educational experience, creating a dynamic synergy between students and teachers. In an era heavily reliant on artificial intelligence, we harness its features to enhance the educational environment.

            </p> 
          </div>
          <div class="col-lg-6">
            <div class="content ps-0 ps-lg-5">
              <p class="fst-italic">
                non-profit initiative where innovation and recognition converge to redefine the educational landscape through the power of artificial intelligence (AI). Recognizing faces isn't just about identification; it's about understanding, connection, and efficient communication.

              </p>
              <!-- <ul>
                <li><i class="bi bi-check-circle-fill"></i> Ullamco laboris nisi ut aliquip ex ea commodo consequat.</li>
                <li><i class="bi bi-check-circle-fill"></i> Duis aute irure dolor in reprehenderit in voluptate velit.</li>
                <li><i class="bi bi-check-circle-fill"></i> Ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate trideta storacalaperda mastiro dolore eu fugiat nulla pariatur.</li>
              </ul> -->

              <div class="position-relative mt-4">
                <img src="{{ url_for('static', filename='about-2.jpg') }}" class="img-fluid rounded-4" alt="">
                <!-- <a href="https://www.youtube.com/watch?v=LXb3EKWsInQ" class="glightbox play-btn"></a> -->


              </div>
            </div>
          </div>
        </div>

      </div>
    </section><!-- End About Us Section -->

    <!-- ======= Clients Section ======= -->
    <section id="clients" class="clients">
      <div class="container" data-aos="zoom-out">

        <div class="clients-slider">
          <div class="swiper-wrapper align-items-center">
            <div class="swiper-slide"><img src="{{ url_for('static', filename='client-1.png') }}" class="img-fluid" alt=""></div>
            <div class="swiper-slide"><img src="{{ url_for('static', filename='client-2.png') }}" class="img-fluid" alt=""></div>
            <div class="swiper-slide"><img src="{{ url_for('static', filename='client-3.png') }}" class="img-fluid" alt=""></div>
            <div class="swiper-slide"><img src="{{ url_for('static', filename='client-4.png') }}" class="img-fluid" alt=""></div>

          </div>
        </div>

      </div>
    </section><!-- End Clients Section -->

    <!-- ======= Stats Counter Section ======= -->
    
    <!-- ======= Our Services Section ======= -->
    <section id="services" class="services sections-bg">
      <div class="container" data-aos="fade-up">

        <div class="section-header">
          <h2>Why Choose Us</h2>
          <p>Empowering Futures, Delivering Excellence: Your Success, Our Commitment.</p>
        </div>

        <div class="row gy-4" data-aos="fade-up" data-aos-delay="100">

          <div class="col-lg-4 col-md-6">
            <div class="service-item  position-relative">
              <div class="icon" style="max-width: 150% ;">
                <img src="{{ url_for('static', filename='aim.png') }}" style="max-width: 150% ;"class="img-fluid"  alt="" style="z-index: 9;">
              </div>
              <h3>AI-Powered Precision</h3>
              <p>Our facial recognition system, driven by AI, is meticulously designed to ensure unparalleled precision in identifying students. Gone are the days of manual checks—experience swift and accurate recognition, fostering a seamless connection in the communication loop.</p>
              <!-- <a href="#" class="readmore stretched-link">Read more <i class="bi bi-arrow-right"></i></a> -->
              
            </div>
          </div><!-- End Service Item -->

          <div class="col-lg-4 col-md-6">
            <div class="service-item position-relative">
              <div class="icon">
                <img src="{{ url_for('static', filename='ui.png') }}" style="max-width: 150% ;"class="img-fluid"  alt="" style="z-index: 9;">
              </div>
              <h3>User-Friendly Interface</h3>
              <p>Education is complex; using AI technology shouldn't be. Our user-friendly interface is crafted to simplify the process, allowing teachers to effortlessly navigate and access the information they need, thereby enhancing efficiency in the educational process.</p>
              <!-- <a href="#" class="readmore stretched-link">Read more <i class="bi bi-arrow-right"></i></a> -->
            </div>
          </div><!-- End Service Item -->

          <div class="col-lg-4 col-md-6">
            <div class="service-item position-relative">
              <div class="icon">
                <img src="{{ url_for('static', filename='custom.png') }}" style="max-width: 150% ;"class="img-fluid"  alt="" style="z-index: 9;">
              </div>
              <h3>Customizable AI Solutions</h3>
              <p>Recognizing that every school is unique, we offer customizable AI solutions tailored to fit the specific requirements of your institution. Our goal is to seamlessly integrate with your existing systems, ensuring a personalized and efficient experience driven by the power of AI.</p>
              <!-- <a href="#" class="readmore stretched-link">Read more <i class="bi bi-arrow-right"></i></a> -->
            </div>
          </div><!-- End Service Item -->

        

        </div>

      </div>
    </section>
    

    <!-- ======= Call To Action Section ======= -->
<section id="call-to-action" class="call-to-action">
  <div class="container text-center" data-aos="zoom-out" id="try">
    <div id="webcamContainer"></div>
    <div id="result"></div>
    <button onclick="toggleWebcam()" class="cta-btn" style="background-color:#888374;"id="stbty">Start</button>
    <button onclick="refreshPage()" class="cta-btn" style="background-color:#888374;">Recognize Again</button>
    
    <canvas id="webcamCanvas" width="640" height="480" style="display: none; border: 2px solid red;"></canvas>
   <div id="recognizedName"></div>

  </div>
</section><!-- End Call To Action Section -->

    <!-- ======= Our Team Section ======= -->
    <section id="team" class="team">
      <div class="container" data-aos="fade-up">

        <div class="section-header">
          <h2>Our Team</h2>
          <p>Nulla dolorum nulla nesciunt rerum facere sed ut inventore quam porro nihil id ratione ea sunt quis dolorem dolore earum</p>
        </div>

        <div class="row gy-4">

          <div class="col-xl-3 col-md-6 d-flex" data-aos="fade-up" data-aos-delay="100">
            <div class="member">
              <img src="{{ url_for('static', filename='team-1.jpg') }}" class="img-fluid" alt="">
              <h4>Walter White</h4>
              <span>Web Development</span>
              <div class="social">
                <a href=""><i class="bi bi-twitter"></i></a>
                <a href=""><i class="bi bi-facebook"></i></a>
                <a href=""><i class="bi bi-instagram"></i></a>
                <a href=""><i class="bi bi-linkedin"></i></a>
              </div>
            </div>
          </div><!-- End Team Member -->

          <div class="col-xl-3 col-md-6 d-flex" data-aos="fade-up" data-aos-delay="200">
            <div class="member">
              <img src="{{ url_for('static', filename='team-2.jpg') }}" class="img-fluid" alt="">
              <h4>Sarah Jhinson</h4>
              <span>Marketing</span>
              <div class="social">
                <a href=""><i class="bi bi-twitter"></i></a>
                <a href=""><i class="bi bi-facebook"></i></a>
                <a href=""><i class="bi bi-instagram"></i></a>
                <a href=""><i class="bi bi-linkedin"></i></a>
              </div>
            </div>
          </div><!-- End Team Member -->

          <div class="col-xl-3 col-md-6 d-flex" data-aos="fade-up" data-aos-delay="300">
            <div class="member">
              <img src="{{ url_for('static', filename='team-3.jpg') }}" class="img-fluid" alt="">
              <h4>William Anderson</h4>
              <span>Content</span>
              <div class="social">
                <a href=""><i class="bi bi-twitter"></i></a>
                <a href=""><i class="bi bi-facebook"></i></a>
                <a href=""><i class="bi bi-instagram"></i></a>
                <a href=""><i class="bi bi-linkedin"></i></a>
              </div>
            </div>
          </div><!-- End Team Member -->

          <div class="col-xl-3 col-md-6 d-flex" data-aos="fade-up" data-aos-delay="400">
            <div class="member">
              <img src="{{ url_for('static', filename='team-4.jpg') }}" class="img-fluid" alt="">
              <h4>Amanda Jepson</h4>
              <span>Accountant</span>
              <div class="social">
                <a href=""><i class="bi bi-twitter"></i></a>
                <a href=""><i class="bi bi-facebook"></i></a>
                <a href=""><i class="bi bi-instagram"></i></a>
                <a href=""><i class="bi bi-linkedin"></i></a>
              </div>
            </div>
          </div><!-- End Team Member -->

        </div>

      </div>
    </section><!-- End Our Team Section -->

    

    <!-- ======= Frequently Asked Questions Section ======= -->
    <section id="faq" class="faq">
      <div class="container" data-aos="fade-up">

        <div class="row gy-4">

          <div class="col-lg-4">
            <div class="content px-xl-5">
              <h3>Frequently Asked <strong>Questions</strong></h3>
              <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Duis aute irure dolor in reprehenderit
              </p>
            </div>
          </div>

          <div class="col-lg-8">

            <div class="accordion accordion-flush" id="faqlist" data-aos="fade-up" data-aos-delay="100">

              <div class="accordion-item">
                <h3 class="accordion-header">
                  <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faq-content-1">
                    <span class="num">1.</span>
                    Non consectetur a erat nam at lectus urna duis?
                  </button>
                </h3>
                <div id="faq-content-1" class="accordion-collapse collapse" data-bs-parent="#faqlist">
                  <div class="accordion-body">
                    Feugiat pretium nibh ipsum consequat. Tempus iaculis urna id volutpat lacus laoreet non curabitur gravida. Venenatis lectus magna fringilla urna porttitor rhoncus dolor purus non.
                  </div>
                </div>
              </div><!-- # Faq item-->

              <div class="accordion-item">
                <h3 class="accordion-header">
                  <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faq-content-2">
                    <span class="num">2.</span>
                    Feugiat scelerisque varius morbi enim nunc faucibus a pellentesque?
                  </button>
                </h3>
                <div id="faq-content-2" class="accordion-collapse collapse" data-bs-parent="#faqlist">
                  <div class="accordion-body">
                    Dolor sit amet consectetur adipiscing elit pellentesque habitant morbi. Id interdum velit laoreet id donec ultrices. Fringilla phasellus faucibus scelerisque eleifend donec pretium. Est pellentesque elit ullamcorper dignissim. Mauris ultrices eros in cursus turpis massa tincidunt dui.
                  </div>
                </div>
              </div><!-- # Faq item-->

              <div class="accordion-item">
                <h3 class="accordion-header">
                  <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faq-content-3">
                    <span class="num">3.</span>
                    Dolor sit amet consectetur adipiscing elit pellentesque habitant morbi?
                  </button>
                </h3>
                <div id="faq-content-3" class="accordion-collapse collapse" data-bs-parent="#faqlist">
                  <div class="accordion-body">
                    Eleifend mi in nulla posuere sollicitudin aliquam ultrices sagittis orci. Faucibus pulvinar elementum integer enim. Sem nulla pharetra diam sit amet nisl suscipit. Rutrum tellus pellentesque eu tincidunt. Lectus urna duis convallis convallis tellus. Urna molestie at elementum eu facilisis sed odio morbi quis
                  </div>
                </div>
              </div><!-- # Faq item-->

              <div class="accordion-item">
                <h3 class="accordion-header">
                  <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faq-content-4">
                    <span class="num">4.</span>
                    Ac odio tempor orci dapibus. Aliquam eleifend mi in nulla?
                  </button>
                </h3>
                <div id="faq-content-4" class="accordion-collapse collapse" data-bs-parent="#faqlist">
                  <div class="accordion-body">
                    Dolor sit amet consectetur adipiscing elit pellentesque habitant morbi. Id interdum velit laoreet id donec ultrices. Fringilla phasellus faucibus scelerisque eleifend donec pretium. Est pellentesque elit ullamcorper dignissim. Mauris ultrices eros in cursus turpis massa tincidunt dui.
                  </div>
                </div>
              </div><!-- # Faq item-->

              <div class="accordion-item">
                <h3 class="accordion-header">
                  <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faq-content-5">
                    <span class="num">5.</span>
                    Tempus quam pellentesque nec nam aliquam sem et tortor consequat?
                  </button>
                </h3>
                <div id="faq-content-5" class="accordion-collapse collapse" data-bs-parent="#faqlist">
                  <div class="accordion-body">
                    Molestie a iaculis at erat pellentesque adipiscing commodo. Dignissim suspendisse in est ante in. Nunc vel risus commodo viverra maecenas accumsan. Sit amet nisl suscipit adipiscing bibendum est. Purus gravida quis blandit turpis cursus in
                  </div>
                </div>
              </div><!-- # Faq item-->

            </div>

          </div>
        </div>

      </div>
    </section>

        </div>

      </div>
    </section><!-- End Contact Section -->

  </main><!-- End #main -->

  <!-- ======= Footer ======= -->
  <footer id="footer" class="footer">

    <div class="container">
      <div class="row gy-4">
        <div class="col-lg-5 col-md-12 footer-info">
          <a href="index.html" class="logo d-flex align-items-center">
            <span>Impact</span>
          </a>
          <p>Cras fermentum odio eu feugiat lide par naso tierra. Justo eget nada terra videa magna derita valies darta donna mare fermentum iaculis eu non diam phasellus.</p>
          
        </div>

        <div class="col-lg-2 col-6 footer-links">
          <h4>Useful Links</h4>
          <ul>
            <li><a href="#">Home</a></li>
            <li><a href="#">About us</a></li>
             <li><a href="#">Services</a></li>
          </ul>
        </div>

        <div class="col-lg-2 col-6 footer-links">
          <h4>Our Services</h4>
          <ul>
            <li><a href="#">Web Design</a></li>
            <li><a href="#">Web Development</a></li>
            <li><a href="#">Product Management</a></li>
            <li><a href="#">Marketing</a></li>
            <li><a href="#">Graphic Design</a></li>
          </ul>
        </div>
      </div>
    </div>

    <div class="container mt-4">
      <div class="copyright">
        &copy; Copyright <strong><span>Impact</span></strong>. All Rights Reserved
      </div>
      <div class="credits">

        Designed by <a href="https://bootstrapmade.com/">BootstrapMade</a>
      </div>
    </div>

  </footer><!-- End Footer -->
  <!-- End Footer -->

  <a href="#" class="scroll-top d-flex align-items-center justify-content-center"><i class="bi bi-arrow-up-short"></i></a>

  <div id="preloader"></div>

  <!-- Vendor JS Files -->
  
  <script src="{{ url_for('static', filename='bootstrap.bundle.min.js') }}"></script>
  <script src="{{ url_for('static', filename='aos.js') }}"></script>
  <script src="{{ url_for('static', filename='glightbox.min.js') }}"></script>
  <script src="{{ url_for('static', filename='purecounter_vanilla.js') }}"></script>
  <script src="{{ url_for('static', filename='swiper-bundle.min.js') }}"></script>
  <script src="{{ url_for('static', filename='isotope.pkgd.min.js') }}"></script>
  <script src="{{ url_for('static', filename='validate.js') }}"></script>

  <!-- Template Main JS File -->
  <script src="{{ url_for('static', filename='main.js') }}"></script>
<script src="{{ url_for('static', filename='soc.js') }}"></script>
</body>

</html>




"""
    return render_template_string(html_content)
   # return render_template('index.html')

@app.route('/recognize', methods=['POST'])
def recognize():
    data = request.json
    image_data = data.get('image')

    if image_data:
        # Convert base64 image data to OpenCV image
        image = Image.open(BytesIO(base64.b64decode(image_data.split(',')[1])))
        img_np = np.array(image)
        img_rgb = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

        # Face recognition logic
        face_locations = face_recognition.face_locations(img_rgb)
        face_encodings = face_recognition.face_encodings(img_rgb, face_locations)

        result = []

        for encodeface, faceLoc in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(encodeListKnown, encodeface)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeface)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                result.append({'name': name})

        return jsonify(result)

    return jsonify({'error': 'No image data provided'})

if __name__ == '__main__':
    app.run()