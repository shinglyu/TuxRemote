if(!self.fetch) {
  alert('Your browser does not support the Fetch API, use Firefox Nightly instead.')
}

window.addEventListener('load', function(){
  for (var i = 1; i < 2; i++) {
    var btn = document.getElementById('btn' + i);
    btn.addEventListener('click', function(){
      fetch('do/open-mozilla').then(function(){
        console.log('Done: open-mozilla')
      });
    });
  }
})
