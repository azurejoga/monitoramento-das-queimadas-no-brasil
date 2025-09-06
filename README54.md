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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 532c26f3-448f-3329-b2b2-f4f153b5f49a | -6.18747 | -53.25852 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ad61daaf-26e3-3393-b931-089034fb4c75 | -6.18373 | -53.25788 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4d833ad-df2b-353f-94db-ee41c5ec75e5 | -6.66212 | -48.40161 | 2025-09-06 04:38:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2e2517fc-e31e-306f-aa47-d07ac4329095 | -3.68021 | -52.1902 | 2025-09-06 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fbb0af9c-ae18-3188-ba85-b98ca2b665b6 | -6.21119 | -43.57897 | 2025-09-06 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 422683b6-0873-3b89-ac5c-d42d4679bc04 | -5.8512 | -57.77275 | 2025-09-06 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c6fd274-96eb-3b38-acea-95397cc96106 | -7.72726 | -50.31165 | 2025-09-06 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ed646d95-2792-3f45-9583-72e99c90915b | -7.33711 | -48.49448 | 2025-09-06 04:38:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 04922935-db83-3d2f-9c6d-ea34abef2086 | -6.20116 | -45.04625 | 2025-09-06 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5a613358-eed1-3a1f-bc63-fcbe8fe2d5c8 | -7.15893 | -43.88549 | 2025-09-06 04:38:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1330ff43-71df-3262-b40e-d7d266f6f800 | -6.80962 | -45.65729 | 2025-09-06 04:38:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b9c2d3b0-1217-3423-a4c2-f95ab4af6678 | -7.36682 | -43.99802 | 2025-09-06 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f0fc8a27-b22a-3362-87bd-e08ccfe0abd9 | -4.45283 | -44.1417 | 2025-09-06 04:38:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1906f890-6551-3cd3-966e-8abb6d81c0a5 | -2.6759 | -52.17175 | 2025-09-06 04:38:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb184e4c-188a-3712-8069-3e60537a8a62 | -6.84587 | -43.04988 | 2025-09-06 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 317108a3-0515-38fc-80d7-5ceed85e1bb7 | -7.77067 | -51.08259 | 2025-09-06 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c5c0df65-a8a1-3fbd-9978-9b23c064369d | -5.97749 | -53.59322 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a0bea61a-48aa-3191-b90b-ea9bc4bce859 | -4.63637 | -42.52882 | 2025-09-06 04:38:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a98a4349-ee60-3fa2-beff-414ac44419b1 | -6.26617 | -53.43823 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f054658a-3118-310b-8074-8c2fec4833cf | -5.82696 | -46.35576 | 2025-09-06 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dea22ad5-abed-3adf-bd12-ee10225184d3 | -5.75717 | -45.53333 | 2025-09-06 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a988728-30dc-3b27-a0ea-c46fbf50795b | -8.36459 | -52.56235 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f32eae3a-7cad-347b-b923-0c668ee7ba70 | -5.96302 | -44.12926 | 2025-09-06 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4d532795-9827-383f-bfbe-0c4e11ea2a74 | -4.50146 | -42.8872 | 2025-09-06 04:38:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 70e9c853-fbf5-3f1d-8548-593fb8ce8c42 | -7.59217 | -46.20628 | 2025-09-06 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b22af9c-34a0-3425-9835-9912e59b4edc | -3.23863 | -50.80808 | 2025-09-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e169031-bce7-3959-ad4e-24ada2c6b7f2 | -6.0395 | -45.99591 | 2025-09-06 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c35b0c6-9826-3ed0-bb91-3a0606de8322 | -4.82495 | -42.74101 | 2025-09-06 04:38:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5b07fa2-c2e9-3ad9-bb5b-fac745c75071 | -6.26919 | -53.44344 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52434aaf-e09b-374e-96f5-2619db60ab2f | -5.8843 | -51.97316 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f49e305-0625-3176-aaea-535f9a4c5914 | -7.25737 | -41.88929 | 2025-09-06 04:38:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a17d8d1b-7d6e-356f-844d-6f806d61035a | -8.34836 | -52.55128 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9720cce9-42d6-300b-b670-0c0ac9990a20 | -3.16438 | -49.48106 | 2025-09-06 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a1361a1-92f4-3321-b6d6-f388b4fa31f4 | -5.0324 | -49.76147 | 2025-09-06 04:38:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9ea20e8-a1ec-383a-9a53-288e60c8a870 | -6.18447 | -53.25343 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0d5766e-814f-3e27-a5fb-b78b520ee79e | -8.02163 | -45.43665 | 2025-09-06 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ebf2cb82-cbd5-3b44-9dc8-faf67a14b80a | -7.96265 | -44.9438 | 2025-09-06 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c5cf8dc-1ffd-3c19-afa6-3111b2086e7b | -7.41649 | -44.95412 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0a705b8-ccde-37dd-967c-4a45feb5d078 | -8.51501 | -51.31621 | 2025-09-06 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e9e3540-9a7a-3f50-8259-aeb70d014bc3 | -6.55106 | -42.94971 | 2025-09-06 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 215bc9bc-70c6-31b0-a08d-5fab8b0374a8 | -8.10251 | -45.32641 | 2025-09-06 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 811cde53-f4bb-39c6-bb34-94136dcc5037 | -4.03544 | -42.52246 | 2025-09-06 04:38:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c72fcdd6-5856-3a6e-867b-8d5b6c1c980e | -6.15978 | -43.19448 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 16a74019-abbf-38c1-a401-a1de63ab4743 | -9.82669 | -46.53507 | 2025-09-06 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 48b55d7b-52ce-3f90-8327-fea201cf433e | -5.9038 | -57.73982 | 2025-09-06 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 72afce6f-88db-3d94-901b-427cc7f089ef | -8.88783 | -52.04788 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf2ef5b3-031c-31b2-be59-eecdc0ac430a | -6.24286 | -43.30358 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ccac6272-4963-3b45-aed5-2ade4bdffbb2 | -5.95893 | -44.73668 | 2025-09-06 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 266b6d5c-9fb9-35f0-ac89-be7599e55068 | -6.94007 | -50.96783 | 2025-09-06 04:38:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60706d10-562e-31a2-bc7a-f8cd1d0315ad | -3.69352 | -49.57132 | 2025-09-06 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9ac9efad-ebcd-376e-b2ea-343a5c6659f6 | -3.37361 | -52.79585 | 2025-09-06 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4898d297-7307-3826-90ab-09a33253b3ea | -3.38036 | -47.60948 | 2025-09-06 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c9d4d7a9-4769-319a-8b12-8c380d824358 | -5.55622 | -46.53907 | 2025-09-06 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 847c0f70-1478-31ee-aad2-d1bb5a660fb0 | -6.85883 | -45.58474 | 2025-09-06 04:38:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9608390-08f5-3dff-870d-a25f3238913a | -4.79345 | -47.2598 | 2025-09-06 04:38:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a3c6e8e1-814c-3b67-bef4-b4c14c64e055 | -5.83526 | -44.12495 | 2025-09-06 04:38:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bdeb463e-49a7-36ef-95a7-e18110bd6c6d | -7.79374 | -52.13162 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78a77cf9-365f-35d5-8ad7-4b59d2c9a34a | -7.05273 | -50.85739 | 2025-09-06 04:38:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05755b86-fced-3b13-85cf-65fd3bf4e1a9 | -6.16516 | -44.3105 | 2025-09-06 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5e95576b-d4d3-3ecf-8c57-9d615a0b6d1a | -6.48054 | -43.97653 | 2025-09-06 04:38:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2890606-28ca-313b-8ebf-2ad999d632b4 | -5.84909 | -45.30515 | 2025-09-06 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 58b65b3d-1211-3002-b346-a9000edcb392 | -6.87266 | -52.78342 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a85f6213-2045-336c-9bca-f2896ec16e28 | -5.85628 | -57.77356 | 2025-09-06 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae0c0833-7f3e-3993-a286-d6a0bda15255 | -8.51953 | -51.30954 | 2025-09-06 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c412264d-0c50-347f-a069-263a2e7a6eeb | -5.88844 | -51.96986 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18a97f65-0348-341d-b13a-374dbde216dc | -8.51896 | -51.31313 | 2025-09-06 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 81af1dd6-abd7-3c09-be61-2dfb61d99cb3 | -7.34667 | -44.32393 | 2025-09-06 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0ddf330-6393-3052-9501-5f8646c67fbc | -8.34724 | -52.51452 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 93313ac5-fa91-32e7-96be-a02c10a6c06b | -5.20867 | -43.69878 | 2025-09-06 04:38:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 846e7094-3d08-30a5-9a9d-8290d32f0b1b | -3.1616 | -49.47706 | 2025-09-06 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3bed31a3-e7f3-3de7-b6d8-6580157785ad | -8.08119 | -50.20029 | 2025-09-06 04:38:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ab1dfd3-6fcd-33b8-9038-f7360ce5b621 | -5.7269 | -43.90362 | 2025-09-06 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a922610a-d28f-36f9-ad5a-2c9cfc6b8134 | -6.75894 | -45.93565 | 2025-09-06 04:38:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab414d06-59b9-3735-ae16-015fb80792d4 | -6.22209 | -45.62746 | 2025-09-06 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39b51360-ef11-3738-93e7-3e0e7295b618 | -5.95149 | -53.78405 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8db6223e-ad9e-344b-8dfb-24ec027cf05b | -2.72872 | -48.3879 | 2025-09-06 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| df4d1532-e5c6-3069-b459-869f6c15f4f9 | -4.38513 | -48.06772 | 2025-09-06 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 798f8cf1-4efe-331f-b8b4-41c83352233a | -9.08747 | -47.01462 | 2025-09-06 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 470d20af-22e0-37ae-8ed0-4d30a44a24b1 | -7.4212 | -44.9496 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 95fdc0a1-96bd-35d7-a3a7-7bcd44e7401a | -5.89819 | -57.74221 | 2025-09-06 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 2bb71dcb-611d-320f-9aec-e13ef1b7fe80 | -6.60593 | -43.97484 | 2025-09-06 04:38:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f7c7af6-1cac-3978-8551-f7f34a94dff2 | -5.92989 | -43.01554 | 2025-09-06 04:38:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| b01f0f0c-fb16-32cc-addd-52f315802b86 | -7.6975 | -50.28512 | 2025-09-06 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 627aca18-1b71-3f30-b085-af7486ed2acb | -6.15691 | -45.02447 | 2025-09-06 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7e8522c-45af-33bd-ad3c-29d1ed227b96 | -8.43795 | -47.31913 | 2025-09-06 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a43f64fe-c601-3d88-b2cc-107038ca7e95 | -3.74937 | -44.37128 | 2025-09-06 04:38:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21ce6f6b-d37d-363b-80f6-6043890dbd8c | -7.46138 | -45.19346 | 2025-09-06 04:38:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 10dd26fb-a26e-3e4d-95fa-f03349de46e5 | -6.00873 | -46.70067 | 2025-09-06 04:38:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b1e7d55-ff11-30ad-b664-dc84b722564f | -8.64001 | -45.74762 | 2025-09-06 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df84c8e6-b7eb-35e4-91a0-962a51b3f7e6 | -4.27218 | -48.18238 | 2025-09-06 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| cf3b1a6d-f996-327d-9a28-9a299493a49a | -6.2722 | -53.44868 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 813c074f-57b5-3f60-81aa-3edabb2a9aa4 | -7.23135 | -43.86264 | 2025-09-06 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af5e603f-5db7-340c-a881-968bce96ba63 | -9.72332 | -48.32838 | 2025-09-06 04:38:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f171c8ca-0e51-3c99-b326-c1145ecdea2a | -6.1744 | -53.5015 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f17b5af-af80-31c4-96a3-de70b87fbabc | -6.15937 | -44.21021 | 2025-09-06 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1896eb85-3bcd-37cc-aaa5-b6e8ddead905 | -6.48527 | -43.97333 | 2025-09-06 04:38:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d348079b-d62b-316d-9af1-0c4e22e61d21 | -4.3818 | -48.0672 | 2025-09-06 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa8c4c18-3856-3b4f-b576-62055641b66b | -6.01619 | -43.69948 | 2025-09-06 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 65df0d76-0c53-3deb-b003-dff46c8c0b99 | -5.9554 | -53.80262 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5b2b0579-79aa-38e9-a1d5-c2ca6b50842e | -4.61114 | -41.54434 | 2025-09-06 04:38:00 | NOAA-20 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |


[Clique aqui para ver as próximas entradas](README55.md)
