extends Node2D
	
	


func _on_print_button_pressed() -> void:
	$HBoxContainer/RightSide/NameLabel.text=$HBoxContainer/LeftSide/NameInput.text
	$HBoxContainer/RightSide/AgeLabel.text="Age:"+$HBoxContainer/LeftSide/AgeInput.text
	$HBoxContainer/RightSide/PowerLabel.text="Power:"+$HBoxContainer/LeftSide/PowerInput.text
