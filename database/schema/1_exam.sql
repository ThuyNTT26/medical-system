CREATE TABLE lichhen (
  id SERIAL PRIMARY KEY,
  benh_nhan_id INTEGER REFERENCES benhnhan(id),
  thoi_gian TIMESTAMP,
  noi_dung TEXT,
  ket_qua TEXT
);
