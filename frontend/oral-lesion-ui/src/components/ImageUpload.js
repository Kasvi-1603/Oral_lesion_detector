import React, { useState } from "react";

function ImageUpload({ onImageSelect }) {
  const [preview, setPreview] = useState(null);

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file && file.type.startsWith("image/")) {
      setPreview(URL.createObjectURL(file));
      onImageSelect(file); // Send file to parent
    } else {
      alert("Please select a valid image file.");
    }
  };

  return (
    <div style={{ margin: "20px 0" }}>
      <input type="file" accept="image/*" onChange={handleFileChange} />
      {preview && (
        <div style={{ marginTop: "10px" }}>
          <p>Preview:</p>
          <img
            src={preview}
            alt="Preview"
            style={{ maxWidth: "300px", borderRadius: "5px" }}
          />
        </div>
      )}
    </div>
  );
}

export default ImageUpload;
