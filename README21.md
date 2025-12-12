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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e99d9b59-af55-3a2f-a075-c8dffb510b3b | -2.42197 | -51.92427 | 2025-12-12 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| b3746c08-d9a4-3991-8ac6-ff6ba9e88dde | -1.66399 | -54.57874 | 2025-12-12 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 85a61196-1fb6-3837-9933-53ff8acbc026 | -1.69486 | -55.39053 | 2025-12-12 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9fa0ca3-f7cc-3381-9f34-0f97186cae8c | -1.61004 | -55.86763 | 2025-12-12 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf69855e-cecc-3779-bd04-14d55d372b6d | -6.51638 | -55.03955 | 2025-12-12 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8760b616-5761-31a9-a154-ac3f5bcec3dc | -3.02943 | -49.05236 | 2025-12-12 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 704499fe-fa72-3805-a0a4-dfeb9f47138d | -2.25612 | -48.23868 | 2025-12-12 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1d47292-d226-3e67-8182-e81b28eca907 | -2.36687 | -47.68486 | 2025-12-12 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6da9b12-d7fd-32cb-b651-a044e9d2d3a2 | -2.65271 | -51.64243 | 2025-12-12 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12eba44e-e649-3cc4-bfa6-e3bedd4783e8 | -6.5632 | -56.13467 | 2025-12-12 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fcc03643-a545-3b46-bed2-fe444a5ae876 | -3.34433 | -53.33837 | 2025-12-12 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9df065ed-051c-369c-bbec-4d04aba8979c | -2.42905 | -51.93052 | 2025-12-12 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 1872146c-ba71-3538-8706-eaeb9f9786f0 | -2.93392 | -52.25328 | 2025-12-12 05:10:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03bcf0e4-7ce0-3c89-a7b2-655dacb19388 | 1.12512 | -60.52631 | 2025-12-12 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80d278ca-d4de-3631-a3c2-0b301c3b0c09 | -3.02082 | -52.82881 | 2025-12-12 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 134c8ee9-97ee-35c2-9896-606b114e6467 | -3.34819 | -53.06852 | 2025-12-12 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7723a27-d7c9-3a44-9e93-ce2e2bb84503 | -1.31572 | -52.53662 | 2025-12-12 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7ad00738-2095-3e33-8f93-b66d41eae5d3 | -1.76471 | -54.04011 | 2025-12-12 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abf1a63a-4d2a-3cb9-a258-5440e162e1d5 | -2.97471 | -52.72191 | 2025-12-12 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| faa1884c-a19c-3e94-84ea-b3ab5d90d2ff | -1.70122 | -53.93247 | 2025-12-12 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af76dcc8-b2f0-39b6-ae8e-596b85ac8fa9 | -6.55087 | -54.95348 | 2025-12-12 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f7b55527-d86a-3406-ae5a-9faa097a0595 | -2.36117 | -47.68713 | 2025-12-12 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13211005-7176-30d9-a583-ef12bf44b605 | -2.90186 | -51.93828 | 2025-12-12 05:10:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d856b78-b698-39d0-a581-652f5759f381 | -1.0288 | -53.73961 | 2025-12-12 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de3c8fd2-15d0-3986-9030-61d4c837fbe0 | -2.66849 | -46.89352 | 2025-12-12 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89c7eb31-a914-3376-834a-5d2217ccbf7a | -3.79999 | -51.37495 | 2025-12-12 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7f197c6-0ca3-3e3e-9e9b-66c8714d2907 | -1.66739 | -54.57925 | 2025-12-12 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dbdda8ed-7515-3056-8195-5c04f077afbe | -2.50459 | -51.79988 | 2025-12-12 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| f4787862-7e84-3685-9a7c-feaffaf14afa | 0.70497 | -56.87836 | 2025-12-12 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1b78bc57-0dff-3b60-a502-9545ba1ee61e | -2.50187 | -51.7979 | 2025-12-12 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 3567a19f-7091-3277-aa89-b288fb192d58 | -2.50108 | -51.80297 | 2025-12-12 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| dc23e44b-bfa0-3f88-8a6f-009cc32c2c0c | -1.1119 | -53.68848 | 2025-12-12 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 228a8d32-2681-3ec2-94e6-b26aef67f003 | -1.34066 | -54.60516 | 2025-12-12 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 065e76ff-4c6b-3023-bb2c-64cd5a28fecd | -2.65968 | -51.6506 | 2025-12-12 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71b1d44f-5dc9-3bf8-a731-f8f32cab3ea7 | 0.45785 | -60.42682 | 2025-12-12 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d6302baa-c233-3464-af3b-11b1f0cac88b | -1.34745 | -54.60616 | 2025-12-12 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd11009e-4705-32f0-a3f0-10ffdebe370d | 1.1291 | -60.52571 | 2025-12-12 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c99bd112-3fa9-33d1-9161-69e9080279a5 | -3.30663 | -52.70526 | 2025-12-12 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0262f1be-3087-303f-b573-246162005fab | -1.54439 | -51.49407 | 2025-12-12 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9be70a20-48b3-3079-ade6-e3f553f6d2a6 | -2.66344 | -47.78617 | 2025-12-12 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7910c5c3-9e63-3c25-b36f-0a1565c28b9f | -2.47152 | -48.06552 | 2025-12-12 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 88031a95-9022-3ae3-8bb3-28f7267cae0d | -6.51348 | -55.03515 | 2025-12-12 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71546af5-30f6-3f95-acba-4842b96c766f | -2.26114 | -48.23947 | 2025-12-12 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 008ea0ac-0887-39e5-b2df-4a1fcc1eaee3 | -2.41805 | -51.92364 | 2025-12-12 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e4446508-37ac-321f-9afa-fc85bdb54ca3 | -3.01264 | -52.83231 | 2025-12-12 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53523589-e383-34bf-ada7-cb8b2fedb163 | -3.79945 | -51.37856 | 2025-12-12 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15f207cf-650a-321e-a947-e522a92a7fa8 | -3.1309 | -54.18193 | 2025-12-12 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cca32d50-4312-368c-9319-bd089ed84cbf | -3.50011 | -52.52481 | 2025-12-12 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7c7494c-cd18-35b6-b560-cddaf84c909a | -1.03229 | -53.74015 | 2025-12-12 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1981fa70-b888-339e-97c1-bba8950e405b | -2.36217 | -54.37278 | 2025-12-12 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 465c1dbe-44ab-3dab-9b2a-da9b5ededb6f | -3.06437 | -52.39299 | 2025-12-12 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 085cd636-3f95-3afa-b9de-851de09268fb | -3.02864 | -49.05751 | 2025-12-12 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ef699655-c40e-38dd-a814-29017c02df52 | 0.45799 | -60.42456 | 2025-12-12 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 35ae7a99-82c5-3ac6-9478-afa484811b2a | -1.1148 | -53.69287 | 2025-12-12 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62cd0f41-7ea8-309f-9498-a7dd4a3d8fa5 | -1.29522 | -53.16636 | 2025-12-12 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc5cbfe2-1ca1-3d2e-808a-d7581409344b | -1.31031 | -53.48663 | 2025-12-12 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d2b6c10-703a-3e65-9af0-1f6a91b97704 | -2.74541 | -52.97392 | 2025-12-12 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 7c90f157-761d-374a-a1d4-ddeb5a4713bb | -2.23118 | -45.40465 | 2025-12-12 05:10:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 493469ed-aab2-30d0-bb00-255a037c1738 | -2.483 | -47.77435 | 2025-12-12 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| db734406-d335-39c9-b58f-22496a349eb0 | -3.85219 | -55.68822 | 2025-12-12 05:10:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd154fad-0fe0-3665-86b2-c5f65216fc5d | -1.46778 | -55.09962 | 2025-12-12 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e8a445f9-664f-358a-ab69-682d6721600c | -3.93566 | -54.7221 | 2025-12-12 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e4ab44ff-a4ca-3b41-9d12-175c007b1a94 | -3.23673 | -47.47328 | 2025-12-12 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8036bb83-7189-30c2-9f2a-60e48c78d8c5 | -3.17557 | -52.87772 | 2025-12-12 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f76bf57b-eb53-34c0-8c55-1d51b591eb00 | -1.29162 | -53.1658 | 2025-12-12 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96b11ecb-6165-3196-a64e-f8abd6b43fe8 | -6.51927 | -55.04396 | 2025-12-12 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c67e791-15e7-3d0d-bf4d-01590e9c774b | -3.48715 | -52.36348 | 2025-12-12 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 045ec615-a2c4-3d70-b86d-76aa6d3efb84 | -2.95931 | -51.68198 | 2025-12-12 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85623a52-1a76-33dd-87aa-2cc22b332368 | -3.63184 | -51.94042 | 2025-12-12 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a65303ae-9146-3c9e-a5d8-094421b24e22 | -3.15474 | -54.60284 | 2025-12-12 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e86b101-a775-388f-b400-1e603c1d9992 | -3.03636 | -51.20249 | 2025-12-12 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d255c47-e2de-3c23-85f1-77f2ef8e3d3b | -1.35443 | -55.37 | 2025-12-12 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b26b4ec-14ec-3804-9260-ef3915d5c9af | -3.81375 | -54.73894 | 2025-12-12 05:10:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b8b24940-b97e-32a3-83a6-1c2afb6625f2 | -1.83084 | -53.82079 | 2025-12-12 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 339011cb-1869-3e38-b3db-09d7781fef9a | -1.59196 | -55.43923 | 2025-12-12 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b47bc776-b10f-354e-b526-9752f4b68af5 | -1.3401 | -54.60881 | 2025-12-12 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 15409678-f2c4-38b4-9507-845174203b97 | -2.43297 | -51.93111 | 2025-12-12 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 1fce20c3-3306-3f9b-bd9e-1df9cbfc19bd | -1.40401 | -52.54438 | 2025-12-12 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 347774ff-27c7-39b7-8c9f-0d9d9c0bd10b | -3.68182 | -52.53431 | 2025-12-12 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37f50829-0d3f-3e11-a3ce-0d1bb2ded3bb | -3.38605 | -47.1913 | 2025-12-12 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab5b2dbb-fa22-31aa-8775-79fdca5d212e | -2.69703 | -45.69884 | 2025-12-12 05:10:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fafeeb9e-73a8-384b-98d2-0851281ae82a | -2.65619 | -51.64651 | 2025-12-12 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dfbf392c-b206-32e2-91a0-711cf064dd89 | -2.42437 | -51.93488 | 2025-12-12 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 1d5a71e4-07d7-363b-aa64-5f57c853cd4e | -2.88824 | -53.01421 | 2025-12-12 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b1365045-7abb-31e0-a2c4-7d2299a91480 | -3.76624 | -54.31422 | 2025-12-12 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 89bf5bc7-bda6-342d-b49f-e8a146ea4da9 | -1.70193 | -52.14762 | 2025-12-12 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4984d05-a33b-34db-adce-95e7526e6093 | -3.12741 | -54.18141 | 2025-12-12 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1390cecf-ef0c-3182-8c1a-eaf81d2aba3d | -3.46968 | -52.80576 | 2025-12-12 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6a9f38a5-5500-3780-87e9-66a59da8c6d9 | -3.12799 | -54.17755 | 2025-12-12 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9855d089-81e4-3ee0-b851-5ccc81b6c0a3 | -6.02886 | -43.69995 | 2025-12-12 05:10:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e2fe6566-ed70-3da4-ae6c-7fb92f9bb6a3 | -2.88537 | -52.69678 | 2025-12-12 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e182b3be-4b80-30f2-be00-9da6db1d4857 | -2.66124 | -51.64018 | 2025-12-12 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 98b4ca67-9162-3f0e-8c77-261a8a5ee04f | -2.36159 | -54.37654 | 2025-12-12 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a09bd20f-cec2-38a5-bbb0-f140612ebb0f | -2.8628 | -53.03249 | 2025-12-12 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 47256253-abc5-3b71-bcf5-ba950691377c | -2.08119 | -52.05156 | 2025-12-12 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 520f39ee-b8bc-34ff-a642-8299e59571d9 | -3.54603 | -54.72586 | 2025-12-12 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a9e11535-41de-3c92-9dec-8dbf9e771ff3 | -3.1344 | -54.18246 | 2025-12-12 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2007fb6e-276c-310a-80fd-d58a7e333d61 | -1.70264 | -52.14291 | 2025-12-12 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a81db6f-a181-3daa-8323-cb2767f82297 | -2.43373 | -51.92607 | 2025-12-12 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| f30f90b2-4a08-3fad-aa63-640ca7bf4f0c | -2.15159 | -53.76299 | 2025-12-12 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README22.md)
