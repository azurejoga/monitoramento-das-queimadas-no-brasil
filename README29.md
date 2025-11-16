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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40882ce2-a766-3ccc-a1e0-6e06b63d7ff2 | -4.41279 | -43.41122 | 2025-11-16 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 19f18d54-db16-3272-84ad-b8e8f9d6bd7d | -4.42235 | -45.55393 | 2025-11-16 04:06:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d826bd4-11ba-3043-96dd-c2e4797f3b9a | -4.41057 | -43.403 | 2025-11-16 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9407a454-7c39-3413-8e4a-4d8fd27d83c1 | -3.99951 | -44.26373 | 2025-11-16 04:06:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 333f8614-195f-3981-a9aa-bdeb54756d60 | -4.74918 | -46.38284 | 2025-11-16 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd66468a-e859-3e58-8abb-0c2a7b295e39 | -2.79466 | -52.97084 | 2025-11-16 04:06:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b62428c-3955-330e-97f4-5523cd586de8 | -4.89302 | -45.0221 | 2025-11-16 04:06:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d780d5c9-9836-3876-a95d-87ab00652d77 | -4.62558 | -47.41252 | 2025-11-16 04:06:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8032dbf8-dec5-3bf2-8d72-f2f7edb60cf3 | -4.69837 | -46.31116 | 2025-11-16 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7bd65342-55b9-3fdc-9317-3d21e6227185 | -2.58781 | -46.93609 | 2025-11-16 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c354971-1855-3f70-ab32-635b8c4c92d9 | -1.16927 | -49.20977 | 2025-11-16 04:06:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 320180b6-bdda-311d-ae9a-b70285cd4f7a | -3.30549 | -45.79766 | 2025-11-16 04:06:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0412a80c-eb2c-3e64-b440-7b7b2a6c6037 | -4.31875 | -46.54559 | 2025-11-16 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f1101b2-dbc8-3177-afaa-d8ec623b47ed | -4.73005 | -47.16053 | 2025-11-16 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6271b0a9-ba02-3d38-826c-de561fef4b1f | -2.72029 | -45.0485 | 2025-11-16 04:06:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12b9a1a2-daa8-306c-9049-673061ad997c | -2.73162 | -49.5619 | 2025-11-16 04:06:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d011861e-6ce1-3960-be77-5bf334334273 | -3.72276 | -49.53653 | 2025-11-16 04:06:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7883da64-13f1-3930-99ba-a37c3a6d6551 | -5.42287 | -42.56745 | 2025-11-16 04:06:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cc798eb6-90f7-38af-a86e-cddb10584d50 | -3.79457 | -43.37612 | 2025-11-16 04:06:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25f4b932-686f-3e07-9e45-fee351ca1146 | -3.94086 | -40.47 | 2025-11-16 04:06:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| efc97a09-2225-3efb-8ff9-c97e5b72627d | -2.58809 | -51.8334 | 2025-11-16 04:06:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2ecb963b-4946-3732-b2f3-e6d9016a2ec6 | -2.54613 | -47.45777 | 2025-11-16 04:06:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c89a4f7-c511-38dc-beae-076d451accbc | -4.74714 | -37.88417 | 2025-11-16 04:06:00 | NOAA-20 | ITAIÇABA | CEARÁ | Brasil | 2306207 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 47040b35-2541-31e0-ada3-c64b8d31d68a | -3.05759 | -44.74261 | 2025-11-16 04:06:00 | NOAA-20 | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8fea4493-3acb-39cc-9e4b-0c77044b87fe | -4.14528 | -46.34874 | 2025-11-16 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c2c488e-f708-3a6b-88ac-27ae2e4147bb | -5.52303 | -40.99489 | 2025-11-16 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 480d9970-73a2-30e0-842b-3110a3ed64ba | -4.43324 | -43.39486 | 2025-11-16 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f558c45-f375-32e4-9dc5-40774f207de0 | -5.43399 | -42.58381 | 2025-11-16 04:06:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d38d5700-ca40-3144-8136-dfd60da8d280 | -3.06136 | -44.74322 | 2025-11-16 04:06:00 | NOAA-20 | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05a41277-c91a-3438-ad50-8c25a4ca945b | -5.51918 | -40.99783 | 2025-11-16 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| aa84be9f-b22c-3673-9fb0-3cd71802d85b | -5.32242 | -35.93022 | 2025-11-16 04:06:00 | NOAA-20 | PARAZINHO | RIO GRANDE DO NORTE | Brasil | 2408805 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c80564f2-d3d7-39fc-8f32-75ceeb2b0811 | -2.93356 | -49.35147 | 2025-11-16 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e31168f3-6902-336f-ba65-1cfe83e396eb | -3.33679 | -45.28576 | 2025-11-16 04:06:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d58de926-31d5-30f2-8d82-cd579e1b6c94 | -3.35647 | -46.86866 | 2025-11-16 04:06:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18db5c28-c155-325a-bed7-943ef6e127b2 | -2.78849 | -43.34587 | 2025-11-16 04:06:00 | NOAA-20 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2cbaa5c0-a902-3aea-8606-b937114f7b37 | -5.53658 | -41.77105 | 2025-11-16 04:06:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0937969e-bbd8-3114-8dbe-84ef1a2325ff | -4.62629 | -47.40834 | 2025-11-16 04:06:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d2366a2d-5722-3a2e-ab7b-01b89b548d03 | -4.03029 | -42.0754 | 2025-11-16 04:06:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 082f9467-010d-339e-91c6-57ac1730fea7 | -4.42729 | -43.40961 | 2025-11-16 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b3ab431e-fe48-35f0-b27f-bcf7989898f4 | -3.38521 | -47.19038 | 2025-11-16 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84023930-5b1b-3f4a-9446-49975e6ab415 | -5.48116 | -40.9813 | 2025-11-16 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8135e1a8-f23b-3b4c-8caa-db87de2ae7cc | -2.88682 | -53.28558 | 2025-11-16 04:06:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 6a48643a-0ac3-3c78-8f71-164a563afddc | -3.99679 | -44.28064 | 2025-11-16 04:06:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55b126bc-96e6-36db-aaeb-f2690bd99339 | -4.44597 | -41.78979 | 2025-11-16 04:06:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 67cda682-964e-3bb6-819d-c70e11c583eb | -3.22226 | -49.22554 | 2025-11-16 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| de6def3f-250e-3958-b300-00ed360d5207 | -3.46175 | -50.12411 | 2025-11-16 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a1c4581-3414-33aa-99d4-5574dc31b108 | -5.28258 | -44.30224 | 2025-11-16 04:06:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bed6eea5-36de-3d67-9382-43f8af038219 | -3.93178 | -47.05292 | 2025-11-16 04:06:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 420b8b8a-7bfa-333c-9e4d-49ceb8527d0c | -5.20329 | -43.47136 | 2025-11-16 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 46024ef7-5934-352d-afcc-dcab010c4e74 | -5.85283 | -39.42598 | 2025-11-16 04:06:00 | NOAA-20 | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| ac11b803-9ddd-32e2-8a5e-7e9c8c2bbf2d | -4.42621 | -45.5547 | 2025-11-16 04:06:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| af0ed1f7-eadd-336f-ae24-695c3c67f2d8 | -3.99816 | -44.27217 | 2025-11-16 04:06:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ccb40e79-dec7-3807-ae00-cc3adde06140 | -4.6875 | -46.52708 | 2025-11-16 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 609ecb37-a63f-3ac1-9c92-bf981082a6a0 | -5.53603 | -41.77451 | 2025-11-16 04:06:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0ef04d8b-2bcf-353f-b0ae-a854917f9494 | -4.20322 | -48.56356 | 2025-11-16 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb41e346-6bdc-3932-96bc-b57fe2c9f807 | -3.22097 | -49.22387 | 2025-11-16 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d28c90a1-be5d-3842-aa6b-ea4ad5b61906 | -2.54568 | -47.45549 | 2025-11-16 04:06:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62af50ca-dfcf-393b-ba92-1d5331b2a6f1 | -3.86794 | -46.05927 | 2025-11-16 04:06:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 80d17bdf-d5d0-36f6-a8f3-210d32384d25 | -5.54191 | -42.69589 | 2025-11-16 04:06:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 47e7a5c9-b520-3cee-84ae-c590f81891f2 | -3.18303 | -46.60345 | 2025-11-16 04:06:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3925dade-13af-3f78-975b-b8c7cdb61ee3 | -4.67809 | -46.73825 | 2025-11-16 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8ad3f724-cfc9-33ae-8155-5042a13b11ea | -3.8543 | -39.83232 | 2025-11-16 04:06:00 | NOAA-20 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c15d1e3b-9c88-3a13-9795-6bb2b123a21a | -4.0264 | -42.07838 | 2025-11-16 04:06:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6fac2e79-c3d1-3e50-942a-0ddb98158292 | -4.75235 | -43.35083 | 2025-11-16 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 12652533-4e93-3546-8d50-8b79f51afdf4 | -5.18118 | -45.04083 | 2025-11-16 04:06:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8c4d003-207d-3a12-a2d3-0d4ae7d9fcce | -3.29984 | -53.85411 | 2025-11-16 04:06:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d77040b9-9aa7-397e-9810-a73136098872 | -5.51638 | -40.97265 | 2025-11-16 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 171fff85-c3fb-39ce-acd5-351985305deb | -1.06047 | -48.85154 | 2025-11-16 04:06:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a61c815a-b35f-3b8e-974b-35348f2f719d | -1.98909 | -47.35232 | 2025-11-16 04:06:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 16111221-a0d4-37bf-a5ba-80a17ad861ea | -4.39673 | -49.78433 | 2025-11-16 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad7cc7ae-a68a-37f9-b081-dbd8e1e3ea7e | -5.51366 | -40.9899 | 2025-11-16 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3507587e-615a-3a51-9b5f-442606f2fc6a | -4.73233 | -46.38346 | 2025-11-16 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 02b64bf4-b0da-38d5-971f-9cb879d106e3 | -4.96452 | -42.60475 | 2025-11-16 04:06:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01223f1e-1662-3b7d-82cc-5b02228b02b3 | -4.59431 | -40.24538 | 2025-11-16 04:06:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bec62187-f653-3cb0-8b87-38684062f15a | -4.42097 | -43.40471 | 2025-11-16 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6eaeb604-2d46-3bcb-a134-ed6b90800008 | -3.59736 | -52.05339 | 2025-11-16 04:06:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bc62e7e0-76dc-3c01-9b25-588ed18c7307 | -5.52941 | -41.77346 | 2025-11-16 04:06:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| da9fdeb4-886f-31cb-9420-e9e6929ff4e0 | -3.85349 | -40.76695 | 2025-11-16 04:06:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 7ab1d6f0-8649-3109-ba64-6b29ac590c19 | -4.10543 | -46.06115 | 2025-11-16 04:06:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5946dae7-1133-389e-add2-c04624c3da97 | -3.7159 | -42.06511 | 2025-11-16 04:06:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 75a7cd07-c343-3b0b-ba25-3872e351c39d | -4.73698 | -46.38065 | 2025-11-16 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ca21798e-bef5-3ad7-9870-eda23e279a44 | -1.99364 | -47.35305 | 2025-11-16 04:06:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 72d1e228-b0ea-34d5-8d4e-a9014cf83c1e | -4.74454 | -46.38562 | 2025-11-16 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a674d8d1-8c78-379b-b2cd-de20c50126b9 | -2.14078 | -45.34571 | 2025-11-16 04:06:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 23c2156d-3112-30a0-8a72-1c5b92f77e26 | -2.71459 | -47.40315 | 2025-11-16 04:06:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b5ac3b90-0dfa-3ecf-9ba1-ec0582fa3d6c | -5.4817 | -40.97785 | 2025-11-16 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 29dfe465-75a7-3b69-a417-89177d3d54bf | -4.42382 | -43.40907 | 2025-11-16 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| eaba65ee-65f2-330d-bb3c-074082fc5a20 | -2.5155 | -47.8128 | 2025-11-16 04:06:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| a5e6935a-6e4b-33cd-a491-9e3192638165 | -2.58299 | -51.83112 | 2025-11-16 04:06:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f2771a15-82ba-3a67-9265-59f59da59051 | -5.32556 | -43.03633 | 2025-11-16 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ea3b0bea-f033-3f89-8f34-39f39ca01537 | -5.49003 | -41.37804 | 2025-11-16 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7ff2c8f5-7b0f-3300-b129-d8393e893ff5 | -4.81548 | -45.50558 | 2025-11-16 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 388c27bd-31bc-3c74-a129-e090496ad255 | -5.10984 | -40.72802 | 2025-11-16 04:06:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0391d9d6-fe91-371f-95ff-61e1e643c7fd | -3.85541 | -39.82527 | 2025-11-16 04:06:00 | NOAA-20 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| be610ade-5051-37f8-8bf9-d4c490bf57a2 | -5.429 | -42.57209 | 2025-11-16 04:06:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a6188639-f453-383d-874d-4e847dcda8bb | -3.45308 | -51.02542 | 2025-11-16 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f8898a1-6a51-3b01-8dce-6c0fb0df489e | -5.28324 | -44.29818 | 2025-11-16 04:06:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 90984d72-d078-348f-9d90-d6f82b20996a | -1.06096 | -48.8485 | 2025-11-16 04:06:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b2fe8fc3-fb29-3a92-98e1-94b6df66c086 | -4.94145 | -44.53304 | 2025-11-16 04:06:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 78acfbee-b342-3a6c-abbc-2aab76ca1fde | -2.48359 | -44.18705 | 2025-11-16 04:06:00 | NOAA-20 | SÃO JOSÉ DE RIBAMAR | MARANHÃO | Brasil | 2111201 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README30.md)
