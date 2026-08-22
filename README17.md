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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e83ff81-7c14-33b0-83c3-623a1a27f17e | -4.46931 | -55.39874 | 2026-08-22 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a741ff17-f3b9-3639-8d37-e141d407d291 | -2.49894 | -48.13362 | 2026-08-22 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 02fec1d3-0eef-3a1e-b795-71f7de5d30c6 | -4.18077 | -48.57188 | 2026-08-22 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6471c8a-7f1c-3dfa-bb9a-f655862d423d | -5.59257 | -44.00756 | 2026-08-22 04:25:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11bd9dcf-3d2e-3a61-896f-cf130a7432d0 | -4.42214 | -55.4451 | 2026-08-22 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a59a06f5-2855-327b-a55b-eeb7d89c6e55 | -4.12338 | -48.93063 | 2026-08-22 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 18f82af9-14f8-3dd8-ace3-98c6b74fb965 | -2.89732 | -48.79156 | 2026-08-22 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 29d041a6-3828-3007-a6b9-8cf2709defd4 | -1.98419 | -56.46205 | 2026-08-22 04:25:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 19f8a176-3993-323d-a551-e50cbc59cb3a | -5.96373 | -51.95443 | 2026-08-22 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4654df1-3420-314f-9d6d-f4b8492ada0a | -6.16632 | -47.48545 | 2026-08-22 04:25:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 062982b9-e8c3-3135-953d-959a682a890f | -5.60761 | -45.71404 | 2026-08-22 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| da6c41d2-ec39-370b-88e4-4c5f04373716 | -4.11979 | -48.93005 | 2026-08-22 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ce1e472-edfa-3b50-81bb-18cab1f01c78 | -2.82546 | -46.73593 | 2026-08-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e1ccdaa-b173-3949-9912-e8c61900c494 | -5.82305 | -43.49631 | 2026-08-22 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76c35b6e-9fa7-3b1b-965d-2e7fee3fa909 | -6.01392 | -44.82462 | 2026-08-22 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f7d087c-c5e7-3656-8ac1-28a101b0734b | -1.74576 | -55.25065 | 2026-08-22 04:25:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fb7a074a-d9c3-3031-a703-48f3d015ffd5 | -7.07191 | -44.99281 | 2026-08-22 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8444eb9-3c70-346a-b6be-b354d097bb76 | -4.8647 | -43.34724 | 2026-08-22 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56acbb68-ee0d-3e9b-80a0-2a03a8187658 | -6.89578 | -43.75116 | 2026-08-22 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3b3be1a5-2aff-3852-9c33-b1f3e3cba782 | -5.59032 | -45.67234 | 2026-08-22 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 00d0636f-1ad5-358e-bd00-aeed2eae3a68 | -7.08147 | -44.9981 | 2026-08-22 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ce1b0c70-1edb-3959-b75b-ca67859d9977 | -4.93693 | -41.97729 | 2026-08-22 04:25:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 93528ba0-1323-34ce-806f-ac8b6d669447 | -4.32758 | -40.55853 | 2026-08-22 04:25:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 59f78ddc-7b48-38ef-9c8d-39d37b448073 | -3.53916 | -48.17807 | 2026-08-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a72d92ff-d14d-34cc-948a-a5f6715b3e8f | -5.7874 | -46.10993 | 2026-08-22 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e7f5e1b-cc9a-379a-b554-8b054d906dbc | -5.78356 | -46.11287 | 2026-08-22 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5fa3a612-c438-3e8f-a610-3f203d2daac8 | -5.56267 | -47.38994 | 2026-08-22 04:25:00 | NOAA-21 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e9670dc-ffad-3246-ad65-83a371e0097a | -1.74637 | -55.24698 | 2026-08-22 04:25:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 509adc33-9c3e-3daa-9da3-fe0efd95d007 | -5.53569 | -46.61165 | 2026-08-22 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 25c2fc4c-4b73-3ee3-b235-c82db460ca7e | -6.88577 | -43.74556 | 2026-08-22 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0210907f-56c6-3855-b5c3-877ddf475c96 | -6.2496 | -43.6924 | 2026-08-22 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 287073a5-41ed-3698-8476-4baf0aa0f15e | -6.88871 | -43.75006 | 2026-08-22 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f7de627b-4896-3672-8601-e44368243a56 | -6.91492 | -44.96893 | 2026-08-22 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 111817e6-263b-3d8e-b9fa-2f49e1be91b6 | -3.36135 | -50.67279 | 2026-08-22 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a28044cd-446f-307b-984f-a1347c4ab4d2 | -6.86925 | -45.99685 | 2026-08-22 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b65eb9cf-b062-3405-abe5-c2d8faccb239 | -6.88517 | -43.74952 | 2026-08-22 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0a375085-5b75-38d6-8855-489854aff11e | -5.60521 | -44.01724 | 2026-08-22 04:25:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 186db75a-0b0f-37f1-83f0-32a2013abdc3 | -5.09476 | -37.95935 | 2026-08-22 04:25:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3f42551f-0f34-3b87-a70f-524e7c0ecbb2 | -5.82014 | -43.46733 | 2026-08-22 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0affc659-9453-3f13-b4e9-2dbbe3ef5609 | -3.53445 | -48.18527 | 2026-08-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03fdd9e3-025a-3eaa-bfca-ace2bed8960e | -5.82368 | -43.46786 | 2026-08-22 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e13e9a2d-20e5-38b8-8924-1b911734f68f | -5.61746 | -45.69431 | 2026-08-22 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3c3b05fb-4160-399d-b204-26617260933f | -7.07755 | -45.00112 | 2026-08-22 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 95ba06bd-84e3-30a2-ae2c-0df18417f7b7 | -2.56561 | -47.24608 | 2026-08-22 04:25:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f9970e6-974b-35f8-8601-dc9b3eceb3c6 | -5.09972 | -37.96024 | 2026-08-22 04:25:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| e20784bf-1f53-3ac4-a2c2-7e24a2148064 | -6.95996 | -44.23492 | 2026-08-22 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57e3f5bb-cf33-315c-a61c-68ebba0dc2ed | -5.76112 | -44.87468 | 2026-08-22 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ce9ec35-b7fd-3c46-aaed-ad14ca073895 | -6.24843 | -43.70016 | 2026-08-22 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7379aea7-1747-3d45-be89-25d249c383d1 | -2.50246 | -48.13414 | 2026-08-22 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 9846bb52-bc89-36b6-84ae-ee753cd5b842 | -6.25371 | -43.68903 | 2026-08-22 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5904f79d-b940-32fb-8261-0a9c7f3073a1 | -6.25078 | -43.68456 | 2026-08-22 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bd809764-eebe-3cdf-8026-629b957b6363 | -5.09568 | -37.95693 | 2026-08-22 04:25:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 6d4f7e48-1ce4-3da8-a85d-351f2931d18c | -6.34654 | -44.07565 | 2026-08-22 04:25:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6b462e57-d319-3e99-81dc-321074d2c289 | -6.87929 | -43.74044 | 2026-08-22 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3340e7ab-d99e-3a9c-a6e8-9350c3ab6170 | -2.89517 | -48.7967 | 2026-08-22 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 7a8509af-65e2-3cb1-b35e-4f966c171c96 | -5.10065 | -37.95777 | 2026-08-22 04:25:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| f896df38-a29b-399c-83e4-c4b5387b3138 | -1.74811 | -55.24944 | 2026-08-22 04:25:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f11c0d0f-041a-32c4-8997-5a439ffee9f5 | -5.59027 | -43.99946 | 2026-08-22 04:25:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e071b917-cb66-38e1-8a16-e16dd8d7f7a6 | -6.22025 | -43.74411 | 2026-08-22 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a8b923e3-5c0b-3624-8995-fb9415290470 | -5.59315 | -44.00377 | 2026-08-22 04:25:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5255e14c-819a-3d31-aa79-d84b47a4761d | -5.60117 | -44.02052 | 2026-08-22 04:25:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e53e1253-b47d-3fde-b657-581172676a0a | -4.06145 | -49.10821 | 2026-08-22 04:25:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f9796449-892c-3d63-9b75-4c3f75d9bd71 | -6.79353 | -42.6727 | 2026-08-22 04:25:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| bed7a8bb-f8b7-3525-bfd2-f12bd2ef7a37 | -3.0165 | -51.05461 | 2026-08-22 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5b8799b4-41b8-3e04-884a-1aa01a49081b | -4.16619 | -42.44003 | 2026-08-22 04:25:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 4796d02c-cb67-3796-9b48-081588d2a439 | -4.6543 | -42.43184 | 2026-08-22 04:25:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b98e2779-94a9-3040-8b43-e849cc5dfd59 | -5.58221 | -44.00598 | 2026-08-22 04:25:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 43fd98f8-46bb-370d-9bab-fa37b7f441ce | -3.54144 | -48.18634 | 2026-08-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1bdda3bd-f66f-339b-9227-0e0ee5c6230b | -4.2693 | -48.19519 | 2026-08-22 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6857562-e85b-35e2-83b6-d77ab8f8f90a | -5.61076 | -44.89877 | 2026-08-22 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 974c397f-16bc-345f-b396-b55823821a67 | -6.78872 | -42.66966 | 2026-08-22 04:25:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 823589ab-63d7-322a-a6fa-095380338f73 | -6.34943 | -44.07995 | 2026-08-22 04:25:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 619a3007-b111-3f2f-a496-97855fedf2b8 | -1.98789 | -56.46889 | 2026-08-22 04:25:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2153c784-41a8-35f8-b81f-628ad1890103 | -5.60176 | -44.01671 | 2026-08-22 04:25:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 66dc202e-1eae-3d24-ae39-30f42ae7d4f2 | -4.52886 | -54.85873 | 2026-08-22 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de16026b-6c57-3d30-b5e9-12e27df322cc | -1.9886 | -56.46446 | 2026-08-22 04:25:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce8384a3-a9ea-3ddd-91bc-518aa8eddab7 | -5.59719 | -44.00048 | 2026-08-22 04:25:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d05225e8-af6b-3adf-b89c-fe65ba2179ae | -4.94245 | -55.78096 | 2026-08-22 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ee0a32b-9ab7-34f7-9592-758e647b1388 | -6.34595 | -44.07949 | 2026-08-22 04:25:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0525370d-8e81-3503-b6ae-589d767b2263 | -6.72629 | -48.11202 | 2026-08-22 04:25:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5825677c-79d1-33b6-a87f-b9c08cf3e611 | -4.16985 | -42.44061 | 2026-08-22 04:25:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 42812f12-ca0e-38f2-8c9f-91a331030227 | -6.87222 | -43.73937 | 2026-08-22 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de969ce2-84e5-396e-aec1-13ea355dd2e7 | -5.60404 | -44.02483 | 2026-08-22 04:25:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf332797-f4e9-30be-9e21-ea4802d4d033 | -4.93689 | -41.97989 | 2026-08-22 04:25:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 216405b3-82fc-3bcf-9d96-37b162446856 | -5.71571 | -44.66488 | 2026-08-22 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cacb540d-3240-323f-8d07-17c8c502b15f | -4.66128 | -43.1352 | 2026-08-22 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 78c2a620-2d78-3499-b222-8296da9f5496 | -7.17285 | -42.7461 | 2026-08-22 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2e600238-13a8-3a32-911a-1d9e86b72402 | -5.53515 | -46.61511 | 2026-08-22 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fb6d26ce-f63e-30fe-a992-5a2ac839032b | -5.82837 | -43.48496 | 2026-08-22 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 0508f30e-5b16-3089-a5bf-137257ed6e18 | -6.87516 | -43.74391 | 2026-08-22 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 471d48e8-b0ad-3bf8-b672-64ed30f9f63a | -6.91436 | -44.97258 | 2026-08-22 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0e57c0f-7403-379f-a597-b113834fbbed | -5.60743 | -44.02065 | 2026-08-22 04:25:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc36646b-8e9b-30f9-8ae8-de7f6abe01fc | -3.54346 | -48.1827 | 2026-08-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| acc98479-4be3-3066-83d8-c54834e42101 | -3.53506 | -48.18141 | 2026-08-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a075cad7-6d2c-3dbb-ae69-9d7f24e88074 | -5.58853 | -44.01083 | 2026-08-22 04:25:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a7bd287-84c4-3cc6-8464-0d7423fb76bc | -3.4291 | -49.4775 | 2026-08-22 04:25:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 68364204-a91e-30af-b9a2-2b52601ec350 | -5.71445 | -46.18694 | 2026-08-22 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6228a063-8092-3eba-8683-cdb2cd303062 | -5.96602 | -51.96679 | 2026-08-22 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 56921635-3c98-313d-94c3-5599c012afd2 | -4.18014 | -48.57583 | 2026-08-22 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cdcc324d-a7cc-31dd-8826-991eae881caa | -5.96729 | -51.95902 | 2026-08-22 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README18.md)
