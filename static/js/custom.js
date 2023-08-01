
function calculateAge(date)
{
//  const now = new Date();
//  const diff = Math.abs(now - date );
//  const age = Math.floor(diff / (1000 * 60 * 60 * 24 * 365));
   var dob = new Date(date);
    //calculate month difference from current date in time
    var month_diff = Date.now() - dob.getTime();

    //convert the calculated difference in date format
    var age_dt = new Date(month_diff);

    //extract year from date
    var year = age_dt.getUTCFullYear();

    //now calculate the age of the user
    var age = Math.abs(year - 1970);
  document.getElementById('age').value = age;
}
