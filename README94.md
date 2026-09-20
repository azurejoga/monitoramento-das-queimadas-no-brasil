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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d502fbe-b0cb-3a2a-83c7-876c73f95dea | -11.20209 | -55.03625 | 2026-09-20 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5e96cef2-e9fe-3231-b29a-079121db4ce7 | -6.30009 | -47.61354 | 2026-09-20 05:25:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a35ea52-ac66-3f33-96c9-2fbfc735f9dd | -3.48466 | -59.59423 | 2026-09-20 05:25:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7951d1e-0d3c-36a1-903a-3f07ab6b99d3 | -5.74722 | -57.60154 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 083f8012-951d-388d-ba5b-da695496c2a9 | -10.86359 | -57.14722 | 2026-09-20 05:25:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2ac4685c-d0b5-32e8-b00c-90671bb003f4 | -3.68782 | -59.2286 | 2026-09-20 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c9c1851-d817-30fa-9855-4a4e3046c4d7 | -3.69266 | -60.59555 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2c36d869-8a2d-39fb-bd64-a93da20b6def | -3.94835 | -59.34703 | 2026-09-20 05:25:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67f5fa13-bc0a-3913-8da8-5623bc819c38 | -15.87848 | -49.90864 | 2026-09-20 05:25:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3886357d-8211-31cc-bae0-0b99e253f38b | -3.48573 | -59.58733 | 2026-09-20 05:25:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d77c5ce0-0f57-3826-8f9d-15048aa4625f | -5.85877 | -53.5533 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2bd3028-1f12-3462-9ffb-f67477ce5e46 | -3.68881 | -60.59849 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1fc26287-7077-31ef-9af8-e1f78af1553d | -5.84235 | -53.53593 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 263fd486-d2ab-3317-ab11-d5ac62ebcff8 | -4.28774 | -56.26471 | 2026-09-20 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0be50a76-a668-3278-ba1d-f3d1ee9e0c15 | -7.52477 | -47.33917 | 2026-09-20 05:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3d0b12be-d850-3961-837c-f25eb5cd503a | -3.69867 | -60.57881 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 997d3f24-931c-39f2-89ac-fe8d6f14a53d | -7.11029 | -48.41895 | 2026-09-20 05:25:00 | NOAA-21 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ed8c1576-19ae-3983-808f-c86e87a5239b | -12.47767 | -50.05161 | 2026-09-20 05:25:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| df1500fe-18dd-3eb8-bd2f-d3076ea72ea9 | -7.11687 | -48.41999 | 2026-09-20 05:25:00 | NOAA-21 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2af7cf08-3841-3305-a7ff-5c15098f6ea8 | -13.89371 | -48.58648 | 2026-09-20 05:25:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fcb0d893-a966-3400-8fa1-e62293a784f0 | -11.12935 | -54.01533 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 35f6fb8c-8b38-364d-9298-8538a07bdf0e | -3.69278 | -60.63798 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d7f86a0-43f6-3ebb-bb70-611ac91c8697 | -6.15133 | -57.75342 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 22a0ca39-7ebc-3979-9824-ce1d63698a09 | -10.8841 | -53.98542 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fa568575-33e2-3d34-84c6-4429761e3569 | -3.69717 | -60.63159 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b6f2cfe-4c6a-3891-bd28-0e3950517625 | -5.8705 | -51.56073 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2c73e73-a3aa-3c4f-9e6b-b9934ed793ee | -5.84492 | -53.55118 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d131524d-9fef-3ed1-8bd0-606fdca4d984 | -10.86435 | -56.17986 | 2026-09-20 05:25:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1e51350e-11be-3bf3-9650-3bd93f8bbb8f | -5.84507 | -53.51664 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eafe1c02-ca12-31d9-a620-6208ff7ed4ab | -3.52893 | -59.94287 | 2026-09-20 05:25:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da376d9a-65a3-3413-a1a6-e6202615ef89 | -5.83977 | -53.52077 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c67fb976-e33b-377a-b196-f4295401f582 | -11.22341 | -54.07932 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 67a97b87-8386-3dcc-ab6a-23efac88b3c3 | -5.78217 | -57.58027 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 63bf77ea-a36e-3968-8852-03cb3d7a01a2 | -5.93291 | -53.52265 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b187d14-e494-3879-a482-90f1ac6230a8 | -16.89242 | -50.58626 | 2026-09-20 05:25:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 83d7f550-ca5b-30e2-9d7f-b9ac42cd735c | -14.91844 | -49.91307 | 2026-09-20 05:25:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 01357975-2d8b-341f-8abb-d9955c4bd23b | -3.48135 | -59.59372 | 2026-09-20 05:25:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ce88fe1-d78e-3a4f-8a53-2a9c643d6480 | -12.87957 | -51.00348 | 2026-09-20 05:25:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5970462f-76d0-30de-97aa-a145b1382806 | -11.12693 | -54.02764 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 3da57952-9d3c-3811-9aa1-ba4c102f1e7c | -3.69921 | -60.57536 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbae4207-a130-3509-b82e-7b094324d7a2 | -13.73436 | -48.7915 | 2026-09-20 05:25:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0bab4576-e745-3112-8de9-6de879dc6748 | -5.83962 | -53.55536 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 99713e29-b24c-39f9-af61-a58c60cbbdd5 | -11.1386 | -54.01313 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 61c4ad54-c1de-3ba9-9ab2-885b473455ea | -6.08062 | -56.47406 | 2026-09-20 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f4bb2808-0006-3228-91d0-826ab447680f | -11.13309 | -54.01773 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4ffcea51-30da-3310-a55d-65249673f1cb | -6.17178 | -57.71494 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 50d7a8a7-ed38-394b-a220-398f6abdf916 | -3.64133 | -58.86844 | 2026-09-20 05:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 78c5930e-5fdf-3ff0-989e-19ee7aadd8cc | -11.23305 | -54.08067 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 51e05265-0180-31a7-9173-dbd3bfb56d0e | -12.7726 | -52.8599 | 2026-09-20 05:25:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d2bea4b5-ef7b-319f-9661-953cfa5d3b4f | -11.68667 | -54.45328 | 2026-09-20 05:25:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 03a835e7-44cd-3747-9f41-234b5ccb6320 | -10.86751 | -57.14769 | 2026-09-20 05:25:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c87a7fc-fa70-3e55-bb41-43bfa14e78e8 | -11.94628 | -55.92092 | 2026-09-20 05:25:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5ac43d10-65b1-3135-83c4-a935ef6e3dce | -6.61965 | -50.06382 | 2026-09-20 05:25:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7925d447-31c0-382a-966c-16852a3b1405 | -5.86905 | -51.57087 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b6395523-62f1-351f-9ef8-f0a8d77f5c0e | -11.98448 | -52.47781 | 2026-09-20 05:25:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2fe059f6-694f-319d-a9bb-baf4322baab0 | -3.68935 | -60.59504 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3d0aeeb1-341f-34d9-89b9-d416ec38727f | -3.69975 | -60.57191 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f598df3-3c79-3ee0-936f-c9d3bdd6c033 | -10.8602 | -56.17922 | 2026-09-20 05:25:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 40d9471d-0a96-3d46-86fc-289c67533793 | -11.12452 | -54.01466 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 73bed76d-4df2-3345-b059-6df2b073c317 | -13.88202 | -48.58266 | 2026-09-20 05:25:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 32781637-856c-332a-9bbf-18cbd6171aed | -10.96455 | -57.19897 | 2026-09-20 05:25:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c28745ec-d5ef-38e3-a772-e376c84ac145 | -3.60422 | -59.06485 | 2026-09-20 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37c13dfb-be2c-389f-a3b2-065e71f63d90 | -3.68718 | -60.60884 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e915f761-1589-3f0c-a265-fb17f7696f6c | -10.87626 | -54.08197 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 1de8785b-c68b-3ea8-a747-8c62bd1be976 | -5.28019 | -49.34516 | 2026-09-20 05:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b98b4473-b686-3ec5-9eeb-49695c166c22 | -3.23256 | -61.20892 | 2026-09-20 05:25:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ffcec264-3fdf-35d3-9f48-26dcd19dd257 | -5.73453 | -51.76171 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a00bd13-bd68-3956-8042-071131c87504 | -11.21704 | -54.08478 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e63f1601-2213-37de-a168-440a63be35ad | -10.8711 | -56.22369 | 2026-09-20 05:25:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| db656882-a218-397f-b462-45169c3a4f7c | -4.49717 | -54.97979 | 2026-09-20 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3a528e99-e15d-3397-a3a5-cbff80aa98ac | -3.45918 | -60.56635 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2fa6108-7718-315f-bb89-a4ad2bba380d | -4.22067 | -59.41079 | 2026-09-20 05:25:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5cad3dd9-43b7-3cc8-97b9-668bc00d402f | -3.60513 | -59.01463 | 2026-09-20 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8efffee-4449-3cfa-930d-8e42899aaa4c | -6.15999 | -57.69644 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c906640f-3e50-3efd-998d-87f4e9b9e846 | -3.69699 | -60.56796 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5323e074-18cd-33bd-b9e7-b8787a2ddd10 | -6.28924 | -56.03591 | 2026-09-20 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f612d209-7c8a-3b19-bb72-4160fa45c261 | -6.39326 | -54.88616 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04b85267-ed05-3097-ae62-385567958bbb | -12.32586 | -50.71122 | 2026-09-20 05:25:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 92cb673b-a2a0-3a4c-8d4d-96e8e1a47971 | -3.79976 | -59.71065 | 2026-09-20 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0dc776f7-ed07-3e00-bd81-534987aa10ce | -4.49277 | -55.48727 | 2026-09-20 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0ccefdf6-3c08-3a1e-8aaa-514e627685b3 | -13.89321 | -48.59155 | 2026-09-20 05:25:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cd7527af-7d54-3b08-a02f-a9d69b9a4a13 | -10.39914 | -56.15943 | 2026-09-20 05:25:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99010dde-448b-3157-b9f0-87e731ca7fef | -6.31862 | -47.62451 | 2026-09-20 05:25:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 92071879-c151-3126-9f6b-583599c7a3f5 | -6.29761 | -47.63289 | 2026-09-20 05:25:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4373a1ab-ed3c-3de5-aaaa-2d28386ff74c | -11.0412 | -54.16476 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42c12b3e-d2fa-3943-ba45-7cfcf30ae897 | -11.19932 | -55.03715 | 2026-09-20 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af8e192c-2931-3c9e-8879-d130b57fb3e0 | -11.98406 | -52.48136 | 2026-09-20 05:25:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5232c223-828d-3343-b184-fbee2f31d223 | -6.30091 | -47.60705 | 2026-09-20 05:25:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c137f098-6560-3e7e-83ac-76171efa6e6a | -12.01936 | -51.47433 | 2026-09-20 05:25:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7fa04f0f-d9df-3171-a561-3c0b3a2774c6 | -5.84575 | -53.51181 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| daaca507-ca00-3bdc-8140-eb0cd542a75c | -5.86835 | -52.03389 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a6cc130-8a07-3d91-b787-73d4fa6e452e | -4.62136 | -55.75426 | 2026-09-20 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b5258476-2ca3-3f00-84f1-82623ce1a24c | -3.36244 | -61.30948 | 2026-09-20 05:25:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a3b80f6c-9861-3bfc-9866-6d77e7ff68ff | -3.65637 | -58.85987 | 2026-09-20 05:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e6c349b-2a5b-30b7-89a2-b160db205d05 | -10.92705 | -53.9586 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d00874de-aea8-3d72-b7fd-cfa736d3b94b | -10.92848 | -53.9479 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6cc7f320-5cb3-328f-b174-2edbb881be57 | -6.0963 | -57.68279 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cfd04f84-3153-3705-a764-6542d6083c67 | -4.32076 | -60.88565 | 2026-09-20 05:25:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 007e887e-5754-303d-9ccc-006f9950239c | -5.85176 | -53.50273 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a87c45a-fcd6-3011-b8df-12b4a6464e4f | -5.74381 | -57.57594 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README95.md)
