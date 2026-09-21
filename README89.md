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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a61a52f5-c699-3e5a-b275-5d8c2864ee80 | -1.32989 | -54.66124 | 2026-09-21 05:40:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98d28b8a-c58c-3bee-8d96-b8f7b06b42c0 | -3.07303 | -61.27622 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9b29df6e-5f64-3175-ad5f-b807bf31559d | -4.34446 | -55.66693 | 2026-09-21 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| af8607a4-e7af-38a8-8b8e-cac137aa02c2 | -3.44601 | -50.60647 | 2026-09-21 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e34c60f2-34e4-36d2-b256-ce3a8f3d20e3 | -3.18198 | -60.65366 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 746b78d0-5144-3d4d-8ae7-b7f80d5bc2be | -3.28745 | -57.86674 | 2026-09-21 05:40:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6f95d081-b0f4-3fca-a397-556efa31f29b | -4.35179 | -55.64772 | 2026-09-21 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7262aed0-098a-35f7-bf1c-f5e1e87ba73d | -3.00435 | -54.16617 | 2026-09-21 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e73d1942-eff4-3cdd-b649-de7648be4679 | -4.046 | -55.71237 | 2026-09-21 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa229250-5182-3403-9f15-ee84d784617a | -3.60021 | -59.01484 | 2026-09-21 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0ffe4877-4ae7-33f0-a063-0c7cca33dca9 | -3.66353 | -58.86386 | 2026-09-21 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3cb39f3c-ddf7-33dd-b865-d02537a84b54 | -3.06694 | -61.27172 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 80ecc588-3712-3ccc-b355-8c7c0a8a5268 | -3.1896 | -60.43222 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| db5e08aa-157e-3de9-938e-31a829507567 | -4.34998 | -55.65967 | 2026-09-21 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ddada8cf-0250-38b5-9a78-5d150bec5dd9 | -3.10828 | -61.4161 | 2026-09-21 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3deb1336-bf97-3f01-97a0-d3de1bbeab2d | -3.14761 | -58.63908 | 2026-09-21 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06a8d516-e00c-3a20-a7b9-a021f56c3349 | -2.91474 | -57.78789 | 2026-09-21 05:40:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 56867b4a-5251-398b-9c67-30c354834bda | -3.06971 | -61.2757 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d64dbbce-153a-3a75-aa75-3252611035af | -3.71588 | -60.54995 | 2026-09-21 05:40:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7b15fa7-c8f2-3e2a-b0c0-4393609ca093 | -3.42858 | -59.26484 | 2026-09-21 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7e492a3-72cc-3b0c-80e7-240894cae14a | -2.90993 | -54.18708 | 2026-09-21 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8b9d041b-1137-396a-b6ce-b4597b6e9c36 | -3.75725 | -59.41807 | 2026-09-21 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a459fbcc-5aea-37de-b997-fb690bf21bc1 | -3.69356 | -60.58253 | 2026-09-21 05:40:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04473308-7da1-36fc-8b31-b2c07ea47991 | -3.07507 | -61.17743 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 032d782c-edc9-3cf8-8fa2-402f5b19819c | -3.44127 | -50.61191 | 2026-09-21 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 20206fd6-b507-31bf-91ae-2dbc3c5ab0ff | -4.07272 | -52.12804 | 2026-09-21 05:40:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60a74ca7-5e80-37ef-b064-2f46e5d751d8 | -2.87316 | -57.80147 | 2026-09-21 05:40:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9250de52-4533-3d32-941d-183abd822ed8 | -4.08794 | -62.08527 | 2026-09-21 05:40:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 60b88dc3-ab76-3fee-a8dd-a0625829d3f6 | -3.4419 | -50.60757 | 2026-09-21 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1aac5d7f-2f70-35d6-8548-200e7336ca93 | -2.85331 | -57.6366 | 2026-09-21 05:40:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba7209ef-75fe-3056-b8bc-929de0187918 | -3.13483 | -61.39903 | 2026-09-21 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 835569dd-d293-3dda-8f28-ce68b6ffa822 | -3.40031 | -59.58298 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb00caa5-1246-3348-900c-87ae345ef544 | -2.87503 | -57.7996 | 2026-09-21 05:40:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e2a7e37c-47a6-34cd-b6d8-2e434e9a11e5 | 0.01134 | -60.60336 | 2026-09-21 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb696071-4c65-3f4f-8cee-5a6a9ff123b2 | -3.23633 | -60.80127 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d450f2f6-e2c4-3eea-94d8-fc97b1582efb | -3.15199 | -61.39819 | 2026-09-21 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dddac17f-ac6f-333c-95e8-097c7a228d82 | -3.50293 | -59.92842 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9f24c9e-4a09-3c8f-a6f4-2f5ac89677de | 1.66698 | -50.9275 | 2026-09-21 05:40:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eb8d60c3-353a-346b-8660-f011aa422ebc | -3.71533 | -60.55347 | 2026-09-21 05:40:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4ddccb0c-3e53-3cbe-85d5-ec8204a78a66 | -3.49713 | -59.60876 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2ba1f13b-36ce-3939-bde9-7d5a84edc385 | -3.00853 | -54.17856 | 2026-09-21 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c7714237-c386-3d28-a01a-e2e2a17b9170 | -3.65026 | -58.90231 | 2026-09-21 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f3ddf0e-a7cd-3a15-bd0c-36eb23df08eb | -3.66167 | -58.87571 | 2026-09-21 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ad2e20c-d269-3f56-9445-271ff9ee08ac | -2.94732 | -51.04224 | 2026-09-21 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d57202ac-80d1-339a-9cd5-63b484b0e483 | -3.01216 | -54.17773 | 2026-09-21 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 462be502-d197-3442-bf95-91a476c9b478 | -4.29857 | -56.26251 | 2026-09-21 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3277fc38-a083-3d10-bc1a-9a49652eba24 | -3.60878 | -54.04216 | 2026-09-21 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef5c3491-951e-32da-b947-75cee65a8105 | -3.71868 | -60.55399 | 2026-09-21 05:40:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ebfd1929-bfc1-329f-9809-fe8630bc7adf | -2.46483 | -49.22533 | 2026-09-21 05:40:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f49df8a7-280c-311a-838b-7c7273a20da8 | -3.78643 | -60.74411 | 2026-09-21 05:40:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0367773-4057-3d1f-ade9-d67162e8cda2 | -3.44791 | -50.60853 | 2026-09-21 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| deb08eb8-acb2-39af-a62d-a6b4617ca345 | -3.45771 | -58.32432 | 2026-09-21 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee62ad06-99a4-381a-981e-306722700c2f | -4.51763 | -55.47216 | 2026-09-21 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e468bfee-9bed-3200-96e2-d4450f6eba8c | -3.38967 | -50.44658 | 2026-09-21 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ed9a843e-07f8-34cb-b08f-319c791f596b | -3.39467 | -59.52892 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f4c86de6-0e30-3d29-9033-7757b8ad24a0 | -3.17718 | -58.59035 | 2026-09-21 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 673d0e93-7ff4-3e33-a81a-eb0fc26d9bfe | -3.33349 | -59.80951 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c1d5907-6d4e-300a-8ac7-62549727e9b8 | -3.32752 | -58.13061 | 2026-09-21 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97fea88a-f39e-3333-9a9c-0e46ea336caf | -3.76514 | -59.48098 | 2026-09-21 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e6182d5-5f71-3b2a-a22f-11bf863edf63 | -3.39811 | -59.52945 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5384cb22-b8a5-31cb-bc7a-e7781b830213 | -3.73643 | -59.43799 | 2026-09-21 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 80f21987-d035-3ea4-9d87-40f6e6fa1018 | -3.06306 | -61.27466 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dea1c659-4ea4-3cb7-8e4d-0338e93018ef | -2.87239 | -57.81702 | 2026-09-21 05:40:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 640e6c85-f0d1-3c38-b95a-9390f91d294f | -3.49317 | -59.56638 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2127768f-32a9-3f3f-8e2e-d26a737fbb70 | -3.68797 | -60.57444 | 2026-09-21 05:40:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2f0a73e-c7f4-308d-b840-b1122d06ea58 | -3.69243 | -60.56792 | 2026-09-21 05:40:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11f35e84-bdb4-3c84-9af2-6a855bfc5a1a | -3.33361 | -59.45146 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36cbf8a6-9888-333a-bac6-9dd898a7870c | -3.75784 | -59.41429 | 2026-09-21 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ff0d195-c0b3-3526-b68d-bb8284a40e15 | -3.56004 | -58.74341 | 2026-09-21 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a41093c2-04eb-3167-9ee9-a6982365f022 | -3.33462 | -59.80222 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47967f9a-0019-3000-8d34-90a8e136e241 | -3.07394 | -59.13096 | 2026-09-21 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4b89336-8d3d-355f-acb3-054134f48348 | -3.44177 | -58.01961 | 2026-09-21 05:40:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| fbabb9e8-3a63-33b4-ab72-8ad457952f19 | -3.12325 | -61.42907 | 2026-09-21 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cdb262ca-d0aa-3ab5-b7ee-928b860140e1 | -3.19016 | -60.4287 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 02cfac90-13d9-3bb9-bfdf-52bab94d0bcd | -3.00999 | -54.16867 | 2026-09-21 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b848b32-d6c4-33da-884d-0c82f8f0953c | -3.75667 | -59.42184 | 2026-09-21 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f2032dab-8396-3d27-abe8-3b94c22b3395 | -4.21922 | -48.61664 | 2026-09-21 05:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 193ace50-8589-3c78-8985-88ff76bfdc6d | -3.59235 | -59.06541 | 2026-09-21 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c7b5bd2c-3d8a-3aaa-8a8a-afe352ec38a6 | -3.60082 | -59.01095 | 2026-09-21 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa77df49-17a4-3b6e-ad8e-7525336374e1 | -2.87893 | -57.78901 | 2026-09-21 05:40:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f2be2b82-1fd3-3673-adad-dee86cb51c24 | -2.91389 | -54.19267 | 2026-09-21 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 368743ce-f0e8-3c27-8b6a-7765d7d0c1f6 | -3.47768 | -59.59814 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f8fbad7-41ac-39be-8c9c-2f9a0a6acfba | -3.29167 | -59.44875 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f5bf0ee5-ff57-3acb-aea0-54e7a78e42e3 | -2.61653 | -51.72776 | 2026-09-21 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5bd68ca6-6251-306b-848d-6f100d70a18e | -3.07249 | -61.27967 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 176573e3-493e-38a6-a8b9-a80716713660 | 1.673 | -50.93013 | 2026-09-21 05:40:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f8f70fd-22b8-3a1f-9a22-6b1dcd155eb0 | 1.53778 | -55.80146 | 2026-09-21 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06fa638c-052e-37e7-a40e-6dac6ae25c08 | -3.39345 | -59.58192 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bf7bf460-b22b-3799-8523-9ab5c7ed6a8c | -3.48343 | -59.56107 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6574b002-b37d-34e8-83cd-70aab3f8f0d4 | -4.01649 | -53.49457 | 2026-09-21 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c03ceab6-47ff-37f4-91a5-f5bedf1a3fa3 | -3.38357 | -50.44589 | 2026-09-21 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1fe62773-1177-33a4-8db7-94f7b83b0e88 | -3.55094 | -62.07863 | 2026-09-21 05:40:00 | NPP-375D | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1630526e-a66c-3e5c-a822-4dfa0db742bd | -3.06584 | -61.27863 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e17e4679-3803-33b1-bc73-3ca07781cd86 | -3.60469 | -59.05541 | 2026-09-21 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b80fa89-98cc-3fbb-a475-e71509748c1d | -3.34541 | -59.86725 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e2326de-2f5b-3340-9760-eecaff00b780 | -3.07581 | -61.28019 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f3751d07-d599-3585-87a5-da5aa235aac3 | -3.40173 | -61.29576 | 2026-09-21 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36a319f4-ea44-3c0a-9922-0f5aed331a09 | -3.78977 | -60.74463 | 2026-09-21 05:40:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cab45141-8b20-3ba4-8237-7bdd7501cc48 | -2.78975 | -59.89345 | 2026-09-21 05:40:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2a305785-bd62-36d9-8180-652e0a17fff3 | -2.96062 | -59.31926 | 2026-09-21 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README90.md)
