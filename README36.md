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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a87dcd28-b7e0-3bf3-8d33-4ba3cbd8f87e | -4.18085 | -48.57413 | 2026-08-22 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e756a0a1-2569-3b56-85fc-f1485b0d3149 | -4.2766 | -50.88948 | 2026-08-22 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e6d72f4-fcc2-3e80-853b-37b18fceee09 | -6.33679 | -46.52588 | 2026-08-22 05:01:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29a44edc-ce41-3408-8c58-e0cbfd1941d9 | -6.87217 | -43.74196 | 2026-08-22 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 27a1776c-0ff8-36f9-95c7-405790cbe495 | -1.98568 | -56.46114 | 2026-08-22 05:01:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 98a90a4c-c266-3084-9034-ca8900ad7067 | -3.54193 | -48.18341 | 2026-08-22 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ced540e0-d5ad-39d5-975f-7c03eeaedbae | -6.87798 | -43.73936 | 2026-08-22 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5c881038-a959-3878-b81f-6af80286c60d | -5.47096 | -45.11764 | 2026-08-22 05:01:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 58bb88f0-87f5-32f4-9753-40c04ad3a12a | -1.98486 | -56.46619 | 2026-08-22 05:01:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dd3da58f-c564-3cfd-9799-6409bf84c535 | -6.8717 | -43.74531 | 2026-08-22 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5380319b-e771-3e23-89e7-5fcdecf92cbc | -3.8201 | -50.63477 | 2026-08-22 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 203b2b0f-f8ad-31ff-a4b8-e1b3336b3954 | -2.45511 | -48.56184 | 2026-08-22 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa1ffb79-6ca7-3763-bbb6-01b8421c1a0c | -6.34391 | -44.0789 | 2026-08-22 05:01:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a9aa7649-6afe-33b7-bdb5-8d03ab754909 | -2.89597 | -48.79557 | 2026-08-22 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fad78ce1-5d10-35f8-bc02-bbf8b04b8c20 | -2.45082 | -48.56549 | 2026-08-22 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 044bf2d4-38c4-3079-aa6b-363530256a1e | -2.45146 | -48.56128 | 2026-08-22 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29f1581c-3415-3624-9293-3c08e73195ba | -4.90465 | -45.24852 | 2026-08-22 05:01:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dfd54f2e-c1ae-3dd2-b37d-952c83ab2147 | -3.26936 | -49.52349 | 2026-08-22 05:01:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 57bd1a2a-f277-37b2-a443-d6032681ea1d | -1.42371 | -55.72131 | 2026-08-22 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c73bcf82-5434-34b7-b3b0-a30eb980f0c6 | -1.98883 | -56.46683 | 2026-08-22 05:01:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4455250-72d6-3417-af78-9a7e66e0d250 | -5.55149 | -43.42985 | 2026-08-22 05:01:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ebaa765f-2502-343d-acb7-c2dc2c58d7a1 | -5.82519 | -43.48862 | 2026-08-22 05:01:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7f26315f-574b-36a4-8f57-bbc3b2e66d43 | -4.94352 | -55.78421 | 2026-08-22 05:01:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd523c50-3319-33c6-ab2e-b9aa8554759b | -3.15095 | -51.0994 | 2026-08-22 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e4e92b4-9d64-335e-bb96-cc8572ecce18 | -3.53886 | -48.17825 | 2026-08-22 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7666ee1d-4984-38ef-b265-035411b7e057 | -2.893 | -48.79081 | 2026-08-22 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e18ddc99-febd-3880-b3cd-0b780411c6e9 | -4.93256 | -41.98144 | 2026-08-22 05:01:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d88647bd-a917-3274-a86d-e1390005147b | -4.1217 | -49.44547 | 2026-08-22 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c0b4a5f-d8f6-3b25-9c7c-db640a176d84 | -5.59227 | -43.99762 | 2026-08-22 05:01:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1fa6d91f-e42a-3106-9147-46fac173690f | -4.72142 | -44.33973 | 2026-08-22 05:01:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1cf306d8-362d-375e-9d87-abe69bd08caf | -3.82357 | -55.66691 | 2026-08-22 05:01:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| afaba0fe-9e6a-35a9-a3c3-9df73e2bf7b0 | -4.93803 | -41.97998 | 2026-08-22 05:01:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 871d327b-75f5-32e8-b808-86c39ee63008 | -5.53499 | -46.61334 | 2026-08-22 05:01:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cd42e149-e3c2-3704-9dbb-7f09961deffa | -5.59181 | -44.00075 | 2026-08-22 05:01:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0412b337-ce56-3feb-97e8-a979ffe95aac | -4.94421 | -55.77995 | 2026-08-22 05:01:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51ef943d-ddde-3ce3-a785-6c9388fa1924 | -3.68975 | -52.04063 | 2026-08-22 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5f9b60b-0be7-3996-994a-19253fb6e249 | -5.59136 | -44.00387 | 2026-08-22 05:01:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 972311c5-c98f-3b4e-ba1f-dc19487e8988 | -2.56695 | -47.24579 | 2026-08-22 05:01:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0ba372a4-0d83-3d2f-b775-b438a330fa28 | -3.82287 | -55.67115 | 2026-08-22 05:01:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27c2fa16-c799-34ee-a512-d79e745a23ea | -6.34519 | -44.07925 | 2026-08-22 05:01:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 53cece1b-561a-3ade-8b8f-6c17a7693a7a | -3.36046 | -50.6716 | 2026-08-22 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a3bac70-a4ff-384b-9cc7-ff42e826e377 | -5.47572 | -45.11841 | 2026-08-22 05:01:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d57ae2e7-09b0-3a60-bfa5-83bc89d1bbaf | -5.86085 | -47.75082 | 2026-08-22 05:01:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db88dc44-9951-37b8-832f-d1646097d7f8 | -5.86596 | -45.15054 | 2026-08-22 05:01:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 483abf3a-d54d-3648-9fb6-067cff592e95 | -3.53509 | -48.17764 | 2026-08-22 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef3f210b-424d-3d8d-ba36-f4cf8d9339ad | -4.93316 | -41.97733 | 2026-08-22 05:01:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a3ab4636-18ec-3969-afa2-3b25561569ba | -2.82898 | -48.64961 | 2026-08-22 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b071e91f-f51d-30fc-8350-c98ae4cc38a0 | -3.1515 | -51.09591 | 2026-08-22 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63df749b-c74b-355d-8bc4-bd8b4a8dc082 | -5.60877 | -45.71531 | 2026-08-22 05:01:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ddd1d9af-e64b-3fad-a442-92c805baeb84 | -5.59046 | -44.01 | 2026-08-22 05:01:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2cc8f809-4163-344e-8e14-d5cee24c3c96 | -2.45479 | -48.56344 | 2026-08-22 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b958bf25-2f3d-3490-90a7-26ce29b9d458 | -3.97843 | -47.20677 | 2026-08-22 05:01:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5b04e4c6-7034-348a-9e7e-9201d1421594 | -6.3487 | -44.08237 | 2026-08-22 05:01:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c58f955b-11cd-3ad4-a753-b0a6dfd791c2 | -2.89532 | -48.79974 | 2026-08-22 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 336e4eed-0e0f-3ca5-a8fb-6967ad5822f9 | -1.74551 | -55.25225 | 2026-08-22 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4b1d3c1-d63a-315f-8241-0e93588faadd | -5.59091 | -44.00694 | 2026-08-22 05:01:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c07785d0-34fc-3fb8-9b46-5b4b2edd2561 | -4.16264 | -42.44102 | 2026-08-22 05:01:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 332d6114-f58c-3bd7-bb06-d736b8f528a7 | -3.66219 | -55.5383 | 2026-08-22 05:01:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17b92035-8070-3e1f-a9d9-3d1523dea82b | -3.53439 | -48.1822 | 2026-08-22 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b43b0c71-697e-3537-81ab-d14161e86afd | -2.89662 | -48.79137 | 2026-08-22 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8681a2e-c29b-3491-ad2c-44714b5d2f34 | -4.96199 | -56.26398 | 2026-08-22 05:01:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 51fb6336-31ad-3a8d-958c-6cd9e3144ff5 | -5.79796 | -43.64336 | 2026-08-22 05:01:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5f531f7-dec9-3156-b7e8-4264431ee173 | -4.66193 | -43.13477 | 2026-08-22 05:01:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c66ac358-bfd6-308e-82d9-a8cc4058da1b | -1.42297 | -55.72602 | 2026-08-22 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e175ab25-3c87-37fd-b3ec-f08c0ca3ec13 | -6.87263 | -43.73861 | 2026-08-22 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| de561d4e-3ca8-3843-971b-619e0d4c4398 | -6.34437 | -44.07571 | 2026-08-22 05:01:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9f4b1e8f-578c-30a6-b4c4-7ae07165d314 | -6.88191 | -43.75024 | 2026-08-22 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 09786173-55e8-3d6a-837e-926384d73247 | -4.93843 | -41.98212 | 2026-08-22 05:01:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 16a3d6c5-7f1b-32ae-8335-8bb85c73f200 | -4.18191 | -49.39989 | 2026-08-22 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b01faf8f-c617-36c6-8b08-4fc15202dceb | -1.4216 | -55.72308 | 2026-08-22 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 50109313-cac1-3354-9c82-ad06c4bb1683 | -4.46899 | -55.3979 | 2026-08-22 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17f7eb70-dc26-3f3c-aab4-782423810bf3 | -4.95822 | -56.26345 | 2026-08-22 05:01:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 880e65be-cd39-3048-b437-eb22f448fad7 | -4.42472 | -55.44188 | 2026-08-22 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af9a6d30-0f9d-32c6-a771-35b0ab64ae92 | -4.06224 | -49.10795 | 2026-08-22 05:01:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0505825-c005-38a7-9e53-4822c98539f1 | -4.17647 | -48.57796 | 2026-08-22 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcb560ed-4769-3013-8c20-a4d24d403ee2 | -3.0369 | -48.40998 | 2026-08-22 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2d60d8dc-1f46-3073-aa2c-2e4e9cb1945a | -3.01584 | -51.06061 | 2026-08-22 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1cee1e9f-1e21-36e6-9c6c-af2e6a3eae7a | -6.87311 | -43.73521 | 2026-08-22 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d6214e0a-c2e6-304d-83bd-74cb9f0f9afe | -6.88237 | -43.74697 | 2026-08-22 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a8d03c5a-4074-3f86-9005-d1265e7dff4f | -4.46966 | -55.39376 | 2026-08-22 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 39325f6c-e6dc-3dc2-b0bd-8ca714996769 | -6.88726 | -43.75098 | 2026-08-22 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 223d4ee3-a34e-3db6-8f01-8539647fc34e | -4.90674 | -45.25065 | 2026-08-22 05:01:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6c75d26a-1207-3495-8186-7f287423bb22 | -4.93216 | -41.9793 | 2026-08-22 05:01:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c3baa5c3-cd29-3a5e-8d56-13c3bc817034 | -6.89305 | -43.74856 | 2026-08-22 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4b4a019f-e043-398b-bb99-cf760cc87cd0 | -5.60501 | -44.01837 | 2026-08-22 05:01:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b352a836-8860-3b87-a4c6-50595d56f87c | -6.35085 | -44.07653 | 2026-08-22 05:01:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8881d6e3-221e-3755-81ea-d431fde3a300 | -4.17914 | -48.57513 | 2026-08-22 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b0560457-c862-38fd-bccb-550f55cdad3c | -2.49968 | -48.13638 | 2026-08-22 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0c2bdc35-ebb8-3f69-8106-7e7eef53bf7d | -3.26584 | -49.52296 | 2026-08-22 05:01:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cd55e2b9-f6be-3963-a4e7-15c3c89192d3 | -4.12525 | -49.44602 | 2026-08-22 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fe42b90e-fe19-3b06-9eb1-a55bad03137f | -6.26059 | -62.51825 | 2026-08-22 05:04:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a9b4ca9-8692-3446-be05-0decaf6fe0c9 | -6.39164 | -54.95746 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 662c6428-28bd-30ab-b28b-068001cf1218 | -8.55419 | -54.85288 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0b1b73c7-7f06-3885-ac47-332cfb1f547f | -8.52715 | -54.82607 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 93386a06-907f-3848-b55b-8f84e08cb047 | -12.26235 | -43.13135 | 2026-08-22 05:04:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2263b370-3fe4-3ee0-a1d7-db0846e31e60 | -6.78765 | -58.64741 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 61a482be-ddd0-3ac5-bc03-84cacda42923 | -8.54213 | -55.30995 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eeda0997-2dcb-3845-99a1-6dfb8acdb11a | -10.77055 | -50.99826 | 2026-08-22 05:04:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3a9f402-677f-3de6-af2b-e84ec9bb2bd9 | -10.8097 | -50.97942 | 2026-08-22 05:04:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 686d8bf3-07e8-3711-8637-d6e1f9fff267 | -6.89962 | -55.71792 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README37.md)
