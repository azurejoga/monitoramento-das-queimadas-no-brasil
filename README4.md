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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8bac1165-13ba-3c7c-be5e-4c3eda22bca1 | -1.06623 | -48.88255 | 2026-01-02 04:25:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3068f49f-fb81-3dfd-85bc-eb7424ab0833 | -3.51817 | -43.62218 | 2026-01-02 04:25:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 09c73c55-b8ec-3beb-a882-481d88740d8c | -3.31319 | -49.7057 | 2026-01-02 04:25:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db0874c5-ba64-36cf-bafb-32cc6619ec94 | -2.09418 | -48.37683 | 2026-01-02 04:25:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a24c565f-f4da-36ed-b281-d33d07e2437b | -5.4732 | -46.19339 | 2026-01-02 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9bf64fe8-ee86-34b7-8a0f-b8110d154875 | -5.26318 | -37.6101 | 2026-01-02 04:25:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 4.4 |
| d0f234f5-575d-3062-a929-5a07bad07292 | -2.7459 | -51.6621 | 2026-01-02 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7c7b9279-ccb3-36a4-b50b-cdceb3b94056 | -5.47713 | -45.41253 | 2026-01-02 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd1e17f6-8eba-33e2-b173-ae207f60e03a | -3.07006 | -44.95515 | 2026-01-02 04:25:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 36f072d2-785d-3b36-9aa9-919e71d8441a | -4.51161 | -43.69108 | 2026-01-02 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 09443735-d6e6-39a6-8ffe-7939fce54518 | -3.81622 | -43.41191 | 2026-01-02 04:25:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a6f4dec-26c3-3ddd-b283-3671587e2ebe | -6.28983 | -39.60141 | 2026-01-02 04:25:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3a37726f-94b8-3f1f-9364-cff7cb75eeb0 | -3.65586 | -52.05599 | 2026-01-02 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b92f6a1b-a39e-306e-8ad5-30d4c2a64fe5 | -5.28113 | -35.76499 | 2026-01-02 04:25:00 | NOAA-20 | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9c69a99a-ca1d-320d-8317-317ebbaa4c64 | -3.04785 | -44.92322 | 2026-01-02 04:25:00 | NOAA-20 | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d40df6e-fdd3-3c8a-bbba-82e753aaa9fa | -3.43134 | -42.19301 | 2026-01-02 04:25:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1e1bfb1c-ff26-3fb9-bf90-48cb6426016e | -3.242 | -46.91357 | 2026-01-02 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b27e5ef2-348f-33e9-805f-3285f05f2d7a | -1.1189 | -47.7442 | 2026-01-02 04:25:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eedf2f18-8a4a-3344-9663-0b0de962dbec | -3.86766 | -54.23329 | 2026-01-02 04:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 154b177c-594a-3d9d-a20a-fd31b62ff6c7 | -3.07061 | -44.95168 | 2026-01-02 04:25:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ec84cb1b-b42d-3809-a0f5-fd4adead7bbe | -5.74283 | -35.38075 | 2026-01-02 04:25:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 95ed3f26-78c4-36a3-ae9e-98ebb8f4c908 | -5.72291 | -45.03226 | 2026-01-02 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9249d97d-c48f-328e-9216-cb4c2acb47dd | -5.28635 | -35.76996 | 2026-01-02 04:25:00 | NOAA-20 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5fd0bdbc-2e51-3adb-a1a4-11dca9db3735 | -1.23876 | -48.15461 | 2026-01-02 04:25:00 | NOAA-20 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6997cad7-62f8-3ed9-a141-d7ecbde23784 | -3.32785 | -39.99781 | 2026-01-02 04:25:00 | NOAA-20 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 09017580-4ddb-3f97-8f03-2e228393ed6d | -5.04837 | -43.60466 | 2026-01-02 04:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 69681084-02ca-3f1b-af91-e9b580e16d32 | -2.86004 | -51.81966 | 2026-01-02 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a511494a-a844-397e-a172-d10b505a4ef2 | -2.26415 | -46.48552 | 2026-01-02 04:25:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 376fd25c-0ecd-3615-9124-34780cb2211a | -3.32774 | -39.99822 | 2026-01-02 04:25:00 | NOAA-20 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a7529e7c-994f-3ce3-a289-75d98226053f | -5.74343 | -35.37641 | 2026-01-02 04:25:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 74f1d3cf-bd3a-3635-b6ac-313931aaca65 | -5.28228 | -35.75681 | 2026-01-02 04:25:00 | NOAA-20 | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 7.6 |
| df1d0b58-63fc-3ded-ab5e-151694b59f25 | -1.06252 | -48.88196 | 2026-01-02 04:25:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a7c05bf-8105-352f-b848-b9abbb91568f | -2.85692 | -52.79981 | 2026-01-02 04:25:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6dee4e6-2cf5-3594-8cb3-c6b3661bb6b6 | -1.06387 | -48.88441 | 2026-01-02 04:25:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 030feb10-2fb6-3418-8161-eaf95caeea6b | -2.39725 | -44.93515 | 2026-01-02 04:25:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 52c2aa23-eee6-3274-a59f-abcba6fda6aa | -1.06994 | -48.88313 | 2026-01-02 04:25:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ecee6ca-29b5-3e44-8ad1-c88b2a9e191e | -3.63945 | -49.70108 | 2026-01-02 04:25:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c468142f-1354-3e52-b4b5-d54cc6891f61 | -3.66474 | -48.92847 | 2026-01-02 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dbced93e-3337-3276-bcbf-ede670f4a5fd | -5.4738 | -45.412 | 2026-01-02 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9dd0a6b-7a1d-310c-9b55-969f35f67dc7 | -3.86649 | -54.23188 | 2026-01-02 04:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c70c9110-5ed5-3143-bfce-562f7419896c | -5.28171 | -35.76089 | 2026-01-02 04:25:00 | NOAA-20 | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a3c47e9f-acca-3ed3-b05b-bdc08820de71 | -0.08933 | -51.28323 | 2026-01-02 04:25:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4f74a7a-7ce7-3396-b8df-c5357774ffe5 | -3.89317 | -50.15021 | 2026-01-02 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00977a22-dee3-3c1c-95a7-39a959cde542 | -3.0473 | -44.9267 | 2026-01-02 04:25:00 | NOAA-20 | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 029da15c-9abd-3808-9069-eb8647d1b16c | -5.04522 | -43.60733 | 2026-01-02 04:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 70dbc933-ed60-302c-bf94-1c914363366b | -4.77092 | -37.82812 | 2026-01-02 04:25:00 | NOAA-20 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8692fda4-5928-39e8-b074-26b19b767459 | -5.7218 | -45.03938 | 2026-01-02 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9db0be04-c1c5-3990-9fc4-43c9a0b74f3a | -2.75388 | -51.66764 | 2026-01-02 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f742aa4-2819-307d-bc59-11dad6b0bb07 | -3.53165 | -43.66537 | 2026-01-02 04:25:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0de551fc-959a-3390-af98-6aa2dd413426 | -3.31734 | -49.70451 | 2026-01-02 04:25:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83401b5c-0a6e-3f3c-9d80-3f9ac28402d9 | -0.86854 | -51.96817 | 2026-01-02 04:25:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8edf174c-c266-3873-a964-27a5d8f1e896 | -5.72626 | -45.03278 | 2026-01-02 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 028b739b-9756-3992-b406-d97f8f846fcd | -3.31356 | -49.7039 | 2026-01-02 04:25:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f72b5e7-50c3-3c99-82b8-f2624b7931c7 | -3.70421 | -50.25584 | 2026-01-02 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eae87965-ded6-3de4-bdec-b58c2401d673 | -3.52361 | -43.6718 | 2026-01-02 04:25:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bead4467-1811-325f-bc40-11d89a03087d | -1.92729 | -52.1027 | 2026-01-02 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0592764c-5c30-3ce1-bed1-00f843d48fad | -1.99431 | -48.00263 | 2026-01-02 04:25:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9f4b7207-8ac3-3ac1-a97e-6a5e0510e968 | -0.08493 | -51.28255 | 2026-01-02 04:25:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| acfafa0b-85a8-34b6-a8b0-359873a7ed21 | -1.92511 | -52.11634 | 2026-01-02 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aa5fddca-d57a-3681-9f38-c0b23d81fcde | -3.52763 | -43.66859 | 2026-01-02 04:25:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e4a1ebc-2bf7-3f80-afcb-c239d81d2c00 | -5.93059 | -43.3983 | 2026-01-02 04:25:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 39a2caa8-30f8-3263-9e22-4fc09fc31397 | -2.74955 | -51.66693 | 2026-01-02 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3cdf8e1-f7e6-3233-88bd-38d68ab3c039 | -3.66633 | -48.92774 | 2026-01-02 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8e7810da-a42a-39c8-836d-14d95eafb0f5 | -2.08245 | -47.87717 | 2026-01-02 04:25:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3879770-203e-3124-bd1c-83e8794b4652 | -6.29048 | -39.60254 | 2026-01-02 04:25:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7f79e214-d4ad-3934-9505-261ad06c8394 | -2.88042 | -52.57163 | 2026-01-02 04:25:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a95c334f-cd69-3493-a598-d33001f76b0c | -2.09776 | -48.3774 | 2026-01-02 04:25:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 658cabf3-6ce5-369d-b224-d12f1ef5ea73 | -5.28693 | -35.76588 | 2026-01-02 04:25:00 | NOAA-20 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 32757ca8-b075-39ea-96df-0d553ced1a64 | -1.79524 | -48.06933 | 2026-01-02 04:25:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7af0c2aa-eeba-3b58-a97b-c5f09e7615b3 | -5.28751 | -35.7618 | 2026-01-02 04:25:00 | NOAA-20 | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7ba4ccc3-8bd6-3729-b7be-4cccad61933e | -3.66565 | -48.93189 | 2026-01-02 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de008cb1-1101-3509-bbd0-0a7cd9977823 | -1.06759 | -48.885 | 2026-01-02 04:25:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef06b581-fef7-381f-bffa-332edb855a1e | -5.02791 | -39.86569 | 2026-01-02 04:25:00 | NOAA-20 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c776643e-6d39-379b-abca-f7a9ddf42370 | -5.04486 | -43.60415 | 2026-01-02 04:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1fd1e2f2-791e-372d-9341-18da30d9fe35 | -3.66408 | -48.93263 | 2026-01-02 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 52a61322-2bf9-3dac-8fab-00b79db7fee1 | -1.86657 | -47.98733 | 2026-01-02 04:25:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 08a53e78-af24-3fff-ad16-4a1a4b9ce022 | -0.09 | -51.279 | 2026-01-02 04:25:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4325f6cd-e617-337a-bc54-ae657cc6dc04 | -3.52705 | -43.67234 | 2026-01-02 04:25:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f7d7b23-7c57-3e9a-94d3-dfae9f3d3483 | -1.75795 | -45.69134 | 2026-01-02 04:25:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a6a345d-7041-3f65-87b2-bc13f939e4f8 | -3.86598 | -54.23483 | 2026-01-02 04:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9fddce7d-b7f5-36a5-8f54-e80401069976 | -5.23771 | -38.13583 | 2026-01-02 04:25:00 | NOAA-20 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 639486a6-74e1-3335-83d2-c7bcb58db223 | -0.86927 | -51.96357 | 2026-01-02 04:25:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab393af3-1735-3361-b8dc-81b3865cca13 | -1.52181 | -45.80988 | 2026-01-02 04:25:00 | NOAA-20 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 904da645-d0d6-3869-93b1-308de0340c41 | -4.13719 | -49.27783 | 2026-01-02 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 45c5a479-cb84-31cf-93e3-07ecff47a5c2 | -0.86999 | -51.95897 | 2026-01-02 04:25:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c65cd46-9615-3564-a577-0c2c93e6778f | -4.21437 | -42.98819 | 2026-01-02 04:25:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| edc1d60a-04b5-3997-950d-d7818b694747 | -5.04581 | -43.60343 | 2026-01-02 04:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 53c35e40-c060-3580-8d69-6fa832c8c34a | -3.62732 | -43.8632 | 2026-01-02 04:25:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d4d604df-1f87-3d96-8716-74cf5911e81e | -10.92256 | -54.2478 | 2026-01-02 04:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 86d0445e-e624-3f9f-bd9b-15720d105867 | -6.02117 | -44.55236 | 2026-01-02 04:27:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be5ea4b5-e747-3b98-9740-6742962a68f4 | -9.57577 | -44.59858 | 2026-01-02 04:27:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e60c2e0-3470-394f-8a0e-31ae1bcd242e | -12.55525 | -49.89436 | 2026-01-02 04:27:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 38e7a122-42b4-3575-862c-b0e2eeed458e | -10.93959 | -49.43729 | 2026-01-02 04:27:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb55c53a-2f26-323b-b9a3-837b36d7b6fe | -10.77545 | -44.33089 | 2026-01-02 04:27:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7514c795-d173-3107-a89a-13301e6f4a78 | -7.46216 | -35.19611 | 2026-01-02 04:27:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| a8d4a913-5f98-3ee2-84cf-2b491ee7a29b | -7.46089 | -35.19663 | 2026-01-02 04:27:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 58748568-42b2-3b5b-b66c-68a99ec1f328 | -7.45594 | -35.19533 | 2026-01-02 04:27:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 4cc1e4b2-0ae8-3246-b999-3201c86859b0 | -9.57928 | -44.59913 | 2026-01-02 04:27:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 778f9c2f-56b6-3e39-bd24-d432c0ee87b1 | -10.92338 | -54.24329 | 2026-01-02 04:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a5511c7-2f90-3109-9427-b632e872a0e3 | -8.70588 | -38.64084 | 2026-01-02 04:27:00 | NOAA-20 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |


[Clique aqui para ver as próximas entradas](README5.md)
