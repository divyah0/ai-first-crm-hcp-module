
import React, { useState } from "react";

function App() {

  const [doctor,setDoctor] = useState("");
  const [notes,setNotes] = useState("");
  const [date,setDate] = useState("");

  const submitData = async () => {
    await fetch("http://localhost:8000/log_interaction",{
      method:"POST",
      headers:{"Content-Type":"application/json"},
      body:JSON.stringify({
        doctor_name:doctor,
        discussion_notes:notes,
        meeting_date:date
      })
    });

    alert("Interaction logged");
  };

  return (
    <div style={{padding:40,fontFamily:"Inter"}}>
      <h2>Log Doctor Interaction</h2>

      <input
      placeholder="Doctor Name"
      onChange={(e)=>setDoctor(e.target.value)}
      /><br/><br/>

      <textarea
      placeholder="Discussion Notes"
      onChange={(e)=>setNotes(e.target.value)}
      /><br/><br/>

      <input
      type="date"
      onChange={(e)=>setDate(e.target.value)}
      /><br/><br/>

      <button onClick={submitData}>Submit</button>

    </div>
  );
}

export default App;
