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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b255a11-1613-32a6-93ba-5ef517e6b473 | -3.12017 | -53.71773 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| e53f735d-e651-3a50-9af4-872eeaff4774 | -1.10572 | -54.13721 | 2026-10-04 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9dbf460d-6046-3f9f-a3e3-336349d439ed | -4.42263 | -55.75061 | 2026-10-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89353efe-c13c-3685-bd69-ba15f512b491 | -3.0927 | -51.09958 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc07bdd9-4e03-3985-816f-c421b976d911 | 2.01186 | -61.09591 | 2026-10-04 05:16:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 722ac92f-2de1-3009-b625-cf5c99279b0d | -2.80437 | -54.09182 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c70a8942-6892-30e9-b70a-ecc0890d4aba | -5.99674 | -53.52924 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 934b9709-92ba-3724-af9f-9267c2e127e4 | -3.04356 | -54.22698 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9ae01262-4eee-34d9-8161-d66837a7b3ae | -3.00995 | -53.88446 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f41db129-a07d-3356-a8d5-2f1a434ee2ad | -2.79717 | -54.11486 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c8bcf95-6134-30f3-8e26-6abc4fe63440 | -3.00418 | -53.88019 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7e29dc0-175d-31aa-add3-14ecfa47dc10 | 1.04111 | -59.46753 | 2026-10-04 05:16:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fce4e7f4-7ae2-36d2-b11b-bb618d5e368c | -2.97162 | -54.08713 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4d0407b9-0e6a-3ab5-ac14-7418b1e619dd | -3.12512 | -53.75637 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 51df8651-60a9-3214-98ce-171d1c8b848e | -2.91206 | -54.14305 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 751c906d-c582-37a4-bf47-7e29ee34725b | -5.377 | -56.05451 | 2026-10-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a7a9c1f0-e00b-3c22-888e-878e2f2d2be7 | -2.43831 | -49.02793 | 2026-10-04 05:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7fe88b0-95fb-3d42-b07e-c8fd1a2831c0 | -3.10595 | -50.2894 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9fe260d7-6136-3ff1-a297-5269973c705d | -4.8172 | -54.73302 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 999b76ed-3395-3079-acdd-33c858c734d2 | -2.75398 | -51.56231 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b3dec977-93d4-35ce-849c-f924e6536673 | -3.12577 | -53.75227 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b95393b5-7102-3156-9c06-8b183b40eed5 | -2.80834 | -54.11256 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 68598e7b-6197-3a76-b71c-7f713933b885 | -3.95964 | -55.77767 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 190c6795-fb5c-3a91-b1a5-b9f45ea95276 | -2.88452 | -54.1348 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1ff94fe0-1e16-3dd2-aebc-e6d52fe8627e | -2.92657 | -54.16537 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 82c93d92-a0f8-3634-96f1-7b5e77002fcb | -2.58328 | -51.8626 | 2026-10-04 05:16:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 788c0e1b-ef6f-3a8c-af85-a70e71649c7b | -6.07059 | -53.47456 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1cae36ee-049b-3390-b643-5736cd3664e2 | -3.86097 | -55.97565 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 912295fc-cfca-30af-bfb8-a8952add21b5 | -3.94014 | -55.83632 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c4cf1af-7088-3a5d-820a-4b6309aa825f | -6.0005 | -53.52991 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e58ba9a8-5ef6-3bdf-b570-b1dad6ce7896 | -5.96074 | -55.34657 | 2026-10-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 89600937-cc67-35e8-85c4-35b8fcb0014c | -4.20835 | -53.45618 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a820c545-8d2e-3ed8-8f1f-2b791b53961f | -3.11657 | -53.71718 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 5cfe4d5d-6c2f-3fac-bd9a-9b106da4bc52 | -1.87894 | -50.61882 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1ce4ce42-f235-3a88-b233-682372d8c4e8 | -2.99963 | -54.23215 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c2fd823-05b6-37d7-ba97-56cf6aa7790b | -3.5175 | -54.61968 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6a2a36cc-147e-3023-9415-8ba239f49081 | -3.79611 | -59.38426 | 2026-10-04 05:16:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af8afb19-b454-3a36-86c3-716c6110ed77 | -1.20943 | -55.85681 | 2026-10-04 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b01f7511-02a1-378a-8526-07d60ea1621e | -1.74294 | -54.95732 | 2026-10-04 05:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 052a6c76-a545-3501-aa67-46d930444609 | -2.88229 | -51.03393 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4bb13987-e1bd-3c15-8cf1-b357472070c1 | -2.61177 | -51.21725 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f81d6a1d-f0bd-36f1-b40e-2ec74ec23d3f | -3.46393 | -50.10445 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d633bd1d-4dd7-3698-b9fa-a47e3f4719a6 | -3.18396 | -50.54192 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2966d4c-d5b8-3156-8810-7a3ca2044deb | -2.95116 | -54.10074 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 09dc4c92-d7e6-3ab9-9779-ae7be648fe4e | -1.62433 | -55.0201 | 2026-10-04 05:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c0c01572-903e-3cb3-8a2d-37777ed2bc80 | -2.61593 | -51.21788 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eedf35a9-f29a-3a9d-9cd8-6bb62ee90207 | -2.89265 | -54.15208 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2cba071b-aeb6-3cc6-80a5-19ba563ca3cd | -2.82119 | -54.12257 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1dac51ad-6b95-3939-9a25-ef28082d6c72 | -3.84976 | -55.80782 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3275c967-355d-3ca9-9b92-7391bbdf4958 | -3.12283 | -53.7476 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b4dfa24-6a5d-311f-948c-8e0f0d9b93ec | -3.24383 | -57.87318 | 2026-10-04 05:16:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ade7bcf-4f45-3615-8cd7-ea5cca9623cb | -3.04232 | -54.23479 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d80ea93d-f766-323a-8dbf-7e65acc852b7 | -3.29255 | -53.83874 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 692a3bb9-b1e5-3848-ae66-45a25e2d5a2a | -4.12879 | -54.16113 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a32d94ce-f676-3362-9991-56ce7ddeff25 | -2.97576 | -54.08372 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df427de9-f034-3168-8795-2ebd8bb6b99b | -3.41696 | -48.33856 | 2026-10-04 05:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e6e4296a-8b7c-3788-8b99-4a72ea8ed647 | -3.79761 | -52.00183 | 2026-10-04 05:16:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fcd2dfed-b9b3-35c2-9975-e10225afac44 | -3.76953 | -51.86063 | 2026-10-04 05:16:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4342923a-7897-3552-ba12-9a9b4f740ff0 | -4.46232 | -50.98276 | 2026-10-04 05:16:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 55c6e902-9191-3e36-94fe-45739eb919d5 | -2.77361 | -57.69104 | 2026-10-04 05:16:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a01e21f6-dca7-3dc3-92cf-7b6885fddee7 | -2.68547 | -54.43012 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f338773c-090c-3095-86d3-aeb4e3eab4f0 | -3.18639 | -54.07779 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| efa0d17f-3852-3b28-8b49-69a0560fa032 | -2.96567 | -54.10239 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dfc48834-a64b-3997-a12e-577b4bbad521 | -2.94702 | -54.10414 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a95a4b9-e726-3120-9a25-4e06f62d2d17 | -3.11564 | -53.74651 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 25909008-2ee7-3188-a8b0-07f77759a623 | -3.61655 | -55.51344 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb07ea8d-dfc7-308f-a940-8985e3286daf | -1.74451 | -55.24263 | 2026-10-04 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f28e663a-1d3c-3583-81dc-acede5dd4755 | -2.16304 | -58.11139 | 2026-10-04 05:16:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ac33ce9-6ed2-3773-9ba7-0783fab7a254 | -2.88513 | -54.13088 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b719bec-b6c0-3b41-bd44-2563ec04f22e | -3.41969 | -48.33745 | 2026-10-04 05:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ccdd893a-13cd-38ad-b7c9-edcdef2b2730 | -2.54392 | -58.00557 | 2026-10-04 05:16:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 921b9c21-b153-3180-b953-1ffbd12a3af3 | -3.84205 | -55.9655 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a392b4a-b4c1-33bc-b634-96381a0e7b28 | -6.00493 | -53.52601 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 547b7792-ec31-32c9-97a2-08e6e121ca94 | -2.34495 | -57.11792 | 2026-10-04 05:16:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 751f2fb1-0728-3c74-9a20-4b5114703cba | -3.05591 | -51.7096 | 2026-10-04 05:16:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b37d7dc7-e227-35d4-9db8-97bfab7769e5 | -2.81706 | -54.12595 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 73b6f9e6-52c5-3884-8002-c3ca6fb40708 | -2.97455 | -54.09163 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 19061e10-1e8c-3dbf-9816-9a8639c55bfa | -3.11924 | -53.74706 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 86c41b90-1de3-3262-847e-aca51e2cddc9 | -2.9357 | -54.19878 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dbdff398-8d94-3087-b3ef-19acc500afd8 | -2.54476 | -57.40097 | 2026-10-04 05:16:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a86ecbce-6a8f-37bb-b838-6c36c8dfdc9b | -4.57331 | -54.94798 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c1ec6cb-bc0f-3d6e-ab04-88271d6f0411 | -3.94349 | -55.83685 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17563ca2-2814-36b3-8dc6-5dbb98be8b0d | -3.13188 | -53.74771 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 772c8825-cf07-3db0-8437-6b2c6c4a9220 | -4.46732 | -54.97038 | 2026-10-04 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d20d4e8-3d74-3e2b-932b-ac8cd4ea5cfd | -3.0759 | -54.36995 | 2026-10-04 05:16:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67afb4ec-6423-3af5-ae02-56fb91566ba3 | -2.90334 | -54.12967 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aa9da852-053f-3e1d-85b0-05a12e2ccedd | -3.49386 | -59.3703 | 2026-10-04 05:16:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf646e46-5aed-38c7-8d08-8d6759deeb4d | -2.48246 | -56.09933 | 2026-10-04 05:16:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85b1a6ad-8002-387a-94b2-f5c5208990be | -3.15942 | -59.0899 | 2026-10-04 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f99edcd9-301c-3212-a69f-1a63af7f9905 | -1.25679 | -55.77217 | 2026-10-04 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 84d5e793-c4bd-305a-b8c5-d3309ae99fcb | -4.39144 | -45.98883 | 2026-10-04 05:16:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2fad8abd-3f62-3996-b583-d114c41c1912 | -6.20029 | -52.80091 | 2026-10-04 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82cdb6bf-aaa8-36e8-b65a-0f249b79f250 | -2.91451 | -54.12737 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7abf343f-691a-3e72-827c-d841dc7e0684 | -2.94558 | -54.13612 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3869f34e-100e-3b7d-8eef-f8c62e2e3e7b | -3.06806 | -49.52686 | 2026-10-04 05:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 37c9e6e4-ced2-3663-bdbf-991eda732969 | -2.69007 | -54.64304 | 2026-10-04 05:16:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 3255491c-e93d-3440-819c-c5a1abd4ea2d | -2.81644 | -54.12986 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 031ef1d9-0d68-347c-a538-518b50b72dfc | -1.6221 | -55.0124 | 2026-10-04 05:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb533937-05ef-39b7-849a-3030d61dda8a | -4.53652 | -55.97201 | 2026-10-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cdd85c03-419f-3403-bc89-fcfa91a95511 | -5.77855 | -50.22332 | 2026-10-04 05:16:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README55.md)
