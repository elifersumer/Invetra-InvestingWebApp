const colors = require('tailwindcss/colors')
module.exports = {
        theme: {
          fontSize:{
            xxs: '.60rem',
            xs: '.75rem',
            lg: '1.25rem',
            sm: '.75rem'
          },
          colors: {
            white: colors.white,
            black: colors.black,
            red: colors.red,
            green: colors.green,
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
                  90:'90%'
              },
              height:{
                  btn: '25px',
                  flag: '20px',
                  icon:'40px',
                  myscreen: '980px'
              }
          }
        },
        variants:{
            extend:{
                backgroundColor:['active','focus'],
            }
        }
    }