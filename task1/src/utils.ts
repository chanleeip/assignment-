
const SPACEX_API_URL=process.env.SPACEX_DATA_URL || 'https://api.spacexdata.com/v4/launches';

const convertUnixToReadableDate = (unixTimestamp:number) => {
    return new Date(unixTimestamp * 1000).toLocaleDateString("en-IN", {
      weekday: "long",   
      year: "numeric",   
      month: "long",     
      day: "numeric",    
    });
  };

export {SPACEX_API_URL,convertUnixToReadableDate}