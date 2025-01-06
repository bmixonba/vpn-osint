import * as React from 'react';
import { DataGrid } from '@mui/x-data-grid';

const columns = [
  { field: 'id', headerName: 'ID', width: 90 },
  { field: 'fileName', headerName: 'File Name', width: 150 },
  { field: 'fileSize', headerName: 'File Size (MB)', type: 'number', width: 130 },
  { field: 'version', headerName: 'Version', width: 130 },
  { field: 'hash', headerName: 'SHA-256 Hash', width: 250 }
];

const rows = [
  { id: 1, fileName: 'vpn.exe', fileSize: 20, version: '1.0.0', hash: 'abc123...' },
  // More rows...
];

export default function ExecutableTable() {
  return (
    <div style={{ height: 400, width: '100%' }}>
      <DataGrid rows={rows} columns={columns} pageSize={5} checkboxSelection />
    </div>
  );
}

