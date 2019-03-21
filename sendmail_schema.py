import graphene

import gmail
import secret

class Query(graphene.ObjectType):
    hello = graphene.String(argument=graphene.String(default_value="stranger"))

    def resolve_hello(self, info, argument):
        return 'Hello ' + argument


class SendMail(graphene.Mutation):
    class Arguments:
        recipient = graphene.String()
        subject = graphene.String()
        body = graphene.String()
        password = graphene.String()

    ok = graphene.Boolean()
    msg = graphene.String()

    def mutate(self, info, recipient, subject, body, password):
        if password == secret.mail_service_password:  # Check password
            result = gmail.send_mail(recipient, subject, body)
            return SendMail(ok=result["ok"], msg=result["msg"])
        else:
            return SendMail(ok=False, msg="Authentication error")


class Mutations(graphene.ObjectType):
    send_mail = SendMail.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
