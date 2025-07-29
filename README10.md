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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02cf5fc8-b7aa-3b1a-8c5e-658a1dfdc86d | -7.79159 | -44.95404 | 2025-07-29 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d06a03e7-5171-38f2-96ea-229560296c78 | -6.38488 | -53.35213 | 2025-07-29 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a2c919cf-14e5-32fc-af7d-f90d37339651 | -7.24082 | -43.05987 | 2025-07-29 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 5489cb00-e560-3fbc-8049-3977ecd7366d | -3.94676 | -41.48218 | 2025-07-29 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2af8c489-4022-382f-9a2c-328c0fe41dc4 | -7.86653 | -47.87486 | 2025-07-29 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 819c57eb-1ee4-389e-acbc-14aa21f9c02a | -6.90338 | -52.86556 | 2025-07-29 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 25f46ebf-1f5a-34f0-a8a9-a7ac40101c0d | -6.3819 | -53.33933 | 2025-07-29 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b1ce3cf-1f10-3adb-9826-904483059d91 | -8.29109 | -45.00147 | 2025-07-29 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49aec2d2-4376-35d4-8346-e60c4d33e1dd | -7.61627 | -44.81297 | 2025-07-29 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9234799b-f07f-3595-813e-ddec4878d7bd | -6.39048 | -53.35003 | 2025-07-29 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0772b8e1-32b2-3c2f-a619-fee403b63465 | -6.17075 | -44.42168 | 2025-07-29 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97ca0c4f-3fa1-3d21-abf4-cea7c10ea72a | -5.40544 | -45.29184 | 2025-07-29 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a245e9a-a6a2-3ec3-a5a1-a2f3ee4d33f2 | -4.12367 | -49.27291 | 2025-07-29 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1e90fe35-7e9b-3168-80cf-d83a5277e583 | -6.38084 | -53.34539 | 2025-07-29 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4fd6a4e-07d9-3198-a540-aa230f1878a5 | -7.93863 | -44.09193 | 2025-07-29 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7df0e858-030c-372e-b964-1cec77faca53 | -2.88719 | -48.29248 | 2025-07-29 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c973ec47-4bcc-3f4f-b60f-a9d395b511eb | -7.80223 | -46.57156 | 2025-07-29 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 61d5e7ba-3fb4-3681-9163-6c850533691b | -6.49627 | -56.19798 | 2025-07-29 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63ba1b15-7e39-3880-bae1-0df201dc2bb9 | -6.38995 | -53.35305 | 2025-07-29 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13b25c6e-50d8-3e7b-a2c2-512d26caf7ee | -7.93584 | -44.08784 | 2025-07-29 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 7e6ed792-9bae-3060-be80-9d9c24292db6 | -5.89097 | -50.57761 | 2025-07-29 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0282175e-816d-3d52-8357-2da2672f687f | -6.39554 | -53.35101 | 2025-07-29 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4d9889e-7c7d-369a-9fa5-5a9075eb9862 | -6.09186 | -42.93745 | 2025-07-29 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8f61ecb1-46ed-30f0-b7b8-f98765ffd86a | -5.48162 | -42.15456 | 2025-07-29 04:19:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5b50fa45-48b7-350d-b2e1-7a509d6d1358 | -8.37037 | -46.65131 | 2025-07-29 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ecdadc87-9dec-3f50-9808-5a801f34ed5d | -8.20282 | -47.66218 | 2025-07-29 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08f6c524-95c8-37f7-bf10-34b570bccc82 | -7.24482 | -43.05665 | 2025-07-29 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 569de2b2-1d33-3480-88e6-ce4d19c51e93 | -7.91967 | -44.0817 | 2025-07-29 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2409c727-9e62-3037-b92d-22f746db14bf | -7.9325 | -44.08731 | 2025-07-29 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 11614467-3fb8-318c-b270-aa61acd67c52 | -4.85507 | -42.99676 | 2025-07-29 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 817a1630-ee5a-3589-8b07-577c708533bf | -7.15242 | -47.42538 | 2025-07-29 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d51e79ba-4938-3e75-a469-973a018e0dc2 | -7.25053 | -43.06519 | 2025-07-29 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 99a741f8-8a10-3900-b3c3-ed12ce01d833 | -6.40131 | -53.31801 | 2025-07-29 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 179a10fc-7528-3599-a1f7-ea6f18150c87 | -6.45554 | -53.35788 | 2025-07-29 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68ac1935-3864-3344-b7b6-1c6a7e4b2b3e | -6.50081 | -56.20599 | 2025-07-29 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8c20c47-07bf-3498-952c-e42e8605e962 | -3.82722 | -41.555 | 2025-07-29 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 98c4cb47-8f76-3d09-aefa-216d8245891d | -6.39101 | -53.34702 | 2025-07-29 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53b54ca3-3507-3f56-b211-53bb9b15ffaa | -7.2431 | -43.06789 | 2025-07-29 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 5b68ff9e-5425-315a-bd63-37e7d8ad1a2a | -7.863 | -47.87429 | 2025-07-29 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4bbdc11e-3963-3e2b-90c6-aa6acc0d3937 | -6.50588 | -56.21415 | 2025-07-29 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e8a0de40-03b1-3522-b47d-958e03fb384c | -6.39258 | -53.33803 | 2025-07-29 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8579fa6e-1003-3357-9a3c-335804ed8bc9 | -7.72963 | -51.10889 | 2025-07-29 04:19:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2baa01b1-d34b-3ada-992d-65037d0e88cc | -7.7246 | -51.11259 | 2025-07-29 04:19:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 714bc392-e1d5-3c26-bbe5-c30fbd766b45 | -7.23682 | -43.06309 | 2025-07-29 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 6f545bd1-1496-32f5-a68e-3987d630475e | -6.77513 | -50.48791 | 2025-07-29 04:19:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02be1c51-ee18-3cbd-a6b0-cf987227e006 | -7.23739 | -43.05934 | 2025-07-29 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6a0eae3b-2102-3067-aaf7-59519024bc37 | -6.45192 | -53.35756 | 2025-07-29 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b2996208-55e0-3f2e-b2e6-72e96b57d7b3 | -5.35383 | -45.27309 | 2025-07-29 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2d98d386-979c-3b18-bc0f-042e7152d5cb | -6.49367 | -56.212 | 2025-07-29 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ba462150-f1e0-349c-b904-5a83e4ad7607 | -6.49917 | -56.21525 | 2025-07-29 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c9136501-ef05-316a-8524-3dbd02e3d0ae | -3.29977 | -48.92276 | 2025-07-29 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e3b9df1-29b8-3e8a-8ef3-b688f6031f08 | -6.4509 | -53.36355 | 2025-07-29 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f61d878e-488a-3696-b810-3109b215347e | -5.35052 | -45.27258 | 2025-07-29 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a70674a9-6ce6-35b4-9735-f7cfa2b9123d | -7.25396 | -43.06572 | 2025-07-29 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| a5e1333d-8385-3ad1-97a1-5e86f3729cb1 | -2.89944 | -48.28959 | 2025-07-29 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4d2d1b64-6b59-33e8-982d-eadcb205d90b | -6.50673 | -56.20955 | 2025-07-29 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d0444b8e-b8e7-330d-94ba-008a974f9c58 | -7.9314 | -44.09444 | 2025-07-29 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2861a018-735d-3918-809c-c04465974f2b | -2.39584 | -47.624 | 2025-07-29 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6768662b-e4a3-3ea3-8a40-16aa4748d42b | -6.42044 | -53.35824 | 2025-07-29 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29471069-351e-3fc7-a115-776c47f49092 | -6.50502 | -56.21883 | 2025-07-29 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 187ea77e-3e0b-33b8-8bfd-41ac26c3433d | -6.49203 | -56.00975 | 2025-07-29 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab7aaf5e-faa6-3590-b3ce-20a36196066c | -6.1702 | -44.42515 | 2025-07-29 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8ccb42e6-7f82-3d56-aa75-f30aca7f3f69 | -3.99821 | -43.23743 | 2025-07-29 04:19:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e4ff8267-29f9-35e5-9bc7-5ed048172af6 | -3.08736 | -52.92678 | 2025-07-29 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b697bd7d-8daf-3fc0-8910-ff95101420a9 | -7.24653 | -43.06842 | 2025-07-29 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 5422ae38-f4f1-3067-b64d-b1915fb47602 | -6.50249 | -56.19655 | 2025-07-29 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9cb60d74-aeea-304b-a177-1dcc82717563 | -7.23974 | -45.39536 | 2025-07-29 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 45215a51-51c6-3f4a-acd1-c86e1dc6f7bf | -7.92246 | -44.08577 | 2025-07-29 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac073a68-7fa5-3cfd-9759-3d87bb773f6c | -8.51316 | -43.31405 | 2025-07-29 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3e5af24c-ea44-32f9-842c-c02083055b36 | -7.81414 | -50.22741 | 2025-07-29 04:19:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2dbf7d89-4ef3-3ea5-81b2-b281b33dfb8e | -7.92861 | -44.09035 | 2025-07-29 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51104be2-9fc6-35f9-9319-c85a9f597c9d | -6.422 | -53.3492 | 2025-07-29 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 01a9b3cc-3b9c-301c-abf3-1f16402c4d3d | -6.26905 | -44.5113 | 2025-07-29 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9ca9d3b-75e6-31be-89af-78ed12fe0521 | -7.38203 | -48.08467 | 2025-07-29 04:19:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a568776b-8a44-3ea1-adf3-075428028e91 | -7.93918 | -44.08837 | 2025-07-29 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e87e72b-398c-394e-9646-6fdab58b21fc | -3.78196 | -48.16233 | 2025-07-29 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d891a9ae-247e-30ad-8bb5-6b62fe24820a | -6.45447 | -53.36385 | 2025-07-29 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ae5e0ab-1959-341d-ab19-5de6d6ed88e9 | -6.39467 | -53.32613 | 2025-07-29 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b69acaff-9dc7-3cb7-a5c6-d21e574ff964 | -7.24425 | -43.06039 | 2025-07-29 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 733fcd14-375f-3a1c-aa41-ce6cbf7e1d9f | -7.33743 | -43.73605 | 2025-07-29 04:19:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c4e7a07d-9e94-303d-8710-d0e8982460bb | -2.66622 | -47.40608 | 2025-07-29 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ba614302-36e5-318c-b572-3597edc5a3f4 | -7.25111 | -43.06144 | 2025-07-29 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| b0e91595-d8db-39cc-b07d-1fbb26e78880 | -7.94252 | -44.08889 | 2025-07-29 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 706e1580-5fd1-3d2f-acfa-b9196edc25fd | -7.10064 | -44.36838 | 2025-07-29 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7201391b-2bda-3d2f-a8ec-89c46d108024 | -6.50527 | -56.21638 | 2025-07-29 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5403d688-703c-3f1e-a569-3841e797dff9 | -8.6355 | -45.51836 | 2025-07-29 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 83f2205e-8bb2-332b-90d3-262ec6c2661e | -3.82482 | -41.57085 | 2025-07-29 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 53a1c0c3-bb59-3cf0-b325-310d023f99c9 | -6.41537 | -53.35731 | 2025-07-29 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88cde088-3c13-3086-8e00-75ee0e3aec57 | -7.86187 | -46.72915 | 2025-07-29 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a8ee427a-1fed-351a-aaff-10d03930b98a | -8.63495 | -45.52184 | 2025-07-29 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4a6a6fd7-455b-3f6c-9a4f-cf97c692dcb9 | -6.49555 | -56.20016 | 2025-07-29 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d5801f58-6d59-305e-83be-c7c85984672a | -6.49639 | -56.19544 | 2025-07-29 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34efe30b-daa7-38aa-b4bd-41aa3d48d30b | -6.49471 | -56.2049 | 2025-07-29 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8420f7d7-560e-3231-938c-2c4c818fc60f | -4.10247 | -48.19799 | 2025-07-29 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4fe59fb-d007-31d9-936f-b18075294368 | -2.4556 | -48.15144 | 2025-07-29 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b80c37e3-806d-3930-9761-67c8f70dee26 | -3.27591 | -49.14208 | 2025-07-29 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ee508e0e-b2ec-33cd-8f50-25998c577e99 | -5.35438 | -45.26962 | 2025-07-29 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23aa58e3-cf48-334a-bab7-cbcf0a353a00 | -6.49306 | -56.21418 | 2025-07-29 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 901a5f6e-397b-37ba-a544-6ec0670d7d09 | -3.82602 | -41.56294 | 2025-07-29 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1ff5b8ab-c12e-3679-9c1e-62635c0b9d26 | -8.45066 | -46.89418 | 2025-07-29 04:19:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README11.md)
