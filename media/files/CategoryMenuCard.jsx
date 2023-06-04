import {useState, useEffect} from 'react';
import { Box, styled } from "@mui/material";
import navigations from "data/navigations";

import CategoryMenuItem from "./CategoryMenuItem";
import MegaMenu1 from "./mega-menu/MegaMenu1";
import MegaMenu2 from "./mega-menu/MegaMenu2";
import axios from 'axios';


// styled component
const Wrapper = styled(Box)(({ theme, position, open }) => ({
  left: 0,
  zIndex: 98,
  right: "auto",
  borderRadius: 4,
  padding: "0.5rem 0px",
  transformOrigin: "top",
  boxShadow: theme.shadows[2],
  position: position || "unset",
  transition: "all 250ms ease-in-out",
  transform: open ? "scaleY(1)" : "scaleY(0)",
  backgroundColor: theme.palette.background.paper,
  top: position === "absolute" ? "calc(100% + 0.7rem)" : "0.5rem",
}));

// ===============================================================

// ===============================================================

const CategoryMenuCard = (props) => {
  const { open, position } = props;
  const megaMenu = {
    MegaMenu1,
    MegaMenu2,
  };

  const [category, setCategory] = useState([])

useEffect(() => {
  let isMounted = true;

  axios.get(`${process.env.NEXT_PUBLIC_BASE_URL}store/categories/`)
    .then((response) => {
      if (isMounted) {
        setCategory(response.data.data);
      }
    })
    .catch((err) => {
      console.log(err.response);
    });

  return () => {
    isMounted = false;
  };
}, []); // empty array as second argument

console.log("navi: ", category)
  return (
    <Wrapper open={open} position={position}>
      {category.map((item) => {
        let MegaMenu = megaMenu["MegaMenu1"];
        return (
          <CategoryMenuItem
            key={item.id}
            href={`/product/search/${item.name}/?id=${item.id}`}
            icon="MicroPhone"
            title={item.name}
            caret={!!item.menuData}
          >
            <MegaMenu data={"MegaMenu1" || {}} />
          </CategoryMenuItem>
        );
      })}
    </Wrapper>
  );
};
CategoryMenuCard.defaultProps = {
  position: "absolute",
};
export default CategoryMenuCard;
