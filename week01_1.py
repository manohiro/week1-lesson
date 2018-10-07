def make_bricks(small, big, goal):
    small_bricks = 1  # 小さいレンガの大きさ
    big_bricks = 5    # 大きいレンガの大きさ
  
    # 小さいレンガのみで作れる
    quotient_small = goal % small_bricks # goalと小さいレンガの余りを計算
    quotient_big = goal % big_bricks     # goalと大いレンガの余りを計算
    
    # 小さいレンガの余りが0で小さいレンガの大きさがgoal以上
    if (quotient_small == 0) and (small_bricks*small) >= goal:
        return True
   
    # 大きいレンガの余りが0で大きいレンガの大きさがgoal以上
    elif (quotient_big == 0) and (big_bricks*big) >= goal:
        return True
    
    # 小さいレンガと大きレンガの組み合わせ
    else:
        temp = goal - big_bricks*big
        # temp が0以上の場合
        if temp >= 0:
            # 足らない分が小さいレンガにある場合はTrue
            if small >= temp:
                return True
        else:
            # temp が0より小さい場合
            if small >= big_bricks - (((-1)*temp) % big_bricks):
                return True
  
    return False
