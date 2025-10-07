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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 85660c7b-3b57-361f-a658-c8145998a927 | -21.85311 | -44.99987 | 2025-10-07 04:12:00 | NOAA-21 | CONCEIÇÃO DO RIO VERDE | MINAS GERAIS | Brasil | 3117702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c59ae2c2-cec2-369b-9b64-325e544b1a63 | -21.20823 | -45.03448 | 2025-10-07 04:12:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 84beb54b-3120-3a37-a439-538ff24a2d29 | -23.22502 | -46.56121 | 2025-10-07 04:12:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| b4002a77-0528-39c0-932f-199df319a4bb | -22.88487 | -43.72238 | 2025-10-07 04:12:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 7151e9bb-867b-3f06-9b44-c6a1ffbfbb54 | -22.54557 | -44.45015 | 2025-10-07 04:12:00 | NOAA-21 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| d99e3ee2-325f-3741-843f-085df571a44b | -22.9758 | -47.59908 | 2025-10-07 04:12:00 | NOAA-21 | MOMBUCA | SÃO PAULO | Brasil | 3530904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4670c527-fa42-3c2b-82ce-618441378d8f | -23.51324 | -47.23051 | 2025-10-07 04:12:00 | NOAA-21 | ALUMÍNIO | SÃO PAULO | Brasil | 3501152 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0df3630d-2e24-324d-bcc6-b739e249824a | -22.3184 | -47.1348 | 2025-10-07 04:12:00 | NOAA-21 | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 38dafa9f-af09-3fbc-913e-6802545054ee | -21.48986 | -46.91193 | 2025-10-07 04:12:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 73317674-58ef-3980-87cb-0c0238b9b40c | -21.51664 | -45.60107 | 2025-10-07 04:12:00 | NOAA-21 | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 60434d1b-a5f4-3430-a4b4-5ebd282477f4 | -20.41686 | -46.0425 | 2025-10-07 04:12:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e05df5e7-4bc3-35b2-8bb7-de6136712a3e | -22.22556 | -49.72537 | 2025-10-07 04:12:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 34a2b3ca-7f40-3f57-b882-576e1230f240 | -21.48921 | -46.91584 | 2025-10-07 04:12:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7869bab8-f77b-36ee-9e1a-ff715d836896 | -21.62015 | -45.2924 | 2025-10-07 04:12:00 | NOAA-21 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c5656f02-2eae-30a0-8502-54c1a3293406 | -23.3122 | -46.93988 | 2025-10-07 04:12:00 | NOAA-21 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 35be37f0-407e-37d8-be82-fe757ad3dbe3 | -21.08278 | -46.9044 | 2025-10-07 04:12:00 | NOAA-21 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1d2e86d1-6685-3722-a7e2-eeb563eb483a | -20.48866 | -47.02674 | 2025-10-07 04:12:00 | NOAA-21 | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b2e168e-0d1f-3908-ba53-acf2d88bc27c | -21.18838 | -45.61063 | 2025-10-07 04:12:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91d7658c-8074-37a6-adc0-81f50147f079 | -20.74958 | -43.4738 | 2025-10-07 04:12:00 | NOAA-21 | LAMIM | MINAS GERAIS | Brasil | 3137908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| c36bfef9-cb23-371e-8874-9eadf4f2f399 | -21.90777 | -44.88797 | 2025-10-07 04:12:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 72eacd17-5d0d-3bbe-80f0-e5633d60ffe8 | -22.00179 | -49.73191 | 2025-10-07 04:12:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c1089813-6d47-375e-a8ec-5f8f79dd6e28 | -21.74712 | -43.33762 | 2025-10-07 04:12:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5950af81-02b7-3e46-bc72-3d871ea32db5 | -22.00401 | -43.57 | 2025-10-07 04:12:00 | NOAA-21 | BELMIRO BRAGA | MINAS GERAIS | Brasil | 3106101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 32e53d55-638b-33bc-a86f-af67085ca75e | -20.28039 | -48.51012 | 2025-10-07 04:12:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2ac49e6b-8053-3b32-9849-6868503cf159 | -20.84953 | -49.47964 | 2025-10-07 04:12:00 | NOAA-21 | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f0770931-c25c-3421-872f-190a9c3d94e0 | -22.00089 | -49.73682 | 2025-10-07 04:12:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1786a93a-6454-3e16-b4e1-016a334b3df0 | -22.97443 | -47.60709 | 2025-10-07 04:12:00 | NOAA-21 | MOMBUCA | SÃO PAULO | Brasil | 3530904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a0208d3d-3027-38ed-963a-57b76d4bb5a8 | -21.90561 | -44.87999 | 2025-10-07 04:12:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| bba12567-d406-33cd-8483-14ad5d6c720c | -21.08067 | -46.89605 | 2025-10-07 04:12:00 | NOAA-21 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 565fbc97-7269-399d-bc94-f3d95585e26a | -22.01449 | -49.72131 | 2025-10-07 04:12:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| e5eca126-3871-35d9-a8b8-b5df3b138972 | -22.78716 | -42.48257 | 2025-10-07 04:12:00 | NOAA-21 | RIO BONITO | RIO DE JANEIRO | Brasil | 3304300 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 35b9b296-7ae0-361c-8f89-18437f509470 | -23.12805 | -47.00572 | 2025-10-07 04:12:00 | NOAA-21 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f9d81c31-ead6-3dfe-b575-2d053a4dc774 | -21.0073 | -47.04024 | 2025-10-07 04:12:00 | NOAA-21 | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3a9812ba-8a0a-3ecc-93e9-7e3a7dbb1bd7 | -23.26055 | -45.50494 | 2025-10-07 04:12:00 | NOAA-21 | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 6505f5ab-c5d4-34ea-b338-58f3dfcca993 | -21.10679 | -44.21385 | 2025-10-07 04:12:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5b3ef2fc-f5ee-35fc-ae44-2a0204c4c74c | -23.18137 | -47.25716 | 2025-10-07 04:12:00 | NOAA-21 | SALTO | SÃO PAULO | Brasil | 3545209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 2d9dd6ac-e989-3de6-8c3c-dcaf06422bfd | -23.27649 | -45.5117 | 2025-10-07 04:12:00 | NOAA-21 | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d7cb8374-b534-3847-8d00-482e1f62a16d | -22.01562 | -49.54863 | 2025-10-07 04:12:00 | NOAA-21 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 39001151-1e11-366c-a2c9-71fb719d2713 | -21.90618 | -44.8763 | 2025-10-07 04:12:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| be2933e6-027b-367c-91ea-5ef77c741dff | -21.49664 | -46.02168 | 2025-10-07 04:12:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 0f5c78e9-6ccd-3acf-952d-209dfe03dda9 | -22.01261 | -49.7313 | 2025-10-07 04:12:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| f95f6a3f-dd81-388e-a475-3ff6ac38e1d9 | -22.00558 | -49.73272 | 2025-10-07 04:12:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| cdf35f9d-8cee-30ac-847b-1f6cbd34e2f2 | -22.01547 | -49.73709 | 2025-10-07 04:12:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| b3e61845-9a40-33cb-a772-cd1b24a2d974 | -20.35503 | -48.78603 | 2025-10-07 04:12:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 428536b5-0f2e-367d-b5a3-3dc8060b6050 | -22.01923 | -49.71707 | 2025-10-07 04:12:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 75dd734e-32b3-3001-99eb-66a2dabaee95 | -22.79432 | -54.67173 | 2025-10-07 04:12:00 | NOAA-21 | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| c058aec1-88b2-3216-8965-8e50dcebb37c | -22.01168 | -49.73626 | 2025-10-07 04:12:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 207b0e56-cbc4-3938-858f-ec2cccc401c4 | -23.29848 | -45.48119 | 2025-10-07 04:12:00 | NOAA-21 | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| a2d095c4-a865-376d-b5c9-03f744fa96a7 | -21.07665 | -46.89913 | 2025-10-07 04:12:00 | NOAA-21 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0df7eecf-4375-3cb4-b13b-85c5b1eed64c | -22.01641 | -49.73206 | 2025-10-07 04:12:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 83e3de1c-c528-31f0-98a3-e2cae45298d9 | -23.38198 | -45.3811 | 2025-10-07 04:12:00 | NOAA-21 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2dcf1c9d-d3ca-3ddf-b89b-5a6b20ccb2f1 | -21.6113 | -43.99982 | 2025-10-07 04:12:00 | NOAA-21 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| bb0d294f-62cb-3d43-9d8b-7610497c2363 | -22.32184 | -42.53503 | 2025-10-07 04:12:00 | NOAA-21 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 49cc9383-0967-31c7-8a30-04b1672bbe2f | -22.54946 | -44.447 | 2025-10-07 04:12:00 | NOAA-21 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 17d125e1-ff02-32e1-8d56-4046e18e2231 | -22.17901 | -49.37846 | 2025-10-07 04:12:00 | NOAA-21 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 93c87676-d080-314b-84dd-dd8808682122 | -22.00269 | -49.72698 | 2025-10-07 04:12:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| f802cf73-fbd7-3002-bd77-75c1976642e3 | -22.02642 | -49.72652 | 2025-10-07 04:12:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 3b7a7984-7107-3d10-ace2-3f3cfd68338b | -22.17618 | -49.37277 | 2025-10-07 04:12:00 | NOAA-21 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 28b959ea-635e-3199-840a-39275bb303d0 | -23.30949 | -46.9354 | 2025-10-07 04:12:00 | NOAA-21 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d5b7d5e9-e013-3e5c-b0ff-c7e0eb0ffa98 | -22.32244 | -47.13153 | 2025-10-07 04:12:00 | NOAA-21 | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 64fa1f71-2ea7-32bd-ab00-f0ec6cc0482b | -23.40244 | -47.57641 | 2025-10-07 04:12:00 | NOAA-21 | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1785db26-708b-3df6-bfcf-8ec917c39579 | -22.22933 | -49.72623 | 2025-10-07 04:12:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 384ab7db-b6be-3324-8384-54da529432ea | -21.9989 | -49.72614 | 2025-10-07 04:12:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| d1f723db-4bcf-38fc-9b60-b3a645f1c1e0 | -23.38139 | -45.38484 | 2025-10-07 04:12:00 | NOAA-21 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 56661595-37b7-39ff-a090-b12a39d29ee5 | -21.55295 | -44.27439 | 2025-10-07 04:12:00 | NOAA-21 | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 290f685a-ad8e-3643-82d2-56a0f04e6a0d | -21.9971 | -49.736 | 2025-10-07 04:12:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 25380a46-c072-38e8-b921-ad28c49df3fa | -23.36943 | -47.16725 | 2025-10-07 04:12:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 664d414e-f7b1-3db3-bd55-9553e2ce5c10 | -21.30087 | -45.94823 | 2025-10-07 04:12:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cd89afd2-e0b6-33c8-8365-0e52c3308354 | -23.33699 | -46.78997 | 2025-10-07 04:12:00 | NOAA-21 | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 548febfc-cb5c-359b-9b08-adb0cf280628 | -22.78928 | -54.67051 | 2025-10-07 04:12:00 | NOAA-21 | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| cf4aa493-77cf-3908-b26e-37e0063393ee | -22.31906 | -47.13087 | 2025-10-07 04:12:00 | NOAA-21 | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| debc40d5-4976-39ef-b2a0-98c67fe8d919 | -22.16896 | -49.39142 | 2025-10-07 04:12:00 | NOAA-21 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ed8a07a-3d5f-34ad-9d2c-9b3f2a987f70 | -22.13402 | -42.91281 | 2025-10-07 04:12:00 | NOAA-21 | SÃO JOSÉ DO VALE DO RIO PRETO | RIO DE JANEIRO | Brasil | 3305158 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f3eef6b0-9507-3ee1-8a6b-5d36ed7bb69e | -21.07729 | -46.89532 | 2025-10-07 04:12:00 | NOAA-21 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d0f581aa-13f4-3fed-ad7f-a722336431f9 | -20.82683 | -42.48307 | 2025-10-07 04:12:00 | NOAA-21 | MIRADOURO | MINAS GERAIS | Brasil | 3142106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 2f9ff758-d917-319c-b0bb-6dd8e4d0e840 | -21.76854 | -47.77901 | 2025-10-07 04:12:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6469db62-4b94-3b0a-8064-51aac8aecc52 | -23.29907 | -45.47745 | 2025-10-07 04:12:00 | NOAA-21 | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c13c46b5-689c-32f3-b7e9-3aab4332b206 | -22.02262 | -49.72577 | 2025-10-07 04:12:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 0bd2bb14-18a2-326b-8c62-66e367acdad2 | -21.49271 | -46.02482 | 2025-10-07 04:12:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| e7d0b776-d522-3e9e-be79-2fb50b437fcf | -21.09851 | -44.20102 | 2025-10-07 04:12:00 | NOAA-21 | TIRADENTES | MINAS GERAIS | Brasil | 3168804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7bc500a5-aa21-3ce9-a6b0-eaff3be03f93 | -23.31957 | -45.7579 | 2025-10-07 04:12:00 | NOAA-21 | JAMBEIRO | SÃO PAULO | Brasil | 3524907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| e1e33cc3-7c0a-33dc-bca8-a6a9b61494e8 | -21.51995 | -45.60167 | 2025-10-07 04:12:00 | NOAA-21 | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| e7641b0b-c591-3829-9c58-61c394426d87 | -22.02732 | -49.72155 | 2025-10-07 04:12:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 5aa29cfa-ac3d-3744-842b-f62019041fc2 | -23.3149 | -46.94442 | 2025-10-07 04:12:00 | NOAA-21 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b3e42645-fdb5-3c0f-9582-4db6e5a7bf52 | -23.20492 | -47.2414 | 2025-10-07 04:12:00 | NOAA-21 | SALTO | SÃO PAULO | Brasil | 3545209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b10f9f23-4381-3d4b-b922-d8f2bf519031 | -19.85362 | -49.0729 | 2025-10-07 04:12:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 058dd3d4-97b8-3c2d-a642-d9137defa38e | -22.90752 | -45.58723 | 2025-10-07 04:12:00 | NOAA-21 | TREMEMBÉ | SÃO PAULO | Brasil | 3554805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 77971831-b338-3a45-9285-16a0df15b85f | -20.75018 | -42.87485 | 2025-10-07 04:12:00 | NOAA-21 | VIÇOSA | MINAS GERAIS | Brasil | 3171303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0ac86861-ffaa-324b-b7f1-771652051525 | -21.39139 | -45.03637 | 2025-10-07 04:12:00 | NOAA-21 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9dd373be-94fa-3c0c-beb3-3c753d69862e | -22.02304 | -49.71782 | 2025-10-07 04:12:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| dbf8b2bb-1894-3583-b03f-709bb7c6c0a7 | -23.15202 | -46.56717 | 2025-10-07 04:12:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 42a29c07-22cf-3234-8c98-533780422f8a | -22.5313 | -43.58101 | 2025-10-07 04:12:00 | NOAA-21 | ENGENHEIRO PAULO DE FRONTIN | RIO DE JANEIRO | Brasil | 3301801 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ee30dc6d-6b35-3cf7-9576-0a4bc6b3d735 | -22.00205 | -47.32049 | 2025-10-07 04:12:00 | NOAA-21 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| bc7be16c-1867-3351-b063-6212904e8593 | -21.74194 | -44.41702 | 2025-10-07 04:12:00 | NOAA-21 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 5fa1b848-ac6d-37be-a55e-6aa8c0503402 | -22.00848 | -49.73846 | 2025-10-07 04:12:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 06868c95-ab67-37f2-8398-647538df26e6 | -21.49603 | -46.02542 | 2025-10-07 04:12:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| b4a5c9d2-ffb8-3cd3-b89c-772514562fee | -21.57314 | -45.26554 | 2025-10-07 04:12:00 | NOAA-21 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2b31d480-36cc-382f-a2b5-5dbba2e39eac | -21.19109 | -45.61493 | 2025-10-07 04:12:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d3b4ee5c-bb3d-3570-848c-58549d6c4c4e | -22.01228 | -49.7393 | 2025-10-07 04:12:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 5db7b82b-f4f1-377e-bd8b-40534ab0838a | -22.00272 | -47.31654 | 2025-10-07 04:12:00 | NOAA-21 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |


[Clique aqui para ver as próximas entradas](README47.md)
