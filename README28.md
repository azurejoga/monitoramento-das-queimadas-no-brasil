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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99eca641-4fbb-355b-af9c-5966df75930f | -7.7595 | -44.76232 | 2026-08-26 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 59c081cb-e3c6-3701-bc51-333d2d99a96f | -6.76489 | -59.44488 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90e91cfa-76ff-3fd5-b1cf-397577aa9021 | -8.11357 | -47.46463 | 2026-08-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b9298274-5b02-39b1-b894-4ff8d33bc1a7 | -7.75641 | -44.74714 | 2026-08-26 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2e2755f0-72cf-30e1-bf09-dc5e7fd9c47a | -7.3775 | -55.17923 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd5996e5-66cd-397a-8d83-8de4b1f39d56 | -9.03467 | -50.80267 | 2026-08-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b76e3cb0-aabf-3629-b6a6-447095cf1b49 | -10.37246 | -45.06609 | 2026-08-26 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 196e4c8a-18f6-3ee1-ab52-3aee026c3745 | -7.25591 | -49.84805 | 2026-08-26 04:51:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0fdae64e-89cc-3a4c-8e65-ea9213febc9f | -9.05045 | -50.79969 | 2026-08-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2dd65b12-58f9-380f-a330-bc040f8f4823 | -6.02009 | -57.7901 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f36ef273-1064-3f61-b1d5-d4a0fd2b78cf | -7.03139 | -59.2299 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9a7b5786-5ea1-302e-8f1c-051946218cd9 | -8.03735 | -51.78958 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1245799e-0f4c-339b-871a-abc7b269d3d2 | -7.28191 | -44.0832 | 2026-08-26 04:51:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 06f045e7-89a5-3395-ab73-03cce3855058 | -7.28617 | -43.0297 | 2026-08-26 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ea337091-7dac-3c94-9cd7-abca3fb5f9df | -7.28712 | -44.08403 | 2026-08-26 04:51:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| edf9943b-72db-3509-966f-8a1210f69e61 | -7.52752 | -61.38279 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 0fc87a33-4688-3e64-8093-4755e82281ce | -7.52648 | -61.3886 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 30.5 |
| fe37de5f-f9b2-3514-a56a-53829de1d83c | -7.38035 | -55.18356 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca01eb51-26ce-3e8b-a844-7a95528da06a | -6.25397 | -53.36039 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa4d6d88-bfb9-315e-8b10-9d80b6203252 | -6.16396 | -57.8036 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 35fdc5cf-a536-3e87-90aa-0eff6b230215 | -6.25069 | -53.35981 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 871ab7d3-35ca-3353-86b9-cbff6125ef42 | -4.79948 | -43.17215 | 2026-08-26 04:51:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51f18c0e-4079-3ab7-8315-326391cadc35 | -6.62797 | -58.49632 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3a087097-f18f-392b-98a7-d1836447be62 | -7.02294 | -59.22557 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 68597d3c-ddb6-3c7c-8a67-a668d59feae1 | -6.40667 | -60.05893 | 2026-08-26 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f0a0537e-6c0f-36cb-8130-c264b523b142 | -6.97759 | -59.25348 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a09b68a3-c434-3aaa-9c6d-37a9f6bc7f09 | -8.59277 | -54.72205 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e199f6eb-2583-3f08-95f5-b4f8134b8d4c | -8.22005 | -55.00905 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85a615e3-1dbc-3b74-8b4e-3182c4030e50 | -7.37565 | -55.1906 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ed4dfba-ccf9-3cc9-a91f-29fe5656134d | -8.12567 | -47.47003 | 2026-08-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1020ba33-738f-3b96-9c08-43fdeef4c861 | -8.95298 | -50.7741 | 2026-08-26 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 405ca481-55c0-36bb-add2-acc1af1789ea | -6.99378 | -59.26472 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5fd756ff-ed24-31df-9408-f403618d7b3c | -7.75718 | -44.7414 | 2026-08-26 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da03865e-46fd-355c-a146-a53df933d21d | -8.62362 | -54.74563 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe239112-af35-3b14-b78a-164d123f8be9 | -8.18239 | -54.96074 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 42a8ee82-f90c-3f67-bc7b-4b6a8884996e | -7.49478 | -55.36774 | 2026-08-26 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 291fa386-826b-3c16-8421-c1de6ebc06e7 | -6.64124 | -58.49449 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b87e8499-83c7-38ab-aaac-8f5a8b54782f | -6.86073 | -59.41017 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1a464ed9-6156-371e-95b7-65f52c725e0b | -10.02324 | -46.41971 | 2026-08-26 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a5b0737e-b107-3dea-91b4-eda3528e0f08 | -6.19875 | -55.64259 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6957521-de58-3af6-b2b0-63576ab81fc8 | -6.83279 | -52.50827 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9dd11426-769a-3db5-bbc5-04ade88a29b6 | -6.99973 | -59.31019 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a62ceece-37d9-3adc-a4ed-52e6474bb11d | -5.34469 | -45.16555 | 2026-08-26 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| da71685e-c668-3536-b383-e1adf6ea7b05 | -2.78882 | -49.58308 | 2026-08-26 04:51:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc7f62ed-18a5-36a3-8045-e1026d70813d | -6.79554 | -59.60353 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e1cebfe-58f3-363a-b084-7264c0d83217 | -9.6488 | -48.31504 | 2026-08-26 04:51:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d9ebff95-e102-3d1f-a9d4-9095ee7b0647 | -6.6519 | -58.50814 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| a228af5b-d80b-32bc-aafe-e0ceb57f128b | -6.63017 | -58.50875 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7e0e109f-e1bd-3ff7-add5-214ad297e810 | -7.51674 | -55.58736 | 2026-08-26 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dffd0830-c357-3364-9b13-dae6c10f510c | -8.12987 | -47.47061 | 2026-08-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bef30187-18de-3a59-8b1e-f393090cb5e5 | -3.27048 | -50.59563 | 2026-08-26 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72224c02-567c-325c-8bd2-f275848f6864 | -8.04189 | -54.01497 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 333fcd9d-2dcb-34a4-912e-083e08ad8ac2 | -7.06356 | -59.2265 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4a389e2d-adcf-3dac-b89d-afba38c51070 | -6.50588 | -55.22508 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e59e103-3328-30e2-868d-f7f9fc336eb0 | -6.27223 | -53.37395 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 739c7cba-4ec1-342d-a32f-3a072680b11a | -8.03183 | -51.80327 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94756980-b7ce-35d5-82cc-85bb46a69dd8 | -8.6888 | -54.71546 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c59e8ef3-0c1b-30a5-947d-f4512f5f770f | -7.55804 | -61.41553 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b6b5569a-7e3e-3508-b9a4-93d0b704eb1e | -7.03469 | -59.2363 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 95ea5dac-9916-39b4-b23a-51038d385243 | -6.2612 | -55.41203 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff03cc2a-45a6-35fd-9f62-1fd6a74cd118 | -6.44533 | -54.97125 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d913014c-42b5-303e-8b98-c5898cf110f4 | -6.72974 | -59.14051 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ced834b8-4342-3a8e-b65d-0a2cacc598f7 | -6.26671 | -53.38737 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1518eb40-22c6-3269-8e60-1a6897e26920 | -4.56279 | -49.52103 | 2026-08-26 04:51:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e24fe0d9-d5de-32b9-a204-f87f112c5588 | -8.55508 | -54.71968 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c22d1572-71dd-3a37-be96-2c42300b302c | -2.98905 | -49.27427 | 2026-08-26 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b3b59c6-9219-3db7-b49f-9c7c236f6947 | -6.27333 | -53.36699 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 13b69f63-fcd8-3edd-84e7-064a43dc85b9 | -7.75878 | -44.76772 | 2026-08-26 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4f87fe86-01b1-3a08-903b-e179c0dd22b2 | -7.39599 | -55.17458 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9c075e6-0104-3e47-9b1b-0ea70e4a75b5 | -10.03844 | -46.04841 | 2026-08-26 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d91868d3-b56b-3b2d-9cdc-8a81ae800158 | -8.62758 | -54.74252 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee7ed9cb-f026-3994-8012-9eb3044635be | -6.32939 | -54.73335 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9fb10b0b-bbc4-3673-b64e-7a9bffb84b3a | -6.1403 | -55.82335 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e2f6969-6a54-3daa-925a-e184b2f7a281 | -7.45837 | -59.99888 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2317f2fd-22ab-3851-9c45-0c9473f6ef9e | -8.81619 | -49.60788 | 2026-08-26 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6bcf558-edb7-3798-80d9-9b2aeb208786 | -6.12336 | -57.8228 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4ba0050b-7164-346a-b4bd-8ffcb16beccd | -6.70434 | -56.34729 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cec46e3f-b9e3-3c2c-bf6e-74c16131e09c | -6.77976 | -59.43836 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ab5f6390-8b3b-31b9-aa44-4ea8ab215e07 | -7.06942 | -59.21868 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 2bb58c46-66ed-3065-885b-5982796d09e7 | -5.1486 | -56.26778 | 2026-08-26 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e74f733f-6bb9-3b61-9ea2-da2750d169b5 | -9.03584 | -50.8017 | 2026-08-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c82654fa-cc06-3c84-bdd9-217d6cb82c38 | -6.78637 | -59.73909 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1caf71d0-d5d1-3b39-9308-8b9c7580c423 | -6.25013 | -55.47968 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| adb3e02b-5b57-3412-a1aa-7fe38aa7b7d9 | -7.47795 | -61.37428 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 73d9ab2f-0ee2-3ee6-8cb0-bb328161df93 | -9.64584 | -48.33635 | 2026-08-26 04:51:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 34b92071-d179-3e86-922c-9391d4e756dc | -6.63793 | -58.514 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2ac9d62e-b402-3285-a9fa-09f20fda4dbf | -8.627 | -54.74617 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23ade7c1-04af-3940-933d-db1b88cb2a68 | -6.35981 | -54.78382 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 110d63e8-5574-34c3-8d1d-3c4c13b341b0 | -7.527 | -61.38569 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 9a57fe03-a938-3ea3-b215-eb48fa642a1b | -6.99745 | -59.26983 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4de0b3ef-b014-3e27-8398-c568b02f790e | -6.78937 | -59.74903 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e524cf7f-a52c-33dd-93b0-7231a9c0fd80 | -7.027 | -59.22918 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 29fdb05a-3c40-3fd0-a84b-7051e6157381 | -8.57313 | -55.27994 | 2026-08-26 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| add471c1-0156-36f8-88e2-24ebb09158fe | -6.43172 | -56.17863 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a222c79b-b0dd-3e8c-8bda-c78c667f8b53 | -6.70066 | -56.34671 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5098930b-1a94-379a-a3e0-926e6a8c2eba | -7.51271 | -61.38331 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 84dc1b10-9299-38ec-9b1e-86b0e1d42fca | -6.27555 | -53.37448 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 41d96b29-e13e-31b1-8888-27804035ea71 | -7.29271 | -44.08722 | 2026-08-26 04:51:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3c7e3dfa-a02b-3b8c-a63f-8c7be4acd80d | -8.60125 | -54.71228 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23fcde44-36f7-3f18-8e7d-2c223cd6b775 | -7.13798 | -42.77621 | 2026-08-26 04:51:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README29.md)
