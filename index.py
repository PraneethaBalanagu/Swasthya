import http.client

conn = http.client.HTTPSConnection("exercises-by-api-ninjas.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "SIGN-UP-FOR-KEY",
    'X-RapidAPI-Host': "exercises-by-api-ninjas.p.rapidapi.com"
    }

conn.request("GET", "/v1/exercises?muscle=biceps", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))




      <div class="row g-4 py-5 row-cols-1 row-cols-lg-3">
        <div class="feature col">
          <div class="feature-icon d-inline-flex align-items-center justify-content-center text-bg-primary bg-gradient fs-2 mb-3">
            <svg class="bi" width="1em" height="1em"><use xlink:href="#collection"></use></svg>
          </div>
          <h3 class="fs-2">Physical Health</h3>
          <p>txt</p>
          <a href="/login.html" class="icon-link d-inline-flex align-items-center">
            Click Here
            <svg class="bi" width="1em" height="1em"><use xlink:href="#chevron-right"></use></svg>
          </a>
        </div>
        <div class="feature col">
          <div class="feature-icon d-inline-flex align-items-center justify-content-center text-bg-primary bg-gradient fs-2 mb-3">
            <svg class="bi" width="1em" height="1em"><use xlink:href="#people-circle"></use></svg>
          </div>
          <h3 class="fs-2">Mental Health</h3>
          <p>txt</p>
          <a href="#" class="icon-link d-inline-flex align-items-center">
            Click Here
            
            <svg class="bi" width="1em" height="1em"><use xlink:href="#chevron-right"></use></svg>
          </a>
        </div>
        <div class="feature col">
          <div class="feature-icon d-inline-flex align-items-center justify-content-center text-bg-primary bg-gradient fs-2 mb-3">
            <svg class="bi" width="1em" height="1em"><use xlink:href="#toggles2"></use></svg>
          </div>
          <h3 class="fs-2">Our Calculations</h3>
          <p></p>txt
          <a href="#" class="icon-link d-inline-flex align-items-center">
            Click Here
            <svg class="bi" width="1em" height="1em"><use xlink:href="#chevron-right"></use></svg>
          </a>
        </div>
      </div>