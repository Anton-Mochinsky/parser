import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import PartSearch from './components/PartSearch';

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/search" element={<PartSearch />} />
            </Routes>
        </Router>
    );
}

export default App;
