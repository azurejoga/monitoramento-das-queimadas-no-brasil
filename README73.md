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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa731cfd-4f58-347c-9771-0ea43f479b6e | -10.48534 | -64.50962 | 2026-08-30 06:14:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61989162-2186-35b5-81ac-2d694f596783 | -9.1763 | -59.61658 | 2026-08-30 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee3f2bb0-63eb-32c0-bf71-f3563c859541 | -7.45797 | -70.13208 | 2026-08-30 06:14:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3af06a5-ff38-35ce-8c5e-c09074337d67 | -8.65267 | -62.84061 | 2026-08-30 06:14:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d6f862e-f807-3766-89e2-3a049da6c5bd | -8.9977 | -65.43707 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82dff516-36a9-3944-bd63-29125cd41640 | -8.91578 | -66.94947 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b238396-2b48-34c7-87a2-f20d0ca31312 | -9.71076 | -60.74197 | 2026-08-30 06:14:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 62257cdd-6fdb-3787-ae12-c7dbb7bf7013 | -9.04708 | -65.41971 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 13308c74-3921-333c-964a-c4a49b19c61a | -7.55626 | -61.31612 | 2026-08-30 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a325e88c-ea0c-3c03-9a6c-d13bb1484db9 | -9.89514 | -60.27869 | 2026-08-30 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 3fb0e6be-1656-3703-b164-f695528db0b9 | -8.62852 | -66.54306 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3bdeebbd-45a2-3dbe-b90c-97fff7896a97 | -7.57649 | -61.30106 | 2026-08-30 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dba73dc2-7303-3d05-a8cf-652e3ccaa858 | -7.29707 | -60.5996 | 2026-08-30 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 04f894ab-2c06-303c-9733-6389a688452a | -7.27175 | -72.72929 | 2026-08-30 06:14:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c961e768-62ba-35a1-9581-a0172255d519 | -9.03863 | -67.62423 | 2026-08-30 06:14:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5015c0a-f31f-3b4d-99e5-741ac6475546 | -9.17702 | -59.6105 | 2026-08-30 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67a16bc2-c518-39e0-bf79-5664b2a00500 | -8.65219 | -62.84417 | 2026-08-30 06:14:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b2e423dd-0fde-3a6b-8ab8-cb7aae549402 | -7.23666 | -60.62584 | 2026-08-30 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e9b5c16b-e0c7-3958-ad7e-f806921ce800 | -8.55441 | -70.26508 | 2026-08-30 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aacabccd-aef7-3ceb-9fab-7470d7a12116 | -9.0719 | -60.48421 | 2026-08-30 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f957b589-b44b-3d10-872e-980f73f73e29 | -8.91163 | -66.94887 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3480950c-6216-3bba-9ee8-b16f40c82f84 | -9.93757 | -60.53015 | 2026-08-30 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2552a4b7-2a1c-37f6-8ec3-96d416ffda9f | -9.93372 | -68.55512 | 2026-08-30 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 703ed3de-921a-3f5f-8906-e55c57a92688 | -9.89339 | -64.98788 | 2026-08-30 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 47ec73e0-2bb8-32eb-b4de-075924d4dd06 | -9.00165 | -65.44247 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 35e4b054-c0bf-3e16-99da-cfd04aeb7162 | -7.30715 | -60.60791 | 2026-08-30 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 28934a99-0a8c-3284-a7b2-935ac9787606 | -9.05372 | -65.40595 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a030016e-7d04-37f5-9070-cb482738939a | -8.93129 | -67.36245 | 2026-08-30 06:14:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 4d53f25d-a701-336f-abf8-d45627779933 | -8.57894 | -66.95216 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 211ef9fb-88a5-33b5-a324-39b4d7355113 | -9.05237 | -65.41557 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 47bc3177-0d03-30b4-b7d7-bd3b66b37547 | -8.96098 | -62.4131 | 2026-08-30 06:14:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 32e03438-0261-3c3d-be66-e8e1bf458be0 | -8.95684 | -70.81602 | 2026-08-30 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6d56809-6fed-3944-b571-71aad94e06d6 | -8.25888 | -62.75904 | 2026-08-30 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b1023b8-5484-3db6-aa29-929c6e0d3053 | -8.91056 | -66.95638 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a9f9952e-55ed-3641-8760-419ad5645a0c | -9.71211 | -60.73148 | 2026-08-30 06:14:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 32417360-8eea-32a9-82fe-f461836e157a | -6.86238 | -59.47221 | 2026-08-30 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| dae9df6a-1564-3c66-a9aa-02e66b7f881a | -9.71287 | -60.74783 | 2026-08-30 06:14:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 71bc605f-50c2-3334-898e-a47b8de23042 | -7.39692 | -60.58899 | 2026-08-30 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a1b9847f-71da-3c5f-93a3-61cd5cadc38f | -8.60659 | -70.21864 | 2026-08-30 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7aff9557-fc56-3a2b-89a4-0347424696f0 | -8.95775 | -62.41551 | 2026-08-30 06:14:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86f4e431-362b-3dd9-b4be-68f2c6fb43d8 | -10.49304 | -59.61666 | 2026-08-30 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 141bb34d-ab93-311a-800f-7a5fbe19beb1 | -9.04261 | -67.62479 | 2026-08-30 06:14:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99129b53-dbb2-34a5-bbdd-39f849bc74d5 | -8.25389 | -62.75486 | 2026-08-30 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2001a5ae-3bf2-3962-ade0-83f0097c4107 | -9.89252 | -64.98936 | 2026-08-30 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| df19d79b-d875-390d-a2c4-eb400bd8e29d | -7.29773 | -60.59483 | 2026-08-30 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6f51f8f8-590a-3e60-81ce-7b8e9b307f9f | -9.84219 | -60.27711 | 2026-08-30 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e6ce656-e57b-32f3-8866-f1fe996d2f78 | -8.60428 | -70.21052 | 2026-08-30 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5985e945-2915-321a-9576-78a9b4f511b6 | -9.05834 | -65.40661 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 82d3f045-a1ba-3959-9921-345f6436bd12 | -9.92119 | -67.87994 | 2026-08-30 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef99a36e-9b54-323a-8681-80998bd78bf4 | -9.01151 | -65.40498 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bcc389ad-ad40-329f-9e83-fae5b185e520 | -7.85293 | -72.28082 | 2026-08-30 06:14:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b766a84b-be12-321b-ade9-c8e6785ff148 | -7.40484 | -60.58715 | 2026-08-30 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 24d5a436-9be0-349e-99ee-c5d2f88ab7fe | -8.60371 | -70.21432 | 2026-08-30 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05dc1f59-4455-3bcd-8b93-aa27d3e0296e | -6.86162 | -59.47779 | 2026-08-30 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d43213a7-7c42-32de-b0f4-ccc389921177 | -8.60486 | -70.20671 | 2026-08-30 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 29d8523b-d645-301c-b91a-542ce6027e3a | -9.04713 | -68.51538 | 2026-08-30 06:14:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7647eb78-2e7b-3eb1-a705-663b13f7d51b | -7.6298 | -61.33353 | 2026-08-30 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07196bde-2cfb-33ad-ab90-900ee5bea20f | -7.5628 | -61.31252 | 2026-08-30 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 04b264f3-86ac-3dd8-b8b2-1790a586f6df | -9.15888 | -59.51356 | 2026-08-30 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 645aea44-996a-3c34-a75d-a6f84169f2be | -9.89583 | -60.27297 | 2026-08-30 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 82c2d1d8-1984-331e-a434-779724fe5a06 | -9.71279 | -60.72623 | 2026-08-30 06:14:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3f36f6b-43b1-3ca7-81ca-d67188b1ac38 | -9.93885 | -60.51944 | 2026-08-30 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 82e04064-9fa9-3cc8-ba02-0839dafec715 | -9.03207 | -68.51313 | 2026-08-30 06:14:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63ecb850-9bc4-3ebd-b7af-04ef00eca329 | -9.93383 | -68.55727 | 2026-08-30 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 99fd5ece-1d1e-3bc8-96ef-4be6ff3308be | -8.95218 | -62.37164 | 2026-08-30 06:14:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f3270523-95c2-3b4c-afce-d499fabd1a77 | -10.48098 | -59.61028 | 2026-08-30 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 911da82a-9420-3050-9173-2b769b6fc11c | -9.04776 | -65.41492 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 90d44bbc-657f-3730-8f45-8650b3961281 | -8.8819 | -71.25942 | 2026-08-30 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 61773053-e159-3439-ba84-6c96c844e504 | -8.57482 | -66.95155 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1972db92-6620-352d-b21d-bab9097db6ca | -8.81931 | -70.6376 | 2026-08-30 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a0f36e1-5a56-34f1-8018-97fc91785c42 | -7.30651 | -60.61273 | 2026-08-30 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 96213ccb-9341-3278-bc63-4df241ffb3f1 | -9.38702 | -66.51318 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 38feba02-3545-350c-8e3a-42df1a8702dc | -8.73685 | -69.56676 | 2026-08-30 06:14:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55debd36-da74-3538-8ff4-fde293399c2d | -7.30589 | -60.61747 | 2026-08-30 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 258d956e-367a-3e35-9b43-b46e7b5dcb92 | -8.64026 | -62.85006 | 2026-08-30 06:14:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a312c8a0-c4c3-34f6-a955-e1e2c1117fdb | -9.93818 | -60.51673 | 2026-08-30 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| eb23f8fd-f493-34c2-9249-54b3f48b2402 | -9.88771 | -64.98869 | 2026-08-30 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d3f47afc-85cb-3ab5-90a7-f6bd068d6ad2 | -7.57709 | -61.2966 | 2026-08-30 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ba3d43b-af05-3ac3-b27d-11a2b39846c1 | -7.29663 | -60.59185 | 2026-08-30 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b66f77f1-8a5e-3f3c-b106-111dab394736 | -9.7091 | -60.72587 | 2026-08-30 06:14:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 085919db-de8f-3492-b1d6-8ec23e735093 | -9.05169 | -65.42036 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ac193bd3-5d6e-3152-b7d5-a191a70689de | -8.25936 | -62.75556 | 2026-08-30 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8fcd1c26-7dd5-3b71-ac5a-c2b44999e21a | -8.96498 | -62.4047 | 2026-08-30 06:14:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6e35f4d-a8af-397f-8a42-cd11acbbf5eb | -9.03541 | -67.61846 | 2026-08-30 06:14:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18df97a5-072a-337f-aa1f-a3f5c43cbea0 | -8.80881 | -67.28706 | 2026-08-30 06:14:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a26d2cf-28aa-3885-9b21-100bb48fbbdd | -8.60773 | -70.21104 | 2026-08-30 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06ae1a66-9a4a-3370-b995-ae61b3dd8096 | -9.70718 | -60.74158 | 2026-08-30 06:14:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 97dd47d7-b007-355c-a879-1f8794da55f4 | -9.16565 | -59.51455 | 2026-08-30 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9c019824-c512-3917-90cd-af416eaef3d2 | -7.5509 | -61.31091 | 2026-08-30 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c6f839a7-2330-3eb9-9cee-ce78ce5e2314 | -8.8961 | -71.41116 | 2026-08-30 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ace1f74-4b27-35c2-ae76-02deba559865 | -7.39815 | -60.57967 | 2026-08-30 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1ecebee1-5338-3cd5-a29c-8beec6b6c9b7 | -9.06227 | -65.41206 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c70a808b-7d76-37d8-aa4c-f13fba360912 | -10.57144 | -59.61498 | 2026-08-30 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3f677832-937c-34d3-8a94-a9d451c5f8a0 | -8.95828 | -62.41166 | 2026-08-30 06:14:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c535a4d1-e47c-3a19-ba05-505aafd35036 | -7.40376 | -60.58516 | 2026-08-30 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6e30c7d6-310f-3201-8f36-7450ce402723 | -9.84873 | -60.278 | 2026-08-30 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57229b51-315d-37ad-ad17-600f1f51af02 | -7.31273 | -60.61348 | 2026-08-30 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e7c35ecb-8969-31c5-a94b-b4811789238e | -9.0056 | -65.44788 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 092daede-14e5-3150-8b52-6058f12fcfb7 | -11.44088 | -61.48789 | 2026-08-30 06:14:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 252b7ba9-96e6-3adc-839f-eab92b4317d1 | -7.30095 | -60.60707 | 2026-08-30 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README74.md)
