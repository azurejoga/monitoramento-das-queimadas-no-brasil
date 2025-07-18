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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4d809e0-cf56-3f8d-9756-299d0929bd84 | -6.46867 | -45.17033 | 2025-07-18 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af7fe1aa-0fe6-3193-a4e7-5fa3996c47d5 | -5.79038 | -45.077 | 2025-07-18 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 49745c83-a3f7-32df-ba45-86d4210e11f5 | -7.06397 | -42.98829 | 2025-07-18 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b73705fc-3b8c-34b4-9cec-15e08a7483c5 | -7.23954 | -42.93454 | 2025-07-18 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1ced0de5-aa10-3730-acb8-713f80d8b570 | -6.99128 | -45.62058 | 2025-07-18 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c269c51e-516a-366a-9a8e-75463940684a | -7.24389 | -42.93066 | 2025-07-18 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e2856c07-5013-3e43-a030-b5bebf8c8ff2 | -7.29148 | -44.22604 | 2025-07-18 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99ce6b3a-44d9-3a6f-baf7-b48fd4f19548 | -5.19659 | -45.48497 | 2025-07-18 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 14923e65-3d6d-3a1e-9a8b-fa7bfbcc29f6 | -7.8339 | -44.83678 | 2025-07-18 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 257be006-ee6b-3caa-a731-d0d57c51d120 | -7.61361 | -45.55048 | 2025-07-18 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d1b0f662-63e1-326d-93e3-620bf8bb6fa7 | -3.38499 | -47.48483 | 2025-07-18 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| f4ccea53-0bb2-3d41-a31e-8c51fc0241f9 | -3.86178 | -50.08485 | 2025-07-18 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 21aa3210-2cdb-337a-b90d-fa6b3d4a8e95 | -2.91426 | -48.24341 | 2025-07-18 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8048c6d7-9273-366e-a533-b2e7033e41b1 | -2.94406 | -48.05336 | 2025-07-18 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fccd3526-23da-342a-a142-ded383a2c846 | -8.11753 | -43.14583 | 2025-07-18 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 49c25ae3-a719-3ead-9086-062609db3b11 | -5.73345 | -44.51518 | 2025-07-18 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b20e6002-c6d2-3604-ae11-a60b7cb39136 | -6.29861 | -43.41006 | 2025-07-18 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 017556f4-a767-3908-9582-c3c732786276 | -3.40022 | -47.49845 | 2025-07-18 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 19f81263-a1c4-3928-a187-6e4c818430d2 | -7.28569 | -44.21717 | 2025-07-18 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c5503359-64b5-38ae-beb3-b8df2404802c | -2.92677 | -49.07192 | 2025-07-18 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d79d1f7b-aa2f-3793-830f-4596a51aa934 | -1.68816 | -50.3421 | 2025-07-18 04:25:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e33a8bb-52c7-3f78-82b0-f7f695147272 | -5.85886 | -42.86703 | 2025-07-18 04:25:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a89f069d-51cd-3cdf-b410-609f69ad7506 | -6.26557 | -44.06152 | 2025-07-18 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4ce075f-27ce-31a6-88e1-1e66cd4bbb16 | -6.87925 | -41.73294 | 2025-07-18 04:25:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4ddb14a5-eedd-3cc5-b748-c13d09091607 | -8.10578 | -43.14857 | 2025-07-18 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d5ba949a-2a98-3202-8629-d6ac2a77a1c6 | -6.97446 | -42.80988 | 2025-07-18 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 17d15d75-2920-39f1-b8f1-74fad0fe8567 | -4.52464 | -42.06782 | 2025-07-18 04:25:00 | NOAA-21 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b4ed86f1-bc72-36eb-8768-cdd75697d210 | -6.48681 | -44.86033 | 2025-07-18 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77f69409-9be8-38a2-8fee-5eadb220788f | -7.58939 | -46.30413 | 2025-07-18 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1b5129a9-2b4d-3d46-8a92-e1550d910454 | -6.87468 | -42.7509 | 2025-07-18 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 76d52185-0b31-3b55-82de-ca4412c7f2ff | -5.84256 | -44.10048 | 2025-07-18 04:25:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2682877e-82ed-3aa2-aa0b-d4c4ca858249 | -7.94035 | -43.85735 | 2025-07-18 04:25:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bf0d8924-1d94-3365-afa6-fc305a00704c | -6.67685 | -43.02626 | 2025-07-18 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dc5675a0-8a8a-36d8-a761-5c5f4a724f96 | -2.44387 | -47.32804 | 2025-07-18 04:25:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6a544462-eacb-3518-84a5-056e7b8f5168 | -4.64887 | -43.12038 | 2025-07-18 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4efe2724-234f-3f28-a76d-a9344fc30181 | -5.78758 | -45.07293 | 2025-07-18 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c4915e5d-ef11-3896-aec0-354d8b69c1dd | -5.91211 | -43.48072 | 2025-07-18 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 94497cfd-5901-30a0-aa37-00958297c601 | -3.73625 | -53.99158 | 2025-07-18 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0072eb38-ec36-3f84-8c31-94191e10e53c | -5.85646 | -44.97457 | 2025-07-18 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fc13880a-b2b6-3509-b2b0-770394ecc272 | -3.9445 | -48.09226 | 2025-07-18 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3631363c-da85-324d-82c3-903a43aba8eb | -6.29922 | -43.40594 | 2025-07-18 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1fb8b11b-ede1-304d-b5dc-1e73cae07f68 | -5.78703 | -45.07648 | 2025-07-18 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6d9fd313-39d1-347b-8371-ed0e2df8e9dc | -5.91626 | -43.47726 | 2025-07-18 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5999c49e-3f40-3c3c-99ab-bd291643fdf2 | -5.99834 | -52.19458 | 2025-07-18 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44f53eee-4c8b-397a-8fd8-08aa3a763040 | -6.57854 | -41.47055 | 2025-07-18 04:25:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 2b3c98f7-d5e5-3682-a8dc-8cd5aef0dfae | -4.11382 | -47.93446 | 2025-07-18 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f465b7c1-aef6-3139-8663-7bdae2d4ce5b | -5.65977 | -43.7117 | 2025-07-18 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 257f03a5-c4cf-3ee0-845e-795f3fff92f7 | -6.95657 | -43.75552 | 2025-07-18 04:25:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a1fddf3-1b69-3711-b1af-c08fbaec6905 | -2.65401 | -48.80772 | 2025-07-18 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| baf6e0de-5b9a-32f6-a4ea-f912b8ab1421 | -6.55393 | -43.61732 | 2025-07-18 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ba000ce-4b71-3060-bc8b-5cc25030132a | -3.51797 | -47.21323 | 2025-07-18 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a9db7d74-4907-3d0e-b2c0-6a4114d2f9e7 | -3.12311 | -47.01268 | 2025-07-18 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 95111b58-bcd1-3699-93a5-b6bc25c4f295 | -6.3382 | -43.74995 | 2025-07-18 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2b6ed83-2bc2-3066-a058-c364fbe17585 | -7.06897 | -42.98004 | 2025-07-18 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6fc3ca8d-2dc1-30ff-a5e6-04d0ef145f1a | -6.26846 | -44.06588 | 2025-07-18 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df5ce59e-2d4c-38f1-b886-524bbb906c26 | -8.08662 | -43.1502 | 2025-07-18 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 7b9e5e39-3f97-3ba3-b76b-f6b0d9715361 | -4.58963 | -43.32018 | 2025-07-18 04:25:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9264b5bd-f634-3bd6-8fd7-ca6ec24e4201 | -3.65594 | -48.32321 | 2025-07-18 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 135cb2d9-d7c2-37af-982b-bf046d2dd083 | -5.65917 | -43.71563 | 2025-07-18 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 48ccd966-c69f-3412-acd4-c80d32413e52 | -6.89369 | -42.77687 | 2025-07-18 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8cd9418d-5bf8-3e9c-abc4-8409588fb61d | -4.96101 | -47.70487 | 2025-07-18 04:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a2963e2b-d041-3d3e-b2f5-9b8ab519d0ee | -7.00093 | -43.74991 | 2025-07-18 04:25:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 926eaab3-95ee-3743-a231-1c5ee4e0e2c3 | -3.3912 | -47.48954 | 2025-07-18 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| a3c73da9-a5ec-383b-a6d5-a00de2a3f5df | -5.85701 | -44.97099 | 2025-07-18 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cc5adfaa-2e15-344b-84a9-388ae6f07f36 | -5.1999 | -45.48549 | 2025-07-18 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 29.2 |
| a539595e-e89e-3ea0-b8bd-5141fe271e06 | -8.08228 | -43.15404 | 2025-07-18 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 168c1af6-797c-3deb-8b8c-63d6d1fe62bd | -5.65567 | -43.71508 | 2025-07-18 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 42c48db6-5875-3865-92c1-f0311efd32cc | -2.9219 | -48.24059 | 2025-07-18 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9cc0b4e5-fe50-3d11-b600-a9d7ab190311 | -5.78313 | -45.07951 | 2025-07-18 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bcada35a-f11e-3db9-9e6a-86b1ce971e56 | -7.61081 | -45.54638 | 2025-07-18 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15bd31e1-981f-3b6b-acbb-ad223693c359 | -7.20673 | -43.01195 | 2025-07-18 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 589adea4-383d-3096-b9ca-213f56a4cae9 | -4.80013 | -43.21982 | 2025-07-18 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 338c63f9-069e-3f4d-84b5-1f151615cb2d | -7.34613 | -44.19471 | 2025-07-18 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| ed09e616-74e3-35fc-955c-6248fc761163 | -4.80309 | -43.22437 | 2025-07-18 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 4a419500-ea91-3b44-bd55-629ea889c159 | -4.58729 | -43.31172 | 2025-07-18 04:25:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e8b808f0-988c-3738-a1b9-c8cf8c838d5c | -3.39459 | -47.49008 | 2025-07-18 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ba41cefe-b003-333d-8aec-74d8d2a02aea | -4.52088 | -42.06724 | 2025-07-18 04:25:00 | NOAA-21 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 07b16874-99ed-3e50-8ac3-3bf1e9f12857 | -3.39236 | -47.48225 | 2025-07-18 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| e4a139bb-a4ac-32cc-a4c1-c984b5d7ae58 | -6.99461 | -45.6211 | 2025-07-18 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e6592f8-479f-3692-a7ba-93f8c235499c | -7.19515 | -44.07302 | 2025-07-18 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cfa723fb-30c5-3b3b-93e7-1aef0592e107 | -6.49914 | -43.472 | 2025-07-18 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 017a11e8-3929-36fe-acd9-5326eb8e0048 | -3.39633 | -47.47913 | 2025-07-18 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 1b974095-c676-3d69-88aa-8a22691c122f | -6.92236 | -43.21132 | 2025-07-18 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 50dca622-644d-3b33-8e09-c8870af2da6d | -6.68661 | -43.1875 | 2025-07-18 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7cdc6b26-a389-368d-8137-b84edeb01e73 | -4.41036 | -42.15482 | 2025-07-18 04:25:00 | NOAA-21 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4db89ef0-5060-3e68-8d14-b03be7f36c74 | -6.34525 | -43.2441 | 2025-07-18 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a59745ec-c0ff-3ca2-846b-0731228e9b1f | -5.66618 | -43.7167 | 2025-07-18 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 609a1989-3d06-3da3-8a41-2d0810459024 | -5.78033 | -45.07544 | 2025-07-18 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 756e27a9-cb3b-312a-95d6-9bda1453d532 | -3.38897 | -47.48171 | 2025-07-18 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| fcdf5365-0d9c-38df-a80f-36cc1a2b944f | -6.16392 | -43.75618 | 2025-07-18 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 30672752-002a-33f6-9375-de5171fe9b74 | -7.06028 | -42.98776 | 2025-07-18 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d0e1744f-101f-3cc4-89d6-89297ccadbeb | -7.00394 | -43.75299 | 2025-07-18 04:25:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 348e5b66-132f-3899-bbdf-5a0e3bd378b3 | -6.45397 | -45.07307 | 2025-07-18 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80101f75-0fd3-3371-afb4-9e74660cdeb0 | -3.73042 | -53.99294 | 2025-07-18 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 48a1fa79-8dfd-39c4-8537-c5ec21b83acb | -4.48236 | -46.07582 | 2025-07-18 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 34cba93e-acdc-387e-a776-495e8ecb7b59 | -3.38838 | -47.48535 | 2025-07-18 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 60458b5d-3798-369d-a50c-5e156dc0b91c | -9.26758 | -48.1967 | 2025-07-18 04:27:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e8155827-ae55-3ad5-bd0b-6f6e33769ca9 | -11.99853 | -45.30603 | 2025-07-18 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 45abcca6-27ed-3035-8113-f7c84e2535f3 | -8.65067 | -47.75614 | 2025-07-18 04:27:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e852e79f-fdaa-3799-ab54-662ad0776e9e | -9.44595 | -50.56176 | 2025-07-18 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README15.md)
