# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6723c5a-a563-3f02-a726-926e3bf2d365 | -10.9624 | -45.09 | 2026-05-01 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 863cbc61-5ec0-321c-b0b1-62ecdddff7af | -10.9811 | -45.1104 | 2026-05-01 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 5e76af39-bd03-3d83-a136-a871f98c6167 | -10.9815 | -45.0874 | 2026-05-01 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 290.8 |
| 6f87bc25-0d6b-3089-90c9-7a086a355bad | -11.0006 | -45.0847 | 2026-05-01 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| e442136f-b693-3eac-bc97-768640c723a6 | -10.9819 | -45.0643 | 2026-05-01 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 135.2 |
| e807bab0-b2db-38dc-9c0a-0ff73f0131bf | -11.001 | -45.0617 | 2026-05-01 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 45.7 |
| a5bb033c-300e-39c6-b289-4bdf72d042d1 | -10.9732 | -45.064701 | 2026-05-01 00:29:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ff9e77ff-9668-3879-93dc-f631fd68c170 | -18.4877 | -51.6791 | 2026-05-01 00:29:00 | METOP-B | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ab19fd09-c90f-3799-9c42-557c88d18f3a | -10.9716 | -45.098999 | 2026-05-01 00:29:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1e467633-7a5a-32a8-bcff-cdbb05a01f3e | -13.3745 | -54.259899 | 2026-05-01 00:29:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9aca6d53-3f39-3d9c-8fd5-fd8d873a7367 | -16.382099 | -52.634701 | 2026-05-01 00:29:00 | METOP-B | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f413423e-7101-3319-9683-89f55c172a27 | -12.3463 | -49.9935 | 2026-05-01 00:29:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f6b4b4a5-135d-3b46-a7a8-bab97cb9edd0 | -12.0916 | -51.213799 | 2026-05-01 00:29:00 | METOP-B | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4a1c6864-840f-3261-aede-5af1be70f01b | -10.9869 | -45.078098 | 2026-05-01 00:29:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bf3d5f26-0024-3954-89a1-0f9262a44bb6 | -12.3789 | -54.7356 | 2026-05-01 00:29:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d4fbbb99-83f0-3975-9306-6f7eccfcc8f2 | -11.4406 | -55.095501 | 2026-05-01 00:29:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a45d1ff0-c81f-3287-9753-dff74897e18a | -19.4342 | -46.882702 | 2026-05-01 00:29:00 | METOP-B | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ef82aa0e-1969-3ea7-a67b-527abed466e3 | -12.9913 | -54.673199 | 2026-05-01 00:29:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cab56339-289b-30e4-ba34-9828af3aeb0d | -20.0618 | -50.452499 | 2026-05-01 00:29:00 | METOP-B | TURMALINA | SÃO PAULO | Brasil | 3555307 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 05b5b718-b07e-347a-8bd1-8ddd801bb881 | -12.3733 | -50.020302 | 2026-05-01 00:29:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ffa9e105-541d-3853-a676-1376592c1c35 | -11.4389 | -55.087799 | 2026-05-01 00:29:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0bcc98e2-feb1-31fd-897d-7115b987338f | -10.9829 | -45.062199 | 2026-05-01 00:29:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 78e5b6f2-39cd-3c58-90d1-b181878850fe | -21.141001 | -48.551102 | 2026-05-01 00:29:00 | METOP-B | TAIAÇU | SÃO PAULO | Brasil | 3553104 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 850778c2-0aeb-38fc-aa08-886634ca6c89 | -12.284 | -44.617199 | 2026-05-01 00:29:00 | METOP-B | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5f2a8425-4dc7-340b-abfc-d7594ba36a73 | -10.9812 | -45.096401 | 2026-05-01 00:29:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a65dc310-7bc9-3dc0-9298-df52eb371e3a | -10.9966 | -45.0756 | 2026-05-01 00:29:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8e078d8c-e36d-3155-88d9-b86819a72dd6 | -12.3751 | -50.028099 | 2026-05-01 00:29:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4c3503f3-20fb-3290-8d0d-02270144527d | -12.3867 | -50.0336 | 2026-05-01 00:29:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f668f5ed-ec10-3aca-a1a5-5483be022967 | -12.3805 | -54.743301 | 2026-05-01 00:29:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 372012b3-8209-3adf-8f8b-db4bc8abb6b6 | -20.0602 | -50.445202 | 2026-05-01 00:29:00 | METOP-B | TURMALINA | SÃO PAULO | Brasil | 3555307 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4cfe62a0-ed2f-3331-8816-d19cabc77cb3 | -12.3482 | -50.001301 | 2026-05-01 00:29:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 365b9261-3a2b-3a98-9138-81c7cbf7b57f | -18.0186 | -52.993599 | 2026-05-01 00:29:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 34961143-2262-3aab-9ba6-e93f05f24a12 | -13.3843 | -54.257702 | 2026-05-01 00:29:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cd057629-9ef5-3da8-a776-81c671035923 | -10.9676 | -45.083099 | 2026-05-01 00:29:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3df08f03-e542-388b-8c72-bf9d81a0e755 | -10.5484 | -44.325199 | 2026-05-01 00:29:00 | METOP-B | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b000d4a9-45a4-337f-8c6b-407d690447ba | -10.9636 | -45.067299 | 2026-05-01 00:29:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4174399d-7dd5-383e-b6e5-de9dc9e9ce52 | -10.9772 | -45.080601 | 2026-05-01 00:29:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| da541fd0-882d-3d37-92d0-f606c8c1b108 | -21.14121 | -48.55354 | 2026-05-01 00:33:00 | TERRA_M-M | TAIAÇU | SÃO PAULO | Brasil | 3553104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 63c39c39-842d-38db-8098-622621ef0873 | -18.48335 | -51.68525 | 2026-05-01 00:33:00 | TERRA_M-M | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 7a62e6b2-24bb-3001-adb3-9840639a8251 | -21.14296 | -48.56483 | 2026-05-01 00:33:00 | TERRA_M-M | TAIAÇU | SÃO PAULO | Brasil | 3553104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 7415140e-87b1-34ef-8478-2d2082e1fe3e | -19.43179 | -46.89244 | 2026-05-01 00:33:00 | TERRA_M-M | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 681c298f-1f0e-30c6-9feb-f5807088b4e4 | -18.48465 | -51.69454 | 2026-05-01 00:33:00 | TERRA_M-M | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bdd2df65-89d4-356b-bd80-764694df145d | -20.0521 | -50.46214 | 2026-05-01 00:33:00 | TERRA_M-M | TURMALINA | SÃO PAULO | Brasil | 3555307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| e896b1b2-25bc-3be6-b40f-0a1e68a2b8b4 | -20.0507 | -50.45242 | 2026-05-01 00:33:00 | TERRA_M-M | TURMALINA | SÃO PAULO | Brasil | 3555307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| b5d9db13-570a-39ea-8a8f-665519d642fe | -20.05968 | -50.45094 | 2026-05-01 00:33:00 | TERRA_M-M | TURMALINA | SÃO PAULO | Brasil | 3555307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| ac2422d8-165e-3776-a52c-4eececda6044 | -18.01901 | -53.00064 | 2026-05-01 00:33:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e899ec58-a180-3145-9696-3ffe32c4affd | -20.06108 | -50.46062 | 2026-05-01 00:33:00 | TERRA_M-M | TURMALINA | SÃO PAULO | Brasil | 3555307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 282a5270-8098-3c3c-a847-e9c049a368e3 | -12.98818 | -54.68038 | 2026-05-01 00:35:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 7326cb44-3309-3557-ba11-69001befb653 | -11.43429 | -55.10751 | 2026-05-01 00:35:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| f2e61ddb-3905-3f1e-99ea-9b313209fa06 | -16.37812 | -52.64491 | 2026-05-01 00:35:00 | TERRA_M-M | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 781965ed-bc01-3921-ab7c-8662398499c1 | -13.37538 | -54.27036 | 2026-05-01 00:35:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 2cc75297-dde4-308d-a1f5-1268d54299a9 | -11.43304 | -55.09803 | 2026-05-01 00:35:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 59861e04-59ec-359f-8af2-3d1b4bc2246b | -10.98421 | -45.10312 | 2026-05-01 00:35:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 155.3 |
| 75b0dbee-3177-3eee-aab4-f22c23a2d41a | -12.41031 | -52.15463 | 2026-05-01 00:35:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9aef4056-aa2e-3dd4-96af-ba39350595ae | -12.99721 | -54.67912 | 2026-05-01 00:35:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 819c8718-0dd5-3841-a4b9-2d64de5837a9 | -12.3733 | -50.03544 | 2026-05-01 00:35:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| fc58b1a0-d1c0-3831-a5ea-5deb3752fced | -12.37177 | -54.7519 | 2026-05-01 00:35:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 17.9 |
| ab54fb3d-ee9e-38b5-bbc8-4d4e44498caf | -16.42588 | -52.79631 | 2026-05-01 00:35:00 | TERRA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6757f365-3058-3978-93d7-e5da6b159748 | -10.9966 | -45.07762 | 2026-05-01 00:35:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.2 |
| dfb0fd00-e87a-3fc8-8167-032cc9384747 | -10.97904 | -45.07359 | 2026-05-01 00:35:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 262.3 |
| f0a8d591-fe0c-3ff8-958a-868822557924 | -10.9815 | -45.08011 | 2026-05-01 00:35:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 338.9 |
| 8a54dcc3-9eb8-3463-8ad2-b25fe8d38453 | -10.99414 | -45.07109 | 2026-05-01 00:35:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 37.8 |
| c0cbc012-88a9-3311-917f-a2aa98d02235 | -13.38431 | -54.26908 | 2026-05-01 00:35:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0902767c-68ab-39ea-81f2-c8d732a90105 | -12.33891 | -50.0109 | 2026-05-01 00:35:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 38281efb-dfa7-3439-ba4c-5db4e7b5aad3 | -10.98643 | -45.10953 | 2026-05-01 00:35:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 63dffc06-67d4-3929-abf9-b7e51890ed40 | -11.001 | -45.0617 | 2026-05-01 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.8 |
| ed25c61f-539a-3c0b-b7ae-7d51c64a188b | -10.9628 | -45.0669 | 2026-05-01 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 8c3d597d-440d-303c-b54b-ff3bd92daa86 | -10.9624 | -45.09 | 2026-05-01 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 6af5d14c-3214-3a40-b02d-678763b01639 | -11.0006 | -45.0847 | 2026-05-01 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.0 |
| b93691b9-bbaa-3c85-b644-baa4ce8d4f80 | -10.9815 | -45.0874 | 2026-05-01 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 222.5 |
| 93b54179-32f5-3f50-8959-558939c24283 | -10.9819 | -45.0643 | 2026-05-01 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 065254d9-df8e-35e2-a505-e1b13c8c3683 | -10.9815 | -45.0874 | 2026-05-01 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 189.6 |
| c25a70b8-6f20-3eae-88ab-cdb4c6f9e342 | -10.9819 | -45.0643 | 2026-05-01 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.4 |
| cbbb9f55-4f2f-303e-bd86-c8372ccf7ce6 | -11.001 | -45.0617 | 2026-05-01 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 4c9fe5f2-148b-3bc7-bbce-d545ce50e9c8 | -10.9624 | -45.09 | 2026-05-01 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.4 |
| cffa7b3e-6fe3-375e-ab4c-f4b9e885c148 | -11.0006 | -45.0847 | 2026-05-01 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 5201aad8-186a-37a7-a5d4-fe971dc5ab3c | -10.9811 | -45.1104 | 2026-05-01 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 75e31ccc-36cd-37ab-9c3f-fd4a2ccf4227 | -10.9819 | -45.0643 | 2026-05-01 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 6e02c824-e309-36d2-b744-232155024d0f | -11.0006 | -45.0847 | 2026-05-01 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.6 |
| b45a2c34-a321-3a0c-b928-25ed187b7138 | -10.9624 | -45.09 | 2026-05-01 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 4800b159-4c50-382e-824e-a9cfd1863e1d | -10.9815 | -45.0874 | 2026-05-01 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 154.9 |
| 1a554974-f45d-3dfc-8db1-b3abefd33af0 | -11.001 | -45.0617 | 2026-05-01 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.2 |
| ce5b4f2d-01d9-3325-b1db-f463820b2a16 | -18.486799 | -51.689098 | 2026-05-01 01:00:00 | METOP-C | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 945e9bd8-7e27-3cde-952c-49fecd39b476 | -10.5641 | -44.341301 | 2026-05-01 01:00:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4d2383ef-41a1-377c-a5f5-7d53779290c1 | -11.0017 | -45.084702 | 2026-05-01 01:00:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a2b4af26-dfb8-3f71-b151-49596a582fce | -13.3827 | -54.266499 | 2026-05-01 01:00:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9355a90b-822e-3241-b9d6-afd2f214d783 | -12.3492 | -50.003799 | 2026-05-01 01:00:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 075f0cc2-04a7-3496-a5c0-783bdd0791d8 | -13.3729 | -54.2686 | 2026-05-01 01:00:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5d95b0c3-5b0a-328f-aa18-9b18ca7d8127 | -10.9823 | -45.089802 | 2026-05-01 01:00:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d187222d-470c-32aa-8981-6b835536e7d7 | -11.4364 | -55.093201 | 2026-05-01 01:00:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8fb12262-060b-3c4e-bd46-f27e18f89340 | -12.3778 | -50.037701 | 2026-05-01 01:00:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2f933f10-0d76-3437-a73a-6cca6d8045d0 | -10.9881 | -45.071899 | 2026-05-01 01:00:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 804de2f6-d66d-3fe3-a2db-74d4f36ea147 | -10.992 | -45.087299 | 2026-05-01 01:00:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 21f6722d-e21a-3af6-ba51-d85a64203e70 | -10.9745 | -45.058899 | 2026-05-01 01:00:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 04a49d08-2071-3881-8f9f-07f6b557ea26 | -10.9784 | -45.074402 | 2026-05-01 01:00:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5a2a0c76-7cf8-31a7-b188-26553d6335ec | -20.0583 | -50.450802 | 2026-05-01 01:00:00 | METOP-C | TURMALINA | SÃO PAULO | Brasil | 3555307 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ed3b1699-5695-3086-a9a2-f6176c578b96 | -10.5596 | -44.3237 | 2026-05-01 01:00:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ed5e73d7-e2cd-3b35-ae0e-84a4537db3f0 | -10.9726 | -45.0923 | 2026-05-01 01:00:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6c0bb8f1-16a4-30fd-a917-adca213c95e4 | -10.9687 | -45.0769 | 2026-05-01 01:00:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1e09ea3a-de20-3f27-8f73-31ab35743d6f | -10.9842 | -45.0564 | 2026-05-01 01:00:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
