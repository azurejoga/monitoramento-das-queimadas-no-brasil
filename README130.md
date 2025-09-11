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

## Dados Diários - Página 130

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f027c01b-72bc-377b-a7de-3883fad8f6b6 | -12.06862 | -64.16835 | 2025-09-11 06:05:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a75e87c-ad2d-3986-b109-1e31e21acd01 | -12.06396 | -64.16771 | 2025-09-11 06:05:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc5d6c37-9f6b-343e-90cc-9d206f0f1d70 | -12.06796 | -64.17324 | 2025-09-11 06:05:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 688ddf8f-0e62-3514-ad46-0b18be4c24f6 | -12.39813 | -63.81031 | 2025-09-11 06:05:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 952371d2-3af2-3ac7-ad2f-35eda8d67922 | -12.87232 | -62.12531 | 2025-09-11 06:05:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8fe82e42-d5a6-3773-9778-7f47fb3af445 | -12.40638 | -63.82186 | 2025-09-11 06:05:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 99119083-1f49-358f-a002-b7f337fd242e | -12.41323 | -63.80674 | 2025-09-11 06:05:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2bcb5d87-4745-3ffa-af12-92defe41c57d | -12.40706 | -63.81665 | 2025-09-11 06:05:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f155c73b-6a76-3a30-9436-09df9d16c86d | -19.2212 | -48.0077 | 2025-09-11 06:10:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 5a81022f-2468-3264-96e1-bc6f41eca424 | -11.6941 | -50.6202 | 2025-09-11 06:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 096c62b9-0e13-312b-8278-7d7cce5e4319 | -11.7132 | -50.618 | 2025-09-11 06:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 156.0 |
| da6c841f-f30d-368c-b7fc-cbdc72e00764 | -18.0547 | -50.7359 | 2025-09-11 06:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 380ea884-04ae-3876-8e2b-891d4b5a784b | -11.7322 | -50.6158 | 2025-09-11 06:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 2a284fa6-4257-35e9-9495-2eec2a71220f | -19.9994 | -47.6271 | 2025-09-11 06:10:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 4b33e248-7779-3858-ab0a-bd30a9e0aa15 | -19.2415 | -48.0033 | 2025-09-11 06:10:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 8d667dae-b86e-3c7d-a359-44bbfaca9858 | -11.7129 | -50.6394 | 2025-09-11 06:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 7fedc75f-c70b-363c-b979-11e0e143f4a3 | -12.8448 | -47.9682 | 2025-09-11 06:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| fe6188ae-c4e3-3831-96c8-2869c4ace143 | -11.7132 | -50.618 | 2025-09-11 06:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 150.6 |
| 6ece4b45-25d3-368a-9b4f-c8121184fe30 | -19.9994 | -47.6271 | 2025-09-11 06:20:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 5e42e1c5-0de3-39dc-80ff-4c5a6aaf244a | -11.6941 | -50.6202 | 2025-09-11 06:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| ef30ab34-a832-3945-b745-84cda8cc87d2 | -15.1016 | -50.1468 | 2025-09-11 06:20:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 02576f1f-53ac-34ff-a0e8-c7d6d10ae619 | -10.1639 | -68.18008 | 2025-09-11 06:25:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a9cd8a9-92a1-3cd7-8065-929d6412a838 | -10.46482 | -67.83791 | 2025-09-11 06:25:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f108aa7-2e9a-3095-af80-bf7e91ffabd6 | -8.57174 | -70.85538 | 2025-09-11 06:25:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b47679ed-d738-34d7-9cbd-eaf239092f2b | -10.16156 | -68.15605 | 2025-09-11 06:25:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 24abee45-06bb-33b5-a090-8a17dbd45510 | -10.16198 | -68.15271 | 2025-09-11 06:25:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f6386c6-4b64-3257-84c4-2601adb51615 | -10.17218 | -68.15749 | 2025-09-11 06:25:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 606e571a-6967-3e98-9fda-57260a03244d | -10.16687 | -68.15677 | 2025-09-11 06:25:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9c78d8ed-21b5-3576-94c7-4b99d75c590f | -10.16729 | -68.15343 | 2025-09-11 06:25:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| edc0ccda-66e2-3308-ab3e-8e1a582fcb39 | -10.16347 | -68.18338 | 2025-09-11 06:25:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b1ef03f-080f-358f-9dc4-8d40d1fd8dad | -10.46436 | -67.84148 | 2025-09-11 06:25:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64f72715-3a7c-3661-82cc-b1b40eec0708 | -12.4068 | -63.82534 | 2025-09-11 06:27:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8b3eae42-63c7-346b-a599-96713ee2fe8a | -12.06835 | -64.17484 | 2025-09-11 06:27:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3201005c-43de-37b5-85dc-6e57e46a93d0 | -12.40832 | -63.81126 | 2025-09-11 06:27:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 37fa5d86-2436-3a32-ae5a-407ce931b51e | -12.06761 | -64.18146 | 2025-09-11 06:27:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5f178f80-f3de-3d91-a169-89d9ae6e4a35 | -12.40756 | -63.81833 | 2025-09-11 06:27:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0dc23311-2374-37cc-8865-6031a90f6975 | -12.39321 | -63.8172 | 2025-09-11 06:27:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a589b7c8-8794-3fc8-9769-dfc469a090a9 | -12.06137 | -64.17407 | 2025-09-11 06:27:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 90438616-bd8e-3328-b183-127be09b884c | -12.40038 | -63.81779 | 2025-09-11 06:27:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f54e5ba7-8203-3f6d-9dd3-fe144c5e405c | -11.6941 | -50.6202 | 2025-09-11 06:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 05ad4a52-3da0-362f-8c0a-c67c388be8f5 | -15.1016 | -50.1468 | 2025-09-11 06:30:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 32f3e1ac-fbed-3e0c-9768-eb0113a19547 | -19.9994 | -47.6271 | 2025-09-11 06:30:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 4d911c53-383c-3bf1-bbc3-690a28f8cccd | -11.7132 | -50.618 | 2025-09-11 06:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 134.3 |
| c42a4294-d02d-3a33-83af-df24df554900 | -11.7132 | -50.618 | 2025-09-11 06:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 9a0d97a9-4794-36aa-8c42-5f2a45f73e97 | -11.7135 | -50.5966 | 2025-09-11 06:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| eb705ee7-fd67-3046-93ab-e062ddbef848 | -11.779 | -46.4821 | 2025-09-11 06:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 46.9 |
| c6e259f0-bed1-32d8-8ce6-dfe890a8cd8f | -11.6941 | -50.6202 | 2025-09-11 06:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 44dfb360-0815-33b0-9002-9d4f96596521 | -18.0547 | -50.7359 | 2025-09-11 06:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 00075281-4a1e-3686-9fbd-f45d509ee900 | -19.9994 | -47.6271 | 2025-09-11 06:40:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 1ce058cc-6113-379f-af41-aa851e817df3 | -15.1016 | -50.1468 | 2025-09-11 06:50:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 51.7 |
| e088b49e-bd7f-3df3-a15a-2c481c243d66 | -19.9994 | -47.6271 | 2025-09-11 06:50:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 25b1f004-86bd-31c7-8122-90857199e1a1 | -11.0201 | -45.059 | 2025-09-11 06:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| dd130276-3986-378e-a1b8-307585361019 | -11.6941 | -50.6202 | 2025-09-11 06:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 1630e9a5-7959-3904-a44a-a1e172d3b737 | -9.3058 | -46.7644 | 2025-09-11 06:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 1d76d2dc-f7fd-3281-9763-a39f50ae5e59 | -11.7132 | -50.618 | 2025-09-11 06:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 1d2e424f-0de7-394a-8035-47d3a05adbf9 | -15.1211 | -50.1438 | 2025-09-11 07:00:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 64.2 |
| b882aac4-87f3-369d-84df-b82a90e2d46e | -11.0201 | -45.059 | 2025-09-11 07:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.9 |
| f239fe17-521f-30c2-bcb5-760ba6bf8543 | -11.3584 | -46.5167 | 2025-09-11 07:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 208.3 |
| 5d4839f7-36e0-3340-928d-53e7d342c0d5 | -9.9059 | -49.9132 | 2025-09-11 07:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 0e0fca03-5dc4-3011-9408-64178d224aa5 | -11.34 | -46.4741 | 2025-09-11 07:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.7 |
| f3b759da-1f7b-3d72-bf30-63e75656d8ca | -11.3591 | -46.4715 | 2025-09-11 07:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 8ad43448-3a78-3cfa-bb57-a69f75728204 | -11.3393 | -46.5193 | 2025-09-11 07:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 9d2a3904-31d1-3f45-b99a-2553f5ee9486 | -11.3588 | -46.4941 | 2025-09-11 07:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 226.2 |
| 7677ca85-063e-36b7-9f1b-55c9fe42ecb0 | -11.6945 | -50.5988 | 2025-09-11 07:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 5823e489-3d99-340f-a4fc-51d9d33f359d | -11.3397 | -46.4967 | 2025-09-11 07:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 172.1 |
| b2212953-035f-3b9b-9111-39831069f062 | -11.6941 | -50.6202 | 2025-09-11 07:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 154.8 |
| b5957ee4-42fd-37ef-8170-94488033249f | -11.7135 | -50.5966 | 2025-09-11 07:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 6b3757f9-4b4a-3197-b7a2-dca620569108 | -11.7132 | -50.618 | 2025-09-11 07:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 162.3 |
| 04fba1b5-e621-3dfd-9aef-ccb7a58961ef | -9.79323 | -61.51909 | 2025-09-11 07:07:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 2e75f4b2-cfbd-3edb-9180-e555ff34f8a1 | -9.79228 | -61.51191 | 2025-09-11 07:07:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f029e3fa-bce1-3e37-827b-80967cc9fdb3 | -10.15819 | -68.15231 | 2025-09-11 07:09:00 | AQUA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a147e882-d68f-3c6a-8585-450999a553df | -12.06679 | -64.17085 | 2025-09-11 07:09:00 | AQUA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 24348a11-4baa-3e82-a683-d4bc7cab4203 | -11.88013 | -58.81193 | 2025-09-11 07:09:00 | AQUA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 14544053-43b7-35f5-a406-c516b452600d | -10.16786 | -68.15386 | 2025-09-11 07:09:00 | AQUA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 163a6aa0-a317-3457-942a-052ef0966515 | -12.40438 | -63.81153 | 2025-09-11 07:09:00 | AQUA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 40784c7d-f2d0-379b-ba8f-6d7131234860 | -15.1211 | -50.1438 | 2025-09-11 07:10:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 68.3 |
| f4ca9a25-32c9-3b7b-ac43-dc13f629600f | -11.6945 | -50.5988 | 2025-09-11 07:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| ffa6a4f9-2c11-3d9e-8b54-50478b6696cf | -11.6941 | -50.6202 | 2025-09-11 07:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 230.2 |
| 1959e0e6-570d-33c7-ba83-80484b044c2f | -9.9059 | -49.9132 | 2025-09-11 07:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 46bf2325-9329-336d-81e4-0f6833570882 | -11.7132 | -50.618 | 2025-09-11 07:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 125.0 |
| f19c16b3-663d-38bf-b973-8c99e68c29f7 | -11.0201 | -45.059 | 2025-09-11 07:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 3ba8348e-fe93-386f-a608-e314e470f89f | -15.1371 | -52.4252 | 2025-09-11 07:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 54.9 |
| c195d2a3-6146-30c4-ac87-41bd71e612d8 | -15.1371 | -52.4252 | 2025-09-11 07:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 56.5 |
| e4a35f41-4f43-3531-b53e-e32286da0c54 | -19.9994 | -47.6271 | 2025-09-11 07:20:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 284e294e-edc9-3069-abfc-ce43c7901537 | -11.6941 | -50.6202 | 2025-09-11 07:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 217.6 |
| 02205342-3ecd-3903-87dc-bbbcf357f983 | -11.0201 | -45.059 | 2025-09-11 07:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 1d5094e9-b130-3889-90f0-b8c931baf4c5 | -9.9059 | -49.9132 | 2025-09-11 07:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| d261855c-6b9d-3f8a-83c4-a6f7cb06b691 | -11.7132 | -50.618 | 2025-09-11 07:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 802c98de-4a4c-32d9-b075-ce26e38a0e13 | -11.6945 | -50.5988 | 2025-09-11 07:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 235281f8-6cf5-3697-94e8-955cfc2bced7 | -11.6941 | -50.6202 | 2025-09-11 07:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 92b59941-8b1f-3669-8c9c-487c51daba2b | -11.0201 | -45.059 | 2025-09-11 07:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 55a901ff-3b33-381c-a4f1-16bd9c3a9b63 | -15.1016 | -50.1468 | 2025-09-11 07:30:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 64.5 |
| c783249a-f57b-38e5-90b8-117ff81b5723 | -15.1211 | -50.1438 | 2025-09-11 07:30:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 166b5138-3c4b-32b1-9b65-89f41ae0f3da | -15.118 | -52.4066 | 2025-09-11 07:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 854b0c51-c04a-3744-8ab1-0ad29a4737ee | -9.9059 | -49.9132 | 2025-09-11 07:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 416f9602-a037-3670-9b4f-b2b535749733 | -15.1211 | -50.1438 | 2025-09-11 07:40:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 15071a8c-2737-38cc-8fc7-35cd824e9c84 | -11.7132 | -50.618 | 2025-09-11 07:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 1eb026be-51c8-396a-b975-ad1efa7d3204 | -18.0547 | -50.7359 | 2025-09-11 07:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 5a2974bc-0adb-3e97-8fae-60bfd3a13307 | -11.6941 | -50.6202 | 2025-09-11 07:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 894f8262-a71a-3de1-8d7e-aaa9c4379c6e | -9.0579 | -46.9688 | 2025-09-11 07:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |


[Clique aqui para ver as próximas entradas](README131.md)
