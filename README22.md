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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1088bb58-d986-3006-99b3-b485b308075a | -10.05434 | -43.85132 | 2025-10-16 03:47:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| de07eeef-3152-3310-807b-ed842d294db4 | -12.02676 | -47.6595 | 2025-10-16 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b00976c0-f5bd-3c46-8956-7091ce1f50ba | -10.703 | -44.4306 | 2025-10-16 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| ded1be51-ad29-3ed9-8917-df02802faf94 | -5.48228 | -42.93606 | 2025-10-16 03:47:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| be7d26d6-5a84-30b4-bfa2-f31ac0719140 | -4.9128 | -41.55655 | 2025-10-16 03:47:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 1d022ef9-7521-387b-baa9-bfb923b8dbb0 | -10.65991 | -45.30936 | 2025-10-16 03:47:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 91283342-5353-376b-ac1b-be25428be043 | -9.72029 | -44.51662 | 2025-10-16 03:47:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a131893e-3c66-3cab-9fea-79e20441fd3b | -3.84904 | -41.58347 | 2025-10-16 03:47:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7e751e8f-0bf0-310e-9bc6-7e6ffd7f7e1c | -5.43774 | -42.90094 | 2025-10-16 03:47:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 7bce583c-e942-3861-b87f-1ab21f413c04 | -3.27275 | -45.84805 | 2025-10-16 03:47:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 19be1210-ddb7-3e6c-9bfb-c69dbd6af7cf | -6.22282 | -42.50828 | 2025-10-16 03:47:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 49fca259-c13b-319c-b8e3-e5989cf960cf | -6.06185 | -44.31382 | 2025-10-16 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 10616008-9e75-3d94-8448-186afdd07390 | -6.40133 | -43.48275 | 2025-10-16 03:47:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2ab88f1c-9d94-3158-9a2d-c67a3fd0d526 | -5.89805 | -42.82629 | 2025-10-16 03:47:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| a051e9b6-2f1a-3118-82c5-b609a50851f5 | -11.48799 | -44.10664 | 2025-10-16 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| edb0f35e-a650-3594-83d8-679c5a494a10 | -6.15225 | -41.78642 | 2025-10-16 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e9aefb94-1318-350c-bcbf-e1793ff8bb57 | -6.22056 | -43.35433 | 2025-10-16 03:47:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01ecca07-10ad-355b-9795-c7369672157a | -5.4344 | -44.23349 | 2025-10-16 03:47:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c74a4d8a-c12b-3b29-a44f-a0aafdebcca1 | -10.52313 | -43.37244 | 2025-10-16 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 62a53ecd-3f29-33a0-9b92-aabe853bf20a | -6.98812 | -38.44309 | 2025-10-16 03:47:00 | NOAA-20 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| de634233-17e4-36ba-8a60-62e76e8017f9 | -9.59388 | -43.0727 | 2025-10-16 03:47:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| eb0333bc-5c64-32ca-9b33-031a9c7ba0d1 | -9.3682 | -46.95207 | 2025-10-16 03:47:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 01633c6a-9aeb-38f8-9bf7-2124e52858f7 | -9.25849 | -44.36074 | 2025-10-16 03:47:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3e83751c-0dd8-334d-9aa9-ebae95d114be | -5.25187 | -40.97852 | 2025-10-16 03:47:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 68b55d83-ce27-3c3e-b08b-6fce46a7a8e6 | -4.81015 | -43.20927 | 2025-10-16 03:47:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a89b459e-b870-3e5a-940a-96a9b7614d83 | -5.83376 | -42.34757 | 2025-10-16 03:47:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ca324d6e-dcd1-3e81-97a9-a630e4bcc44e | -9.08662 | -47.95016 | 2025-10-16 03:47:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| efeae5b4-2bf3-308e-a22a-f71383279724 | -3.43444 | -39.6489 | 2025-10-16 03:47:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 0344ca00-3669-3a89-b3f5-a9b154893ddd | -3.83545 | -44.54919 | 2025-10-16 03:47:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3f44c180-f2a9-3d70-ba89-8d2dd877b23e | -6.06282 | -44.30833 | 2025-10-16 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6f3d749b-123a-35d5-8f3d-7415b1ffd206 | -10.66152 | -45.32288 | 2025-10-16 03:47:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3d8fc3ed-28b0-31b1-abb1-b18ace36254e | -5.89303 | -42.8313 | 2025-10-16 03:47:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| db830bc3-4c54-3692-ae57-94e7c5d85e6b | -9.36604 | -46.96346 | 2025-10-16 03:47:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9103f8b-84cd-3ac7-8fd8-aadf076aaa7b | -5.88099 | -43.85611 | 2025-10-16 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a9016bfc-0053-34c9-ac91-b9325f752007 | -3.68196 | -47.63681 | 2025-10-16 03:47:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0a234a67-0e47-3de3-af9b-64a886cf7f72 | -4.65571 | -44.10007 | 2025-10-16 03:47:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a6582bac-4652-3776-925e-c4d80d9745a9 | -6.43095 | -41.88963 | 2025-10-16 03:47:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 18076559-c355-3f50-8378-7822f15dd50d | -5.91336 | -42.84275 | 2025-10-16 03:47:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6e200147-b1c4-3f0e-ae29-1cb9eaae42fb | -10.99141 | -49.54784 | 2025-10-16 03:47:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f728f3d-f743-30a6-96b7-0d28a4cce7f0 | -11.45004 | -44.16671 | 2025-10-16 03:47:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4813e96-c1db-33a5-ada4-834f9b0d1dd1 | -5.87248 | -42.81859 | 2025-10-16 03:47:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| a1c86438-9ec5-310a-88d8-66c24f0608e6 | -9.16168 | -46.87015 | 2025-10-16 03:47:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 812760f2-d82d-311b-a325-ee76c6c01838 | -5.42519 | -40.97815 | 2025-10-16 03:47:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c061deb4-ab4a-3271-9ce3-879e03081040 | -3.84421 | -41.58664 | 2025-10-16 03:47:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 87220b9e-3807-3462-9fa3-99c2f97d850b | -10.61708 | -37.72618 | 2025-10-16 03:47:00 | NOAA-20 | PINHÃO | SERGIPE | Brasil | 2805208 | 28 | 33 | nan | nan | nan | Caatinga | 0.5 |
| dc63eac0-f8e8-3c6b-95e6-cb25bb396e28 | -4.39057 | -43.40258 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e811575e-6778-3dbe-b42c-738bdbeaa076 | -6.04505 | -44.24802 | 2025-10-16 03:47:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c20f9e94-b157-3e9c-b61e-a42d97da6410 | -6.13075 | -41.76395 | 2025-10-16 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c9ee78aa-e151-3619-b53b-e746536eb60a | -4.66062 | -44.10089 | 2025-10-16 03:47:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 27cee173-6557-3c61-b530-5b8c089454d2 | -4.65878 | -44.11181 | 2025-10-16 03:47:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dfa392a8-2087-3011-9067-9d984da2cecd | -6.46765 | -41.84631 | 2025-10-16 03:47:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ac9d1611-a5c5-30ed-8fbb-4ad0164e5552 | -9.71372 | -44.50028 | 2025-10-16 03:47:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a243afd-d025-3116-9887-56e529cff4f9 | -10.1461 | -44.54123 | 2025-10-16 03:47:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d148ecb7-fe09-3b69-abb4-5c8ca0fc526d | -11.58438 | -44.07487 | 2025-10-16 03:47:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0917fde-414f-3c60-9034-d9ed0954345d | -6.09867 | -40.88948 | 2025-10-16 03:47:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 72b254df-83f8-318d-b999-74d7e3aec88d | -6.56797 | -42.97732 | 2025-10-16 03:47:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e6ad18a-7910-3a47-98bd-04d3da365973 | -6.37312 | -41.48906 | 2025-10-16 03:47:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e7e1e337-33ce-3ea9-9850-925640457f95 | -6.37254 | -41.49252 | 2025-10-16 03:47:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d18120df-41ff-36d8-a6ab-4ecec91170c5 | -6.56943 | -42.96873 | 2025-10-16 03:47:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 00bbc334-feb0-3980-95d0-090136c840a3 | -6.33952 | -43.18116 | 2025-10-16 03:47:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 532d7903-5178-3c70-b09c-e25590756f4c | -10.62617 | -45.24895 | 2025-10-16 03:47:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c22b1934-7b37-3e4b-896f-88f677590912 | -10.72111 | -47.58441 | 2025-10-16 03:47:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 364b6ff3-5371-3c6f-b0cb-b7c1ba3d21ce | -4.5039 | -45.40211 | 2025-10-16 03:47:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb24e749-cfef-3ea4-a374-a4c39cf13e2b | -3.00924 | -45.39614 | 2025-10-16 03:47:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a36b6996-ce6a-3071-a23f-c60f0452d970 | -10.28144 | -44.02212 | 2025-10-16 03:47:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa88543e-2ea6-3096-b036-059d93db7cf4 | -5.68195 | -45.10608 | 2025-10-16 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 4b985e36-ab95-3ff6-b9b3-0180802e2ff8 | -4.38147 | -43.38887 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 9f119c3d-fab8-304d-8520-92aed92f3223 | -10.71276 | -44.53571 | 2025-10-16 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 847d40f8-5199-3247-b890-59adb4fc9560 | -5.76535 | -47.91467 | 2025-10-16 03:47:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a075ad1c-45cc-31fe-896f-5caca52a73b4 | -5.41735 | -40.97672 | 2025-10-16 03:47:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9d3459bb-28b5-3870-9124-dca5687ea1e5 | -6.15164 | -41.79008 | 2025-10-16 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e5e786e3-5f2a-351f-9af2-eb34c4473696 | -10.85218 | -43.64422 | 2025-10-16 03:47:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92e25db1-9c29-3201-ae6a-bb64c9342e4e | -6.22417 | -42.50026 | 2025-10-16 03:47:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 538accd8-92d5-38db-9575-7de987104db7 | -6.2182 | -35.65339 | 2025-10-16 03:47:00 | NOAA-20 | JANUÁRIO CICCO | RIO GRANDE DO NORTE | Brasil | 2405306 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6cc221e7-19d3-3750-83a1-e6bbfcd46724 | -6.04755 | -41.93089 | 2025-10-16 03:47:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c1d3808f-9aa9-3872-b996-28a94ca9dec0 | -10.12661 | -44.59069 | 2025-10-16 03:47:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e1329edf-bc3e-338f-95bd-07f95caee1b3 | -6.39772 | -41.48948 | 2025-10-16 03:47:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9d943b55-ea35-3bce-ba57-745750de6473 | -10.66247 | -45.31782 | 2025-10-16 03:47:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4b45044a-50f0-3e68-b3eb-418ea7e2efc5 | -10.80687 | -43.9432 | 2025-10-16 03:47:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ba103b0-3a93-3e76-9897-d850987140b4 | -3.84057 | -44.55014 | 2025-10-16 03:47:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 65850ecf-fd61-3f16-b3d0-6e9212eb0f5e | -6.06746 | -44.54071 | 2025-10-16 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 643c32d2-6048-3375-8639-8046aafb2bbd | -3.287 | -40.89655 | 2025-10-16 03:47:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 538795aa-696a-3464-98df-6edaeab8d076 | -5.09843 | -42.64341 | 2025-10-16 03:47:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d3bf79d-53a8-32b2-ae84-9da573b88542 | -4.8842 | -46.71239 | 2025-10-16 03:47:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e852891e-b767-384e-ac6a-47f6adcaff45 | -4.65265 | -44.08828 | 2025-10-16 03:47:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5da69b33-5e24-313b-8032-d3bc3e7b5435 | -12.66561 | -44.13079 | 2025-10-16 03:47:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ac0b899-b650-3dae-9fad-77f46a2ca0bb | -5.57264 | -41.32878 | 2025-10-16 03:47:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bce15a7f-2c39-3ffe-a933-27f30a2e50f5 | -6.20108 | -42.61087 | 2025-10-16 03:47:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 7dcc4c8b-e335-3e5c-8376-9d18fe72e9ad | -6.38285 | -41.48009 | 2025-10-16 03:47:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 6fa8cf07-9f03-3e07-b52b-a8ecb3792430 | -4.37899 | -43.40398 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| dc12312b-2232-3d21-b2a4-7339d1e86428 | -6.15751 | -40.90142 | 2025-10-16 03:47:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 8cf2aaa7-f069-364e-a310-d1284f761434 | -4.65757 | -44.08899 | 2025-10-16 03:47:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f342555-b3fb-35f5-ab43-68ed17db4bb6 | -5.72027 | -44.52153 | 2025-10-16 03:47:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de5b344c-d2fc-3dd7-a813-1d51c612f59a | -12.66999 | -43.42959 | 2025-10-16 03:47:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3223acc5-e85f-34f0-ab1c-8b6b228d00fb | -6.4505 | -43.38538 | 2025-10-16 03:47:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 40ff1408-f73e-32dc-a241-6cb519d9f6eb | -6.05874 | -41.89026 | 2025-10-16 03:47:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e26b3c9a-2a46-3d74-8dab-e12af0f8fea3 | -11.45285 | -44.17625 | 2025-10-16 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd67c2ab-f183-3f39-b609-f91d5ad2348c | -6.04885 | -41.92331 | 2025-10-16 03:47:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3e4e996c-4562-3806-890e-63130ca4723f | -12.6388 | -44.22956 | 2025-10-16 03:47:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 79383020-ff62-340c-8491-5d72ed44bc2d | -11.42768 | -44.14001 | 2025-10-16 03:47:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README23.md)
