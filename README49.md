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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02b3652d-9df5-33a9-ae41-1de00871a736 | -9.71008 | -51.97284 | 2025-08-19 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| b4f677fa-d11f-301b-a098-8cf11d0d509a | -5.97813 | -61.36286 | 2025-08-19 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ca63337-51b3-326e-8701-9b2d64ebf22d | -9.19601 | -59.62544 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0ce6613b-98a8-33ad-a23c-49b72f20b3f1 | -7.97521 | -55.30355 | 2025-08-19 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7b3dd155-7ba9-3b66-ab4c-f93c4cb7d68a | -9.34265 | -48.52312 | 2025-08-19 05:16:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 539fc18e-c39c-357e-a555-51a71baae835 | -9.72546 | -51.969 | 2025-08-19 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 239c566f-c0d8-3c3c-859d-962a2c371740 | -8.77091 | -50.01699 | 2025-08-19 05:16:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8517ef4-7b69-36c7-af63-dbc3dfbbcb79 | -8.70322 | -50.69456 | 2025-08-19 05:16:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36f26364-c1c4-397a-997b-b0ddde73ec1f | -6.49036 | -53.39037 | 2025-08-19 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6813b4c0-ea29-399c-a5f6-438113072416 | -5.87072 | -48.11624 | 2025-08-19 05:16:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7aa9bdaa-e81a-355a-a809-821ac8eec029 | -8.97196 | -60.49994 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6a3297ab-9606-326c-9294-02a4fefce943 | -9.04225 | -50.17941 | 2025-08-19 05:16:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4231bfce-f414-33f1-96ce-bc8ca62c2a50 | -12.99134 | -56.86215 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 517366fc-c567-362d-a232-9eaed2439e47 | -16.62305 | -51.36313 | 2025-08-19 05:18:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1c034f7-a176-3141-a049-7d74756f8cf2 | -13.73709 | -52.0251 | 2025-08-19 05:18:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72dbcbb8-d5d8-3844-9875-f31e50f726a6 | -12.97615 | -56.84828 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a4534be7-c723-3f14-955b-b11849a75ee2 | -12.98645 | -56.84312 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af0b2f97-0fe3-31ca-b43c-8772aaeae096 | -13.44138 | -56.8977 | 2025-08-19 05:18:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 25e6300a-db17-3ebb-85dc-efb808dd3c74 | -14.973 | -54.81075 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 51ddebe4-309f-33ab-af4b-cf6d6de2297d | -16.8117 | -49.37253 | 2025-08-19 05:18:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d387e2d4-c868-3668-b801-0f7b67cde9d0 | -14.64748 | -54.90671 | 2025-08-19 05:18:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19f3e903-8b7f-38eb-a9b9-cdc661cd8fc4 | -12.99451 | -56.83969 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c450f69-b9c8-325b-88fd-afc020ccb307 | -13.16317 | -54.9416 | 2025-08-19 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6623a89-4f37-3ccd-9472-cfa5a84f8401 | -14.86861 | -48.04301 | 2025-08-19 05:18:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 396ac7f3-c6c8-3723-9e1e-086946b0c7a7 | -14.87405 | -48.05596 | 2025-08-19 05:18:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a5bd92cc-025f-3294-92c3-c0baf82eb663 | -13.16787 | -54.93835 | 2025-08-19 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a550ae3f-8ea5-322f-9204-a67a29d88407 | -13.30773 | -50.81734 | 2025-08-19 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| da129549-4a47-3f1c-8a44-365552bf2853 | -13.02664 | -56.8535 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70e5cfaa-e0dc-3345-a630-81a9cb04e7f0 | -12.98763 | -56.86161 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1ec38a9-c831-36ca-8f0b-bd7ff9971152 | -15.02526 | -54.81513 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cfd0dc75-17e1-3f7d-9e24-fd5453d956c5 | -12.97777 | -56.85103 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6743af44-ffdc-318f-bcfe-b46d63c4c8d3 | -10.44265 | -64.4559 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e9b75926-80fa-3e24-b762-2db50a9df9f7 | -12.50932 | -57.78187 | 2025-08-19 05:18:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9d93c49-01e3-3019-9c38-1cd61ba1884b | -13.1689 | -54.93063 | 2025-08-19 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a17dc48-969e-344c-8f42-8a40c10f0640 | -13.14467 | -57.14982 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9f0a286-3873-3334-ab6c-938941426253 | -8.36826 | -70.14455 | 2025-08-19 05:18:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 879156a3-6ced-3aa6-bb16-dfc93f4609bb | -11.85908 | -51.58487 | 2025-08-19 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2acbefea-4a4b-37ba-a91d-57bf5923739d | -11.86058 | -51.57265 | 2025-08-19 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d6b1143-58c9-38da-9906-f308b6009881 | -9.51217 | -60.52237 | 2025-08-19 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4804771d-5d7b-3531-afbd-1397c818b5ee | -12.9784 | -56.84651 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b1182a2-3f7f-3888-a273-cf4c8efd064f | -13.16369 | -54.93776 | 2025-08-19 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f8020d9-e876-36cb-8445-aa273cfded92 | -13.14408 | -57.15237 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4cef8915-93f8-359b-b768-eea561c4edb7 | -13.01 | -56.8373 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 18c5773c-f3df-3098-b8d4-481b13daa474 | -13.00501 | -56.84579 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d4ec99b-eca6-3d71-b016-9434a6f5aaac | -12.9833 | -56.86554 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5cff85fd-e463-3763-b924-68b8caa862e1 | -12.97789 | -56.86228 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6b08fe78-12bc-35ce-8e3f-f958130ebb80 | -13.73746 | -52.02205 | 2025-08-19 05:18:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d1758fe-d12a-3b8e-997f-a1939c67a3e3 | -9.47966 | -63.51449 | 2025-08-19 05:18:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d5fe17c-d7be-3b64-84ab-a549dfc3e817 | -12.98393 | -56.86108 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3894bb20-1343-3edc-ae71-ae06564c5796 | -14.64268 | -54.91019 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c7c0efd6-8e7d-3f1b-87ff-9929fc4bb785 | -12.97549 | -56.85279 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4c4afc27-c038-3bc4-bccd-e21021677b2d | -12.97245 | -56.8477 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f4621fcd-d97d-3f22-ad2c-671e1c05c45c | -12.99071 | -56.86661 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93af0df2-b06e-35c1-9e8b-a34904dc1765 | -13.30863 | -50.80994 | 2025-08-19 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1081569-30a7-3cc6-a613-1969aa7b54f2 | -10.44181 | -64.46085 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6154926c-4caa-3701-b1a9-cb0bc7c5de0f | -13.16838 | -54.93449 | 2025-08-19 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| daae9bee-3dd7-3979-90e2-feca6669a058 | -13.01436 | -56.83331 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2389a313-e445-3394-8cf5-3e0f4d07f1ab | -13.16735 | -54.9422 | 2025-08-19 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6932c688-1e19-32ac-82a5-289bb042874a | -13.14833 | -57.15034 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb26b4a9-66ea-3242-9638-517daf8ec205 | -12.97651 | -56.86 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3785fe99-01bc-3507-b0c6-6fc299c66cc7 | -11.31308 | -55.22367 | 2025-08-19 05:18:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 179a9d0b-b168-3075-a469-6496741aa12d | -12.98455 | -56.85662 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87facace-8f04-3e04-adac-4c469a1b1390 | -13.13545 | -57.16177 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96c92295-b2f7-352a-bd9f-3da7864dd0fb | -10.16874 | -69.02015 | 2025-08-19 05:18:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1203f029-6c1d-3fe0-9591-372ae08edbe3 | -15.03759 | -54.82181 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 44562252-f45b-3c52-bd02-d2e0474b3395 | -15.02097 | -54.81426 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1624dd06-aa31-3e71-ada1-e382b0b632d6 | -14.84488 | -48.0767 | 2025-08-19 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f8db9280-26ab-3639-85a5-ede798ded701 | -9.52102 | -60.53104 | 2025-08-19 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7ec73ef6-c643-3847-b7a3-8e63914801b7 | -12.5064 | -57.77731 | 2025-08-19 05:18:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16f60cc2-f373-339c-9e27-26a73bd08cba | -11.85983 | -51.57878 | 2025-08-19 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9be133fc-314b-30ca-8119-03b26a9ead53 | -13.00693 | -56.83224 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5fbcafa-c519-3ff9-82e4-01649927e172 | -15.7949 | -48.22483 | 2025-08-19 05:18:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57269276-eaff-3278-830c-1e56bd136441 | -13.13671 | -57.15312 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7936d9d-5832-33f1-865a-40d989d98014 | -13.00936 | -56.8418 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c7045f4-310d-3605-95d8-6af5ad546f53 | -8.7598 | -64.19946 | 2025-08-19 05:18:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f679165-0872-351d-b38f-7f524e80b5a3 | -9.37656 | -61.53244 | 2025-08-19 05:18:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7af80fe-c908-345e-a8ba-ed4f445c60c7 | -11.11568 | -61.66711 | 2025-08-19 05:18:00 | NOAA-20 | PRESIDENTE MÉDICI | RONDÔNIA | Brasil | 1100254 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 926d589f-4c87-34bd-848a-5b4c985adb16 | -15.02679 | -54.80328 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2ae16ba-5b91-392c-b89c-700ef6a5293b | -13.43973 | -56.85557 | 2025-08-19 05:18:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c883162f-3000-34e5-95bb-3b1b0da3f8f3 | -14.87267 | -48.06931 | 2025-08-19 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8e34526-9a23-3bdd-9ae2-39f1ca5c62a3 | -15.04244 | -54.81839 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 817aaefb-a2de-3066-84e1-b1a9b309188a | -13.17413 | -54.95508 | 2025-08-19 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a1bd2ad-e1a9-3f33-a87c-449108f61875 | -11.31406 | -55.21665 | 2025-08-19 05:18:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bbcac5c8-05a7-33e6-8b3b-54bb260bd9b6 | -10.29527 | -59.45753 | 2025-08-19 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5460c37d-2620-3683-829e-3ebdb598ce7c | -15.15923 | -48.78292 | 2025-08-19 05:18:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ec6bc0dc-2a2f-389b-af03-a8a7ab94bb8d | -13.31551 | -50.79951 | 2025-08-19 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47440c97-9447-3e02-b8f8-0afc3f4b7331 | -12.3 | -50.02196 | 2025-08-19 05:18:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 66f5e6a9-d16a-3408-99df-ccdbd2c4e930 | -11.86301 | -51.5778 | 2025-08-19 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a0d3185f-167d-34f6-afb9-830242151fb0 | -12.97484 | -56.85727 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bca58133-37a1-3549-a46a-c895e4a602cd | -11.75007 | -55.84132 | 2025-08-19 05:18:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44895781-824b-3344-a885-115aafb5b232 | -13.47356 | -47.06339 | 2025-08-19 05:18:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 310f2c94-5d1c-36a4-ab6f-9ad86560478b | -13.31596 | -50.7958 | 2025-08-19 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ea50371e-b39b-3e60-8e3a-ee12d096621a | -8.92327 | -63.63585 | 2025-08-19 05:18:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3417eae8-9f7e-3d5e-9b32-80fdec1d63c0 | -16.79607 | -50.09308 | 2025-08-19 05:18:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 07fb9f9d-ebe4-3ee4-afd8-ab200fbd2077 | -15.04621 | -54.82319 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 73520812-d0a3-38b1-b215-9cfd89370811 | -12.99886 | -56.8357 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dcbea467-bad9-388b-bd0a-ef2b62be8ba3 | -13.16523 | -54.92618 | 2025-08-19 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0c4738c1-8941-3247-9325-c19b97350682 | -14.98753 | -54.80025 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b9ccb501-2f6c-33f4-bc75-295502ae0cd0 | -10.10812 | -57.76759 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54538f92-521f-3136-9ab4-acedd39b4827 | -15.02627 | -54.80729 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README50.md)
