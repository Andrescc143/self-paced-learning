package com.spring.DemoApp.config;

import com.spring.DemoApp.Model.Coach;
import com.spring.DemoApp.Model.SwimCoach;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class CoachConfig {
    @Bean
    public Coach swimCoach (){
        return new SwimCoach();
    }
}
