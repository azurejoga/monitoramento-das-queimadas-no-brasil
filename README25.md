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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9637bb61-595c-3833-9f51-953c83466fdc | -11.17537 | -55.91888 | 2025-06-27 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 858ef441-7b8f-3d17-b9fb-db6d42ac4065 | -10.10875 | -64.91896 | 2025-06-27 05:10:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aca8a4a3-b329-3ebb-a020-4519d5d16f99 | -11.06184 | -55.37085 | 2025-06-27 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b6a8c846-2e6b-3527-9be5-dc53f65c8fbc | -11.44199 | -54.46611 | 2025-06-27 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a762f8bd-19db-3d90-b9b2-a42aa8fe624e | -11.77203 | -55.03698 | 2025-06-27 05:10:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 676884f5-3057-35c4-bf89-6ea611c6ba2c | -10.87126 | -53.76742 | 2025-06-27 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c602b41-7688-3c41-8c3b-f02dbb3cd19c | -11.05762 | -55.37448 | 2025-06-27 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5582b718-a1c5-32a6-9b3c-875bc1b3070c | -13.10203 | -52.29224 | 2025-06-27 05:10:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d31370d4-70fa-32b0-98d9-398516efd6c8 | -9.34028 | -58.85361 | 2025-06-27 05:10:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eda5acdf-be90-3590-b401-79b83f85e266 | -10.70866 | -59.13784 | 2025-06-27 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65ae5fc2-7267-37bb-ac16-61634c614544 | -6.77775 | -46.32674 | 2025-06-27 05:10:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 26b33ce1-e119-31f9-9997-e0425803266f | -9.35469 | -58.84872 | 2025-06-27 05:10:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90fcffd6-ebe1-3b9e-aa86-7cdf722b02f7 | -10.86288 | -54.3019 | 2025-06-27 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64dd5878-7a5d-36d3-abf9-416f0175a81d | -11.43741 | -54.46766 | 2025-06-27 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 34a78474-4a25-3af9-9ba6-7a722d4c2985 | -10.80764 | -57.75544 | 2025-06-27 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a5344059-259a-3b64-a751-4d0636d2c7a7 | -9.11393 | -49.43845 | 2025-06-27 05:10:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8bc7b336-be4c-3ba4-a41b-2d064380444e | -8.47782 | -50.2767 | 2025-06-27 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5b33b65-cb55-3f33-9f4f-8a3752c134b4 | -9.79249 | -48.56658 | 2025-06-27 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2d0fbffb-4061-30c3-885e-ea9835473c8c | -9.23433 | -50.03092 | 2025-06-27 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| db2d056a-1810-3c5d-85d8-e9a7855443c4 | -10.87054 | -53.77245 | 2025-06-27 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b83d073-bf17-358f-9f5f-1c7e0572dd1b | -13.04337 | -48.82168 | 2025-06-27 05:10:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 054ba0fc-9b74-3f50-b836-59a335dd8f97 | -8.61402 | -51.57797 | 2025-06-27 05:10:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8e533709-03dd-3d10-bc6f-5cf525b25bae | -10.82962 | -54.05505 | 2025-06-27 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef1685c4-4816-393b-96c1-9b48cc1c8521 | -9.74622 | -48.04408 | 2025-06-27 05:10:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f2c8c0b-aba4-35ea-aa78-3a02bf2ee907 | -11.77767 | -55.02422 | 2025-06-27 05:10:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 623a14a3-c255-3e54-9c1d-afe34a70a79f | -11.77507 | -55.04194 | 2025-06-27 05:10:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51405e83-b844-3022-a0f2-d2c6f4fcec6e | -10.71035 | -59.12725 | 2025-06-27 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a56f9c2d-94ae-3660-8985-e673fc1133eb | -10.3624 | -57.25729 | 2025-06-27 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9eed5852-01b7-3b14-b8a8-b82ed05a65f4 | -11.77332 | -55.02813 | 2025-06-27 05:10:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 535a447f-8b1d-33f6-ae3d-82f3064e1467 | -8.33547 | -55.09415 | 2025-06-27 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e71da34-f6d0-38c8-863f-beb1ed38d38b | -6.17356 | -48.08836 | 2025-06-27 05:10:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 699679b1-d6cc-3dbd-92e0-b2baa0423c85 | -10.70759 | -59.1232 | 2025-06-27 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e97d9dff-2551-3886-8893-be6729731581 | -11.17828 | -55.92344 | 2025-06-27 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1050d94d-f78d-3d92-a1db-6e1d8d9b93f6 | -13.04381 | -48.81783 | 2025-06-27 05:10:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c2da4a2-bb79-3d15-ac3a-b78103f86926 | -9.47953 | -56.07416 | 2025-06-27 05:10:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c23b64f-0aae-3da2-86f2-489367f6d614 | -9.11473 | -49.43227 | 2025-06-27 05:10:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4ce91263-ae13-39ef-929d-3111c4a12f7d | -9.11689 | -49.43815 | 2025-06-27 05:10:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6a3b7f2d-6dbf-34a6-ba5e-56fb52df37b8 | -11.5794 | -52.11995 | 2025-06-27 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 001fd789-c8b7-3396-b544-28c9fc4ba1cf | -11.57055 | -52.11864 | 2025-06-27 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 40.1 |
| b77f11bd-e26d-39e3-b4ab-8b11ff0bb8d9 | -12.00553 | -47.16021 | 2025-06-27 05:10:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1e973fa-a050-3733-b88b-7689a023bd86 | -8.54254 | -55.03698 | 2025-06-27 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c628674-7b27-3361-a575-1f89ad70b47c | -10.71699 | -59.12831 | 2025-06-27 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9665f8ec-c52c-3bcc-97a4-bbf72e83d931 | -8.49014 | -48.26179 | 2025-06-27 05:10:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1aa1fee3-0312-3da7-89ff-4aeaab7de82b | -8.61977 | -51.5682 | 2025-06-27 05:10:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dd616911-dbd1-3a89-91b5-d95a633c9845 | -8.61528 | -51.56933 | 2025-06-27 05:10:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 78a9573d-c903-3a36-b5a3-c3c0c7696093 | -13.05157 | -48.82382 | 2025-06-27 05:10:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e65bbf1-e7b1-3600-af45-96813edb07b0 | -12.01115 | -47.16595 | 2025-06-27 05:10:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bbb5f86f-45d7-31da-985b-d4b6e756afcd | -8.61798 | -51.58124 | 2025-06-27 05:10:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a558a467-eb3c-302c-9b3e-6a23a1bfe7f7 | -8.61967 | -51.56997 | 2025-06-27 05:10:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e6677887-57b6-39ba-bf00-5a603a06e8bc | -9.36684 | -47.63169 | 2025-06-27 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cbe521d2-b934-38b8-9c0c-18e731aeb164 | -11.07532 | -55.07774 | 2025-06-27 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b85ae9d-b94e-3f54-b117-df70664a812a | -11.17477 | -55.92287 | 2025-06-27 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e15823f1-be75-35d6-94f5-98ccd948627a | -7.53139 | -45.82988 | 2025-06-27 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5369d3a4-18ca-3f9b-9168-7df4bee8f352 | -8.5467 | -55.03346 | 2025-06-27 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ae45499-e587-3a7d-be3c-f0236a8854c3 | -8.61477 | -51.5719 | 2025-06-27 05:10:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 58329ff1-0d61-3d60-a7ad-61ec28f46b50 | -11.60509 | -55.54699 | 2025-06-27 05:10:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 26224573-e69a-34b8-a63c-bf93fd907ef0 | -13.59007 | -45.25577 | 2025-06-27 05:10:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1bb83e6-9850-3e08-b4e2-646cdb6af205 | -8.61858 | -51.57686 | 2025-06-27 05:10:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9f4bb910-4975-3a04-874d-dfe0c9caca1f | -9.4973 | -56.09617 | 2025-06-27 05:10:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0f2fed3-7663-3bfe-aa03-e4915d6ff7f0 | -11.60349 | -55.54354 | 2025-06-27 05:10:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5b4fde77-bbb4-3b4d-aef1-1fd16c109a1d | -10.82646 | -54.04964 | 2025-06-27 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 238f98b0-1446-3486-bff1-9d2dcdabfcb8 | -10.8602 | -54.03463 | 2025-06-27 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd9ae704-e962-3e93-8c30-af1f82deccbb | -9.37501 | -57.55803 | 2025-06-27 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53a5e43d-1ab1-3ba3-a0e2-bbad3c1c37f0 | -11.057 | -55.37866 | 2025-06-27 05:10:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a7a44658-30a6-38d0-98b5-f53cc6b4fe92 | -11.82489 | -47.5382 | 2025-06-27 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5f7bbd02-f98c-36f1-8b2a-6cef2fd365e2 | -10.81096 | -57.75596 | 2025-06-27 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 486b5f14-f393-3087-a3c3-e40b259ce4f1 | -11.43675 | -54.47239 | 2025-06-27 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 250f2929-eb22-3a3a-9f1c-e7465b3d85aa | -9.07236 | -49.41936 | 2025-06-27 05:10:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 43880101-a31a-3a53-8097-ca2c4bdf309d | -9.12118 | -49.44498 | 2025-06-27 05:10:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13db1661-4dd6-33a3-86bf-6e33785a97c9 | -9.7519 | -48.04494 | 2025-06-27 05:10:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77ed931c-238a-3315-9aa6-19e21b77b79b | -10.52748 | -53.62346 | 2025-06-27 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6a37baea-ecde-3e0d-915f-c951d6f44ca1 | -11.77267 | -55.03256 | 2025-06-27 05:10:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb288615-9417-3293-9eb6-26d45ac6b846 | -11.77138 | -55.04138 | 2025-06-27 05:10:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 727fd8db-85ce-34cb-8623-03775ec48318 | -11.82228 | -47.54286 | 2025-06-27 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a943b119-6082-3ffc-a631-640581014ca4 | -7.14329 | -55.37299 | 2025-06-27 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bf666923-0169-33f3-a35b-99e7e797fb9e | -9.11433 | -49.43536 | 2025-06-27 05:10:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ef95d250-ed0d-3eb2-aa63-d8e1031afd5f | -9.11866 | -49.44228 | 2025-06-27 05:10:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fbf7b1b8-f8cc-3f3e-b929-3d37aa6c2567 | -11.84019 | -57.86087 | 2025-06-27 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 496a4b94-42f4-3363-b37b-0fdb244c23ac | -10.71423 | -59.12426 | 2025-06-27 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a97866f-4e0b-342e-a170-d88de30db893 | -11.43681 | -54.475 | 2025-06-27 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8474856-92e7-3e29-8851-7ffabd4c8d33 | -10.71311 | -59.13131 | 2025-06-27 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 347adc4d-7309-32a0-a9b1-5505ede9fcd7 | -10.63915 | -46.71065 | 2025-06-27 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d193dbc-ee21-3e52-b582-e78dac66ca9a | -11.36144 | -48.71493 | 2025-06-27 05:10:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e75d657f-cf2f-39ba-943f-074c752d46da | -11.57113 | -52.11428 | 2025-06-27 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 40.1 |
| c289db4b-598c-32a0-889f-7a0406e3997a | -11.36096 | -48.71037 | 2025-06-27 05:10:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a05deeb-8ca6-311a-ae70-a7cc7ab524a9 | -11.44433 | -54.47353 | 2025-06-27 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0512a5fe-6843-3b3d-8f93-d68b2ab3a79f | -9.78697 | -48.566 | 2025-06-27 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77fa5ba3-0ae5-39cf-812d-26780f501a82 | -8.61418 | -51.57622 | 2025-06-27 05:10:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 393a5b9d-a417-3466-ab29-567bbabbf667 | -11.75297 | -54.23358 | 2025-06-27 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a34a766-7095-32c9-9754-d633732303a3 | -11.36653 | -48.71104 | 2025-06-27 05:10:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f8e19d77-888b-35e3-ae6d-fd09733bd930 | -12.02748 | -47.77419 | 2025-06-27 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 810afcef-6621-3a52-8ae2-769c5e8368f7 | -13.5823 | -45.26191 | 2025-06-27 05:10:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b7dae93-113e-3209-aeee-fd1b7c33e6e5 | -9.11731 | -49.43508 | 2025-06-27 05:10:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2a66e6ef-4028-314d-9f34-e0c988393df6 | -8.11838 | -55.07198 | 2025-06-27 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 9ac0862e-c026-3f3e-b5cd-503e63b0bcbc | -7.55041 | -45.83286 | 2025-06-27 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 52869d6d-4a60-303b-b799-6e64323266fa | -10.23012 | -56.75273 | 2025-06-27 05:10:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b29ec686-4e93-3778-ab7c-3adaaedbf6ce | -11.4375 | -54.47029 | 2025-06-27 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa6b0f1c-1591-344b-9e70-7d797b671de2 | -11.50441 | -61.8301 | 2025-06-27 05:10:00 | NOAA-20 | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a775628-c835-3eeb-866c-b10f0b38c549 | -9.82191 | -48.37952 | 2025-06-27 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b2f7db0-8ad2-3152-a455-ea3933da35a8 | -6.1799 | -48.08251 | 2025-06-27 05:10:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |


[Clique aqui para ver as próximas entradas](README26.md)
