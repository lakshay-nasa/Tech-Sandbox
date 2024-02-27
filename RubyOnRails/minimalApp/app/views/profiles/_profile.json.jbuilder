json.extract! profile, :id, :name, :youtube, :twicth, :twitter, :email, :other, :created_at, :updated_at
json.url profile_url(profile, format: :json)
