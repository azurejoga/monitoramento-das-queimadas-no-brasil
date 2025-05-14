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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 915826fa-1caf-3b86-b8f0-0edfd611bbe9 | -13.98493 | -56.80446 | 2025-05-14 05:14:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f0a9a94b-8ac5-361d-b6f9-73989e486df5 | -10.73299 | -59.31941 | 2025-05-14 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f29b8b69-6b21-3dfe-aaeb-643959a33018 | -11.79178 | -47.36676 | 2025-05-14 05:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 483e44d9-fa5a-372c-a4c0-60221b3e6040 | -10.00289 | -62.58046 | 2025-05-14 05:14:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a0f2a15-27c5-36dd-8975-44bf368efd79 | -11.84717 | -57.85557 | 2025-05-14 05:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e78326ab-f502-307c-9f9d-e1acb21297e0 | -10.5231 | -59.38388 | 2025-05-14 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ae41e2e-e9e7-3a11-b469-a46962f6d514 | -13.07 | -52.0239 | 2025-05-14 05:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2bd5349a-99e0-3bf3-bb86-aa1f8dc960a0 | -13.93715 | -54.49204 | 2025-05-14 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16d09d69-735f-3553-8ad6-8ada07b99c09 | -13.96162 | -56.79275 | 2025-05-14 05:14:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a7370651-ad24-31b6-8e16-9684d64acb19 | -12.08802 | -54.57758 | 2025-05-14 05:14:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a146933-7c4b-321c-bbbb-3c5e7d8a989a | -13.62364 | -54.8811 | 2025-05-14 05:14:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 26ab8f7b-1c03-379f-a774-f970f31ab541 | -10.68794 | -57.59245 | 2025-05-14 05:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a770995f-48e9-3762-93d8-13041dff9d4e | -12.50111 | -57.2235 | 2025-05-14 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 274636e4-6e78-310c-bb57-86a957637407 | -10.47995 | -59.14996 | 2025-05-14 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a68cfcb-bfd7-3864-8750-a00040806e5a | -13.96628 | -56.78539 | 2025-05-14 05:14:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| cbd99065-3396-3372-962b-727a2a69e49d | -11.91332 | -54.40537 | 2025-05-14 05:14:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4dc3ab1b-28f1-384f-85f8-ccb42dbb24cc | -12.50564 | -57.2166 | 2025-05-14 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e966d60-b8b9-3b1a-a98f-0d39ec4a3ccd | -11.69481 | -48.82013 | 2025-05-14 05:14:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b155d15-409a-3979-afff-be370f68befd | -14.63584 | -45.10549 | 2025-05-14 05:14:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8b5e8eb6-ab41-33dd-9199-a61761760830 | -10.68349 | -57.59904 | 2025-05-14 05:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9799c39d-4d95-32ba-bb89-375794482d1c | -12.60813 | -56.02445 | 2025-05-14 05:14:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8ffc45b-4843-3cf6-bbe7-01758006bd87 | -11.66047 | -54.9547 | 2025-05-14 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d59f597-a441-3484-831a-c2727ff109ba | -13.09108 | -52.29276 | 2025-05-14 05:14:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f75ba54-bb55-3437-ab69-a7512dccb52f | -12.08419 | -54.57699 | 2025-05-14 05:14:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3383716a-44e4-339e-ad71-beb8cba58af3 | -12.68612 | -58.13443 | 2025-05-14 05:14:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b47e7f4-6cc7-31a8-aa69-3f84326cd7a0 | -12.50905 | -57.21714 | 2025-05-14 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ead82781-0113-3dab-97d2-87d187bde458 | -12.49827 | -57.21924 | 2025-05-14 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f97ff48-deab-30ef-9ed2-aa6d8f42fb19 | -12.68667 | -58.13084 | 2025-05-14 05:14:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b629fcc6-3e70-31d6-836e-89374dbc11c3 | -13.67481 | -53.94638 | 2025-05-14 05:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3b7bc4a7-f5b8-30e0-8765-d90f5897991a | -12.50395 | -57.22776 | 2025-05-14 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f28a4aaf-b95a-3b71-b481-c8bbf1122b66 | -9.5765 | -62.47205 | 2025-05-14 05:14:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 140ab064-e8c1-37b0-8e91-bf115fe4f5bf | -13.93966 | -54.49381 | 2025-05-14 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e27148c3-36c5-346b-b136-018395a27f1d | -12.72652 | -54.97468 | 2025-05-14 05:14:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dd5c1764-d3b2-3705-bf3d-5e067c818275 | -11.69128 | -48.81916 | 2025-05-14 05:14:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b2572f19-13b9-3846-9b9c-d6b80595a00b | -11.9153 | -54.4035 | 2025-05-14 05:14:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0e80137-128c-389e-a6f5-9def199f90cf | -12.49883 | -57.21552 | 2025-05-14 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f56cbd69-6643-3f4e-959a-60b46d52edc3 | -12.14953 | -48.01291 | 2025-05-14 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a2e30f71-3893-3e5e-acaf-9b896f55f81e | -10.68684 | -57.59958 | 2025-05-14 05:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4c0cbe8-cb90-3f04-b5ab-d0515c329a7b | -13.67887 | -53.94693 | 2025-05-14 05:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 52090e0c-0377-3d0e-aef4-03f615447bdf | -13.95871 | -56.78822 | 2025-05-14 05:14:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 06aae42a-256a-3d8f-9bd6-572a2c05f149 | -12.69002 | -58.13139 | 2025-05-14 05:14:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ac041f3-cf8f-36e6-9d3c-3ef57240d70a | -13.09167 | -52.28823 | 2025-05-14 05:14:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14dff2b8-01e0-31e5-9ddb-207230b2d7bb | -12.50167 | -57.21978 | 2025-05-14 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e764ddb6-1dc8-3410-81d0-04345f872df8 | -13.04998 | -53.71737 | 2025-05-14 05:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d65592d3-c94c-3aa0-aed2-f046949ee42d | -13.67531 | -53.94273 | 2025-05-14 05:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f664cf93-ea77-375b-95c1-bf18bff45855 | -13.95929 | -56.78426 | 2025-05-14 05:14:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9af9f2fa-9e30-310e-a2cb-a221c72a3876 | -13.95813 | -56.79218 | 2025-05-14 05:14:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3a4787a1-ecf4-3045-a006-b8f6dc5d98d8 | -13.5573 | -52.88347 | 2025-05-14 05:14:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 54709c57-4be6-3532-b523-4ff95933988e | -13.98143 | -56.80395 | 2025-05-14 05:14:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 13d95bd5-390a-3f08-9685-41c2b697011e | -12.86717 | -55.06445 | 2025-05-14 05:14:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7b1404ad-219a-3176-b982-eedde4c4b1af | -13.04947 | -53.72105 | 2025-05-14 05:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 143c4f2d-d5a5-3acf-91f4-9115ae1507e3 | -11.79123 | -47.37146 | 2025-05-14 05:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d095abeb-e599-352d-a537-7c8cdcad8dfb | -14.6286 | -45.1047 | 2025-05-14 05:14:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 08aac40a-a9e1-3f56-84b9-78f1359fafae | -10.73634 | -59.31995 | 2025-05-14 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a0072ec9-1d31-3bd2-9e15-6270911410bc | -14.63529 | -45.10034 | 2025-05-14 05:14:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 81832d57-b57b-3b5b-832b-3c7c9753113c | -13.9657 | -56.78936 | 2025-05-14 05:14:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 441cae20-df3e-3b85-aec0-20b8e5f5854a | -13.9622 | -56.78879 | 2025-05-14 05:14:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 94d73c00-2d03-353c-abd7-a4b8ed284aa8 | -10.68739 | -57.59602 | 2025-05-14 05:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5265f4ea-9ced-3e8b-bd1a-24f08e8414a5 | -12.5062 | -57.21288 | 2025-05-14 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c501ed9-2bc2-3bdc-b48e-bbc79216a98d | -14.63654 | -45.09809 | 2025-05-14 05:14:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93d8a8ae-45ed-3d00-a8fb-2314bc7e26fe | -13.16258 | -53.27553 | 2025-05-14 05:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 495d6e30-81d4-38d9-b905-835237f698ca | -11.69081 | -48.8229 | 2025-05-14 05:14:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7bf6aa9d-ea24-3144-8e78-cb1fcc8fc480 | -13.57205 | -52.87247 | 2025-05-14 05:14:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 250e59bb-bf94-33ae-bf62-00153d7ecea2 | -12.99815 | -48.88127 | 2025-05-14 05:14:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a34453c7-8669-3a7a-9087-926146ee0dce | -14.63454 | -45.10772 | 2025-05-14 05:14:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 40cabc3b-2613-320e-a6c4-98b617dbdfd7 | -12.29206 | -52.47268 | 2025-05-14 05:14:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 688f29bb-dd55-35fb-9fa0-06cbc687e71f | -13.06543 | -52.02321 | 2025-05-14 05:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da6323ae-9b27-37bf-badd-d064312bd9ca | -13.95755 | -56.79613 | 2025-05-14 05:14:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8f2b1caf-adee-363a-86c7-8a709141e49c | -14.62731 | -45.10695 | 2025-05-14 05:14:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed90078d-d154-34e6-918a-b25e68462644 | -12.68723 | -58.12726 | 2025-05-14 05:14:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7bb93f02-6e2f-3a3b-a096-542d90b4db9a | -12.50961 | -57.21342 | 2025-05-14 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c5893a3-4e7f-3035-866e-7e52794b43c2 | -13.06149 | -52.01775 | 2025-05-14 05:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd9c2fe7-01da-32f9-94e0-aa476f2f0e9f | -13.96861 | -56.7939 | 2025-05-14 05:14:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8bf8163a-fb11-3886-96b7-5e04006b2cc8 | -13.96919 | -56.78994 | 2025-05-14 05:14:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09983b52-ad9c-3f29-acf7-ce8018edf862 | -12.72718 | -54.97006 | 2025-05-14 05:14:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ed58843f-3881-3429-a7ac-a7c1930fa205 | -13.97793 | -56.80342 | 2025-05-14 05:14:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 818add70-5207-35d2-b296-18d1e785ec25 | -13.97851 | -56.79951 | 2025-05-14 05:14:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1a619425-5918-3617-b031-92c704e7395f | -13.05356 | -53.72158 | 2025-05-14 05:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a8d5d900-98a4-3005-bbb0-0c2dc6c41c05 | -21.46549 | -57.1476 | 2025-05-14 05:16:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91034097-140d-380e-b5f7-ee3450a40fd5 | -21.46485 | -57.15233 | 2025-05-14 05:16:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ddebada3-9f5d-3b46-8381-ec619b65d3ac | -21.60576 | -56.04061 | 2025-05-14 05:16:00 | NPP-375D | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e60ce800-3beb-3c38-b982-9e19989a57a4 | -21.60905 | -56.04659 | 2025-05-14 05:16:00 | NPP-375D | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 01aa30e7-2b80-320e-9d78-b7dee43b7a93 | -19.27091 | -54.99329 | 2025-05-14 05:16:00 | NPP-375D | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2037bce4-75db-3ad6-b849-4f86c6775d1a | -21.71816 | -55.37378 | 2025-05-14 05:16:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8a4286e0-6ec6-3430-9088-bb1cd8ea8171 | -25.09843 | -49.75992 | 2025-05-14 05:16:00 | NPP-375D | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a850ab9a-6423-376b-9210-4e5559ea1338 | -21.72229 | -55.37439 | 2025-05-14 05:16:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1d21db69-47db-303c-9952-b15046a8768d | -21.60508 | -56.04596 | 2025-05-14 05:16:00 | NPP-375D | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3c94b089-6d23-35f4-b288-6353daf05916 | -7.7298 | -46.3409 | 2025-05-14 05:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 773144ea-9f6f-34af-a3c1-752a365430e3 | -7.92953 | -61.55451 | 2025-05-14 05:33:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d23e62d-5b4d-367c-bf46-9776e59c5e0d | -9.57535 | -62.47195 | 2025-05-14 05:33:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d5dc548-6246-32dd-ac2b-3b5deb761ccb | -13.98067 | -56.80111 | 2025-05-14 05:36:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ba665138-2302-32bd-9819-5cfabb2efc12 | -12.7313 | -54.97026 | 2025-05-14 05:36:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4e7b4df-312a-39d3-a211-381e971e761b | -13.55927 | -52.87784 | 2025-05-14 05:36:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 112fff27-674b-3beb-9ae6-198ca75449f8 | -12.73083 | -54.97417 | 2025-05-14 05:36:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4c7a3b3-65b3-38d9-a6e8-e89c775eea6b | -13.97556 | -56.80053 | 2025-05-14 05:36:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 019eb88b-5cf9-3cd9-bd28-ddf0617cdf17 | -13.55801 | -52.8846 | 2025-05-14 05:36:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0abab747-fa48-353a-9ad0-8384bdfd0317 | -13.09196 | -52.29159 | 2025-05-14 05:36:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e34fe0f2-a2d1-3178-868f-74100528684e | -13.55863 | -52.88353 | 2025-05-14 05:36:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3aeab3f9-d50a-32e4-b047-c1fb2a6cf6ed | -12.87011 | -55.06015 | 2025-05-14 05:36:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d724da4-54e9-323e-8b6b-ee5c9b212a81 | -13.9603 | -56.79823 | 2025-05-14 05:36:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README11.md)
