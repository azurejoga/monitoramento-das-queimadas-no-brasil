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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 98307fcc-e035-30c5-8be6-78fa4912da0f | -2.6264 | -54.205399 | 2024-12-02 00:57:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be181de7-1a05-3917-b39e-511bd6445830 | -0.3022 | -51.773499 | 2024-12-02 00:57:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 2ee2cc74-6eee-3433-8309-bc8d1b2cb2c4 | -2.6289 | -53.363098 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2cddd949-e84c-3436-b783-47d42bf417e9 | -2.5549 | -53.399601 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7b66059-bae6-34eb-b656-ad74d3109822 | -3.1393 | -53.8368 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6de9bf0f-f8ce-36ec-80ed-7cde2ea35bcb | -1.6176 | -53.8913 | 2024-12-02 00:57:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83cf2b3a-58c1-35d0-8ffe-4cc98763979f | 3.3744 | -60.518002 | 2024-12-02 00:57:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| fc5896cd-75a4-3e3d-9097-4abf19e49e74 | -2.8711 | -53.924999 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b653509a-5821-3fb7-98a7-6eb860bd47ac | -1.5742 | -55.328999 | 2024-12-02 00:57:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dfa71a36-b32a-307c-85ac-844951e846ad | -2.4167 | -54.0093 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 100533f4-b314-3d3f-843d-e07d4eec1582 | -2.9788 | -53.9006 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8428b1f1-8537-3a8c-bbe3-f76cadf9b327 | -2.8634 | -53.9814 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3026ff88-d256-36df-af5f-12bd07904105 | -1.3863 | -53.5541 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 588c1d05-2766-347c-9442-5aed46325b01 | -2.5872 | -53.989201 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 641cc56b-fc17-34d2-84ac-fead92e5f920 | -3.1102 | -53.979698 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d078642d-e8a0-3356-ae01-ec6c42de3c44 | -1.3981 | -53.6507 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e03a6065-e4aa-338a-9907-48122fa6c71e | -2.0211 | -54.306099 | 2024-12-02 00:57:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 910216f0-7b15-32de-a3cb-462c2a33ec78 | -3.2434 | -53.931599 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 740cd0f5-f044-30d9-a8d8-4762d7f63328 | -2.0094 | -54.299801 | 2024-12-02 00:57:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b6f0d82-97c1-3990-b15b-9917a1fa52e7 | -3.0985 | -54.018398 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9d5d029-a280-379a-b788-98da0087e37d | -3.2436 | -53.618401 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d27fea98-b1aa-3ac7-a8ed-14964dccd943 | -2.6323 | -54.186298 | 2024-12-02 00:57:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6dbbde1e-914d-3c2b-97f4-c8ec253a98ee | -3.2512 | -53.920799 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| efb7bf62-3178-368e-b9e3-dc3b0327dff5 | 3.394 | -60.5224 | 2024-12-02 00:57:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 89fa5119-2cda-3573-8e26-2e95b7ffe1fc | 3.3826 | -60.482201 | 2024-12-02 00:57:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e9b79f35-5fc4-3cc8-a7b7-4a0e2f110955 | -3.0946 | -54.0462 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32b69b6c-0464-3c73-8e9b-185d67269383 | -2.6283 | -54.213902 | 2024-12-02 00:57:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19a35040-5bd9-3eab-8b99-ccf1e478e63f | 0.9084 | -59.4361 | 2024-12-02 00:57:00 | METOP-B | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 837b8ac4-3d82-3afa-bb2f-d5dd6f9e8790 | -2.8399 | -54.103699 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c87d32b2-be33-3a25-957a-f112af074f24 | -1.2976 | -52.850101 | 2024-12-02 00:57:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50459bcb-3890-3e52-98be-6704496b198a | -2.8223 | -54.0718 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 518ecb09-1e36-30b9-a427-8ae5ffe78dc4 | -3.03 | -54.033901 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df1bb47d-bcf4-38ec-b37f-ded4952bc53d | 3.1838 | -60.1768 | 2024-12-02 00:57:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ded355a9-164c-36db-a101-dc41dee2e809 | -2.9846 | -53.881001 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ddc24388-1d25-3630-99ad-b646f9ba85a2 | -2.5669 | -53.4067 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6cfe70e-7ce7-309e-8854-a4a2325b114a | 3.3874 | -60.460701 | 2024-12-02 00:57:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c7267a28-0037-3290-9abc-25a5de272f0d | -1.6156 | -53.882198 | 2024-12-02 00:57:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e57368cf-4b47-34a6-b244-071d50d4f5e4 | -2.8243 | -54.080299 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3a52592-aa69-3a0a-9ea5-56aa78e0bbe4 | -3.1024 | -54.0355 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fc2bbbf-5ca6-32f6-93a8-50c07f84fbd2 | -3.327 | -53.533401 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aaa2c894-43fa-3a9a-ab24-9dbca0ffd381 | -2.5528 | -53.390202 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9167b794-442c-3264-99a2-50577c30f1a4 | -2.5473 | -53.411098 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 890bccf7-dca6-378f-adfb-e4fb3681b017 | -2.8791 | -54.005001 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69a78416-b620-39bd-944c-a53570dd2d56 | -3.0617 | -53.678398 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38cbe7f4-d4ea-36d5-8e32-7b29b65edb34 | -2.6191 | -53.365299 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5b47467-1f7f-3536-9225-d6e671841189 | -2.8141 | -53.0494 | 2024-12-02 00:57:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e05af11-659c-33c3-a9ad-08c79d24e42d | -2.4407 | -53.6199 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02ab5c3b-f98d-3f7a-9c40-999b8b612d8e | -2.4403 | -54.022301 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37bc0139-8ba3-347b-8e5e-c8d08c424e43 | -2.967 | -53.894199 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94f06fb6-adb4-3af5-ad5a-a3b818b59e21 | -2.3614 | -54.8494 | 2024-12-02 00:57:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e6b45b8-d954-3f07-9a33-c3af9acfa3fd | -1.0873 | -53.641201 | 2024-12-02 00:57:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8dda5b7-f897-3c16-b22a-3230e4eb803e | 0.8645 | -59.6763 | 2024-12-02 00:57:00 | METOP-B | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 84f4d2f0-d848-333d-81f0-7993fdefa982 | -2.7851 | -51.899399 | 2024-12-02 00:57:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2271592a-041b-3bdf-9151-10e0dc219203 | -2.9865 | -53.350899 | 2024-12-02 00:57:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84adb57a-93e6-300c-b31a-3c4f9dd6e908 | -3.0976 | -53.7449 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1522b6ac-6054-3cb9-a025-16ecba0a8e59 | -3.2093 | -53.111698 | 2024-12-02 00:57:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64fcead5-28ba-38b7-9fcd-c38ded945e70 | -3.2414 | -53.923 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b73937a4-82f6-390c-952e-f923f98beda5 | -3.0888 | -53.258701 | 2024-12-02 00:57:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5870a10-ecdd-3be9-86c7-ca700b568d27 | -3.3291 | -53.5424 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09277f9f-7dba-33c4-88b2-2fde7d72fa90 | -2.4505 | -53.617699 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f71e45cf-8a8b-37d1-b695-a986452db44d | -3.1122 | -53.9883 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 418e000a-b2e0-33c7-9ff6-bfc253f5c477 | 0.8629 | -59.6833 | 2024-12-02 00:57:00 | METOP-B | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ded3aa42-4313-3606-ba29-3f29fb089fee | -2.8478 | -54.0481 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77c8f1d8-3ab8-3201-a9fd-8941df37a2de | -3.2652 | -53.622898 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2628a6e6-6221-3443-87e9-78d5d3cafe60 | -2.7223 | -54.1749 | 2024-12-02 00:57:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 416b31d0-e23b-32a4-8bca-81dea7e54f51 | -2.8889 | -54.002701 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cbca7464-35a8-3890-a04c-6757e87560af | -3.0637 | -53.687302 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93bc82af-26a2-3ec0-80d2-6e4004dcaf1f | -2.7818 | -55.338001 | 2024-12-02 00:57:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71839f1b-a865-3a7f-ae62-9c8b3ef2fc6f | -2.5852 | -53.980499 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 693a1600-00b8-3223-b8bd-07c049735e00 | 3.3793 | -60.496498 | 2024-12-02 00:57:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| a1e96a04-3704-3249-8776-7c0d208e26d4 | -3.2595 | -53.642899 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46294ec0-66d6-38cd-bbd8-cf89b836ed0e | 3.3761 | -60.510799 | 2024-12-02 00:57:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 8eb3d78a-6492-3a7e-9fd9-d01f009e0cda | -2.9144 | -54.113701 | 2024-12-02 00:57:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e8f3d50-1ad5-335b-bc19-7619b469b11e | -3.2532 | -53.929401 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d727fd00-a445-3d10-896b-f2375b66a0f7 | -2.8674 | -53.9986 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2dfc4893-01cf-3d0e-aa0d-819bb340deba | -2.7946 | -53.053902 | 2024-12-02 00:57:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7f87f5c-7248-3d4e-b770-fe1d3cdc6cb9 | -2.7597 | -54.1129 | 2024-12-02 00:57:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9524cff-7663-3950-906c-0c19e9359de9 | -2.8262 | -54.088902 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2744382-53b4-3618-86d4-a5a91f05d758 | -2.8027 | -54.0313 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b21d0b0a-4798-3e58-9867-585e958a3bf1 | -2.7362 | -54.100201 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eac39e33-2f42-3165-a847-b335021346d5 | -3.2492 | -53.912201 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f94ce5c-d0bb-348f-a8e8-6dfbdd89603e | -2.4461 | -54.002701 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef958981-d5da-315c-9401-cf419cc6dda7 | -3.0925 | -54.126801 | 2024-12-02 00:57:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e18be4af-fd44-3560-94aa-3ec9f6c570c2 | -2.9882 | -52.510799 | 2024-12-02 00:57:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23a7acab-c97a-362c-8a91-da001100a197 | -2.6344 | -53.342098 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d295d9d-8eb6-3a92-b2b0-3b89570d174d | -3.2456 | -53.6273 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a84542f-ebbe-36ed-b367-b2148cdad3f7 | -2.9728 | -53.8745 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60eb1777-bf3c-3857-87d6-5f2253805c0d | -2.617 | -53.3559 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbce8076-3291-38e7-a8c0-93223f8d3211 | -1.0729 | -53.4426 | 2024-12-02 00:57:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd7e247e-6f3e-3d3b-a7c4-431688e78e77 | -3.2115 | -53.1213 | 2024-12-02 00:57:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fbf2cbf-a25c-3347-b65d-8e32c2756144 | -2.5571 | -53.408901 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5469db12-3a18-3489-92dd-16af52c3ee2d | -1.7204 | -52.632 | 2024-12-02 00:57:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 313d8785-27a8-3fca-9aae-0c6bdc30a28e | -1.0264 | -53.554699 | 2024-12-02 00:57:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d02c948-eb78-3ee2-9600-2d092d914b17 | -2.8232 | -51.8419 | 2024-12-02 00:57:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30b35a71-1d95-3fdb-8dd7-b506b19a1095 | -2.7901 | -53.034302 | 2024-12-02 00:57:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7986cd6e-7c95-3b72-85da-097b26ac0f07 | -2.9768 | -53.891899 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5072ccf-745a-3664-9093-29de9841fa3c | -2.8909 | -54.011299 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6af9cbe5-7621-33ad-831e-22be8994d4b0 | -1.3283 | -54.971901 | 2024-12-02 00:57:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 225a26c3-019a-3b80-a64b-03bba3cee8df | -0.312 | -51.771301 | 2024-12-02 00:57:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 85734f66-d5d3-3470-857c-3a7454e9a711 | -2.7999 | -53.032101 | 2024-12-02 00:57:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README10.md)
