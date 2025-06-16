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
| 8ee0a67d-e062-3b44-b82b-b87504365aab | -7.92861 | -47.80703 | 2025-06-16 04:25:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96c828fc-599e-3c99-a52f-0d4c86dc77a3 | -7.11508 | -44.03143 | 2025-06-16 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 716092f7-cf90-3fa4-afd8-2d2417d6b86e | -7.64342 | -48.31372 | 2025-06-16 04:25:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| ddaa805f-ab18-333e-895b-1525367f28de | -6.99417 | -42.10821 | 2025-06-16 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dd56e519-eece-3f01-9734-97d849ca6e3c | -7.11797 | -44.03591 | 2025-06-16 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19a846b1-30cb-35c6-90d3-b48a99907d52 | -5.00623 | -46.87359 | 2025-06-16 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2eb5c5d7-e67a-3020-a215-1ed8b69c9cfe | -5.00291 | -46.87308 | 2025-06-16 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b438f30c-7e43-302f-9190-f13e9031351b | -8.07233 | -43.11183 | 2025-06-16 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4ace5137-d160-33d4-9a97-b0aabd4f22a4 | -7.12436 | -44.04091 | 2025-06-16 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 837a7ddc-0d33-3c33-8a79-8e1931fbd4ae | -7.92584 | -47.80296 | 2025-06-16 04:25:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a34154e-0f8b-3e8d-a71c-bbefbf748d00 | -7.14115 | -47.27782 | 2025-06-16 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 674681a3-46f0-3dc3-b14f-f075f4b9e076 | -7.11449 | -44.03532 | 2025-06-16 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc0965bd-5027-3eed-82e6-b77df381cbe6 | -7.11562 | -44.05151 | 2025-06-16 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd1f440e-3d58-3435-9a40-b1625b4834a4 | -7.12264 | -44.02861 | 2025-06-16 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bec17fdf-4eb4-3942-9b6d-2d6a07329072 | -3.77852 | -41.67038 | 2025-06-16 04:25:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f1ceb6a6-62b9-3ca6-bcf6-1abe407f9bfa | -7.14004 | -47.2848 | 2025-06-16 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ab2ae594-22d5-3cbd-868a-4701ef360e9f | -7.644 | -48.31009 | 2025-06-16 04:25:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 0b35ad73-f7ae-356c-ab88-832989e1bbae | -7.12725 | -44.04535 | 2025-06-16 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e1a584b-c74f-3bba-ad71-d677924666d6 | -7.12844 | -44.0375 | 2025-06-16 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9b6a275-face-3fde-8308-a60a41237cbd | -7.1406 | -47.28131 | 2025-06-16 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d3635090-ffdf-3c5b-bc2f-45f8852bc43f | -7.11391 | -44.03921 | 2025-06-16 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 75ab1d3f-bd6c-344e-b74a-82b733dacd7a | -7.12028 | -44.04428 | 2025-06-16 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 87194b42-f065-3883-924e-cec657412361 | -7.12205 | -44.03255 | 2025-06-16 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6cc8747-86cb-3079-a591-b1e3b3e2668b | -8.19501 | -43.75479 | 2025-06-16 04:25:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 956ca7f5-99cf-3c3a-a9d5-13476318ad9a | -7.11739 | -44.0398 | 2025-06-16 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1cee940b-5d5a-3532-8fa0-b1deb828c069 | -7.11042 | -44.03865 | 2025-06-16 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 696d7fe7-bf37-3a3a-b3b6-8da074dc7e6d | -7.92528 | -47.8065 | 2025-06-16 04:25:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79df3056-c284-303f-b8fb-1c35f1544dca | -7.64283 | -48.31737 | 2025-06-16 04:25:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b2ff354f-355a-3ac2-b892-0ca87905eda2 | -7.12495 | -44.03699 | 2025-06-16 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71a5ea61-e3c2-31f8-8166-88b52f3f5a21 | -7.12146 | -44.03648 | 2025-06-16 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad5b0f00-3d1c-3e14-83f4-08d3359d9570 | -7.11332 | -44.04311 | 2025-06-16 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8836827a-74fe-392c-8ec1-939e362a0067 | -8.26703 | -47.0024 | 2025-06-16 04:25:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3486b908-39e4-3dc6-9d60-1918f26e37f7 | -6.87155 | -47.23822 | 2025-06-16 04:25:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6b2e3d84-43f4-3008-81df-b7f6e20f42ac | -7.12087 | -44.04038 | 2025-06-16 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 80899859-9a95-376a-9d90-a6cf5a6bb990 | -7.11779 | -47.51104 | 2025-06-16 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 485a1349-d007-3475-8cbb-042c279ee304 | -7.11621 | -44.04759 | 2025-06-16 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eaed7458-b7ff-3031-b92b-e28ed459566f | -7.11856 | -44.03201 | 2025-06-16 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a24f9c5a-fac0-3554-a786-c6481b5542c3 | -7.12318 | -44.04872 | 2025-06-16 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7977c0a-ede7-3f5d-a9de-43ef6707fcdf | -7.12324 | -44.02466 | 2025-06-16 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 22d98d9c-968f-3ffe-9deb-8e835d8dc5aa | -5.68608 | -46.57354 | 2025-06-16 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d4eced8-2d3d-367d-8ec8-3031c33696ed | -7.11446 | -47.51054 | 2025-06-16 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3dadab40-3d2e-313c-90fb-35ac8e0509fd | -7.14502 | -47.27483 | 2025-06-16 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8796f894-f231-310c-b225-d79e1f216091 | -7.1168 | -44.0437 | 2025-06-16 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 83dc04dc-d237-3ae3-b84c-1e7ca03af71a | -7.12377 | -44.04482 | 2025-06-16 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a05fee74-76bd-324d-a0a5-fea6cce3f9ff | -8.07094 | -43.1145 | 2025-06-16 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ecf70679-0664-3c06-9560-cce0fc7ed6a3 | -7.93194 | -47.80755 | 2025-06-16 04:25:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2fe26240-17f1-3c0e-bb71-79ff6c14f243 | -12.75955 | -44.40702 | 2025-06-16 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e60d7517-2892-3432-8876-1dd6f96c5911 | -11.13545 | -53.91496 | 2025-06-16 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70a4ec81-441b-3a78-93fa-ad01594dab1d | -13.9155 | -54.61929 | 2025-06-16 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ecee68bb-9178-3ada-a534-713a180f21c9 | -12.08966 | -49.48985 | 2025-06-16 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 03a1ecaa-5757-3ebd-806f-73f980a0a5a0 | -11.00535 | -55.05424 | 2025-06-16 04:27:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 75d13865-de69-3122-b154-0739581d59a9 | -12.05507 | -48.07991 | 2025-06-16 04:27:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a1d8454a-1110-3c19-8f54-6d9487e6e854 | -11.14029 | -53.93828 | 2025-06-16 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 5ff0b952-5525-3d17-899b-9a8a83ca4fe3 | -11.01156 | -55.05227 | 2025-06-16 04:27:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 0a9038c1-42fd-3114-a435-289aa895bed3 | -10.21978 | -51.6517 | 2025-06-16 04:27:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b096fad-6ed0-35ff-a18e-f0024febde2d | -12.08943 | -52.57751 | 2025-06-16 04:27:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b99cf291-89c1-3993-96af-e8e22684fa13 | -11.00682 | -55.05142 | 2025-06-16 04:27:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 411b1749-9a80-3784-843a-543daf71ac71 | -10.78485 | -55.45205 | 2025-06-16 04:27:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 70a8ef22-fe7b-3a2f-93fb-09513f66e4fc | -12.76258 | -44.41191 | 2025-06-16 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f3d4768a-d7be-31f2-a22d-2465f2f37ccb | -12.52438 | -57.22398 | 2025-06-16 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e1d8c8a-0212-3480-9fd9-31169e639c11 | -10.44854 | -47.95087 | 2025-06-16 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f6c68f8-f175-3759-9c76-a3df61d8f710 | -15.40495 | -47.84513 | 2025-06-16 04:27:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9799ef71-5d33-3784-ba9a-b5b1278c93eb | -12.05562 | -48.07639 | 2025-06-16 04:27:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8e42b119-7815-3cc4-b2ac-ddb1ea76c26d | -9.40523 | -48.43365 | 2025-06-16 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71391d34-f404-33bf-b12f-af22695293b4 | -13.91782 | -54.63289 | 2025-06-16 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ca546d18-68cc-360f-b07e-6e3cb360a32d | -11.01115 | -55.07663 | 2025-06-16 04:27:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7545a8e3-302f-376c-b44f-4c641aade750 | -10.22423 | -54.29594 | 2025-06-16 04:27:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d4d9d132-f924-3d52-854a-68e7eedc19ca | -11.98806 | -57.19317 | 2025-06-16 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be4f6fe0-71f5-3b49-a7ea-8b28be101d3a | -8.89989 | -48.84702 | 2025-06-16 04:27:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d5fee7e7-3aef-3de2-9e25-ef7b98e8ee6e | -11.00869 | -55.0676 | 2025-06-16 04:27:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 038851dc-77cd-3631-a5b9-09d79a867a06 | -12.72375 | -46.2765 | 2025-06-16 04:27:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25dbb88b-78f3-3a2c-b2dd-492503ade5e5 | -9.16766 | -45.32606 | 2025-06-16 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 256fe439-593c-388b-8605-1e830c1ab484 | -14.82255 | -48.41996 | 2025-06-16 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 406befbd-40d7-337b-99b3-122e4f7f64cb | -11.13949 | -53.94267 | 2025-06-16 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 79b2e4d7-89ed-341d-9825-2a6c7c7743cf | -9.45957 | -57.84727 | 2025-06-16 04:27:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c34959d9-8434-38bc-90bc-260aa2ddce50 | -14.83459 | -48.45105 | 2025-06-16 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 67fcc833-a10c-3680-be3c-e3f5d549c34b | -10.85173 | -53.77767 | 2025-06-16 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| da24cdcf-03ab-39eb-af09-64e8041937c7 | -14.82744 | -48.45348 | 2025-06-16 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee8fddd8-f260-3389-a32d-af4691ebc75c | -10.73835 | -44.49468 | 2025-06-16 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec8feaae-73fb-3969-9f5b-c42bb1d73ab1 | -10.85328 | -53.76901 | 2025-06-16 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0b7e8bb-e790-3864-b8d3-032239884418 | -11.00966 | -55.06244 | 2025-06-16 04:27:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| a6388b9f-6cca-35fe-bbda-ea4ef940649e | -12.02987 | -57.09012 | 2025-06-16 04:27:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ee697d7-6ac5-3179-b96a-8eca02f38352 | -14.0322 | -55.12288 | 2025-06-16 04:27:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3411686b-ba4e-3e86-ae12-5fe84bfa94a3 | -9.40916 | -48.43058 | 2025-06-16 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8ef06f8-5fbc-3d3b-b07e-b35933b649ea | -11.013 | -55.06625 | 2025-06-16 04:27:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0688853f-74c4-3c0d-8248-5ae412e98621 | -11.03087 | -44.64665 | 2025-06-16 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d670027-9f2a-3fc8-82f0-021c1da482aa | -11.14548 | -53.93465 | 2025-06-16 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 224a6730-033b-3eb0-ac16-e6da66acf515 | -12.76319 | -44.40758 | 2025-06-16 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 599f56e2-1f52-384b-95af-fd32baf68740 | -11.47714 | -48.54745 | 2025-06-16 04:27:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b981ce2-fb2a-3ad7-9926-bbd7a03c26d8 | -11.00298 | -55.07188 | 2025-06-16 04:27:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8471fb6c-1086-3f1f-b864-418f3ac76ae4 | -10.56844 | -52.0152 | 2025-06-16 04:27:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 57bd892e-7ba8-3e7a-951e-614e42649782 | -10.22363 | -51.65235 | 2025-06-16 04:27:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4fb38aa7-5dcf-38ce-bd19-8665bcd30cca | -15.05651 | -49.47267 | 2025-06-16 04:27:00 | NOAA-21 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 1f67e3c2-a66b-38d6-8708-2b1ed976a602 | -14.82581 | -48.44231 | 2025-06-16 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 043a70d0-0203-38b8-ab8c-7bb6dc21af7b | -12.76292 | -44.40532 | 2025-06-16 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29f123ca-4c63-3e3a-a8c9-2742982a3c3f | -11.00826 | -55.06536 | 2025-06-16 04:27:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 1ece9baa-5264-3e04-a166-4e194e5b0b8f | -10.22879 | -54.29681 | 2025-06-16 04:27:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a8e766a7-75b4-37ed-b93e-d3bb08651949 | -11.00676 | -55.07792 | 2025-06-16 04:27:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 21164592-3998-3f7f-9775-057339092254 | -9.41194 | -48.43473 | 2025-06-16 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54dc1370-749d-3504-b029-b7ce65c6e5e9 | -12.72428 | -46.27298 | 2025-06-16 04:27:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README6.md)
