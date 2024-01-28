package com.spring.DemoApp.Model;

public class SwimCoach implements Coach {
    @Override
    public String getDailyWorkout() {
        return "Swim 1k meters today, go on!";
    }
}
