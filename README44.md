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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dcb0264a-e818-35ee-80b1-ffba428d1b2d | -10.776 | -46.39158 | 2025-08-25 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| e7f02948-7734-33b9-af3a-daddf8b2e7cd | -13.44641 | -46.91673 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6dcc6757-508c-3274-a982-19718648be80 | -7.79072 | -61.57602 | 2025-08-25 04:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 69268dee-2a54-367f-b7b2-ff2d437e77c7 | -7.91043 | -63.07312 | 2025-08-25 04:42:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 355ac525-820a-3044-a980-b9b4f9561825 | -9.24468 | -59.62486 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d6ee7f5-4111-3926-b07d-0b2014838dbf | -11.69454 | -60.1805 | 2025-08-25 04:42:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df646833-38d8-3244-b893-31845dc63f23 | -8.76684 | -49.95055 | 2025-08-25 04:42:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3030f358-5c11-3d04-8685-d41742049438 | -9.19291 | -59.47848 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f36f600-2088-3078-9618-b02c544193fc | -9.20191 | -59.5169 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27f5eef1-5c1b-301e-86f5-ed7ef813a4cc | -6.8214 | -59.43437 | 2025-08-25 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 166a4806-8650-3e7b-8c6e-54280eec26aa | -12.73361 | -48.11962 | 2025-08-25 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 421c003b-bdff-30eb-9a81-dffd2fef11bb | -10.88722 | -55.79414 | 2025-08-25 04:42:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 952176e1-4f44-3597-a23b-565cf83ab34f | -6.68618 | -58.85823 | 2025-08-25 04:42:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6f1de86-038e-3563-bc28-d9d8d0f5e91c | -8.58128 | -62.62781 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 47d8dabb-6a4c-3820-b6bd-4e8f5a64b73a | -9.17371 | -60.81087 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4131320-b5f5-3ed2-9015-157a957bedd1 | -13.44635 | -46.91423 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5dae38a8-c3fb-3323-9e2d-b1dbb4618f73 | -9.05844 | -60.62663 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c54869f1-cc8a-34e9-ace7-f1df56b18d83 | -8.13441 | -47.301 | 2025-08-25 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a55affc8-391e-39a9-8107-acaaad5b3d08 | -9.20319 | -59.50981 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a39f602a-e558-3ab6-9179-b3cd55a272b0 | -9.17894 | -59.6124 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d055731f-a490-36ed-8e9f-b86d6839de47 | -6.35938 | -57.96732 | 2025-08-25 04:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a603266e-3c2f-320f-b15d-ca33820f1d2d | -13.15186 | -53.74086 | 2025-08-25 04:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 282b258d-08dc-3c58-b3aa-d5f5b66f4b2a | -8.87172 | -62.4223 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 94f1a233-bec6-39ba-8a73-1198013b9a14 | -13.50862 | -46.91158 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c5bf30c8-72ad-34a7-b71a-6ee85568b790 | -12.68939 | -47.8279 | 2025-08-25 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec78ffa3-7cf5-39d3-9ce5-512c26a434a1 | -6.82773 | -59.4315 | 2025-08-25 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6144ac99-766b-3a8b-8082-96401a492ca2 | -8.12747 | -47.13136 | 2025-08-25 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1e004a11-23d0-343c-82b2-e8f824d97eb6 | -11.18557 | -55.02541 | 2025-08-25 04:42:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 042b05ca-9636-31b4-843b-2f16cb4a15bd | -8.12474 | -62.88437 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 97ca33a5-365c-31a5-a3de-e499e0c271b9 | -13.83654 | -46.70589 | 2025-08-25 04:42:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6595d76c-2541-3c26-b657-a3f2683c383d | -13.61382 | -48.16804 | 2025-08-25 04:42:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cca2beee-3ebf-33ea-9a61-f67b9229c88f | -9.19712 | -59.51579 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7224e79f-37ed-3756-9e2e-71779d2edaee | -10.59973 | -44.32458 | 2025-08-25 04:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5cfc9662-04d6-3c2e-856c-898143779df4 | -13.50299 | -46.89669 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6deec01e-3956-35e3-9bba-458feb1d9e02 | -8.6334 | -62.64446 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c5641775-60fc-3d3a-af54-5ed668801c15 | -11.64383 | -46.20969 | 2025-08-25 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ba0d4ec3-7ec5-3725-afaa-4cadfb17415d | -8.54248 | -48.85135 | 2025-08-25 04:42:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9b6a528-a170-395b-ac0c-2b985dc5c474 | -13.43427 | -47.02702 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0fa87608-e99d-3bc8-893a-0fbec1da661a | -6.91997 | -62.99523 | 2025-08-25 04:42:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6f810b7b-787d-320f-b5cd-dbc5cf86bd9e | -8.92257 | -62.43132 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b04d7750-c26e-3ff3-ad1c-ff61fa86839c | -11.1813 | -55.03242 | 2025-08-25 04:42:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce4c9c5d-ea45-3300-a67f-18eadaec8e4c | -10.71515 | -47.13641 | 2025-08-25 04:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d80dc385-5362-35fc-88d7-cf00941cc301 | -11.46934 | -55.46966 | 2025-08-25 04:42:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 634b9b60-673d-3488-b93a-2fb319fa8564 | -9.19851 | -60.79428 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 67889e9e-66c9-3558-925e-2631485d49b6 | -11.54806 | -51.91426 | 2025-08-25 04:42:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac9aee3b-d167-3c75-80a6-3ff998be3c8b | -8.22633 | -61.39651 | 2025-08-25 04:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c4743768-f566-3510-8128-d0931a4c598d | -8.80873 | -45.46345 | 2025-08-25 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63874b47-f814-3779-be77-2cc655a20231 | -13.19291 | -47.20364 | 2025-08-25 04:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ce60c3ca-e9f1-39d0-8e0f-b74f7a8b944c | -9.20604 | -60.7869 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00b32190-230b-3b09-9de9-ad46a06e3c21 | -9.17764 | -59.46465 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e75e5d23-f93b-3902-9173-8b3e43cf01dc | -9.19979 | -59.50168 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 73b17cfe-4877-344a-a4e3-48a9b3ee1635 | -8.05727 | -49.6871 | 2025-08-25 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 850cd1f9-a843-3ec4-abe3-5c0810f63bf4 | -7.62208 | -62.72825 | 2025-08-25 04:42:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8abbcfe0-2b6c-3ed4-8a6c-9040f8ee0d4f | -8.21913 | -61.40039 | 2025-08-25 04:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 77e6e01b-6ebb-3315-b5fe-4c17dcb0619f | -8.22109 | -61.39011 | 2025-08-25 04:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| c08fb4d7-c2dd-365e-945b-61d91d141e62 | -9.16069 | -59.46505 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7dd2706e-8c9a-3168-b7f0-f62216d66ecc | -9.61174 | -55.34734 | 2025-08-25 04:42:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 25e2a7fa-053f-33db-b346-98dcc2f34b94 | -9.15526 | -59.46398 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78437792-ef6b-3f19-87d2-49327d08b965 | -9.96539 | -60.18383 | 2025-08-25 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5ef7b7f3-4917-310c-b57b-1cd4a7fa81c5 | -11.02907 | -59.17639 | 2025-08-25 04:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 630d6bb0-1205-3d83-a4d5-95007759fcb2 | -11.18522 | -55.03308 | 2025-08-25 04:42:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a3a3ddc2-a6e7-3d44-a6aa-0ae87f3c85b7 | -13.48198 | -47.0177 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df283e35-4c62-3036-bc02-09a9d4480293 | -9.19298 | -59.44215 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f43c88e-af6a-3160-a721-94c2c17bad28 | -8.59738 | -62.59935 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 33c03d59-e392-3512-9feb-4996e1720dcf | -9.19157 | -59.48557 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ad4824f-a7b9-344b-b59d-1095fb5bb458 | -6.79453 | -58.63581 | 2025-08-25 04:42:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 92449949-2cc2-3a61-94da-d90d56cc225b | -10.83819 | -46.41127 | 2025-08-25 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3867bf7d-9ea2-3116-bead-324831818d7a | -9.16418 | -59.47666 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af4a8b16-b103-3210-a2d2-2660ad7f9d20 | -8.2955 | -47.23684 | 2025-08-25 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d893e0f7-2a37-390c-a9fe-f5a2fa3eb59b | -7.65325 | -63.52937 | 2025-08-25 04:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d17bf999-ebd8-3bd6-a6ef-a324f8936172 | -13.37916 | -51.78909 | 2025-08-25 04:42:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a941e06-7bb5-35fa-b094-16f319092fcd | -11.57353 | -46.30363 | 2025-08-25 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68d7b5dd-4b87-38e7-81c8-aed7448ffd94 | -6.83242 | -58.95754 | 2025-08-25 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1811697f-6480-3395-8778-68f3626e987b | -9.20772 | -59.60993 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 776b53e2-3eaa-355f-aa32-40ef2d5e15dd | -10.39536 | -57.69088 | 2025-08-25 04:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b44cd8a2-b51b-3427-a07e-969cb31e6a65 | -11.14109 | -44.78717 | 2025-08-25 04:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c07ba096-bde6-394a-93ad-220a96dc63ee | -9.16133 | -59.46156 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 67fbc68e-9b21-3ebd-81a3-1021b636be8b | -11.60374 | -46.35478 | 2025-08-25 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| ff93134d-e1d3-3f96-bc35-3f7698986818 | -10.03029 | -59.35717 | 2025-08-25 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33933db2-0124-342e-babb-159967bbffc8 | -13.42886 | -46.9043 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4a6afc0-5dd1-3553-80c5-896c468df1d6 | -8.06005 | -49.68743 | 2025-08-25 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| bf0fd058-4741-3940-818d-4b3950caf290 | -12.43316 | -56.50505 | 2025-08-25 04:42:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ee80ac7-3dd8-3736-9ae7-0e6fc63346ac | -9.2574 | -59.77312 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 93c91fd6-c41b-33b8-b456-7a49f20e899c | -11.23859 | -50.40453 | 2025-08-25 04:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0decc970-4f2c-380f-9003-2b5159df3be2 | -9.61513 | -55.36304 | 2025-08-25 04:42:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ce60e400-61eb-387a-8dd3-42528f6f7618 | -8.06282 | -49.69144 | 2025-08-25 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 43254016-6f63-3577-a408-5149a807451d | -11.14839 | -44.79608 | 2025-08-25 04:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f00b578a-b4cf-33c1-8f42-4f02518fa8f2 | -8.11793 | -62.88301 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d535abf1-4e22-312f-ba1b-eb5f2f4d4fd4 | -12.48697 | -53.82467 | 2025-08-25 04:42:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd222ade-fbc6-35e1-b748-1081941503a9 | -9.17225 | -60.77149 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e6596ffb-a66c-3cd8-9d02-a3f2874105d5 | -8.80393 | -45.47034 | 2025-08-25 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 80e23c3e-899d-3f0a-ab66-72c9dfb10cc2 | -13.43794 | -46.89509 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9e15b01f-1f27-3b9b-9d22-8066ba9aa549 | -9.06268 | -60.63644 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b56c478a-7609-36ac-bf19-973c92299603 | -8.6497 | -63.43351 | 2025-08-25 04:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ed6fcff-89bb-3514-8e85-4f29557be97a | -11.09604 | -44.77267 | 2025-08-25 04:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a09e0e9-54ec-37d4-a245-46028682160d | -8.05672 | -49.69058 | 2025-08-25 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f6aba95a-9520-3415-ab90-6dbacbbaaa1b | -6.79514 | -58.63239 | 2025-08-25 04:42:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 99961618-46f6-34bb-8346-502234da7e04 | -8.06447 | -49.68099 | 2025-08-25 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cf438f29-03fd-331a-9ddc-0a22587c163b | -10.60401 | -54.88802 | 2025-08-25 04:42:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c0ffb40c-7f07-31a5-8925-aa709ef534c0 | -9.26234 | -59.76826 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README45.md)
