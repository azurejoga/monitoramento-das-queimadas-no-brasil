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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a0e4cd0-725e-349f-b3f9-eb9f86c8835f | -1.7546 | -52.37716 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9248705-9832-31bf-aa5b-bd913b12b15b | -0.79833 | -51.78204 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 55ef4ef6-e256-3cec-a623-944f069789ae | -2.68014 | -46.24236 | 2024-11-21 04:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 46051a06-d7ff-3f79-9182-96381539f048 | -2.40288 | -48.60775 | 2024-11-21 04:53:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce0bb44d-c2af-3546-bd1d-a92c54c2fbba | -2.19936 | -53.67687 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff2dd524-4ee9-3752-989f-2b9e519b409e | -1.91548 | -53.34358 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de398661-0721-3112-9ef1-d6009f129215 | -2.94888 | -48.33863 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 507b7f78-15a4-3e6f-aacd-22ad43ec2c7f | 0.14191 | -51.09077 | 2024-11-21 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a0b10b8-ec4a-384f-903c-3ea847afd1c1 | -2.47653 | -49.17667 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 73997f39-752c-3d5a-a39c-e250ab8f19ab | -1.24174 | -51.74913 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4697f3e3-7bf5-30f9-8486-024f7d96fd4a | -1.8964 | -53.3335 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8b9d7ed1-4b7d-3879-b95a-fc28a289e476 | -1.28099 | -54.55056 | 2024-11-21 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 94fcac68-92a7-391b-9001-1292bb0170f1 | -0.95728 | -51.72351 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7bece237-0dd0-3b9b-98dc-1ef3ae589baf | -2.60942 | -48.2192 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 68da2016-f0b2-337a-93f6-51acc755e515 | -1.52935 | -55.37989 | 2024-11-21 04:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 54d5f68b-b582-3cb8-b9e6-b1b012bad1a5 | -2.21862 | -50.38844 | 2024-11-21 04:53:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94bbb079-4ae9-3803-a757-c2b1a437e7d3 | -2.28609 | -51.09945 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 941de2ab-fd7f-3200-b486-e0519d68b280 | -2.62163 | -48.32941 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b54d9a56-f01d-3d93-87e6-2c28517b8e2c | -3.58958 | -43.63748 | 2024-11-21 04:53:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0e97613f-5ca8-30cf-ba30-6b9ae71ff1b2 | -2.19052 | -53.66844 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c92fcd6b-4a6b-3970-a1d4-43555f00cd45 | -1.44901 | -47.11812 | 2024-11-21 04:53:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c53b2f0e-defe-37c9-a628-05da4dd9657d | -1.112 | -52.12094 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1847be6c-d553-358a-9d7f-f173000fe652 | -1.96782 | -48.3839 | 2024-11-21 04:53:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e1bec4a-5f2a-3f5c-888a-3852b9801368 | -2.90658 | -48.31771 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93cc9f24-ff20-34f0-9569-93f4b0c32f0f | -1.32948 | -51.86026 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8cbb80b-f74f-3261-b00e-0e439377823c | -2.6716 | -46.23623 | 2024-11-21 04:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bfb37bc4-e06c-3081-8260-11a04321429b | -0.89201 | -51.72427 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f27bed74-abb8-3084-9e82-2c601f5f1949 | -1.72867 | -52.39057 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 096921a5-1e14-332a-b780-a4cf88365e10 | -1.09864 | -51.74912 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3feb85b4-879e-3258-9942-146517ff9d88 | -2.33737 | -47.41244 | 2024-11-21 04:53:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e15fabf0-9438-38d6-ac1f-5faa3a0a59a7 | -0.33721 | -51.56266 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 390c0f28-da1b-30e4-b231-ab95060b2500 | 0.14134 | -51.08717 | 2024-11-21 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b97fe6a-0a96-311a-8c4a-ff8d379f5925 | 0.41734 | -50.81436 | 2024-11-21 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 870198ca-20ac-3ff2-b2d5-a38217e64b95 | -1.50698 | -52.0928 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f4416ea-a629-312a-8729-e4e9862c5a25 | -1.39291 | -55.18095 | 2024-11-21 04:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7fa6380b-f78d-344a-9dbc-b7009f4e2b0c | -1.74919 | -50.47469 | 2024-11-21 04:53:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 839da585-7cdd-33f7-adb3-523cf568c76b | -1.6839 | -55.02316 | 2024-11-21 04:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d30dc6ca-2e3f-3b72-80a3-0be181bd05c6 | -0.30428 | -51.57566 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 73a24829-8f7a-331c-ad20-ab0eb058594b | -1.39355 | -51.99283 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2abc8fa0-f28a-3630-a81f-0a5621c9d736 | -0.83603 | -52.55945 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dfe64032-d30b-3762-9b22-c829987e7df8 | -1.18622 | -53.7233 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 265a4c12-c0de-3dc8-b632-ddefe90270c2 | -0.8132 | -51.59983 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f4d693c-eda4-31b8-be48-616b6e4fe1a4 | -1.76664 | -50.85636 | 2024-11-21 04:53:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f23f4bb5-f35a-3e41-af68-2c06ba136045 | -1.39233 | -55.18471 | 2024-11-21 04:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b6c159e-b87a-3212-a999-296a7a1519cc | -0.77211 | -51.75276 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce42e459-8125-32f3-8e6e-e1b598f721bd | -2.20697 | -49.54702 | 2024-11-21 04:53:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8eb1dddd-a00f-3ed6-8dee-ca96538f5209 | -1.46526 | -52.68217 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c54795d-bea9-3771-ad11-2f378c836718 | -1.33153 | -52.2369 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fa8a23e6-b538-3cca-bff0-e5467568347b | -1.98479 | -48.71286 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40c2cc7d-e401-3792-a73d-fdf1d3cf8366 | -1.14763 | -53.51542 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac636e93-6a62-3a91-b59a-01bf7fa72bd9 | -0.19408 | -51.16831 | 2024-11-21 04:53:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4629f27c-873d-3d87-9d45-3bf0a7205433 | -0.70709 | -51.67026 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b1ad9e1-bbc1-3461-9edf-13af8c743766 | -1.10066 | -53.18734 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17fab3db-1858-3aaa-809f-d26bcd77d13d | -2.02583 | -47.00226 | 2024-11-21 04:53:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7993b7a6-7782-3505-bd45-d136229a5b4c | -2.62035 | -48.06622 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd76d1ca-ad9a-33a7-8a49-3b63ddcf1512 | -3.22812 | -43.27288 | 2024-11-21 04:53:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9b86afa9-c48b-329f-b512-3409630d5cce | -1.15461 | -53.66491 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| af7b2a5d-d678-3b5c-8eaa-8033236a5155 | -2.13389 | -50.70208 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87f2310a-9a85-3299-9588-065d4491b2b0 | -0.79018 | -52.46037 | 2024-11-21 04:53:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3fc14297-6d8e-3865-9cae-eb136f7c641a | -2.21101 | -53.71047 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dea581ee-6b0d-32e4-ab41-a1cbf591f5ba | -1.61594 | -53.28228 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ce1f2e2-b814-3de4-b042-a869af28e021 | -1.78428 | -53.61545 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4faeb369-1cab-334d-a8e7-369a9eae8569 | -0.86884 | -51.85044 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c00181b9-a09b-36af-8f08-253cc6778d2f | -1.76742 | -54.23623 | 2024-11-21 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d3b67448-b092-3a5a-a8d3-67a0d8662046 | -1.1048 | -53.61477 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49e33de5-2396-3965-b183-c5290e1f7f69 | -1.78759 | -53.61597 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a79168c9-0883-3223-a2b5-ff5933456a91 | -1.50498 | -54.39809 | 2024-11-21 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b9c86c99-cf4e-38f8-b86b-7f3d61eb59bd | -1.91431 | -55.40283 | 2024-11-21 04:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6432b592-f200-3e6e-94b9-1caa9674547c | -1.27909 | -55.67941 | 2024-11-21 04:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3aec649b-1740-3af8-b86a-a2864ac703bc | -2.16843 | -51.96798 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 56fa4581-ec06-37af-bb53-b08db7e88fe4 | -1.28192 | -54.55348 | 2024-11-21 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5437f7e-47e6-30b1-bf96-62720aed52ec | -1.46304 | -52.67478 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 9e8543ac-1c8b-39ed-ad02-bdc22281f397 | -2.61213 | -49.25192 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2045abe0-40c5-3649-aebc-e2d144a0cd4c | -2.60888 | -48.22274 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05125f3d-1978-3ffe-91c5-297f72eaf237 | -0.91437 | -51.77829 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60f354d5-6d22-3f30-b0d3-43329be770ed | -1.56645 | -55.12318 | 2024-11-21 04:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a3e8744-450b-384c-82ae-faed11a8beb7 | -1.20763 | -53.69458 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ec62519-f7d6-354e-bcad-461484743247 | -0.93775 | -51.71688 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70e98cb1-bd94-34ba-865b-235d5f5a8879 | -0.18198 | -51.61886 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8d788808-5a1d-3725-a96f-ec6865224d55 | -1.70732 | -52.48297 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65b20aff-5e72-36ae-aa6f-a2cca6370665 | -1.07586 | -53.36636 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 44ea075b-eb45-311e-baa4-8c741f37b9e2 | -1.71341 | -52.48745 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 075d513e-9701-3157-bfcb-c29910a842e2 | -2.10311 | -50.36362 | 2024-11-21 04:53:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a699f927-bfc6-38dc-80f6-3d0067b5a196 | -2.01978 | -54.53642 | 2024-11-21 04:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7dff122a-6317-38f7-8c7f-08380c4a6e92 | 0.1832 | -51.22054 | 2024-11-21 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 443b3aae-e8a7-3b92-be8b-ba33cb71fc99 | -1.97818 | -53.33223 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dde2dcaa-67dd-316f-a168-bbf205924501 | -1.63728 | -52.69112 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7089d0b5-5b25-302f-bdee-9780842c71c3 | -1.49881 | -54.70951 | 2024-11-21 04:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0bbccfd-4646-3a7e-a7c7-c14b1865f826 | -1.5789 | -51.27434 | 2024-11-21 04:53:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a929e9d-1cb5-344d-baf7-191294ca4e7f | -1.73252 | -52.38795 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 2087ccad-d1cc-3d7f-969c-1ffe21826ebb | -1.19821 | -51.76414 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2b30103-ff23-3e75-8278-48c9753400e3 | -1.62426 | -52.57973 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8d36ebfe-30e7-39e4-acb3-5bfe23031e47 | -2.15382 | -50.91743 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a70231b-344e-35f7-abbc-238ed46aca39 | -1.22058 | -51.79655 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a5cf207-d592-34b3-af98-f56fe1afb8fe | -1.21039 | -53.6986 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 0f8530ff-5292-38f4-8e90-86996f243e51 | -3.1278 | -45.44956 | 2024-11-21 04:53:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c33aa785-053c-363c-a912-dbfb80e80bc8 | -2.84423 | -49.15281 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f001eea6-5d31-3147-896e-b13c8f79298a | -1.25326 | -53.36274 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e6eacdb0-e6c0-34e8-93cd-09b37fc21ca8 | 0.4076 | -50.82335 | 2024-11-21 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ad791ea4-6eaf-3638-bd3a-6707fe316231 | -1.61933 | -52.58957 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README59.md)
