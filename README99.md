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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63291ffc-09ba-30e2-8337-9abbb967322b | -16.43532 | -57.27497 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 3eaa9b35-9e5e-37c8-baf0-a8ba358f65a0 | -16.43387 | -57.26247 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 017f6a73-c15d-313f-b078-aedb8957497c | -16.4332 | -57.26643 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a992e195-5d98-3140-8f05-3f23fb243e30 | -16.43254 | -57.27039 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b5c13479-9f16-373f-9b71-f5aef07c47dc | -16.43187 | -57.27435 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 617e3a12-b46d-3e64-ad24-53f4e6a332a6 | -16.43078 | -57.32304 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3e789dd1-e9a5-35a9-b870-356636522988 | -16.43053 | -57.28226 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 06336a41-de71-35ae-b189-6d0d347bddda | -16.43042 | -57.26185 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c31aa405-1c18-3d69-9c19-dacf0e2e21a1 | -16.42975 | -57.26581 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 8988f965-ef6c-3264-afb3-9d417f4cc152 | -16.42908 | -57.26978 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 2a6bd02f-2da9-3a44-aff0-0bcbb625274c | -16.42811 | -57.33891 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 81f4c884-19c8-3e34-b907-75c16546d5ad | -16.42732 | -57.32242 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c20ee688-309c-32bc-a491-8f6910c7cb13 | -16.42665 | -57.32638 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 6130cdce-17f8-35a8-a8af-4942b7a6d268 | -16.42641 | -57.28559 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 4395884e-f366-31e0-8cb0-944facb99de0 | -16.42632 | -57.39183 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8aab4d45-a867-3a41-a063-a139e4b1bd68 | -16.42464 | -57.33828 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 4b7306bf-9af8-3967-a548-6efdc17b020b | -16.42386 | -57.3218 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| c387a4cc-1494-3433-a30b-f63ad2c89034 | -16.42319 | -57.32576 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| e0983440-ebd4-3c7b-9098-a2e68e6bf9dc | -16.42118 | -57.33766 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 671765a9-1b71-34e4-acc3-a779384e546e | -16.4204 | -57.32117 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 20bf75ee-f212-35fe-bb7b-3f2ae708a219 | -16.4195 | -57.28434 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| deb78573-03fb-3aa0-b4b0-c64cd3b5e9f3 | -16.41895 | -57.30867 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| eea8dd67-8ea1-3b60-9495-e3c4421c07e9 | -17.84529 | -57.68169 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 9fcb0729-cd02-37e8-b8a9-349b93303043 | -16.41883 | -57.28829 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e6dc1a46-6a53-3eda-8963-1fc9f792cb6b | -16.41828 | -57.31262 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d7ea2673-817b-3503-8f6f-b5be4df3857e | -16.41816 | -57.29224 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b09a7663-7657-3022-a70b-a9c90d330062 | -16.41749 | -57.2962 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 9fe33b1c-6d0d-33cf-bddb-73526b0aa6d7 | -16.41694 | -57.32055 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d791f9e7-1ecb-3f65-a3fa-d3525f8c2b97 | -16.41604 | -57.28372 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| de5e4507-2a5c-3373-8307-9af371486e36 | -16.41549 | -57.30803 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5d1ea8c4-269c-3468-a8ab-a7d577307203 | -16.41537 | -57.28767 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 27b313b4-05eb-3020-9f6b-71c92d1d477a | -16.41482 | -57.31199 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| da5b785d-e08a-36ef-8357-db18ace477b3 | -16.4147 | -57.29162 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 19cd35cf-35e6-3cbc-b260-f197580901cf | -16.41348 | -57.31992 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 8abde83e-f19c-349b-88c0-0edefcaeebf9 | -16.4127 | -57.30343 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 16316280-3d0a-3fa5-a87a-4bc8b9482533 | -16.41203 | -57.30739 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| a2539240-73bc-3291-988e-1678923f1438 | -16.41191 | -57.28705 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 1dff1348-6332-356f-81be-3448cb2d13c1 | -16.41136 | -57.31135 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 9fa1e519-ee57-3b48-b38e-091668bc14cb | -16.41125 | -57.29099 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 46d456e5-ff2d-3c76-9748-1924078d636e | -16.41011 | -57.33975 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 62bac5c4-c99a-3113-80a2-f5455b8c9b0a | -16.40924 | -57.30281 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 92fd571a-d117-3db9-80f0-c858c01104c2 | -16.40857 | -57.30677 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 62176b3a-bb1f-3551-b106-89d19ccf5f32 | -16.40665 | -57.33912 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e8bdedf9-e249-3682-9d6d-4acea8b1d455 | -16.40598 | -57.34309 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 9f68c637-5a5b-3830-87b1-03481f676f86 | -16.40251 | -57.34246 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 0cf1a986-321e-3695-97fd-588e109d6f52 | -16.40184 | -57.34643 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 3a4301c3-0423-34c8-95ea-b68350b5d961 | -16.39856 | -57.38682 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 92100425-f7b9-3281-b686-b7b98e59e3d1 | -16.38045 | -57.36715 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b87798ef-6d62-3141-852f-93ed44187f9d | -16.37698 | -57.36652 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 3cf84b83-6aec-34eb-933d-768e7f97906f | -16.15996 | -57.42226 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 398f457b-fb45-3ae2-9610-40253b67040a | -15.96817 | -57.22532 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 487294a9-874c-3981-a111-67b20768e95e | -16.64083 | -57.16068 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 0ece2a44-0e78-36d6-9093-18109c136f97 | -16.63872 | -57.15228 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 7d9699f6-ced3-3484-a2b2-8f270e085af1 | -16.63806 | -57.15617 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| f9603d19-9197-3646-98d4-df92aa44ab36 | -16.6374 | -57.16006 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 29853692-47ee-3d6a-b0a5-270d219f57a6 | -16.63528 | -57.15166 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.5 |
| 72380cf5-5ee0-31ea-97d5-cfa019d1aff9 | -16.63462 | -57.15556 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.5 |
| ce085d23-4c62-3469-830e-f21a1f79489f | -16.63397 | -57.15945 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 27ed6a09-9075-343a-b33b-ba4191b9af0b | -16.63185 | -57.15104 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.5 |
| 065181e5-b2eb-37e1-ac23-cf8c93a42cf8 | -16.63119 | -57.15494 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.5 |
| a514eac3-be13-3c75-9ef0-f362b4b506d7 | -16.63106 | -57.13486 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.0 |
| 6629d6e3-98bc-33d9-bdef-1a56e07a4579 | -16.63053 | -57.15884 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 5c0c6536-f15b-39e9-b914-d9bbb0e0aa17 | -16.6304 | -57.13875 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.0 |
| 01f155b2-c341-3174-b4b4-676d6a74c509 | -16.62974 | -57.14264 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| e37d85f8-b400-3f11-b1eb-2eb1da1f4f5b | -16.62908 | -57.14653 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| 65ae964b-6474-303e-95ae-f1e51a7ded9c | -16.62842 | -57.15043 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| d1692e24-4bc2-32e9-a3e1-228f2f6f9e92 | -16.62794 | -57.13518 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 412e1424-7aa6-337a-b668-c78fe3a00a8c | -16.62776 | -57.15433 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 1dfa434d-b6ac-3dbc-842b-944d045d6467 | -16.62762 | -57.13425 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.0 |
| 8cc0225d-7a19-37d6-916f-8bc22b68555b | -16.62729 | -57.13908 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| a64d0c87-2194-31f0-b08a-98714d4ef32a | -16.62696 | -57.13813 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.0 |
| 1becb3ab-9296-3e2e-a97b-6365e23f2896 | -16.62665 | -57.14297 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 6458e1f8-6ced-323a-9c07-8a245148d76b | -16.6263 | -57.14202 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| 814b5c86-2cd6-30b8-b523-88807571cd8d | -16.626 | -57.14687 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 1474f1f3-4a54-3d78-aa6a-24a951e4df9d | -16.62564 | -57.14592 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| ddce9dd6-4ef3-3f4c-be4b-9df6eb6b9d5c | -16.62536 | -57.15077 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a9b6d38d-e6a3-3313-bcf3-9e9bb9e6071f | -16.62498 | -57.14981 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 15a87fb0-59f7-398a-9c38-68628bea94d0 | -16.62471 | -57.15467 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e8b67201-715f-3e18-b515-88395e639b64 | -16.62432 | -57.15371 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 9ea8fbad-5440-36e6-9bd6-3b7e9316abd1 | -16.62386 | -57.13846 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| c6873cd1-29bd-3601-b2c4-b572724aa0a2 | -16.62322 | -57.14236 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 790dc366-a269-3f75-ad4c-a7501c0cd583 | -16.62257 | -57.14626 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 5d0a55e9-7c51-3f1f-933c-79785eb9aa42 | -16.62192 | -57.15016 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a87db557-7da3-3874-aafc-d0f020cbb9f8 | -16.62043 | -57.13784 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 0d79375f-4edc-3b2a-8a0d-f6bc2439e910 | -16.61978 | -57.14174 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| f89eaffe-ba62-39fe-b515-8c80bc636f81 | -16.61914 | -57.14564 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 08c06e90-275d-398d-b01a-ccf24384f55c | -16.61849 | -57.14954 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 62eb6fd6-d369-37ea-bc44-8a546de2dabd | -16.61699 | -57.13723 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| cfa9e5ee-f94f-3739-80bd-78955b776436 | -16.61635 | -57.14112 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 38230e4a-3e80-3a2a-a307-8427b207cdaa | -16.6157 | -57.14502 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 9c989cb5-70db-3b8f-9ffc-0a6b80dca7f5 | -16.61505 | -57.14892 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| cc06fe4c-1234-3802-8e60-2e8c6ad0de02 | -16.61441 | -57.15283 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| e5e409ef-a5d5-32c4-82ae-9c8e1b77ab99 | -16.61227 | -57.14441 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.8 |
| 02499b2e-d897-3148-9973-55631dfde9c1 | -16.61162 | -57.1483 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 57cb3725-ef31-3c1f-8be3-275314706906 | -16.61097 | -57.15221 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 81e61796-3e79-3f46-bc9a-4d2f227d75ea | -16.50914 | -57.73892 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 274c900c-2f21-366e-89e0-8d1ba41ef038 | -16.50846 | -57.74301 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 4dc55581-85be-3470-8d71-383bf40b1c64 | -16.50842 | -57.72174 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e6602694-9232-39b5-a206-d70e30f13312 | -16.50772 | -57.72592 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 4640463a-11cc-343d-af83-30d71a0e7106 | -16.50632 | -57.73418 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |


[Clique aqui para ver as próximas entradas](README100.md)
