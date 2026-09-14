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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 117e541c-cf43-3fa7-8721-0f9296921396 | -6.30614 | -55.2839 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfa533b3-99ef-39f5-ba9e-bad377e00ea6 | -2.95116 | -50.40222 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6612b156-dc17-3554-80e9-2cd801a34998 | -2.93272 | -50.41851 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7a78d37a-0534-3a24-adf0-43d5f63ae589 | -9.12668 | -51.58481 | 2026-09-14 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a89a95c3-40b2-3254-8216-4dcc79cb4837 | -3.38708 | -50.76423 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2345e973-29a0-35c8-b7db-4b4f9c24e75a | -2.7859 | -51.36266 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| da86a26a-6e97-380b-b02a-7b9bdabb90b2 | -6.77522 | -42.74723 | 2026-09-14 04:32:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| eb4a715f-a081-3db9-8103-eb160f44b9dd | -2.92067 | -50.39267 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9e1062c8-636f-3a60-953d-6fad68dd4b3b | -6.33308 | -46.38566 | 2026-09-14 04:32:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a9670f9-4dbf-3d3c-b5d1-ad1359409fe8 | -2.91174 | -50.44556 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| dad0fff3-fc6a-3c5c-9373-6da437efd244 | -2.92219 | -50.43816 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 723b3ff2-9c6d-3ca4-85ee-d613b416a106 | -7.2286 | -47.55475 | 2026-09-14 04:32:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9b3bb0a9-5c92-3097-a3db-7be842f79bd4 | -7.42284 | -41.93261 | 2026-09-14 04:32:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 03ba226a-06c5-31c9-ab07-0ffaf0fad3ba | -5.81395 | -42.74194 | 2026-09-14 04:32:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 66ee3b44-117c-30ad-9af8-9572d5adcada | -2.89339 | -50.43462 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| bf6b172a-80fa-3bb7-8982-59a0f871b73d | -2.9311 | -50.41245 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 40514d5d-2050-3479-b826-cafed4e10625 | -2.91997 | -50.45138 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8104afee-bd54-3bb3-b291-916d50e2f63b | -6.57474 | -58.84793 | 2026-09-14 04:32:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| aa043e27-d096-3f81-8152-eb7d81ad62da | -7.86747 | -54.71643 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9abadb9-fcbd-32e0-b8b1-9fb7f88c6421 | -3.3741 | -50.39705 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce76b75f-b7a3-3824-8083-8970152a14e6 | -9.44176 | -47.86021 | 2026-09-14 04:32:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd3b8784-9949-30b5-a73a-f83bed544cb9 | -4.76015 | -42.78874 | 2026-09-14 04:32:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0bc30c94-ec59-3cfa-86e4-6ae6870fd612 | -6.20769 | -45.40132 | 2026-09-14 04:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6079be1-95fb-3549-8899-a398bb2ebb55 | -3.53841 | -53.98178 | 2026-09-14 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 786aa45f-d8d4-363d-a613-78cd3a3f95b2 | -2.91932 | -50.41628 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 133.6 |
| 17033011-4804-3bad-8f26-72fcffae63cf | -9.84926 | -48.34411 | 2026-09-14 04:32:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77a152a2-4223-3538-8b6d-9d86aca4a5f0 | -6.32652 | -44.17953 | 2026-09-14 04:32:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b49bde2b-b065-386e-81b3-8fc3af3c3632 | -6.32972 | -44.11565 | 2026-09-14 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57f1af3f-0439-34e9-b771-7f31578cd83a | -5.13504 | -55.95273 | 2026-09-14 04:32:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6f236604-53bf-3c08-b555-d8de9b3a79d9 | -4.35994 | -50.85681 | 2026-09-14 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd3b11f7-ad71-3da1-bb09-0486534f7309 | -6.11397 | -57.66909 | 2026-09-14 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f2c37c80-09ff-370a-9383-ba1651ab92b2 | -2.92732 | -50.395 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dd105fc1-a33c-37a7-a261-31e1e1732504 | -3.24192 | -43.0265 | 2026-09-14 04:32:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7485acc5-8666-374d-9209-dce3660cfa7f | -2.93935 | -50.44551 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 011792b6-d647-3f94-949c-d59142f0e692 | -8.54373 | -54.69434 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17528fd9-b10f-3fbf-a949-5060afbc734b | -7.47365 | -42.11489 | 2026-09-14 04:32:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| aa62d536-5fe7-3a68-9dec-9dd6291fe4e4 | -2.69752 | -57.53807 | 2026-09-14 04:32:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 31310feb-968b-3b4f-b925-e650658aa40e | -9.48538 | -45.46833 | 2026-09-14 04:32:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c4928e7-409f-3189-964c-70d31989c7e3 | -2.92145 | -50.40303 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 1a2cf613-5ed1-3a2e-b639-24da8303485b | -6.86963 | -55.29567 | 2026-09-14 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f12379e5-754b-3a50-85f0-1ab6a19848c2 | -9.14128 | -51.57864 | 2026-09-14 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63dd0a4e-a1e9-3a03-9490-b3bf71b15998 | -3.24528 | -43.02703 | 2026-09-14 04:32:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 427805ac-0bd4-3f1c-bbf6-fbd27c655fa0 | -8.79468 | -47.71261 | 2026-09-14 04:32:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3d8e8ac-8b4a-376f-bfe7-857f77ac2b56 | -7.07876 | -41.79999 | 2026-09-14 04:32:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e47045b3-ff15-363b-8149-08514b5bbe39 | -4.34791 | -48.96301 | 2026-09-14 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| f4566fe8-cbf3-335f-ad23-388820f33ed9 | -4.85784 | -48.35986 | 2026-09-14 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 3cecbcf1-6671-31a7-b993-2081fb2f2441 | -9.41174 | -50.16859 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| ae64c01d-d153-3d45-a8a8-aa1f9c92a1b4 | -2.91464 | -50.38837 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 82f3321b-b25c-3bea-a0f6-025e3057749b | -2.91343 | -50.42437 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 193.1 |
| 5e5dc5d1-dd19-3d8c-b54c-5cf1384915a2 | -3.54342 | -53.98639 | 2026-09-14 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 76f875b5-0b5c-3296-99e6-3acaa44d2930 | -5.03438 | -42.729 | 2026-09-14 04:32:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b3252289-c14d-3bf0-ab6c-c5e1dedf4321 | -6.30689 | -55.27975 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36bbe3e4-59ce-3596-8b3f-d41b48274ffb | -6.8451 | -55.56488 | 2026-09-14 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 569745d3-4f26-328e-aadb-34fd2ce7434e | -2.92439 | -50.3978 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2f6f903d-ce74-3a01-987a-105011e720aa | -4.13634 | -54.01864 | 2026-09-14 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d901e01-1e12-317e-9dc9-3f552fe02422 | -2.88963 | -50.42949 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 9cf7d9f7-056c-30d8-bcbe-e47196ce1daa | -3.37925 | -50.39344 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9d20730f-b39f-3aeb-87a5-6fcb5051e5ff | -5.81572 | -53.80436 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 105f955f-abd7-3643-8409-fc3d9f84bc28 | -5.81633 | -53.80095 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e9339f85-a7d5-356c-9b84-0cd1102587ae | -9.45121 | -50.12814 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 69219c0c-198a-36c6-a604-6d970b47e278 | -3.79659 | -44.11414 | 2026-09-14 04:32:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| afd9aad2-05df-30d1-a29f-6af1749b5986 | -3.38879 | -50.39082 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| eb8a8c19-446d-3b22-aac3-fcf7d81a1a32 | -8.05959 | -46.83096 | 2026-09-14 04:32:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 63e17c1a-3415-32e8-b804-c8c7fcb4d7bb | -2.66801 | -57.53974 | 2026-09-14 04:32:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 444548f8-72b6-3414-ad87-496f8ba83520 | -7.9694 | -43.98526 | 2026-09-14 04:32:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0880adf7-b148-3966-8e8f-277fdc268fc6 | -8.54018 | -54.71889 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16a68e3f-e806-3a1b-bd6e-f6dad050e5cf | -2.69478 | -57.53365 | 2026-09-14 04:32:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33da4637-ee96-3d1b-aaa8-84e7e1b06f95 | -6.2938 | -55.28517 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec43f38c-133d-3033-a5a6-20b096fb8690 | -3.22997 | -50.5875 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d47417fb-1a4d-3fab-82c4-4e51a3227b64 | -8.38816 | -46.29491 | 2026-09-14 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 51925d12-d8e5-321b-91d6-cf885580b5d9 | -2.9167 | -50.4612 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b36bb294-4486-30bb-9c9b-d8b7bf226841 | -5.81037 | -53.80331 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 53452881-90d7-3766-9936-2988d5757773 | -2.92754 | -50.42221 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 57649891-17e8-3dc5-8abf-1182ad916882 | -7.11335 | -41.79478 | 2026-09-14 04:32:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| a838d34d-ae14-3eaa-bd62-c6e705332c69 | -7.10409 | -41.80355 | 2026-09-14 04:32:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 8eb78065-8423-3126-83f8-f316da786c3c | -6.58777 | -58.85815 | 2026-09-14 04:32:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eee3e565-c2b0-3363-8ea0-394335f5b70b | -3.1161 | -53.9471 | 2026-09-14 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 922cce60-c9e9-3232-a6a5-31aa4dcca271 | -6.29506 | -55.28714 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5abe593-cacc-3d6c-9d91-04598eeb5fc5 | -8.11679 | -54.80513 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e976727e-47c2-35c2-8c2d-a39f6b393277 | -6.33803 | -44.10623 | 2026-09-14 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 25455132-8a76-31f2-bc9e-7e7218f02bdf | -6.582 | -58.85473 | 2026-09-14 04:32:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| dff94507-fb64-34f3-9a5f-dff4b2f6fbcf | -2.93555 | -50.40083 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cf50c70c-30fd-3f17-9297-f86c8dc1a761 | -8.58988 | -44.45613 | 2026-09-14 04:32:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1419bb06-d218-330f-b3c0-fe4e5b312503 | -4.13513 | -54.01387 | 2026-09-14 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5cd6e58-48cd-3474-a4e4-d0d37de92e6d | -2.9192 | -50.42865 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 274.4 |
| 8921e8df-17ec-338e-a07c-995bb60df886 | -10.31544 | -45.2888 | 2026-09-14 04:32:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f84280f1-971e-3df2-8c4f-dbf0109de706 | -4.09549 | -54.43915 | 2026-09-14 04:32:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a006e76-1abe-3beb-af7b-8a02213c31ee | -3.37649 | -50.77189 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fad04715-1030-32a2-becb-a8ca83ee52c8 | -9.45005 | -50.1242 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 15fa2531-759d-3549-9f91-1448f9fc03d6 | -2.91181 | -50.40597 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| edded82a-4866-33a9-88b5-adb048f04e21 | -6.33851 | -43.36631 | 2026-09-14 04:32:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| f92ece54-c047-32b1-a38f-0a173f779b20 | -7.09068 | -41.81863 | 2026-09-14 04:32:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 07530a1b-ae22-3a23-be9f-85bd2044bdbd | -7.87232 | -54.71891 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80e4f6d0-aeae-33a8-943a-be8db60984f0 | -2.88372 | -50.43758 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a35b930b-2103-3613-bfd6-1e7183d014f1 | -3.44494 | -47.27236 | 2026-09-14 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c51085d9-5806-3a3e-807c-c66e7977d300 | -5.28762 | -45.26569 | 2026-09-14 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 93e962a3-82b5-3dba-9f52-3740e326ae86 | -2.9115 | -50.46489 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9f4be26-3524-3d06-b179-56e59470e59d | -2.88892 | -50.43389 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 48726618-d75b-321a-bf95-f427597a53a8 | -2.91364 | -50.45164 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 3d763de4-b8de-3375-a02c-4944e11a0817 | -8.39616 | -42.21914 | 2026-09-14 04:32:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |


[Clique aqui para ver as próximas entradas](README20.md)
