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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6738b73e-ad89-3b15-b6e8-a89bb46eaf70 | -3.38453 | -47.48099 | 2025-07-17 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 38f9d0c5-2f61-34a8-b3c0-44eebac4a25b | -9.35173 | -38.30061 | 2025-07-17 03:53:00 | NOAA-20 | GLÓRIA | BAHIA | Brasil | 2911402 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a234cddb-4def-3537-a50e-5cbb0147a2d9 | -7.19071 | -43.11619 | 2025-07-17 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 64d65b70-1649-348a-a48f-e7ef5f40d24d | -3.58584 | -47.52885 | 2025-07-17 03:53:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 402c28f5-0124-3170-9544-dca8313511ca | -4.91005 | -37.34198 | 2025-07-17 03:53:00 | NOAA-20 | TIBAU | RIO GRANDE DO NORTE | Brasil | 2411056 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| feeff62b-6d91-327a-8b67-a0b94385534b | -6.19338 | -39.41582 | 2025-07-17 03:53:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 518e837b-5fc5-39aa-9898-4dd9d969a221 | -6.99846 | -44.22482 | 2025-07-17 03:53:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6742deb2-dc26-3a91-bacc-8c8a9b63b52f | -3.04494 | -49.4349 | 2025-07-17 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37069573-e41a-367c-9a7f-40f36a4d970a | -6.3484 | -44.60936 | 2025-07-17 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 61f82f17-2fc4-300c-8780-fc41633097c5 | -3.80314 | -43.2225 | 2025-07-17 03:53:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d264b407-802b-35ae-896b-04412ab996fb | -4.30293 | -48.10107 | 2025-07-17 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 0b9281fb-383f-3a78-a069-5b929c6eee29 | -7.23033 | -43.50157 | 2025-07-17 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 525d3522-e0b7-3f3b-a610-d4bee8d98886 | -7.46593 | -44.71437 | 2025-07-17 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1aab9899-e9bd-3e0e-b0b6-b326299d27f0 | -3.37962 | -47.47639 | 2025-07-17 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d4f85e8-a328-3778-88b1-2261c7267586 | -8.5404 | -47.85181 | 2025-07-17 03:53:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d300de57-c4d1-3d84-b3b3-639a9e4d2a00 | -7.21962 | -35.78054 | 2025-07-17 03:53:00 | NOAA-20 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 3bcbae43-5e8c-344a-92f3-d7a153a4a5ec | -7.89485 | -44.49473 | 2025-07-17 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b7a1c48-b53d-31a7-91c1-6ef757e67c09 | -3.66895 | -48.31754 | 2025-07-17 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba1f4c80-eeab-31fd-a9d5-c3ccedd2d28d | -8.21656 | -44.91968 | 2025-07-17 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 46857f56-a971-3a65-9f61-fb4474c0b923 | -8.085 | -47.61779 | 2025-07-17 03:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 20c8753f-4926-3271-b01d-f6d236785a56 | -9.58501 | -40.34871 | 2025-07-17 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 24749346-8d32-396d-9462-087ee76c6ffd | -7.14411 | -43.00666 | 2025-07-17 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e26c4b04-6bdd-3b8b-96ca-45ef414f1b10 | -3.378 | -47.48292 | 2025-07-17 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 61e3f75d-6ada-39d2-9778-ce8bdd0feeaa | -6.72853 | -44.33138 | 2025-07-17 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b1ebdde6-d41b-3e49-9b44-e1615a4a297a | -4.59647 | -43.321 | 2025-07-17 03:53:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c0e585f3-d8c4-3db0-a425-1a28222faa1b | -8.88105 | -44.79206 | 2025-07-17 03:53:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3d25b65c-fcaa-358e-811d-583e6adf774f | -7.19458 | -43.11686 | 2025-07-17 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| c3bc0597-7bde-37fb-9e25-54434a33b322 | -9.10803 | -44.29924 | 2025-07-17 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 67437bfe-3a87-3387-a20b-0a13fe497e6f | -7.05378 | -43.52718 | 2025-07-17 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce8fc410-6ab0-3cfd-97f2-698f16f072ea | -6.70808 | -44.32384 | 2025-07-17 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 07b441ea-9aa6-3658-8761-f429d3687f58 | -9.60284 | -40.55785 | 2025-07-17 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 54a187cb-1f5a-396f-89f4-2316b2b8e0a1 | -6.4332 | -45.31472 | 2025-07-17 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cb473987-f312-3c0b-879b-51bf6a1b8029 | -7.17912 | -43.59863 | 2025-07-17 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8300d8b3-3bae-3e3c-8dfe-d8220f6e424e | -5.53283 | -43.88272 | 2025-07-17 03:53:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 59c17697-793d-3ff9-881d-8016282d9967 | -3.03112 | -47.86141 | 2025-07-17 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5dfdacd7-5a79-33ee-a17d-bb52e517f2f8 | -3.39746 | -47.50614 | 2025-07-17 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f844b4f1-5444-3b9c-92c8-12937512b593 | -7.20741 | -43.15937 | 2025-07-17 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f7d6f7e5-3ba0-34e4-ba3d-db354b11cc39 | -8.10213 | -43.14818 | 2025-07-17 03:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| f9c48a0e-6712-3f37-a19f-f6554df13751 | -6.7123 | -44.32455 | 2025-07-17 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 1e8a3a0a-9e09-3099-ab87-b4b15106aaac | -7.30667 | -44.30233 | 2025-07-17 03:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 34edd269-bd2c-3fbe-8039-e7095f78e500 | -5.49687 | -43.67908 | 2025-07-17 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c6530b2-f9e5-36d5-b744-5fb9936b3ce7 | -8.11058 | -43.1447 | 2025-07-17 03:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| ff9ac3e4-599a-3bcc-a0a0-83642586086d | -6.5712 | -36.55701 | 2025-07-17 03:53:00 | NOAA-20 | CARNAÚBA DOS DANTAS | RIO GRANDE DO NORTE | Brasil | 2402402 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0b9777a5-b7c7-3650-a7a0-dcc3c45b631b | -7.09584 | -41.39836 | 2025-07-17 03:53:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| bfe34d06-1a4e-3d53-8b8a-ddd92bddee3c | -8.46652 | -46.00767 | 2025-07-17 03:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7e621d7f-18a2-30bd-acef-aec056ccbc08 | -7.18684 | -43.11551 | 2025-07-17 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| a09d4a95-3515-3590-bfd3-b4e165a6e8fb | -7.6196 | -44.32667 | 2025-07-17 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ca62fd5-057a-38d3-88f0-723bdc0b6256 | -3.39757 | -47.50144 | 2025-07-17 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ae11e2ec-e7f2-3e33-ac94-9d9ee546874a | -9.38178 | -40.62275 | 2025-07-17 03:53:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d7a2884c-f1b8-3de4-9d5f-a6dca48498c6 | -7.587 | -46.33801 | 2025-07-17 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fdec2065-ed42-3a21-ae64-dd6f043ddfe4 | -8.09367 | -43.15165 | 2025-07-17 03:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6a43d188-5dcf-3ae1-a26c-12a9e0ec0e1b | -3.38225 | -47.49127 | 2025-07-17 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| b31ea80a-652e-3a88-900e-9261623af0af | -7.1797 | -43.59513 | 2025-07-17 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3682001e-b49d-38ca-b4d9-0afe568f6cf6 | -8.88037 | -44.79601 | 2025-07-17 03:53:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 7e56c26c-ce85-3603-879a-60a3b928fe79 | -7.09773 | -44.3807 | 2025-07-17 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5b6746b-6648-3e6c-a52c-d8f1ff7f4855 | -4.59298 | -43.3167 | 2025-07-17 03:53:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0cebbbcc-f6cb-3c84-830a-8c86ef56270b | -5.66906 | -43.71906 | 2025-07-17 03:53:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 30762247-731e-3c65-bb6b-f8b71863c737 | -2.65775 | -47.39729 | 2025-07-17 03:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3599d844-eb0a-312a-b46a-ccda209956fe | -4.29727 | -48.10006 | 2025-07-17 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 5831a582-3caa-38d3-9b0e-0a7842d7718f | -4.80927 | -43.21855 | 2025-07-17 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b16376cc-a84a-350c-9b0d-54cb1e1a6019 | -6.34272 | -44.75153 | 2025-07-17 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85c63dce-39b1-3d37-b0e3-1bad23bd0222 | -7.13221 | -43.29794 | 2025-07-17 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fbe3d8d4-c369-3a79-a70a-ad9cfc0dafd8 | -7.20682 | -45.33268 | 2025-07-17 03:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ce9f1bb6-32a5-383a-8a9d-83d134b9e759 | -6.14072 | -43.96153 | 2025-07-17 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7933b5c-20a4-3083-8b44-5ddb103188ce | -5.04139 | -38.53721 | 2025-07-17 03:53:00 | NOAA-20 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ff0b088e-9144-3593-b528-dd8f6b7e801c | -5.78812 | -45.09485 | 2025-07-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fbd584aa-60aa-3388-ba6e-9737d223aa50 | -4.80347 | -43.22858 | 2025-07-17 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9ab138eb-645c-3688-898e-485ee8b1856b | -6.70451 | -44.31928 | 2025-07-17 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32b5b9e4-86f4-35e4-96ec-7f3d26008428 | -9.13586 | -40.54159 | 2025-07-17 03:53:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9c7f7b4d-79a4-36bb-b204-928aa759093d | -3.38945 | -47.48565 | 2025-07-17 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 3b571a36-f909-3ab5-9c68-87a19febf312 | -6.72366 | -44.33457 | 2025-07-17 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 754c22d6-5355-3751-898d-7eee39e59248 | -6.99913 | -44.22087 | 2025-07-17 03:53:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 67d75da1-b8e2-3a01-8b0b-8f148b5d959e | -3.38968 | -47.48116 | 2025-07-17 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3b404fce-215f-3091-94db-a4ec873cca6f | -4.58539 | -37.80879 | 2025-07-17 03:53:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b36dd19f-0204-399f-899c-0b24aa12d353 | -6.96525 | -41.53426 | 2025-07-17 03:53:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 005643d3-9060-392f-ae27-ab3abf459300 | -7.61528 | -44.3022 | 2025-07-17 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2b4f6563-d36f-375a-914d-fbf683941948 | -3.38289 | -47.48753 | 2025-07-17 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| d392e439-dd08-34cb-905a-4e21308e6242 | -7.57129 | -43.95304 | 2025-07-17 03:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2a4f8904-76bc-36d4-b82e-5f98bdc08eba | -6.85424 | -44.77173 | 2025-07-17 03:53:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed3e1945-0cdf-3810-81f1-f8cc3bebd46b | -6.70873 | -44.31997 | 2025-07-17 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| b8b5e280-67ea-3394-bc23-db5b4d56a6de | -3.38393 | -47.48467 | 2025-07-17 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| a6a3ef82-1945-3888-9b2c-95622dc9f99f | -7.94543 | -43.86494 | 2025-07-17 03:53:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c8df057c-b38d-380c-8f35-93fa2308ce3d | -6.85062 | -44.76671 | 2025-07-17 03:53:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a07d545b-2430-31a3-b1a6-e072e5615927 | -6.85472 | -42.05398 | 2025-07-17 03:53:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 121fc66a-27dd-3292-89f8-01e04005783e | -4.80406 | -43.225 | 2025-07-17 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1adf3c0c-7158-3d2e-a8b9-4b8253de1f56 | -3.66315 | -48.31652 | 2025-07-17 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7966670-3675-331b-af65-3f0aef3eed53 | -7.35053 | -44.19587 | 2025-07-17 03:53:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cab2dbea-be2f-3448-b865-c72bfe018057 | -6.73339 | -44.32821 | 2025-07-17 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c2dc4fc6-6cae-32fe-8900-67a9c7f5b438 | -5.78889 | -45.09027 | 2025-07-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b2919a43-320b-3601-82ec-cbef6f17f714 | -6.85651 | -42.75037 | 2025-07-17 03:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a0c8eb23-8396-352b-a635-480559c2c539 | -7.15231 | -46.09168 | 2025-07-17 03:53:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2470a668-7cfd-3df2-9760-05fcbea69250 | -5.56817 | -44.28931 | 2025-07-17 03:53:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cbb8ae25-fc72-3ec1-8481-9970ab04d003 | -7.60944 | -44.30191 | 2025-07-17 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cad3a21a-5ae4-31d8-bb28-ea279001de92 | -3.37901 | -47.48005 | 2025-07-17 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1631a114-d0da-3d8e-9887-957624424f2f | -9.58167 | -40.34816 | 2025-07-17 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3cb68419-dca7-3f2c-80f4-8eb7bbcb9f96 | -7.46095 | -44.71774 | 2025-07-17 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ec2e677-a256-3a0b-a5c5-03c0944e38d7 | -8.10596 | -43.14883 | 2025-07-17 03:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| fbb1b1ff-e3fe-3efc-8cfb-eed0162dd96a | -8.75141 | -46.60124 | 2025-07-17 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95fd328e-312f-3c93-89c1-08107a2d3a7d | -4.44751 | -38.4467 | 2025-07-17 03:53:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 0032f7a4-6c63-3d2b-9b8f-f84f60c5f439 | -6.71587 | -44.32917 | 2025-07-17 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |


[Clique aqui para ver as próximas entradas](README13.md)
