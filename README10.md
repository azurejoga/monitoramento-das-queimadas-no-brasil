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
| 618f331d-d43b-3208-aca0-4c80aa29512d | -13.29298 | -40.31691 | 2025-08-07 04:02:00 | NOAA-20 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 192e5116-61b8-33e6-8131-f6cc919917b8 | -8.25303 | -45.08184 | 2025-08-07 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c5e2ee05-44d9-3103-93b5-5e26c4f04212 | -10.7005 | -48.87057 | 2025-08-07 04:02:00 | NOAA-20 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f2818441-e36a-3257-8d76-f783554383f3 | -8.25779 | -45.07747 | 2025-08-07 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48fad13a-6483-386c-a9a6-36751ec2f80d | -16.2168 | -40.13904 | 2025-08-07 04:02:00 | NOAA-20 | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4d1e2fac-00cf-311c-8eb2-0bb0f6f7bdce | -10.43814 | -44.39501 | 2025-08-07 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d1353890-f835-3c41-b417-e7954d61062d | -10.43449 | -44.39439 | 2025-08-07 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 69e9767f-db2d-3a78-b951-6bd5ed7ab8de | -10.43303 | -44.38073 | 2025-08-07 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d9254f29-8b6a-306e-b0ba-aa20f09022d1 | -12.70297 | -46.38526 | 2025-08-07 04:02:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0d4c876d-a22c-3c0b-8e2f-6bd0b22beffd | -6.91374 | -52.84741 | 2025-08-07 04:02:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6ec49f64-26fb-3837-b1e8-69ae4cb13696 | -10.43084 | -44.39377 | 2025-08-07 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cfa0e6a2-35b7-3bc3-8854-68e835039f9d | -10.4411 | -44.35503 | 2025-08-07 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46d9db1d-fdd9-3c7a-ab9e-c81a25f75c10 | -10.42207 | -44.40124 | 2025-08-07 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cde49c6a-b188-3fe5-b7bb-3af4118c58ef | -10.64572 | -44.7486 | 2025-08-07 04:02:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7b7f4a99-0b8d-3cab-aa55-e7a23a00d23c | -14.52617 | -45.59913 | 2025-08-07 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 415f377e-7220-3637-935a-ab5e28d5eabf | -14.52249 | -45.59845 | 2025-08-07 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07c1beef-5038-341e-a36f-7c82402679bf | -11.75085 | -48.19125 | 2025-08-07 04:02:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 604c0096-faa0-36be-8849-b0ae901a66cd | -12.53268 | -47.1511 | 2025-08-07 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf0c29e2-de8d-32a4-bb89-e3c5940c4245 | -12.54459 | -47.15667 | 2025-08-07 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 72101d35-d3f7-3b83-bb44-b2ab50beff47 | -12.71089 | -46.38675 | 2025-08-07 04:02:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0193fd1f-cc9c-3f87-aba6-e3d6469496b4 | -10.41989 | -44.3919 | 2025-08-07 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bac08444-16e2-37fc-b771-ecc7ad0b64b5 | -10.47756 | -44.38348 | 2025-08-07 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 84172cb9-cbb0-3efd-8f8c-8d564b2ed457 | -10.70633 | -48.86605 | 2025-08-07 04:02:00 | NOAA-20 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fbc939e0-fb3c-33b0-bbaf-c66da60693c0 | -15.90854 | -44.30478 | 2025-08-07 04:02:00 | NOAA-20 | LONTRA | MINAS GERAIS | Brasil | 3138658 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6679ad10-2bae-34db-8cd7-cec7f59c0954 | -7.9089 | -45.53611 | 2025-08-07 04:02:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bbc32fa8-8d6c-3333-9b01-b36e377c768f | -11.17846 | -51.44272 | 2025-08-07 04:02:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3ef0b98a-1942-3794-a480-672bdad9fec9 | -11.78428 | -47.53067 | 2025-08-07 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 87600ca4-f41d-3ae4-b788-4766e1fcde8f | -12.79284 | -45.44439 | 2025-08-07 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 129106b8-81d5-36ab-b570-6d2075396ac8 | -10.62792 | -44.74091 | 2025-08-07 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 50cc801f-00f1-3d89-8104-1824d6457644 | -10.43377 | -44.37632 | 2025-08-07 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 18e6bd86-2d40-330f-a228-8ff9c0b08667 | -12.41295 | -47.78263 | 2025-08-07 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bdb04b0d-15a2-3ca7-81e5-f8423a3ae339 | -6.91862 | -52.843 | 2025-08-07 04:02:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fd0d8b39-d974-3541-a226-f801e3bc3e6f | -11.7427 | -45.02071 | 2025-08-07 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31ab7dc4-62e6-35c7-bd9c-011cc4bd6a1d | -14.81732 | -48.40824 | 2025-08-07 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d5c9c0d-ac3f-339a-bde5-53869e05b8a1 | -8.11077 | -45.50029 | 2025-08-07 04:02:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9496aad-3816-357b-8372-a12435956827 | -10.43521 | -44.39006 | 2025-08-07 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 67ec9619-70d7-3020-98e2-39f9ff7e4a39 | -10.63384 | -44.75119 | 2025-08-07 04:02:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ab069d7e-181e-3447-b32d-f1498bdf0e2b | -11.40474 | -41.7108 | 2025-08-07 04:02:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a90acb50-5793-37c7-aaaf-c362577a4b14 | -12.37679 | -47.04716 | 2025-08-07 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56cec60a-e13f-3ae1-a0b4-be85a8236a89 | -15.7466 | -43.38967 | 2025-08-07 04:02:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| c62b210a-35b3-33f4-9069-d4fba7667365 | -11.17621 | -51.44223 | 2025-08-07 04:02:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7689cdd6-d03b-36b7-9e32-0a2e3f1662d2 | -10.42645 | -44.39751 | 2025-08-07 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 22c7a9fa-2b75-34f7-8407-b4e758cb3e25 | -12.79579 | -45.44967 | 2025-08-07 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7a0cc72-9174-30d2-8250-de52ae47e85c | -11.17768 | -51.44666 | 2025-08-07 04:02:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5408d15f-0f8e-37c2-9ac5-6214b60b2b60 | -12.72763 | -46.38449 | 2025-08-07 04:02:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1852fa70-e088-3fb7-b58b-330475cf12e0 | -9.64542 | -43.84356 | 2025-08-07 04:02:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7c68c83e-c51b-342b-8103-b5cf94858410 | -11.78007 | -47.52216 | 2025-08-07 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 57a11e22-0a99-3ccd-9f7e-4f63194ed322 | -11.75423 | -44.9531 | 2025-08-07 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e951e4e6-b9b4-3a1b-aa89-4c263b4449c8 | -10.4301 | -44.39813 | 2025-08-07 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75e7a6bf-1dd0-3014-aa6c-108be6538921 | -10.64276 | -44.74346 | 2025-08-07 04:02:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 765c3463-d57a-3615-8aa7-81855222be82 | -11.77542 | -47.3979 | 2025-08-07 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a90604b8-4928-3aa7-986a-90e4902e710c | -12.33014 | -46.05251 | 2025-08-07 04:02:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c797cd1d-05f7-3418-9bc2-5391203395d6 | -11.17203 | -51.44549 | 2025-08-07 04:02:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c792bfc-9669-3295-98f7-81fae9b2f7a4 | -8.5184 | -43.29422 | 2025-08-07 04:02:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 78fe99f6-e8c4-32aa-b07a-c61b13e9359f | -10.4812 | -44.38414 | 2025-08-07 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| e552e6e6-48c2-3d34-956f-74952b3c3531 | -8.88914 | -44.78704 | 2025-08-07 04:02:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 670fa0c0-5a81-31cd-8abd-503e4a91b67b | -15.93321 | -43.51633 | 2025-08-07 04:02:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4c16ea53-c125-30d9-a8bb-cbe15fe2b600 | -12.34365 | -45.76991 | 2025-08-07 04:02:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 66678f72-0689-3581-9ba7-0cf023d4d9ea | -13.00739 | -44.88572 | 2025-08-07 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2866d288-a39a-37fc-a7b1-258d278712e4 | -10.6368 | -44.75632 | 2025-08-07 04:02:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 60c70da4-77f5-3d6f-ab8b-776f5c693833 | -9.64899 | -43.84422 | 2025-08-07 04:02:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5f5fead4-aa9c-3347-bfe4-11b18c784eb1 | -11.76788 | -47.51528 | 2025-08-07 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa774baa-7902-300d-b488-721fcdc34afe | -11.77175 | -47.54399 | 2025-08-07 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8cc4f907-2e90-3ac0-ac52-107c3b4b7078 | -10.43302 | -44.40309 | 2025-08-07 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4452c49d-1a28-3ab6-8cab-ffec457cea91 | -7.91233 | -45.54034 | 2025-08-07 04:02:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| edb7eec1-9c89-3554-b835-76be1f5d0661 | -12.34878 | -46.06109 | 2025-08-07 04:02:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c611c152-f968-399f-a329-85720bcde7f3 | -14.52449 | -45.60056 | 2025-08-07 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a889bd2-89c5-361c-9019-9c2686462a27 | -11.75168 | -48.18666 | 2025-08-07 04:02:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| b2793d8c-e086-3749-b3a4-2667bb99719f | -9.72988 | -48.30371 | 2025-08-07 04:02:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c8169985-2eef-3f64-b88e-1e9c4693575c | -6.94523 | -51.63387 | 2025-08-07 04:02:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b7bbb57-4615-3ad4-9b57-82b7060f84a6 | -12.71879 | -46.38827 | 2025-08-07 04:02:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| adffbe27-2ae5-3b9c-9dd9-e528cab21a2b | -14.14472 | -44.7392 | 2025-08-07 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f2778c4-00ae-3b44-a9e7-e992af60ee2c | -9.55848 | -40.34447 | 2025-08-07 04:02:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fb1801d4-2a83-39ef-a7bf-573d5dd0c8e3 | -14.52541 | -45.60362 | 2025-08-07 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1da55c85-3791-33d7-8cb2-88658c7cd770 | -11.77929 | -47.5266 | 2025-08-07 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fc323dc1-d669-35ce-84f9-c89ea0a21dcd | -12.99944 | -44.8886 | 2025-08-07 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 985c9ae5-daf7-3775-8205-50132231db5f | -10.43671 | -44.35886 | 2025-08-07 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb50dd67-50a6-3d5a-983c-87e70a674e53 | -9.65256 | -43.84489 | 2025-08-07 04:02:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8839cfef-111f-37f1-b2b2-87531e2d8eaf | -11.76742 | -47.54313 | 2025-08-07 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d6825aa-3724-3052-acec-a00870561abb | -10.43157 | -44.38942 | 2025-08-07 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 75103f42-3927-3ffd-9293-a31acb860f1a | -9.08242 | -45.05995 | 2025-08-07 04:02:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4a13e917-7cf4-3499-987f-650b22a76c14 | -10.62642 | -44.7499 | 2025-08-07 04:02:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6110e955-a965-390d-ac42-57d50aadc849 | -11.18899 | -51.44894 | 2025-08-07 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 72dbc4c5-3bd7-30a8-a596-afe0df2b19a9 | -12.55066 | -44.74817 | 2025-08-07 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b85cd9a-4395-3341-a640-008bf3b3590a | -10.47381 | -44.33843 | 2025-08-07 04:02:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5684a819-b541-3b1f-9654-55f360b47447 | -8.25388 | -45.07683 | 2025-08-07 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 543724b6-619a-3cb8-b18f-924e30a5d1a4 | -14.52739 | -45.60571 | 2025-08-07 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85bf36ae-01c8-3163-8006-fe0ecdcbd08c | -10.44033 | -44.4043 | 2025-08-07 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a03d40b9-d800-31be-8d06-acb4f4f59aa0 | -9.46593 | -46.29665 | 2025-08-07 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fb470d87-4d3f-31b2-b5cc-3124c9120ed8 | -12.54811 | -47.16108 | 2025-08-07 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0e53fe65-5200-3033-856e-86cae73a94a0 | -15.7472 | -43.38601 | 2025-08-07 04:02:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6252a88b-4e7c-3a6c-85f0-db1b5a8bac07 | -11.7863 | -47.53756 | 2025-08-07 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3a582069-acfa-3e39-bd04-9f9c63ebd8a1 | -11.73976 | -45.01556 | 2025-08-07 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11136ece-e87f-312a-9e43-486b64cc4730 | -10.64201 | -44.74796 | 2025-08-07 04:02:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d31f91e0-c913-3342-acad-c78038a6cedc | -12.34536 | -45.76018 | 2025-08-07 04:02:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85a24c6d-8b48-3c23-8523-2c542022f898 | -10.6383 | -44.74733 | 2025-08-07 04:02:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 23479208-50c3-3d4a-b9eb-d7f54dd1f0e1 | -12.5149 | -47.14882 | 2025-08-07 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b375f38f-cf5f-3335-868d-b33778ef852e | -10.44549 | -44.35119 | 2025-08-07 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| badcc49d-e61f-3cd4-abaa-d6e98eeb0195 | -12.5474 | -47.16499 | 2025-08-07 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ae874326-eee8-34b1-8105-408521d0e2ed | -12.46195 | -43.56235 | 2025-08-07 04:02:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README11.md)
