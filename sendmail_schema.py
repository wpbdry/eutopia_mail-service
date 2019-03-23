import graphene
import graphql

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

    exitcode = graphene.Int()
    msg = graphene.String()

    def mutate(self, info, recipient, subject, body, password):
        if password != secret.mail_service_password:  # Check password
            return SendMail(exitcode=2, msg="authentication error")
        result = gmail.send_mail(recipient, subject, body)
        if result["exitcode"] == 0:
            return SendMail(exitcode=0)
        return SendMail(exitcode=3, msg=result["msg"])


class Mutations(graphene.ObjectType):
    send_mail = SendMail.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
