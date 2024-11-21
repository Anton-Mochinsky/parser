import React, { useState } from 'react';
import axios from 'axios';

const PartSearch = () => {
    const [partNumber, setPartNumber] = useState('');
    const [results, setResults] = useState([]);

    const handleSearch = async () => {
        try {
            const response = await axios.get(`/api/accounts/search/${partNumber}/`, {
                headers: {
                    Authorization: `Bearer ${localStorage.getItem('token')}`,
                },
            });
            setResults(response.data.results);
        } catch (error) {
            console.error('Error fetching part details:', error);
        }
    };

    return (
        <div>
            <h1>Part Search</h1>
            <input
                type="text"
                value={partNumber}
                onChange={(e) => setPartNumber(e.target.value)}
                placeholder="Enter part number"
            />
            <button onClick={handleSearch}>Search</button>
            <table>
                <thead>
                    <tr>
                        <th>Part Number</th>
                        <th>Price</th>
                        <th>Quantity</th>
                        <th>Link</th>
                    </tr>
                </thead>
                <tbody>
                    {results.map((result, index) => (
                        <tr key={index}>
                            <td>{result.part_number}</td>
                            <td>{result.price}</td>
                            <td>{result.quantity}</td>
                            <td>
                                <a href={result.link} target="_blank" rel="noopener noreferrer">
                                    View
                                </a>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default PartSearch;
