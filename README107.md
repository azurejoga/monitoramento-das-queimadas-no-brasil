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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ca5497c-95c7-3e81-ac72-e091636cdfcc | -4.34996 | -55.64968 | 2026-09-22 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a1fb5a04-d576-3341-84d7-4a5387003936 | -6.13096 | -59.96759 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7118b27c-9f9e-3c49-a359-a6c4a8eb3501 | -5.98464 | -57.70123 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1286c546-8c8d-3921-a1ad-d679dfba6b85 | -3.38884 | -59.4269 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 525813b0-7caa-3653-8c59-2f305eb5a3d2 | -3.96903 | -59.63515 | 2026-09-22 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e07df5a6-b121-3d5e-b316-43cd362a41c6 | -3.07144 | -61.27448 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5165257-dd30-3f0c-96ae-6f1dba876fcc | -2.92726 | -57.79117 | 2026-09-22 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ba17ddff-4a1c-3db3-98bf-7faffe5e3440 | -3.40075 | -59.42415 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a8a1d79-e0f3-3cf7-b2b7-72d6a35aa3ca | -6.16141 | -59.94428 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6d37ac61-0220-3ab0-9d03-f1b85d9d763b | -3.18687 | -57.88566 | 2026-09-22 05:42:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fb01edbc-4697-3725-b85b-3a7aa3bcd2f3 | -6.09497 | -57.65662 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54b3472c-15be-3e70-bb65-b3da5177c991 | -7.32924 | -55.5957 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 599b58bd-bf16-3095-a3e5-eeb726da1dbc | -3.04622 | -61.25557 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b1b9af89-8889-3ffd-90cf-60579d7697e2 | -6.09136 | -57.62119 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f4a4cca3-d9d9-3754-9d65-6e0a6a08be18 | -7.71706 | -61.23674 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5bd26ce4-1b86-3f86-9f6f-03a3cd45cb40 | -6.75577 | -59.06378 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f518f13d-b452-3d28-9d39-b02329bdec4d | -5.98527 | -57.69704 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a07c847f-b218-3b27-9ba8-b6eb23232d55 | -3.04505 | -61.26294 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d2e6f163-3126-33c2-a6ef-37bd9a06f322 | -8.62135 | -54.6323 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ecfb27c-9069-3130-a18b-af62b5f54fc2 | -4.07789 | -55.32191 | 2026-09-22 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| caaacf47-ab9f-3bfb-99a4-87109fc1c093 | -3.93156 | -56.05424 | 2026-09-22 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c888b35a-b460-372a-8101-5e7b548ddb42 | -5.65252 | -60.21644 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9af40ea5-0014-35e0-a665-c46a45ca94e0 | -6.19308 | -57.7802 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1d4480c4-7bd6-33a9-a113-42c26ed25af7 | -8.60973 | -54.63452 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11d96155-518a-32b5-810a-8fbc281f5045 | -3.72136 | -60.57685 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2ad1c1be-3708-328d-9829-b57c6052964f | -3.07713 | -61.28292 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b372727-e6eb-3a47-a313-07b4bef2ab63 | -4.32149 | -60.88496 | 2026-09-22 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d1d817bc-d905-329a-b0ae-030b97b6500e | -3.14809 | -60.655 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4d33b98-f096-37af-9c30-34b40a1e7191 | -6.46309 | -59.96958 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e8597bf7-a12a-38b0-8335-559186b76127 | -4.20449 | -59.9099 | 2026-09-22 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5830d29a-a552-3307-a84f-8bcecf983f7f | -4.22248 | -63.077 | 2026-09-22 05:42:00 | NOAA-20 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3b88d848-3da4-340b-bf2d-e9f7d05f1aeb | -7.32321 | -55.6014 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 18a4dc5c-2e65-3b2a-93df-c0d3d97b4322 | -5.211 | -56.10337 | 2026-09-22 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0f11e78f-ec53-37ae-b8e8-2a5617b22a64 | -5.81838 | -57.73741 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 24f3ae4e-4068-3425-bb82-c30c66d3a805 | -3.97275 | -59.63571 | 2026-09-22 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c97ea33-d1c5-3c2c-b472-879cc20178ab | -6.45658 | -60.03835 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 472e5f20-7859-302d-a275-597263072833 | -8.10177 | -55.35518 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e18eb132-04ff-3fb7-8249-fdb2cbe53374 | -6.30778 | -57.73616 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 51c8bbbb-aba4-3020-979a-26bda88f6fcc | -6.72209 | -55.07753 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70b97e54-8aa5-31bd-8b1d-f2467d6e747a | -6.42757 | -55.61409 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2eefc7a-717f-3ca8-b4b4-b10955f6df89 | -7.61513 | -55.35511 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f110ce6e-b79e-3bd5-9728-b17a00d819e9 | -3.23705 | -60.8028 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 099ec575-679f-364f-a6c9-92bb3e8114f8 | -6.30741 | -57.74632 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d62730a5-ca61-345a-9a71-09aa5acf5354 | -7.60947 | -55.35758 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 129940c2-3ca3-305b-9771-f0f72d0e093d | -6.1217 | -59.95244 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a6f0b628-30db-36aa-8bc8-c943a1ab6ca2 | -3.05168 | -54.40868 | 2026-09-22 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ecbb9598-c18f-3671-8c83-d0767417494f | -6.86583 | -59.91193 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a4b8d7a-6faf-3e89-b184-0d5fcc686399 | -8.2437 | -55.29564 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| af46613d-ccd6-3e45-8b62-f8e5d42f4af7 | -6.7074 | -59.00319 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4e7b8789-55e4-3b51-81dd-8d9f9f79b2b0 | -3.78501 | -60.74804 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 986a0f6e-4c48-3710-b463-3a9fbef787b3 | -6.15747 | -57.95835 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d9d85e22-35d7-3093-9373-a94593643390 | -6.74724 | -59.06604 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 435d0ec3-2d9e-3233-abee-bb56984283ee | -5.2004 | -56.07543 | 2026-09-22 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b9cf7115-29cf-35cf-ae16-73ab9e2b5ec8 | -4.27056 | -55.44016 | 2026-09-22 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 062bc689-bc92-3ae0-a1e6-aa84fbfd51fc | -5.72452 | -53.45786 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3418a65a-8ba7-3150-96cb-beeae59e9b04 | -5.93549 | -59.97992 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1edbdfcd-5ab5-3537-8ac0-916744463b67 | -7.4568 | -61.37743 | 2026-09-22 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd0bfeee-ed5b-33df-a670-e9b3408869a9 | -6.4463 | -60.00439 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| deb0a591-3800-3386-95b6-bb86bea3857e | -3.5827 | -59.07227 | 2026-09-22 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 78fc70fc-f13d-33ad-a061-793eefb33bd0 | -7.4026 | -55.22577 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2ccbb95-ca40-38f7-9be5-34cb3dc907bc | -6.92652 | -59.63338 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab6b4cf0-9947-37bb-8f5b-104261a3ea13 | -3.39309 | -59.52326 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4154f2fa-2a00-3d38-bd4b-1c8335dde32d | -3.48201 | -59.57487 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc2ed01b-2cd9-34fd-b658-eb89ace0a566 | -4.63464 | -55.77099 | 2026-09-22 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8beffc2-878c-3360-a972-697de6b05636 | -3.07086 | -61.27817 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6589e15a-1f75-3782-bdf9-aa641cedbce1 | -7.24463 | -55.58471 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 41f2e230-3a25-3cf1-a1e3-b620b9ba03db | -3.15283 | -60.64775 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 022f22b6-333d-3fe6-a69f-5a36074a81f1 | -3.38073 | -61.29079 | 2026-09-22 05:42:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 835d73f8-d2a8-3271-b486-c6d450f5827a | -3.70435 | -60.64013 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 629fd3d6-a1ac-3ed1-971d-82aa4c06fdd3 | -3.48269 | -59.57045 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| faf2ed3b-e221-379c-b4f7-b1efb3f069c7 | -3.0663 | -61.28503 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eca4284b-f6db-3303-9a67-9bc41c3bab09 | -6.737 | -59.42504 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b663577-682c-398d-877b-b820d4346a2b | -6.27984 | -57.74477 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 45b15dc7-fb56-318b-abf6-3ca3d94f72b1 | -8.91961 | -50.92801 | 2026-09-22 05:42:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| eb89099f-a971-31dd-942a-dbb72e14b2f7 | -3.1082 | -61.41934 | 2026-09-22 05:42:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a8ad4437-1560-3394-be6c-bc01c2576bdc | -5.42809 | -60.16784 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| afef413e-0c35-3950-826a-0dbac31933e0 | -3.32792 | -58.13589 | 2026-09-22 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 13972cd6-7a89-3770-a0b3-c7ff024b7e40 | -2.56918 | -57.51314 | 2026-09-22 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e75ab535-123b-3f44-bfc1-62e3cad0dd8b | -5.98634 | -57.7006 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 74c3713b-e32e-38ee-a336-0b609867a2cf | -7.61376 | -55.36028 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2200863-7c44-37f5-bce4-a270dd8eb1f2 | -2.41471 | -58.27378 | 2026-09-22 05:42:00 | NOAA-20 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 919b97dc-84c9-34f2-8c08-2c91adf88065 | -3.23992 | -60.80717 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6134fcb-3f8b-338b-b84b-a9c7d493f937 | -5.93617 | -59.97541 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50e9696f-c87d-3c3e-a1f7-a47451d5c918 | -6.92723 | -59.6286 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41a60cc0-2d60-3b97-aa1c-0f64ee56b7d5 | -8.25385 | -55.3003 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08c36afa-1262-3a68-9da2-6903884353e3 | -4.18383 | -51.24318 | 2026-09-22 05:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 42c13075-f08f-3cff-8d4c-acf24e4daf6d | -6.09573 | -57.62183 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fd02995c-5e4d-3409-81d6-be11b128796d | -7.61034 | -55.34684 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d81291a4-70d7-3825-a57d-84304003a61e | -3.39681 | -59.52383 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 27f40465-3292-38cc-9bf5-5a311bc855ff | -3.42112 | -61.30036 | 2026-09-22 05:42:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 639dbeee-697e-340b-bd4a-bbabf61d36b1 | -8.1543 | -54.80697 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec29325d-7e6c-3750-817f-d72076e18cdd | -8.62232 | -54.62503 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 02c39c65-ea70-3472-b92e-e23b781d0cfb | -3.55545 | -59.42175 | 2026-09-22 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19c9c0e4-58c3-3f4e-9a61-f943dd3358f6 | -3.76972 | -51.35236 | 2026-09-22 05:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6cb3f59a-602f-3ab3-9ff5-96c87e3b8cf0 | -6.13951 | -59.88511 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 083aec71-26e5-3032-8b3b-8a3fdb658bdc | -3.22615 | -53.95182 | 2026-09-22 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 351b8090-53c0-3380-8c0b-26d1c18088ba | -6.3419 | -59.95357 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 819e3fab-909e-364b-bf70-6dbdb4db1524 | -3.06287 | -59.28136 | 2026-09-22 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41b47a67-ab0c-3926-988b-4f1b67f73ba0 | -6.83835 | -55.53566 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5ddbb36-a7d6-39b1-9da7-6381aa497d78 | -3.48635 | -59.62057 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README108.md)
