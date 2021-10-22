const colors = require('tailwindcss/colors')
module.exports = {
        theme: {
          colors: {
            white: colors.white,
            black: colors.black,
            red: colors.red,
            primary: 'rgba(10, 75, 94, 0.8)',
            secondary: 'rgba(10, 75, 94, 0.25)',
            blue:'#007395',
            darkblue: '#003545',
            orange: '#FF7C53',
            darkorange: 'rgba(255, 83, 30, 1)',
            gray: colors.gray,
            lightblue: 'rgba(10, 75, 94, 0.05)'
          },
          fontFamily:{
            oswald:['Oswald', 'sans-serif']
          },
          extend:{
              width:{
                  btn: '60px',
                  navitems: '600px',
                  icon: '40px',
                  flag: '20px',
              },
              height:{
                  btn: '25px',
                  flag: '20px',
                  icon:'40px',
                  myscreen: '1280px'
              }
          }
        },
        variants:{
            extend:{
                backgroundColor:['active','focus'],
            }
        }
    }