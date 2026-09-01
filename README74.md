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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c8f6e04-1652-35da-bbd2-8aca6b9a8471 | -5.25159 | -55.91571 | 2026-09-01 05:33:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2540f763-bd0c-3e35-899d-a482de65126a | -3.06908 | -61.22185 | 2026-09-01 05:33:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 22912736-8d5c-3c16-93de-8a4a4455030f | -3.12747 | -59.00167 | 2026-09-01 05:33:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b158b2e-1da8-3bdf-8584-de4bd69b0d17 | -3.62094 | -60.56276 | 2026-09-01 05:33:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9ca8e870-3869-368d-b49c-650578c45471 | -3.13371 | -61.17932 | 2026-09-01 05:33:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e48bb231-bf41-3e96-855a-4e450ab40e85 | -4.95578 | -55.84692 | 2026-09-01 05:33:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50432a48-307f-37a9-92ee-3355e4bbaa32 | -3.62039 | -60.56629 | 2026-09-01 05:33:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f57f17f2-0d0f-3bcc-9608-84f7c599114c | -4.22299 | -59.86608 | 2026-09-01 05:33:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c7a75de-8c71-372f-98b9-d8931ac18b07 | -3.62819 | -60.56027 | 2026-09-01 05:33:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cac3b628-ddcf-3a9b-b6f7-0087b995c9b5 | -3.12709 | -61.17828 | 2026-09-01 05:33:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d6c1ec7-9850-314a-8fd8-0d28101349d3 | -2.92612 | -59.31166 | 2026-09-01 05:33:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 623190c5-f677-3d05-996b-3f6a40d5ec99 | -3.90549 | -59.65411 | 2026-09-01 05:33:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87d2c848-d7a9-3790-89ff-535129626089 | -3.34237 | -59.42755 | 2026-09-01 05:33:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6aa5a7c6-0482-30b4-92b9-b1e77edea922 | -4.1553 | -60.70679 | 2026-09-01 05:33:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a392b20d-76f2-38ef-9910-fded6a432a34 | 0.20018 | -51.5252 | 2026-09-01 05:33:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75a395a5-d525-31bb-9134-d47f3765ba9c | -5.25346 | -55.90313 | 2026-09-01 05:33:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9b2fbc44-9c39-3524-a620-2902c498991c | -3.06631 | -61.21788 | 2026-09-01 05:33:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| abc101f1-82b5-3ae5-90e2-86066d5b1d26 | -3.5129 | -56.31924 | 2026-09-01 05:33:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9fc8b158-4bac-3225-8894-0385ea2e8926 | -3.12169 | -61.23397 | 2026-09-01 05:33:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f429aa69-ed12-3978-be1c-f260acdf3d76 | -4.15699 | -60.7179 | 2026-09-01 05:33:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8335e1be-1eca-3d38-8ee0-1ea477dc1723 | -3.11452 | -61.23638 | 2026-09-01 05:33:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| be4cfeac-025a-34e5-b2ac-133ad026c503 | -3.07042 | -61.04168 | 2026-09-01 05:33:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ddce59aa-ed33-3b9b-be94-aa28b86c9cd1 | -1.46326 | -54.23706 | 2026-09-01 05:33:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b96e5c1c-7cfa-38a8-b9ac-4ff12d5d3307 | -3.09684 | -61.21949 | 2026-09-01 05:33:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 85d2a341-2e62-32af-a59c-1dfe3d8aa9fd | -3.60835 | -59.07196 | 2026-09-01 05:33:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b0e35f6-63cb-332c-97e8-3c9027961d09 | -3.62484 | -60.55974 | 2026-09-01 05:33:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3e5d8ba6-4006-3140-98a2-5e441e324a47 | -4.1017 | -60.66239 | 2026-09-01 05:33:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f37543f-3691-3fff-8063-647ed5ba70e3 | -3.63044 | -60.56785 | 2026-09-01 05:33:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e080f24-30ac-3940-bd18-bf821498c2f5 | -4.15923 | -60.72547 | 2026-09-01 05:33:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5567d9ff-0034-3e7c-9d8a-47f6645ef549 | -3.51135 | -56.31846 | 2026-09-01 05:33:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 040b8a12-775e-3dcb-a5ca-b53c445715fa | -3.63458 | -59.55211 | 2026-09-01 05:33:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0191864-c590-3976-b02c-928b652e3d6e | -4.22642 | -59.86661 | 2026-09-01 05:33:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75bd593c-5bf9-39f8-80c3-8f8569313b99 | -4.96015 | -55.84746 | 2026-09-01 05:33:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c18c3c00-62d6-334e-a2ca-848b3f43fce6 | -1.37983 | -60.2577 | 2026-09-01 05:33:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ea31288f-3df3-3bed-8d64-80b1cac62e68 | -3.59885 | -54.5518 | 2026-09-01 05:33:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e56fb52e-6a6d-356c-b345-3f8718f9dc28 | -3.2595 | -58.24157 | 2026-09-01 05:33:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1d38b49f-bb5b-37f2-af64-53e926bd422f | -1.47296 | -54.23064 | 2026-09-01 05:33:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1f9b397-bc93-33e8-98d8-af84b86926f4 | -1.43983 | -60.26704 | 2026-09-01 05:33:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3eed8548-de2a-3630-9429-4977e3195fed | -4.9726 | -55.85342 | 2026-09-01 05:33:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| de8638b9-a60f-3518-82c7-6d05f5fab0f4 | -6.94804 | -55.63087 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9e2dd4d9-d17a-3656-a435-9f57091a0d1f | -8.5841 | -66.97717 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 34c9abcf-aa00-30a2-abd0-2fe47948641b | -8.96198 | -62.40783 | 2026-09-01 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c887fd7-ded3-3ad5-9533-3a358b58543d | -9.13748 | -60.53439 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01479e2e-220a-39ff-bbce-220197882fda | -8.79978 | -62.48948 | 2026-09-01 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a9f79c4-76bb-36f2-8bea-bc992f59ee21 | -7.56267 | -60.45981 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70b0ac0c-3da6-3d37-b876-3292efd692bf | -7.47959 | -61.38127 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6619bc99-725a-3ed5-9ffd-d5963015eee2 | -9.02997 | -65.42845 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4fe18b04-6966-3893-8dd2-849c83e6e4e3 | -8.78762 | -62.4804 | 2026-09-01 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 096c26e7-aa9d-36d4-bc9b-eb1c61a32524 | -6.83964 | -59.45599 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b91e3761-4dbf-3c12-a476-42177ce2365c | -9.06306 | -60.48315 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 419a57e3-3f57-33e5-8bb1-27f9cda98b58 | -7.5303 | -61.37743 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3254e06d-f78c-396c-801e-d94a60aa8e27 | -6.261 | -55.42587 | 2026-09-01 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 02a13593-17e4-39b5-953b-d3fdf68629a7 | -9.59266 | -60.51225 | 2026-09-01 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebc65379-09ef-39ad-856b-2bd370e79c63 | -9.02887 | -65.4565 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4b1421a-c736-3b95-a455-411e622b2a46 | -5.9512 | -57.68779 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6938ee59-2f34-3366-8bfb-a96978476704 | -6.93783 | -55.63122 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f942917a-5772-34e9-b923-4e46a5f2458e | -9.8915 | -60.28037 | 2026-09-01 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d01146fc-60d8-3e55-ab64-64fd184c763c | -8.11746 | -54.96854 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| dede5f20-2bd6-3ca0-a07a-21ec615dfd7d | -6.74637 | -55.66694 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5408b1c7-3c91-3467-bd23-cf7c94e7a86d | -7.73604 | -55.22196 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c2c7dcc8-8dca-3819-96c6-6e71217e465f | -9.93003 | -60.48283 | 2026-09-01 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57a6112e-ec87-3ce6-bae7-6dfdbb229700 | -7.31619 | -61.14683 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4114101-317f-3361-8168-13eb9bb3d4ef | -7.57014 | -60.48031 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ffd48ebf-92b9-3936-8367-963ccabcabac | -11.30534 | -50.57237 | 2026-09-01 05:36:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 06dc8b00-3f9d-3a7d-a33d-073d7828e505 | -6.92805 | -55.63453 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7784da1f-1517-3947-beba-a2a1fdc47b94 | -8.95088 | -62.37024 | 2026-09-01 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 020c1c6f-6cfc-3bc2-9d72-3dd626f6a261 | -9.45324 | -67.45406 | 2026-09-01 05:36:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 590b3d87-bb09-32e3-9164-e386ef704822 | -11.2498 | -54.01114 | 2026-09-01 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 64f1f613-6b6d-388e-80a2-e17c4fb5e619 | -7.18789 | -60.69029 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 905162f3-9f16-3634-b6e1-15db896b6787 | -11.25396 | -50.57631 | 2026-09-01 05:36:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b26aa79d-9fef-3a42-aca0-7c06b45116b6 | -7.35501 | -60.58274 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a9bc306b-8e9e-31bb-acc7-19ff0cdcc9d2 | -8.5858 | -54.77486 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f195937-fb4e-35b3-ad66-cd07470f2703 | -9.1903 | -59.447 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f553bd3-2430-39cf-bdaa-c812194c71aa | -6.36222 | -56.00178 | 2026-09-01 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6066924-3261-33ad-b6e2-2275c5018a41 | -6.7753 | -59.43029 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 232c6215-b232-3391-838b-dee6a800382a | -6.95585 | -55.64148 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 2187cfde-b8e5-34c4-8f7e-0d35f85a9750 | -6.00269 | -57.8288 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9732211c-ff7b-338f-8422-0cdaba6943f0 | -11.26815 | -50.57187 | 2026-09-01 05:36:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6614370f-fd06-3acc-8e8a-41541d7b838b | -7.3453 | -60.5774 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 881ddb15-dbd0-3af0-a50d-4b0a820bf46c | -6.95398 | -55.6478 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 64ceb30f-9670-3975-b978-4e6c1c81495c | -8.79649 | -62.5104 | 2026-09-01 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a6fc53c-cb2d-3458-af83-d106abf11cd3 | -6.15401 | -57.77838 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 094215ec-1372-344c-be75-90318879865e | -7.68049 | -55.34262 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b356b579-7116-3bcb-82a0-8594f12a97ea | -9.47178 | -57.02569 | 2026-09-01 05:36:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1bebb3a4-e699-32c8-9b55-8ea058f1aeb3 | -6.88086 | -59.44972 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c86c92b-c864-331e-89b1-6fdfe519574f | -8.12948 | -54.96319 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 69a2a846-134b-3fa9-9431-6db68b6919d2 | -6.96041 | -55.64206 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 63637c01-f67a-34a7-b30c-bfc0ba61cfd0 | -8.40528 | -62.66507 | 2026-09-01 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba8930ef-3db5-399b-a936-2b636bb648df | -8.1223 | -54.96927 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bd6154b6-d66e-335a-b405-065a6e6f3431 | -9.08317 | -65.49792 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82c40adf-2322-331b-9aef-86d32adccb77 | -6.94739 | -55.63554 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 31cc0912-4b64-304a-a623-2e056f5386ea | -7.91446 | -61.33461 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e85ed734-0e6a-3e88-9217-36f510e10490 | -6.78336 | -59.47339 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0c817131-547b-322e-9dcd-ea6867ddd64e | -7.5572 | -61.42543 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a6423d0-4d4a-3c3c-bcaa-e3b30e3c0667 | -8.69197 | -62.93595 | 2026-09-01 05:36:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d274ecc-a301-329a-9a8e-008fcee1b4cf | -7.59084 | -60.46033 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7e85f54a-d25c-30c5-af33-0420ef5a1c86 | -6.10525 | -57.86596 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4e530816-1691-3582-bc05-4b20b7be0682 | -7.35279 | -55.19775 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 812d1e4f-4410-3131-92fb-58bf2e73008f | -9.79981 | -59.43717 | 2026-09-01 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f1585e1-5194-3899-b8fa-c26efa0f6bff | -6.93395 | -62.88152 | 2026-09-01 05:36:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README75.md)
