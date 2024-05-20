import React from 'react'
import './Item.css'

const Item = () => {
  return (
    <div className='item'>Item
        <img src='https://images.unsplash.com/photo-1612838320302-3b3b3b3b3b3b' alt='item' />
        <p>{props.name}</p>
        <div className="item-price">
            <p>{props.price}</p>
            <button>Add to Cart</button>
            </div>
    </div>
  )
}

export default Item