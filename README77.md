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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 58fb75f3-418a-37c3-83b1-207f33e3098b | -6.15146 | -51.63227 | 2025-09-13 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df412b22-2d31-3a16-b45f-cb72d8116115 | -7.91019 | -55.26574 | 2025-09-13 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44686013-1cf4-3666-ab77-9665623ee2ff | -9.89992 | -51.88613 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29a54874-0e22-360d-8013-e0871b5e9d75 | -7.56168 | -44.09272 | 2025-09-13 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bde044b6-7e6b-30b7-ab46-cab40416b929 | -7.39215 | -45.85913 | 2025-09-13 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b0570c04-61bd-39dc-b928-2044098ce6fb | -3.22211 | -47.12674 | 2025-09-13 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 03a58079-ee5b-3ddf-9899-87b71db1f4da | -9.02505 | -47.04221 | 2025-09-13 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bac6eb66-f000-342a-93af-564a0f16c9be | -3.4106 | -52.66342 | 2025-09-13 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 94c92161-127a-361a-aa89-fd2e547ecd64 | -4.92249 | -47.8679 | 2025-09-13 04:57:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fbc7e742-a824-34e8-8be8-671c9018a907 | -5.18352 | -46.16895 | 2025-09-13 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3e0d00b-c59e-397a-b442-365b0770a7ea | -3.21806 | -47.63642 | 2025-09-13 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 684bd553-ad31-3be6-8964-5454a737a785 | -2.98516 | -48.60391 | 2025-09-13 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da1db0c8-87d9-35b2-a9bb-1aa92526726a | -9.90247 | -51.86897 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 428fed90-376b-384e-ab9f-ef74672441d9 | -9.25044 | -51.24701 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2a0859d4-a8cb-3231-8404-465dfb978106 | -7.31765 | -43.92311 | 2025-09-13 04:57:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f84d5a80-013c-3315-8fbb-3fe898cc6841 | -9.99759 | -51.7333 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 622b2dfa-7e58-3af1-982a-db9ec6af2345 | -7.0189 | -44.88931 | 2025-09-13 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48c96da5-77f0-3aeb-8d19-b410aec96e0f | -8.47723 | -47.26435 | 2025-09-13 04:57:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9030be27-7f8d-3648-8548-20987e2a9c58 | -8.0996 | -50.18751 | 2025-09-13 04:57:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a943eadd-fc8d-3135-9a0b-fd742b1e4a9f | -9.05572 | -47.0362 | 2025-09-13 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 058e6ad9-6063-32d6-8484-908eb74d38d3 | -10.11609 | -45.50168 | 2025-09-13 04:57:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d82e0fd4-4309-3f91-a2f6-27cc4ebd0656 | -9.99697 | -51.73758 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 00dbe7f5-c08a-3cab-8b80-608018a254e0 | -9.78905 | -47.79234 | 2025-09-13 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5899f138-9239-3f0d-a031-4ceac4c9f07e | -7.01843 | -44.89286 | 2025-09-13 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46ec2807-3e3a-3675-8c8a-3cbd068e82cf | -9.50443 | -50.89129 | 2025-09-13 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0c924701-6df4-3406-a57b-789c80551537 | -10.0186 | -50.38465 | 2025-09-13 04:57:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dcb8948f-0aa2-354d-a455-42d6b76faf67 | -8.09634 | -50.18253 | 2025-09-13 04:57:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| da2676f0-38ca-3a60-83c1-8cad37ea24a5 | -7.6719 | -61.16839 | 2025-09-13 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 06912769-f2ee-367a-954a-05b05227c09a | -9.89223 | -51.86316 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 42b9c492-828e-3a67-b677-8b99821caf5e | -4.39895 | -47.8423 | 2025-09-13 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ee434da-76cd-3a8b-9d6b-e5d43bd6d6a2 | -6.57122 | -50.87086 | 2025-09-13 04:57:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 416193b5-3e11-39ba-88ec-2c3efc8afbec | -9.73162 | -48.35289 | 2025-09-13 04:57:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4a0f9ea9-1407-31c0-9269-139edbf2d921 | -9.49994 | -50.89544 | 2025-09-13 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8f37b58f-de79-35c5-be6b-e34f924c4213 | -8.9486 | -44.44548 | 2025-09-13 04:57:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e6b5813e-f333-3fb6-b106-5801215862af | -3.22145 | -47.13114 | 2025-09-13 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| f92a3a90-3252-3f18-b0c5-4f69a64612b6 | -5.64588 | -45.9457 | 2025-09-13 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6570302b-8e90-3670-bd8f-d82b846d2e5a | -9.71761 | -48.32098 | 2025-09-13 04:57:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c8f0ff9-58ed-3093-b847-87f4a23aaebb | -9.51714 | -54.62981 | 2025-09-13 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| ebff3535-61e2-3179-b7d1-729e71666d49 | -9.24475 | -51.24837 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 16f4a5c9-901e-3070-9e64-6e9ae42d9849 | -8.43331 | -55.6366 | 2025-09-13 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4be44403-5a01-39a7-809a-7749751e4a6a | -8.11008 | -50.1922 | 2025-09-13 04:57:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba93d371-4071-3852-9d56-c423fe0ba7f1 | -7.96868 | -55.3036 | 2025-09-13 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3db7ff3c-fdf2-31a4-bb8e-56012fd231b5 | -9.24104 | -51.2592 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| cfbb4ddb-f440-3326-8088-f5bf4271df18 | -9.79026 | -48.90177 | 2025-09-13 04:57:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fef1a26a-ac9a-3403-876f-865e62cc4f72 | -8.09777 | -50.17228 | 2025-09-13 04:57:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ea602e1-626a-3e77-b7e8-e1afe1ad0470 | -3.22655 | -47.12746 | 2025-09-13 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 32fbfe9f-67e0-3c67-9313-f2bcf4a41248 | -9.52759 | -54.62786 | 2025-09-13 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 7fe97baa-98b9-3afa-8922-81c256d08b21 | -9.52321 | -54.63432 | 2025-09-13 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f8b36af1-6a2f-3db3-84c6-47c05a2ec534 | -8.43386 | -55.63314 | 2025-09-13 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11f12666-41dd-3583-b0b8-4fb80b6d4bab | -4.96226 | -55.99296 | 2025-09-13 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 12b35087-c4d3-3ac0-8243-c7a575ed02b7 | -9.24779 | -51.26482 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0deb6a22-d7ae-3913-bed8-43c7925a6d58 | -6.1117 | -45.94657 | 2025-09-13 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4b69e846-6cc7-3ec2-982e-ed6c071a1cf0 | -6.31924 | -43.33285 | 2025-09-13 04:57:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ca935a3a-f84e-3602-8b6c-cb21639ad056 | -7.32348 | -46.58284 | 2025-09-13 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 298ecd76-ac7a-3e42-862e-be0b52ec180c | -7.90461 | -46.24896 | 2025-09-13 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 59e45309-da56-342f-8dae-50cad1518b6a | -8.47389 | -47.25324 | 2025-09-13 04:57:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 22e5a5d6-1025-3d33-b2f4-123e4349b84b | -9.72658 | -46.92257 | 2025-09-13 04:57:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4828796f-12d0-301b-9d00-04d4897065d1 | -2.98569 | -48.60043 | 2025-09-13 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2fb091f-9cea-3ea6-8243-4bfe59ba6e4f | -8.08109 | -54.74216 | 2025-09-13 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c5ca224f-1f06-35f8-92d8-8df3756360b1 | -3.63001 | -49.19923 | 2025-09-13 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9663f835-ae53-3805-b2e7-e5f304c96dca | -9.24022 | -51.21345 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9f2e0d76-8eb7-3a31-91ef-5ee95807cda3 | -9.24782 | -51.25339 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 1e6debed-db6b-3e16-b9d7-02970e9f193c | -6.17795 | -42.75647 | 2025-09-13 04:57:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 87451dba-93b3-34ac-ac05-666cab5e85a2 | -9.98184 | -51.71342 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a0e1099-14f0-3e05-a3ae-a3e864101d13 | -6.10201 | -45.94234 | 2025-09-13 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2735b0f6-2e9a-3bc8-9f40-0a950d2a3395 | -8.08736 | -42.56184 | 2025-09-13 04:57:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 82344680-3c8f-3f5e-9d0e-48fc45bda4f3 | -8.47795 | -47.25911 | 2025-09-13 04:57:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab9f8fdc-0b61-3116-a58f-21be0f0309bc | -7.55867 | -42.65735 | 2025-09-13 04:57:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4e434d19-3321-388d-93bb-6157325a8424 | -5.72487 | -43.18388 | 2025-09-13 04:57:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 980313a2-0085-3f5e-b6da-c9c48f5996ad | -9.23824 | -51.22686 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b6483af5-1c53-3846-bdc2-a9cfae005416 | -8.3618 | -52.51514 | 2025-09-13 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6aeb1f0d-71b7-3a1e-8d6f-8994e530414f | -8.10092 | -50.17827 | 2025-09-13 04:57:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bfbf38d4-79ee-3b18-9d16-322f3ba0fc6a | -9.66627 | -47.54546 | 2025-09-13 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3bd4ff93-d29f-3787-a3b0-bfd36feb598f | -7.39258 | -45.85598 | 2025-09-13 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 275f7d55-1adf-3611-9160-e6eb2cef11d1 | -10.36024 | -45.39545 | 2025-09-13 04:57:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c682831-79ea-37d7-a4da-28f5c49277d9 | -9.24607 | -51.25085 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 4599da15-0a63-3dc7-b011-7d4425553305 | -9.89947 | -51.86429 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 213d696c-6a5e-31c4-a19c-e30eeff78156 | -5.72421 | -43.18865 | 2025-09-13 04:57:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a536f9f-8653-39c3-8585-4e03e568025e | -8.46911 | -47.2526 | 2025-09-13 04:57:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 63f6456e-7ce4-3eab-853b-ec5002e74859 | -5.71574 | -46.45039 | 2025-09-13 04:57:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ffd2886b-0179-3859-b8a7-4cd54daaffb4 | -10.32805 | -48.81639 | 2025-09-13 04:57:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0c2bbe52-2876-3bfd-b0d2-cf219aaa6e87 | -5.32995 | -45.71838 | 2025-09-13 04:57:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef5e24a9-c1f3-3e65-8b82-8d1f8a3a9821 | -9.05647 | -47.03068 | 2025-09-13 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| d8b0ce3d-765a-3e0c-9d9f-83bf1907d3bb | -7.57279 | -42.64865 | 2025-09-13 04:57:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cd6526dd-97b3-376d-9e2c-2280eb619411 | -5.32691 | -55.88667 | 2025-09-13 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6d9ca512-1236-3fc3-b8de-bb1eb6802686 | -9.89583 | -51.86384 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ac351a18-388f-3b65-8a5a-ed01cbb511d1 | -9.88864 | -51.86247 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 727f2aed-12e6-39b0-a77e-b4ca55fde764 | -4.46301 | -55.06915 | 2025-09-13 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ab900d3-620c-3891-9ecc-df64c153befd | -10.23639 | -48.63437 | 2025-09-13 04:57:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a7393c3-4a43-3102-bc57-27a542a128f1 | -7.46152 | -44.44238 | 2025-09-13 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cb4f7481-5333-31f9-b29b-061d72066d6c | -9.95143 | -51.69133 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 754703e5-6edf-33a3-838f-d17570393704 | -6.21208 | -43.33833 | 2025-09-13 04:57:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c50fc28b-2f9c-36b0-98bf-ee41a00c44b1 | -6.11155 | -45.94217 | 2025-09-13 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1443ed6c-d386-3710-8129-27f76d880d57 | -9.79902 | -48.90245 | 2025-09-13 04:57:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6b7d309b-ae3a-3ef9-861b-9c4d5eda6981 | -9.96481 | -51.70216 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 253bd340-352e-3132-ba56-55eb7efd4808 | -9.96116 | -51.70159 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50870405-8272-3755-ad80-fc8c4dc3c33d | -9.78974 | -48.90546 | 2025-09-13 04:57:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 65c26dac-652a-364b-a2d0-1d843cf45e7a | -7.13899 | -52.34639 | 2025-09-13 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 442fc76b-9b1c-34c3-8fc9-8e6f87741ddd | -5.95405 | -47.22365 | 2025-09-13 04:57:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0c79b49b-a021-3c67-b4fe-a4cf78a6fec0 | -9.89521 | -51.86806 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README78.md)
