extends Area2D


var speed = 300

func _process(delta):
	position.y -= speed*delta #move downward constanlly


func _on_area_entered(area: Area2D) -> void:
	if area.name.contains("ABC"):
		area.queue_free() #destroy the enemy
		queue_free() #destroy the laser
