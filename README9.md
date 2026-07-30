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
| 07e20582-bca7-3d45-abcc-eecf309ecc17 | -18.35402 | -47.19708 | 2026-07-30 04:17:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 999a1aae-32cd-3e22-bbb1-717dc9ed4d21 | -20.47457 | -45.18313 | 2026-07-30 04:17:00 | NOAA-20 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 59358d41-378c-37b8-b17b-9d5d43c119ab | -21.35172 | -44.80999 | 2026-07-30 04:17:00 | NOAA-20 | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 0e198d97-7b98-3fc3-9601-39d34e7faadd | -17.69563 | -44.04773 | 2026-07-30 04:17:00 | NOAA-20 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72447997-9df9-35e5-8800-ddd9811fc79a | -18.89928 | -46.06947 | 2026-07-30 04:17:00 | NOAA-20 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e955e51f-ed12-322c-b9f9-764f5aa00f8d | -18.47532 | -51.73138 | 2026-07-30 04:17:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f358923-7b6d-318c-9e66-bee69ee9e274 | -18.23348 | -42.2124 | 2026-07-30 04:17:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 26.9 |
| e693c971-4d01-3c36-8f77-7d34f221500e | -21.35547 | -44.82963 | 2026-07-30 04:17:00 | NOAA-20 | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| f8566fa4-916a-38fd-85ec-77128da554de | -22.41179 | -42.245 | 2026-07-30 04:17:00 | NOAA-20 | CASIMIRO DE ABREU | RIO DE JANEIRO | Brasil | 3301306 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 789b99dd-02dc-330e-8ca7-ea9d5c8e7b69 | -10.9397 | -43.0593 | 2026-07-30 04:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.7 |
| eea8cef7-12b9-386b-87b4-7b14df32a623 | -10.9205 | -43.0622 | 2026-07-30 04:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 62.4 |
| b4a2b5eb-be65-3b65-b49b-68bd6ccfcf0a | -18.2374 | -42.21 | 2026-07-30 04:30:00 | GOES-19 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 59.2 |
| 6fa25ead-fe68-34f2-8bbb-170dbda69e6e | -10.9397 | -43.0593 | 2026-07-30 04:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 97915f9b-1d3c-3fc3-8393-5c4af00a83db | -10.9397 | -43.0593 | 2026-07-30 04:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 8903c291-de9a-353f-bf4c-1f219c08e309 | -10.9397 | -43.0593 | 2026-07-30 04:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 93e79812-55f1-3088-97c5-cfedfd2fa585 | -18.2374 | -42.21 | 2026-07-30 04:50:00 | GOES-19 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 68.3 |
| 6436626a-5527-3d35-a893-2fc3c9640a78 | -0.85623 | -52.7159 | 2026-07-30 04:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9622d257-7d47-35ba-a3c9-aa1f47f5bfb6 | 1.76586 | -60.23135 | 2026-07-30 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4206e8e-ad54-3dd6-a534-124821bff500 | 2.14433 | -50.7062 | 2026-07-30 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 37c2d29c-8321-329d-8ecd-46c9e7bd0ac1 | -0.08961 | -51.28145 | 2026-07-30 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ae0efd42-b02e-338b-9b32-cc30faae870d | 1.76832 | -60.22896 | 2026-07-30 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 12cdd6cc-b40a-3e96-95bf-9183a3b85241 | -1.59009 | -50.43937 | 2026-07-30 04:55:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 09d80fa9-f874-3032-accc-1ea30774546c | -1.59068 | -50.43893 | 2026-07-30 04:55:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| de035660-eb4c-370f-b746-8f54b32db1f5 | 1.77076 | -60.23068 | 2026-07-30 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b033d287-bb54-3b96-b0e7-f77ddc673955 | 0.92536 | -60.5375 | 2026-07-30 04:55:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09cf6bbc-6985-3056-80b1-06f7ac1691e6 | -3.16811 | -48.13604 | 2026-07-30 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 793a1db4-0b05-3308-961b-62fea52fe3fc | -9.61409 | -47.7669 | 2026-07-30 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 94627f4b-d1db-3553-8763-c1d0ce3922e9 | -3.18525 | -48.02064 | 2026-07-30 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69a58518-32e1-3112-89f5-ec7900c1a7e0 | -4.38742 | -47.75541 | 2026-07-30 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bfab05e4-1361-368c-ba9b-a8570fc4f5d9 | -6.85711 | -56.53022 | 2026-07-30 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57a249ee-6a69-3d15-989b-0e6dfd1bf791 | -6.22483 | -55.65888 | 2026-07-30 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb546244-486f-3646-886d-64e2a1e7108c | -7.54698 | -46.90141 | 2026-07-30 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c5ddecde-4fd2-3a59-9094-7b00379739a3 | -4.56091 | -48.02171 | 2026-07-30 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0710f113-a8a0-3241-a522-8ccb2d808889 | -9.45351 | -50.31194 | 2026-07-30 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14f801b8-f111-3fae-b3f8-dfa2dc1146c9 | -2.78826 | -49.58196 | 2026-07-30 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e99d74f9-39d4-3b6a-9f9d-8465610a4bb1 | -7.39048 | -49.74583 | 2026-07-30 04:57:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f987bb7b-b9a9-3472-8317-654205b62e1d | -9.2223 | -50.10736 | 2026-07-30 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa5f15c1-151e-3a05-920c-1a8447db5427 | -5.82878 | -44.1419 | 2026-07-30 04:57:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 367f80fe-7ccf-3b9f-a286-0dff88cb8513 | -3.17998 | -48.02756 | 2026-07-30 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 02a04183-3c63-31bf-83c9-d35c3039d94e | -7.54627 | -46.9066 | 2026-07-30 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 00dc26c8-684c-3e55-9caa-98a8be7b07ba | -3.4571 | -52.76812 | 2026-07-30 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 64c1a2fe-04a4-3b85-90c7-da2f0e7c3aa9 | -9.14123 | -49.66172 | 2026-07-30 04:57:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 03b0403d-96f1-3a22-b974-b93fba4c40f9 | -7.34553 | -45.8501 | 2026-07-30 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be197277-08f9-308f-9e83-4d7aec4058fd | -2.8998 | -48.01336 | 2026-07-30 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e56afc0-e7f2-3259-bf5e-2da9f15db5bd | -6.65103 | -59.11115 | 2026-07-30 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2c026953-8644-3472-a577-3717d5c0aa3b | -6.86553 | -46.00784 | 2026-07-30 04:57:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 109546a8-4ece-396b-8f24-90a2a9e4e4ef | -6.8651 | -46.01093 | 2026-07-30 04:57:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bbf63967-63c8-3e56-b8c0-d439b2125e6a | -7.33998 | -45.85249 | 2026-07-30 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7a5e889d-5a79-302c-bfbd-ffa2564e9172 | -9.22304 | -50.10226 | 2026-07-30 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 452f29b8-510e-35a1-809a-23bb2bbaffbc | -6.86048 | -46.00718 | 2026-07-30 04:57:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e733b0eb-bf48-3192-9374-f68595263c58 | -2.69936 | -54.26668 | 2026-07-30 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 854c6503-7014-3bd4-8b01-85d280d40e16 | -4.36998 | -47.76606 | 2026-07-30 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9a915489-7ad3-30e5-9041-1c64e95f8c07 | -3.17398 | -49.5212 | 2026-07-30 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70bd0c9c-9cde-30d0-9c31-9051121d0f3f | -7.34259 | -45.85309 | 2026-07-30 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5d318339-64d3-30fa-a340-28e5d8357a56 | -6.8565 | -56.534 | 2026-07-30 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92e49ed2-94d6-3465-9798-35058f387bc3 | -6.65585 | -59.10674 | 2026-07-30 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 2da7b1c4-6b44-3580-a069-8e971ea090ea | -5.28519 | -56.01923 | 2026-07-30 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 436b43d8-366b-39df-af0b-1629146865c4 | -7.38975 | -49.75085 | 2026-07-30 04:57:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 689e2cf4-d5ef-32a5-b128-b46b9d950f6d | -7.19883 | -45.50068 | 2026-07-30 04:57:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9be39ac-3133-3cc6-88c6-2e5a0f17fa6a | -5.23431 | -56.00735 | 2026-07-30 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c21b823d-997a-3e8c-b9cb-c811d4893c3f | -3.6821 | -47.6452 | 2026-07-30 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0ba6e7c1-550c-3131-9d9c-8b34cdb28bcd | -7.90944 | -48.28323 | 2026-07-30 04:57:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 341702cc-f4f3-31e2-b177-5b4e33671e07 | -9.4496 | -50.31133 | 2026-07-30 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a612469f-8dd5-3131-b8f6-56c68767408d | -8.07741 | -46.00764 | 2026-07-30 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4980ea41-a19d-3b93-9d6d-ba25c5f9c3dc | -8.08014 | -46.00758 | 2026-07-30 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 315baf99-fb70-3fef-b98c-076d1adcbc98 | -8.07502 | -46.00677 | 2026-07-30 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9da1aeb8-8a21-3525-b33d-8c3d90232c94 | -4.56057 | -48.02383 | 2026-07-30 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c76527e1-d13d-38da-876f-7df3c9bf830b | -7.24198 | -46.05591 | 2026-07-30 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f40abfaf-8826-3d41-a159-0a208a761f05 | -3.69069 | -47.64642 | 2026-07-30 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d938df16-3a09-35e3-bdc5-748921867185 | -2.72721 | -54.631 | 2026-07-30 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a728d744-d6c5-314a-a1a8-42fe8957c8b3 | -6.31102 | -43.65571 | 2026-07-30 04:57:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 75ca02fb-718f-30b1-b92d-cf68bd86ee2c | -9.55458 | -48.66837 | 2026-07-30 04:57:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 526d75eb-2d7c-3458-b7d4-bf639aa46f5e | -3.6784 | -47.6405 | 2026-07-30 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b4e0794-8989-3439-b54c-962cfde1b076 | -7.20408 | -45.50136 | 2026-07-30 04:57:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 208bc689-734d-3a70-8f02-a1509e8c0a98 | -4.90737 | -43.47188 | 2026-07-30 04:57:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7324f6b2-fec9-38e1-9a22-23f67f309a9e | -9.21983 | -50.09657 | 2026-07-30 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42813c1e-7666-3733-b51b-739ce1f4da31 | -8.18117 | -55.42776 | 2026-07-30 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25c02db7-c749-3144-95cc-42786359f95c | -8.80621 | -49.15487 | 2026-07-30 04:57:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 23d77c21-6452-3154-ac9f-ba8ae49a22a8 | -9.14547 | -46.37205 | 2026-07-30 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8168c9c3-3ff7-3570-a950-a253bc069c8f | -3.23752 | -47.92753 | 2026-07-30 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb6a6790-7673-36ed-9bb1-ef76b6642750 | -3.48133 | -47.68789 | 2026-07-30 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54cf3d10-3351-3116-bdee-e1db2a28ad0e | -6.65896 | -59.11249 | 2026-07-30 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 94d68a8a-190f-3e58-9706-151c12183594 | -6.33812 | -44.60739 | 2026-07-30 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e06ee496-0714-3de4-ae91-4902c6dab76f | -7.34773 | -45.85371 | 2026-07-30 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a555230b-033a-3975-81f8-e35de2a3cc8c | -6.33842 | -44.60897 | 2026-07-30 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9c1081c-3969-393d-9824-83978ab940c4 | -6.655 | -59.1118 | 2026-07-30 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 0bb01e5c-2519-3719-8d79-77667dcd79d4 | -5.75248 | -51.70383 | 2026-07-30 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dc6888e8-8763-3a94-a86e-d711657c1a6b | -5.74843 | -51.70714 | 2026-07-30 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5e4138bd-0a8b-38fc-86e0-845be320c76d | -9.61009 | -47.7614 | 2026-07-30 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7f5d9acb-37ab-3cec-81a9-7af7f3383d50 | -5.77171 | -45.78244 | 2026-07-30 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fde347da-0a37-3681-bb70-24e1f58f5042 | -5.47756 | -45.11747 | 2026-07-30 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6bfda43d-89b4-3e82-91e0-9cf23f2442b8 | -4.39173 | -47.75602 | 2026-07-30 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a3d56b1d-79fc-3cd5-be6c-153b801ac726 | -3.73892 | -53.7332 | 2026-07-30 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a44d6fe-51cd-3fd0-afe1-9d6d3ef502f6 | -3.68022 | -49.47968 | 2026-07-30 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8d6fbd42-aa3d-3e94-b203-ade73c004618 | -3.17223 | -48.13663 | 2026-07-30 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 83750bb6-b77f-3d52-9b7f-f6b896b2e4bc | -7.91003 | -48.27901 | 2026-07-30 04:57:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3a5a2d47-12ed-3f2a-a515-eb9b049b8898 | -3.67641 | -49.47909 | 2026-07-30 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5e3e1370-abd1-3b9f-88aa-30c9b7bffc63 | -4.35743 | -48.64977 | 2026-07-30 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cca4619e-1ef3-3575-a519-26dc5f8a9b8c | -8.44541 | -51.50309 | 2026-07-30 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c3a4e50-19e8-39ea-ba72-478615fa020b | -3.68269 | -47.64117 | 2026-07-30 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README10.md)
