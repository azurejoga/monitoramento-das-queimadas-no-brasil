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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d97758d-1711-3fe0-a7b3-bbfc61d5462e | -0.9815 | -53.6789 | 2024-10-27 03:25:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 6e4f4832-33ee-3353-973d-0fa8b9200175 | -0.9998 | -53.719 | 2024-10-27 03:25:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 27ac2921-a3a5-31e8-ad8d-892a8e57c887 | -0.9998 | -53.6989 | 2024-10-27 03:25:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 110.5 |
| ae893c7c-9627-357e-8895-4d18a1b7c0cc | -2.4753 | -45.8338 | 2024-10-27 03:25:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 32.7 |
| ded38a33-ec25-3e8a-9640-d26a8f55a5fe | -2.4786 | -50.2858 | 2024-10-27 03:25:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 35035c4c-dd4a-39f7-ae82-d2a9383dbefc | -2.6321 | -54.2975 | 2024-10-27 03:25:20 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| c6e8ed19-bcc8-326a-a20e-df29c8043237 | -2.7033 | -49.33 | 2024-10-27 03:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 1350ca30-c247-3d9c-b377-f342d5bf477e | -2.7034 | -49.3088 | 2024-10-27 03:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| e85cbf1f-4af5-330b-98ad-13ba0e064973 | -2.8329 | -49.2626 | 2024-10-27 03:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 62995b0f-3965-3c55-8082-430d7eee2898 | -2.833 | -49.2413 | 2024-10-27 03:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 7b8c4fcc-407c-3301-81a4-707e36fe2bd6 | -2.8514 | -49.262 | 2024-10-27 03:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 9d8bf8a0-4a7d-37a5-99c4-073bd7a5f009 | -2.8515 | -49.2408 | 2024-10-27 03:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 61635d9d-7584-3d0b-bc08-d6cf44f3c544 | -2.9161 | -51.751 | 2024-10-27 03:25:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| e38f37f0-635b-3fbd-ba9f-9fb4cfb32fea | -2.9214 | -50.295 | 2024-10-27 03:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 2119d6c3-4aff-365e-9afd-0a5c8e15dde8 | -2.9215 | -50.274 | 2024-10-27 03:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| ee74281d-65d2-3d78-9818-dccc9c4cc336 | -2.9345 | -51.7711 | 2024-10-27 03:25:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 5db6b629-e251-3e06-801c-c712c4e0b7a3 | -2.9345 | -51.7505 | 2024-10-27 03:25:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| cc777176-f046-3fb0-b6ef-ae9e7a68e404 | -2.9399 | -50.2735 | 2024-10-27 03:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 557199b2-c92c-350b-ae92-e6b326ab3558 | -2.9669 | -53.0389 | 2024-10-27 03:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| e129e098-cc2f-33dc-9f0e-616f7254f250 | -3.7573 | -45.7858 | 2024-10-27 03:25:26 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 013b2154-d481-3b68-a65d-f8f1aead7d0d | -9.9497 | -36.2836 | 2024-10-27 03:26:00 | GOES-16 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 69.5 |
| 22b8ccd5-f995-3fdb-a2e7-89c868498495 | -0.9815 | -53.7192 | 2024-10-27 03:35:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 4b22e265-375f-3d20-bce0-a50732a4d9eb | -0.9815 | -53.699 | 2024-10-27 03:35:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 154.7 |
| 7671c4aa-fe87-3422-8324-7ca5e07e52da | -0.9815 | -53.6789 | 2024-10-27 03:35:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 872c7168-a661-302e-adb4-0368a12559ed | -0.9998 | -53.719 | 2024-10-27 03:35:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| ef1999ea-0d06-3164-9771-77c279f5de49 | -0.9998 | -53.6989 | 2024-10-27 03:35:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 6e433c59-093f-3bde-8234-0c32cdba6cc8 | -1.4407 | -53.4321 | 2024-10-27 03:35:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| a1e0072b-b184-372d-a647-6c59062a2e34 | -2.4753 | -45.8338 | 2024-10-27 03:35:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 3d4ebbd8-6460-3492-a2dc-5eda232b0db2 | -2.8145 | -49.2418 | 2024-10-27 03:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 0512469f-f2be-3bc2-9f97-f46b3754bdda | -2.8329 | -49.2626 | 2024-10-27 03:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 132.0 |
| 4d23652b-2e60-3ab2-9378-226dbfed49bd | -2.833 | -49.2413 | 2024-10-27 03:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 149.0 |
| 81e3c30f-d8ef-374f-a18e-38fcf133e1cd | -2.8514 | -49.262 | 2024-10-27 03:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 0b4d3788-dfe5-3935-a082-fe1df6316b79 | -2.8515 | -49.2408 | 2024-10-27 03:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 2d4ffdb9-abfc-3020-9d46-2858073aa224 | -2.916 | -51.7716 | 2024-10-27 03:35:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 515d9115-cc77-3fb0-b29f-84aad14ae1c3 | -2.9161 | -51.751 | 2024-10-27 03:35:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| ee3f4897-de77-35d3-8ba5-540d8ffab39a | -2.9215 | -50.274 | 2024-10-27 03:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 9e866836-5606-322d-a202-e0ac25f84139 | -2.9345 | -51.7505 | 2024-10-27 03:35:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 7b05fee2-b450-3e0e-afe1-60fd4f047ab3 | -5.1921 | -43.308 | 2024-10-27 03:35:34 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 96e0e1de-3d52-31d5-8970-acca74ee941a | -5.19518 | -43.30124 | 2024-10-27 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 01edf481-4f0a-3c34-8891-6478bc7bc4bd | -5.19451 | -43.30502 | 2024-10-27 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| d6d06384-fa16-39f7-88d1-85eddf67b6e8 | -7.76688 | -35.07595 | 2024-10-27 03:36:00 | NOAA-21 | ARAÇOIABA | PERNAMBUCO | Brasil | 2601052 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d4e2ba2b-4042-3d4d-8002-4b0632e94c6d | -5.46964 | -36.80906 | 2024-10-27 03:36:00 | NOAA-21 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 34da5790-f606-3f5f-87ba-98b3a0837bfb | -7.71707 | -37.43217 | 2024-10-27 03:36:00 | NOAA-21 | INGAZEIRA | PERNAMBUCO | Brasil | 2607109 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4d5daf8c-e48f-3b7d-bfbe-4021592f01ee | -7.48104 | -37.40528 | 2024-10-27 03:36:00 | NOAA-21 | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 13812b2e-dbd1-3c6d-8ef4-08c9e3946cdd | -7.47807 | -37.40571 | 2024-10-27 03:36:00 | NOAA-21 | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 5af8eb23-c67f-3841-9ccf-2916f4cc00f6 | -5.93858 | -38.12944 | 2024-10-27 03:36:00 | NOAA-21 | RODOLFO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2411007 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fcbf8788-2d77-3d37-98c0-9913d5d4f960 | -5.69105 | -38.04268 | 2024-10-27 03:36:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8997cb6b-db4e-3f7b-b133-244e474acf61 | -5.68795 | -38.03709 | 2024-10-27 03:36:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 66a22ce3-59e8-32d7-8c6e-aa88df8bff0a | -7.56343 | -38.7506 | 2024-10-27 03:36:00 | NOAA-21 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 76169ce9-968a-3584-85ad-2bd9f5c3ffb6 | -7.56285 | -38.75413 | 2024-10-27 03:36:00 | NOAA-21 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 1697bcde-1c23-3d55-be4d-f4043f232999 | -7.55944 | -38.75 | 2024-10-27 03:36:00 | NOAA-21 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a49f7807-411d-31a6-9551-f3acb6eabf6a | -7.55884 | -38.75356 | 2024-10-27 03:36:00 | NOAA-21 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 62bb8d68-bc07-30cf-bcbe-c4dc6db20ee1 | -7.55484 | -38.75299 | 2024-10-27 03:36:00 | NOAA-21 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ff22b148-84f6-3f61-861b-f97e015b3815 | -7.55085 | -38.75232 | 2024-10-27 03:36:00 | NOAA-21 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6b67a45c-aa80-30d6-b17e-6f397646b53a | -7.48793 | -39.05278 | 2024-10-27 03:36:00 | NOAA-21 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 99ea59ca-0dfd-39f7-83be-bf83541cc26a | -7.48446 | -39.04853 | 2024-10-27 03:36:00 | NOAA-21 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b5d2f3a1-2042-3e98-873c-da768d5b29f8 | -7.2898 | -38.93824 | 2024-10-27 03:36:00 | NOAA-21 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2dc86885-8fe9-3a6f-9246-f94dd5acbabb | -7.88635 | -39.16996 | 2024-10-27 03:36:00 | NOAA-21 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 3ea358b3-c7e8-3265-8fa1-ab9b8d40580b | -7.88573 | -39.17363 | 2024-10-27 03:36:00 | NOAA-21 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 45317dc9-2588-304e-8f3d-b9003a263abc | -6.50184 | -39.69113 | 2024-10-27 03:36:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e9b88b7c-c0f3-3895-a32c-5a546ac863bb | -6.50114 | -39.69528 | 2024-10-27 03:36:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 36b4dc25-8fbb-3d19-b5d6-7d33ad42d7a5 | -6.41647 | -39.55471 | 2024-10-27 03:36:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 218dfea5-5f94-3b9f-8a11-8c7ea07ae93c | -6.40744 | -39.87341 | 2024-10-27 03:36:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| df6765ad-241b-3f25-866f-db4410bfedc9 | -6.40658 | -39.69183 | 2024-10-27 03:36:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0b8ff346-a78c-36fc-ae0e-9e0e5778af70 | -6.04503 | -39.82386 | 2024-10-27 03:36:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 3ccf7274-99e9-36b6-b8d8-357b0eefd617 | -6.0443 | -39.82819 | 2024-10-27 03:36:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 8cef6ec0-eb0f-3e12-8a39-b81ce95e51c2 | -6.04064 | -39.8231 | 2024-10-27 03:36:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 4037ae61-84e3-39aa-99a3-5eaec8cdae74 | -6.03989 | -39.82757 | 2024-10-27 03:36:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 47c302f1-7286-383a-b7ca-753f32299fe0 | -5.87429 | -39.21407 | 2024-10-27 03:36:00 | NOAA-21 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| cf141a63-9402-3bf9-a46a-c2a8420f82e2 | -5.87426 | -39.2136 | 2024-10-27 03:36:00 | NOAA-21 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 3da26bc5-ca0b-3834-9968-b33a7371d002 | -5.87003 | -39.21295 | 2024-10-27 03:36:00 | NOAA-21 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c3a154f8-89ac-3f4f-b7f7-954f3f4c0b89 | -7.56859 | -39.88423 | 2024-10-27 03:36:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7c4d8e7f-5c06-3250-9980-75aade8789ed | -7.11135 | -39.58385 | 2024-10-27 03:36:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4e638e78-0482-3b11-a99b-514e2c10b6d4 | -7.08053 | -39.53399 | 2024-10-27 03:36:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f2f2ab95-7950-3aec-96c8-0053cc6fd6ef | -7.06816 | -40.00762 | 2024-10-27 03:36:00 | NOAA-21 | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| dbbab863-e99c-3e55-8127-36fe1c3bd362 | -4.29321 | -40.59889 | 2024-10-27 03:36:00 | NOAA-21 | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a53954bd-baf0-3228-bd30-3a11b0dbb96c | -4.07302 | -40.47519 | 2024-10-27 03:36:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 992e45cd-771a-393a-8efd-d74ebee247a6 | -4.06738 | -40.4797 | 2024-10-27 03:36:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 69a11daf-6ec0-3099-978f-bfc0a74b1ba4 | -6.5509 | -40.51086 | 2024-10-27 03:36:00 | NOAA-21 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 7.6 |
| f59a0d7d-3fca-36b4-8042-3581284d7543 | -6.29104 | -41.91034 | 2024-10-27 03:36:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4b59cebf-8fd1-3ac3-a33e-16dda663f14f | -6.29046 | -41.90886 | 2024-10-27 03:36:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 099f2de3-27e9-3488-b9fa-92c252096688 | -5.69802 | -41.64302 | 2024-10-27 03:36:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0f5033e3-8198-3a25-a955-7b914b7c8ddc | -5.69302 | -41.64217 | 2024-10-27 03:36:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 01af8b29-bf61-3223-a7f8-d363cd836a28 | -5.69252 | -41.64506 | 2024-10-27 03:36:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f8be8eca-ca8d-3f8f-84db-92c7818bcd64 | -5.692 | -41.64797 | 2024-10-27 03:36:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c992069d-f095-3328-8994-dd8fd412a694 | -5.68752 | -41.64421 | 2024-10-27 03:36:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| db6f39c8-4068-39f5-b67d-165f3add20ee | -5.65949 | -41.83298 | 2024-10-27 03:36:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f68f2103-f0f8-310b-80c7-a15586fabfbf | -5.65605 | -41.83121 | 2024-10-27 03:36:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 848442c1-8dd6-358f-9c0c-dc4f06546f2e | -5.65505 | -41.83715 | 2024-10-27 03:36:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 338fb130-4dbf-35b8-bd30-a850deae227b | -5.6539 | -41.83514 | 2024-10-27 03:36:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e559ac71-68db-3264-a6b0-89dfdbb90a31 | -7.26001 | -41.22486 | 2024-10-27 03:36:00 | NOAA-21 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ae83cd6a-2cd9-3a7e-94fe-38d5d2ea0842 | -7.25832 | -41.22759 | 2024-10-27 03:36:00 | NOAA-21 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1d3e269c-ec30-3f4b-a108-d578cfc61ac6 | -7.25356 | -41.22691 | 2024-10-27 03:36:00 | NOAA-21 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 4ee29b77-4466-3950-b461-7a9b1e5409a1 | -7.2527 | -41.23194 | 2024-10-27 03:36:00 | NOAA-21 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 43de2468-1f9f-32c3-95df-92eb911878da | -7.24879 | -41.22633 | 2024-10-27 03:36:00 | NOAA-21 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| b1c0fb5d-e562-3c1f-86de-dfbbe5a6ccfb | -6.95781 | -41.31462 | 2024-10-27 03:36:00 | NOAA-21 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| a201392b-fe0d-38d8-826b-244367d78052 | -6.95689 | -41.3199 | 2024-10-27 03:36:00 | NOAA-21 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 40dd1fb1-251c-32cf-b200-7a129cf27cc9 | -6.95419 | -41.33522 | 2024-10-27 03:36:00 | NOAA-21 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 26c14a0b-55c9-32f0-b5be-32026a044889 | -6.69206 | -40.89142 | 2024-10-27 03:36:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f7edb3ca-a1ff-37dc-a3b6-598a0feb3b32 | -6.69122 | -40.89625 | 2024-10-27 03:36:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README27.md)
