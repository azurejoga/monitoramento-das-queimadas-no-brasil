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
| 813cdf7e-8291-3e37-a02c-d86714e69744 | -4.88099 | -48.90231 | 2026-07-03 04:19:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e528ef8d-fb81-3bde-ac2a-a867e46d5250 | -12.74891 | -44.51891 | 2026-07-03 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 180.6 |
| e95f797d-1c72-3707-851d-8205f1418681 | -12.36017 | -47.42947 | 2026-07-03 04:19:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cbfad967-a77b-371d-a72e-1259aca88fe1 | -4.47393 | -40.86502 | 2026-07-03 04:19:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c09cf5a2-dd3f-3cc3-b51b-3c81eafaffd7 | -5.37609 | -43.38147 | 2026-07-03 04:19:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3398178-6683-359d-add4-fd566c11fe98 | -10.56282 | -49.13829 | 2026-07-03 04:19:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16593b95-a146-3268-b982-19d1198c61aa | -4.15042 | -43.09513 | 2026-07-03 04:19:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 005ae90e-8cef-3078-a4d4-dfe3d5d4e30b | -5.9086 | -43.62231 | 2026-07-03 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a80d10bb-db9d-31d9-9c09-4632ce5f0a8f | -5.78779 | -45.05752 | 2026-07-03 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2affe0d2-64a4-3544-ba3c-48c86744d56a | -5.80225 | -45.03314 | 2026-07-03 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 25a657ce-b138-36e0-8b9b-73a2e254cbea | -5.78942 | -45.06924 | 2026-07-03 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e2c8b3cc-b3cb-3a80-8294-ff206ffdef37 | -10.48449 | -42.41287 | 2026-07-03 04:19:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 135e16f4-14fb-35a0-8aaf-798d6f1717cf | -5.80263 | -43.79789 | 2026-07-03 04:19:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7b94632d-ecf2-3028-bc78-d9bde9cb4580 | -10.94999 | -43.05487 | 2026-07-03 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 37ac10d6-e570-3533-9e95-7b0fbb580af3 | -11.35328 | -55.40512 | 2026-07-03 04:19:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eaeb74cb-5112-3de0-b86e-4361d1696375 | -12.32087 | -46.73523 | 2026-07-03 04:19:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4f3444f-1452-38c7-a8b4-2519d61a6b71 | -4.38604 | -43.34464 | 2026-07-03 04:19:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7d5fdc0b-1b85-33a7-ae58-b1b8bcf7de7c | -11.43929 | -46.52976 | 2026-07-03 04:19:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e4834434-6c08-35aa-a3ee-091bf544336e | -12.75274 | -44.53758 | 2026-07-03 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 6c37e0f1-28c2-356d-b819-311857c26b2e | -11.49852 | -47.39831 | 2026-07-03 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6f668ba-9f91-3c77-a1a2-212f207fe9c8 | -11.44337 | -46.52647 | 2026-07-03 04:19:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1a7cc8c7-dd0e-35b4-8c2c-76ba94ed41af | -4.35004 | -47.7656 | 2026-07-03 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a09cfc6-eb39-30fd-9e81-ff31d153c18e | -11.35747 | -55.41524 | 2026-07-03 04:19:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a96e0692-4c74-31dc-aa7b-e24effecafa0 | -5.10967 | -43.75243 | 2026-07-03 04:19:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0c77dbb4-366a-3921-98d8-ff257231abf4 | -5.93809 | -46.34994 | 2026-07-03 04:19:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 24ffe8ec-230e-3121-9072-8ee1164be958 | -17.30934 | -42.65939 | 2026-07-03 04:19:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e56be6a7-315c-319a-bf17-acf5fb437f2f | -3.99787 | -48.4024 | 2026-07-03 04:19:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efd57b5a-c0c1-3616-ba82-fd347fc93479 | -12.75277 | -44.51593 | 2026-07-03 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 37.8 |
| e9144150-1d1c-3b67-a7c6-fb93c6e1f633 | -11.01336 | -47.47525 | 2026-07-03 04:19:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 892fa378-84b7-32c4-aeba-695f5cabb07b | -12.74946 | -44.51539 | 2026-07-03 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 37.8 |
| e0f608d0-c402-3a7f-9819-55ad90ec42ea | -15.72866 | -41.352 | 2026-07-03 04:19:00 | NOAA-20 | DIVISA ALEGRE | MINAS GERAIS | Brasil | 3122355 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ade6285d-0ee8-35f7-9c07-e1e4001f90fc | -11.35832 | -55.41087 | 2026-07-03 04:19:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf03d131-db55-3359-9dc3-1378d161d14d | -10.50919 | -50.31761 | 2026-07-03 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7ce5fe42-481d-3ce8-a1ce-6af74d81e550 | -5.55158 | -43.96626 | 2026-07-03 04:19:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 985e3e34-cea4-372b-bf66-c85ea8304e64 | -5.79159 | -43.63214 | 2026-07-03 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d372b17f-d6c3-3925-a7f6-17339608a62a | -11.35069 | -55.41838 | 2026-07-03 04:19:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c931d1cb-f691-3afe-a055-615ad7a54630 | -5.80846 | -43.80236 | 2026-07-03 04:19:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4680a839-fb9d-3746-bded-ad79aa8e5221 | -10.93379 | -43.04865 | 2026-07-03 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8230fa65-c77e-319a-a7c0-5b227d74fcf7 | -12.7511 | -44.52649 | 2026-07-03 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 18d5ddaa-a956-3fa2-b942-c80386eb57c9 | -14.41473 | -44.59484 | 2026-07-03 04:19:00 | NOAA-20 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 27e57088-1199-3de9-83d7-34b58ca5e7d7 | -11.5334 | -46.64023 | 2026-07-03 04:19:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ff2bf954-ca33-3b8f-bd7e-016ddc422e06 | -5.79747 | -45.0629 | 2026-07-03 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| dc1d6593-d038-3bd4-adbe-56189e02e468 | -14.41142 | -44.5943 | 2026-07-03 04:19:00 | NOAA-20 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 63bbab85-6660-3b5a-93a6-1f46e945c0b6 | -13.97968 | -47.44246 | 2026-07-03 04:19:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 922cec2b-c4fa-3ebe-bf4a-c3415be5af07 | -17.3189 | -42.64356 | 2026-07-03 04:19:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff07f990-e783-3dde-aa38-de06c33e2cb1 | -17.30994 | -42.65518 | 2026-07-03 04:19:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 1a963548-9047-3271-9c02-e7310637dc01 | -11.34209 | -55.43086 | 2026-07-03 04:19:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aeb3138a-7f32-364e-9b25-f133a682c76b | -17.31532 | -42.64303 | 2026-07-03 04:19:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2418719-d5d4-3b61-bd0a-c0efdd6fe876 | -11.85735 | -48.24567 | 2026-07-03 04:19:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b9428f97-233a-3f4b-9e54-60e6073e7620 | -5.80208 | -43.80138 | 2026-07-03 04:19:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5678726e-1840-3947-97fd-edf6a56f4d29 | -13.98666 | -47.44357 | 2026-07-03 04:19:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8cc503b1-d573-3b38-aa9e-f765607034d6 | -4.34659 | -47.76148 | 2026-07-03 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f661d256-64d6-3b17-811e-fa4e37935166 | -5.79883 | -45.03258 | 2026-07-03 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d59b97b8-473e-32ce-a863-13f8aa2d45e4 | -6.03349 | -42.6189 | 2026-07-03 04:19:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0c2aa84c-878d-36a8-a259-f4da04920fd1 | -12.86725 | -44.35056 | 2026-07-03 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 656abf7a-d1ae-3ea3-8ec8-26cd7fa6b878 | -13.98798 | -47.43571 | 2026-07-03 04:19:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a4c6f3e-a304-3c8e-b368-e76a298bd419 | -5.78899 | -45.05008 | 2026-07-03 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 425fa7f8-d8d8-3092-98ae-c74d42288fab | -11.91073 | -43.38566 | 2026-07-03 04:19:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ab81170b-6434-34c8-9e35-826464418058 | -10.93099 | -43.04452 | 2026-07-03 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 1f5ba314-f8ad-3076-9746-aabfbc17657f | -12.74888 | -44.54056 | 2026-07-03 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eb488336-c956-3637-a4dd-6bae36fd076a | -5.80105 | -45.04061 | 2026-07-03 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e714dbfd-8626-3e5a-b2a6-b76cb1bc19a2 | -14.41529 | -44.59129 | 2026-07-03 04:19:00 | NOAA-20 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ed81129-9ef5-3f08-903a-cd43d30625af | -5.91191 | -43.62284 | 2026-07-03 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c899c846-ccd2-35d7-a9ca-78b7c5fbede9 | -11.34982 | -55.42289 | 2026-07-03 04:19:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e8d56d49-cb01-39ba-a20e-3efb81317f14 | -11.34803 | -55.43201 | 2026-07-03 04:19:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 048b7744-620d-38c7-9414-b7a737e36b3c | -4.8846 | -48.90712 | 2026-07-03 04:19:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 348e96b5-8a77-3f1a-8adc-ffa19332794c | -4.34601 | -47.76497 | 2026-07-03 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2de98381-5311-3371-b681-5922718d7264 | -6.20233 | -42.51774 | 2026-07-03 04:19:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 90399bac-b7c9-3175-a9f2-351c1c371407 | -5.79002 | -45.06551 | 2026-07-03 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 30f3e072-2f78-34b8-9524-68d21efd6725 | -5.78839 | -45.0538 | 2026-07-03 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f0535826-fed6-3d5a-9485-74880c2f038c | -12.49755 | -43.80447 | 2026-07-03 04:19:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b406d0aa-7563-3f36-b685-7f76df7e11b6 | -10.50994 | -50.31344 | 2026-07-03 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1f28b455-b469-31f6-918e-06010b064871 | -10.90452 | -56.85789 | 2026-07-03 04:19:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40c0d942-e59e-3db8-a15f-041fd2c2184f | -12.7456 | -44.51837 | 2026-07-03 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e855604b-f42e-38c4-a3f9-718395e4cf32 | -10.94609 | -43.05795 | 2026-07-03 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.3 |
| c3431b57-128c-35cf-ab19-9ba3830fc987 | -11.34562 | -55.41278 | 2026-07-03 04:19:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1b77814-8ee7-3a6e-8dee-572418f2dd86 | -12.67 | -48.21616 | 2026-07-03 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bf098ab6-4272-3488-9249-512d44e1309f | -12.51148 | -48.2624 | 2026-07-03 04:19:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d79ec907-196e-357e-9b3f-3bda90f064fc | -5.8085 | -45.03801 | 2026-07-03 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a9fb3794-ce62-3395-87cc-ff80f0f66ed3 | -5.79301 | -45.04694 | 2026-07-03 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1ff60a00-8aa1-392b-8b5c-c94661823883 | -9.75582 | -47.87656 | 2026-07-03 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 638ea1a1-f71e-3ddb-af19-ce06fae881ba | -8.70731 | -54.58003 | 2026-07-03 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 758d3e59-3038-3d0f-9141-2962df86e2e3 | -17.30398 | -42.64564 | 2026-07-03 04:19:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a4ca4c0-0c6c-3bba-a083-9007a48a4137 | -17.25643 | -42.65702 | 2026-07-03 04:19:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af96aba0-11db-36a2-b2e9-4a62870587d5 | -6.19902 | -42.51722 | 2026-07-03 04:19:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f5b608bb-0e89-356f-a63f-b66001470658 | -5.80448 | -45.04118 | 2026-07-03 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 342bce79-fc80-3007-97b9-4d1c3cd8d083 | -11.41591 | -56.05305 | 2026-07-03 04:19:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3c581d4f-473b-3251-857f-f9fc8ef68d81 | -12.35949 | -47.43356 | 2026-07-03 04:19:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f9054969-55de-3047-9e5d-cda399117237 | -5.91136 | -43.62631 | 2026-07-03 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| dd71bce7-7a9e-383b-bb26-1869fde308d3 | -4.88029 | -48.90641 | 2026-07-03 04:19:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4cda92d7-a2c7-36db-ae26-2011bf9286ff | -17.30636 | -42.65466 | 2026-07-03 04:19:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 862b7af6-a703-3a8d-9e86-8c635c208797 | -5.93997 | -43.46758 | 2026-07-03 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d68d44ff-8212-3b30-a5da-85074696a171 | -4.01022 | -48.05988 | 2026-07-03 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 8ee3677d-8e3f-3b67-a76e-072b7165a5aa | -5.78719 | -45.06123 | 2026-07-03 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e6164f9-f6ad-321a-88bb-bc8826d99b53 | -10.94494 | -43.04304 | 2026-07-03 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5c95d721-7932-38a1-bb07-d8e273b9ed69 | -10.9416 | -43.04251 | 2026-07-03 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2e528220-d256-3be4-bfe2-238de4c124de | -11.34986 | -55.40662 | 2026-07-03 04:19:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e840a2a1-036e-3757-8ae1-ec4d2ef3d41f | -12.85177 | -44.40589 | 2026-07-03 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6d9dc36d-1091-36ea-902c-b8e87a765faf | -12.75496 | -44.52351 | 2026-07-03 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 82e1f2bf-53ee-3c51-ad4c-84ff774dff5c | -11.84993 | -48.2443 | 2026-07-03 04:19:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |


[Clique aqui para ver as próximas entradas](README13.md)
