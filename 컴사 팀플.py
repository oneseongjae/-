#파동 관련 물리 문제 해결

# 파동의 v = 람다/주기
# 도플러효과
# 굴절

#파동의 속도,파장,주기

def wave():
    print("파동의 주기(진동수), 파장, 속도 중 구할 요소를 입력하시오")
    exfactor = ["주기", "진동수", "파장", "속도"]

    while True:
        factor = input("요소: ")
        if factor in exfactor:
            break
        else:
            print("다시 입력하시오")

    if factor == "주기":
        print("\n파동의 파장과 속도를 m와 m/s 단위로 입력하시오")
        wavelength = float(input("파장: "))
        velocity = float(input("속도: "))

        period = wavelength / velocity
        print("파동의 주기는 %.2f s입니다." % period)
    
    elif factor == "진동수":
        print("\n파동의 파장과 속도를 m와 m/s 단위로 입력하시오")
        wavelength = float(input("파장: "))
        velocity = float(input("속도: "))

        frequency = velocity / wavelength
        print("파동의 진동수는 %.2f Hz입니다." % frequency)
    
    elif factor == "파장":
        print("\n파동의 주기와 속도를 s와 m/s 단위로 입력하시오")
        cycle = float(input("주기: "))
        velocity = float(input("속도: "))

        wavelength = cycle * velocity
        print("파동의 파장은 %.2f m입니다." % wavelength)
    
    else:  
        print("\n파동의 파장과 주기를 m와 s 단위로 입력하시오")
        wavelength = float(input("파장: "))
        cycle = float(input("주기: "))

        velocity = wavelength / cycle
        print("파동의 속도는 %.2f m/s입니다." % velocity)


#도플러 효과

def doppler():
    print("관찰자와 파원 중 어떤 것이 이동하나요")
    exthing = ["파원", "관찰자"]

    while True:
        thing = input("대상 : ")
        if thing in exthing:
            break
        else:
            print("다시 입력하시오")
        
    if thing == "파원":
        frequency_sound = float(input("파원의 진동수를 입력하시오[Hz] : "))
        movingvelocity_sound = float(input("파원의 이동속도를 입력하시오[m/s] : "))
        velocity_sound = float(input("파동의 속도를 입력하시오[m/s] : "))

        frequency_observer = velocity_sound * frequency_sound / (velocity_sound - movingvelocity_sound)

        print("관찰자가 관측하는 파원의 진동수 : %.2f" % frequency_observer)
    else:
        frequency_sound = float(input("파원의 진동수를 입력하시오[Hz] : "))
        movingvelocity_observer = float(input("관찰자의 이동속도를 입력하시오[m/s] : "))
        velocity_sound = float(input("파동의 속도를 입력하시오[m/s] : "))

        frequency_observer = (velocity_sound + movingvelocity_observer) * frequency_sound / velocity_sound

        print("관찰자가 관측하는 파원의 진동수 : %.2f" % frequency_observer)


#스넬의 법칙

def snell():
    import math

    print("빛이 굴절할 때 구할 요소를 입력하시오(각도, 굴절률)")
    exfactor = ["각도", "굴절률"]

    while True:
        factor = input("요소 : ")
        if factor in exfactor:
            break
        else:
            print("다시 입력하시오")

    if factor == "각도":
        factor_angle = input("입사각 또는 굴절각 중 무엇을 구하나요 : ")
        if factor_angle == "입사각":
            angle_out_degree = float(input("굴절각을 입력하시오 (도): "))
            angle_out_radian = math.radians(angle_out_degree)

            refractive_index_in = float(input("입사하는 매질의 굴절률을 입력하시오: "))
            refractive_index_out = float(input("굴절되는 매질의 굴절률을 입력하시오: "))

            sin_value = refractive_index_out * math.sin(angle_out_radian) / refractive_index_in

            if -1 <= sin_value <= 1:
                angle_in_radian = math.asin(sin_value)
                angle_in_degree = math.degrees(angle_in_radian)
                print("입사각은 %.2f도입니다." % angle_in_degree)
            else:
                print("계산된 값이 물리적으로 불가능합니다. 입력값을 확인하세요.")

        elif factor_angle == "굴절각":
            angle_in_degree = float(input("입사각을 입력하시오 (도): "))
            angle_in_radian = math.radians(angle_in_degree)

            refractive_index_in = float(input("입사하는 매질의 굴절률을 입력하시오: "))
            refractive_index_out = float(input("굴절되는 매질의 굴절률을 입력하시오: "))

            sin_value = refractive_index_in * math.sin(angle_in_radian) / refractive_index_out

            if -1 <= sin_value <= 1:
                angle_out_radian = math.asin(sin_value)
                angle_out_degree = math.degrees(angle_out_radian)
                print("굴절각은 %.2f도입니다." % angle_out_degree)
            else:
                print("계산된 값이 물리적으로 불가능합니다. 입력값을 확인하세요.")

    elif factor == "굴절률":
        angle_in_degree = float(input("입사각을 입력하시오 (도): "))
        angle_in_radian = math.radians(angle_in_degree)

        angle_out_degree = float(input("굴절각을 입력하시오 (도): "))
        angle_out_radian = math.radians(angle_out_degree)

        refractive_index_in = float(input("입사 매질의 굴절률을 입력하시오: "))

        sin_out = math.sin(angle_out_radian)
        if sin_out == 0:
            print("굴절각이 0도 또는 180도일 때 굴절률을 구할 수 없습니다.")
        else:
            refractive_index_out = (math.sin(angle_in_radian) * refractive_index_in) / sin_out
            print("굴절되는 매질의 굴절률은 %.2f입니다." % refractive_index_out)


