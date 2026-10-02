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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5602c0c0-3ac1-3977-98dc-a29930bf1fee | -9.52666 | -45.3298 | 2026-10-02 04:14:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9eaf27fb-929f-3750-803a-55966da583cd | -5.14355 | -42.96308 | 2026-10-02 04:14:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8011ab1-27da-3389-bf89-e98556ba59d5 | -7.27315 | -55.59367 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8dee455e-7ce3-3e89-a81c-e623a526dc6b | -6.24527 | -53.14415 | 2026-10-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a1f7f274-33e3-307b-a059-a599cc59ea0a | -7.46404 | -54.99708 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1863f390-22d6-3f02-9c56-fa14e6a73717 | -7.33301 | -55.58406 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c6b89adf-067d-32dd-ba58-691fc00a2bb2 | -5.75453 | -45.14896 | 2026-10-02 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 39e0c584-6cac-301e-a599-e73c1458cb53 | -9.52392 | -45.34614 | 2026-10-02 04:14:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51d8c0f3-784d-3fa3-8d78-f67466406a56 | -7.74124 | -49.20741 | 2026-10-02 04:14:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 1fc3dae4-d120-3341-9f6c-89ffce456dc2 | -4.255 | -50.76321 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66873adf-e96a-388f-abd1-801a845c81dc | -7.81765 | -55.1282 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c91bb015-5475-3d67-97ff-0a264a872c92 | -6.43928 | -51.70773 | 2026-10-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| babe90c4-c9a3-3508-9a73-6c64c3b9098d | -4.26417 | -50.74277 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 1279998f-9bfa-3720-96d9-6fe3f29a08eb | -3.39351 | -44.75315 | 2026-10-02 04:14:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 416e83a7-3c51-383f-b8c3-d43a7612b45d | -3.39531 | -44.75135 | 2026-10-02 04:14:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd8ca915-100d-3b33-bfe5-5580c8fee750 | -4.27575 | -50.77358 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db370e37-aaef-3eff-b373-390cb1575c5f | -3.03838 | -53.88055 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2f12d06c-af84-364a-a4eb-889c49ad4fde | -5.86589 | -43.59292 | 2026-10-02 04:14:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7f9433d5-8be7-31f4-a153-d5908df62cae | -5.75011 | -45.15271 | 2026-10-02 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 63db3098-103e-353b-9cc8-55fe23fa22c8 | -4.29144 | -49.0953 | 2026-10-02 04:14:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e76c5f64-6bd0-3f4b-a23d-6175e60ffc6c | -4.30307 | -50.77853 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d5ae7338-ef2c-30bd-815a-53a27d92e75c | -6.44574 | -51.70412 | 2026-10-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7fe3cfcb-3d45-3bd4-b306-7493ebf89530 | -7.87904 | -44.17758 | 2026-10-02 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a02503b2-a78f-33c1-806b-6672f0a68e91 | -3.00352 | -53.88048 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2312d1d0-582d-3439-952c-bd67ee3f3295 | -7.19367 | -52.61794 | 2026-10-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 22f097dd-d3e8-3ab8-9b6e-e2e2866604d5 | -4.26774 | -50.78734 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3cbc7614-c83c-3754-92d1-e45624bd3bc0 | -6.24 | -43.77532 | 2026-10-02 04:14:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c4173463-6fd5-3ddc-a84c-52680be941e4 | -7.52084 | -47.33467 | 2026-10-02 04:14:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8d0705d8-017f-3f1d-ae51-eb0b65a946ee | -5.76045 | -45.159 | 2026-10-02 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 34bc2fac-bb80-3c85-b44a-969f6fca0da7 | -6.23465 | -53.13248 | 2026-10-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0967b5b2-1226-36c2-a840-a88b858715d7 | -9.83136 | -44.82933 | 2026-10-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48dab690-a4f7-37af-abe3-a1bd8a4aa5cd | -6.8908 | -43.69768 | 2026-10-02 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3df6fb26-4375-3798-aea0-7d389947be01 | -4.26356 | -50.74632 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f69d4a88-aedc-3c74-a50b-5156bbf43a41 | -5.73652 | -43.28835 | 2026-10-02 04:14:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 30fa9313-2d7f-3deb-8546-d7f14a189c70 | -3.28758 | -53.84478 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 7fbd19ac-5576-3adc-b076-955962ba2c03 | -6.3319 | -43.38273 | 2026-10-02 04:14:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c8039082-5768-3131-8c85-c483f8426c11 | -6.1467 | -47.47007 | 2026-10-02 04:14:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d5a6f137-de92-3aa8-ac4a-1176b7bdec30 | -6.90284 | -43.68823 | 2026-10-02 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 76b027f1-3087-3848-974a-140d30a850d3 | -3.41738 | -48.33992 | 2026-10-02 04:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6aaa7a77-0d53-356f-b57b-7fe9d425990b | -3.13773 | -53.76025 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 68324a4d-d887-3971-87a5-f106da8cd157 | -7.27218 | -44.30114 | 2026-10-02 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee6fed5c-b93a-3f01-97c6-36ca3b3f71e4 | -8.17277 | -54.80412 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f52b060a-57ec-3a9d-9d17-6b9f4979188b | -8.63474 | -47.82275 | 2026-10-02 04:14:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d61876a-5dd9-3dd3-843b-6ba900e0499b | -6.43997 | -51.70399 | 2026-10-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0e4c1be-a861-326a-ba1e-25484ebeee06 | -4.26237 | -50.75318 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 22083e16-cb4f-3887-b9a4-aaaa3d3a73ca | -7.74802 | -49.20591 | 2026-10-02 04:14:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 8429bea5-2f08-3a06-9599-4d62312320b4 | -4.29437 | -48.06813 | 2026-10-02 04:14:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b57ea083-d2d2-3a78-9e38-eb9f719bfe26 | -6.86549 | -44.43412 | 2026-10-02 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9fd58395-35ae-3e95-9fcc-b4d4706126d4 | -6.90464 | -43.6771 | 2026-10-02 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5a86efdf-9ac1-3936-9e1b-5ca5cfd42585 | -5.54937 | -45.2603 | 2026-10-02 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 85e19a2a-3216-303b-96a5-e5df4f60665a | -5.66263 | -42.65285 | 2026-10-02 04:14:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b7f11d93-1915-3966-98b7-1d1df07e7dc8 | -4.27996 | -50.78185 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| efc75156-36c5-3f47-9c81-89e48acec44f | -3.06912 | -49.36485 | 2026-10-02 04:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a10b7a82-b7c6-3d1a-8787-6f14232100bc | -7.87622 | -44.17318 | 2026-10-02 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d8217296-128c-35a1-834a-168e1808b0fa | -4.25563 | -50.75957 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb26dc55-fb02-3356-a647-9cdb05d24e0a | -6.91147 | -43.67822 | 2026-10-02 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b1a06726-a580-3fc3-af9e-97951d1b4a1b | -5.58242 | -45.79313 | 2026-10-02 04:14:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac04f4b6-454c-3f7d-ae32-b09b9cde1270 | -4.27326 | -50.75531 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e9d1209-efe1-3e5c-afeb-e700507b64f2 | -5.7343 | -43.28051 | 2026-10-02 04:14:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c2571dc-3914-3162-af80-00ef6b1d95b7 | -4.01494 | -48.94583 | 2026-10-02 04:14:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0dc32beb-dc89-3b6f-96e6-46ff4121384b | -7.69266 | -48.41582 | 2026-10-02 04:14:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ed858fbf-260f-3262-8999-b3a52fe38ec6 | -8.00069 | -42.90482 | 2026-10-02 04:14:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 64f43cde-8fd0-3b71-8daf-197fec570ed2 | -4.2648 | -50.73919 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 2e455036-cdb2-3c9e-b933-f9c6483bdfbc | -3.39422 | -44.7487 | 2026-10-02 04:14:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3591824d-0c70-319a-ab8f-5e0690f00dd1 | -5.89301 | -53.49532 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b1132edb-c373-37b1-8f15-06823a2a9de9 | -2.93708 | -41.73863 | 2026-10-02 04:14:00 | NOAA-20 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d4496b90-ffa4-30d7-b63b-f7f63ec8f0c8 | -6.12859 | -43.72689 | 2026-10-02 04:14:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 90e418ea-da9f-36dc-9d3b-156914d0b07f | -7.33185 | -55.59019 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7bd44866-8026-3735-937d-11edd4eedcef | -7.40057 | -55.59819 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 939b9a9a-a2dd-3551-b7a9-f0522ad1f567 | -8.26506 | -39.07136 | 2026-10-02 04:14:00 | NOAA-20 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3eabd6b3-8f04-31f4-812b-cecb583174ef | -4.24588 | -50.74646 | 2026-10-02 04:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b771521e-d70d-367c-824b-036368d32935 | -7.49395 | -54.99641 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bb7887a3-5664-3275-b6d7-2888d348c0f5 | -3.13875 | -53.75429 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 9881145b-29ba-3fd3-8a43-3141c0c2fefb | -6.44974 | -43.82294 | 2026-10-02 04:14:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e74cc507-6426-3173-bbc8-2b7ab5856172 | -8.96779 | -44.17113 | 2026-10-02 04:14:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ccc764f2-03da-352f-83ad-9e69c049e740 | -4.2909 | -50.78382 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 51282841-9f44-3fc5-b1d0-fa507abad7ac | -9.82983 | -44.81705 | 2026-10-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 33f0f634-59f2-33de-a219-ab7d0e1ff386 | -3.17684 | -54.10897 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8bac7f02-50d4-350c-a7ba-705764efb58b | -5.86938 | -50.16482 | 2026-10-02 04:14:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3cc46b3e-d22a-3fe5-8a37-6f5db3004e72 | -6.33829 | -43.36493 | 2026-10-02 04:14:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2fe3e0a6-c886-38b7-abe8-fa24617f951a | -4.24653 | -50.74715 | 2026-10-02 04:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 815f1f49-6a87-3f73-9317-4d25b4414553 | -7.8287 | -55.14391 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fb82bd56-f361-32a2-aca8-70aa9bd316a3 | -9.83381 | -44.85764 | 2026-10-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 244dec00-a6d0-3da2-bc25-82c4506237a9 | -6.23149 | -43.10974 | 2026-10-02 04:14:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ec793739-7785-32b7-819c-13ff959ed615 | -8.07426 | -54.88656 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8423e6c0-597b-3629-bd41-a98aac13bfc3 | -3.17325 | -54.08905 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 396d294c-5067-38ae-981e-111c35845f2b | -8.78303 | -45.8253 | 2026-10-02 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c0f17543-1572-3ae4-8233-adf59d3ca03b | -6.24467 | -43.76831 | 2026-10-02 04:14:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| a7249a99-84fc-3f53-aace-dfcd3b2453b3 | -5.7619 | -45.15023 | 2026-10-02 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4eca86a7-6214-366e-8924-8fa0e38f2412 | -3.2891 | -53.86161 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fb5670c8-7114-3483-b085-85efb64a8080 | -6.19266 | -52.80574 | 2026-10-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 57519f98-6a23-3ad6-9a58-3be35b400d5e | -2.18638 | -46.5736 | 2026-10-02 04:14:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca64e0bc-7f08-33a2-9799-634e3eb4591b | -6.71194 | -45.97175 | 2026-10-02 04:14:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e058f8f-faa4-3521-94e7-f33fb818ee2a | -7.39899 | -55.59651 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 032f11b1-5a86-3b1a-b91b-39d0718a88d5 | -5.74051 | -43.28527 | 2026-10-02 04:14:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| dbed1cf2-bf5f-3759-a4b3-6c333b2acd6c | -4.35798 | -47.77182 | 2026-10-02 04:14:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 47366394-8baf-3d02-8d0a-fd9547e383d0 | -7.5678 | -55.13324 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 40f432ba-f13d-381b-836c-e3b2a2aed6cd | -9.07569 | -44.98963 | 2026-10-02 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| ad4c1c2b-5bbb-31d9-b329-ef5de538bed3 | -9.13491 | -46.66 | 2026-10-02 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 282cb36c-ca01-3eba-b93a-2fbd0ce50fd4 | -5.13901 | -49.86908 | 2026-10-02 04:14:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README36.md)
