from NewsPortal.models import *
User.objects.create_user('d1ams')
User.objects.create_user('admin')
user1 = User.objects.all()[0]
user2 = User.objects.all()[1]
Author.objects.create(user=user1)
Author.objects.create(user=user2)
Category.objects.create(category='Политика')
Category.objects.create(category='Спорт')
Category.objects.create(category='История')
Category.objects.create(category='Искусство')
author1 = Author.objects.all()[0]
author2 = Author.objects.all()[1]
Post1 = Post.objects.create(author=author1, name='Зенит распался', content='Питерский клуб Зенит вчера в 2 часа дня распался и прекратил свое существование')
from NewsPortal.resources import *
Post2 = Post.objects.create(author=author1,type=article,  name='Почему распался СССР?', content='Множество причин и предпосылок сподвигло развалу СССР')
Post3 = Post.objects.create(author=author2,type=article,  name='Какое послание зашифровал в своём гениальном полотне «Триумф смерти» Питер Брейгель Старший', content='Он писал масштабные мифологические и библейские сюжеты, а прославился своими картинами')
Politics = Category.objects.all()[0]
Sport = Category.objects.all()[1]
History = Category.objects.all()[2]
Art = Category.objects.all()[3]
Post1.category.add(Sport)
Post2.category.add(Politics, History)
Post3.category.add(Art)
user3 = User.objects.create_user('reader')
comment1 = Comment.objects.create(post=Post1, user=user3, content='Очень жаль(')
comment2 = Comment.objects.create(post=Post1, user=author1.user, content='Я рад что они распались!')
comment3 = Comment.objects.create(post=Post2, user=author1.user, content='Интересная статья!')
comment4 = Comment.objects.create(post=Post3, user=author2.user, content='И вправду в этой картине есть какое-то послание')
Post.objects.all()[0].dislike()
Post.objects.all()[0].dislike()
Post.objects.all()[0].dislike()
Post.objects.all()[0].dislike()
Post.objects.all()[0].dislike()
Post.objects.all()[1].like()
Post.objects.all()[1].like()
Post.objects.all()[1].like()
Post.objects.all()[1].like()
Post.objects.all()[1].like()
Post.objects.all()[1].like()
Post.objects.all()[1].like()
Post.objects.all()[1].like()
Post.objects.all()[1].like()
Post.objects.all()[1].like()
Post.objects.all()[2].like()
Post.objects.all()[2].like()
Comment.objects.all()[0].like()
Comment.objects.all()[0].like()
Comment.objects.all()[1].dislike()
Comment.objects.all()[2].dislike()
Comment.objects.all()[2].dislike()
Comment.objects.all()[2].dislike()
Comment.objects.all()[2].dislike()
Comment.objects.all()[3].dislike()
Author.update_rating(author1)
Author.update_rating(author2)
Author.objects.all().order_by('-rating')[0].user.username
Author.objects.all().order_by('-rating')[0].rating
bestpost = author1.post_set.all().order_by('-post_rating')[0]
bestpost.date
bestpost.author.user.username
bestpost.post_rating
bestpost.name
bestpost.preview()
bestpost.comment_set.all().values('date', 'user', 'rating', 'content')






