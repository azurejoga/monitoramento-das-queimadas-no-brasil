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

## Dados Diários - Página 155

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d6fc6af-a950-351c-be09-3ee9a68630a7 | -8.97764 | -50.97797 | 2026-09-28 17:09:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3da3bbbf-a6af-362b-9163-c5a8eebdcaba | -11.86235 | -50.88465 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c059a2f2-3e01-37c7-a5f4-fae331149150 | -7.9039 | -54.75259 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| fb210abe-5fb7-35c4-96dc-9a5729e743b0 | -7.3814 | -44.76513 | 2026-09-28 17:09:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 2f8ba801-48f5-3407-8ce2-7bfab6400b52 | -10.96733 | -50.69231 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e563051c-08a0-3d1d-b1e0-460369ea5afd | -10.51556 | -45.36552 | 2026-09-28 17:09:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 0b84734d-57fc-3be6-8c22-aef78047802b | -7.04707 | -44.29912 | 2026-09-28 17:09:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8430547d-b460-3078-83cc-087bc1db9fc8 | -8.03282 | -42.85677 | 2026-09-28 17:09:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 7e80d36e-8e5c-3998-91c0-21601535a313 | -12.38074 | -50.23422 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 8ea5bf99-71bf-3439-b054-a1d3cb3f8036 | -7.41628 | -55.63548 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 9202ea33-17d4-3e92-95cb-d3528d9a31ea | -5.27545 | -48.37652 | 2026-09-28 17:09:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b3665807-19b0-3d14-a26e-96ce932784e6 | -12.1603 | -50.39985 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 83d2ebed-fdd6-338e-90ca-ec6197fe90b7 | -12.78872 | -54.02231 | 2026-09-28 17:09:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 943b064f-5690-3aef-b35f-c0ff2e10a573 | -11.07797 | -48.88944 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 8f4c074e-92c7-3aa0-b149-c92f03fdb099 | -12.76575 | -52.81565 | 2026-09-28 17:09:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 341ef845-f9d8-3d05-9698-bbeba198a50b | -8.30459 | -45.42868 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 87ec47ee-9381-32e3-9e02-11a74332d685 | -8.26763 | -54.70888 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| f78686c3-06df-3392-8b6e-87672c26d702 | -12.37702 | -50.23487 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 31.7 |
| fe47e887-b1cb-36de-b9ca-082e71f9e9d9 | -11.39683 | -45.41713 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ef965283-04a3-31c2-877a-1626071feb8f | -10.94747 | -43.88933 | 2026-09-28 17:09:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 6aec5c0c-6b3b-3a49-9433-1ed13e56dcd7 | -6.33502 | -55.31757 | 2026-09-28 17:09:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9f6ce5f3-2839-3797-a841-0fe5c576fea0 | -12.75627 | -52.82092 | 2026-09-28 17:09:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cb324b3b-9d88-34ae-a7f2-656f4f519d5d | -11.45252 | -44.93019 | 2026-09-28 17:09:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| fc9b203d-d05a-3afa-8459-ff86eab0865a | -9.26035 | -47.36349 | 2026-09-28 17:09:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| c34e2809-7551-3df3-b939-ccb3f37faec0 | -7.75909 | -54.78219 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| e15ad85d-6c4b-330a-b3e3-f4902a0631bd | -9.16871 | -51.4672 | 2026-09-28 17:09:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| b5108dec-13ea-3b2b-81c8-c0dd6bfd9ee8 | -7.70441 | -44.93066 | 2026-09-28 17:09:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e218d144-3819-3748-b148-3b83bc06c13a | -10.16015 | -46.57284 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 33.5 |
| a45308c4-fb3d-3fd5-9186-a277f39b66c9 | -9.96695 | -50.14963 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 3c7b31b1-d575-3816-9568-48c1968bcf1c | -10.82763 | -60.73933 | 2026-09-28 17:09:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| e12b0b04-7c10-3311-b4c2-d5d0b53236ba | -7.76293 | -54.78515 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 82f3e88b-989f-34f8-badb-a8e05a8bfe23 | -11.47926 | -49.75052 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 4739ad90-f3db-34e6-81ce-51aee082f136 | -9.59649 | -49.64614 | 2026-09-28 17:09:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 13c972ff-6d6c-3ca7-859a-a86e0d7a0036 | -10.80964 | -60.7375 | 2026-09-28 17:09:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 55d8ec36-6ba7-3109-ab29-ad23646009eb | -10.87274 | -56.21598 | 2026-09-28 17:09:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9f491c58-d003-3d00-aea5-f684e57e0dd5 | -9.51134 | -46.37656 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4bc02ecf-4b41-34ad-a8dc-2611ec1334a3 | -10.01351 | -46.01851 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 1ba9314e-52bb-3a8f-958c-b4e121898f7f | -8.65378 | -45.34918 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 56acdc67-c56d-3c3c-98b4-ade5796ccdaa | -10.82622 | -57.22972 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 328436db-cae2-3120-a9a7-a7a0d3a33e3b | -7.67849 | -54.74575 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| c8d882ef-892f-3f47-8781-8c862e6e6739 | -5.55961 | -47.4808 | 2026-09-28 17:09:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c27d4d0-3bdd-3476-a9b4-eb01e7f30eb0 | -4.37252 | -43.06578 | 2026-09-28 17:09:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e8293dd1-2b54-3f54-94cf-0c19a6cb6f09 | -11.98112 | -57.60986 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c43fd8bd-bbfc-3ffb-9e50-e080a68953ea | -11.56125 | -47.39117 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 02d47bc8-4a22-3d07-beed-0635ac4d2e98 | -4.31932 | -46.64519 | 2026-09-28 17:09:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 78970397-4199-3760-a8ae-e65c3c8a1c04 | -11.19549 | -44.80544 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 2ce9c5b3-813d-3654-9faf-fcae17264b31 | -9.18297 | -60.76258 | 2026-09-28 17:09:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 28124dd4-219c-3f14-b9ff-3be2ac42c9b7 | -6.68424 | -45.64557 | 2026-09-28 17:09:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| e581b3d6-2879-3a76-9fb9-6571993c6671 | -9.94064 | -50.2381 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| fa06c729-7229-303a-9501-7a66025af3dc | -6.68434 | -45.64444 | 2026-09-28 17:09:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 84a62b26-94b9-3cb4-8f29-64c186ac7ca2 | -11.84284 | -50.85701 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 248c34d9-39e3-3eee-ad81-130d886bca73 | -7.69374 | -54.77897 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1a4863ec-1f09-39d1-b9df-b3cc4fa0ae21 | -6.88914 | -52.47982 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| df21e9e2-cfaa-30d4-ae90-0c824c6fcb7e | -5.111 | -45.79932 | 2026-09-28 17:09:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 18.3 |
| f9ae1d31-89f2-3b42-ab17-850b177a0c58 | -7.20809 | -47.60627 | 2026-09-28 17:09:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 30b1f696-859a-3e12-a8d7-153f578e7306 | -7.2512 | -43.35526 | 2026-09-28 17:09:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 13ac95c3-de19-310f-9afe-0678531ac0f7 | -6.81779 | -45.05729 | 2026-09-28 17:09:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| b20170f0-812a-3d20-a4b1-9d6d5bf45e42 | -7.6977 | -54.76058 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| beb96d60-c7f9-3d19-9fee-92985282ddca | -10.94019 | -43.88248 | 2026-09-28 17:09:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 02f4dfd7-fb2d-334a-951d-9351c0dd1823 | -10.72141 | -53.99494 | 2026-09-28 17:09:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| c53273a8-d279-3238-b848-3ef864d48ba3 | -8.35064 | -64.07895 | 2026-09-28 17:09:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 4855077f-94e0-3c51-965a-cd14b608213b | -11.0539 | -47.67088 | 2026-09-28 17:09:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 3b555ef6-0e6d-301c-948e-4530fbaa6791 | -9.51709 | -46.06471 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 62d8921d-d438-32e1-9797-74b7b42e2dfe | -11.15385 | -48.32968 | 2026-09-28 17:09:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| d55f85b3-4203-3b88-9fcd-9a1457a88d3b | -6.16171 | -52.89941 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| b9038c89-482a-36af-9438-05f24f6e7f38 | -10.82532 | -57.22472 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 82170845-c1a3-3efb-80f0-55e2a0a706b8 | -8.285 | -54.70921 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 291446b2-1801-3a85-a156-2c004e8a71b6 | -10.45949 | -47.4925 | 2026-09-28 17:09:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| f67cf67a-a812-37d8-8803-53004c7faa2f | -7.32872 | -42.08582 | 2026-09-28 17:09:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| be665411-3b09-3dd1-b18f-8b3aea7411da | -6.15819 | -52.89994 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 715b70c8-1c13-3e35-9aaf-48b9bfb3a1a2 | -7.2613 | -45.34167 | 2026-09-28 17:09:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 311f8728-2ffa-333a-bc4c-fcaef4cba9b6 | -8.73237 | -44.90678 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 8b83b0f5-e68d-30da-ad7b-fd8618ca07b1 | -7.99553 | -43.26358 | 2026-09-28 17:09:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 8836a768-b70e-371b-8917-7c4bc1bad56e | -10.82179 | -57.22524 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 261afbaf-c9be-3b7b-b9e7-f9c7b4d0bd02 | -10.81297 | -57.21424 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 2eadf76f-b298-3cc7-afc6-15e57998c7b0 | -9.79652 | -48.21409 | 2026-09-28 17:09:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 1b8a7484-1be9-3678-a157-a2016931e300 | -11.12747 | -51.18517 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 87bbdf78-a72e-3899-83c0-20c4ed1d0130 | -12.16247 | -50.3902 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 6c7afb62-d41c-31db-8374-7143a2035423 | -9.34324 | -65.75795 | 2026-09-28 17:09:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| b0e769a5-2b65-354f-8253-38356973a0d6 | -9.34938 | -46.53968 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 089e768e-bf02-3e9a-9f4d-1720cae75d79 | -11.05837 | -47.67004 | 2026-09-28 17:09:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 5a1518a5-175e-376f-8059-6f21fcd02851 | -11.21162 | -44.80199 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 0843be5b-e746-37df-83bf-af55a049b1b4 | -6.20411 | -52.91702 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| fb66da30-734a-3f2c-95b6-3fa950df8293 | -10.93241 | -50.66589 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 027ac8e5-a62d-3b98-908c-0055e64280f1 | -9.45171 | -45.9679 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| add69f59-a53e-3026-bb65-d6962ca510fe | -10.91747 | -43.85748 | 2026-09-28 17:09:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 0c50ce78-12e2-3c7c-a93f-a84c63d778b2 | -11.38906 | -45.39676 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 33f50096-0492-390f-9239-554cf375048e | -8.61228 | -63.78589 | 2026-09-28 17:09:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 27b3b83e-b1cd-3c17-820a-f0a4cb90ba56 | -7.77777 | -54.68322 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0ccf5b0a-008f-3d44-8058-aca622557dae | -11.39844 | -45.41794 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d9fa2fa3-4524-3b48-b1dd-d071ed8783ea | -11.53029 | -47.16753 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 710ac202-5b22-3722-af3d-c1290ae75943 | -11.22237 | -44.79967 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| abda73f6-7c5b-3eb7-b2a6-550482351ef9 | -8.64416 | -45.35833 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| af493928-5353-337e-84e3-7b3bed47b47d | -7.13042 | -47.61065 | 2026-09-28 17:09:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 4d73d511-5e3c-3d4f-943b-5e784dd5550f | -12.1611 | -50.39349 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 69643826-c4c3-323b-97e9-6829df34e164 | -7.98702 | -67.24168 | 2026-09-28 17:09:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 24.1 |
| c7e2dd61-ee87-3571-b008-83f21798ea87 | -7.76624 | -54.78464 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 23e0cb24-ffc6-3bb3-9b22-97e39435b8b4 | -7.03785 | -45.81956 | 2026-09-28 17:09:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e0cd988f-9d68-3054-a3f8-99c966f900e4 | -11.84563 | -50.89636 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8f356035-33c2-36ee-a149-4b01ef4f0604 | -7.4581 | -64.32812 | 2026-09-28 17:09:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 39.4 |


[Clique aqui para ver as próximas entradas](README156.md)
