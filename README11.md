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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb978f3b-333b-33d1-94e6-5171686151dd | -1.791 | -46.6455 | 2024-12-03 00:37:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ff85d24-ea37-3b6a-ad26-87804d9631f5 | -1.7476 | -52.789101 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b59af3d4-ff3c-3f5e-a311-07b9e243797d | -1.6552 | -52.745201 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86f418f1-cc0d-38a9-8ad6-68b34fc31808 | -5.7953 | -46.4804 | 2024-12-03 00:37:00 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9ab94250-be06-3dbb-97fc-9c7b70a933a9 | -3.1011 | -53.999802 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b199a05-cdbc-3ca7-bd26-ba985474fedf | -1.2603 | -53.370701 | 2024-12-03 00:37:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 241c0d5d-e6d9-3086-8a52-c257ddbf1e25 | -1.2325 | -51.603001 | 2024-12-03 00:37:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1d03a4b-7789-3e69-9c83-38756ad2c3a7 | -2.8446 | -45.8283 | 2024-12-03 00:37:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c1a7a745-8e93-36f0-a3f2-42b829b12b24 | -3.1027 | -54.007 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5c0d80a-4bef-3846-a5c3-27f9a0f60f4f | -2.4243 | -54.012199 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e753420-31e0-3339-b338-3fb53e6fce6d | -2.3504 | -45.690201 | 2024-12-03 00:37:00 | METOP-B | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 295c9e93-7ab8-3b5e-851a-c96f9b8e472c | -1.7445 | -52.775398 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ab99ede-d1ad-3d84-9fe3-715afe79c3ef | -3.088 | -54.033199 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 063cfb74-7948-33fa-a990-e27f04076bf6 | -2.9855 | -53.3461 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3457fd4d-1dd7-3bb4-b43a-c582316530c2 | -3.4028 | -50.220699 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66e78d8e-8448-3226-9f5b-9f6e0c43a726 | -4.7303 | -45.1082 | 2024-12-03 00:37:00 | METOP-B | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a51cc7f3-4b53-3cb2-880b-027a1a5f7b6a | -3.0577 | -52.750099 | 2024-12-03 00:37:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 550b07d3-c196-3ed7-bbc1-1b4f94a382a3 | -2.8173 | -53.055599 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38de633e-08ff-33e4-b9b4-4e7e21bf3dfa | -3.5351 | -50.167801 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a119cc4-87c3-3ef1-84e9-07bf9c5706d9 | -4.0339 | -54.213402 | 2024-12-03 00:37:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56943780-08b4-3c08-8ad5-bc7457283bea | -3.0949 | -54.2939 | 2024-12-03 00:37:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d648856-69a3-37f8-84b9-19c87e8de72e | -3.2248 | -51.298302 | 2024-12-03 00:37:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fe13906-3144-3841-ac84-3a5861586a6d | -3.3425 | -54.619701 | 2024-12-03 00:37:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e09e132-70ab-3236-bec5-43c6affb3687 | -3.0406 | -54.051201 | 2024-12-03 00:37:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6861989-6cba-3810-be31-90927af74109 | -1.7604 | -52.800499 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f52c7d06-1878-3def-9b81-eb7917a3c4cb | -1.6742 | -52.783798 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e9740e9-4db0-3751-97d2-d86e1c2a5468 | -3.0696 | -53.2617 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4edb7253-dfa4-308f-92bb-3be0d5b6c6ac | -2.4808 | -45.5886 | 2024-12-03 00:37:00 | METOP-B | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 35a121f1-3865-31f9-a445-37e2ee999f78 | -2.6301 | -54.195099 | 2024-12-03 00:37:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 094a5007-735a-3939-814c-b8fd27b58cbe | -4.2659 | -50.6618 | 2024-12-03 00:37:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1d489c5-22e1-3ce2-94bc-bf7105388fe2 | -3.2221 | -45.686001 | 2024-12-03 00:37:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0314bc70-f8b0-3110-8347-6e7bab55c6cf | -1.0702 | -53.441601 | 2024-12-03 00:37:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8cebac02-916f-3c31-aacc-03aeb6c76774 | -4.4046 | -49.777 | 2024-12-03 00:37:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43c4e233-7b78-332b-b7af-2d5a29d3071a | -2.3662 | -53.844898 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d535cd2c-a6a1-3054-9229-d2a78d4cbbe9 | -2.0614 | -50.7122 | 2024-12-03 00:37:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19f63d83-e80b-3f5c-81d7-ed4f13267b5f | -1.9043 | -52.8904 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c111afa8-5f86-3105-bf02-ae5cfcc34ace | -3.2497 | -53.605499 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e4916a9-48ec-349e-817e-c2ca5d55ba2f | -2.7642 | -54.104301 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a7d51dc-1daf-3c39-b5f2-351406765ca9 | -4.1956 | -50.6702 | 2024-12-03 00:37:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e24f656c-f61e-321f-a364-aa8cdbfd6281 | -3.863 | -50.885101 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad126aee-f275-3e06-a77d-59a2af7fcf42 | -2.7577 | -54.121101 | 2024-12-03 00:37:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79fdd571-621e-3aa5-9f69-4ddaaaf3d23e | -2.3539 | -45.6609 | 2024-12-03 00:37:00 | METOP-B | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 03a40715-551b-3b5b-a6d8-3413cf00c0c1 | -3.1497 | -51.103199 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 202ede5f-20f3-343c-9d28-9e216a557d12 | -3.08 | -53.905701 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72be9610-da8b-365c-aafb-43a0bb81c2fa | -3.4021 | -52.861401 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14078f0c-2b32-3b52-822e-6778c7c2d1f6 | -3.0959 | -53.241299 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6d556f3-6748-3a0b-9678-f4d24dd3522a | -2.4227 | -54.005001 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea82b928-b58a-3a52-a701-ab432ce1f4b0 | -2.4494 | -53.618698 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2b6f9ca-29b4-3dab-b4d7-b5f97c285588 | -3.2099 | -53.1068 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77cf4032-3b27-3438-8a68-084335d0adc6 | -3.2935 | -53.663101 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d0860f0-6988-363f-9261-028a6b8c9cc8 | -3.044 | -49.370098 | 2024-12-03 00:37:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af40b52c-5d0f-3f29-976e-6aa051e3a997 | -3.4922 | -53.814999 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47e36313-7d00-379f-b3b9-9a901fbd7311 | -3.1817 | -54.3139 | 2024-12-03 00:37:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4693ee9-2269-3ebf-940c-a7ac0756d8d5 | -4.53 | -42.8955 | 2024-12-03 00:37:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e5f66923-35a5-34db-9a50-46568e0e3c57 | -2.8035 | -54.0499 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9310f6d2-cc46-3cf2-8a36-3a23a2fcdef3 | -2.438 | -53.613899 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0514191-4e83-3556-acd4-137c509462ac | -3.0995 | -53.2113 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5be853ac-f757-3d4a-8e4a-6ec6a510c213 | -3.0962 | -54.1157 | 2024-12-03 00:37:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03cae71c-c3f0-3278-9581-151157080612 | -1.3277 | -54.997898 | 2024-12-03 00:37:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 599f00cf-ebee-3098-aba0-426552f0a68a | -3.1043 | -54.014301 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5e7d870-f8b8-3883-a0d9-fc25a8af57c1 | -3.1751 | -54.330898 | 2024-12-03 00:37:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f94b28f6-d911-3e12-80bc-4017b6414362 | -2.0782 | -52.244202 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 687f5a8a-7714-387c-8f8a-a167b5e17af4 | -3.1836 | -51.161598 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e47bbafc-4494-3ff5-99e7-13d5cc8aba8b | -3.4984 | -50.0518 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8aeaf045-bbdc-3326-826a-0427b5fbe19d | -1.6994 | -52.621101 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e53404d-6f72-340c-b4e0-aa88c639167a | -3.5084 | -46.1637 | 2024-12-03 00:37:00 | METOP-B | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 63b4ee69-51a9-3157-b0c4-710a713c3e5a | -3.0931 | -53.366402 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0b025a3-4c6a-3d73-92de-749d999038d1 | -2.8296 | -54.074699 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 025f70e5-55e2-33e3-9200-84a89c58d9ca | -10.9061 | -48.5341 | 2024-12-03 00:37:00 | METOP-B | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 975acfcf-ccc2-3535-bc83-c4ae29c5b6b9 | -2.7204 | -45.207802 | 2024-12-03 00:37:00 | METOP-B | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f2096873-190c-3f54-90ab-4a1e322cbdd7 | -3.0242 | -54.0243 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60e8e938-b906-3e4c-9303-74be3363de82 | -3.3421 | -50.180199 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 994e2bc9-def4-37f9-b645-b4abd18a751f | -12.1129 | -51.391899 | 2024-12-03 00:37:00 | METOP-B | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0ba7b963-0daf-3c97-84c6-c2b5eb1412db | -2.6755 | -46.604801 | 2024-12-03 00:37:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2c3252a6-99ce-3c94-90c2-71b0e3d4c6f8 | -2.7002 | -52.9011 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f6a367f-70d0-374f-b104-0d1b5e8efd56 | -1.1115 | -54.173698 | 2024-12-03 00:37:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5296a803-cd9a-3ae3-8df0-0603c6086844 | -3.1513 | -51.110199 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df61c227-2eb1-338b-9ae2-4c2ddc0cf81c | -3.0994 | -54.0383 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 456e27ee-a813-307e-bdf2-0eee816fe037 | -3.1037 | -53.2761 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46cd701f-4de3-3eb3-9063-3e45b7381ec5 | -1.7273 | -52.6077 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4809e1e8-bb1a-3b65-865d-e845d53f2666 | -1.789 | -52.744099 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a629d022-d19c-3cdf-95d7-4184962a61a9 | -2.4475 | -53.656101 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5d50fc4-2ca8-3db6-8dae-d1cf28abf182 | -2.5541 | -53.3974 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cfab3315-c74e-3c4c-8ecc-3b27664bc91c | -2.8772 | -54.011002 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e806fa60-11ae-3b98-9561-d593f9078ff0 | -2.8205 | -52.565899 | 2024-12-03 00:37:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff679f41-c9bf-3218-884d-d1d823476912 | 2.7345 | -60.365501 | 2024-12-03 00:37:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 5dcae2ed-b280-3fcf-b565-608832640895 | -2.9839 | -53.3391 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e53f9f38-4c14-3254-8c09-571086ed6f1b | -3.7225 | -50.040298 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 009b62c4-e591-343c-87d6-c509c3bc4379 | -5.7903 | -46.459 | 2024-12-03 00:37:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 498083d0-8ffa-3578-ae45-a55e7d557b08 | -5.1143 | -43.193298 | 2024-12-03 00:37:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4f8cd7b9-41d9-3e1e-9efa-efd6db193b17 | -3.7002 | -51.805401 | 2024-12-03 00:37:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 410078d8-a6b2-343c-9995-9a905b63bd98 | -3.4405 | -41.980301 | 2024-12-03 00:37:00 | METOP-B | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 08e50081-7123-31e8-9568-60c3463d32d2 | -6.0222 | -44.019299 | 2024-12-03 00:37:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4c9be612-5b64-3a05-8e81-bea9d4b52bc6 | -1.7276 | -52.471901 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db160092-5d19-385e-b70d-a838738fa3bc | -5.0993 | -43.216202 | 2024-12-03 00:37:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c7e07838-ae0a-3f68-9937-b0b7112d7e92 | -3.0565 | -54.490799 | 2024-12-03 00:37:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1840725b-e67c-3614-b2cb-995d105f1c45 | -3.4935 | -49.443501 | 2024-12-03 00:37:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9e22b59-ef3e-3dec-8a44-5ac9d2a0d7ed | -3.4627 | -50.937698 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a002d7f3-2b3e-33c2-b335-33853bdcf5b1 | -3.0357 | -54.0294 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ff52495-b110-37ed-bd3f-fe8650f46ed0 | 4.0633 | -60.6562 | 2024-12-03 00:37:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README12.md)
