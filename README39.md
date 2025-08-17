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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ded494c-5656-3f25-88ef-6e46dca1b6be | -5.44733 | -60.13314 | 2025-08-17 05:55:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 340f2c29-8d63-37c4-bd00-76f24eb5541e | -9.38961 | -60.54224 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98549f92-5f36-3dfe-abfe-f9dbf6a2b948 | -9.51824 | -60.53608 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bbfca6c0-e16a-3363-b3a0-0bbfa94d9d3e | -8.87108 | -68.51012 | 2025-08-17 05:55:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9fe4d761-e666-3253-af83-231b7d0ef4a0 | -12.78669 | -60.15796 | 2025-08-17 05:55:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5b63cb48-844e-30b6-981e-6a6e3d27d763 | -9.55604 | -63.6601 | 2025-08-17 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f674561f-5035-3ede-8204-4ffd451ded1f | -12.99283 | -56.85735 | 2025-08-17 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| db730471-1d4f-39e4-85e3-b40bda3079d7 | -8.33392 | -70.57288 | 2025-08-17 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 05cf5f21-89e0-30b4-a75b-fa5f96c6d4ed | -9.85868 | -65.26071 | 2025-08-17 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c53f038e-58d8-3be0-8fe0-26aaccc03a4a | -9.50463 | -60.55965 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 73e8cf6e-3038-369a-806e-da3a8ba6f11c | -9.62233 | -65.37201 | 2025-08-17 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2db1c1c0-a5cf-3f03-b568-35479bf61735 | -9.55549 | -63.66399 | 2025-08-17 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fed2f3da-4bf2-3983-9d14-0fa516a931b9 | -11.36182 | -61.84678 | 2025-08-17 05:55:00 | NOAA-20 | PRESIDENTE MÉDICI | RONDÔNIA | Brasil | 1100254 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 579fa689-182a-318b-8299-56146cce6d6d | -9.55495 | -63.66784 | 2025-08-17 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bee10f5d-1a09-3f79-9dba-e45d02e21f71 | -9.50868 | -60.52849 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 336ee52d-ac6b-3574-a4f4-46c53d4ee9cc | -9.50429 | -60.5216 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a576986-f3f1-3849-997b-2e95e8614726 | -8.87772 | -68.51116 | 2025-08-17 05:55:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea5e2894-958e-3ed6-9bde-66ae85aa71f8 | -10.11127 | -57.7638 | 2025-08-17 05:55:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c9d4fff-2f3a-3123-9690-5beb10d6f9d4 | -8.52258 | -70.82116 | 2025-08-17 05:55:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c0db6682-aea4-31b8-af16-e77c2a15916b | -5.45277 | -60.13097 | 2025-08-17 05:55:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7b3ed84-031b-38c5-9f3a-bc81a25ca51d | -10.35796 | -64.50747 | 2025-08-17 05:55:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1b2948f-4423-3a04-84b4-b08eee53b6ea | -9.0469 | -67.42297 | 2025-08-17 05:55:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e01f35d-2b09-357a-9f8c-309ff271d88a | -10.46148 | -69.15279 | 2025-08-17 05:55:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 51bd6ea5-4f9a-3f03-9782-b5b33a10abcf | -9.39478 | -60.54291 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf1d2b05-dc9d-30f7-8b84-f92288d36fea | -8.86831 | -68.5061 | 2025-08-17 05:55:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6e208d6e-f508-3d23-9979-4d33f186191f | -9.92776 | -60.4691 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b4914f3-8617-3ded-ba9c-c1796157f16d | -12.99219 | -56.86355 | 2025-08-17 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a2ad5855-1ec9-3c2d-87e5-cb5d6c30cf55 | -10.6843 | -69.55109 | 2025-08-17 05:55:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e6d35ca7-4723-3d0d-ad8c-f699edc18916 | -9.51346 | -60.53227 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| be6be946-c241-34ac-a43b-2c2fa0f78f0b | -9.0435 | -67.42245 | 2025-08-17 05:55:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 60369a28-bf81-34ed-be18-71902b4be4e2 | -9.55636 | -68.57833 | 2025-08-17 05:55:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 400eafa6-7d26-3e64-9345-f9de07895cdb | -8.51918 | -70.8206 | 2025-08-17 05:55:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c0ac952-3255-387a-a31f-35a73182a485 | -5.45737 | -60.13458 | 2025-08-17 05:55:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1fe3c549-e9e9-34a0-bec6-774914e4dbd2 | -13.42896 | -57.03125 | 2025-08-17 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 221003f9-56ae-3f0e-a38d-9573276d081b | -9.51387 | -60.52912 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4e661b1e-055d-3546-9300-3fe0d444fbb0 | -14.84462 | -59.64133 | 2025-08-17 05:55:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0d4ae53-b5f1-3eb1-bfc3-1367425079d9 | -9.51021 | -60.55725 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 75387f53-7c6f-3f39-b90c-32e9e27eb72a | -10.00152 | -65.2881 | 2025-08-17 05:55:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20ba9742-95fa-30e6-9aa7-fb83d036b730 | -8.43369 | -70.7203 | 2025-08-17 05:55:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0195423e-eaec-3f55-9f48-1a02e1b23b19 | -8.87717 | -68.51466 | 2025-08-17 05:55:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e1cc87a-b72f-3fa3-b2aa-d7adc89f5e6d | -10.35396 | -64.50686 | 2025-08-17 05:55:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4df5660-6d6c-3078-bca8-65abd171d800 | -8.88377 | -68.51539 | 2025-08-17 05:55:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 763a7f9e-2db2-3891-a792-9b13e462f972 | -10.36245 | -64.50458 | 2025-08-17 05:55:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2e92a66-cf4e-3a6c-a441-b71957e246be | -9.50163 | -60.5319 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d609aefb-2a88-39bd-90f7-c5fdc8a7c886 | -9.04293 | -67.42614 | 2025-08-17 05:55:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f2d45850-5e29-3b9f-a2e5-8924547daa8b | -13.0134 | -56.85918 | 2025-08-17 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2e635af8-cf8b-3216-b8ad-9e59f367969a | -8.88049 | -68.51518 | 2025-08-17 05:55:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec15c750-247f-3509-8536-8f27013bb9b2 | -10.34426 | -64.47662 | 2025-08-17 05:55:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b0c7a64e-de05-392a-8991-cfc836f83f62 | -9.50786 | -60.53475 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b90595c9-7d51-3c2f-ab3f-2a8ab377ba5c | -9.04633 | -67.42667 | 2025-08-17 05:55:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1db9f589-d4a2-3e33-ae7b-fef8244ec6f7 | -9.49945 | -60.55897 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee49d7ae-8398-3f41-89ff-555a733a9233 | -8.87662 | -68.51817 | 2025-08-17 05:55:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96152fa3-0ad1-3168-bffd-69edd2e878a8 | -9.88404 | -64.27307 | 2025-08-17 05:55:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b1a6e2ac-51ff-3b94-8ad4-813215d20c82 | -10.24662 | -68.26083 | 2025-08-17 05:55:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97593999-ce7f-37cc-a23c-7864e9445ae6 | -10.34374 | -64.48016 | 2025-08-17 05:55:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 82c58cb1-c5b4-3eba-a0e9-c7bd0fa9d327 | -8.56805 | -69.6792 | 2025-08-17 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 99d0ac11-4263-3c0d-894e-14052c8e6dbf | -9.51061 | -60.55412 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ee3a627-0db4-327a-8cfd-540612e12a48 | -8.05898 | -70.58464 | 2025-08-17 05:55:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c0c31ec5-bc06-3c3d-8f9c-ee16cfdef943 | -5.44607 | -60.1418 | 2025-08-17 05:55:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4de8a754-8e52-336c-8e1c-d45330e8a3d1 | -9.73308 | -67.95654 | 2025-08-17 05:55:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 82a6ab02-8568-3b7c-9e1b-5c371897d583 | -8.87994 | -68.51868 | 2025-08-17 05:55:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb5f85d1-747f-3ddc-9f11-86f005a19a38 | -10.11036 | -67.17305 | 2025-08-17 05:55:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb57c136-9504-3d4c-8cbe-03b1f7f7ece3 | -9.49986 | -60.55589 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61527c33-5a82-3a84-bd9c-3bf791a5d71a | -5.45066 | -60.1454 | 2025-08-17 05:55:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1581f2f-1054-379b-92e9-260582449b83 | -8.87163 | -68.50663 | 2025-08-17 05:55:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9795cfd3-d065-3b7d-8122-fe0ec6ee214f | -9.50308 | -60.531 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 53569564-7277-3a1f-920b-620d4f625c74 | -9.3892 | -60.54539 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d9d04ca7-8a36-3d48-bd06-8ef0d20fca65 | -5.45695 | -60.13747 | 2025-08-17 05:55:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f36a9381-4bae-3902-b9a7-5a8cbe091743 | -8.8744 | -68.51064 | 2025-08-17 05:55:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c1e2f76-68d5-3670-b294-a524345ff3a1 | -9.50503 | -60.55656 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6123be43-5c84-341d-a636-ce8acd02e0ae | -9.9791 | -67.8568 | 2025-08-17 05:55:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 06497451-fd5b-3c15-bb16-8fdaf5b02bd7 | -5.45568 | -60.14612 | 2025-08-17 05:55:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c5c68d91-7197-3c85-9fd7-88aaf66b1a4e | -10.82299 | -68.24278 | 2025-08-17 05:55:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf342706-b050-3638-a48f-a48abcfb5a15 | -5.45235 | -60.13385 | 2025-08-17 05:55:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6a3376a-1211-3fdd-a9c9-e31d5f09c316 | -9.50267 | -60.5341 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0246ea04-45e1-3e9a-892c-0bee0d2fd459 | -8.35654 | -70.30196 | 2025-08-17 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2d0a9ad1-e538-3285-8dca-141d24ce8e1a | -9.51102 | -60.55101 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5632de58-e496-359d-8386-b215f8d30222 | -5.45652 | -60.14035 | 2025-08-17 05:55:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8f67683-79c5-391e-8141-525384a0d538 | -9.54235 | -63.57474 | 2025-08-17 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4f691c6-260a-3ec5-9f5e-d6b9aeb331a3 | -9.41459 | -68.55273 | 2025-08-17 05:55:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f38ef313-6d28-3cce-9fa1-1ca341cfebc3 | -10.23266 | -67.31593 | 2025-08-17 05:55:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1e7ee11c-22ea-3a6c-a292-7f92fd8c416f | -8.02919 | -72.50108 | 2025-08-17 05:55:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 65dcdd77-66c7-38db-ad82-55a988a004d0 | -9.88454 | -64.26951 | 2025-08-17 05:55:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce2bf562-2db1-31aa-94d8-e593954a4dab | -8.87495 | -68.50715 | 2025-08-17 05:55:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e50122f8-baba-3010-abdd-6cd7d13e6d56 | -10.1381 | -67.73064 | 2025-08-17 05:55:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75829250-e131-377a-8b9e-d87493c0c259 | -9.55077 | -63.66722 | 2025-08-17 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 17b15659-fa57-32a0-b70a-0641a64ea149 | -13.01123 | -56.86662 | 2025-08-17 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 07688335-c03a-3561-9dd8-0d041bac83b4 | -9.92808 | -60.46548 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 135df35e-766d-34f3-b6f4-63040501a403 | -9.49905 | -60.56208 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbd4a481-fe0c-341f-b9d1-05254176ebff | -9.54144 | -67.1636 | 2025-08-17 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f3826d50-ab3b-37f7-bd82-05ddf350dd02 | -9.50388 | -60.52475 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81bd4c45-e2d3-3162-9053-20d7e9b120eb | -9.51305 | -60.53542 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab26b4e5-41db-3f1b-b92e-3f99fe65e358 | -13.01192 | -56.86044 | 2025-08-17 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5c8deb8f-b6ef-354f-9ce8-95413e2eb865 | -9.51143 | -60.54789 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b235c055-fadd-3909-b330-0215e62de4c5 | -7.98119 | -70.03666 | 2025-08-17 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d77d2bc6-5b17-3030-8062-12388247241b | -9.51183 | -60.54478 | 2025-08-17 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e1d2240b-6b89-3ffd-89ec-7a0880285496 | -5.45193 | -60.13676 | 2025-08-17 05:55:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da307ecc-7071-3540-90d1-dab005b60f7e | -8.7879 | -69.64254 | 2025-08-17 05:55:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db8a22c5-f619-3aaa-9a4d-2463b03e016c | -8.87827 | -68.50767 | 2025-08-17 05:55:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 015a4510-05bf-3957-814d-859fed6e0f6d | -14.9819 | -54.7536 | 2025-08-17 06:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 67.0 |


[Clique aqui para ver as próximas entradas](README40.md)
