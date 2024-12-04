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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea697c8c-a480-3dcc-ae40-103bdd4752a8 | -1.74419 | -52.61852 | 2024-12-04 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6ef147e4-102a-34bc-b47f-22769ec093ee | -3.05391 | -51.06575 | 2024-12-04 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f8f96b2-c5b7-3f53-b88a-db2ea0444dd2 | -3.72864 | -51.08881 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 02b6050d-74ba-3c7e-b93e-04ad19fb76d0 | -3.55614 | -50.18084 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 166b9d9a-2424-3bae-bec3-f08df661f525 | -2.6884 | -48.85635 | 2024-12-04 04:10:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 61aca714-c2ed-31d4-a409-caa7378b5b3e | -3.79309 | -46.70305 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9de8a3d8-410e-3d99-9895-8b16c65c1db2 | -3.55445 | -51.51814 | 2024-12-04 04:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9044b95b-bd99-3e01-96c7-d42c66a52665 | -1.9423 | -48.31589 | 2024-12-04 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe8d34a9-c3f5-3c5d-9a35-50eaa8835441 | -2.68484 | -46.12426 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7889e77a-0954-35ba-a949-18f6e6ca9020 | -3.80665 | -46.94149 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ec27572-4c15-3826-9fe2-8979cf3072b8 | -2.81339 | -53.05112 | 2024-12-04 04:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13ff340a-0e39-321a-8480-6e7a3a609360 | -2.94873 | -51.41079 | 2024-12-04 04:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ce01d2f4-728e-3dba-964e-f02ff19f7946 | -1.7598 | -52.63437 | 2024-12-04 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a5321ca6-7be5-3d87-ade8-6c521249aa9a | -1.35758 | -46.40693 | 2024-12-04 04:10:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 19d4b8f7-e0cd-3418-99b7-c0d21ac59719 | -2.68093 | -46.61868 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a72812e0-52b6-3f11-84cc-6e200ac05c5b | -4.05324 | -47.0061 | 2024-12-04 04:10:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9666c22f-e971-305e-aa0a-da86ba1ae57b | -2.66901 | -46.12635 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 101feb32-014b-38f1-9fa6-605aeae57ebc | -4.04321 | -46.87324 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cf4b540b-f07a-3ae3-8d4b-ce26269c37aa | -3.89843 | -52.16749 | 2024-12-04 04:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e91f7c67-de96-32d9-ac51-2f97dccfb423 | -3.93945 | -46.88692 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 33e3d7f1-aec8-3e6f-8e0a-ea876af9eca4 | -5.87493 | -42.65281 | 2024-12-04 04:10:00 | NOAA-20 | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 63b64e5e-b79f-33ad-b635-4f80a24ac03f | -4.07079 | -47.09574 | 2024-12-04 04:10:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 6c5e92da-45d4-3346-80c8-6b8c149e7e87 | -1.96112 | -45.82841 | 2024-12-04 04:10:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9b2cad99-b63e-37f5-878c-236c3386677e | -2.72989 | -46.22887 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f53e1c1-40af-3c36-8c77-d98435d209d3 | -3.19173 | -50.64799 | 2024-12-04 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 12fdcbe9-ba85-3a89-86bd-ab36944f248f | -2.802 | -53.0675 | 2024-12-04 04:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 24e8da22-3b01-38ff-8dfd-e701151dd6d5 | -2.61517 | -45.41541 | 2024-12-04 04:10:00 | NOAA-20 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 23d414a1-d8bd-3a8c-9a55-25e7e1d1b9c8 | -3.47897 | -50.2392 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 201dc9c3-1fbb-3e4c-9925-dd9a360e2873 | -4.68734 | -40.69392 | 2024-12-04 04:10:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7783b1ab-4f06-3613-b5c7-c310094d491b | -3.8216 | -52.12125 | 2024-12-04 04:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07ba30fe-6a0f-3c3d-b880-73c68028c76d | -2.80514 | -53.06337 | 2024-12-04 04:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 24aebcd4-a972-3a08-b045-5b8ae9490253 | -3.48067 | -49.98509 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 184b313a-38a5-3304-b189-880b90090868 | -3.56976 | -50.31231 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c3bd5f68-a35a-3d82-ac50-79d047ae9c00 | -4.07383 | -46.69889 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa36aa98-5081-3dd8-bb35-d12ead5d8058 | -3.97757 | -50.51847 | 2024-12-04 04:10:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3d152527-9b81-396e-9dfd-b5889c524762 | -5.61957 | -44.83811 | 2024-12-04 04:10:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d25ab04c-027d-37a7-9c12-7b3a2a382b31 | -4.05176 | -46.81295 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bbfb0e64-a3dc-3a01-a7e0-225107ea71eb | -3.11553 | -54.67501 | 2024-12-04 04:10:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25b22d20-0c09-3621-86e3-c61c0b01d4c8 | -2.68016 | -46.6236 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 656b3e3f-dd15-3418-82d9-1f47ea4c2aee | -3.54968 | -47.37917 | 2024-12-04 04:10:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d09a4c9-9a15-3151-a0bf-f743850b806f | -3.31296 | -50.43892 | 2024-12-04 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f81cb1b8-a60f-360a-ab50-fba1dcbc6561 | -4.05669 | -46.81589 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0e2a9aa7-c8c5-3ae4-be39-15be28bb29c5 | -3.37641 | -51.10156 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c69f648-791f-35b0-b3d5-b73ffd461a82 | -2.82358 | -54.15371 | 2024-12-04 04:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2dbd369a-2f78-3ccf-855e-291cc7e93600 | -3.06552 | -54.06079 | 2024-12-04 04:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a9090f0-723b-34f5-8109-446eeca59321 | -3.13472 | -39.90913 | 2024-12-04 04:10:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| de978e5a-7e7f-35e4-bdde-98639147f5ea | -3.17344 | -54.33644 | 2024-12-04 04:10:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 00362e2e-7ca0-3cec-9b86-279a59699613 | -2.31066 | -45.42403 | 2024-12-04 04:10:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 767ca219-f597-3f69-950a-01d105867740 | -4.04431 | -46.81883 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a3b88fa-8c47-3d98-a2c3-9a5b4ba10ab0 | -3.82006 | -46.68274 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1347ce69-6d27-392f-9c32-a0e1a618aedb | -3.20234 | -50.64675 | 2024-12-04 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 86a6bfc9-5e1d-3448-9c2d-ecd925867116 | -3.28614 | -53.71307 | 2024-12-04 04:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f83cdfbe-f0d6-36aa-a235-ad9c028e1798 | -3.6408 | -51.12886 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 770b8796-3e37-3b32-abf4-03a8977b683a | -3.82081 | -46.67804 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af1ac36c-ba1c-3b31-a5e6-55933ce35cc0 | -4.27179 | -46.57335 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c217b3c0-9fc1-38aa-bf21-5c15193522db | -3.29233 | -53.71405 | 2024-12-04 04:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64e53b63-d319-357f-a1fe-6e24ffae76ee | -1.96627 | -48.3893 | 2024-12-04 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa358274-3880-319a-97d1-6dd756d2864a | -3.09257 | -53.25183 | 2024-12-04 04:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f218aaa-9949-326a-a23d-e266adda25e8 | -2.81785 | -53.06095 | 2024-12-04 04:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8813f268-ae89-3f48-a8c1-4f272873df2e | -4.04351 | -46.82365 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e3ee163-d045-35ba-b869-6697a9052af9 | -3.80807 | -46.95708 | 2024-12-04 04:10:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e74886b-3c57-3eb3-a758-e6db17777a3f | -4.04544 | -47.0047 | 2024-12-04 04:10:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f73081ec-c65d-3cc5-a76c-4b8540b294a6 | -2.8317 | -46.7578 | 2024-12-04 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 4235198d-3a9f-32e2-9728-61e0686f15d9 | -3.78005 | -50.97064 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1138b9bc-e2c3-36af-b727-811e08b61103 | -3.10896 | -54.67389 | 2024-12-04 04:10:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b246756-2000-333a-8005-6c4cc18523b6 | -2.88605 | -48.09143 | 2024-12-04 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f71d224-a5a0-3ebc-85aa-63e5b0927ab1 | -3.93478 | -46.89122 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| daf8599e-c40a-35c8-b642-04f8f8072d80 | -3.19632 | -50.65179 | 2024-12-04 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6c5a4aa1-f89e-3ed1-86f3-a61ab2b733ed | -3.25387 | -50.60903 | 2024-12-04 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2b8aed0-bfb4-3fc5-bd5b-d0a667468195 | -3.73261 | -50.0602 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28188c67-94fe-36c2-ba86-52bf4bb50414 | -4.05699 | -48.35007 | 2024-12-04 04:10:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b2fe992c-14ab-345c-9175-5805800b32b5 | -3.78569 | -50.96844 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9ec21dba-223a-3677-8566-97eb3948feec | -2.85112 | -54.83228 | 2024-12-04 04:10:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cb2fb7c9-c913-3d34-a20d-3273e2234b17 | -3.23926 | -54.14248 | 2024-12-04 04:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 402adce2-caa3-3f65-8ec2-60734190ddeb | -2.90438 | -51.81938 | 2024-12-04 04:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3ace8ea5-bd26-314b-9ecf-d17ca9f3ffb7 | -3.10639 | -50.32131 | 2024-12-04 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5ae1dca-3287-34d5-bd25-08e46db2548f | -2.65843 | -46.11992 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9079b9d2-3fa9-38a3-b14c-93d6e7a7502e | -3.33611 | -51.21259 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aede5310-1426-3096-be35-348a3146b9cd | -1.73899 | -52.61324 | 2024-12-04 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a061a4b7-d370-339e-b537-0197696c84ce | -2.6773 | -46.12302 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54b68fa9-e487-38b5-bd12-8b0716ad8225 | -2.79674 | -53.06209 | 2024-12-04 04:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cab62ca6-2104-3c04-85ce-a0ad02c2ae5f | -2.88477 | -51.8009 | 2024-12-04 04:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7e521858-cf09-3a3e-9acd-5fc00494bc8f | -3.60596 | -50.8018 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68455161-7593-3445-a3df-a60fcb11cf63 | -4.02928 | -46.92931 | 2024-12-04 04:10:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c643d162-e657-31a8-b29d-39aac018becc | -2.33804 | -46.35448 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80f6e0aa-14a1-305f-ab6f-55c553170207 | -3.93429 | -46.92383 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5b97db50-fe03-3131-a9cb-acaec7522f74 | -3.33708 | -51.20914 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c09667d9-0fd4-3af3-8279-4b0d6b81d567 | -3.33665 | -51.20937 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b286b5f-59ae-3882-9d54-5a4add235b0c | -2.81414 | -53.04673 | 2024-12-04 04:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 939c550d-453e-319d-88c0-00a736500133 | -1.61834 | -53.53919 | 2024-12-04 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4077da0e-886e-353e-a318-a3b936d86235 | -2.20317 | -47.24881 | 2024-12-04 04:10:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41cc5675-af24-3c04-a5cb-dbfc3399f124 | -2.06903 | -45.48491 | 2024-12-04 04:10:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b2d4617b-48b9-3237-bc22-f7c57e21f9d3 | -2.75662 | -45.27862 | 2024-12-04 04:10:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d11aacc-3516-31fb-8d0a-1e08f19bfe04 | -3.57067 | -50.30674 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| be995548-8a10-37ae-a440-43a67e5adbf3 | -3.90169 | -46.65379 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7a59999-e17e-3acf-852c-52bd1933a4ed | -2.82067 | -53.0661 | 2024-12-04 04:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 21988191-042c-3f57-9047-f59f84273b0b | -2.88731 | -51.81991 | 2024-12-04 04:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37d5d1e5-ec08-3278-96ca-475c35ea60ed | -2.7984 | -53.06682 | 2024-12-04 04:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cbc66f38-0d36-3ed8-aa28-e6947d3f15b3 | -3.84839 | -52.15971 | 2024-12-04 04:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 03f87b0b-3555-3c11-b2b8-5fc0dd47dc06 | -3.26357 | -53.65927 | 2024-12-04 04:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README28.md)
