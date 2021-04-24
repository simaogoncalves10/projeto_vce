from modAL.models import ActiveLearner
from .query import Query


class ActiveLearner(ActiveLearner):
    def __init__(
        self,
        model,
        query_strategy: Query,
        X_training,
        y_training,
        **fit_kwargs,
    ) -> None:

        '''
        initiate Active learning instance with Deep Learning classifier,
        AL technic, X and Y training data
        '''
        super().__init__(
            model,
            query_strategy,
            X_training,
            y_training,
            **fit_kwargs,
        )

    def get_images(
        self,
        X_unlabeled,
    ):
        print("3")
        query_idx, instances = self.query(X_unlabeled)
        print("4")
        return instances

