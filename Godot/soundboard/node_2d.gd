extends Node2D

func _on_bone_pressed() -> void:
	$AudioStreamPlayer2D.stream=preload("res://bone-crack.mp3")
	$AudioStreamPlayer2D.play()

func _on_cat_pressed() -> void:
	$AudioStreamPlayer2D.stream=preload("res://cat-laugh-meme-1.mp3")
	$AudioStreamPlayer2D.play()


func _on_death_pressed() -> void:
	$AudioStreamPlayer2D.stream=preload("res://death sound.mp3")
	$AudioStreamPlayer2D.play()


func _on_shot_pressed() -> void:
	$AudioStreamPlayer2D.stream=preload("res://mm2-hit-shooting.mp3")
	$AudioStreamPlayer2D.play()






func _on_h_slider_value_changed(value: float) -> void:
	# Converts a 0.0 - 1.0 slider value into the correct decibel scale
	$AudioStreamPlayer2D.volume_db = linear_to_db(value)
	#we need to connect the value from the function to the content for example to the volume db
