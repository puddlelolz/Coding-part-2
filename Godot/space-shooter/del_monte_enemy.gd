extends Area2D

var speed = 300

func _process(delta):
	position.y += speed*delta #move downward constanlly



func _on_body_entered(body: Node2D) -> void:
	if body.name == "player":
		print("Crash! Game Over.")
		get_tree().reload_current_scene()
