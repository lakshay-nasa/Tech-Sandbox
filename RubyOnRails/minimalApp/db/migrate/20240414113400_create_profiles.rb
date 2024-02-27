class CreateProfiles < ActiveRecord::Migration[7.1]
  def change
    create_table :profiles do |t|
      t.string :name
      t.string :youtube
      t.string :twicth
      t.string :twitter
      t.string :email
      t.string :other

      t.timestamps
    end
  end
end
