
module.exports = {
    theme: {
      colors: {
        white: '#FFFFFF',
        black: '#000',
        primary: 'rgba(10, 75, 94, 0.8)',
        secondary: 'rgba(10, 75, 94, 0.25)',
        darkblue: '#003545',
        orange: '#FF7C53',
        darkorange: 'rgba(255, 83, 30, 1)',
        gray: '#ccc'
      },
      fontFamily:{
        oswald:['Oswald', 'sans-serif']
      },
      extend:{
          width:{
              btn: '60px',
              navitems: '600px',
              icon: '40px',
              flag: '20px'
          },
          height:{
              btn: '25px',
              flag: '20px',
              icon:'40px'
          }
      }
    },
    variants:{
        extend:{
            backgroundColor:['active'],
            maxHeight:['focus']
        }
    }
}