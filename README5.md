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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca4be8ab-e71f-39f8-9fd4-086bfca2258e | -6.68329 | -39.50509 | 2025-12-03 03:46:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5013bef1-d0bd-324d-b450-54671907bd4f | -6.90413 | -39.55526 | 2025-12-03 03:46:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a550d9d0-a878-3cd7-841d-0067183c1e94 | -3.86644 | -40.64663 | 2025-12-03 03:46:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 346324d1-fc48-325d-927d-5dab6818883a | -2.84662 | -46.7423 | 2025-12-03 03:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| dc416d72-85a6-365b-a83d-a41dd2389135 | -2.98708 | -49.52515 | 2025-12-03 03:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 42456177-4823-3ad2-891d-58bd4e646abf | -2.24285 | -48.31569 | 2025-12-03 03:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0b88d591-b8d5-366b-b976-0abacd3b1618 | -4.4567 | -38.38765 | 2025-12-03 03:46:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 49b81a8e-c211-3e66-aadb-aafc2c61a05a | -6.1549 | -35.31806 | 2025-12-03 03:46:00 | NOAA-20 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b574e52e-d9d6-3e78-957a-9ce4a97c8705 | -2.57154 | -46.8855 | 2025-12-03 03:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 359c661c-5b07-36f4-afe3-f7ea1c51104c | -2.78708 | -47.43411 | 2025-12-03 03:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a2605575-50bb-3bd8-9e21-2d5376038e61 | -5.19462 | -38.89997 | 2025-12-03 03:46:00 | NOAA-20 | BANABUIÚ | CEARÁ | Brasil | 2301851 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 88f621ce-ba6c-3471-8651-5715238ec802 | -2.78768 | -47.43594 | 2025-12-03 03:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c92f559f-eb0b-3115-be62-cfdf9af99129 | -2.62475 | -45.1405 | 2025-12-03 03:46:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f5dd0892-5827-30be-be08-7f8e27846ddf | -3.22335 | -46.87064 | 2025-12-03 03:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b8ace816-d918-3e16-959f-997d92af50b4 | -7.75991 | -35.06562 | 2025-12-03 03:46:00 | NOAA-20 | ARAÇOIABA | PERNAMBUCO | Brasil | 2601052 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 33073345-f74f-3a1d-ade5-619d9500ae84 | -2.17438 | -48.37106 | 2025-12-03 03:46:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 060e42c9-f7e2-3631-8df7-c44bc9648e1d | -3.75574 | -50.15609 | 2025-12-03 03:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2879351c-a054-3569-aa9d-5566bb5ae155 | -3.62921 | -48.89429 | 2025-12-03 03:46:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5b1ba01-6d30-3802-b1c0-9f1047600e5e | -3.19391 | -41.85925 | 2025-12-03 03:46:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0993ece9-85af-3eaf-8444-256be459d625 | -3.56327 | -42.7089 | 2025-12-03 03:46:00 | NOAA-20 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| df2e78d7-240f-34a0-a325-c24dc3acd9a8 | -2.82699 | -48.45207 | 2025-12-03 03:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 749f9775-6915-3db4-9de2-da92d55b23aa | -3.44167 | -45.39088 | 2025-12-03 03:46:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d40b4124-4058-31de-9cab-aebde59254bd | -3.56436 | -42.7104 | 2025-12-03 03:46:00 | NOAA-20 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf14998f-fc06-3841-8a3b-9516b4f0421e | -5.85242 | -39.94845 | 2025-12-03 03:46:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fed993b5-104f-3169-a3e5-dcf233f02cf4 | -3.04939 | -48.43118 | 2025-12-03 03:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| cf2a254a-5162-31bc-9762-184b49d6635f | -4.28281 | -43.7723 | 2025-12-03 03:46:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bff36086-da4e-36d3-9c96-8d35daeefad0 | -2.69603 | -49.32338 | 2025-12-03 03:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 675a6915-60f9-34be-b11a-a0335eb97b41 | -3.23987 | -45.57277 | 2025-12-03 03:46:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 9e8e4253-31ef-3424-a3de-683b9758a224 | -2.38613 | -49.39634 | 2025-12-03 03:46:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a5b4024a-b405-36d5-8e54-fa73ca907593 | -6.68042 | -39.50056 | 2025-12-03 03:46:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 558a8ae4-1be9-3637-a1ff-b696af44a9e0 | -6.50967 | -39.07808 | 2025-12-03 03:46:00 | NOAA-20 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1303da8c-7b3d-3e48-8709-e0b584b76736 | -6.67978 | -39.50453 | 2025-12-03 03:46:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2d763f7a-ae42-3efd-a7db-483021e66db6 | -3.25988 | -45.58689 | 2025-12-03 03:46:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3499dad3-5e37-3fbe-a80d-21613ed934e7 | -2.84733 | -46.73803 | 2025-12-03 03:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 732ee033-7ef0-3519-8806-7cf5358ef9bc | -5.27588 | -40.35147 | 2025-12-03 03:46:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 294afa29-3dff-3670-99a2-0f55522802e6 | -5.85542 | -39.94695 | 2025-12-03 03:46:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 7c9b1b66-4396-3374-8db4-6fcbf79ae728 | -2.98595 | -49.53164 | 2025-12-03 03:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 16714bb2-bd41-3cbc-993d-69f52d2f53cd | -7.50937 | -35.17031 | 2025-12-03 03:46:00 | NOAA-20 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 85cf26c4-d27b-38ac-83b7-9bfbd8f854ae | -3.85354 | -47.05462 | 2025-12-03 03:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75164d6c-6801-36f3-86b3-11dfd3caf4eb | -7.51222 | -35.17456 | 2025-12-03 03:46:00 | NOAA-20 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1ce1a1f3-0b28-380c-910c-31cc1932c309 | -3.31756 | -43.4373 | 2025-12-03 03:46:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb85320f-8ef5-33da-b052-121181edfcac | -3.86336 | -40.64116 | 2025-12-03 03:46:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| e44e44cd-f606-32df-a85d-9198df9f39e7 | -3.84461 | -47.07109 | 2025-12-03 03:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 38d2158d-21f0-3364-b879-6f3497f91ef8 | -3.22408 | -46.86639 | 2025-12-03 03:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6a82ebae-7ab8-319a-9b97-6093d5278129 | -2.17306 | -48.36766 | 2025-12-03 03:46:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b66eba53-2218-3a9f-9f61-a8b21eaf2a4a | -5.85181 | -39.94629 | 2025-12-03 03:46:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4bbc4aa5-6139-33e0-8889-e34f125d2feb | -5.65611 | -35.55212 | 2025-12-03 03:46:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 11c7093a-6cbe-356b-8616-1e45a1b4f2ba | -3.85877 | -47.05973 | 2025-12-03 03:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00474eeb-69e7-3fd6-8ff0-82a07e4e1a57 | -3.2176 | -48.62414 | 2025-12-03 03:46:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08d68a68-45fa-3a4f-92e6-55288bb810d8 | -6.90478 | -39.55129 | 2025-12-03 03:46:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6e57061b-059c-35f2-b9ef-664f9ec1c5a7 | -3.42805 | -49.23432 | 2025-12-03 03:46:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bd8551a2-a353-3c0a-91dc-c2003e880d45 | -4.80635 | -38.56796 | 2025-12-03 03:46:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 32207d62-be1b-3c13-94a9-64887fdd144b | -3.63037 | -49.49483 | 2025-12-03 03:46:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9407801a-8a99-31fb-9494-cb82d41ae092 | -3.21744 | -46.86962 | 2025-12-03 03:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c78d601d-2558-3158-890a-87600b02cb69 | -3.23384 | -45.57537 | 2025-12-03 03:46:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 36fab0c4-de60-34ef-a055-b55989c29598 | -2.62209 | -45.14333 | 2025-12-03 03:46:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7d5f6d87-9c1a-32c8-9401-dd4b634c7f2d | -2.20233 | -48.00074 | 2025-12-03 03:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| dc0aa760-650e-349b-9138-1ddb2e365a98 | -2.96219 | -48.59318 | 2025-12-03 03:46:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16c558bd-d6a4-32fe-8d15-e70ee91d6a88 | -3.86911 | -41.58151 | 2025-12-03 03:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a67c8430-d2ab-38ba-ab88-0a2b50fb2f8e | -3.44109 | -45.39426 | 2025-12-03 03:46:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 99f8d433-e98a-3c46-848e-8733c9f325f9 | -3.85131 | -47.06764 | 2025-12-03 03:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 45f8b563-be75-3668-9567-051509e0be28 | -3.24463 | -43.28644 | 2025-12-03 03:46:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9b9cc5f-1b2f-32b0-8cc9-5b38f0bb1e9a | -5.60225 | -37.72001 | 2025-12-03 03:46:00 | NOAA-20 | FELIPE GUERRA | RIO GRANDE DO NORTE | Brasil | 2403707 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fd5dfaf1-ac06-35c6-ae32-0588aee85621 | -5.54205 | -39.23901 | 2025-12-03 03:46:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 499a9496-44c3-3927-a681-f25d3c50419c | -3.33837 | -44.34048 | 2025-12-03 03:46:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| dd38e71d-bbfa-32a2-89ca-285304d6aabb | -5.85603 | -39.94912 | 2025-12-03 03:46:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8293182d-9c04-36bd-97d5-72a373e12d31 | -3.04502 | -48.42236 | 2025-12-03 03:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3cfd9d06-e903-3a3a-a876-d8144064614c | -4.28753 | -43.77314 | 2025-12-03 03:46:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 18e73bf8-92fe-37ab-a828-2e6aa7bed93e | -2.98122 | -49.51755 | 2025-12-03 03:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6643bb1a-d957-376d-bd8f-ebe52dbc358e | -3.24131 | -43.28812 | 2025-12-03 03:46:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 78c919e0-9167-3084-ba4f-263e1680ede3 | -5.0443 | -43.21827 | 2025-12-03 03:46:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 94386c72-62ca-3ed7-8bf3-f18f62de5431 | -2.61942 | -45.13956 | 2025-12-03 03:46:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5fca29a1-c239-3c73-b744-abc51d6596f6 | -5.27514 | -40.35593 | 2025-12-03 03:46:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1171d919-cfa5-303b-981f-59abe15fcbdf | -2.20142 | -48.00618 | 2025-12-03 03:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b0e95aa3-1352-3823-badd-0306f308476e | -2.82793 | -48.44642 | 2025-12-03 03:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e0f7850-a686-3bfb-8df1-d1ae291fd9b0 | -2.98008 | -49.52408 | 2025-12-03 03:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 43620cb1-6423-3369-ad84-9c44b5c690f3 | -7.41871 | -35.19133 | 2025-12-03 03:46:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7873f1cb-cc20-3217-9271-cb54b7e6a354 | -3.75726 | -50.16513 | 2025-12-03 03:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d44e1924-fa33-39b4-b289-ce390d5a1a40 | -5.74092 | -35.55068 | 2025-12-03 03:46:00 | NOAA-20 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 3ef09390-3b7d-3fb4-aa85-e9ac69769088 | -2.40517 | -45.3514 | 2025-12-03 03:46:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70450f8e-cf5e-3e2b-8b2b-be96caa7acf6 | -5.46299 | -38.49911 | 2025-12-03 03:46:00 | NOAA-20 | JAGUARIBARA | CEARÁ | Brasil | 2306801 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 01e44484-4359-33be-9d2d-ddcc5164a8fa | -3.24518 | -43.29382 | 2025-12-03 03:46:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b6e6d4fb-9cb4-3e47-83af-bbba85887898 | -3.8726 | -41.58588 | 2025-12-03 03:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 30ef1047-29e5-3d0b-a079-efa3344c89f8 | -3.19098 | -41.8507 | 2025-12-03 03:46:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 10846be5-1cc1-3ad8-8111-bf9e3546fa1d | -3.24596 | -43.28894 | 2025-12-03 03:46:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9b720ea-2f73-3b02-991d-0eae1c72c141 | -3.77246 | -50.14471 | 2025-12-03 03:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5da45610-23e5-3032-aede-12abb7f8dad6 | -3.22411 | -45.73385 | 2025-12-03 03:46:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 412e0dd2-8cf4-32a0-b76c-28cbc13c5a36 | -6.46809 | -36.19971 | 2025-12-03 03:46:00 | NOAA-20 | NOVA FLORESTA | PARAÍBA | Brasil | 2510105 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 06692ada-a9b9-3275-8339-55ddb47f1267 | -4.80696 | -38.56421 | 2025-12-03 03:46:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b6bd9bb4-9ea5-3918-9572-1c70be094200 | -2.99744 | -41.78849 | 2025-12-03 03:46:00 | NOAA-20 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6e6f0800-1c37-378b-a98b-164e05e2d712 | -7.41529 | -35.19083 | 2025-12-03 03:46:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2f826f4c-d260-3886-aa3a-11cecebcdc1a | -3.76823 | -50.14535 | 2025-12-03 03:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9bf44f37-05cf-3f16-862b-e0cf78e66e95 | -5.04504 | -43.21383 | 2025-12-03 03:46:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe9195b6-38e5-307c-b661-4593310f994b | -2.82666 | -48.44602 | 2025-12-03 03:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd27e3bf-66ef-38f7-805e-768eae88f009 | -3.76166 | -50.16433 | 2025-12-03 03:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3d0b80e4-70cf-3bc9-9b64-c05ebf6931c0 | -5.991 | -35.58233 | 2025-12-03 03:46:00 | NOAA-20 | BOM JESUS | RIO GRANDE DO NORTE | Brasil | 2401701 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| eb435e74-8ce8-38c5-850a-a188d99a584a | -5.03336 | -41.01392 | 2025-12-03 03:46:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 59a55a1c-7fa5-3cdd-a20c-da60345b0d54 | -3.04383 | -48.42449 | 2025-12-03 03:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 002cf3e3-4014-336b-a279-c979ae5fa295 | -3.55991 | -42.70969 | 2025-12-03 03:46:00 | NOAA-20 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e8bfaac-ffe0-3237-bc11-050e2c484e69 | -2.99245 | -47.90133 | 2025-12-03 03:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README6.md)
