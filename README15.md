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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1e3011e-e104-3cb4-9b81-e8b1a7efca7b | -2.83189 | -52.35991 | 2025-07-29 04:46:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8276758b-0537-3721-ba81-1bfcca351963 | -6.39203 | -53.3474 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03df4747-c15b-3862-8e7a-0a521b30d286 | -6.3834 | -53.35022 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d839644-212c-3a58-8644-0b62db04666a | -3.25676 | -43.27295 | 2025-07-29 04:46:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c553b2c6-6a16-3c8c-bdde-9f6e7f8a4837 | -7.93999 | -44.08617 | 2025-07-29 04:46:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ad2bcdf1-d4f9-3d6f-8e3a-9a54ca788131 | -6.38463 | -53.34247 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a67707e-5367-3603-abe0-12f5c4078fe2 | -2.27444 | -48.12412 | 2025-07-29 04:46:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b6e4e34e-0d06-33cf-bced-279b4b26e0d4 | -6.38918 | -53.34295 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 093a8f02-5cfc-3b6a-89c6-6dc96ff4199a | -6.38695 | -53.33467 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6214434c-6ad9-3eda-89ab-150c1c20f3d5 | -6.39457 | -53.33195 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2dfd7ca1-945f-3b68-8f5a-ddd185707e79 | -2.39193 | -47.62324 | 2025-07-29 04:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c047c690-8b02-3baa-bc3c-8bb0d1f98a1b | -6.39235 | -53.32366 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a21cce3-09ee-3ff8-b321-7ab1e7201afc | -6.12218 | -47.73195 | 2025-07-29 04:46:00 | NPP-375D | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5b9368cb-0a10-3bcc-be92-dcab8a834ebc | -6.4187 | -53.35968 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d8bee4a-7064-3fe2-8e50-8a9c8741a9a3 | -3.11306 | -46.80298 | 2025-07-29 04:46:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b783ce83-246f-3cc4-b1ed-ef94352d1ad2 | -3.08864 | -52.92726 | 2025-07-29 04:46:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 670fa8cc-a3fd-30b5-b3bd-071fef091797 | -6.40472 | -53.35743 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46c33a9b-ca05-37f0-ab1c-b9b924b9de9d | -6.38441 | -53.35012 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ce6a73b-3935-32b4-90e5-1bd8a5a5045f | -5.62146 | -45.10605 | 2025-07-29 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51ee385d-9b28-339c-af8c-48f008f9fc32 | -6.38568 | -53.34239 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56a93ab8-708b-392f-b620-f4b6b050b250 | -7.93531 | -44.08538 | 2025-07-29 04:46:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0381fdf7-55c4-3207-9365-29640471d327 | -6.39076 | -53.35515 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| affb328c-0b33-3df9-8158-05a38d8c0e61 | -4.22045 | -56.08395 | 2025-07-29 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4fe22b60-0b6a-3e13-8ccd-3a7391671b2d | -4.59831 | -43.30901 | 2025-07-29 04:46:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| dcdfcb66-09e1-37d2-a967-dcb5998cb68d | -2.79448 | -49.5975 | 2025-07-29 04:46:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 05696d12-3d76-3bfd-a10e-1ae893c967a5 | -6.39393 | -53.3358 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3bac025-05fc-3f34-8643-8505f6694007 | -6.72153 | -44.23824 | 2025-07-29 04:46:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c07bcf76-e2fe-3910-a3e0-7d4de11f2e11 | -7.92452 | -44.09415 | 2025-07-29 04:46:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e62009ed-b9e4-3b0e-99cb-3b8a6bdb329a | -6.39932 | -53.32479 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 625a2083-1ffb-365d-86f0-3b34019f36e8 | -5.64994 | -44.35675 | 2025-07-29 04:46:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f1c0de47-e761-33ef-bdb2-52292ce4624f | -7.7909 | -44.95481 | 2025-07-29 04:46:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 24b5f579-0506-332e-8e3a-98a33284292a | -6.40123 | -53.35687 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc2c89cc-4199-3b71-b335-155c23d20bff | -2.58679 | -51.92469 | 2025-07-29 04:46:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e758a63c-d81f-3fe2-ab18-6b04f35f24c2 | -7.24274 | -43.05679 | 2025-07-29 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 8b28d87e-45d1-3fdb-91a7-e917aac6530d | -6.38114 | -53.34192 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83bf30bc-7968-3f9c-89d2-fc0f6dc10df2 | -6.45361 | -53.3654 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b795f73b-de29-3402-b4f2-344569f621ba | -5.27454 | -44.47296 | 2025-07-29 04:46:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9067dd61-e1e8-39ab-bb66-43647f969dda | -6.40757 | -53.31819 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96006c99-3250-3aec-bbcb-64f618f044c4 | -6.39932 | -53.36849 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0140b991-375c-30fe-8ed7-dca89389065c | -6.39584 | -53.32422 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef5cb902-6233-32aa-9b55-813468ee54d1 | -6.39044 | -53.33524 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1319c15f-49e4-36d3-abac-c45e56730615 | -6.12154 | -47.73616 | 2025-07-29 04:46:00 | NPP-375D | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bdc3b3ed-2586-3244-98d1-f91932c4c3ab | -5.40907 | -45.29255 | 2025-07-29 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b83f28d-fde4-3084-a3f9-fa72639e099a | -6.38505 | -53.34626 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f9d08a3-b16d-3392-b9f1-e28d55e4fa5f | -6.38401 | -53.34635 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df1b0914-cd8b-38d4-803d-7a684da9f967 | -7.2511 | -43.06976 | 2025-07-29 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 133caf72-b352-3737-a2b8-7fcbb6721cc9 | -6.38649 | -53.33089 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 74190526-9b7b-312e-b922-7a972e73fe05 | -2.77652 | -49.19802 | 2025-07-29 04:46:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 265b718c-52b8-3899-ab66-071be0055a44 | -2.90138 | -48.29016 | 2025-07-29 04:46:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 976a826d-79a4-3c6b-901b-c7fda05d2ed7 | -3.04142 | -49.42553 | 2025-07-29 04:46:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| abe39cf5-5272-30c5-afc3-1aae5a5b4112 | -4.10152 | -48.20054 | 2025-07-29 04:46:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 35390067-8bb8-3d6b-b8a0-3108394565af | -3.22787 | -49.3433 | 2025-07-29 04:46:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6308f1a8-e61a-3100-815b-4bef1dfe9cc5 | -6.38854 | -53.34682 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9640360-3bf1-307f-9256-2ce454df4422 | -5.4049 | -45.29198 | 2025-07-29 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f1931a3-010c-330d-938c-8bd7f97d406b | -2.66681 | -47.40615 | 2025-07-29 04:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1de93358-251c-31dd-86be-ce911883b5de | -6.40282 | -53.36906 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3fabe868-983f-32d5-9dcb-397e8554568a | -7.92051 | -44.08852 | 2025-07-29 04:46:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ab34ac50-8347-35f9-885c-cb71a0d322dc | -4.0148 | -41.79092 | 2025-07-29 04:46:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0fab5ce0-617d-32b7-837b-d0f5ac2b990a | -2.88709 | -48.29175 | 2025-07-29 04:46:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c6b2a0d2-9c12-3067-9265-7ab7c1a33e63 | -2.89052 | -48.29228 | 2025-07-29 04:46:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 23697d39-8d0e-306c-b8e8-6fe2a38dc1b4 | -3.82435 | -41.56126 | 2025-07-29 04:46:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c3ed2a5f-4edd-35ce-91da-bd0209931838 | -6.38525 | -53.3386 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ecc7d1a-4916-37b0-8c59-df45fc018202 | -7.92921 | -44.0948 | 2025-07-29 04:46:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19af9915-96e9-389c-a13e-fc9cf39c348a | -6.83907 | -44.76274 | 2025-07-29 04:46:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4b11d923-b982-30e7-967a-f5ba8f954a53 | -2.89394 | -48.29281 | 2025-07-29 04:46:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a00f180b-0270-3e90-86b5-0efd32f9db38 | -2.90423 | -48.29439 | 2025-07-29 04:46:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 5ce10815-2e95-3781-becb-f50730f4e0dd | -6.45012 | -53.36483 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c1d1817-7770-3bd0-99c4-7ce6902333c1 | -6.38155 | -53.34572 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2814b115-44ae-3773-a650-e5049602b027 | -6.40345 | -53.36518 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e1876a1c-d54c-3a7c-b7f9-4072e22e6b74 | -3.08926 | -52.92329 | 2025-07-29 04:46:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61e45436-9b5e-3716-8b24-15949958ada9 | -2.48148 | -49.37069 | 2025-07-29 04:46:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30b69c1b-7d48-3256-ba41-ee72a23d75ed | -7.23775 | -43.05605 | 2025-07-29 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 66975503-ce7f-3743-af24-ca36bc9ee1c4 | -4.94148 | -47.4407 | 2025-07-29 04:46:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d965a724-ad9b-39fa-95e3-e28dd51fb57b | -7.9339 | -44.09553 | 2025-07-29 04:46:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 50aec2bb-7b5e-3219-a711-e6dd4b663a66 | -6.16754 | -44.42423 | 2025-07-29 04:46:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 26d9d13c-9238-3aad-a21b-1d79fa05acb9 | -2.89737 | -48.29334 | 2025-07-29 04:46:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a24f6801-3112-35e8-bcda-3c4b68ded1fe | -6.39806 | -53.3325 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 43d0353e-afb7-3384-85f4-9ac54b8c3186 | -6.12516 | -47.73669 | 2025-07-29 04:46:00 | NPP-375D | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 39abe357-45fc-317d-ac37-00c5573d0725 | -6.40345 | -53.32149 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad42bcf6-12e3-36d9-aab6-d63db7b2b0c9 | -6.83934 | -44.76364 | 2025-07-29 04:46:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7f6b2634-1a68-31e8-bc62-abc9a1db1081 | -3.82482 | -41.55804 | 2025-07-29 04:46:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bb9e16b5-c928-3f48-9993-4f655a17cb7a | -6.38219 | -53.34184 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41deadbc-390f-3a59-a85c-0baa3da379bb | -3.04196 | -49.42204 | 2025-07-29 04:46:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c442060-9ee7-3f14-a616-b78a1b79135d | -6.39171 | -53.32753 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b577df91-0c7a-35ba-8f92-bd9a64d25d9c | -6.3879 | -53.35069 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d29f91c-2580-35d1-9c7e-492d90e7ea88 | -6.39488 | -53.35186 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b6be96b1-32dd-3971-bc2f-1f4b57926ba6 | -7.25192 | -43.06391 | 2025-07-29 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 4d8ef937-a579-33c3-9c82-ee15ebf0ae96 | -6.41996 | -53.35193 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a53c536-17c5-343e-b35e-2737697f9d4b | -6.38283 | -53.33796 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ec49962-9db2-3f56-8f2f-3dc1a4e22c61 | -6.38981 | -53.33909 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6cdaa03c-aab6-31d2-88db-6555eb8b7cba | -6.38587 | -53.33474 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e44dce8-e247-3f9f-b093-cd051b71e7a5 | -6.39424 | -53.35574 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ca42c2bc-f55d-3254-bff1-5db08fbb633f | -4.94574 | -47.43705 | 2025-07-29 04:46:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3867862-2268-3b40-9db8-4486ed96b28a | -6.84289 | -44.76761 | 2025-07-29 04:46:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b4bf21a6-3252-3e01-8968-f00bfc136b31 | -6.38759 | -53.33084 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 156f6750-d4ca-397a-b1e2-07888814caa5 | -5.8145 | -50.18957 | 2025-07-29 04:46:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 633d0dfc-0ce9-3ae0-bbf4-f84c363ac64e | -6.42282 | -53.35639 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2539224-ea15-3c8b-9e52-e57c919d2917 | -7.92121 | -44.08347 | 2025-07-29 04:46:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 66f80f52-c57d-37e3-a49d-5f66b8232f30 | -3.08572 | -52.92272 | 2025-07-29 04:46:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9632d00c-6f44-35ad-9fd4-2e525da73f00 | -2.62514 | -47.97772 | 2025-07-29 04:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README16.md)
