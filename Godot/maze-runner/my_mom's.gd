extends Area2D
func _on_body_entered(body):
	print("test")
	if body.name == "player":
		print("credit collected")
		queue_free()
