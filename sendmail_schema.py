import graphene

import mailchimp

class Query(graphene.ObjectType):
    hello = graphene.String(argument=graphene.String(default_value="stranger"))

    def resolve_hello(self, info, argument):
        return 'Hello ' + argument


class SendMail(graphene.Mutation):
    class Arguments:
        recipient = graphene.String()
        subject = graphene.String()
        body = graphene.String()

    ok = graphene.Boolean()

    def mutate(self, info, recipient, subject, body):
        ok = mailchimp.send_mail(recipient, subject, body)
        return SendMail(ok=ok)


class Mutations(graphene.ObjectType):
    send_mail = SendMail.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
