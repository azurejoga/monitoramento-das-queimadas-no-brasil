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

## Dados Diários - Página 147

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90ebaf9f-e7b8-36d4-86e7-46977715e20b | -8.63149 | -66.77814 | 2026-10-10 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca4a26b8-dfcb-3a06-8e64-b8e8f14acaf1 | -8.17758 | -54.71617 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b0583629-6f62-31ac-ab0c-cf1897e2cc54 | -8.18428 | -54.71713 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5ea35ec8-7e09-37dd-a9b5-e8b44f0c50fa | -7.91885 | -54.71339 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e97b8cf5-083f-31f4-82ab-2da2ad4d6311 | -10.61695 | -60.48652 | 2026-10-10 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9fde2729-d8c1-300e-b068-40837bdf712c | -7.22342 | -55.07785 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 11f980e1-575b-356c-bf5d-f2cc2a7fa766 | -9.0896 | -61.05054 | 2026-10-10 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d1e7b473-518c-34af-abba-367dbc17f3ee | -7.90399 | -54.72334 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 733ee09f-f902-3e31-a5c4-70e03d6cfe0a | -5.70957 | -63.15643 | 2026-10-10 05:50:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| beb82a4b-9502-3224-b48e-45c6d7205161 | -6.93413 | -59.24406 | 2026-10-10 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 01200566-630b-30a2-9e4d-f22a1ea34509 | -7.93367 | -54.73186 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 7d88d5f0-b0ea-3be8-a52f-3cf0bde64f19 | -9.51414 | -54.67603 | 2026-10-10 05:50:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b5c1074c-b689-3ce3-b68f-2910e645ff1a | -6.46093 | -55.49908 | 2026-10-10 05:50:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d02dcb9f-36ec-39c4-84aa-b6a1ad91c811 | -12.2905 | -63.3805 | 2026-10-10 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e60f723-09f4-38cc-8036-a81ab875f026 | -7.91215 | -54.71262 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 277aabea-d226-3c4a-8568-4896e9107edb | -6.49697 | -55.3193 | 2026-10-10 05:50:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 587f08bf-cff3-37be-891d-10c5d024d1c2 | -7.88852 | -63.77285 | 2026-10-10 05:50:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 934b5f63-961d-362b-93eb-2ec1af51b4ed | -8.50326 | -54.61429 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 302c5372-6c24-3a60-ab2c-5b1dea85fdd6 | -12.30262 | -63.36407 | 2026-10-10 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61a8b473-6c38-3ed1-a174-e95bbaa0e98c | -10.35733 | -67.97739 | 2026-10-10 05:50:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4f5d022-018a-3e2f-a703-a8b97b69c67c | -12.2986 | -63.36349 | 2026-10-10 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c15ad2b-d322-382e-a554-acee729fd8b3 | -10.60743 | -60.48508 | 2026-10-10 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| dc0c83d2-54a6-3242-9acd-f076b3410596 | -8.5018 | -54.60651 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 124b05ec-5b6d-344c-907e-bc3685ed9a11 | -12.24283 | -64.17752 | 2026-10-10 05:50:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 445967d4-54f7-3142-b1ed-c88d0ae7f222 | -8.5389 | -66.98225 | 2026-10-10 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d79de59-df4c-39b1-af41-fd0b0b1ea692 | -7.24282 | -55.08098 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| dd6f160f-0e84-3d51-ac29-13e0e8d3fc2b | -9.25254 | -62.30824 | 2026-10-10 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1cdf2fbd-531f-39c1-88e0-58895cd80977 | -9.25308 | -62.30445 | 2026-10-10 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5374dc52-f590-38ae-a7cd-f57448d7385b | -8.66649 | -67.12354 | 2026-10-10 05:50:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72a713ef-9f5f-34e7-bfda-c1f1c505cbb9 | -7.49783 | -55.00063 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 7dc23b7f-7a62-3d2b-a354-618c1a4cfa25 | -10.61219 | -60.48579 | 2026-10-10 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b14399fe-c63e-317b-99ed-756781db8626 | -7.50436 | -55.00156 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| cfb00fba-b5d0-3a95-a9f8-a125f571e36f | -7.88787 | -63.77726 | 2026-10-10 05:50:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d532d02c-ea90-39e9-bb6b-e6ce6cee2438 | -9.74253 | -68.44625 | 2026-10-10 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 77dbc48c-6154-353b-ac21-9792e952701b | -7.09975 | -55.73364 | 2026-10-10 05:50:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1630792-8ae9-390c-a88a-337584fbdb3d | -7.49809 | -55.00373 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 4eaaa688-7160-3412-9378-d132b8448ade | -10.60674 | -60.49028 | 2026-10-10 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 708fe0db-efce-3c15-9399-6c7b84f515cf | -7.93077 | -54.72655 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| cdd7de42-cffb-380a-ad56-e538204ba2b8 | -10.55444 | -68.02287 | 2026-10-10 05:50:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c3011d37-3b59-3481-a7ca-f25a4f91aea4 | -7.45485 | -63.64369 | 2026-10-10 05:50:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2865b4a6-9763-3540-bf95-63fd505a9960 | -8.653 | -54.53323 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fe770925-9cd2-38ee-861d-b68dd2434272 | -6.94142 | -59.24868 | 2026-10-10 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 90112ad3-ac56-345a-a6fb-8579d40595e5 | -7.91737 | -54.72503 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b20ea194-6102-30bc-ba41-c81424891b7b | -7.4988 | -54.99835 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 14e8e936-4c58-307b-b032-5464d2751628 | -7.21767 | -55.07127 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| e3bf1a0c-0c09-3cf4-b5d4-59af43048444 | -7.08732 | -55.73182 | 2026-10-10 05:50:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18bd1675-2425-3f3a-bba0-b07712f33a09 | -8.59144 | -67.03684 | 2026-10-10 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5199a620-2a5d-3c0e-aada-9df748fecd8f | -10.60813 | -60.47989 | 2026-10-10 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1e922221-396d-31df-942e-8ce6337a5067 | -6.94177 | -59.10503 | 2026-10-10 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 43126b4f-be0f-3aaf-9828-9a1ff5df224a | -6.6467 | -55.33075 | 2026-10-10 05:50:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c9e1c4bb-0141-38bf-8fa7-4ff8d1d1ba22 | -9.67987 | -68.67008 | 2026-10-10 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7b511878-874b-33a1-9b86-24464e6993d8 | -9.96308 | -55.33361 | 2026-10-10 05:50:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4f882ba1-6bed-3c8c-9892-1ae440b36075 | -10.61351 | -68.68468 | 2026-10-10 05:50:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 546a3713-929e-3a7a-95c3-1197f9e2b2b9 | -6.9937 | -59.10301 | 2026-10-10 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d028d8d9-d3dd-3083-ad73-eda298fc0349 | -7.57123 | -61.54325 | 2026-10-10 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f29dd69f-cd88-3064-bc75-3ce12628640f | -8.48831 | -54.60424 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3ce7386a-5e59-3555-9bb5-45e569859382 | -6.44982 | -59.95169 | 2026-10-10 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6433f84c-1eae-3109-aecc-2d0cd4727fd7 | -6.2828 | -35.05175 | 2026-10-10 05:57:00 | AQUA_M-M | VILA FLOR | RIO GRANDE DO NORTE | Brasil | 2415008 | 24 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 1928581c-9f60-3d31-ac24-c34d8b9a3500 | -4.66529 | -42.85637 | 2026-10-10 05:57:00 | AQUA_M-M | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 36.0 |
| fdde6bd6-54fd-3b04-bb5d-aa2dfb8773f6 | -4.67902 | -42.83348 | 2026-10-10 05:57:00 | AQUA_M-M | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 953dfe76-29f9-3f64-88e7-037b615de6f6 | -5.06425 | -38.01566 | 2026-10-10 05:57:00 | AQUA_M-M | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 1ad7940b-b093-3eb5-83d0-ab055912f405 | -6.28142 | -35.06068 | 2026-10-10 05:57:00 | AQUA_M-M | VILA FLOR | RIO GRANDE DO NORTE | Brasil | 2415008 | 24 | 33 | nan | nan | nan | Mata Atlântica | 26.5 |
| 0a83ec88-67fa-3ba5-8b32-6053db061d12 | -7.21096 | -34.90209 | 2026-10-10 05:57:00 | AQUA_M-M | JOÃO PESSOA | PARAÍBA | Brasil | 2507507 | 25 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| e4f751ad-c96e-3d51-8aed-b38d92c4f3e0 | -4.67371 | -42.86523 | 2026-10-10 05:57:00 | AQUA_M-M | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 82b088eb-afcf-3d12-a18b-7faeb99f939b | -17.46245 | -45.09061 | 2026-10-10 05:59:00 | AQUA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 30.0 |
| aea0fd58-9a19-3e59-98af-099c8aeaf12c | -13.09583 | -46.3707 | 2026-10-10 05:59:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 4c37d3d5-96fa-3ea2-8087-b1c18b778558 | -10.89226 | -44.8215 | 2026-10-10 05:59:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 281989b4-a1ba-36fa-9d2d-fcae35835435 | -10.90272 | -44.81651 | 2026-10-10 05:59:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 6ed81b1e-9485-38d9-9a08-64f8f96186dc | 4.8521 | -60.26814 | 2026-10-10 06:22:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dabae40b-20f8-386d-94c8-678fa20cae5f | -2.05909 | -61.14206 | 2026-10-10 06:22:00 | NPP-375D | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a41d536-335d-3e72-a5c4-a913453f7e40 | -2.02145 | -61.27045 | 2026-10-10 06:22:00 | NPP-375D | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05025a0e-ec11-37d8-b774-e416db79da7d | 4.27602 | -60.89315 | 2026-10-10 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf01c382-03d3-32f0-b9c6-6c265a37410e | 0.00451 | -60.57977 | 2026-10-10 06:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d37a9b72-56f3-3715-8104-23b33de35efe | 4.8574 | -60.26612 | 2026-10-10 06:22:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 524e4315-798f-39fe-a74a-6f7b6126962f | 4.26918 | -60.88683 | 2026-10-10 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82f093a1-b949-3234-9427-96cbe7a40f34 | -2.05979 | -61.13764 | 2026-10-10 06:22:00 | NPP-375D | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1590408c-c67f-3dd2-8431-ddc1f0807f6f | 4.27539 | -60.88949 | 2026-10-10 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75538032-d5a6-3ee2-9f26-37119eaae540 | 4.85151 | -60.26643 | 2026-10-10 06:22:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ba6c964-cc6e-33d8-84c2-84e5e389aed4 | 4.28485 | -60.91111 | 2026-10-10 06:22:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 196fc985-1d02-360f-a164-3b93ce2b607a | -2.02212 | -61.26599 | 2026-10-10 06:22:00 | NPP-375D | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6988d26-a6e9-3c11-9cad-2d1032d1161b | 0.00381 | -60.57525 | 2026-10-10 06:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48fd904b-1727-3bc9-aa0f-58067aba190b | -2.05972 | -61.13868 | 2026-10-10 06:22:00 | NPP-375D | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 62353306-3514-3370-b56b-a5008ac3e253 | -5.06877 | -60.22073 | 2026-10-10 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8c9580f9-0b4f-3da4-89d5-d2dbec798f87 | -6.93042 | -59.26164 | 2026-10-10 06:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| acc9a87e-94cc-3bf3-9431-e4df36b238d9 | -8.52164 | -67.02562 | 2026-10-10 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3829e199-2aea-3f7f-a0f3-41a87775ff8f | -8.53387 | -66.97226 | 2026-10-10 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 17972caf-720d-3f7f-9971-0121a1603e1d | -9.26696 | -67.93676 | 2026-10-10 06:25:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a0f9fe9-250e-3c75-8d5e-f2569b6f56bb | 2.01525 | -61.09155 | 2026-10-10 06:25:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6be3c9a-4787-35b1-9166-76d946325bdc | 2.01592 | -61.09548 | 2026-10-10 06:25:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d2eccdc-83bc-3106-8fd4-1dc31d38cca7 | -5.06958 | -60.21491 | 2026-10-10 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e7c51c6d-cc07-3dcf-a0bc-f6f1fad72e3c | -8.4239 | -70.12252 | 2026-10-10 06:25:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87a7d10d-9ddd-39a6-a6c9-40bc40c1941b | -6.94293 | -59.10366 | 2026-10-10 06:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 451133e7-6978-3aad-881f-797e135e4e51 | -3.02932 | -59.16111 | 2026-10-10 06:25:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 615c0e70-a720-33ae-a892-8f48f9fe21da | -3.17031 | -58.62415 | 2026-10-10 06:25:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1b53d02-28bc-30aa-b6ae-7533a1bc3052 | 3.04401 | -60.53574 | 2026-10-10 06:25:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c24defd9-0342-3dee-b0be-f11efd35966e | -3.98932 | -59.36081 | 2026-10-10 06:25:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13db5e19-f1ab-3e7a-9b62-6f0fcf29970a | 2.72684 | -60.25951 | 2026-10-10 06:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 4206e2b0-6d55-3d4b-940c-f561844c2488 | -8.53773 | -66.97746 | 2026-10-10 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3d1f5545-9310-3bb7-8c22-5302d0a5046a | -8.68619 | -62.40509 | 2026-10-10 06:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 94efdc91-c15f-3d35-b8ed-88ea2e24cbe7 | -8.62649 | -66.78104 | 2026-10-10 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README148.md)
