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

## Dados Diários - Página 181

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c31675e-a2ab-34a7-93c6-9b41e04556cf | -2.5516 | -45.3162 | 2026-08-28 20:20:00 | GOES-19 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 119.4 |
| e1cf7a14-7fb3-3943-bffd-3f7bd4c03183 | -6.7652 | -63.054 | 2026-08-28 20:20:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 120.6 |
| ccfd83a4-7dd9-35ee-9702-c43b5f03693d | -11.7357 | -54.5227 | 2026-08-28 20:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 8d390c32-90cd-343a-bba8-99e057bec298 | -9.7267 | -47.7606 | 2026-08-28 20:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 116f2a2d-2e91-3f61-bd09-e4dcf0edfc0c | -9.971 | -53.9214 | 2026-08-28 20:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| e2348c33-1b99-3fc9-ad3b-8aeb84a21033 | -5.1227 | -44.9682 | 2026-08-28 20:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 33875ed1-e207-3381-b2b8-142cadb8909a | -8.6013 | -70.2009 | 2026-08-28 20:20:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 39e85268-af21-304c-87db-f828819070b9 | -14.1982 | -48.7451 | 2026-08-28 20:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 0803721b-8645-30d3-bc4a-49c266650bb9 | -8.8219 | -70.638 | 2026-08-28 20:20:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 5ac09736-4746-33b6-811f-bb942c0dcbc7 | -12.7797 | -44.2576 | 2026-08-28 20:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 105.0 |
| c2e54824-b61d-326b-9cd4-05d62adf2574 | -2.533 | -45.3168 | 2026-08-28 20:20:00 | GOES-19 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 4aa9a554-3802-3e8b-9659-8e06534f0e2b | -7.5662 | -61.3049 | 2026-08-28 20:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 299.5 |
| 0efcfe25-dad4-31ed-a5a2-1f5c74bc277d | -6.7833 | -59.4208 | 2026-08-28 20:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| e33ca25f-9de5-3f75-bb02-d9c065a7edbd | -5.1414 | -44.967 | 2026-08-28 20:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 257.4 |
| 6647d643-23a7-3bcc-ab98-39a9fb84bef4 | -11.6975 | -54.5467 | 2026-08-28 20:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 40b2e944-9443-38b1-b31b-9ecea5d97d0e | -7.5477 | -61.3247 | 2026-08-28 20:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 49d1f931-c39a-30ab-8a7a-88b19bbeba14 | -3.8349 | -52.4012 | 2026-08-28 20:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 76d1ca11-2c3c-3dad-a6ec-cf3a56c5c5cf | -14.6224 | -50.8901 | 2026-08-28 20:20:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 103.4 |
| eb7acf1d-86cb-34fa-949e-1c58c37c72d3 | -10.4502 | -46.1826 | 2026-08-28 20:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 112.9 |
| e25132a2-8cf5-39de-a349-aabe55331311 | -6.1657 | -57.7793 | 2026-08-28 20:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 105.4 |
| ad0bc023-133b-35a2-aff0-35961735668c | -7.5516 | -70.0146 | 2026-08-28 20:20:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 91.9 |
| c2e50a27-45af-3105-8b66-381a3f35566f | -3.8348 | -52.4217 | 2026-08-28 20:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 9dbf22dc-1672-3eb5-bb9b-96f1bf4f7029 | -17.0869 | -47.1834 | 2026-08-28 20:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 4748a84c-6695-378e-8c0f-d66b10c8e950 | -9.02 | -57.5377 | 2026-08-28 20:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| e1ce61ce-fa14-3b6c-859f-4ff44f108f83 | 1.2055 | -51.0182 | 2026-08-28 20:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 52b7beac-5148-3389-8568-defb40480a20 | -6.7504 | -58.7268 | 2026-08-28 20:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 2ac5316a-7ad4-3986-84db-704534a37d8d | -9.1239 | -61.0078 | 2026-08-28 20:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 44f1438f-f960-3a12-ac55-56a79c6eae04 | -14.1594 | -53.1429 | 2026-08-28 20:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 80f04ebb-846a-3484-b762-905f830bfd56 | -6.7248 | -59.9998 | 2026-08-28 20:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 82.9 |
| f2e9bae3-763e-3919-8173-35b1c8a8cb8a | -3.6216 | -60.528 | 2026-08-28 20:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 09204825-c935-3e7e-ba86-121bfb32190c | -5.8895 | -57.7513 | 2026-08-28 20:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 243.0 |
| 4dc9b5f7-148a-3cb2-9b74-f360b7a9c0c1 | -14.9386 | -56.3216 | 2026-08-28 20:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 167.3 |
| 48a58e8e-45c8-3a81-9442-a42cd22a860f | -6.0389 | -44.927 | 2026-08-28 20:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 2fce827c-1b5a-3c5f-8871-443903874857 | -5.6512 | -44.339 | 2026-08-28 20:30:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| a7e130b8-bf48-34e8-8b7e-3b731fdaf181 | -2.533 | -45.3168 | 2026-08-28 20:30:00 | GOES-19 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 94b8a3be-410e-30a9-8ab5-b237bfd0d6ed | -11.7167 | -54.5244 | 2026-08-28 20:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 208.2 |
| 77dbf911-ce52-3401-8d6f-b20de8ca7343 | -6.7432 | -60.0182 | 2026-08-28 20:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 04cd0b43-f128-30b9-947e-306f616f4c90 | -8.0115 | -47.9943 | 2026-08-28 20:30:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 156.5 |
| a0fad57d-db7a-35d0-9dd7-5110f11edc54 | -6.0004 | -57.6884 | 2026-08-28 20:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 103.4 |
| d684626b-950b-3014-9395-d2694f67da77 | -9.0198 | -57.5574 | 2026-08-28 20:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 136.9 |
| 9f555187-e899-34f3-b9bd-89047ac95ac5 | -6.1657 | -57.7793 | 2026-08-28 20:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 121.3 |
| 030ea2bb-662c-326c-b655-500cc80d4f0a | -11.0244 | -49.6872 | 2026-08-28 20:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 2101805b-62da-361c-a9ec-943b69cab037 | -14.1784 | -48.7703 | 2026-08-28 20:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 125.9 |
| cef4d74b-883b-36d5-aff5-c39fe66ff070 | -6.949 | -59.4719 | 2026-08-28 20:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 4b41c1ca-8997-353a-8d74-985289f54805 | -14.2027 | -52.8432 | 2026-08-28 20:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 4117a676-6e10-34b9-add8-3ce1dbf2ed5e | -6.3467 | -44.0782 | 2026-08-28 20:30:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 256.8 |
| bc55c93d-5585-3f36-9ca9-8b4e176c21ce | -14.1978 | -48.7673 | 2026-08-28 20:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 64389c00-0800-3c04-8ead-011202ed33f7 | -7.4919 | -61.403 | 2026-08-28 20:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 108.4 |
| 3c7ae391-9f5b-3cf8-88b5-231b62a7e022 | -14.1788 | -48.7481 | 2026-08-28 20:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 95.0 |
| b444f65b-b2e9-3c3c-9e9d-c8fd23022522 | -6.3279 | -44.0797 | 2026-08-28 20:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 858d156d-efe4-3705-981f-b5ac597f8951 | -17.9875 | -50.1948 | 2026-08-28 20:30:00 | GOES-19 | PORTEIRÃO | GOIÁS | Brasil | 5218052 | 52 | 33 | nan | nan | nan | Cerrado | 92.3 |
| b8bd6db9-36bb-3d25-925c-63f7793bd916 | -6.4997 | -43.7878 | 2026-08-28 20:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 1e23b108-a533-32e5-ba97-b5d938b98e44 | -5.1412 | -44.9897 | 2026-08-28 20:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 6a983d1f-5b67-343d-ba18-7d7fc1a42772 | -5.9079 | -57.7506 | 2026-08-28 20:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 118.8 |
| 69f8badf-0001-3812-af1e-e4b87d1ef10b | -8.6012 | -70.2192 | 2026-08-28 20:30:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 134.4 |
| 2ff344ae-ef1b-36f3-8d01-5fc7ea1d7c78 | -11.1916 | -51.2708 | 2026-08-28 20:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 177.7 |
| 1e6c19c2-ad7c-3f58-8805-17a531d6b1db | -5.871 | -57.7715 | 2026-08-28 20:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 48aab9e8-34a6-317e-8ada-e30386d20de5 | -11.1919 | -51.2496 | 2026-08-28 20:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.3 |
| d6b2cefc-1276-32c6-bdb6-ccaccb95bff7 | -8.1617 | -64.0047 | 2026-08-28 20:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 94.0 |
| fe0c6486-5f7a-353a-a3ba-3afb5411176d | -7.5103 | -61.4022 | 2026-08-28 20:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 86cb6875-dc75-32e3-a63f-29bfc83a6198 | -13.5991 | -45.772 | 2026-08-28 20:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 08385d3f-49da-3bf7-81db-ce9f4ed23e2d | -8.7757 | -50.083 | 2026-08-28 20:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| bf11066a-0d5e-3335-a479-82d6a91550d7 | -9.9288 | -60.4277 | 2026-08-28 20:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 298.4 |
| bc6b3565-78bc-3e34-aeae-a772dcc703aa | -7.5516 | -70.0146 | 2026-08-28 20:30:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 068d5bfb-c2d7-3221-a411-6b1dc5043019 | -9.1523 | -49.9853 | 2026-08-28 20:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| f1c6f7c3-76b8-37b7-a0f4-e73e4683291b | -5.9819 | -57.6892 | 2026-08-28 20:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| b8a66037-4be7-3ee7-b382-5b114477e817 | -9.1424 | -61.026 | 2026-08-28 20:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| dd78c900-ad22-3da0-8dcf-92bd32c8d381 | -7.4734 | -61.4037 | 2026-08-28 20:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 5d400fe2-8657-3d1b-b9bf-632d04a39e4b | -15.577 | -56.2916 | 2026-08-28 20:30:00 | GOES-19 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 2dcccda9-e6c9-34aa-94d4-a4a3ad6b5844 | -12.3799 | -50.6038 | 2026-08-28 20:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 170.5 |
| 61a5f936-fb4d-3b70-a0c9-6c04a29edd87 | -11.2317 | -53.9958 | 2026-08-28 20:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 5387c45d-b9ad-35fc-9325-482a69440724 | -6.7653 | -63.0352 | 2026-08-28 20:30:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 2637c0c9-e275-3cc6-adab-aeb40abdb481 | -5.8894 | -57.7708 | 2026-08-28 20:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 266.5 |
| eb986b20-124d-3581-933a-244a83323d37 | -10.5711 | -59.6149 | 2026-08-28 20:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 95.7 |
| d5e8805d-e3a7-3fc2-b984-2d972b7f38d8 | -7.4952 | -55.3062 | 2026-08-28 20:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 5ceee895-340a-32db-a525-444c440fedeb | -10.7596 | -54.0384 | 2026-08-28 20:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 122.8 |
| 677ce787-fcbb-3cbc-9fcd-d51e093acec4 | -14.9015 | -52.6055 | 2026-08-28 20:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 43b542a1-92ee-32cf-8b0e-fccceb3a8170 | -14.4057 | -50.0537 | 2026-08-28 20:30:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 125.7 |
| aa3fd93f-10a8-30a4-8e28-5420f11440b8 | -9.1711 | -49.9835 | 2026-08-28 20:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| c0f8932e-8293-3a68-8b21-ec880b84ce9a | -5.2634 | -43.7444 | 2026-08-28 20:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 5bf3fb57-ec47-3b3b-b090-974b9fa3e29b | -12.3608 | -50.6061 | 2026-08-28 20:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 1ab7101d-694b-3cb2-bcf8-4bed193d64b2 | -11.7165 | -54.5449 | 2026-08-28 20:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 245.9 |
| cb7c3eb4-22df-35e9-b1f0-4402a9137b2c | -5.251 | -45.2768 | 2026-08-28 20:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 0e42edcf-7b4d-33ad-adae-372fd6a24a27 | -14.6224 | -50.8901 | 2026-08-28 20:30:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 084c8e00-4273-3980-8d94-1962fbcf408e | -17.988 | -50.1725 | 2026-08-28 20:30:00 | GOES-19 | PORTEIRÃO | GOIÁS | Brasil | 5218052 | 52 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 4cd7d8a1-fbb7-3d8b-90dd-53adbbed8b5c | -8.6197 | -70.2189 | 2026-08-28 20:30:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 75.5 |
| b8abfe92-c4c9-3e7b-b390-e009e975a0b5 | -8.0113 | -48.0161 | 2026-08-28 20:30:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 168.0 |
| 8e250fc6-4768-3562-9e43-4be3591dbf9a | -21.5152 | -55.3985 | 2026-08-28 20:30:00 | GOES-19 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 67.0 |
| e2dec87a-ae59-315b-8782-d9c3fa6b732f | -9.7267 | -47.7606 | 2026-08-28 20:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| dcecc496-80d2-3ff3-a04d-0a70fedd1665 | -6.1656 | -57.7988 | 2026-08-28 20:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 27802b3f-a2c8-36fc-8d68-340122c0a0a1 | -5.8711 | -57.752 | 2026-08-28 20:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 365f48cd-297d-34bb-a6c6-ddfb28d077d1 | -9.1978 | -61.0809 | 2026-08-28 20:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| a5c6b7a4-de83-3242-a0af-0c2b1ff651ba | -14.3565 | -51.7208 | 2026-08-28 20:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 95.3 |
| de8ae2da-1b07-3717-9db4-67c9cb1896d1 | -8.8219 | -70.638 | 2026-08-28 20:30:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 8afd666b-886a-32df-a2a0-87524162e7f6 | -8.5783 | -54.7768 | 2026-08-28 20:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| be9644f1-afe7-3373-a644-30799ff5ea27 | -20.9207 | -57.5723 | 2026-08-28 20:30:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 80.8 |
| 40df91be-fa2f-3879-b72b-6ccaa6f79129 | -7.5139 | -55.2851 | 2026-08-28 20:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 6b1b7930-b2c1-3487-92c1-11a2f4426f66 | -4.5694 | -44.0657 | 2026-08-28 20:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 280.4 |
| fc63188f-a557-32ee-8303-cc5e7ef0a715 | -6.9336 | -58.9514 | 2026-08-28 20:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 108.4 |
| 3bef2ec6-8e8d-371f-881f-69df9d3e1fe7 | -7.4953 | -55.2862 | 2026-08-28 20:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 126.7 |


[Clique aqui para ver as próximas entradas](README182.md)
