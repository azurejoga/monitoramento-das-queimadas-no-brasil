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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c29b01cb-e9a4-32d9-b6d4-61fe63ce3a4a | -13.31505 | -47.22015 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e44c5a18-4ef4-365f-b598-e9514de17359 | -11.92198 | -51.53857 | 2025-10-01 04:51:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a4e36122-1c18-35dd-be87-07f149ee5dcb | -12.86738 | -46.94106 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 02430959-30d3-3640-aa68-4a1d58cfacd3 | -11.46126 | -45.08944 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fef185d8-5b0b-37a5-8d8c-b90d3987d0b7 | -13.32938 | -47.87354 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 964d6e57-fe1c-3591-8508-acc7f11c7d82 | -13.33218 | -47.34169 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ded91f01-7ebc-31b6-8e71-d723a8839f70 | -12.86594 | -46.98238 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80d82923-97a6-34c4-ac03-d05c5f458b0c | -11.76499 | -46.84531 | 2025-10-01 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5cdfce54-579c-377d-aec5-8ba3b7224cb4 | -13.24608 | -47.30724 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 251853f2-e7d2-3978-87f7-9c88a1040fa1 | -10.08315 | -45.62518 | 2025-10-01 04:51:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e3cb371f-10a0-31d2-acd6-d14fe5aeb6a4 | -16.00278 | -50.87348 | 2025-10-01 04:51:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5e2c3d8d-411e-3234-87a1-b41e18dd245a | -13.38865 | -48.0832 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc50b168-83a3-3527-9f1a-399313c3d384 | -9.99123 | -48.35489 | 2025-10-01 04:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c037a2b0-c0f1-3ef5-82da-3dc6358e4374 | -11.156 | -54.12231 | 2025-10-01 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ebcb78f-b2b2-313c-b7fe-d0a8e37c3893 | -13.66106 | -48.04092 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a6cc960f-43d6-37ba-82d6-583e9daa614b | -11.14863 | -54.30868 | 2025-10-01 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 2679950a-8822-32fb-94d2-51e1c543318f | -15.48295 | -45.89975 | 2025-10-01 04:51:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bcb7028e-e3c4-3bc8-85f5-f8702a0180d4 | -15.16646 | -52.80809 | 2025-10-01 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f315c2ed-14d8-34f6-979b-9552c20246be | -10.90947 | -46.5747 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fae4753d-fa3b-34db-964b-4732a8f70d7e | -11.52568 | -43.55141 | 2025-10-01 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4b18971-34ef-378c-a365-356f9450fe45 | -13.89425 | -51.83592 | 2025-10-01 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6e8a1c50-070e-3672-9906-3403d3a507e3 | -15.36013 | -46.11343 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 21e5805e-604b-3f2f-add0-b11a12933a0d | -13.98088 | -44.87974 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 248dc2f1-4aba-391e-8202-3dac69c3c7d0 | -15.54068 | -42.66226 | 2025-10-01 04:51:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 925e0fc4-b5fa-314b-abec-12eb9c07e7dd | -11.47128 | -45.08535 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a424eced-8cc6-3292-8886-2c8cf296efe9 | -15.53619 | -45.2246 | 2025-10-01 04:51:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eacf55ae-7500-3432-b20f-7273a6891cbc | -13.14496 | -47.41398 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d993ca4-6a62-384c-a272-ac9039d03825 | -15.99795 | -50.87772 | 2025-10-01 04:51:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f77bf92e-ec11-3392-b3c8-c94797ba2a95 | -14.50744 | -48.47865 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ffb7312f-70b8-3825-a901-c02b004e1243 | -8.71233 | -50.05138 | 2025-10-01 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa8b9b32-1910-3e11-b160-35a7066c81d9 | -13.7034 | -48.64309 | 2025-10-01 04:51:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 48f16c37-9216-37f8-98b9-c5d857b32c7a | -10.90274 | -46.56219 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d526fe70-91ee-3608-815d-3cfd78595a2b | -11.84206 | -44.99095 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8ceef692-a295-3091-8c6a-c2af1dfe2a66 | -13.6712 | -48.08364 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ee13c9d7-37a1-31bb-9448-2574611823f3 | -11.198 | -47.74495 | 2025-10-01 04:51:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dfde156f-b43b-3d4f-8a22-e90370f9d1ac | -15.07645 | -45.0759 | 2025-10-01 04:51:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| da058d78-94fe-3c27-a828-bc0b8658ad56 | -11.09403 | -47.72221 | 2025-10-01 04:51:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 39f263d2-41a7-3c1e-b66b-b2b623c0c56e | -14.05208 | -47.98115 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| acaa2db8-526f-31c0-aac1-0c5ebdefd701 | -10.95737 | -48.83195 | 2025-10-01 04:51:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 213d5872-f42a-314c-bab4-f4be4397c643 | -13.28237 | -47.22749 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a5cad149-27de-32ff-a911-3ec0274f3432 | -10.90657 | -46.56919 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 05010f96-4899-3efc-98ff-3645c9e83bb2 | -14.35628 | -45.93895 | 2025-10-01 04:51:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 20.6 |
| a83de6b3-8a92-3a60-9f9e-0b22e669c0b7 | -11.76349 | -46.85623 | 2025-10-01 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 10e7dfed-67fe-306c-b6ff-032e6339eafa | -13.76537 | -51.22203 | 2025-10-01 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 860344af-be34-3ec4-854d-7589eab7351f | -14.70529 | -42.31802 | 2025-10-01 04:51:00 | NPP-375D | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6c0d0c06-1170-3727-ab88-4c0c438df3bb | -14.18594 | -46.11012 | 2025-10-01 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e3c0aa2d-ef60-3fa5-ab8b-feb4a2d8f7e2 | -15.17257 | -46.42141 | 2025-10-01 04:51:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8cc698a4-ed5d-3e60-bcbc-6f4158d34674 | -13.8167 | -48.02964 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 16a774ce-c747-3768-90c9-02406714fdf1 | -12.88052 | -44.68249 | 2025-10-01 04:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2a4a77e9-ab5e-309e-8ae4-ba70b0000285 | -12.01427 | -46.62174 | 2025-10-01 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98631ba0-235b-3c58-8660-80ea4db5c6c1 | -13.97462 | -44.88997 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5083da57-5109-3aa0-916b-b270cef0351e | -12.36506 | -50.20377 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6aac7936-c3a6-3eff-a39f-318a377746e9 | -14.40908 | -47.14649 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0eb42fe1-e1bb-3833-8b5b-4b75ef47c363 | -9.73213 | -48.02816 | 2025-10-01 04:51:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa8cae4f-7fd4-3ded-8a06-7edc1fe048dd | -13.08094 | -47.0707 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1d1c2a74-7aa3-3ac1-9835-76c07e68f5ef | -14.05057 | -47.97699 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4e427cf6-73c8-395b-8c7e-e637eebc6bd2 | -10.49283 | -51.51969 | 2025-10-01 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f67088a-95fb-32ef-8ec8-b05a7d4cf83b | -15.3941 | -44.97557 | 2025-10-01 04:51:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c2f7c9bd-3ff6-3398-afad-e909d669e784 | -14.03441 | -47.96228 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bbffcfff-fe3b-3eb1-8af2-591ffcaf8975 | -13.7951 | -51.23441 | 2025-10-01 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 776ab7c2-4edb-3662-9753-5ffd02928656 | -13.94516 | -48.11016 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 98da50d8-6377-3158-95df-999b08a44fe0 | -15.48989 | -45.9207 | 2025-10-01 04:51:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6750e61f-58a1-3d84-b653-4ab4b4bc6650 | -10.03575 | -52.10176 | 2025-10-01 04:51:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aa2ad792-f671-3b27-bf82-f2a5cf54de7d | -13.80581 | -47.49305 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d663e4ac-4af1-33af-af90-7f6385edcb08 | -14.97977 | -50.76413 | 2025-10-01 04:51:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f7d9fd8-b996-38d6-b698-7da150693665 | -10.28739 | -50.46703 | 2025-10-01 04:51:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 4458c6d2-9d16-3e0a-9d41-80aed11a9f04 | -14.71008 | -48.22302 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6fc226a8-d8e2-3e3f-9d3e-c083ba62f1a2 | -15.27398 | -49.27624 | 2025-10-01 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8010f7a9-334a-338d-92ab-9e0bc5441ed1 | -15.5303 | -44.34503 | 2025-10-01 04:51:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 67e5de32-1a1d-3458-af7a-e646535d2ebc | -11.49865 | -43.51126 | 2025-10-01 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d3c21767-1561-32ee-9dbf-ae8e52d40a08 | -11.74104 | -46.86585 | 2025-10-01 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e14041dd-6449-3b10-8bd6-29d28e15449c | -11.93427 | -47.08382 | 2025-10-01 04:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9a874f2-33ac-3786-b7b9-bb7d2a80a619 | -16.37623 | -47.07243 | 2025-10-01 04:51:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a01d8e33-f439-3d97-a493-16d73a5c6105 | -16.20981 | -48.27442 | 2025-10-01 04:51:00 | NPP-375D | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 47517cb5-834d-328a-bcf0-56dd6a8914fb | -12.43301 | -50.17847 | 2025-10-01 04:51:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e102480c-fb0b-367b-9c34-5bb9af93a82e | -15.66158 | -51.33002 | 2025-10-01 04:51:00 | NPP-375D | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ffaa9259-13b9-3f18-82af-0ba0b2ef67fd | -11.57124 | -50.18563 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| be99f35e-3ed3-3e20-af1d-b306b9c81a97 | -14.54604 | -48.22257 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 45a04de1-71dd-3f35-98fa-d5883d4dba2e | -9.92641 | -43.65663 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78bbe95e-6ea5-357f-84a1-033c7c3c6e29 | -15.44377 | -43.64673 | 2025-10-01 04:51:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 145256c3-7403-3156-9ae6-ad9758c83e9a | -13.9393 | -48.1235 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 949b8771-1aa6-39f6-982c-74e90623c5cf | -11.94247 | -43.91198 | 2025-10-01 04:51:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a42dc17-e5ba-325e-9c3a-438133efb69e | -9.39964 | -54.70827 | 2025-10-01 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 976b6903-a873-3d5c-b83b-1c1d6fa33339 | -8.87112 | -50.9023 | 2025-10-01 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0bc7aa4-4fbd-33df-b8a7-1606195856ce | -13.81722 | -47.50126 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 45ce337b-304f-3a07-998f-aa1ccc5c2594 | -14.80278 | -48.32816 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 868eea74-1618-3d2a-872f-10fe4a5a1c7a | -16.02669 | -50.88148 | 2025-10-01 04:51:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a38e6b08-69d9-34fd-a40e-63dc0984fbb8 | -10.04407 | -52.09231 | 2025-10-01 04:51:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af10e54d-bc50-3125-a66a-536ac8f26ac5 | -11.43002 | -43.50243 | 2025-10-01 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0f48c50-eeb6-36df-a76e-717c2dd66bd1 | -9.42832 | -54.71312 | 2025-10-01 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3b0a1a46-6161-3c82-a9fd-393f40947316 | -14.79155 | -45.7994 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 9fc8e563-7afb-3600-b830-0f2c999a79c5 | -12.95106 | -46.42617 | 2025-10-01 04:51:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9fc4598a-41c5-3cac-9e4e-2fa89e602403 | -10.63541 | -48.59055 | 2025-10-01 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b2ef2f44-1f26-3b14-abcd-43e5da1ba6b0 | -12.95225 | -46.41745 | 2025-10-01 04:51:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 89bee29f-6100-34cf-918f-b3ce7ebf5111 | -10.90603 | -46.5391 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| efe1c753-5cb4-3fb2-b963-422f07da93b1 | -14.88332 | -48.32127 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4104f416-49ec-3e18-ad23-36f3e28095f6 | -12.80036 | -46.89934 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b889216f-801f-3d5f-a3b1-d3e5e5037742 | -13.67402 | -48.06343 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d0e5cf1a-1cc6-31e2-a6c3-3b7228f3592b | -13.30297 | -50.66612 | 2025-10-01 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6bb3640d-b2dc-3f7f-a8b7-2f4174f61c0a | -9.40813 | -63.6981 | 2025-10-01 04:51:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README105.md)
