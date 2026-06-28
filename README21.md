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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 18a686a6-845d-3a2c-9106-b44d2e14518e | -12.16399 | -57.13381 | 2026-06-28 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1f423b85-3987-39cd-a49d-3cdef43c1d0b | -12.19255 | -52.88807 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f855fc5-3423-3273-a5cc-aff8f2348be3 | -11.21351 | -54.30779 | 2026-06-28 05:33:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 38.5 |
| a073d5af-5e71-302a-8eb5-d71624fe98b7 | -10.05205 | -59.11458 | 2026-06-28 05:33:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e309c27-a163-31c0-8d5b-7a7bdb3f6603 | -9.18593 | -58.07215 | 2026-06-28 05:33:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93b8f4df-ff02-380e-8bad-7e5fbf574e70 | -9.08575 | -59.41268 | 2026-06-28 05:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 617c22ab-8d56-3883-8d74-79a6a0530748 | -9.08632 | -59.40892 | 2026-06-28 05:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 344458c3-0ebd-3463-b4eb-19cf7c65de59 | -10.78365 | -54.10346 | 2026-06-28 05:33:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9084ab29-c748-35a1-b648-943eb58d57df | -12.17973 | -52.90352 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cf84c7f3-4035-344f-bcdc-b7012b377c47 | -11.91821 | -57.40669 | 2026-06-28 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 783c3dba-5e1c-3a2a-9438-0208398b2dcc | -10.63725 | -50.53578 | 2026-06-28 05:33:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6ab206d9-6ff4-3ae3-8324-af027b727067 | -11.66318 | -57.26215 | 2026-06-28 05:33:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| faf5ab26-9013-3214-bd0c-f224dc484b23 | -11.90997 | -57.12085 | 2026-06-28 05:33:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6026903a-772e-3e05-9016-390ec0b30538 | -12.18721 | -52.88732 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc09e64e-6cff-36d1-8128-83e4d9b1d706 | -12.20092 | -52.86491 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a03415e6-b96b-3a7f-966c-017ddbdd8bf0 | -10.93908 | -56.84987 | 2026-06-28 05:33:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 63f7b7cc-470d-3f74-90a6-cc12ac2e149d | -10.90527 | -56.85675 | 2026-06-28 05:33:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ed117be-deae-3b16-9175-a16b726f262c | -11.91749 | -57.41172 | 2026-06-28 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a54e25b-9536-3c9e-ac99-b8133c06fd8e | -12.22897 | -56.54909 | 2026-06-28 05:33:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 42c78f6e-6b84-311d-ba18-2485dfdfae14 | -12.17202 | -57.13503 | 2026-06-28 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ecdcc2c3-1523-33f9-8f67-90fc4a2c5061 | -12.19962 | -52.87518 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 205a22ba-40ae-377d-b3be-070921ca2a5d | -10.53414 | -53.70966 | 2026-06-28 05:33:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b27fbb4d-1b1d-3e52-8ce6-432091767d4a | -9.0344 | -61.3351 | 2026-06-28 05:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e819c2a4-607b-399d-afe7-566301d7223d | -12.28714 | -57.55595 | 2026-06-28 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 298e82ad-0726-393c-b3c3-0565cfd4bcb2 | -12.19876 | -52.88201 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7eab4b76-e419-3f93-a33d-ed03076ade05 | -11.8994 | -57.10863 | 2026-06-28 05:33:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6c82c32-b30f-31ad-baf7-4900b7f41e9c | -9.8119 | -62.95811 | 2026-06-28 05:33:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7abb6f4-487d-32e1-b47b-6865f95c5310 | -11.31013 | -53.94925 | 2026-06-28 05:33:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c7e57aba-5716-3b04-b5d1-b225e08dc6fd | -12.17704 | -57.15736 | 2026-06-28 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0e02a92-3ad6-3d3a-80f2-f3ade3129d4d | -10.53909 | -53.71037 | 2026-06-28 05:33:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a03ae840-9705-3f8f-b3b0-0a0156aa76d5 | -9.09379 | -59.40622 | 2026-06-28 05:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6494b362-306f-306e-9331-f9c73a37a5a1 | -11.5262 | -54.79824 | 2026-06-28 05:33:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 822c5255-0f1a-3bfb-a2e1-62daf6a22d29 | -9.09264 | -59.41376 | 2026-06-28 05:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 769de852-6b2f-37d0-9940-0ea26b077497 | -12.17779 | -57.1521 | 2026-06-28 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db610993-aa52-3bf7-922b-b1982cf78d1a | -12.18954 | -57.1614 | 2026-06-28 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e573dabf-89de-35cc-a736-e7936286e643 | -9.08977 | -59.40946 | 2026-06-28 05:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d9b2d6cf-cb3b-3cbd-847a-c1071bbb9f95 | -12.19919 | -52.8786 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1e95ae4e-5e7a-3c81-95aa-2a2bb85fbc6e | -10.93405 | -56.85627 | 2026-06-28 05:33:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b38aa0b0-10fd-3d63-9c59-77357941a6d0 | -9.08862 | -59.41698 | 2026-06-28 05:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bce34e6b-462b-318a-97a9-8e5a1ea1db6b | -12.17678 | -57.13039 | 2026-06-28 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e454954-6871-3d31-a155-de5498dfe36f | -11.5222 | -54.79273 | 2026-06-28 05:33:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| c0b1b248-a064-325b-95e8-8f78021f84a2 | -12.08454 | -52.00907 | 2026-06-28 05:33:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a899cd97-7bbc-321f-8e63-026a8959c3fa | -10.35894 | -50.18532 | 2026-06-28 05:33:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b6ebeb20-a60c-35d9-b8af-9ea5bc4c7af4 | -10.81095 | -56.61599 | 2026-06-28 05:33:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8b58104-f0f5-3011-9b90-41b10bb76a46 | -11.88068 | -57.11504 | 2026-06-28 05:33:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5392a304-3233-3254-81dd-0a2c3673fadb | -12.19534 | -52.90898 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0834ac27-cb0d-336e-b97c-7f096abc3cca | -9.03385 | -61.3386 | 2026-06-28 05:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 186364e7-1637-335a-bc83-e16d061ed2f7 | -12.08878 | -52.02128 | 2026-06-28 05:33:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8f010267-6402-3d27-9d61-92167c3dab48 | -11.21496 | -53.8215 | 2026-06-28 05:33:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| b07c91aa-7111-3a60-a9b9-1021f2bfe99b | -11.21419 | -54.30256 | 2026-06-28 05:33:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 6195e65f-8ef4-3438-915b-55c7020c799c | -12.08973 | -52.01364 | 2026-06-28 05:33:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5175bcaa-7dd7-3e50-9255-e5c3e159ae1c | -11.95105 | -54.09439 | 2026-06-28 05:33:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60a8bdab-ffbd-3a16-8139-b9bc0aa53ffc | -11.92075 | -58.66434 | 2026-06-28 05:33:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ced29259-ebef-3277-94f3-91e266c8f913 | -12.19042 | -52.90493 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 91877043-acde-3ba7-9205-507674f5a0c8 | -10.93505 | -56.84935 | 2026-06-28 05:33:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c4742af-37d3-3731-9d59-4a6ff68d9dc0 | -11.52154 | -54.79765 | 2026-06-28 05:33:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 464977e2-1126-3fc4-90ab-6801f3293dc6 | -11.92379 | -58.66919 | 2026-06-28 05:33:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 983fd076-fc5a-3411-b714-916a3492917a | -10.3938 | -50.14104 | 2026-06-28 05:33:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 55f72050-f524-345e-b014-60d68ad7a542 | -12.09445 | -52.02192 | 2026-06-28 05:33:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9d23f844-57d4-3e9b-a189-4c42a416e2a9 | -10.30356 | -57.13132 | 2026-06-28 05:33:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1eb91b8d-c179-3713-9226-e9f884871822 | -12.19833 | -52.88542 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 57d6b99e-09e3-3aaa-8cdd-6cd9ebc29daf | -11.21009 | -54.2966 | 2026-06-28 05:33:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 53375668-cd8f-3cb8-9b88-eeac0cb8041a | -9.09149 | -59.39811 | 2026-06-28 05:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e4a11b49-a84e-3407-afad-b63b0b6230d2 | -12.18764 | -52.88391 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| df81017d-1516-34dd-a00d-6bd379a1f455 | -11.65993 | -57.2564 | 2026-06-28 05:33:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a6dd4029-847b-313e-afbb-f7f63bfe5576 | -12.17439 | -52.90277 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ac5f8a8f-776f-38ac-ac87-84dae83d1fc7 | -12.08831 | -52.02507 | 2026-06-28 05:33:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e1557867-f790-3b80-a3de-7da16e8aa119 | -12.19384 | -52.87786 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4bce3516-ad4b-37fb-ac6b-9370ac457bec | -11.66389 | -57.25701 | 2026-06-28 05:33:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5d8b8ba8-d644-3e7e-a127-1ffc4f07ec03 | -9.0869 | -59.40515 | 2026-06-28 05:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4f6c06f8-38bc-35a7-b6c3-75d80e73f6c7 | -11.21001 | -53.82074 | 2026-06-28 05:33:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28dd128f-2480-309b-88ac-bdac240dfbc0 | -11.94673 | -58.61484 | 2026-06-28 05:33:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 658eeb27-a375-3c42-a440-8fa4b005bd9d | -12.20325 | -52.88952 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 63c0c433-ed6c-3dc8-9c2a-90486df14d25 | -10.35335 | -50.17962 | 2026-06-28 05:33:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 535d351c-259b-398f-b2dd-eb218a89189a | -12.15998 | -57.13321 | 2026-06-28 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16fe4c4e-f4a5-376d-bd57-47ab04caf6b1 | -12.17453 | -57.14621 | 2026-06-28 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d439c662-1ab4-35c9-9fd0-4365ace56068 | -12.18593 | -52.89749 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0335efb0-9da4-3cc0-9911-1bef39f0523b | -12.18508 | -52.90423 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8b1a7510-84e6-356f-a2ec-57865a1e902b | -12.17276 | -57.12978 | 2026-06-28 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d688558d-100e-35e5-a68f-5d9f7161f35d | -11.52686 | -54.79335 | 2026-06-28 05:33:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 00fcba45-1599-36b1-a6f6-8dccfcf9bcef | -9.03163 | -61.33108 | 2026-06-28 05:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9085ef4-5857-3bbc-a408-324fb02922ed | -10.77924 | -54.10737 | 2026-06-28 05:33:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f9cdfc7-eb75-3726-aa89-345644ce9524 | -12.27375 | -50.10447 | 2026-06-28 05:33:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6a8f5128-cfd1-3151-b38e-6c48d5ff374c | -12.23261 | -56.5536 | 2026-06-28 05:33:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bf6b113d-5c99-3ce8-8a46-71e9e9ac0d3d | -10.78296 | -54.10881 | 2026-06-28 05:33:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ede813a-e04f-327f-a035-f33529267d69 | -11.93939 | -58.61369 | 2026-06-28 05:33:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bed7f6fc-a3ce-33f7-8005-cab8a3ae591f | -11.86777 | -57.81112 | 2026-06-28 05:33:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63e688ff-4701-3c50-9178-8858a9f82263 | -12.1695 | -57.12386 | 2026-06-28 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b051edb-1efb-34aa-b7c5-bb8bb11d3a83 | -10.29645 | -57.12516 | 2026-06-28 05:33:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 4116e27d-eef8-3fbe-a854-099cd87c0506 | -12.20497 | -52.87592 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e8640e14-a920-35da-b8e5-87d9ee435809 | -10.05968 | -59.11174 | 2026-06-28 05:33:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ec5f657-a26b-3360-995f-fbf97ef50e73 | -12.19084 | -52.90157 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d786db4-66f1-3948-ae95-20acbbb9427b | -10.78408 | -54.10797 | 2026-06-28 05:33:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5932b78-ddc9-327e-95e7-228ecfb44128 | -11.35061 | -55.2695 | 2026-06-28 05:33:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2db6e494-fe67-36ef-a925-0292c4e47e47 | -12.18553 | -57.1608 | 2026-06-28 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 76b969e0-c52f-3f83-adbd-e9a55f6b0add | -12.08502 | -52.00522 | 2026-06-28 05:33:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac187490-d0e9-3829-ac51-ffea1e564119 | -12.17397 | -52.90615 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 43c09468-7eac-3bfa-82fd-176ceccaa3c1 | -9.08919 | -59.39 | 2026-06-28 05:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90f9c6d4-edea-300b-b939-1d5ae5947c07 | -12.20368 | -52.88614 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 13435246-88de-38b1-82f3-dfdceb5e38d1 | -10.30213 | -57.14131 | 2026-06-28 05:33:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README22.md)
