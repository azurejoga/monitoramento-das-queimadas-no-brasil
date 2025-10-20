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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8bf76f9e-fe5e-3022-a5a7-5c4cf485dcad | -4.42185 | -43.88621 | 2025-10-20 05:59:00 | AQUA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8886b351-acd3-3430-86fd-778282ee12d3 | -2.86719 | -50.71321 | 2025-10-20 05:59:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d066c98d-707d-374c-b8f4-9231fd23b082 | -4.42529 | -43.89219 | 2025-10-20 05:59:00 | AQUA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 677fa910-953c-38d7-8d5e-d9d3daf39b01 | -2.2435 | -51.90944 | 2025-10-20 05:59:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 70baadce-0824-35ac-9a36-7966facf4770 | -6.36607 | -46.14983 | 2025-10-20 06:01:00 | AQUA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 04370a83-cb8f-3a66-a001-25f1322e8bd9 | -6.8744 | -43.58346 | 2025-10-20 06:01:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 16.7 |
| e8e1092e-446c-36ce-95b1-c1385dec8a31 | -6.89475 | -43.58645 | 2025-10-20 06:01:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 4303d83b-06b5-34fc-9212-33ba2ec7bb44 | -6.88457 | -43.58502 | 2025-10-20 06:01:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 790ab22f-f4ae-325a-adc3-9b0f4e60fb8a | -6.88288 | -43.59703 | 2025-10-20 06:01:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 1b6fa011-7857-3d06-9a15-4bb5b181c3ca | -6.79487 | -47.53777 | 2025-10-20 06:01:00 | AQUA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9c455752-1443-3c09-a000-82ec47e6d7d2 | -8.42452 | -44.12561 | 2025-10-20 06:01:00 | AQUA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c0f88a7e-e180-3579-aeab-45794a373f7c | -5.61743 | -43.64251 | 2025-10-20 06:01:00 | AQUA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 480ac87c-d69c-3cd3-96c3-28af705e4fda | -6.36473 | -46.15881 | 2025-10-20 06:01:00 | AQUA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1a6e3a66-e803-3b94-b96a-8b67cc4c5ebc | -10.86593 | -47.44165 | 2025-10-20 06:01:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b7677581-621b-317c-b9ef-e5605862f18c | -14.18982 | -51.52025 | 2025-10-20 06:03:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 7ecb14ed-3fe6-3ac0-9bab-d63940f17262 | -14.19442 | -51.4321 | 2025-10-20 06:03:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 355a08e9-6356-31b5-b4d6-16bae6f3ef3b | -14.19587 | -51.54366 | 2025-10-20 06:03:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ef2c8b93-8604-36a8-b89f-c137b932ed61 | -14.18804 | -51.53114 | 2025-10-20 06:03:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 8bce1818-27cc-3cab-ba17-fb4df158bff0 | -14.20397 | -51.43371 | 2025-10-20 06:03:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 00ad2e58-406c-3654-b1a6-a7b24154639d | -14.17842 | -51.52952 | 2025-10-20 06:03:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 6446277b-7e81-3719-8ea2-7a32559bbb51 | -14.17663 | -51.54041 | 2025-10-20 06:03:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 578f821e-67c7-352a-b160-a87304a2c0b3 | -14.18625 | -51.54204 | 2025-10-20 06:03:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 47.3 |
| b2750692-c095-396c-940c-3e492e97a9ee | -14.23264 | -51.43853 | 2025-10-20 06:03:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ff42397b-6c5e-32b8-9368-c9fdb2902f12 | -19.0359 | -49.6901 | 2025-10-20 06:05:00 | AQUA_M-M | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| f890cafc-0ff2-3b94-be42-1a2812132324 | -19.03452 | -49.69936 | 2025-10-20 06:05:00 | AQUA_M-M | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 733279a3-cdef-31d4-9949-1fac6ad71ce8 | -22.07364 | -46.89859 | 2025-10-20 06:05:00 | AQUA_M-M | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 18.2 |
| c5d3c006-0639-34f3-a79b-7ed7f18a7c55 | -8.10712 | -39.45882 | 2025-10-20 11:19:00 | TERRA_M-M | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 53.2 |
| 2325b7dc-58ee-3d44-8ef7-b9ad3bf512bd | -8.10399 | -39.47854 | 2025-10-20 11:19:00 | TERRA_M-M | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 80.0 |
| 81bd901a-b5b4-3171-874a-6857c42d3a20 | -7.33256 | -37.33655 | 2025-10-20 11:19:00 | TERRA_M-M | BREJINHO | PERNAMBUCO | Brasil | 2602506 | 26 | 33 | nan | nan | nan | Caatinga | 26.3 |
| af4daa42-c3ff-3bee-b5df-a89f08568543 | -9.51507 | -37.14436 | 2025-10-20 11:19:00 | TERRA_M-M | OLIVENÇA | ALAGOAS | Brasil | 2706000 | 27 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 20af7111-99ff-3753-8108-bead2c3b036b | 1.7115 | -55.9418 | 2025-10-20 12:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 124.3 |
| e4f2f6f3-f185-319f-ab40-e0c7fa5aa05a | 1.7298 | -55.9415 | 2025-10-20 12:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| e8ad0731-78c9-39f5-a89e-1d46b857b7d4 | 1.6935 | -55.7843 | 2025-10-20 12:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| edcd8de2-7e16-35a8-9edb-d164c676975b | 1.7298 | -55.9415 | 2025-10-20 12:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 90b93d34-e47d-3fb6-a06d-8ef0ab79ce7c | -11.4355 | -44.2344 | 2025-10-20 12:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 189cca6f-a3d2-3901-8239-b925545ba6ac | -11.4543 | -44.255 | 2025-10-20 12:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 133.9 |
| b4b8cc89-e5aa-3719-9f2c-c4975ff1056a | 1.7115 | -55.9418 | 2025-10-20 12:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 118.0 |
| 2359b16c-5212-32a0-bc1d-5fcdb046ea5b | -11.4351 | -44.2579 | 2025-10-20 12:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 128.8 |
| e0b53b77-bf56-3b01-8c0a-1c30274ae8c4 | 1.7115 | -55.9615 | 2025-10-20 12:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| b4f3f4a4-47b6-3612-9a9f-ac50cc4ecccb | -14.2052 | -51.5488 | 2025-10-20 12:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 14ed0b8f-57af-3d96-bf47-aed9b51c90f3 | 1.7298 | -55.9612 | 2025-10-20 12:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 9f54b8ae-c8ce-368b-b7eb-751f95b72e0d | 1.7298 | -55.9415 | 2025-10-20 12:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 132.8 |
| 925add2d-5568-3190-856d-34720f2a1a23 | -11.4547 | -44.2316 | 2025-10-20 12:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 134.7 |
| b668ff3e-7103-3d86-bba7-1e81ff6906eb | 1.7115 | -55.9615 | 2025-10-20 12:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 369c32ac-3dd8-3a2a-80fe-ae5fcc2f74b9 | 1.7298 | -55.9415 | 2025-10-20 12:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| c599ed9d-07a2-3e8b-b853-ced06c1c5be2 | -14.2457 | -51.4364 | 2025-10-20 12:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 7d15800b-6926-36a4-8876-5c369eb7e1b7 | -11.3976 | -44.2167 | 2025-10-20 12:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 3fb4707a-3628-3e61-ba3a-4bb67c33df02 | -11.4543 | -44.255 | 2025-10-20 12:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 46e9da49-1c93-3a7b-98b5-ec9057297c4d | -14.2052 | -51.5488 | 2025-10-20 12:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 94.4 |
| af8c6300-3a40-3611-b87e-500b280fa16c | -11.4739 | -44.2287 | 2025-10-20 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 138.5 |
| f9cae3de-5782-3ecb-a89a-d6826cd4997d | -11.4735 | -44.2522 | 2025-10-20 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 140.4 |
| 9ddb00df-98ee-3da9-9c1a-8d0bc161796c | -14.2457 | -51.4364 | 2025-10-20 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 102.6 |
| ff352416-a193-3c28-8100-2b19c1275250 | -14.2395 | -51.8004 | 2025-10-20 13:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 8ff14ac3-1575-3aac-bf1d-12ecacf0402f | -14.1863 | -51.5299 | 2025-10-20 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 48eb0108-9a21-3218-8b0e-9fc583b4762e | -14.2052 | -51.5488 | 2025-10-20 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 124cf6ba-16d2-3fc9-92cb-2ffe19440ed8 | -11.4752 | -44.1584 | 2025-10-20 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 942d5a4b-6969-3f2f-bcf6-1c3dc76c4e1e | -11.4939 | -44.179 | 2025-10-20 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 6095930e-ad4f-304a-a3ac-3bca953e9020 | -11.4748 | -44.1819 | 2025-10-20 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 687d84f4-3fce-3eba-bfaf-c126f37d8988 | 1.7115 | -55.9418 | 2025-10-20 13:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |
| ecd05806-ddac-3ec9-8892-ce24a49cf06d | -14.2457 | -51.4364 | 2025-10-20 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 98.0 |
| e7a2fe7a-ef8f-3810-8c00-4a066c3f05d1 | 1.7298 | -55.9415 | 2025-10-20 13:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| b273d4e7-73c9-3ff0-8980-ed6e07236c54 | -14.2577 | -51.8619 | 2025-10-20 13:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 92.6 |
| decdca40-7568-34c8-8837-6d31c8a29447 | -14.2052 | -51.5488 | 2025-10-20 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 69148e73-6eb2-37b6-b62e-ba0ecda068dc | 1.7298 | -55.9415 | 2025-10-20 13:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| b334fc55-2bff-3aa0-9b4b-6490b6e1a9e0 | -14.2264 | -51.439 | 2025-10-20 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 00d5ec7b-16ae-380b-a3d7-94def7b394ae | 1.7299 | -55.9218 | 2025-10-20 13:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 30c2c19e-458e-37bc-873d-048aba6285c7 | -14.2577 | -51.8619 | 2025-10-20 13:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 4e2b6a79-c838-3dc8-9633-8f03e0677d54 | -14.277 | -51.8593 | 2025-10-20 13:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 57856dcb-7dc0-357d-8a99-d393b0f8c5ff | -14.2457 | -51.4364 | 2025-10-20 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 113.0 |
| b2e527e9-ac45-3801-adc9-e623bfd7ade2 | -14.2457 | -51.4364 | 2025-10-20 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 154.8 |
| e7bef203-6f1e-3053-9f24-837cf4276736 | -14.277 | -51.8593 | 2025-10-20 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 90.5 |
| f3107ece-cf21-3555-a5da-11a7821ea7e9 | -14.2264 | -51.439 | 2025-10-20 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 154.1 |
| 4ed5319c-0333-3cca-9074-c68ed3d810e6 | -14.2577 | -51.8619 | 2025-10-20 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 100.3 |
| d0fc7ced-3a09-3517-8e56-cea2ab57a95f | -14.2573 | -51.8832 | 2025-10-20 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 946b5a27-d412-33df-8b19-a2449390da0d | -14.4523 | -52.8961 | 2025-10-20 13:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 6268bc1f-62f4-3503-900e-ccad91b91a4c | -2.7236 | -48.8393 | 2025-10-20 13:30:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 176.8 |
| 88380305-dfc1-3cfd-a83d-bd3edb453adf | 1.7298 | -55.9415 | 2025-10-20 13:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 5d463527-5bce-3994-a00d-4c569d42ee85 | -14.2205 | -51.7815 | 2025-10-20 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 28da31be-92d0-3a50-859d-6044454261a9 | -14.2395 | -51.8004 | 2025-10-20 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 505fd383-b786-3dff-9eb1-5160a7512eba | -14.4764 | -51.4909 | 2025-10-20 13:40:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 8b20d539-af27-33f7-8d32-58f6093e5d82 | -14.2387 | -51.8431 | 2025-10-20 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 90.0 |
| f7303121-6d97-3bbb-906b-d88a21950f62 | -14.1811 | -51.8293 | 2025-10-20 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 93.2 |
| dde1c80c-3a81-33df-b42e-1bacc35fde3f | -2.7236 | -48.8393 | 2025-10-20 13:40:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 186.7 |
| 477d0ae3-730f-37c8-b3dc-a7422fedd163 | -14.277 | -51.8593 | 2025-10-20 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 95.8 |
| ff35cd57-7c75-35b6-8d9d-636387723e4e | 1.8036 | -55.6842 | 2025-10-20 13:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 1e0c010d-7a1e-3d70-88df-1f04cbe55019 | -14.4523 | -52.8961 | 2025-10-20 13:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 9d0332f1-6cd2-3f77-8ce6-02831c1105ec | -11.3988 | -44.1464 | 2025-10-20 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 84cbabfc-3e95-3f3a-8fa7-c27ff7d3360e | -14.2577 | -51.8619 | 2025-10-20 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 103.7 |
| f9e1952f-83a0-3931-9ea0-b1f02f141b82 | -14.2264 | -51.439 | 2025-10-20 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 52065d6b-4c0b-3208-992e-3522fe3e4eec | -14.1859 | -51.5513 | 2025-10-20 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 106.0 |
| d967f6ae-bef3-3c67-889d-23dc41140421 | -14.2398 | -51.779 | 2025-10-20 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 65c295b0-64cf-3496-98ce-4a4348ecaa24 | -14.4377 | -51.4961 | 2025-10-20 13:50:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 1af3d7c7-d0ca-3d4f-8b0b-795edc63109b | -14.2457 | -51.4364 | 2025-10-20 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 3b34f64c-ce01-3909-9f87-af1e1ce1583f | -6.2092 | -40.965 | 2025-10-20 13:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 122.7 |
| 574b79ea-3a63-36c1-bcca-72480805f7ec | -14.4764 | -51.4909 | 2025-10-20 13:50:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 63c1a95d-a43c-3582-8c04-12cc505751c4 | -2.7236 | -48.8393 | 2025-10-20 13:50:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 108.2 |
| c3c5ea96-f06b-31a6-bd4b-99df3b4d8ee3 | -6.1512 | -41.1161 | 2025-10-20 13:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 114.8 |
| b27017f1-c014-3227-9b95-111b89764273 | -5.2863 | -41.0673 | 2025-10-20 13:50:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 83.6 |
| 71f50a2e-e7c1-30e2-96ec-4bfb45ad286b | -11.3584 | -44.2692 | 2025-10-20 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 1351dbe0-cb03-3502-961c-ebb4201a5ade | -6.209 | -40.9894 | 2025-10-20 13:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 106.7 |


[Clique aqui para ver as próximas entradas](README23.md)
