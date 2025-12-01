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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 35ccc36e-7b5a-30d5-a77c-d4f19c5a8bdd | -4.4064 | -43.3351 | 2025-12-01 03:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 4c739ebc-c561-36c7-babd-2d2e887bf97a | -3.2174 | -50.139 | 2025-12-01 03:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 8c769800-3ff8-3da6-82f4-b13fa1fe0dec | -4.369 | -43.3373 | 2025-12-01 03:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| e2a8018d-c91d-3646-ae90-379e92ba932a | -6.3119 | -43.8036 | 2025-12-01 03:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 35cd3bfb-7deb-307d-9d49-2ad08c1adb88 | -3.7009 | -45.9 | 2025-12-01 03:20:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 46ec68a1-8131-3a8c-b382-70c8f0cbf614 | -4.3703 | -43.1508 | 2025-12-01 03:20:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 173.5 |
| 53078939-f2e9-31b1-8223-6de20291f36a | -3.7195 | -45.8992 | 2025-12-01 03:20:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 1531ff2a-8de5-3e13-8195-4558624f6783 | -4.3702 | -43.1741 | 2025-12-01 03:20:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| d494115c-bc7b-3c77-9593-22c2da36d085 | -4.3879 | -43.3129 | 2025-12-01 03:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 2dc50dbd-b78d-3bb1-9275-c9d3d5717cd0 | -4.4066 | -43.3118 | 2025-12-01 03:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| e1cb7b3c-a09c-31bb-8d40-798a21469c84 | -3.7195 | -45.8992 | 2025-12-01 03:30:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 842abd44-4409-33a6-b555-00d85a77e562 | -3.7009 | -45.9 | 2025-12-01 03:30:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 80.2 |
| c6290e61-3989-3718-8c8a-1bbb9f233abc | -4.3877 | -43.3362 | 2025-12-01 03:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 207.3 |
| 8d842938-b8dc-3766-a739-943af62f268b | -3.2174 | -50.139 | 2025-12-01 03:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 9ec04870-6ed3-31dc-bd8a-e6d654e76948 | -4.4064 | -43.3351 | 2025-12-01 03:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| cef62e3f-cce0-3c08-a365-7464910918ac | -4.3703 | -43.1508 | 2025-12-01 03:30:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 221.7 |
| 80dffa0e-0666-33fa-abd0-e6ae1f860f19 | -4.3879 | -43.3129 | 2025-12-01 03:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 2e989b06-0663-3e1e-95ca-e76374574947 | -4.389 | -43.1497 | 2025-12-01 03:30:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 135.9 |
| 8e48baef-a65b-316a-bf07-1d335e3a2793 | -4.3702 | -43.1741 | 2025-12-01 03:30:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| e29e7a8c-8da1-32ca-9bdd-ea48dfec2ab4 | -2.73643 | -45.21722 | 2025-12-01 03:34:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c6406770-ab83-3230-b2f2-5217db991b9b | -2.88343 | -40.46693 | 2025-12-01 03:34:00 | NOAA-21 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e2c336b2-4dcd-366a-a01d-24de7285fad4 | -2.93929 | -40.09933 | 2025-12-01 03:34:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e34102b7-190f-3125-aca8-ea0a481ac946 | -2.84937 | -45.62654 | 2025-12-01 03:34:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4fc4768e-c4da-310d-999f-12d6825679ce | -3.1452 | -40.18157 | 2025-12-01 03:34:00 | NOAA-21 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a350d3f3-33f8-346c-a6dc-afece58484f8 | -2.7344 | -45.21873 | 2025-12-01 03:34:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 760953bb-dcd6-354d-9ba0-4968de9ec7a2 | -2.85041 | -45.62066 | 2025-12-01 03:34:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fe65018f-4e74-33b5-8c44-4c56305869e1 | -2.847 | -45.62464 | 2025-12-01 03:34:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8007b11b-cbd6-3251-b7f1-42736e888f92 | -2.25159 | -45.61433 | 2025-12-01 03:34:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 4cfcf17f-6339-3bed-a665-107f6e48e1bc | -2.99301 | -41.47012 | 2025-12-01 03:34:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c7a497d9-6896-38fa-aff0-2c8be6dda1c2 | -2.24521 | -45.6209 | 2025-12-01 03:34:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3bb7a8c9-4629-34d5-9cc8-cdb32d98ff86 | -2.88215 | -40.46875 | 2025-12-01 03:34:00 | NOAA-21 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 50097ab4-3e54-377c-a2eb-b642ddda8319 | -2.34545 | -45.73977 | 2025-12-01 03:34:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b8d9a2c7-8e22-37a5-a850-2cd0d56b362c | -2.25304 | -45.61594 | 2025-12-01 03:34:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f552ef3e-1a4c-3e03-8b99-135e88e3d08f | -2.25058 | -45.62046 | 2025-12-01 03:34:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 58b0e919-c1cb-3400-8303-570954864c26 | -3.58696 | -40.42981 | 2025-12-01 03:34:00 | NOAA-21 | MERUOCA | CEARÁ | Brasil | 2308203 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cbbb2b7f-0acf-34b2-b32b-b30143e35b70 | -2.24626 | -45.6148 | 2025-12-01 03:34:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f668cdc6-c70f-3d83-8a0a-c078da85e9b0 | -2.2438 | -45.61927 | 2025-12-01 03:34:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d1ccadf0-fed2-3bad-a3c6-0d5dca4bb897 | -3.43505 | -39.04548 | 2025-12-01 03:34:00 | NOAA-21 | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 10229141-053e-3adf-9d76-72412fa9abc6 | -2.94246 | -40.0975 | 2025-12-01 03:34:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 33d6765d-3382-3c74-8b6a-0c585a8b6381 | -3.58617 | -40.43456 | 2025-12-01 03:34:00 | NOAA-21 | MERUOCA | CEARÁ | Brasil | 2308203 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1fbb3f48-470b-3130-be46-d60afeed21c2 | -3.70299 | -45.90342 | 2025-12-01 03:36:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 74812f52-1c5e-37db-9d83-79b6bb9b66f5 | -5.75177 | -40.81733 | 2025-12-01 03:36:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5caa2499-da51-363c-ac64-c3e8d322b8d5 | -4.385 | -43.33785 | 2025-12-01 03:36:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 22fe4796-79bc-35a0-aa9e-36863d0edc6e | -4.38433 | -43.34177 | 2025-12-01 03:36:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e46ace33-a9ac-322a-80c1-c713e9dfa15e | -4.37964 | -43.14929 | 2025-12-01 03:36:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 881fa3ca-c481-327f-828d-c0603977a7d8 | -4.37704 | -43.16483 | 2025-12-01 03:36:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9e9192e2-654e-344f-867a-d50886966290 | -4.38635 | -43.33003 | 2025-12-01 03:36:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 62d540cd-e06d-35f6-86ec-51f48159fe84 | -6.98286 | -37.62874 | 2025-12-01 03:36:00 | NOAA-21 | CONDADO | PARAÍBA | Brasil | 2504504 | 25 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 395d0709-9faa-3e9b-8472-38bc3061a001 | -4.6008 | -45.2111 | 2025-12-01 03:36:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a6c02def-31be-31b3-b9ea-49846c1b438c | -5.52716 | -42.59924 | 2025-12-01 03:36:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fe304c62-0ab3-37ee-b188-cc079ea90b67 | -4.36575 | -43.16287 | 2025-12-01 03:36:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a270589a-d34f-3cf8-a43f-f955213cec31 | -4.38527 | -43.15028 | 2025-12-01 03:36:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7c34fb84-03ba-3f27-a382-e0eec28e3115 | -4.39073 | -43.33871 | 2025-12-01 03:36:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f115f55a-8084-310a-befe-5ca58edc4d05 | -4.37638 | -43.16878 | 2025-12-01 03:36:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00cf7650-bcab-3332-a147-5e92562733e9 | -4.37835 | -43.15699 | 2025-12-01 03:36:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| fd54829c-a90f-3b1d-9583-f3047b902b3a | -4.39848 | -43.32781 | 2025-12-01 03:36:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5ef70047-deff-31dc-a013-7991dc57dcf2 | -5.49051 | -40.92992 | 2025-12-01 03:36:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 796f0da4-9ec6-3cf9-a152-9c60dfd1283a | -4.70478 | -44.40702 | 2025-12-01 03:36:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 07a7b384-bcf5-3d95-b708-83c05e20a3d9 | -4.37999 | -43.16494 | 2025-12-01 03:36:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0052594e-72c4-3125-815a-da4b37b43812 | -3.70839 | -45.90009 | 2025-12-01 03:36:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 152535b8-a50e-33f5-9726-d419027b433a | -4.59987 | -45.21638 | 2025-12-01 03:36:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b0a1bd64-d2b5-3db9-a174-659972c6e4fa | -5.3317 | -43.56611 | 2025-12-01 03:36:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 8662fa3b-0ab7-3b79-940d-6bab4fe34a50 | -5.52124 | -42.60171 | 2025-12-01 03:36:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d83e2da5-ff12-346f-bcfc-fb5336091109 | -3.70969 | -45.90491 | 2025-12-01 03:36:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 40.5 |
| fbaa17e7-4c29-36e1-8a76-b7c8476b0673 | -4.38704 | -43.32607 | 2025-12-01 03:36:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 323d82ec-9560-3035-b567-ae87510c110f | -5.14611 | -37.7482 | 2025-12-01 03:36:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0ac01519-fb18-3555-89ea-e666ed2ca94f | -3.32944 | -45.63947 | 2025-12-01 03:36:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 777711bb-bfcf-3376-aaf7-edc3781bc79d | -4.37139 | -43.16389 | 2025-12-01 03:36:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 24654881-31d4-3331-9741-97783589e2b8 | -7.14181 | -35.09916 | 2025-12-01 03:36:00 | NOAA-21 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 63fc5f44-368d-36d0-8e0e-d0ba4adca7d6 | -4.37335 | -43.15218 | 2025-12-01 03:36:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b13ccb48-c35e-31e1-95dd-0cde87058ff4 | -4.38135 | -43.15716 | 2025-12-01 03:36:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 12479459-6a1a-3440-b563-57ee618baf1e | -4.36938 | -43.15913 | 2025-12-01 03:36:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 157aa2d6-8805-34a6-95a5-cebae249a5dd | -8.54309 | -40.21446 | 2025-12-01 03:36:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9904682b-6c84-3c68-bd38-fb5d0877eb3b | -4.37638 | -43.15233 | 2025-12-01 03:36:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f9f4f30a-fe91-321f-bfd2-7ce700d69ef2 | -10.13435 | -36.33953 | 2025-12-01 03:36:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f57b2ae4-915e-384a-95be-12323bbdc697 | -6.66715 | -39.89254 | 2025-12-01 03:36:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5f4bb1db-4b5f-3f18-91e1-48e9a2b599ca | -4.37433 | -43.16402 | 2025-12-01 03:36:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3a56549b-c6f7-3b84-acb9-7fdb3e729eb1 | -5.51876 | -42.58414 | 2025-12-01 03:36:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bba0b00c-7476-3303-ab34-59bb37f207a2 | -5.33032 | -43.57402 | 2025-12-01 03:36:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| dfce4698-8e59-318d-bf5d-00df70c6617a | -5.33737 | -43.56736 | 2025-12-01 03:36:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a05b0993-74eb-35f6-88de-21afdcfa8de9 | -4.38028 | -43.14548 | 2025-12-01 03:36:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb3df518-9622-3900-9f12-ab11f56ccab5 | -5.52065 | -42.60512 | 2025-12-01 03:36:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 75b3f51c-7c02-386e-8ffe-d4b425afe624 | -3.70734 | -45.90629 | 2025-12-01 03:36:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 97886f3e-6074-3072-a684-3ec51b9464d6 | -5.33668 | -43.57128 | 2025-12-01 03:36:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b8cf5b12-4d92-37fd-9181-60dff46b3310 | -4.3664 | -43.15898 | 2025-12-01 03:36:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| caaa15cb-c4e5-33e6-bcbd-92a07e401d18 | -4.3677 | -43.15127 | 2025-12-01 03:36:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 72bb7604-1391-32df-a37f-1544b33c7daf | -3.13207 | -45.82765 | 2025-12-01 03:36:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| abcb1f3e-6c87-39f9-9e5e-a54057aa2ca6 | -6.31006 | -43.81406 | 2025-12-01 03:36:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 55bed067-d76f-38b4-8e8b-41b059dbf814 | -4.36869 | -43.16304 | 2025-12-01 03:36:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 18799100-2516-3710-a353-1442063d44b8 | -6.31781 | -43.81442 | 2025-12-01 03:36:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 93ebb03e-c408-3181-a017-9905004a2c45 | -4.37771 | -43.14474 | 2025-12-01 03:36:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 04e19b1f-175f-3f85-9218-c894020a6d56 | -5.75516 | -40.81591 | 2025-12-01 03:36:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7372ce50-b829-35c1-b954-d45c19599a5a | -4.37571 | -43.15619 | 2025-12-01 03:36:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 8dd8b073-134a-3cc3-a6fd-f580f3fcbc7a | -4.13298 | -43.72672 | 2025-12-01 03:36:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ed74ffc1-b6e6-3347-946b-5e52aa611e7c | -4.379 | -43.1531 | 2025-12-01 03:36:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b83e5240-fdef-3b9f-8db2-1efb1a119901 | -4.37139 | -43.14767 | 2025-12-01 03:36:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5a993bbf-05dd-3ef5-9b4c-6b3b6702bee1 | -5.33238 | -43.56223 | 2025-12-01 03:36:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 386bfe8d-d24c-3cbb-b74c-77e86343cdb1 | -10.04521 | -36.28305 | 2025-12-01 03:36:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| dcde4891-ef5e-3fe7-8f92-8600a2a3f285 | -4.3978 | -43.33178 | 2025-12-01 03:36:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e9b05f84-63f5-318c-9f1b-864f8dc88f41 | -4.39711 | -43.33576 | 2025-12-01 03:36:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |


[Clique aqui para ver as próximas entradas](README8.md)
