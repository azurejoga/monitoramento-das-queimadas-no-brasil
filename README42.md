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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9fb79964-15fb-3cb9-ae30-aa5f85ba6fda | -10.8352 | -45.8843 | 2024-09-26 01:56:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 5b1eb4c4-8728-3554-9a30-d238ce8e0a10 | -10.9148 | -45.669 | 2024-09-26 01:56:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.7 |
| eb5248a3-c6a7-39c7-a9d0-1f78f1e62384 | -10.8915 | -57.4521 | 2024-09-26 01:56:08 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 233da56c-81ac-354b-988e-a56c0efd4318 | -11.286 | -46.278 | 2024-09-26 01:56:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.2 |
| e6f1a463-e6e2-3d18-812e-f466eb8f8740 | -11.2123 | -51.1415 | 2024-09-26 01:56:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 50c63e05-d845-3978-800b-8f1f2e589983 | -11.1845 | -54.7769 | 2024-09-26 01:56:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 5d2fe881-88d7-352d-9411-2d84648f2a22 | -11.2034 | -54.7752 | 2024-09-26 01:56:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 7a63e94c-3600-36e8-9d5a-9ba408e61677 | -11.2599 | -65.299 | 2024-09-26 01:56:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 1d305016-1fcd-3ba9-a9db-95183e66fed6 | -11.26 | -65.2801 | 2024-09-26 01:56:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 6fbf0d75-cdd3-3842-9edd-86f4331a961f | -11.5013 | -56.7677 | 2024-09-26 01:56:12 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 0b558d91-cb22-39e6-b2e0-0bb755c7b4b0 | -11.7179 | -47.8551 | 2024-09-26 01:56:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 31b57591-7dec-39f8-82ec-2cb83f33c172 | -11.955 | -60.363 | 2024-09-26 01:56:14 | GOES-16 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 67.8 |
| dff8a95a-f9ad-3e0a-ba35-15cd76cb2882 | -12.2367 | -45.5045 | 2024-09-26 01:56:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 122.3 |
| faac207c-4860-3fac-ad1f-63ed313a37c9 | -12.5276 | -53.496 | 2024-09-26 01:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 073c6004-1c18-396c-a91e-7d8aa62ca828 | -12.8076 | -51.3423 | 2024-09-26 01:56:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 82ee0d82-59d8-36f8-b27e-6b13f154a339 | -12.822 | -62.7078 | 2024-09-26 01:56:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 45.8 |
| dbc74d8e-f392-3320-983b-47a5147d4bc6 | -12.841 | -62.7067 | 2024-09-26 01:56:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 147.9 |
| d2947dbe-4835-3e0f-81cb-36425ebbd1f6 | -12.8411 | -62.6874 | 2024-09-26 01:56:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 41d67bb2-c637-3c61-8d54-8260be0071f2 | -13.286 | -51.3473 | 2024-09-26 01:56:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 103.7 |
| d17cb400-8d50-3115-8bfa-c71b4328a8cd | -13.2863 | -51.326 | 2024-09-26 01:56:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 188.9 |
| 45f1058e-bed2-3aea-a8f8-c2cf291ec594 | -13.3052 | -51.3449 | 2024-09-26 01:56:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 91.6 |
| d2a3f3fe-fb8a-3d07-9e0d-2e7df03437d8 | -13.3055 | -51.3235 | 2024-09-26 01:56:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 162.5 |
| 47835885-d856-3c34-aa2b-722aa2a6bdad | -14.57 | -45.7205 | 2024-09-26 01:56:28 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 58.4 |
| a3217676-6b47-383b-9723-9f6fd95f326e | -14.5705 | -45.6973 | 2024-09-26 01:56:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 208.2 |
| 2dd291b4-3851-3792-968b-e83189ac061c | -14.571 | -45.674 | 2024-09-26 01:56:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 35de7038-5fb3-35c2-a02b-e29f46f8ea2c | -14.8626 | -51.5234 | 2024-09-26 01:56:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 80.5 |
| ea0c8ce8-8ee7-3cd5-a752-efe578b5da93 | -14.863 | -51.5019 | 2024-09-26 01:56:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 252.0 |
| b966bbda-1402-38af-ba20-7a8eba3bfb23 | -14.8634 | -51.4804 | 2024-09-26 01:56:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 0321263a-ae0e-3766-8cd4-ba999c3f64dc | -14.882 | -51.5207 | 2024-09-26 01:56:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 6aa3d6fe-508e-3e27-a6c1-3555d8357ab8 | -14.8824 | -51.4992 | 2024-09-26 01:56:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 191.2 |
| 63fe30c8-8459-3a18-b98c-ef1d0ac22bab | -14.8828 | -51.4777 | 2024-09-26 01:56:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 57.5 |
| fb6a7290-3c64-3af5-9c61-e26b6932014f | -15.7676 | -49.9555 | 2024-09-26 01:56:35 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 158.2 |
| d30e7c12-ec8c-3a23-9749-e7b90b9d5b20 | -15.768 | -49.9334 | 2024-09-26 01:56:35 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 2286b044-4c50-3d62-b9d1-b5a7f98ce62d | -16.098 | -52.0111 | 2024-09-26 01:56:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 162.2 |
| acb548e2-31af-31ef-8bb9-fb7d92e47916 | -16.0985 | -51.9896 | 2024-09-26 01:56:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 214.6 |
| 15bd7531-729e-3636-9eb6-07e51b25e73c | -16.1176 | -52.0082 | 2024-09-26 01:56:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 3dc2885d-fc77-31aa-a6b2-f7677cd7136e | -16.118 | -51.9867 | 2024-09-26 01:56:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 141.1 |
| f2eb6306-4fb3-3371-a7aa-010f6f46c65d | -17.096 | -56.3576 | 2024-09-26 01:56:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 83.8 |
| 34584f1f-82d6-341c-9d69-2d723d58d823 | -19.929 | -43.7959 | 2024-09-26 01:56:56 | GOES-16 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 61.8 |
| 296eb78f-70bc-3207-b9a6-5e4e29a991fd | -21.9374 | -48.5688 | 2024-09-26 01:57:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 56.6 |
| b35d270a-ec1e-3eb2-a7d0-89ad6c61c4ba | -21.9381 | -48.5453 | 2024-09-26 01:57:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 61791a33-c30d-3601-b894-ee77ac4e4cc1 | -20.6 | -51.55 | 2024-09-26 02:03:26 | MSG-03 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c5125547-e1da-33a7-9662-efd03f9a25bd | -20.6 | -51.49 | 2024-09-26 02:03:26 | MSG-03 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4fd538f4-7ea1-3c52-994d-ba31dea5fa37 | -13.29 | -51.32 | 2024-09-26 02:04:08 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4f5cf864-49cf-3b75-a49b-ffa6fb178df6 | -13.29 | -51.38 | 2024-09-26 02:04:08 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| af4f7c8d-00b7-345a-8493-7920bf2ea3f1 | -12.8 | -51.25 | 2024-09-26 02:04:11 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3facc3fd-264b-3f8b-b141-21779b0c352b | -12.83 | -51.26 | 2024-09-26 02:04:11 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d41bd7fa-f45b-3956-8f44-9e68b95243ad | -12.8 | -51.19 | 2024-09-26 02:04:11 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 785bf034-ae72-3575-82d0-b5d9d42e53cc | -12.8 | -51.31 | 2024-09-26 02:04:11 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3702a058-391f-3412-b923-50ab1d4084b9 | -12.77 | -51.18 | 2024-09-26 02:04:11 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b820be8f-39c0-3cb0-8b05-2e4a63bf8ac1 | -12.77 | -51.24 | 2024-09-26 02:04:11 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f5c511d2-e7d5-3a13-8914-6bdda400d8ce | -12.77 | -51.3 | 2024-09-26 02:04:11 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4ac79139-48c8-3872-9690-aae7a1e9e5dc | -10.01 | -53.48 | 2024-09-26 02:04:29 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5075f5a9-c6ab-36d4-ae4f-5b14c677aef5 | -10.04 | -53.48 | 2024-09-26 02:04:29 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5b770ac0-333b-397c-8a43-97f3d5bb32a9 | -7.37 | -55.5 | 2024-09-26 02:04:45 | MSG-03 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 691dea6c-0272-3f20-b442-5904f8628456 | -1.0553 | -53.3553 | 2024-09-26 02:05:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 91811b41-ded2-3ebd-b87d-4ca7ff27c7fe | -2.6785 | -57.531 | 2024-09-26 02:05:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| b3b3d6c6-8272-3620-b9e9-2e4d3e68bc29 | -2.6968 | -57.5307 | 2024-09-26 02:05:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 46d6f1b5-c6d0-38ef-92e8-eadda022d840 | -3.3342 | -53.2117 | 2024-09-26 02:05:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 6b103868-d30d-3dd4-ace1-042b1a4dc2c7 | -3.5674 | -50.3584 | 2024-09-26 02:05:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 4531b4ad-03ed-340d-91da-9dcb1abb03e3 | -3.5673 | -50.3794 | 2024-09-26 02:05:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 171.0 |
| 21de9df5-041e-3382-8bba-dbb138da8d60 | -3.9208 | -46.4459 | 2024-09-26 02:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 5fbbc789-a08a-377a-b611-c88e698a4c3c | -6.8024 | -59.3044 | 2024-09-26 02:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 0bfb3ee6-a5ae-3eec-8d02-8cc74c8bcb0e | -6.784 | -59.3052 | 2024-09-26 02:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 7442aff5-c13f-38da-8209-7de98d946d17 | -6.949 | -63.1048 | 2024-09-26 02:05:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 9573ef5c-1f25-39bb-b9ec-a607102ad4c7 | -6.9306 | -63.1053 | 2024-09-26 02:05:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 15a27d98-ef4c-396d-a65f-4b5d245a4ab7 | -7.3824 | -55.4924 | 2024-09-26 02:05:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 157.3 |
| 9f073211-3c38-3cc6-8dd4-6ae1c17c8a9d | -7.3823 | -55.5124 | 2024-09-26 02:05:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 204.8 |
| fa9b09e1-32eb-3bf7-ba4c-0efd9edfb6e1 | -7.3639 | -55.4935 | 2024-09-26 02:05:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 247.7 |
| 2c206049-607f-3d6f-9c66-76fbbaa24b0c | -7.3637 | -55.5134 | 2024-09-26 02:05:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 391.6 |
| ba53f293-c9b0-3c54-96e1-db80dfa47fcc | -7.3636 | -55.5334 | 2024-09-26 02:05:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 8c1bf57e-2103-3f32-a6df-c27b4ac4527f | -7.2905 | -61.106 | 2024-09-26 02:05:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 2923c8a8-c9e4-3373-9a1c-04d997f29ef4 | -7.8156 | -54.7252 | 2024-09-26 02:05:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 146.4 |
| 747ae354-d0d5-3ec5-a8fc-65df9122bb07 | -7.8154 | -54.7453 | 2024-09-26 02:05:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 106.3 |
| a6a38c1b-c468-3d6e-bc72-441cd6f7ae26 | -7.7314 | -72.7695 | 2024-09-26 02:05:51 | GOES-16 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 452734ad-66f2-3e22-8793-128e125dca06 | -7.797 | -54.7263 | 2024-09-26 02:05:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 532bbd75-7a49-352f-b562-b065f174a77c | -8.3155 | -54.9956 | 2024-09-26 02:05:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 542243af-32e2-3c55-bcfb-3701b0693826 | -8.7087 | -54.7881 | 2024-09-26 02:05:56 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| fee9dc36-64b0-39e5-9719-4fd9e453344c | -8.8098 | -58.2172 | 2024-09-26 02:05:57 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 79.9 |
| fa1afcfd-2e78-36d0-bc18-099a560ca6a5 | -8.8096 | -58.2367 | 2024-09-26 02:05:57 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 5ed90778-bac7-3a6a-9198-1dea3fcf1a44 | -9.1046 | -61.1237 | 2024-09-26 02:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 113d342c-ef9c-355f-90bf-2788ffd56b45 | -9.1035 | -61.2769 | 2024-09-26 02:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 9f674919-4c50-3d65-b4bc-1cbc70c37b6c | -9.086 | -61.1245 | 2024-09-26 02:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 538c1157-bdb4-3039-8d82-3e6ae464f93a | -9.0657 | -61.3743 | 2024-09-26 02:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 84a11ca1-168c-3fb3-8c76-c19af5bb57ac | -9.1349 | -65.564 | 2024-09-26 02:05:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 5d3e4660-4d16-34bf-bf8c-802385332068 | -9.6018 | -50.1352 | 2024-09-26 02:06:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| c7223f9b-715b-36df-85d7-62c3da933ffe | -9.6015 | -50.1566 | 2024-09-26 02:06:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 1d0eed4b-6c37-3e03-8dbf-a371582aa669 | -9.5827 | -50.1584 | 2024-09-26 02:06:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| ed57cf96-400b-3aa7-b376-26768e0390dd | -10.4562 | -45.7968 | 2024-09-26 02:06:05 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 23d4ab45-9177-3d31-a6d7-8a02d5db98a5 | -10.4752 | -45.7943 | 2024-09-26 02:06:05 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 52a79d38-7209-3be2-84fb-2caaea3d966d | -10.4749 | -45.8171 | 2024-09-26 02:06:05 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 9d543501-05c9-3d22-8b7c-ee4288e157d4 | -10.4558 | -45.8195 | 2024-09-26 02:06:05 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| b9d76adf-7508-37d2-949c-fcf56ba5ed21 | -10.3882 | -67.8737 | 2024-09-26 02:06:06 | GOES-16 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 1077f88c-325c-3ce7-9b47-2be42011e235 | -10.9148 | -45.669 | 2024-09-26 02:06:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.9 |
| f1fba2c7-b6fe-3d1a-866f-85908c8e14f3 | -11.2033 | -45.5158 | 2024-09-26 02:06:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.8 |
| f08a536f-0f5d-3bd2-8de8-4fb301ba6589 | -11.2029 | -45.5387 | 2024-09-26 02:06:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 0e20e325-b812-3aee-a63e-008b536d2a60 | -11.2223 | -54.7735 | 2024-09-26 02:06:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 132.1 |
| f8b39587-96f2-35df-a7f8-106ce0cec4f9 | -11.2036 | -54.7548 | 2024-09-26 02:06:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 041ac64b-55da-3916-b4d0-1856deb83eeb | -11.2034 | -54.7752 | 2024-09-26 02:06:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 275.1 |
| b5d2bfaf-fbbe-312d-b36f-8ee9ad8f97dd | -11.2031 | -54.7956 | 2024-09-26 02:06:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 122.0 |


[Clique aqui para ver as próximas entradas](README43.md)
