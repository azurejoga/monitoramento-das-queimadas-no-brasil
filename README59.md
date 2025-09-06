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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 91b2029d-4b72-32cc-afed-80e6f85991dc | -8.83486 | -52.00879 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c1d38bc-618f-3fc5-9230-4fe36d92ecd8 | -6.60701 | -43.96758 | 2025-09-06 04:38:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9074da37-5205-3ed8-bf72-d408c468c934 | -7.33564 | -43.94625 | 2025-09-06 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 653d47b8-7f9b-3d1f-9d31-87cc4508ddbf | -5.8484 | -45.30972 | 2025-09-06 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea36afc4-f106-35db-b015-f85b79f0a71b | -6.54291 | -49.51139 | 2025-09-06 04:38:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 78138bd4-7e24-3552-af6f-03265e72134f | -6.54346 | -49.50793 | 2025-09-06 04:38:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ffbcb05e-5398-34eb-8f27-3fe54290b190 | -7.79437 | -52.12777 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7619bf94-d3a2-3661-9f33-3c2083aab596 | -9.02027 | -49.80164 | 2025-09-06 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cbd3fb3c-4921-349e-a9a6-7c7326d12b95 | -8.08825 | -45.31486 | 2025-09-06 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3db37f79-a1a2-38be-992a-a67ed5ddd7ae | -6.45827 | -55.88771 | 2025-09-06 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 389c2da1-6d6b-346a-81cf-d8e94fee1f80 | -5.94621 | -42.96497 | 2025-09-06 04:38:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c5ef1888-2fb8-3e71-abf1-1dc0b486a3b5 | -9.87878 | -46.54239 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| df1c39cb-8e1e-3426-9310-f76a6a6e5474 | -6.45634 | -44.67635 | 2025-09-06 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 34d200cf-03d3-3c5c-a9c8-883b5349b63e | -6.34619 | -53.44704 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b20448cf-36d3-3c09-8180-fb100c652e0c | -9.00702 | -49.79954 | 2025-09-06 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ba9c65f-af15-3056-a846-6c296d388519 | -7.35133 | -44.32077 | 2025-09-06 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c130836d-6a6d-3a0b-81fd-d303e934c0e1 | -5.55914 | -46.54363 | 2025-09-06 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ef5dc8e3-7b95-3b1a-a287-eca027d74a6b | -5.90219 | -57.71895 | 2025-09-06 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7fb7b506-68a3-315d-91d7-9b23bf4c521f | -8.09309 | -44.81862 | 2025-09-06 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9739cec-fe60-38f1-bfa9-c7bd22537f4d | -8.86191 | -52.01271 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72677c08-fcd9-3105-978e-35c58c4292a7 | -7.3304 | -48.4935 | 2025-09-06 04:38:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f5f73d52-b9ea-300a-af64-6adb048cecdc | -4.99796 | -56.2599 | 2025-09-06 04:38:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a95e5739-cdc3-39ee-92ee-3cbb94c3138a | -7.98879 | -45.47143 | 2025-09-06 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dd3d2c12-1cae-3011-8ede-f87a2189ab6b | -3.16284 | -48.60744 | 2025-09-06 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 20c343fb-e1f0-3d24-bec3-034efdf9b9f3 | -8.35321 | -52.54381 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bf22269d-7685-38bf-961d-30a337aa6e00 | -3.16215 | -49.47357 | 2025-09-06 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4addb405-6d57-364d-8fe1-d585cecfa1e9 | -2.93735 | -49.45581 | 2025-09-06 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6640327f-dfec-37a5-88d8-f559f115b13a | -6.47328 | -53.40673 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5dca0e26-72e2-3dec-b13b-e8d6faec5a05 | -6.54237 | -49.51484 | 2025-09-06 04:38:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e36a86c-e935-3edf-ba07-ae14aef6179f | -6.82012 | -52.80926 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0a17f7cb-19fd-3e92-9edf-49cac4c85e3c | -3.6902 | -49.5708 | 2025-09-06 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 752cda27-5836-3987-80db-2364626a7f26 | -9.08572 | -47.00184 | 2025-09-06 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 077372b8-8aff-3cf7-a254-e758f195ac83 | -8.51048 | -51.3229 | 2025-09-06 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d1273f3a-950f-357d-9822-9152545a08c1 | -5.49371 | -42.15167 | 2025-09-06 04:38:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e02dfaa6-b41a-3388-89cb-ae29bfd0ce6b | -6.3879 | -43.81546 | 2025-09-06 04:38:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f83733d-07fa-39f9-acbe-3b4d1d357bd8 | -5.95207 | -53.80411 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8186b0fe-3eb2-30f0-80e5-cf69c265b5d4 | -9.77976 | -46.91105 | 2025-09-06 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c24384e-cc1a-3a17-a05b-d618e0cc9ca8 | -6.86972 | -52.77863 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d667136-3100-3eb4-a5ea-780968880b86 | -5.46858 | -44.13077 | 2025-09-06 04:38:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea4eacc6-ddd0-3046-a63e-d7730167dba8 | -6.04615 | -51.6888 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57380b89-d97c-382a-9a72-1bc6cc6d15e9 | -5.53753 | -43.08602 | 2025-09-06 04:38:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 005727e8-0b87-386d-af6a-4455a53e03c5 | -8.364 | -48.2703 | 2025-09-06 04:38:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9334ff3-98fe-3a63-8f67-1b1558d65fec | -8.4914 | -45.10477 | 2025-09-06 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eebfeb90-04e8-32a1-8963-12285a02bc72 | -9.07887 | -50.4211 | 2025-09-06 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0057a57-b3f0-3cab-9ff4-6deb83a7e95a | -9.05733 | -50.44981 | 2025-09-06 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ffe10027-85e1-3ab3-b129-9aa8f89825e8 | -5.95954 | -43.0283 | 2025-09-06 04:38:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e18c09d6-3efc-3610-9e40-a9bc6797a9c6 | -6.99987 | -45.6501 | 2025-09-06 04:38:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7a6f351-452b-350a-a265-b02c34c37a61 | -4.48188 | -47.66593 | 2025-09-06 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eccf0f34-072d-3364-bbe3-9a3df904e735 | -6.44374 | -58.14766 | 2025-09-06 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| a96e8222-3393-3fc3-a9ae-006f0908b4ab | -5.99978 | -46.68808 | 2025-09-06 04:38:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e49bd34f-40ad-3739-88ef-edba41f76afd | -8.06332 | -52.38967 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d2b8a454-5607-376a-bd0c-4f5dd9af6200 | -7.32984 | -48.49705 | 2025-09-06 04:38:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 32b2e37c-2c0a-3684-909e-370a48f19aee | -6.83166 | -52.80696 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28d7ad73-b13e-35f0-aeed-9a808aa7de5c | -8.44501 | -45.03166 | 2025-09-06 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1202a9c9-27f9-373b-b907-e83084f3f6c5 | -6.19928 | -43.42104 | 2025-09-06 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1e6bd433-80d3-3ad9-a287-6d0c0c09b12d | -7.38517 | -50.90342 | 2025-09-06 04:38:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 780fe2c6-f09d-34b3-89dd-3773871bf372 | -5.67958 | -45.17449 | 2025-09-06 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5c83ad8-fe1e-346f-82e5-ed1cecd43d04 | -7.41801 | -44.94386 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| de4e3dc3-3a47-308f-9a55-a44a9684e307 | -3.69739 | -49.56837 | 2025-09-06 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 34b2aba0-332e-3026-98ad-5de8f6eac51c | -9.08685 | -47.01874 | 2025-09-06 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6ddf8583-b747-3915-af9e-e5dba3ab5789 | -6.83959 | -52.80397 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6fcff219-9a55-38b6-87f2-9f603a9e2ead | -6.40829 | -43.82272 | 2025-09-06 04:38:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5134bd98-cf35-3bc7-9319-c7309e484921 | -3.03718 | -49.42513 | 2025-09-06 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb0f1d3c-3215-37c7-a47f-9eb6d7ce260b | -5.89768 | -57.74518 | 2025-09-06 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 71365e67-c345-3d2e-8c42-25c98f919df2 | -8.35189 | -52.55178 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0dfb54fa-a293-39e5-955a-90fded5f6460 | -6.36431 | -43.53833 | 2025-09-06 04:38:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25c35192-2b11-3cd1-8f23-d9b6b20ee4a4 | -3.47983 | -48.94626 | 2025-09-06 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9e4147e7-a01f-319a-a3d5-f62b374dc2a5 | -5.91583 | -57.73033 | 2025-09-06 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 074d173d-18f2-3bd9-a5b5-f0be51bbc50c | -5.90431 | -57.73685 | 2025-09-06 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cf4dece9-d16e-3238-b7af-e5befadad812 | -6.64445 | -43.41655 | 2025-09-06 04:38:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d676b2eb-7c2e-3832-a385-816e7276073b | -6.20277 | -44.19548 | 2025-09-06 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7099e706-20c1-32a0-8b75-bfa1b5b8489b | -8.64226 | -45.7497 | 2025-09-06 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 080d64fb-4a43-3ffe-9082-73cece7dee2d | -5.85808 | -46.10616 | 2025-09-06 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c40b48ec-db67-32a8-b7b7-80ad28f4f914 | -7.68533 | -50.25474 | 2025-09-06 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7514c029-b19c-3894-bf8c-c172965426c6 | -8.3674 | -48.27083 | 2025-09-06 04:38:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2992fb1d-e53c-3e75-a894-9cd3870e97e8 | -6.07325 | -43.3013 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 29ad11ed-6858-3267-a2cb-0e4c6a01ff18 | -8.89083 | -47.26221 | 2025-09-06 04:38:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 72e9d432-b2fc-3b70-b58e-5c69683258cb | -8.3536 | -52.5197 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3fbb7e97-c9ee-3f11-8556-600a52a2f0d3 | -8.51443 | -51.31981 | 2025-09-06 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88c54d38-4909-377f-bcaf-31b84e73ccd9 | -6.27373 | -53.4395 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 131be0e4-928a-3915-b2f7-35cc347e91d9 | -9.7737 | -46.90151 | 2025-09-06 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e6bf7ae-c61a-3f5b-b05b-ce9bbbd932d6 | -8.44147 | -47.31964 | 2025-09-06 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 61bc544c-8580-3247-8027-e1604b54a139 | -5.86756 | -51.72322 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa4b2137-6ee7-312f-91e7-6df3a75a3766 | -2.55925 | -48.96733 | 2025-09-06 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be26c3e6-4917-3fb0-bb67-c3ce3ea8ee6f | -8.34355 | -47.48632 | 2025-09-06 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 11d8d97f-8e73-3f28-9e60-a8c27b42f1d1 | -9.01033 | -49.80007 | 2025-09-06 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30ccf3e5-3847-3bf7-8c2c-ea542ea7d69d | -8.36527 | -52.55828 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ce971d4e-7d1b-3d1b-9dc5-5c1c9dc7b56d | -5.95153 | -53.80194 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3ded0681-8baa-37aa-9907-a33b29dab766 | -6.26465 | -53.44741 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2fda985-b83e-3f9a-9bb0-ff36477ce18e | -9.77006 | -46.90096 | 2025-09-06 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0818792a-14d8-351e-bfcd-d699d63c39ba | -2.85199 | -49.49952 | 2025-09-06 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 71d8c3de-357e-36c9-af66-12a1c5329e19 | -5.91685 | -57.72437 | 2025-09-06 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e241136b-1817-35d7-b6dd-c7cc5e090bf7 | -3.25013 | -50.80225 | 2025-09-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4c29f01b-86ad-38d1-9738-4f98e7e62e10 | -9.30603 | -45.4174 | 2025-09-06 04:38:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4d24f6f8-8010-3c28-813a-f29f9e8e7074 | -7.20941 | -43.98459 | 2025-09-06 04:38:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cde9c6a1-7f30-3372-ba07-29273d4ce9af | -6.01405 | -46.68933 | 2025-09-06 04:38:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f9e8d9bf-ffe2-347a-b5b3-1f14eff587ee | -6.15851 | -43.17268 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 39f9ce38-f878-35e7-8b91-14f8794a0a5e | -1.34493 | -55.47197 | 2025-09-06 04:38:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a9bff70-ee33-3b6e-b93b-cf86750ece06 | -5.21397 | -43.69174 | 2025-09-06 04:38:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d37f2dd-1e16-314a-a71a-e9fe1acaa036 | -6.35939 | -47.09956 | 2025-09-06 04:38:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README60.md)
