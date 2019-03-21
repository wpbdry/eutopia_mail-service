import graphene

import gmail

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
    msg = graphene.String()

    def mutate(self, info, recipient, subject, body):
        result = gmail.send_mail(recipient, subject, body)
        return SendMail(ok=result["ok"], msg=result["msg"])


class Mutations(graphene.ObjectType):
    send_mail = SendMail.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
