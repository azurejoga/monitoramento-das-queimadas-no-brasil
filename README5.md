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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0828997-9845-3923-9bba-4a15f30d4e08 | -9.09916 | -50.02763 | 2025-06-22 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 912ec522-a909-36ee-8f7f-51b310354a95 | -4.42443 | -48.1409 | 2025-06-22 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9fe08773-3adb-3ec2-b74b-ba4d0d6b25fb | -6.86942 | -47.23869 | 2025-06-22 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ca5745d9-87ea-3b80-9213-72f4e77107d6 | -5.77429 | -46.56995 | 2025-06-22 04:14:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b89a8960-4017-3f61-b632-264d8bcc76ea | -8.72682 | -47.15699 | 2025-06-22 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c13f1ee1-95c8-3507-8726-0787806440cd | -8.08324 | -43.1521 | 2025-06-22 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| c73d4621-3da1-3a16-8d68-c853950511c3 | -4.53741 | -48.01311 | 2025-06-22 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 372978cb-c09f-3ccf-b24e-276174e3593f | -7.10653 | -43.71956 | 2025-06-22 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98e60b5e-54de-3135-ac60-e606b13e2de0 | -8.00258 | -49.71085 | 2025-06-22 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b6d255a-f82b-3297-8d66-2aaaf4bcd450 | -10.65044 | -44.4919 | 2025-06-22 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2667c6b6-b49c-395e-96ab-91ad155d2ca0 | -7.14792 | -48.20675 | 2025-06-22 04:14:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e01bf618-ad40-3dac-b393-916e63c21daf | -8.03509 | -47.64209 | 2025-06-22 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 98b6044d-c122-32ce-87b0-aadd33d828b7 | -7.8784 | -47.88431 | 2025-06-22 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8380cc05-cfd3-37d3-87a4-861c7d6cebe3 | -7.87457 | -47.88365 | 2025-06-22 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0a1f6c1d-a733-3ec0-b1b3-1d2207639419 | -8.59972 | -51.58675 | 2025-06-22 04:14:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 37b77c0d-8bda-32a4-b67e-826821760440 | -4.54209 | -48.01011 | 2025-06-22 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9e8136d-47c2-37fa-93b2-aa873e489d41 | -8.00779 | -47.66632 | 2025-06-22 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aeb9e6e7-afc7-3c58-a731-9e88ffc01add | -22.00303 | -47.81204 | 2025-06-22 04:17:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a07f108-f054-3b0b-a045-613405b66585 | -22.69897 | -43.34712 | 2025-06-22 04:17:00 | NOAA-21 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3c2ab0c1-2d9d-351f-bf90-e4f8e9dd99de | -22.7853 | -43.7579 | 2025-06-22 04:17:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 46ac99e9-e86e-38db-8336-c38687d86b12 | -22.95494 | -43.04268 | 2025-06-22 04:17:00 | NOAA-21 | NITERÓI | RIO DE JANEIRO | Brasil | 3303302 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d90e9af0-7472-307b-95b2-dfa2e51cb2af | -21.19495 | -44.93888 | 2025-06-22 04:17:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 01eb54cb-fe28-36cc-bb9b-4b917bc66e61 | -21.13277 | -47.80105 | 2025-06-22 04:17:00 | NOAA-21 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca5a4b0a-0337-3861-8726-c34509b6b997 | -23.33766 | -46.77337 | 2025-06-22 04:17:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ea4e0597-bd7c-325f-88df-a30a321ca7a7 | -22.00364 | -47.8083 | 2025-06-22 04:17:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 650e040c-cb77-3d9a-b8a7-464faa5b0e20 | -23.59937 | -45.95642 | 2025-06-22 04:17:00 | NOAA-21 | BIRITIBA MIRIM | SÃO PAULO | Brasil | 3506607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 07f8006a-91d2-3e4d-a490-8804b4ce3fd5 | -22.73825 | -42.96053 | 2025-06-22 04:17:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a6534685-2fae-3e7f-8535-e0715f9d7747 | -22.89527 | -43.46829 | 2025-06-22 04:17:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| eaf9dbfd-5556-38da-974c-4db6b3175ad3 | -22.47444 | -43.54832 | 2025-06-22 04:17:00 | NOAA-21 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2f9d1a03-954c-3d7d-a44c-2ac35b997714 | -20.76396 | -46.77055 | 2025-06-22 04:17:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8269db4b-c64f-3b6c-bef1-892a0e2fc51f | -14.26093 | -45.50363 | 2025-06-22 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7c4cd54-c75d-3fdc-a9e0-69998bbf0882 | -12.41843 | -43.81647 | 2025-06-22 04:17:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7b015e04-52cc-33fd-bcbe-fd67fade4ed5 | -9.4674 | -56.05858 | 2025-06-22 04:17:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2605c2ed-5fe6-32b8-9e44-4130396b5d34 | -13.79264 | -54.30195 | 2025-06-22 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9665a94d-cc9a-3512-a51f-24b32098e020 | -11.83577 | -57.76504 | 2025-06-22 04:17:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1a8c83d-303a-3690-94ce-29d5eeac046c | -10.56844 | -46.93659 | 2025-06-22 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b4e2c2be-0867-3eb9-a85f-5768e47906c7 | -10.4563 | -47.0217 | 2025-06-22 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 531f1c17-1168-3c0b-869f-130c9f62b768 | -13.03793 | -53.71268 | 2025-06-22 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 714a08cd-a350-3d47-9ba0-621c68840f43 | -10.89181 | -56.46831 | 2025-06-22 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ad6d31b8-86d6-3913-8cb0-3185dc437e55 | -11.13781 | -53.92244 | 2025-06-22 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 48bf19a2-3287-30f3-b6be-b41a085cde3e | -13.04491 | -48.84431 | 2025-06-22 04:17:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5c39525-6050-37eb-8093-0ba2b34801ec | -13.8032 | -54.30412 | 2025-06-22 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d0cc8829-7619-3b9d-b8c4-6d0696e8c414 | -12.47266 | -54.42567 | 2025-06-22 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| a88f874e-e9b7-356d-9cc0-48bbe50dcce0 | -14.26036 | -45.50718 | 2025-06-22 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a3a3ca72-4186-30dc-978d-e42e342b4778 | -10.95863 | -49.57192 | 2025-06-22 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4d47244c-c44c-3a78-af0b-c8b08add15c4 | -9.45729 | -56.06561 | 2025-06-22 04:17:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b365fe37-7cad-3292-9cfe-21003f74e545 | -13.80513 | -54.29419 | 2025-06-22 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 73e815a4-1123-3649-a7f3-e77b23475d99 | -11.11133 | -46.66279 | 2025-06-22 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19cac991-0d6e-3445-9120-cf8b2d484f13 | -17.0483 | -43.7728 | 2025-06-22 04:17:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 26dab49a-468f-3431-8477-07a34ea18ceb | -17.65762 | -46.8484 | 2025-06-22 04:17:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc55e21c-5f6f-3ff2-8fca-045a51fc091f | -11.74345 | -54.71661 | 2025-06-22 04:17:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3985a586-9031-3787-aa90-7095174b263d | -18.06031 | -44.49171 | 2025-06-22 04:17:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d00cc2f9-201f-320d-8def-66154dd3394d | -12.65266 | -54.08154 | 2025-06-22 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af8c9fb7-0aac-3318-90b9-99759d86c0b5 | -11.61257 | -58.28767 | 2025-06-22 04:17:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e13e1602-1e44-3520-98d5-d169cf096625 | -9.45892 | -56.06805 | 2025-06-22 04:17:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 1c47d469-cd5e-37ab-9ce0-660f00d87a50 | -10.89409 | -56.46756 | 2025-06-22 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e371c86d-c8dc-307b-b080-44e17eb76fc0 | -10.2308 | -54.29354 | 2025-06-22 04:17:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78d1e77d-7435-332d-a9cf-017a514ae828 | -9.4647 | -56.06136 | 2025-06-22 04:17:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 0046b816-ac18-3f25-a179-ef1064ed7646 | -10.99152 | -45.08788 | 2025-06-22 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3ee82153-da17-34ef-a16d-74d135de23e2 | -12.42175 | -43.817 | 2025-06-22 04:17:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb0f4192-3c0a-3eb2-99a8-293b131e94fa | -10.98764 | -45.09089 | 2025-06-22 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 22b2113c-4624-3de8-a352-e13c677fb3d0 | -13.78865 | -54.29427 | 2025-06-22 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 812ca3b7-cf65-340f-bbc3-fb2fe8ba3325 | -9.47336 | -57.84253 | 2025-06-22 04:17:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0571c9eb-007f-3f8e-af74-76a9a472493e | -15.3961 | -46.68476 | 2025-06-22 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c865383-b146-3f33-ab5a-543f4c8c6e91 | -14.11945 | -41.67615 | 2025-06-22 04:17:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ce8b1c07-a587-3693-91b1-3a12b2be530c | -10.44081 | -47.02841 | 2025-06-22 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f785480b-f5a2-38d7-8144-86356572847c | -17.66096 | -46.84899 | 2025-06-22 04:17:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 038b58a1-00d9-3396-acc7-e9f6e246a7ed | -10.8656 | -53.76194 | 2025-06-22 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01b5f55c-7eaa-3c45-ae26-beb8203aa4a2 | -10.85958 | -53.76434 | 2025-06-22 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62740b40-152b-3bed-80f4-5987f829f325 | -17.59641 | -43.1979 | 2025-06-22 04:17:00 | NOAA-21 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf464377-eea8-327c-a58f-ac95754198e2 | -10.45985 | -47.02227 | 2025-06-22 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d8cb50a9-a56f-39d0-8ee0-ad741c32be8f | -9.46235 | -57.83879 | 2025-06-22 04:17:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ff72c2c0-aae2-3b7a-b0d4-6c2b6e76e2a1 | -13.80449 | -54.2975 | 2025-06-22 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 44d50f1c-b738-37c2-a77a-b5ddee6193bb | -10.57328 | -46.9291 | 2025-06-22 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 21eb6f22-1849-3b63-ba73-02830c145802 | -9.46638 | -57.8409 | 2025-06-22 04:17:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 90382632-fff3-32e8-8951-2fef657d9823 | -14.25431 | -45.50253 | 2025-06-22 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4cd79111-8d92-37c5-bd32-7e4a9a041b33 | -11.79259 | -57.24513 | 2025-06-22 04:17:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8fd9ddad-e1b7-39a7-af1f-c80baf7beac4 | -10.06322 | -49.66542 | 2025-06-22 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ebdfac39-48f8-3baa-b7e5-01f6df32d182 | -12.47338 | -54.42196 | 2025-06-22 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d4adf2cd-c940-3dcd-960c-c5f8782c15a9 | -13.23849 | -48.4155 | 2025-06-22 04:17:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7cfaf452-a683-37a9-87a0-e2a1343f52b4 | -11.33682 | -45.22781 | 2025-06-22 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ac530a6b-b7d6-37c2-9f37-af8a7529ba98 | -10.23337 | -54.29709 | 2025-06-22 04:17:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6983e5a3-fed9-3507-8f71-42ed5358eeb2 | -12.65135 | -54.08839 | 2025-06-22 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03ea29ce-727c-35df-af7c-8061483b3fbc | -13.78737 | -54.30085 | 2025-06-22 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cadaac62-260a-3af3-9c0d-9a10ad289f6a | -10.06804 | -49.6623 | 2025-06-22 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3870c14-f15b-377b-8520-8af82cc71bbb | -11.42595 | -54.32586 | 2025-06-22 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aff3d3f5-764f-37ca-9983-027228b26c9e | -13.65605 | -53.94223 | 2025-06-22 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2252fce8-c1d3-3bc6-b921-f5c79312a65e | -12.58335 | -56.97135 | 2025-06-22 04:17:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e000ece-dd99-3a1a-b2dc-1f87b8ead8ee | -11.13914 | -53.91543 | 2025-06-22 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7df10362-2dde-3a66-91b3-51667311ede6 | -11.58069 | -44.65398 | 2025-06-22 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| faf7718e-db84-3568-9487-dd72b4f3a4da | -15.39886 | -46.68905 | 2025-06-22 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a1bd81ca-0214-30ff-9e0b-7ecb7c18e26a | -13.65149 | -53.93797 | 2025-06-22 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5e0ea91e-39ae-3a19-aa6f-af20e0a3a6e6 | -12.58228 | -56.97654 | 2025-06-22 04:17:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f454fc97-674f-32bd-8c1c-a89d717abe15 | -9.45833 | -56.0602 | 2025-06-22 04:17:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 26d65c24-0c9d-32cc-90da-8392e19f5886 | -10.285 | -47.6116 | 2025-06-22 04:17:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79018507-4e38-3445-bcce-b622dca00b55 | -11.61959 | -58.2889 | 2025-06-22 04:17:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b1e5d9b0-77e5-3d03-8a33-65f717ed598d | -12.41898 | -43.81292 | 2025-06-22 04:17:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bbf25f43-a0e3-392e-a1f5-57dd9db31820 | -11.09771 | -46.68061 | 2025-06-22 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 403284cc-3452-3a94-968f-7daa4f0de673 | -13.80384 | -54.30082 | 2025-06-22 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab3b5d24-ed06-3f19-8418-b0f28afb1538 | -10.98489 | -45.08681 | 2025-06-22 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |


[Clique aqui para ver as próximas entradas](README6.md)
