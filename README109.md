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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f41efbc-f3e6-3740-8f08-63839c4ee418 | -6.30996 | -60.01066 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6cce2f91-5bb2-36d4-b402-fec1feed43f7 | -6.74318 | -59.42165 | 2026-09-21 06:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 5375a4a1-38d8-3954-8ee8-ef14231a490f | -6.45451 | -59.9728 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 24b58a43-3315-3414-8d33-85b3c608afcb | -5.92803 | -59.95515 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae196173-23cd-350d-9f67-d7be3fe5028f | -11.98986 | -58.079 | 2026-09-21 06:01:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| cf132a27-6b8a-348d-b7bf-e0539da0f49a | -8.85773 | -68.50845 | 2026-09-21 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d17a8c3c-5b40-3a86-b59b-5e8d8c84d32e | -10.46533 | -61.31797 | 2026-09-21 06:01:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d825fa80-5d2f-384a-a990-fd29c1d98132 | -9.55304 | -66.04256 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a883809d-e4b7-3110-82e5-b139d82e848f | -9.20648 | -71.86082 | 2026-09-21 06:01:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4df8c05f-b526-3622-b6a6-d1085852aad3 | -7.58701 | -63.04385 | 2026-09-21 06:01:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4fe0f697-e17e-3e6e-817c-a8a289b3e5b9 | -9.56199 | -66.0601 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f8a9915-862b-31b9-90e6-c40ef65e73ee | -6.3495 | -59.9672 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be6b7579-83cb-3858-b77a-21379c9f6320 | -6.30899 | -59.94391 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d3fea63-9bfe-308b-862b-7415c957a994 | -6.72453 | -55.09727 | 2026-09-21 06:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 110d10e9-380e-347b-86ca-6f6462f715bb | -8.79681 | -60.79974 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 670333f6-2f5e-3eeb-b4ed-a7107fa0d00b | -7.57219 | -57.67903 | 2026-09-21 06:01:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 769b4ff7-f2cc-3859-9256-c4aa399c0090 | -7.57832 | -57.67988 | 2026-09-21 06:01:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a5eefa9c-7c23-3465-9089-42513842525d | -6.34817 | -59.96564 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e3d57b2-409a-3151-9c3e-080ad33864b0 | -10.4657 | -61.31515 | 2026-09-21 06:01:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 560f61b6-7b2b-3c8e-bea8-0ee8bfea1b6b | -6.13179 | -59.94233 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c69f1d2-9022-33df-acf8-a609f85fb0b1 | -6.82732 | -55.54314 | 2026-09-21 06:01:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 2224a48c-d644-3086-91fb-21132e1a79e1 | -6.19366 | -57.78456 | 2026-09-21 06:01:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 85756b6f-71ef-3f4c-8fc7-492a694141ca | -6.09723 | -57.6272 | 2026-09-21 06:01:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d171834f-2ca0-3b74-ad31-00dc618c1d63 | -9.17551 | -60.304 | 2026-09-21 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96c2c743-5d40-3187-9735-c3665969882a | -6.10089 | -57.6885 | 2026-09-21 06:01:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9f997020-9913-32b8-acd2-f83295c1c2f0 | -8.79639 | -60.80275 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf1c22f2-59b9-3a6a-9e08-48c3eec8db02 | -6.15434 | -57.7162 | 2026-09-21 06:01:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9caedbd8-e286-3484-82a3-ac7878d4b2d9 | -6.4594 | -59.98388 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 28b4f6aa-594c-3d24-a9f4-145c02ecee68 | -9.55968 | -66.02476 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d4decd31-2ea6-317b-a747-07830f90b505 | -6.49424 | -58.38585 | 2026-09-21 06:01:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 255cf5ba-e658-3523-a501-314ceed608bd | -9.55433 | -66.03399 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8938f3ad-74c1-3639-ad4a-0b6c138dba26 | -7.57644 | -57.69386 | 2026-09-21 06:01:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7b15e676-760b-3fa6-8d0f-69d1bdf9fa25 | -10.76511 | -68.96506 | 2026-09-21 06:01:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 187053e5-ea4d-3d20-9def-7bb876426e61 | -6.45852 | -59.99025 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| adfaef92-cd74-37d1-a2bc-37c2e30de7cd | -6.31041 | -60.0076 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 972a3030-601e-37e1-97cb-94b203d55888 | -8.03561 | -70.89886 | 2026-09-21 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e08e37e1-415c-3d34-8092-2560e2e6acb8 | -11.99049 | -58.07371 | 2026-09-21 06:01:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 12b2a2f3-c1e5-3262-8cbf-bed6e63dd0ac | -6.44472 | -59.97523 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b46d34d6-bee5-3253-a20d-4ce34ac4b5bf | -6.29473 | -59.93252 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3067067c-b497-3906-894e-3bda2ee7b464 | -9.74589 | -65.05564 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4e3eee4-233e-380b-a4b2-94e45434e2b3 | -11.99683 | -58.07438 | 2026-09-21 06:01:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 322158bb-db43-3fab-bb57-3d79b206fe36 | -7.31723 | -55.61171 | 2026-09-21 06:01:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e912fa9-b5e1-3cd2-9666-11a0cf8d464a | -9.56033 | -66.04364 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ee5279ab-dcfa-3ca0-aaaf-75b43e10586b | -6.34475 | -59.96332 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 294ef09e-d49b-31fd-8549-224402bd720c | -7.56544 | -57.68283 | 2026-09-21 06:01:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0b9c8233-d402-3ec8-829e-819e8b213c4a | -8.65627 | -62.482 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0f77646-3d9a-323d-b834-823ce6112616 | -12.8246 | -54.0442 | 2026-09-21 06:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 28622deb-a062-337d-bc0c-4aa0e0362770 | -12.8246 | -54.0442 | 2026-09-21 06:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 873687a7-fe4a-36a2-a146-ab3b22b3f2b6 | -12.8246 | -54.0442 | 2026-09-21 06:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 9c19cc16-46d0-3a50-b56b-d2d56931043e | -12.8437 | -54.0422 | 2026-09-21 06:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 6a47b751-849b-33f5-9092-b68364e3a8c1 | -8.78139 | -68.84837 | 2026-09-21 06:46:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d6fab730-20de-3f70-8002-57b8e33037fe | -8.22705 | -71.04532 | 2026-09-21 06:46:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28c37bc0-9465-3162-9d24-379ea74e0d74 | -8.23239 | -71.05046 | 2026-09-21 06:46:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b5703f8-9c82-336f-820b-e7f898309b49 | -6.96377 | -71.75692 | 2026-09-21 06:46:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d2a8e02-0bc6-3378-ba67-e6b195bac781 | -6.96328 | -71.76054 | 2026-09-21 06:46:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fbdf5fcb-ea75-34b1-91f7-a73f4658a68f | -9.22341 | -71.86988 | 2026-09-21 06:46:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b4beb981-b22c-3f23-b4b2-9ad154eb3a45 | -8.22762 | -71.04098 | 2026-09-21 06:46:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 065e2fb2-fe3e-3f07-b65d-7e07bae3333d | -8.01896 | -71.23201 | 2026-09-21 06:46:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03339e21-1844-325a-8e56-edba4529238f | -9.22107 | -71.8677 | 2026-09-21 06:46:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d0a59e09-47a1-34bf-9222-968c4043fa5f | -8.78214 | -68.84218 | 2026-09-21 06:46:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 577ffb5e-4fa3-35b6-9072-992b08f105be | -8.02425 | -71.23699 | 2026-09-21 06:46:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4850c19f-2411-346b-b083-1ed4e69d0e1c | -10.89284 | -69.34666 | 2026-09-21 06:48:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| da54035e-a80e-3773-8d4f-3f620d373f2f | -12.8246 | -54.0442 | 2026-09-21 06:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| ed77d590-c811-3b3f-abe1-0cc89501bf7c | -1.11423 | -47.73034 | 2026-09-21 06:59:00 | AQUA_M-M | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| d9177341-1d64-3381-a3af-c68f6ddb27f1 | -1.11276 | -47.74028 | 2026-09-21 06:59:00 | AQUA_M-M | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| ce50fe58-0d1c-38cc-aee2-8bc9705c27b9 | 1.54184 | -55.79219 | 2026-09-21 06:59:00 | AQUA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 7e77853c-d1e0-3e2c-933d-500fc8918cb5 | -16.0495 | -52.5106 | 2026-09-21 07:00:00 | GOES-19 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 913df873-e7b4-3204-b99a-1dff083e34de | -6.7281 | -63.1303 | 2026-09-21 07:00:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 68188a29-3e37-39ec-b9a6-f3cb7d78768f | -9.68005 | -54.33583 | 2026-09-21 07:01:00 | AQUA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 9d5b20a8-ca65-340f-a1fc-22c039a5ff86 | -9.0179 | -49.82062 | 2026-09-21 07:01:00 | AQUA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 16202740-a153-3725-a398-a87dfc365e60 | -8.78776 | -48.74025 | 2026-09-21 07:01:00 | AQUA_M-M | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 30.2 |
| d6967fbb-0410-386c-b1fa-1a0b67b28482 | -10.67728 | -48.71181 | 2026-09-21 07:01:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 3901697e-54f8-30c1-86fa-e21e248b0e6c | -9.26436 | -46.19279 | 2026-09-21 07:01:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 2ad71f29-4d8d-3997-9a43-3631ff1dc5c2 | -5.88234 | -52.04257 | 2026-09-21 07:01:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1abf1cf0-2b7d-398f-9b18-729488001b48 | -10.37345 | -48.907 | 2026-09-21 07:01:00 | AQUA_M-M | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 07e564ba-145a-3370-bcc8-08656cf7f956 | -10.37502 | -48.89572 | 2026-09-21 07:01:00 | AQUA_M-M | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 37e531f8-5988-3d2a-b745-1f24e28b92f4 | -10.43301 | -50.24376 | 2026-09-21 07:01:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6f697043-906a-3efc-9562-229257dded88 | -6.56406 | -45.53939 | 2026-09-21 07:01:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 1c29aba0-78a4-3324-998e-68c76bc46da0 | -10.46701 | -50.26419 | 2026-09-21 07:01:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 78448f47-73b3-3fc1-b292-0f2278466d4b | -5.81054 | -52.08992 | 2026-09-21 07:01:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 31159ed2-4177-3df5-a72b-31858e08dc06 | -5.89432 | -53.64217 | 2026-09-21 07:01:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0017c88d-7b69-3c31-846e-6f2cad1c0a9d | -4.09468 | -52.1239 | 2026-09-21 07:01:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 8ff3d20e-720e-3bec-b1be-25ae005f32a2 | -8.3337 | -50.83021 | 2026-09-21 07:01:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 35c0a994-cb8a-3017-b9b9-62993727dd05 | -5.60019 | -44.84788 | 2026-09-21 07:01:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| d5e58b7e-2cef-3fd0-87ca-0dec83979685 | -10.38643 | -48.88581 | 2026-09-21 07:01:00 | AQUA_M-M | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| eb6a0734-e6f9-3879-ae24-976a9fc8296d | -10.38883 | -50.2275 | 2026-09-21 07:01:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 908965f8-174b-3d05-829a-bb82c42646c3 | -3.37821 | -50.43873 | 2026-09-21 07:01:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 34cb6907-2404-30fe-95b7-1e1a8de299f1 | -3.44601 | -50.60571 | 2026-09-21 07:01:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 302063d5-273d-312d-8e1e-a83fda65a886 | -7.29817 | -46.7717 | 2026-09-21 07:01:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 200150cf-32cb-3de1-8fae-71d92598b9c0 | -9.45421 | -45.39997 | 2026-09-21 07:01:00 | AQUA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 0de0423c-dc67-364d-abe5-d5dc69f228f2 | -7.32845 | -55.59923 | 2026-09-21 07:01:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 52b0513d-5d5f-3c9c-a009-75dd1c7461c1 | -5.81096 | -53.51704 | 2026-09-21 07:01:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| da58b782-80bb-30c1-9f4f-f2166da83dea | -10.47612 | -50.26552 | 2026-09-21 07:01:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 33ba82fa-212f-39a8-9db2-253b3ac604ce | -3.43726 | -50.60442 | 2026-09-21 07:01:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 2cae4b56-aa80-3ae5-8b72-3bb9bc969166 | -9.82596 | -48.43372 | 2026-09-21 07:01:00 | AQUA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ff6790e4-1e23-3a1d-be58-8d54270737f2 | -10.39023 | -50.21789 | 2026-09-21 07:01:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 601283d9-633a-3054-b3b6-73c880608206 | -5.60277 | -44.82903 | 2026-09-21 07:01:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 61bd18f8-4f9b-3572-8dca-de619ad780c7 | -9.68169 | -54.32552 | 2026-09-21 07:01:00 | AQUA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 717f7b9b-c252-3d83-a2e0-6a5ad8caa78e | -2.61084 | -51.72162 | 2026-09-21 07:01:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bb768b2f-53ce-3bc1-9cae-647324a68c7a | -8.77803 | -48.73906 | 2026-09-21 07:01:00 | AQUA_M-M | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 12.2 |


[Clique aqui para ver as próximas entradas](README110.md)
