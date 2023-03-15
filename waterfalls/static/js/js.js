
window.onload = function () {
  document.body.classList.add('loaded_hiding');
  window.setTimeout(function () {
    document.body.classList.add('loaded');
    document.body.classList.remove('loaded_hiding');
  }, 500);
}

function F1() {
  let imgs = ['5.jpg', '6.jpg']
  let ln = imgs.length
  let rnd_int = Math.floor(Math.random() * ln)

  document.getElementById('wf').style =
    `background-image: url(/static/img/${imgs[rnd_int]});`
}
F1()

function F2(id) {
  console.log(id)
  let s = String(document.getElementById('srh').value)
  if (s !== '') { window.location.href = `/waterfalls/` + s + `/district/` + id + `/type/all/sorted/0/` }
}


function F3() {
  elem = document.getElementsByClassName('btn-sort')
  a = window.location.href
  url = a.split('/')[a.split('/').length - 2]
  url1 = a.split('/')[a.split('/').length - 4];
  url2 = a.split('/')[a.split('/').length - 6];

  for (let i in elem) {
    if (url.split('&').find(e => e == elem[i].id.split('-btn-0')[0] & e != '0') != undefined) {
      elem[i].style = 'background-color: grey;'
    }
    else if (url2 == elem[i].id.split('-btn-1')[0]) {
      elem[i].style = 'background-color: grey;'
    }
    else if (url1 == elem[i].id.split('-btn-2')[0]) {
      elem[i].style = 'background-color: grey;'
    }
    else if (url == elem[i].id.split('-btn-0')[0]) {
      elem[i].style = 'background-color: grey;'
    }
  }
}


function F4(id) {
  window.location.href = `/waterfalls/${id}/info`
}


function F55(id) {
  let a = window.location.href;
  let sorts = a.split('/')[a.split('/').length - 2];
  // arr = Array(sorts.split('&'))
  if (sorts.length > 18 | id == 13) {
    l = a.split('/').slice(0, a.split('/').length - 5) + "/" + a.split('/').slice(a.split('/').length - 5, a.split('/').length - 2)
    window.location.href = l.replace(/,/gi, '/') + '/0'
  }
  else {
    window.location.href = a.slice(0, a.length - 1) + `&` + id;
  }
}

function F66(id) {
  let a = window.location.href;
  l = a.split('/').slice(0, a.split('/').length - 6) + "/" + id + "/" + a.split('/').slice(a.split('/').length - 5, a.split('/').length - 1)
  window.location.href = l.replace(/,/gi, '/')
}

function F77(id, dist) {
  let a = window.location.href;
  l = `/waterfalls/all/district/` + dist + `/type/` + id + `/sorted/0/`
  window.location.href = l
}

function F88(div, cl, dk) {
  if (document.getElementById(dk).style.display != 'flex') {
    div.style = 'None'
    document.getElementById(dk).style.display = 'flex'

    for (let i in document.getElementsByClassName(String(cl))) {
      document.getElementsByClassName(String(cl))[i].style = 'none'
    }
  }
  else {
    div.style = 'background-color: rgb(71, 25, 115);'
    document.getElementById(dk).style.display = 'none'

    for (let i in document.getElementsByClassName(cl)) {
      document.getElementsByClassName(cl)[i].style = 'display: flex;'
    }
  }
}

function F99(id) {
  if (document.getElementById(id).style.display != 'flex') {
    document.getElementById(id).style.display = 'flex'
  }
  else {
    document.getElementById(id).style = 'none'
  }
}

