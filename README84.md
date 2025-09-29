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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09717a5e-a0dc-3f62-bcd9-f0374e8423ef | -7.22608 | -44.76803 | 2025-09-29 12:17:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| ebe03fb6-4f09-3731-829b-8e0de09b1ac4 | -7.85687 | -46.75131 | 2025-09-29 12:17:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 905946dd-d393-3e37-8f61-4ca79d5baa9e | -6.30008 | -45.25446 | 2025-09-29 12:17:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 709c5cb1-5554-38a4-ac7e-5a3569773e47 | -4.11193 | -44.23559 | 2025-09-29 12:17:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| d13bc507-4b56-3b88-9b0a-c1bcbe50dd75 | -9.04244 | -46.71515 | 2025-09-29 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 0f96ab8d-a0f4-34af-88b9-582ac596fecb | -5.91476 | -43.91974 | 2025-09-29 12:17:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f4f9adc2-4826-3caa-b3c5-100e9fd34f59 | -8.91222 | -47.62447 | 2025-09-29 12:17:00 | TERRA_M-T | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 039cac2b-ca81-3ba2-9bf9-68425b56ac9c | -7.82125 | -46.99984 | 2025-09-29 12:17:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 145.4 |
| e2f0eae9-895e-387d-af97-7309d7a14ba6 | -8.15759 | -46.39132 | 2025-09-29 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 6df02911-6e8f-31d2-9383-d0226bf633fe | -9.24665 | -48.559 | 2025-09-29 12:17:00 | TERRA_M-T | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 44dd59a9-443b-3ca9-8bcd-b1edb3edae95 | -5.68134 | -45.06824 | 2025-09-29 12:17:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| dc7fa9b7-493b-340b-9eb8-57dce2f59279 | -6.90589 | -43.9979 | 2025-09-29 12:17:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 99a20d3d-24e5-3d0f-bd28-b7ab248f6170 | -6.1023 | -44.48935 | 2025-09-29 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c5af66f1-ff49-31b8-8101-d3410004dc02 | -8.25571 | -45.49303 | 2025-09-29 12:17:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 30.3 |
| b33f399a-2381-3741-a8ae-5653e47fadc8 | -2.72826 | -43.59455 | 2025-09-29 12:17:00 | TERRA_M-T | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 5930b306-b56b-32dc-8995-70de54343202 | -6.12976 | -44.43069 | 2025-09-29 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| ca14681a-b5eb-3d19-b97b-69804eb0e69d | -7.89488 | -44.59608 | 2025-09-29 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 85c00313-29e4-3346-91a6-1c524c912bd6 | -7.96834 | -47.32226 | 2025-09-29 12:17:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 757e7413-9e25-3edb-80d7-07a6dce3ec8e | -8.00783 | -47.04765 | 2025-09-29 12:17:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 3b1dace6-a3e3-34a3-955e-428417c42dc2 | -9.09864 | -45.86047 | 2025-09-29 12:17:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 98dc054b-c3ad-37e1-8dff-fcb8c0c075b7 | -9.07638 | -45.88644 | 2025-09-29 12:17:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 61346335-7d0c-33a2-b3ba-dc10f36c26d4 | -7.84943 | -46.22168 | 2025-09-29 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5ca8ed51-6c8b-360f-9f03-7bf03b776a41 | -5.79133 | -42.64588 | 2025-09-29 12:17:00 | TERRA_M-T | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 37.2 |
| bb1a70c6-e19c-3e41-a81e-93234ff80074 | -8.27008 | -45.52462 | 2025-09-29 12:17:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 9bb87178-fd4d-3ad8-b8f1-245fe6fc5bd9 | -8.1474 | -46.39909 | 2025-09-29 12:17:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 9643fbbd-f67e-34a7-9ae3-ed82ba5b9bb4 | -7.45863 | -43.9146 | 2025-09-29 12:17:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 749a95d9-3e53-38a3-ba26-83397325ec72 | -8.30437 | -45.48046 | 2025-09-29 12:17:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 210e3620-2bd2-3974-aa15-0edabbcbf35c | -7.00672 | -44.46363 | 2025-09-29 12:17:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| bb518756-9b91-3147-b21a-9e6b582857a0 | -6.77434 | -45.61526 | 2025-09-29 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 67043431-c7ff-3739-888c-51b43e0dda01 | -7.90723 | -49.19196 | 2025-09-29 12:17:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fd569d63-0831-34e8-a1ca-7612e74de734 | -7.8588 | -47.25511 | 2025-09-29 12:17:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| af4adf1c-6207-3830-9953-03d8c2aa61fb | -8.15631 | -46.40035 | 2025-09-29 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 3b1418ab-9f72-3986-bb22-410fb22bb4cb | -8.88569 | -47.62069 | 2025-09-29 12:17:00 | TERRA_M-T | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a93650a3-f0cb-35c4-8518-a3f6980aadaa | -6.15594 | -43.88148 | 2025-09-29 12:17:00 | TERRA_M-T | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d24a2dc3-5295-3a49-b0ae-b2313257b2ab | -7.28987 | -42.83374 | 2025-09-29 12:17:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 9573e7f6-1871-33a3-9d12-267c29300e5b | -9.3662 | -47.54816 | 2025-09-29 12:17:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 757f934f-1f5e-395f-9a10-b638f2275978 | -6.04054 | -36.53254 | 2025-09-29 12:17:00 | TERRA_M-T | BODÓ | RIO GRANDE DO NORTE | Brasil | 2401651 | 24 | 33 | nan | nan | nan | Caatinga | 131.6 |
| f8889e5b-cda6-3175-a8d8-b8bde72418df | -5.91164 | -45.85057 | 2025-09-29 12:17:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 6b54cc47-776f-3aa4-b457-cf633c5d14a8 | -5.90231 | -42.50286 | 2025-09-29 12:17:00 | TERRA_M-T | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 21.2 |
| c54bf0af-c1a4-35a1-935a-78b204a69849 | -9.37376 | -47.55832 | 2025-09-29 12:17:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 0b2a21c0-4714-3011-8f7a-c69f2f08b3b7 | -5.22438 | -44.63959 | 2025-09-29 12:17:00 | TERRA_M-T | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 205b6af8-bccb-3a68-b045-c9f28bf95a74 | -9.14872 | -47.7771 | 2025-09-29 12:17:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 245130c4-3654-3b63-941a-2019218ca7c4 | -5.03839 | -45.11901 | 2025-09-29 12:17:00 | TERRA_M-T | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 35bec077-a1ac-3e79-bb41-2b2660783025 | -7.9709 | -47.30454 | 2025-09-29 12:17:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| be47bf01-bd4b-3186-bcc9-d73c25d0fbee | -8.27653 | -45.54553 | 2025-09-29 12:17:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 46ea9f3a-043d-379a-9c83-94a263ca9da0 | -5.69137 | -42.62598 | 2025-09-29 12:17:00 | TERRA_M-T | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 59becafc-7538-3d92-b7fe-e2e60a3c2754 | -8.71383 | -47.98166 | 2025-09-29 12:17:00 | TERRA_M-T | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| cdf6ba69-8b22-3a6a-a9a9-aa31c774f57e | -7.4442 | -46.99409 | 2025-09-29 12:17:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| f41dd28b-9b90-343c-a0b7-08203503b34d | -4.35249 | -43.83155 | 2025-09-29 12:17:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 30026f63-0f50-3b9f-bab0-45a75492f278 | -6.75779 | -44.75566 | 2025-09-29 12:17:00 | TERRA_M-T | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d51624b2-4620-35d8-87ed-33e63ce5140b | -7.22464 | -44.77824 | 2025-09-29 12:17:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |
| eb7c8e1c-2008-3cfa-a794-14e00cc76939 | -7.99899 | -47.04641 | 2025-09-29 12:17:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 2227d5e8-5347-3daf-ae6b-d367651ee854 | -4.3621 | -43.83289 | 2025-09-29 12:17:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 5de985b5-7c2b-3fb3-a70d-54a463c8d149 | -7.38483 | -47.03085 | 2025-09-29 12:17:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 24f31a8c-94e0-3cbd-91e0-2878f0c7ea9c | -8.52064 | -47.84371 | 2025-09-29 12:17:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 12f2ef6e-d964-35b7-aaef-b23d53a1fcf5 | -7.21665 | -44.76673 | 2025-09-29 12:17:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 6052ae1c-664c-364b-b98a-cc841fa719ad | -6.07299 | -44.70078 | 2025-09-29 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 9774ac15-9abc-3fbe-85dc-beff8c5a8185 | -9.55018 | -43.25647 | 2025-09-29 12:17:00 | TERRA_M-T | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 12.2 |
| ec5af80b-91e3-3164-a3fd-02e040687316 | -7.55273 | -46.10645 | 2025-09-29 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 9330ef1f-e33f-308b-abcc-ab16be66ba4b | -8.0234 | -50.25368 | 2025-09-29 12:17:00 | TERRA_M-T | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| c67ad63b-4361-3faa-a002-475f64ed5a1a | -7.30062 | -42.8352 | 2025-09-29 12:17:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 6d31df4f-a4a0-31a5-87dc-7530b57aed44 | -6.9866 | -43.77845 | 2025-09-29 12:17:00 | TERRA_M-T | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 26.3 |
| bc1c16ea-422c-3b1e-a518-b5ea5c0b698a | -7.50996 | -44.29034 | 2025-09-29 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 18.1 |
| e2640df4-614f-32d0-91ee-ba3dd289772c | -6.71424 | -44.58472 | 2025-09-29 12:17:00 | TERRA_M-T | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e55c8106-e354-378b-95a5-c3fe054489ee | -2.9691 | -43.70927 | 2025-09-29 12:17:00 | TERRA_M-T | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 60aa236f-1a07-35e5-8e76-d6d34f42441b | -3.19868 | -43.45309 | 2025-09-29 12:17:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| d37db811-c724-360a-b2d6-aaab5ae1f9a2 | -7.96962 | -47.3134 | 2025-09-29 12:17:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 20b49907-2d41-3160-80a0-10bf937c191e | -4.35102 | -43.84208 | 2025-09-29 12:17:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 7c8606d5-3c50-30de-87e4-e246fe015b88 | -4.29811 | -49.19973 | 2025-09-29 12:17:00 | TERRA_M-T | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 80f1bdb0-9b16-300a-ac86-b8c41a638479 | -8.51178 | -47.84244 | 2025-09-29 12:17:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5b1ca1e4-d584-39d1-9769-696bfb13576e | -13.64475 | -48.05361 | 2025-09-29 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 12e36c19-f2df-3938-a438-9ee8b6c8c829 | -15.75921 | -48.15048 | 2025-09-29 12:19:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 4a74779d-d7db-3a01-aea1-59586dff0495 | -15.2167 | -50.11318 | 2025-09-29 12:19:00 | TERRA_M-T | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 35e557cb-f0c8-3567-891d-4f4ef42fa7ef | -16.2819 | -47.83691 | 2025-09-29 12:19:00 | TERRA_M-T | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 16.9 |
| ba862ab1-2f21-3086-b0aa-6d27969e3091 | -15.53905 | -41.49402 | 2025-09-29 12:19:00 | TERRA_M-T | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 26.0 |
| a28ba1f4-88f4-3dff-962f-24466518d955 | -15.28055 | -49.24648 | 2025-09-29 12:19:00 | TERRA_M-T | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 3a1314d4-2e1a-30ee-b12a-73e4fde3451f | -10.6271 | -48.51863 | 2025-09-29 12:19:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 476803fa-7a85-3f3b-9619-fd801d554dda | -14.49739 | -48.53698 | 2025-09-29 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 06598f13-6d85-3e69-952c-72683dc46046 | -10.69605 | -48.73984 | 2025-09-29 12:19:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c80ef049-0ca9-3b78-b57c-712f6ea218f7 | -14.59796 | -45.02188 | 2025-09-29 12:19:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 083a37ea-177e-3392-95dc-214b0a4f730d | -15.21813 | -50.10359 | 2025-09-29 12:19:00 | TERRA_M-T | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 8b77c3de-9cba-33dd-b754-5ab705dd2445 | -13.84232 | -47.50053 | 2025-09-29 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 22.9 |
| b988a304-9a9c-35a1-920d-a8808c3e74e6 | -14.61898 | -41.27276 | 2025-09-29 12:19:00 | TERRA_M-T | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 44.9 |
| 5a93d65f-578f-3a9c-831d-01da46cd39ac | -15.19813 | -48.47681 | 2025-09-29 12:19:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 9e4f5797-4b32-342a-8466-dd5debcc2bd8 | -9.41042 | -54.70166 | 2025-09-29 12:19:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| f8992d48-be24-389d-9353-eb2a9da3693c | -14.68263 | -48.14932 | 2025-09-29 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 16.8 |
| da3fa117-6d11-3242-81ac-8d42b9b2944d | -14.69568 | -45.21457 | 2025-09-29 12:19:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 7189387a-0760-3b44-b4a4-17000c8823fc | -9.77256 | -46.17682 | 2025-09-29 12:19:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| e08d3728-1fda-38db-8708-0059d401fcf3 | -15.22741 | -50.10175 | 2025-09-29 12:19:00 | TERRA_M-T | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6de352bb-0087-3dad-a7fd-f600db835bab | -13.85316 | -47.94778 | 2025-09-29 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a8f78b2b-9539-3b68-a4aa-551ccd5976ce | -10.44429 | -48.25829 | 2025-09-29 12:19:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 7b5c7215-e18f-31e7-a6f9-f39335a1ecf9 | -13.02805 | -49.44457 | 2025-09-29 12:19:00 | TERRA_M-T | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 1b52eddf-4146-3fb1-8a40-8dfb28f62af1 | -10.61686 | -48.52644 | 2025-09-29 12:19:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 31f66a78-4ccc-358b-b3b1-5f222c50f77d | -11.35903 | -45.06244 | 2025-09-29 12:19:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 37.9 |
| c1485e5e-b59d-3d15-afc3-52a4edf57ad6 | -17.74001 | -46.68404 | 2025-09-29 12:19:00 | TERRA_M-T | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| f1a80636-f759-36a7-8c06-f4eb1d02f438 | -13.00021 | -49.44364 | 2025-09-29 12:19:00 | TERRA_M-T | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 20f209fa-30e4-395c-9d9a-d2f4677fe9af | -16.42075 | -47.01465 | 2025-09-29 12:19:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5aae77e6-fccb-3776-bcfc-da16586f7ea7 | -11.4353 | -44.95374 | 2025-09-29 12:19:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 9a714a39-4404-3265-8f7c-9f5ba66f1f48 | -17.14156 | -48.27443 | 2025-09-29 12:19:00 | TERRA_M-T | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 171a6971-cae5-3e3f-a96d-49a21d9d22e7 | -15.55934 | -47.87154 | 2025-09-29 12:19:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 31.7 |


[Clique aqui para ver as próximas entradas](README85.md)
