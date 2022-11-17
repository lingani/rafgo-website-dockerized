# Django imports
from django import forms
from django.forms import TextInput, Select, FileInput

# Third-party app imports
from ckeditor.widgets import CKEditorWidget

# Blog app imports
from blog.models.article_models import Article
from blog.models.category_models import Category


class ArticleCreateForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.filter(
                                      approved=True),
                                      empty_label="Select Category",
                                      widget=forms.Select(attrs=
                                                          {
                                                              "class": "form-control selectpicker",
                                                              "type": "text",
                                                              "name": "article-category",
                                                              "id": "articleCategory",
                                                              "data-live-search": "true"
                                                          }
                                      )
                            )
    body= forms.CharField(widget=CKEditorWidget(config_name="default", attrs={
               "rows": 5, "cols": 20,
               'id': 'content',
               'name': "article_content",
               'class': "form-control",
               }))


    class Meta:

        # Article status constants
        DRAFTED = "DRAFTED"
        PUBLISHED = "PUBLISHED"

        # CHOICES
        STATUS_CHOICES = (
            (DRAFTED, 'Draft'),
            (PUBLISHED, 'Publish'),
        )

        # Article featured constants
        FEATURED = "FEATURED"
        NOT_FEATURED = "NOT FEATURED"

        # CHOICES
        FEATURED_CHOICES = (
            (FEATURED, 'Featured'),
            (NOT_FEATURED, 'Not Featured'),
        )

        model = Article
        fields = ["title", "category", "image", "image_featured", "image_credit", "lead_paragraph", "body", "tags", "featured", "status"]
        widgets = {
            'title': TextInput(attrs={
                                     'name': "article-title",
                                     'class': "form-control",
                                     'placeholder': "Enter Article Title",
                                     'id': "articleTitle"
                                     }),

            'lead_paragraph': TextInput(attrs={
                                     'name': "article-title",
                                     'class': "form-control",
                                     'placeholder': "Enter Article Lead Paragraph",
                                     'id': "articleTitle"
                                     }),

            'image': FileInput(attrs={
                                        "class": "form-control clearablefileinput",
                                        "type": "file",
                                        "id": "articleImage",
                                        "name": "article-image"
                                      }

                               ),

            'image_featured': FileInput(attrs={
                                        "class": "form-control clearablefileinput",
                                        "type": "file",
                                        "id": "featuredImage",
                                        "name": "featured-image"
                                      }

                               ),

            'image_credit': TextInput(attrs={
                'name': "image_credit",
                'class': "form-control",
                'placeholder': "Example: made4dev.com (Premium Programming T-shirts)",
                'id': "image_credit"
            }),

            'tags': TextInput(attrs={
                                     'name': "tags",
                                     'class': "form-control",
                                     'placeholder': "Example: sports, game, politics",
                                     'id': "tags",
                                     'data-role': "tagsinput"
                                     }),
            'featured': Select(choices=FEATURED_CHOICES,
                             attrs=
                             {
                                 "class": "form-control selectpicker",
                                 "name": "featured", "type": "text",
                                 "id": "articleFeatured",
                                 "data-live-search": "true",
                                 "title": "Select Featured"
                             }),

            'status': Select(choices=STATUS_CHOICES,
                             attrs=
                             {
                                 "class": "form-control selectpicker",
                                 "name": "status", "type": "text",
                                 "id": "articleStatus",
                                 "data-live-search": "true",
                                 "title": "Select Status"
                             })
        }


class ArticleUpdateForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.filter(
                                      approved=True),
                                      empty_label="Select Category",
                                      widget=forms.Select(attrs=
                                                          {
                                                              "class": "form-control selectpicker",
                                                              "type": "text",
                                                              "name": "article-category",
                                                              "id": "articleCategory",
                                                              "data-live-search": "true"
                                                          }
                                      )
                                    )

    body = forms.CharField(widget=CKEditorWidget(config_name="default", attrs={
               "rows": 5, "cols": 20,
               'id': 'content',
               'name': "article_content",
               'class': "form-control",
               }))

    class Meta:
        # Article status constants
        DRAFTED = "DRAFTED"
        PUBLISHED = "PUBLISHED"

        # CHOICES
        STATUS_CHOICES = (
            (DRAFTED, 'Draft'),
            (PUBLISHED, 'Publish'),
        )

        # Article featured constants
        FEATURED = "FEATURED"
        NOT_FEATURED = "NOT FEATURED"

        # CHOICES
        FEATURED_CHOICES = (
            (FEATURED, 'Featured'),
            (NOT_FEATURED, 'Not Featured'),
        )
        
        model = Article
        fields = ["title", "category", "image", "image_featured", "image_credit", "lead_paragraph", "body", "tags", "featured", "status"]
        widgets = {
            'title': TextInput(attrs={
                'name': "article-title",
                'class': "form-control",
                'placeholder': "Enter Article Title",
                'id': "articleTitle"
            }),

            'lead_paragraph': TextInput(attrs={
                'name': "article-title",
                'class': "form-control",
                'placeholder': "Enter Article Lead Paragraph",
                'id': "articleTitle"
            }),

            'image_credit': TextInput(attrs={
                'name': "image_credit",
                'class': "form-control",
                'placeholder': "Example: made4dev.com (Premium Programming T-shirts)",
                'id': "image_credit"
            }),

            'featured': Select(choices=FEATURED_CHOICES,
                             attrs=
                             {
                                 "class": "form-control selectpicker",
                                 "name": "featured", "type": "text",
                                 "id": "articleFeatured",
                                 "data-live-search": "true",
                                 "title": "Select Featured"
                             }),

            'status': Select(choices=STATUS_CHOICES,
                             attrs=
                             {
                                 "class": "form-control selectpicker",
                                 "name": "status", "type": "text",
                                 "id": "articleStatus",
                                 "data-live-search": "true",
                                 "title": "Select Status"
                             }),


            'image': FileInput(attrs={
                "class": "form-control clearablefileinput",
                "type": "file",
                "id": "articleImage",
                "name": "article-image",
            }),

            'image_featured': FileInput(attrs={
                "class": "form-control clearablefileinput",
                "type": "file",
                "id": "featuredImage",
                "name": "featured-image",
            })

        }
