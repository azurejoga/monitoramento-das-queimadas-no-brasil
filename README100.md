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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5470423e-8a62-3cd3-8c22-bd961962df30 | -3.52796 | -62.77231 | 2024-12-01 06:01:00 | NOAA-21 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7b77050-4ae6-3b87-ace9-25a1725a01aa | -5.43383 | -60.18552 | 2024-12-01 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 478b0e2a-b35e-36e0-b794-17fb19994d03 | -5.43584 | -60.18561 | 2024-12-01 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e6cd328-3a51-33fa-80b5-3bb9a83583b0 | -2.85398 | -65.20976 | 2024-12-01 06:01:00 | NOAA-21 | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a77a1d8-b722-3035-8172-0c2b980d9fa4 | -3.79434 | -58.97632 | 2024-12-01 06:01:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ab90fd46-5cd1-3403-b889-80a4f7a69836 | -3.70193 | -64.59272 | 2024-12-01 06:01:00 | NOAA-21 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cdf869e4-2280-36ab-9f6b-3a7ec7f49730 | -3.52092 | -62.7569 | 2024-12-01 06:01:00 | NOAA-21 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b6758cf-1fda-3121-ba0d-c1d509a35538 | -3.5371 | -62.77369 | 2024-12-01 06:01:00 | NOAA-21 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77eb441a-2801-3b49-86d0-7268f8c66bf9 | -12.22034 | -64.35796 | 2024-12-01 06:03:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f20f4b02-3ecf-37b3-94f5-b77ca60a3b3b | -12.27697 | -64.32502 | 2024-12-01 06:03:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76284b99-5872-3a4a-a58e-4eabc2fab39a | -12.22501 | -64.35856 | 2024-12-01 06:03:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a95b3b93-2c1d-3f21-bbc6-181d54c333f7 | -3.1459 | -45.3854 | 2024-12-01 06:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 114.6 |
| d9c34784-4846-3768-a561-e41172a9dca0 | -3.146 | -45.3629 | 2024-12-01 06:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 224.4 |
| 391357a7-77c8-3406-b117-261eac06fa28 | -3.1274 | -45.3637 | 2024-12-01 06:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 39d3e268-d81b-3f29-a82e-7c50811153c4 | -3.2591 | -53.6186 | 2024-12-01 06:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 4d320352-dd0d-3e3a-ba89-3a466d43858f | 1.1439 | -55.9871 | 2024-12-01 06:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| dd7513e7-6606-3e95-9d56-bf85f0850868 | -4.5562 | -43.3028 | 2024-12-01 06:10:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 114.3 |
| c75ebe35-5a5b-32f5-9b8e-c24bdd5e62a3 | -3.1645 | -45.3622 | 2024-12-01 06:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 418dc607-6930-3253-9248-bdfbe06d5b5f | -2.8197 | -53.0425 | 2024-12-01 06:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| b701a884-cd97-3dc3-b537-9d6758af6a98 | -3.259 | -53.6388 | 2024-12-01 06:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 04c5ba31-92cc-3c82-85ab-bfb4deb0cafc | -3.1273 | -54.5264 | 2024-12-01 06:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 9ef6b5e5-2188-3395-86ee-8227aa3eb6d4 | -4.5562 | -43.3028 | 2024-12-01 06:20:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 117.3 |
| e9edb06b-d7e0-301a-9608-6283807eabb3 | -3.1274 | -45.3637 | 2024-12-01 06:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 109.4 |
| af2f4379-55aa-3efe-a921-14f1eae28ab1 | -3.1273 | -54.5264 | 2024-12-01 06:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 03df2b63-3196-3cf3-bbf1-e09bf4814bff | -3.1273 | -45.3861 | 2024-12-01 06:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 74.1 |
| b86bf437-b19c-3291-87e2-0cb5a52ac375 | -3.259 | -53.6388 | 2024-12-01 06:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 2b1741ee-70a1-3c81-baca-5b638dc92b5b | -3.146 | -45.3629 | 2024-12-01 06:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 317.1 |
| d9b986d6-43bd-3be3-acd9-d827d7476bd8 | -3.1645 | -45.3622 | 2024-12-01 06:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 126.3 |
| 2d61d836-501c-3198-b78c-f2cc1f0d09f0 | -3.2591 | -53.6186 | 2024-12-01 06:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 68b39d7d-28e2-3f19-a93c-5cc1504e20f8 | -3.1644 | -45.3847 | 2024-12-01 06:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 2f03b5f1-aab6-3e92-b66b-564e4d9e936a | -6.9344 | -43.5401 | 2024-12-01 06:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 53.6 |
| cd6cf27c-93e2-3afd-bb78-b87153989920 | -3.1459 | -45.3854 | 2024-12-01 06:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 163.9 |
| 5ae654df-8564-3f78-af0f-57ef8d807c90 | -2.85091 | -65.20516 | 2024-12-01 06:24:00 | NPP-375D | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b72b0a86-a993-3b86-8ddb-3db050f89c3c | -2.85122 | -65.20502 | 2024-12-01 06:24:00 | NPP-375D | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ca4b31c8-5034-33bd-b106-7a24d2a0f5d4 | -3.51657 | -62.75813 | 2024-12-01 06:24:00 | NPP-375D | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fe796cc9-fb6c-3946-a88a-165544825e6a | -2.85032 | -65.20927 | 2024-12-01 06:24:00 | NPP-375D | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c8e24a12-0958-399a-8f18-6587402a42f2 | -2.8506 | -65.20911 | 2024-12-01 06:24:00 | NPP-375D | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b098e36e-7235-3102-a3c5-037902932f8b | -4.5562 | -43.3028 | 2024-12-01 06:30:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 00b8914d-ec02-3fe3-978a-ba965ee9739e | -3.2591 | -53.6186 | 2024-12-01 06:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 3a25517c-8a26-39fb-9828-23f7faa1f622 | -3.146 | -45.3629 | 2024-12-01 06:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 562.8 |
| b791eb62-f896-33f0-a356-9f45d4adbec8 | -3.1645 | -45.3622 | 2024-12-01 06:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 5857d2f9-ea30-32f8-a3dc-dd2670ba5072 | -3.1273 | -54.5264 | 2024-12-01 06:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| f5fe11df-9cdd-3383-9622-658831951956 | -3.4974 | -53.8339 | 2024-12-01 06:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 950f8764-48c5-36b3-8d62-a241b6a885e2 | -3.1273 | -45.3861 | 2024-12-01 06:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 496dc99f-5427-3c52-bcd1-9ed3f872e3a3 | -3.1461 | -45.3404 | 2024-12-01 06:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 739a2628-8ffd-33df-972f-9f9f171ae1e9 | -3.1459 | -45.3854 | 2024-12-01 06:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 323.1 |
| 513e0d3d-3c9b-3412-b7e3-16f705b12a5f | -3.259 | -53.6388 | 2024-12-01 06:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 899c6fd7-622e-38eb-9c55-2992ffee26ee | -3.1274 | -45.3637 | 2024-12-01 06:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 126.1 |
| b25230d0-5181-3e0d-a673-7794dce3a6cb | -4.5375 | -43.304 | 2024-12-01 06:30:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 81e9c548-2de6-34b4-a8bb-72f327f74269 | -3.2591 | -53.6186 | 2024-12-01 06:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| ced84a4b-c590-3612-a9cc-b61b0ee46d73 | -4.5562 | -43.3028 | 2024-12-01 06:40:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 138.0 |
| b9727d4d-3fb7-3d48-80dd-459d2945879a | -3.259 | -53.6388 | 2024-12-01 06:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 0f637925-7eb4-3052-b1fd-9fc08a8d3934 | -2.8197 | -53.0425 | 2024-12-01 06:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 704696c0-e110-3b03-aa3b-a0dcc9d39f70 | -3.259 | -53.6388 | 2024-12-01 06:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| cd3b3c0a-516f-30e5-baf2-ec7642890182 | -3.1273 | -54.5264 | 2024-12-01 06:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 3fd7fe1b-189f-30c5-907b-803ac1675f83 | -4.5562 | -43.3028 | 2024-12-01 06:50:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 37548378-8e37-3dd3-b17d-27ce775c3171 | -3.1273 | -54.5264 | 2024-12-01 07:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 7e882ca0-2fd0-346c-af10-70dd6a752a89 | -4.5562 | -43.3028 | 2024-12-01 07:00:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 79d4a5fb-adaa-349a-bdf0-e78f1c79bd21 | -3.259 | -53.6388 | 2024-12-01 07:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 4a8265ae-3d01-3738-8c1e-bf6990960ee3 | -3.16 | -45.35 | 2024-12-01 07:00:00 | MSG-03 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bafb49e2-334f-3dbd-a8e5-46d288302f61 | -3.13 | -45.35 | 2024-12-01 07:00:00 | MSG-03 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7a4fe4db-857b-3238-859a-47f80f2e2521 | -3.13 | -45.39 | 2024-12-01 07:00:00 | MSG-03 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b995fabf-615a-3156-8979-0cf710284d83 | -3.16 | -45.3 | 2024-12-01 07:00:00 | MSG-03 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 82cb026f-68c4-3219-ae95-ea4e2d9f1923 | -3.13 | -45.3 | 2024-12-01 07:00:00 | MSG-03 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c48afe5d-882c-36eb-9ee8-9e0393c639ba | -3.16 | -45.39 | 2024-12-01 07:00:00 | MSG-03 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8191caa8-713a-379d-919f-e8a92e4e2243 | -2.84555 | -65.20823 | 2024-12-01 07:03:00 | AQUA_M-M | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| c486dde4-f986-31be-9af4-96d5fef43686 | -3.1273 | -54.5264 | 2024-12-01 07:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| af87545b-0a3a-3b60-9bb6-5b2d0d456940 | -3.259 | -53.6388 | 2024-12-01 07:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| b82c0997-a321-3300-9db4-e1c51228a9dc | -4.5562 | -43.3028 | 2024-12-01 07:10:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 499e3a7f-fbe7-32c1-8bfa-1e2c451f42df | -3.2591 | -53.6186 | 2024-12-01 07:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 727f24c6-ada5-3138-b51e-60dc90565b23 | -3.259 | -53.6388 | 2024-12-01 07:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 0477f5ca-a5f5-3237-8fc3-bff068bfb41a | -4.5562 | -43.3028 | 2024-12-01 07:20:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 2d3d7798-7ff3-3478-bfec-e55e52ceaf98 | -3.1273 | -54.5264 | 2024-12-01 07:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 96948d17-db64-3bcc-8ef0-2d33983ca5cb | -4.5375 | -43.304 | 2024-12-01 07:30:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| d908cc44-db66-3e3a-9413-d7bb5cdadd5e | -3.259 | -53.6388 | 2024-12-01 07:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| eadded03-bb79-3cd6-90f9-e854915be2fd | -3.2591 | -53.6186 | 2024-12-01 07:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 061a12da-331b-3341-ab73-3b0511af7311 | -3.1273 | -54.5264 | 2024-12-01 07:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 344e7a10-1788-3557-a542-7c1ed20c6f8c | -4.5562 | -43.3028 | 2024-12-01 07:30:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 106.0 |
| ea0b54f1-c605-3bcc-8cc0-d86449f7e83d | -4.5562 | -43.3028 | 2024-12-01 07:40:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 3748be81-adec-344c-99f8-a7e84b50eff2 | -3.259 | -53.6388 | 2024-12-01 07:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 610b2d2b-960d-3ff3-a616-dcd7ce8f4e4a | -3.1273 | -54.5264 | 2024-12-01 07:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| bfbe242c-6e20-306e-84fb-57346dd3de6a | -3.2591 | -53.6186 | 2024-12-01 07:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 7b985343-59a2-3aa8-af82-ce3027d3e294 | -3.1273 | -54.5264 | 2024-12-01 07:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| fba5cb50-dd5d-37f9-b9b5-26214c0f204f | -3.1274 | -45.3637 | 2024-12-01 07:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 127.5 |
| 16cb8beb-9539-3e3c-b29f-36e519fe7a6b | -3.1459 | -45.3854 | 2024-12-01 07:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 130.9 |
| 5c4342e7-4621-3ed1-bfcd-743cdb0d5d74 | -3.259 | -53.6388 | 2024-12-01 07:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 0ba80a4a-2eba-387e-a396-50709ece7afd | -3.1461 | -45.3404 | 2024-12-01 07:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 5c8bb0f2-11b5-3f0d-93be-7026612f12c8 | -3.146 | -45.3629 | 2024-12-01 07:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 374.2 |
| 4069c938-2110-3b8e-b517-a3e4ff55e5a3 | -3.1645 | -45.3622 | 2024-12-01 07:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 7007d572-160a-3a27-8d86-c314b44917f0 | -3.2591 | -53.6186 | 2024-12-01 07:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| a073895a-9491-39d3-a458-2354a3dad335 | -3.146 | -45.3629 | 2024-12-01 08:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 232.4 |
| b9b37232-ae37-36e0-a8af-6feceaa98acd | -3.1461 | -45.3404 | 2024-12-01 08:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 74a57240-c0ed-38a3-bba2-9ba045efa61a | -3.1274 | -45.3637 | 2024-12-01 08:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 276957ff-7c1b-369a-99a8-8cd466a09b58 | -3.259 | -53.6388 | 2024-12-01 08:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| eb0f2191-83dc-3908-b28e-3dcefd92b2e1 | -3.1459 | -45.3854 | 2024-12-01 08:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 90.2 |
| f7cd44b9-8c00-389a-9bcd-b6ccc2468c5f | -3.1645 | -45.3622 | 2024-12-01 08:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 71.5 |
| dc5521bb-9d6f-3f3e-ab80-aa74e550c04e | -3.16 | -45.39 | 2024-12-01 08:00:00 | MSG-03 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 212f84f7-f7bd-3d70-bb3e-e1d3f7042a96 | -3.13 | -45.35 | 2024-12-01 08:00:00 | MSG-03 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bb8bf35f-a49d-32bf-a23e-bec5882cbf89 | -3.16 | -45.35 | 2024-12-01 08:00:00 | MSG-03 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6aa2e952-ed7a-3f92-9bdd-08a15636ff99 | -3.259 | -53.6388 | 2024-12-01 08:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |


[Clique aqui para ver as próximas entradas](README101.md)
