import React from "react";
import axios from "axios";
import { useParams } from "react-router";
import { Container, Row, Col } from "reactstrap";

import { API_URL } from "../Constants";
import { nonEmptyArray } from "check-types";

export default function Berry() {
    const { id } = useParams();
    const [berry, setBerry] = React.useState(null);

    React.useEffect(async () => {
        const res = await axios.get(API_URL + `berries/${id}/`);
        setBerry(res.data);
    }, [setBerry]);

    if (!berry) {
        return null;
    }

    return (
        <Container>
            <Row>
                <Col md="2">
                    <img className="image-fluid" src={berry.image} alt="Berry product image" width="200" />
                </Col>
                <Col md="10">
                    <h3>{berry.title}</h3>
                    <p>{berry.description}</p>
                    <p className="fs-2 fw-bold">{berry.price} {berry.price_currency}</p>
                    <p>Berries left: {berry.quantity}</p>
                    <p>Berries weight: {berry.weight}kg</p>
                </Col>
            </Row>
        </Container>
    );
}