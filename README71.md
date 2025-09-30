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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 927c3b19-bee9-30c3-aa13-1e6762011065 | -9.42163 | -54.71128 | 2025-09-30 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4dce9154-4aa4-3cb3-a804-7ef5de906d7f | -11.2906 | -47.82303 | 2025-09-30 04:40:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3f12fa91-532d-3a96-a7ac-7b3810b2bea2 | -7.44302 | -46.97155 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f8c32403-fddb-3141-b692-2906557e07bd | -8.83216 | -50.6705 | 2025-09-30 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ccab0f17-1569-37a3-bf27-cb8d8e5496b0 | -9.05748 | -47.62998 | 2025-09-30 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f1135f2-476a-3bbc-b769-2043d58d93c3 | -10.64525 | -48.59268 | 2025-09-30 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8153a8bb-a644-320e-9509-240b47cb25e8 | -13.79288 | -47.86521 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 66dca0c1-64e6-3589-a06b-1a50236576a8 | -13.64385 | -47.32825 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f5b92ece-30bc-37ae-9f04-f03882ed1913 | -12.16897 | -47.77398 | 2025-09-30 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05c33c09-06f4-3170-bba2-46b586af9b65 | -5.98402 | -51.9104 | 2025-09-30 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 072e4024-d5be-3547-9355-6d953e6c5f6d | -10.75857 | -45.37853 | 2025-09-30 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04b7fca8-614f-3263-8d32-0759d587b72c | -13.20997 | -50.94341 | 2025-09-30 04:40:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b5028fc-69c4-37b9-a015-0bebe22858c1 | -9.12841 | -47.63278 | 2025-09-30 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d848da0a-bb4d-3e12-adb0-2385bc13b0f2 | -14.40308 | -47.14389 | 2025-09-30 04:40:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 087450db-7e54-35f8-a7e8-4db33e9338d0 | -13.79096 | -48.00874 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5db3876a-b42e-3408-8f93-791fe267d55b | -8.67144 | -47.709 | 2025-09-30 04:40:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c95b5b82-a0c8-3875-b56f-bddaaf7154da | -10.39498 | -49.03981 | 2025-09-30 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b060a2b6-0b85-30c9-8b31-85d9de6466fd | -9.47717 | -45.5064 | 2025-09-30 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f0c32558-785a-31f0-84b2-484f23ef1407 | -13.5924 | -48.03468 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 737dd684-32da-3fa5-8cc7-98b34c7df609 | -7.60897 | -47.33666 | 2025-09-30 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e80d797-1a18-30a7-824d-5af4a5c38a16 | -12.84004 | -47.01933 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| dc978d11-c27e-35fc-aad5-f113b12bc8e3 | -13.39611 | -48.16862 | 2025-09-30 04:40:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b4a5b9dc-fc49-393e-a586-ac282848c087 | -11.25537 | -47.23634 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1e420d16-41e0-31bc-8a0f-495bce775f2d | -11.20077 | -47.74479 | 2025-09-30 04:40:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 07440f2e-e678-382b-836d-954d90ca6b85 | -11.74184 | -46.84628 | 2025-09-30 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 99cbf602-9ec8-3e70-a69e-f4e9a3865402 | -10.91515 | -44.79466 | 2025-09-30 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77e984eb-b97b-3db5-a3ec-54dfce94e192 | -9.41165 | -54.69948 | 2025-09-30 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8e78abc4-b318-359a-bc53-3aa97e6802e9 | -10.41071 | -48.1675 | 2025-09-30 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1c1a9fa0-1cdc-37a1-9376-30a2177c9013 | -12.85275 | -46.98338 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 5fbb4b93-df85-3573-b6ff-ca09818a40e6 | -11.10839 | -49.77595 | 2025-09-30 04:40:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 768b8344-8386-3e69-82c6-18d0b0a94b7d | -13.5905 | -48.0479 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 395b3007-ffa3-3c3c-a1d7-336c4bf30bcb | -11.19628 | -47.2287 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 68ea7e8b-bef0-3ed2-ae47-70bf4303648e | -7.83021 | -46.99709 | 2025-09-30 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8f064c3d-b39d-385e-9c9b-211ac69c41ed | -10.19918 | -44.88821 | 2025-09-30 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bd634ef8-a439-3818-ab24-51d138b09ffa | -13.59795 | -43.45943 | 2025-09-30 04:40:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ec2f520-a1d6-31b3-be2d-2acf81812cc0 | -13.84278 | -47.5094 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8e9344ae-53f4-3f67-884a-36cc9a8c148f | -13.39226 | -48.07057 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 3f54ed68-be10-3b86-9dbd-b43ce1c68d8e | -8.3226 | -50.87871 | 2025-09-30 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 26b505c5-cd5c-3f52-9afd-32f4f2ea1886 | -7.50564 | -45.44563 | 2025-09-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e2e6812-a3ab-394c-a63f-7bcb1dfba923 | -13.41224 | -48.15269 | 2025-09-30 04:40:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dd75a4ea-df7d-3b3f-af5f-711a11cf549a | -8.32536 | -50.88279 | 2025-09-30 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb40832c-61b6-3dc7-b37d-118ff18b87d9 | -7.81705 | -46.9883 | 2025-09-30 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 66dfcec9-3ec0-3562-a92e-3d737621fcae | -13.01618 | -48.76574 | 2025-09-30 04:40:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8228030-5148-33a7-9e82-00a0285260c2 | -9.31819 | -49.82642 | 2025-09-30 04:40:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6fb88c7b-9316-3318-b812-b21550c1578b | -11.14549 | -54.11792 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1d391ee6-0969-3c8d-9205-ab6a04cc8df1 | -8.67262 | -47.70128 | 2025-09-30 04:40:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31c3edef-fa92-36eb-a8ed-6d368aeff7aa | -11.94017 | -43.91587 | 2025-09-30 04:40:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 49b3f103-6e89-3b18-961d-90b1e0677e97 | -12.84086 | -46.98603 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4f199d5b-c506-3874-bf9a-0fa67f767352 | -12.45602 | -54.30434 | 2025-09-30 04:40:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af075b4b-8603-34b1-b8bd-2d7c00d50b10 | -14.58078 | -48.21595 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 139eabae-4fd6-3315-a100-54012f49a68e | -14.5596 | -48.47035 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9571b8bf-1d92-3068-a2d6-ed6175dfe52a | -20.61008 | -46.0679 | 2025-09-30 04:42:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 55daeab2-c837-3a73-b59a-f9de5a2a3ea0 | -15.68964 | -46.25885 | 2025-09-30 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4da97512-b02a-333e-aa21-a1f4369a1a5f | -15.25191 | -49.71227 | 2025-09-30 04:42:00 | NOAA-21 | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c20c03c-a2ca-36b4-9b9a-17fd03d26a7e | -14.85544 | -48.32523 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aac4f339-a9f8-3252-8b78-fd349eea378f | -14.6959 | -48.24594 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f5182f29-a373-3c51-90a9-b9aa6e2c126a | -14.51356 | -48.46463 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c0416bef-0c37-3bcc-8a3e-f830a9e2b795 | -15.26296 | -51.47624 | 2025-09-30 04:42:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f3f58dfe-4f23-301f-8775-11f42c746276 | -18.19437 | -45.21881 | 2025-09-30 04:42:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e077566-79e6-3778-82bb-7afefaae552c | -19.94184 | -41.64599 | 2025-09-30 04:42:00 | NOAA-21 | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 8fedbd84-8999-3e8b-8a12-de8379f4eef7 | -14.53892 | -48.23802 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 98d962e0-79f6-32d5-ac87-12a3a48169fd | -15.30239 | -56.79383 | 2025-09-30 04:42:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51b41df4-1d83-306a-8c46-35c7b1a3980a | -14.76437 | -45.75801 | 2025-09-30 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61618d64-3017-3e93-bfb1-582b671e975a | -19.24352 | -46.54507 | 2025-09-30 04:42:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 472f5a9b-ff66-3beb-a474-5fb8c2fa31ae | -15.3743 | -47.08032 | 2025-09-30 04:42:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5ca04290-8861-3427-ad63-68ed72126684 | -15.55169 | -44.35098 | 2025-09-30 04:42:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 08dd103d-7b17-31ad-8120-4477a9192c30 | -14.69349 | -48.23697 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3cba6bbd-28b7-30bd-b0ac-d151e48a89d1 | -15.25747 | -56.83043 | 2025-09-30 04:42:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f2a35998-8a26-3147-ba82-314755268d64 | -17.75619 | -51.33935 | 2025-09-30 04:42:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7f788275-9c79-3770-8e47-936469daa0ec | -15.72353 | -59.50488 | 2025-09-30 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dd952b9c-4a5b-338f-8a9d-6b4e01765fe0 | -19.53025 | -43.90032 | 2025-09-30 04:42:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3667048a-9a33-39d2-9da3-8e12ba7e1a95 | -15.92911 | -46.20603 | 2025-09-30 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| e52ee9b8-cf63-3efd-8fc5-07428470848a | -15.49067 | -48.55849 | 2025-09-30 04:42:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f3406f48-a540-351b-887e-61d7c9bc7f87 | -15.25158 | -48.73672 | 2025-09-30 04:42:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff3a4fb1-e410-3084-a49d-6f3cd7d2e360 | -20.23256 | -41.34623 | 2025-09-30 04:42:00 | NOAA-21 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6f125b97-e713-3b91-b2d1-c8ff9213a6b3 | -17.91509 | -57.6115 | 2025-09-30 04:42:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 97e96923-365d-3346-81e0-8dd1173c7f56 | -15.80994 | -59.51992 | 2025-09-30 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| beb21913-83fb-31e0-8152-6d0c6665687f | -19.84945 | -43.81496 | 2025-09-30 04:42:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d060b1a0-71d1-3e01-8544-5c76d1fe5978 | -14.70663 | -48.24792 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 970eb3e7-687b-35ee-b2ea-02dc4bf11f36 | -15.39105 | -47.07323 | 2025-09-30 04:42:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2caa68bf-2aad-3520-bc74-f09cfe2e8374 | -15.3804 | -47.0776 | 2025-09-30 04:42:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1a52f700-dcce-3445-8069-124fdbc212f8 | -16.67809 | -44.55887 | 2025-09-30 04:42:00 | NOAA-21 | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 813225f8-367d-38e6-b4af-1ade58051d2f | -14.51007 | -48.41334 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 820b155b-59c6-331f-83e5-99f5a0504992 | -16.61047 | -43.35855 | 2025-09-30 04:42:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2af65ed1-bd7d-33e4-afa5-e916af0cd954 | -18.70738 | -43.19164 | 2025-09-30 04:42:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fd214f74-1e16-3fc2-882e-9fd1fcdb7ea6 | -15.53554 | -42.65717 | 2025-09-30 04:42:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3be5b4b2-7d49-3aae-aae6-81885d58edb2 | -15.92137 | -46.20121 | 2025-09-30 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba14d6a5-2bff-390e-a835-cedce72787bf | -14.69943 | -48.14151 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 92a82c9c-86cc-3b8a-a5bf-a51628b4060f | -14.7115 | -48.16067 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5d4c4d68-bb29-3a37-8f36-67036ecd3f15 | -15.1907 | -48.45817 | 2025-09-30 04:42:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 675e9732-be16-3496-94c8-7a4bcf61ac23 | -16.0655 | -51.03714 | 2025-09-30 04:42:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a2471673-52d0-39f0-8b24-05986fd953b7 | -14.58154 | -48.22229 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab0d57dc-dc52-3366-9618-6005b25c2c3d | -15.2714 | -47.89146 | 2025-09-30 04:42:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1217f7b8-a34a-36c2-944d-0e7b4fa145bc | -15.27813 | -49.24775 | 2025-09-30 04:42:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e1717aac-5ca5-387c-8e8e-49d112d4fccd | -14.70197 | -45.7034 | 2025-09-30 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6f7f14d-7392-3f84-9c80-9065da3c8333 | -15.16872 | -52.81934 | 2025-09-30 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1fa9285d-c9e4-34bf-8d53-8622129b788d | -14.57495 | -48.21708 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 16e2d559-33e3-3279-abfd-a9836c79740b | -14.6807 | -49.35625 | 2025-09-30 04:42:00 | NOAA-21 | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 444a1d06-8506-3373-92e7-f14a5440f4f9 | -14.51002 | -48.46406 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 766d8cd2-bbd7-3ac5-a5ff-43e21d885f01 | -14.88769 | -47.18863 | 2025-09-30 04:42:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README72.md)
