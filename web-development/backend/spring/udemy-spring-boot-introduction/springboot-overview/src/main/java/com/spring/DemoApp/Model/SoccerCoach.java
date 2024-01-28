package com.spring.DemoApp.Model;

import org.springframework.context.annotation.Lazy;
import org.springframework.stereotype.Component;

@Component
@Lazy
public class SoccerCoach implements Coach{
    @Override
    public String getDailyWorkout (){
        return "Here is your Soccer workout for today !";
    }
}
