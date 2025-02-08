'use client'
import {
   Table
  ,TableContainer,
  TableHead,
  TableRow,
  TableCell,
  TableBody,
  Paper,
  TablePagination 
} from "@mui/material";

import React,
{
  useEffect,
  useState
} from "react";

import axios from "axios";

import {
  SPACEX_API_URL,
  convertUnixToReadableDate
} from "@/utils";

interface TableData{
  serial_no:number;
  time:number;
  name:string;
  status:boolean;
}

export default function Home() {

  const [data, setData] = useState<TableData[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [page, setPage] = useState(0);
  const [rowsPerPage, setRowsPerPage] = useState(5);

  useEffect(() => {
    const fetchData = async () => {
      try {
        axios.get(SPACEX_API_URL).then((response) => {
         const format_data:TableData[]=response.data.map((item:any,num:any)=>({
            serial_no:num+1,
            time:convertUnixToReadableDate(item.date_unix),
            name:item.name,
            status:item.success
         }))
         setData(format_data);
        }).catch((error) => {
          setError(error);
      } );
    }
    finally {
      setLoading(false);
    }
  }
    fetchData(); 
  }, []);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  const handleChangePage = (_event: unknown, newPage: number) => {
    setPage(newPage);
  };

  const handleChangeRowsPerPage = (event: React.ChangeEvent<HTMLInputElement>) => {
    setRowsPerPage(parseInt(event.target.value, 10));
    setPage(0);
  };
  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <main className="flex flex-col gap-8 row-start-2 items-center sm:items-start">
        <h1 className="text-4xl font-bold text-center">SpaceX Launch Details</h1>
        <TableContainer component={Paper} sx={{ maxHeight: 500 }}>
      <Table stickyHeader sx={{ minWidth: 650, borderCollapse: "collapse" }} aria-label="launch details table">
        <TableHead>
          <TableRow>
          <TableCell align="right" sx={{ border: "2px solid black",backgroundColor: "white",textAlign:"center",fontWeight: "bold" }}>No.</TableCell>
          <TableCell align="right" sx={{ border: "2px solid black",backgroundColor: "white",textAlign:"center",fontWeight: "bold" }}>Rocket Name</TableCell>
            <TableCell align="right" sx={{ border: "2px solid black", backgroundColor: "white",textAlign:"center",fontWeight: "bold" }}>Launch Date</TableCell>
            <TableCell align="right" sx={{ border: "2px solid black",fontWeight: "bold", backgroundColor: "white",textAlign:"center" }}>Launch Status</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {data.slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage).map((val) => (
            <TableRow key={val.serial_no}>
              <TableCell align="right" sx={{ border: "2px solid black" ,textAlign:"center"}}>{val.serial_no}</TableCell>
              <TableCell align="right" sx={{ border: "2px solid black" ,textAlign:"center"}}>{val.name}</TableCell>
              <TableCell align="right" sx={{ border: "2px solid black", backgroundColor: "white" }}>{val.time}</TableCell>
              <TableCell align="right" sx={{ color: val.status ? "green" : "red" ,border:"2px solid black",textAlign:"center"}}>
                {val.status ? "SUCCESS" : "FAILURE"}
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
      <TablePagination  sx={{ border: "2px solid black",backgroundColor: "wheat",position: "sticky", bottom: 0 }}
        rowsPerPageOptions={[5,10,15]}
        component="div"
        count={data.length}
        rowsPerPage={rowsPerPage}
        page={page}
        onPageChange={handleChangePage}
        onRowsPerPageChange={handleChangeRowsPerPage}
      />
    </TableContainer>
      </main>
    </div>
  );
}
