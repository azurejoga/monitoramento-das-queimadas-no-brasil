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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e420cd1c-f026-3a65-bd70-6e622c991494 | -11.10745 | -49.61283 | 2024-10-02 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0abc1550-f63f-34bd-b7dc-367c2b8405c3 | -11.10688 | -49.61674 | 2024-10-02 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ae710f1f-7a52-3fef-a2be-e13da5e99bb1 | -11.10633 | -49.60983 | 2024-10-02 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a13434c9-7923-3f44-919b-14fcb130608d | -11.10574 | -49.61375 | 2024-10-02 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| aba13d13-8f27-3966-9b44-537e2b26c0e8 | -11.10343 | -49.60538 | 2024-10-02 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4b34d67e-e37c-3f4a-810b-a00711c53fe8 | -11.10284 | -49.6093 | 2024-10-02 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4f2bc366-6e99-35e8-9837-470d6519932b | -11.10225 | -49.61322 | 2024-10-02 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9df3cf82-9bf4-3cd3-8d67-aa778daaa51c | -11.10054 | -49.60092 | 2024-10-02 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9bafd3ac-631c-3b28-815c-b8278a3b4287 | -11.09995 | -49.60485 | 2024-10-02 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ace3864f-1501-381f-9846-dadce2d72942 | -11.09764 | -49.59646 | 2024-10-02 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9befc25e-98e6-30a8-962e-7dc8f2058cc7 | -11.09705 | -49.60038 | 2024-10-02 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9f67c060-8726-352e-ad0c-625bf9dae727 | -11.09533 | -49.58807 | 2024-10-02 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7e12c895-bf88-3d64-b55e-dc7f667cb300 | -11.09474 | -49.592 | 2024-10-02 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 85b9deab-fd14-38ce-87cd-ee00654625e7 | -11.09415 | -49.59592 | 2024-10-02 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fd44e382-c4fe-387c-91f3-b0be477f5dfb | -11.09356 | -49.59984 | 2024-10-02 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e7fb76fe-fabb-30f5-b804-0bc844a24b74 | -11.09184 | -49.58753 | 2024-10-02 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9dd39bef-5033-3573-980a-7fd161736aa0 | -11.09125 | -49.59146 | 2024-10-02 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c6902165-a6f0-3c7e-9c74-84bc984c7f30 | -11.09067 | -49.59538 | 2024-10-02 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8b986733-04b5-3133-ad1a-4433e49b21ef | -10.9848 | -50.15883 | 2024-10-02 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3dcc7172-db6a-31d5-893d-49165bc6ffb2 | -10.98083 | -50.16204 | 2024-10-02 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 26280d00-ebeb-315d-b70e-23aa4dc10ee1 | -10.97176 | -50.17595 | 2024-10-02 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ffb9fd75-165a-36d4-bc63-6ffae3e180ab | -10.91536 | -50.12962 | 2024-10-02 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44e2bdee-767a-389d-8b43-acc0853077f5 | -10.91194 | -50.1291 | 2024-10-02 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d51ad84-ff47-35c9-a86b-609aa254b126 | -10.91138 | -50.13284 | 2024-10-02 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c190b296-e5f1-3e03-b5ad-d503e9edae7d | -10.90284 | -50.097 | 2024-10-02 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ead7507a-6f04-38ac-a24e-9b4c81ea2a75 | -10.90056 | -50.08895 | 2024-10-02 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9dfc8f8d-1530-3c21-8ebe-5a52d139390b | -10.89999 | -50.09271 | 2024-10-02 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2e1738a-754a-3dd5-b63d-db9d3cf48510 | -10.89942 | -50.09647 | 2024-10-02 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad63b95e-d66a-3222-942d-7c7a92a62258 | -10.89773 | -50.13072 | 2024-10-02 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3d5fb69c-3393-3120-bf8c-d3c556537ba3 | -10.89716 | -50.13446 | 2024-10-02 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bc83a660-355f-312a-a6ac-e56db81c6962 | -10.89714 | -50.08843 | 2024-10-02 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05cb2d64-c46d-3fec-8aa9-0fbf58362346 | -10.8966 | -50.13821 | 2024-10-02 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 51123883-3dc2-3955-aea0-ea7269a48742 | -10.89657 | -50.09219 | 2024-10-02 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90dfa985-c71b-3e3a-bcc5-1e1b06331f6d | -10.89603 | -50.14195 | 2024-10-02 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e5e76572-ac61-397f-8f89-e10df7a25135 | -10.89601 | -50.09594 | 2024-10-02 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e9d8fa45-b888-36e4-a266-1b216f05d8db | -10.89544 | -50.09969 | 2024-10-02 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94f2bb81-5404-322c-9a6a-8547d2addc45 | -10.89487 | -50.10344 | 2024-10-02 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9cb0761-e20e-3e5f-b060-268f3f3a0792 | -10.89259 | -50.09541 | 2024-10-02 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55e0d2d0-07ea-351a-8478-36fef2c2d3c2 | -10.89203 | -50.09916 | 2024-10-02 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e08fe4f6-242e-39ee-bddc-dca643f989a3 | -10.85032 | -50.32876 | 2024-10-02 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69239fa8-c3d4-31f1-a305-1759523e49dd | -10.84976 | -50.33245 | 2024-10-02 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d472708f-34c0-3d0a-9738-b8d99e85e87b | -11.69297 | -49.90203 | 2024-10-02 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38e43a31-2d4f-3c1f-a9ff-4d59ea7e5298 | -11.68951 | -49.9015 | 2024-10-02 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f19d66bf-944a-3197-846c-d7e90dd90ad1 | -4.04057 | -50.38286 | 2024-10-02 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2306b413-ef49-366a-a527-1e904fd6d764 | -4.04003 | -50.38629 | 2024-10-02 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7d9cac1-d9c8-311c-ba2b-db859127f447 | -6.4252 | -50.14501 | 2024-10-02 04:46:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3c1b5fe-0049-300a-bb02-b5312c33f788 | -5.51869 | -50.04656 | 2024-10-02 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83c61aec-2812-3cb7-ac7c-d7969bbbb60a | -7.80564 | -50.2343 | 2024-10-02 04:46:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98b8e0a1-d557-3400-9c89-1b45c429dad0 | -7.80509 | -50.23785 | 2024-10-02 04:46:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 51d629a7-632a-3227-9597-0a48b75fea6d | -7.35909 | -50.81254 | 2024-10-02 04:46:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d792391c-ba76-315b-9d80-641b1375df2f | -8.07744 | -51.13582 | 2024-10-02 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 390edf7f-2376-3bd0-a94a-457abff17302 | -8.0769 | -51.13928 | 2024-10-02 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b1c5d9c9-b7e7-3c59-b99e-2a412cf25192 | -8.07636 | -51.14274 | 2024-10-02 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1d65f48f-9b14-37ed-af38-1458e2019ee0 | -8.06813 | -51.15209 | 2024-10-02 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16bff6fd-cd1c-3e46-9c7d-04f0b92ad781 | -8.06537 | -51.14811 | 2024-10-02 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41dfdbbe-4556-3b7b-8e20-f411b25a585d | -8.06483 | -51.15158 | 2024-10-02 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4053a2c9-fb89-358c-926e-21472f0f6702 | -8.06429 | -51.15504 | 2024-10-02 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc6d50d2-0d04-37cf-8f13-bd3daf306dde | -8.06207 | -51.14759 | 2024-10-02 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ff414189-b4f0-3b5a-9ada-13998ed72898 | -8.061 | -51.15453 | 2024-10-02 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc4c36c1-a4e3-3a9b-9fbb-840d6219d605 | -8.81021 | -50.66559 | 2024-10-02 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7cc63e4e-c697-3fc1-81fa-111e1bf21bbb | -8.3346 | -50.64106 | 2024-10-02 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ba6f61b4-e0c2-323b-adf3-dca6711776b8 | -9.60466 | -50.87289 | 2024-10-02 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df8f7505-6c45-3649-910d-c74ae6c252aa | -10.68786 | -51.07968 | 2024-10-02 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6abc1c4c-3083-3de1-ae96-03928cb520d7 | -10.62898 | -51.10988 | 2024-10-02 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c71f0e0c-11c7-3eee-a030-fb0729565ed2 | -10.54756 | -51.08644 | 2024-10-02 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eebc398b-cfc6-3f76-8ce2-7648c674e560 | -10.54701 | -51.08998 | 2024-10-02 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2974863a-08c6-3694-8842-b7a6f42ba178 | -10.54091 | -51.0854 | 2024-10-02 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 401e375d-2930-3940-b68e-da43dd3b1b0c | -10.53759 | -51.08489 | 2024-10-02 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b29cabd3-756c-3af7-ac2b-53d1a7484800 | -10.53426 | -51.08437 | 2024-10-02 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 478ea5fd-2c63-3a93-9498-a4eead1efd8e | -10.53094 | -51.08386 | 2024-10-02 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9955b7c0-e09a-3470-949e-89ec2a36590a | -10.52761 | -51.08336 | 2024-10-02 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 58ca2fec-7fae-3316-99c2-9a1c1c1790bc | -10.52429 | -51.08286 | 2024-10-02 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 65df0cd0-17d1-3439-8931-e3c59005a728 | -10.52096 | -51.08236 | 2024-10-02 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7c5219cf-f353-3347-958c-790afc4f9e36 | -10.52041 | -51.08593 | 2024-10-02 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f75a8871-213d-3b3c-b4a8-8f6fd31858d0 | -10.51764 | -51.08182 | 2024-10-02 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0725ba93-984e-38e7-8bdc-46877ca8dcd3 | -10.51709 | -51.08538 | 2024-10-02 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4f57cd55-ffda-3555-89d3-7229f1d30a85 | -10.51654 | -51.08894 | 2024-10-02 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f659b52e-ed6a-3577-8a2c-1f7fa404a4fc | -10.51322 | -51.08838 | 2024-10-02 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 17e9da0e-a864-3bab-8dd0-64d54fbac453 | -10.51268 | -51.0919 | 2024-10-02 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1f944e19-da3d-3e99-9845-8d9e4fb83fb7 | -10.51213 | -51.09542 | 2024-10-02 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a4b0c1d-4bb0-3e65-be7a-794b88909c5c | -10.51159 | -51.09897 | 2024-10-02 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3bac91d2-1ae8-38d4-97fc-51d25d8de703 | -10.51104 | -51.10251 | 2024-10-02 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 772fd94c-d6cd-355b-9ac3-bdd69cf1b406 | -10.5105 | -51.10605 | 2024-10-02 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 220b519f-0d1c-38c9-a409-28babe0c7c63 | -10.50995 | -51.10959 | 2024-10-02 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4c3ed3a-4606-3d3d-bba5-1b2ce9a21fd9 | -10.5094 | -51.11314 | 2024-10-02 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dbc67470-c263-3881-96e5-7984c81c8a0c | -10.50663 | -51.10904 | 2024-10-02 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f279c21b-bcea-37fa-8c7e-28dc5098fe92 | -10.50553 | -51.11616 | 2024-10-02 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 190aa670-e9b3-3798-a143-6ee10ea21972 | -10.50167 | -51.11918 | 2024-10-02 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b6fe866-f476-3dbf-958e-356c2f077c17 | -10.50112 | -51.12271 | 2024-10-02 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 480811c1-279a-359d-bf2c-ffb2bcbb6dd9 | -10.48427 | -50.83652 | 2024-10-02 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ea5aec6-92fb-39bc-aa76-417170bab928 | -10.4513 | -50.76185 | 2024-10-02 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f70962c8-4ffc-3ff7-a89c-48f974183b07 | -10.45075 | -50.76541 | 2024-10-02 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c67a0828-1e8d-3e92-8866-1594125bea64 | -10.44363 | -50.81184 | 2024-10-02 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eaedf802-401f-358a-a7c2-a87eda073302 | -10.44029 | -50.81133 | 2024-10-02 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca3c5b28-5da1-3ce9-8db1-f9c8c1807b05 | -10.43915 | -50.79648 | 2024-10-02 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 56776cc1-ed89-31eb-aae1-4289edd36a6c | -10.4386 | -50.80006 | 2024-10-02 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5ea67b60-9c27-33ac-8eff-8b1e0bb584f1 | -10.43805 | -50.80365 | 2024-10-02 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 51c22622-4e3d-30b9-8a8d-645be110c02a | -10.4375 | -50.80723 | 2024-10-02 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 892be8b5-1313-3ca1-83ee-e4a29b94d1c7 | -10.43581 | -50.79596 | 2024-10-02 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9648289f-9783-3bbb-88cc-02ed61fa7e0d | -10.43526 | -50.79955 | 2024-10-02 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README91.md)
