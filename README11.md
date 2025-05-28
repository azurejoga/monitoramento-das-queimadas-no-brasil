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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80bc82ad-a843-366a-be70-7435d9c82505 | -12.46115 | -44.28663 | 2025-05-28 04:32:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f7243b2-d439-32f3-b50e-91cc57d1cbe5 | -11.39285 | -44.82795 | 2025-05-28 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| cddf0d20-b922-3e1d-a742-780da2253da9 | -8.38844 | -49.86179 | 2025-05-28 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7af699e-af3b-3962-bbd7-740c3a300cf9 | -10.24318 | -52.23297 | 2025-05-28 04:32:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c94591ff-fe24-3b21-a9bc-6072094e9311 | -10.66511 | -44.40763 | 2025-05-28 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3165a70d-8022-3427-8834-c448d9a0404e | -11.2882 | -54.01439 | 2025-05-28 04:32:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c64cb115-467a-30d3-abdc-9dd1a9e36017 | -6.61551 | -48.02193 | 2025-05-28 04:32:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a62fd67-3544-3981-ad56-96bbf5a09c11 | -10.53015 | -47.58322 | 2025-05-28 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7879708-fd67-3b08-8f8c-a5c52da72679 | -7.62723 | -45.75932 | 2025-05-28 04:32:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 22d68b3a-4c04-301a-a39b-d93bbf924167 | -10.23657 | -52.22735 | 2025-05-28 04:32:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e016f15b-0957-364d-b5fa-30783917c70c | -7.20346 | -43.53927 | 2025-05-28 04:32:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1adbd429-31dc-31c6-aca4-68b72ff1a0ef | -11.81514 | -46.14241 | 2025-05-28 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e6c73b4-b13c-31b0-b60c-c068bb8fd082 | -7.68022 | -46.09701 | 2025-05-28 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 46ed0728-3eb7-3715-9398-2a3569d71873 | -9.03754 | -48.94357 | 2025-05-28 04:32:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a29406d2-6df5-3465-a36f-9f7ec49d6d2a | -9.03422 | -48.94304 | 2025-05-28 04:32:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d92690c8-4d10-3a52-b66a-b35c1effbb9c | -7.20113 | -43.12034 | 2025-05-28 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c732ca96-b061-3fb4-8047-6758c276ec04 | -10.58053 | -49.02405 | 2025-05-28 04:32:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 594c43cf-c95f-3ac2-9fcc-99fda150cbda | -11.57002 | -47.62203 | 2025-05-28 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f7dcbcb1-2d52-3608-b8ee-47abf616f8e6 | -13.09894 | -52.28696 | 2025-05-28 04:32:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3a9bb61f-7d74-3c53-91f2-229f0af28346 | -7.19015 | -43.11162 | 2025-05-28 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 11e81e75-523e-3588-9974-53190acafadf | -10.23878 | -52.23668 | 2025-05-28 04:32:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 63490d75-a653-344a-8bab-d151597393f1 | -11.29396 | -54.01209 | 2025-05-28 04:32:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40edc1d4-13f8-3799-9ef8-0e0da476157a | -11.57058 | -47.61839 | 2025-05-28 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c272ab02-4e6f-379c-9ce3-2c454353b8e8 | -7.95226 | -49.76195 | 2025-05-28 04:32:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 07da15a1-a965-3105-9242-5423d1b96488 | -7.21813 | -43.11578 | 2025-05-28 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7b78115a-fc72-3c53-9405-b643650de143 | -7.19415 | -43.11217 | 2025-05-28 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c24ae94d-bf79-33b5-a9d7-57c0bbf15509 | -11.91518 | -54.42304 | 2025-05-28 04:32:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ebdfaa19-3cda-3560-8386-8d23cc15ae19 | -13.07636 | -45.28212 | 2025-05-28 04:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 60ef6371-e6f8-3fa6-aa35-d94997caacaa | -10.2351 | -52.23606 | 2025-05-28 04:32:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 244d3f5f-fca0-3b79-a3d9-c901067c7a74 | -8.14646 | -47.15882 | 2025-05-28 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cd84e5b1-29a3-3bfb-91c4-2c857a8fff8a | -7.18164 | -43.11396 | 2025-05-28 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 70815ae2-c3b1-399a-bd1b-f2f15f4d4a54 | -11.68662 | -47.4333 | 2025-05-28 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c5ef58d9-c26d-3825-a839-a41ed8a95698 | -8.72602 | -47.99075 | 2025-05-28 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be122738-522d-32e0-840f-b8295942ffaf | -11.04212 | -55.07639 | 2025-05-28 04:32:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c690061b-e723-38a1-9365-6ef9881bae25 | -11.40045 | -44.82911 | 2025-05-28 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 55e8871e-799d-39b8-a112-1dcc13cb1c8b | -8.01759 | -49.68642 | 2025-05-28 04:32:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c64e8553-6e8d-35b6-a2bd-46d0c72b8571 | -11.29332 | -54.01565 | 2025-05-28 04:32:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01bcc99e-dba4-3f96-ace3-0c46d552a0a4 | -9.84579 | -48.14693 | 2025-05-28 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8cc850fb-ef18-33b4-8fbd-9ceb0c4c2cc9 | -10.47082 | -47.94653 | 2025-05-28 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| bd2ec014-8e10-374d-8d59-0378ea052756 | -11.29733 | -54.01638 | 2025-05-28 04:32:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 931f14b5-0fce-3971-9177-d9acb3d0be9b | -8.74263 | -49.75076 | 2025-05-28 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b3e1679-86c0-3dd5-bceb-71f8d5b18480 | -7.19116 | -43.10461 | 2025-05-28 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| ff826e0a-e6a5-3d73-9944-a84de898a508 | -9.35327 | -50.23172 | 2025-05-28 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f22cd340-49e5-35e0-b754-ad1ec74e74fa | -7.18241 | -45.10194 | 2025-05-28 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51a877c2-ce23-3bcb-a504-a731b3a0a5ba | -7.96297 | -45.93724 | 2025-05-28 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa340ab4-6c39-320a-9331-2d84814b1c51 | -12.37419 | -49.98347 | 2025-05-28 04:32:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 47df1782-8536-3b0b-b1fa-fed4d4e44e2d | -8.72988 | -47.98779 | 2025-05-28 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6865183-fc3c-36e2-a02f-c8bdce8e7367 | -7.20963 | -43.11805 | 2025-05-28 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f12dbe60-434a-32c6-b2a7-478ac576b5a8 | -10.54076 | -47.9794 | 2025-05-28 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 578bc5be-3ef2-380d-acdb-3f6414dfa92f | -13.08906 | -45.27438 | 2025-05-28 04:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 51d3c0fa-fccc-3110-94de-65b581865724 | -7.61133 | -43.40977 | 2025-05-28 04:32:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d767a01-f515-3600-9930-6e59778fd072 | -8.72933 | -47.99127 | 2025-05-28 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17fa04d3-c53e-3fb3-987d-624fbd1c8dbd | -9.20133 | -49.47252 | 2025-05-28 04:32:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3698a35b-d396-3f46-9483-e24bab95a843 | -6.63389 | -47.34356 | 2025-05-28 04:32:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c31c9fdb-04fa-3486-89ad-7b9fb2403476 | -10.58537 | -48.51923 | 2025-05-28 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 469c27ca-2a8c-39c6-8e54-8c4b5aa5be29 | -11.39665 | -44.82854 | 2025-05-28 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 74feea5e-858e-3a31-9642-26399a12bbd3 | -10.23584 | -52.2317 | 2025-05-28 04:32:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| be222834-3c55-3546-96bc-6f2c6f375e10 | -7.18215 | -43.11048 | 2025-05-28 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c8e5caf7-5f0a-37e2-a69f-560623036b41 | -7.67621 | -46.10023 | 2025-05-28 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 98f55816-094f-36c8-93c1-47680f97e582 | -11.14511 | -53.9274 | 2025-05-28 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27d66433-b834-3283-ae61-acf5c0f4e00a | -11.13833 | -53.91897 | 2025-05-28 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31e118bd-6bce-36ff-861f-ace2b2f09920 | -12.40862 | -49.99973 | 2025-05-28 04:32:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e30f7b97-3e94-3d7b-aead-66e2588a921a | -11.91648 | -54.41573 | 2025-05-28 04:32:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9923c3a7-a551-352f-bae4-6a57f40b8330 | -7.68366 | -46.09754 | 2025-05-28 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 02cf76c5-2e53-35d8-991c-7c844ba62814 | -11.1371 | -53.92601 | 2025-05-28 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16c10c80-9ea2-3355-b99a-762c9a85aabf | -10.47137 | -47.94299 | 2025-05-28 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bba33db4-31ba-36cd-a756-a06f795922ab | -7.21014 | -43.11457 | 2025-05-28 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c7c9d140-cdf7-339f-b611-1407d7ee0364 | -11.57339 | -47.62255 | 2025-05-28 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 56b16e56-126f-32b9-a867-32e6b8d61779 | -8.87945 | -49.04033 | 2025-05-28 04:32:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0958f6ed-70d6-3051-aa1a-832689195327 | -11.39217 | -44.83269 | 2025-05-28 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| da127c01-0197-3a96-a07f-e2f729232e35 | -11.81601 | -55.07628 | 2025-05-28 04:32:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cdae4a08-ccbf-31ab-aeea-5068c4ef9759 | -11.91305 | -54.41133 | 2025-05-28 04:32:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e023cd2c-ee3e-3d1a-a4ab-8acb090f17ae | -9.676 | -49.71054 | 2025-05-28 04:32:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bcdea263-2c0b-339b-a4e0-24f44dd3a5aa | -8.72657 | -47.98727 | 2025-05-28 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ba12125-5e98-3e69-b271-1d8699917b7f | -7.38796 | -43.73637 | 2025-05-28 04:32:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d3c8621-defe-3c62-b3c7-0fddf3a0d1b0 | -11.56599 | -47.44514 | 2025-05-28 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7dfc62c5-c4ad-39da-b2bc-2802b710eac2 | -8.01901 | -43.18371 | 2025-05-28 04:32:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b3ad64fe-96dc-38d0-8da5-868b1ff619ff | -7.61058 | -43.41489 | 2025-05-28 04:32:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 67388001-ccf3-32e8-9017-4d1d322d2764 | -11.89082 | -47.44888 | 2025-05-28 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97d6244d-b3dc-367b-9166-9c36270f168d | -7.33894 | -43.68332 | 2025-05-28 04:32:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d6a6c70e-0cb8-3563-9148-1b7724dd02a0 | -9.042 | -47.03 | 2025-05-28 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8e14443-6cbd-3b96-aab0-2525c7e3188c | -10.66056 | -44.41191 | 2025-05-28 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e1754ec-8cd1-3b4b-9a21-5f2f93df9294 | -7.08497 | -46.05049 | 2025-05-28 04:32:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 15877b10-c9a3-3bf8-94fe-8c010ebbbc85 | -9.03931 | -47.74604 | 2025-05-28 04:32:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 07b80346-4df2-3886-9fb7-43f77eab392c | -11.30408 | -54.02502 | 2025-05-28 04:32:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8aee71f3-b279-3144-a76f-3f8a780299d5 | -11.75244 | -54.23164 | 2025-05-28 04:32:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ade53e1f-14bd-3845-9983-0a2fe1e2e33e | -9.18255 | -40.31273 | 2025-05-28 04:32:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 8314ded3-5f15-3ba7-88bf-27f3d57ce024 | -7.7969 | -46.22522 | 2025-05-28 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5407c9b6-a217-37d9-9699-14fe927c0e9c | -11.56609 | -47.62513 | 2025-05-28 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d401b3b-ed0c-367a-b22f-901a7e9d703c | -7.62376 | -45.75876 | 2025-05-28 04:32:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1e10b05f-9a9f-3a1c-bba7-e59ef79c21c2 | -11.29427 | -53.97904 | 2025-05-28 04:32:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b73f1e39-e65b-3659-a40b-d2191ca238f6 | -10.53411 | -59.22702 | 2025-05-28 04:32:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8556e86a-6950-3dba-bffe-e97d48f22585 | -7.56073 | -43.34794 | 2025-05-28 04:32:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5da88fb-b3d3-3990-9363-da58100173d2 | -7.99662 | -46.15617 | 2025-05-28 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 577cc40c-677a-34e1-ac32-b45ca413a042 | -9.85178 | -48.0652 | 2025-05-28 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7ca37523-6050-30a8-a006-e1b9bc34ed39 | -10.53983 | -59.22816 | 2025-05-28 04:32:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac0185b9-f383-3cef-809f-8d789adb5e52 | -10.5296 | -47.5868 | 2025-05-28 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 54e814cc-8e4b-3265-9b1d-9a81a7f94ea5 | -11.8159 | -44.27098 | 2025-05-28 04:32:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 560d37df-f1d9-3ffd-9a3a-928128ebfb4a | -13.08527 | -45.27383 | 2025-05-28 04:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d521c577-d9a2-39a3-bf64-e2bd573f3842 | -6.61882 | -48.02245 | 2025-05-28 04:32:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README12.md)
