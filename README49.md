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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba6fe5c3-42de-35f2-96ce-ed47fb021aeb | -11.97169 | -45.78441 | 2025-09-04 04:27:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6cb42e75-bc80-3761-8b97-5d5b900e0b9c | -13.65167 | -48.14624 | 2025-09-04 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80d59101-7d77-3b1c-89b0-52127a513f61 | -9.06078 | -46.98681 | 2025-09-04 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb5174d0-8764-31aa-87ec-95da9bea7552 | -12.88964 | -56.93715 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34bf05a7-2735-3cb7-81b0-df81140df02f | -14.78755 | -48.16924 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a5fefbd-5065-391d-8779-a4ba716e5bef | -14.9951 | -50.06972 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2bb5ee5-14a2-379d-98a9-780295b4bef1 | -11.76383 | -44.65292 | 2025-09-04 04:27:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42c58f2b-049e-37f3-b7cd-e357cf46ec31 | -8.19942 | -44.79181 | 2025-09-04 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 787018de-1275-3727-a812-86559e7462ff | -11.87661 | -51.54085 | 2025-09-04 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a9428b0c-470d-3765-b154-8ee79979bc5b | -10.89889 | -50.83455 | 2025-09-04 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 18b7335c-903c-371a-a379-b57aef04367b | -13.74566 | -46.94266 | 2025-09-04 04:27:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 16e0e65a-e378-39c9-aa32-18461d7d794c | -7.2679 | -57.55835 | 2025-09-04 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e69ae9cb-7c0c-365e-a0af-1c6ba5365a48 | -8.08527 | -45.35773 | 2025-09-04 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 426e3a6b-a989-385c-a0ab-1942bb8af728 | -11.24557 | -44.9603 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f4e5ebfd-8e44-390b-83bf-7cb2e82dea6e | -12.87255 | -48.01808 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aa7ce965-4407-379c-a10f-1dc840c4db15 | -11.79353 | -51.52433 | 2025-09-04 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea94141e-04c6-3d0a-866e-06bc269c1d8a | -19.68507 | -49.36248 | 2025-09-04 04:29:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8e8bc9e8-ea2e-3818-b94c-cb4623ea947a | -19.6845 | -49.36613 | 2025-09-04 04:29:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a140f7e6-63cf-3363-882f-712e8cd0be5c | -16.31193 | -52.95343 | 2025-09-04 04:29:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 35355d6a-ca57-32ad-beb3-fa3e27cbf82b | -19.26865 | -49.7844 | 2025-09-04 04:29:00 | NOAA-21 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 52349cff-845b-3274-9aa5-8f0356be4fed | -15.54733 | -48.33422 | 2025-09-04 04:29:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1adbdea3-376c-3b2d-9839-e521bdfe2177 | -15.53851 | -48.34737 | 2025-09-04 04:29:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95932345-aacc-380e-a846-1ab954b2bc62 | -19.69395 | -49.34903 | 2025-09-04 04:29:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 405fe8ed-ab00-37b3-8220-f5aeb96ea0e7 | -17.97293 | -47.12392 | 2025-09-04 04:29:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 44765e0b-87ae-330f-9ed9-9452b37ed73a | -15.73688 | -53.63505 | 2025-09-04 04:29:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 56c6a5ed-c32f-3443-9343-e8c070b3b986 | -15.5544 | -48.4194 | 2025-09-04 04:29:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 077c07b8-1f34-36a3-81c6-fb49d6970e46 | -15.14221 | -52.33514 | 2025-09-04 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 058ef99b-5749-30bf-85da-e670b0cfcce1 | -14.88027 | -59.50227 | 2025-09-04 04:29:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 253531eb-7424-3afc-8a6a-a0ece75475ee | -15.14945 | -53.51405 | 2025-09-04 04:29:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bdd47fdb-a17d-3960-85bc-f561b5a20383 | -16.31382 | -45.70536 | 2025-09-04 04:29:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7179e55-e23d-3e33-b488-54c21130d40d | -19.71572 | -49.14281 | 2025-09-04 04:29:00 | NOAA-21 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b3a89a20-ae89-33f0-b9cb-7e16725b5d8b | -15.74154 | -53.63202 | 2025-09-04 04:29:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f3b9879d-6d2f-3702-b9d7-eb373caccd9a | -20.70681 | -46.30783 | 2025-09-04 04:29:00 | NOAA-21 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc3ff340-f829-37bf-9b37-66cee1e749ef | -17.9735 | -47.12002 | 2025-09-04 04:29:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d5911dd3-5b37-374d-aef3-bd3a93d07751 | -15.58393 | -54.31906 | 2025-09-04 04:29:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d5db373f-682f-3177-bf01-03ee2084bcdc | -19.42719 | -46.51814 | 2025-09-04 04:29:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa99d540-b6c6-34b1-920a-9786ee3725f1 | -15.15831 | -52.37543 | 2025-09-04 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f837aab0-2a03-3bcb-aaae-be806df05964 | -16.85674 | -49.62931 | 2025-09-04 04:29:00 | NOAA-21 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ceee9332-d7a6-39b8-95c1-4cb705994f23 | -19.75626 | -44.11007 | 2025-09-04 04:29:00 | NOAA-21 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fb2c3950-f18d-3a8b-85cb-4896f16e24f4 | -15.30633 | -52.75859 | 2025-09-04 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1417d5cd-748b-3394-862c-71f1652c502b | -20.09708 | -44.13482 | 2025-09-04 04:29:00 | NOAA-21 | MÁRIO CAMPOS | MINAS GERAIS | Brasil | 3140159 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 78a68496-829c-375c-ad02-101f917b6c42 | -15.54729 | -48.37806 | 2025-09-04 04:29:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3496e1a8-da9a-3e6c-ba80-55dace9acd52 | -15.30123 | -52.74284 | 2025-09-04 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77d52367-fff7-30ad-adf3-ca0c3ae7dd07 | -17.05993 | -46.44762 | 2025-09-04 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ec79f233-38fb-39bc-bca6-e87e3d0877de | -15.54679 | -48.31587 | 2025-09-04 04:29:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39e39bda-470e-3ca4-b586-4c49d685d695 | -17.03911 | -46.49334 | 2025-09-04 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a0e62dd2-e792-3080-8693-ba1df1b3ee7a | -18.56523 | -44.02755 | 2025-09-04 04:29:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6d7732e-7b16-3d0f-b45f-e5e946128055 | -15.40808 | -55.94279 | 2025-09-04 04:29:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2ef3a310-ade5-38f0-b3af-002609275442 | -20.09213 | -44.14112 | 2025-09-04 04:29:00 | NOAA-21 | MÁRIO CAMPOS | MINAS GERAIS | Brasil | 3140159 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| dc3cc1d3-bfae-3ed2-8212-8b81528194bf | -19.22127 | -44.48036 | 2025-09-04 04:29:00 | NOAA-21 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 72e402ce-cb7c-3876-98f4-92e568b7e715 | -15.5446 | -48.3082 | 2025-09-04 04:29:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e45840f8-ee73-394a-b9ab-a87fca5892d2 | -17.17375 | -46.23655 | 2025-09-04 04:29:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 765e0120-5206-3962-bac2-1b1c28635b4a | -16.29779 | -45.69003 | 2025-09-04 04:29:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 37d79464-6c3d-3b05-accf-7168a38ef0c8 | -16.53359 | -55.08995 | 2025-09-04 04:29:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a6876305-cfe2-3eb6-9f6b-1f28b013da02 | -16.47352 | -46.86679 | 2025-09-04 04:29:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4bf251b2-9649-3d1a-a5a4-e63ee278724b | -15.20206 | -52.35306 | 2025-09-04 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d4cbd7d-8266-3bdb-9557-e5a6bbe1ecf9 | -15.72565 | -53.62904 | 2025-09-04 04:29:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3e318f3-40cf-3e11-99e8-7c734d65edd3 | -16.31573 | -52.95403 | 2025-09-04 04:29:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 393b6155-ec1d-3b5e-abc7-220d3605d954 | -17.17784 | -46.23301 | 2025-09-04 04:29:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 518ece44-b22a-3d71-b7ec-14441c4a13d1 | -15.47146 | -53.01694 | 2025-09-04 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74845995-e0ce-3b69-bb27-2c1e18f90789 | -18.97117 | -47.47941 | 2025-09-04 04:29:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c8f87e5f-3f4d-3203-9be6-9e8af62e2c72 | -20.09663 | -44.13841 | 2025-09-04 04:29:00 | NOAA-21 | MÁRIO CAMPOS | MINAS GERAIS | Brasil | 3140159 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e6f12157-23f7-3cc7-b6fc-834884016325 | -15.60766 | -52.88371 | 2025-09-04 04:29:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9c656c1e-455a-3f9e-b8d9-8d29763969a2 | -16.00718 | -49.28032 | 2025-09-04 04:29:00 | NOAA-21 | SÃO FRANCISCO DE GOIÁS | GOIÁS | Brasil | 5219902 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5ace66fc-e535-326c-aaa0-3e955b4a4fa4 | -17.17435 | -46.2575 | 2025-09-04 04:29:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| df293b9e-04cf-34ca-bd8e-782b55e41a16 | -15.19678 | -52.36129 | 2025-09-04 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c2be4b3-ce27-3770-a991-459debc571a7 | -14.58119 | -53.0293 | 2025-09-04 04:29:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4f315d2a-f841-367e-8bbf-80ce58d73506 | -20.29853 | -46.71555 | 2025-09-04 04:29:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6a5aba26-6beb-3383-9862-d5148a7638e6 | -17.15796 | -46.2466 | 2025-09-04 04:29:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 5cdb6c6c-f9df-3b47-9759-ac4db8c589fd | -20.93294 | -49.47103 | 2025-09-04 04:29:00 | NOAA-21 | BADY BASSITT | SÃO PAULO | Brasil | 3504602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 44b3fbe9-78e4-342f-ab79-9a6a1b9e9bfb | -17.61263 | -43.76447 | 2025-09-04 04:29:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66e191cf-d4bd-3cc8-a122-6e1e97ed2f99 | -18.32937 | -50.98228 | 2025-09-04 04:29:00 | NOAA-21 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 88b8cf2d-072a-30ce-93fa-5e0f9a152463 | -17.67835 | -47.86292 | 2025-09-04 04:29:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ed30e1b-d5a6-35e6-94e6-8fd5157420f9 | -15.17525 | -52.35276 | 2025-09-04 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b0e98a03-02b6-312e-aa0f-e15dc9ad13df | -14.58392 | -53.01379 | 2025-09-04 04:29:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 33d506af-95e9-33c8-94a4-62ea12fb8c27 | -15.40913 | -55.93737 | 2025-09-04 04:29:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3045edf5-26cd-3e84-8a88-a965170bfbc2 | -19.62097 | -46.31345 | 2025-09-04 04:29:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6ee56416-2a17-3548-b577-2af78d1a5099 | -15.15533 | -52.37039 | 2025-09-04 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f1c25ea3-a825-34fe-ac7f-d81a36ab587b | -15.7105 | -48.87698 | 2025-09-04 04:29:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7572c6ee-bd07-3f40-9556-375635ce3099 | -14.56703 | -54.53642 | 2025-09-04 04:29:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 23c0d11d-f672-3622-a5cd-6438dab2b7f2 | -20.09794 | -50.00462 | 2025-09-04 04:29:00 | NOAA-21 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| c7aa7bb8-c4ad-368b-b91a-92edeeb75744 | -16.30789 | -45.69587 | 2025-09-04 04:29:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ae1e6136-603c-3b66-84be-20fea5f66d48 | -15.60497 | -52.67572 | 2025-09-04 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 046ac326-6355-3b8e-a76b-bf4322843f12 | -16.31107 | -52.95825 | 2025-09-04 04:29:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e87ed383-d79a-3141-8c28-26ffb3faff2d | -19.7522 | -44.10944 | 2025-09-04 04:29:00 | NOAA-21 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8649d271-7946-3367-8144-8c37392013bb | -14.5851 | -53.03001 | 2025-09-04 04:29:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 618f7f4d-ba2d-3de7-89fc-9e8a8f8db99f | -16.31776 | -52.96464 | 2025-09-04 04:29:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c829ec5b-f866-35c5-82f5-317c597d60f0 | -15.61948 | -52.87822 | 2025-09-04 04:29:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45e71e6d-208d-3fc5-b6f8-2b00a55ab8cd | -18.56975 | -44.02427 | 2025-09-04 04:29:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 555fe75c-2903-3a5e-a571-39ed67ca6c6e | -15.56892 | -49.55084 | 2025-09-04 04:29:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f9c5e93-5f08-3d41-aa38-7e3ebcc0f188 | -15.9897 | -55.9773 | 2025-09-04 04:29:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 2586f416-39c6-3edb-9453-32f5e5e57a8f | -21.34211 | -45.63958 | 2025-09-04 04:29:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| ac42437c-1fdd-3527-9782-f2298376801e | -15.61993 | -52.88099 | 2025-09-04 04:29:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 782d1fb6-af58-35d3-bc10-027be8b46351 | -16.8154 | -51.32832 | 2025-09-04 04:29:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fe7c3869-86f7-3890-a410-5652746f90fb | -20.18471 | -48.69639 | 2025-09-04 04:29:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f10b8c9-8506-3589-8e5a-325d9f472a76 | -17.0426 | -47.14157 | 2025-09-04 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 4cd30dd2-aa59-33a6-afca-1c40b65491f2 | -15.30463 | -52.76837 | 2025-09-04 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6645da96-ed66-38bd-9f61-fa4c6864c63c | -15.24628 | -53.79446 | 2025-09-04 04:29:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 438f9d40-8a0f-311f-a55e-2e366afdba14 | -17.75039 | -48.64085 | 2025-09-04 04:29:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5026431c-e871-3712-9bdf-dced45b79903 | -15.5678 | -53.96295 | 2025-09-04 04:29:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README50.md)
