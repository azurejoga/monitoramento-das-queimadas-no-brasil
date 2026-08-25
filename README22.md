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
| 5a8c642a-b76c-333a-b48f-23bcbf780834 | -12.20937 | -43.18509 | 2026-08-25 04:08:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ac10923d-5add-3f9b-bb3f-0fa4b62eda52 | -8.16877 | -46.69653 | 2026-08-25 04:08:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0dbe30bf-ee88-363f-9cd5-3f57b3829f3e | -7.67 | -49.38427 | 2026-08-25 04:08:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11efc38e-e8ba-30de-9155-647dfbf159a3 | -11.98537 | -45.91701 | 2026-08-25 04:08:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a129b32f-6d1a-36a7-9ffd-fb286770f6eb | -8.76339 | -45.79782 | 2026-08-25 04:08:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89d2a10a-8020-3526-be96-b761d0d901ef | -12.13283 | -43.3884 | 2026-08-25 04:08:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bee967e3-b479-37b1-884d-a754f29dc5b2 | -10.80225 | -50.92774 | 2026-08-25 04:08:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a3403e32-d2b7-37a2-b415-3790c26311d0 | -12.77719 | -44.27237 | 2026-08-25 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| d87fbc06-29bf-318c-bc1f-a0760ace9403 | -8.08672 | -47.5202 | 2026-08-25 04:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 16bb4e0e-4886-3813-b1f9-44a1597689bd | -11.1666 | -54.00167 | 2026-08-25 04:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 440b850d-cd19-31bc-8134-6f6319065ee0 | -13.44842 | -43.84404 | 2026-08-25 04:08:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2bc34410-5837-39ca-90d5-f688f095e271 | -6.83297 | -52.51202 | 2026-08-25 04:08:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0bb5573e-6337-3a01-a6b7-786038c047ad | -12.41174 | -40.92298 | 2026-08-25 04:08:00 | NPP-375D | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d3f210f3-6c1f-3a9e-bb06-cc17fd0d77d8 | -8.16292 | -46.70098 | 2026-08-25 04:08:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d923159f-7a52-303d-9ab1-d52b312e2a9a | -11.15937 | -54.00011 | 2026-08-25 04:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1578d45b-dfdf-3023-a46d-43ba665cba87 | -10.79506 | -50.93364 | 2026-08-25 04:08:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f8630e88-39e6-3366-9a48-cb31f2972639 | -7.89076 | -46.33734 | 2026-08-25 04:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4db21101-6f51-3ff2-a3d6-935e0feab19e | -12.14382 | -48.26384 | 2026-08-25 04:08:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 13b5ccf4-412e-35e2-a324-26d13026b355 | -12.14344 | -50.60205 | 2026-08-25 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a07691bd-3661-330f-9a47-10397aa5605f | -10.57016 | -46.31106 | 2026-08-25 04:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e5607bff-b103-3c8a-8d2f-f85a2c9d8fcb | -8.16066 | -46.69904 | 2026-08-25 04:08:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55b5d547-3f3a-3620-ba2c-fd3e26fa9b2d | -12.86563 | -48.50006 | 2026-08-25 04:08:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b469165-6ade-3fff-b7e8-1f43c561f1a6 | -12.70767 | -48.4154 | 2026-08-25 04:08:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c12e16f-8864-320f-8197-fbfcbb5ccd9d | -10.37751 | -45.05981 | 2026-08-25 04:08:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 6311c7c3-3a32-368c-99f9-91c28d77537e | -9.69003 | -46.05718 | 2026-08-25 04:08:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e6a53482-6898-3ec7-9eef-151a951ef670 | -12.75427 | -46.44364 | 2026-08-25 04:08:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bc1bce5a-c53e-3d43-b854-f59e59d74e12 | -13.3582 | -48.21143 | 2026-08-25 04:08:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7181de62-400c-3ff7-9a66-9cc19680094f | -10.90808 | -51.06911 | 2026-08-25 04:08:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1d32ed5-a1e6-3ee3-b81c-ef78d177ea30 | -8.93812 | -50.16515 | 2026-08-25 04:08:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3b8970b5-2f8b-35f0-b857-de5dca2e6327 | -12.78103 | -44.27307 | 2026-08-25 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 53046e3f-58ab-31a3-b3e1-235c41e16672 | -11.14083 | -44.47697 | 2026-08-25 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 881d62a9-b940-3c2b-a6a3-fbd9671e219d | -12.205 | -43.18867 | 2026-08-25 04:08:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| afcf4005-7368-3d52-9a1e-1984efa378b5 | -12.70332 | -48.41073 | 2026-08-25 04:08:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 28f71149-f1b0-3f82-8f35-d1fc97ed8864 | -12.75263 | -46.45235 | 2026-08-25 04:08:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1719d4b3-d725-3a6a-a733-800f3ea4a737 | -9.6568 | -48.32614 | 2026-08-25 04:08:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3d032d78-534d-3f50-ab16-7f47833f3c72 | -11.88391 | -43.82003 | 2026-08-25 04:08:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ac31ace8-7455-3618-8c06-c25e2b2f8fbd | -9.69092 | -46.05233 | 2026-08-25 04:08:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0b95d27d-4dcc-3ebc-9651-a0248dc7137b | -8.9332 | -45.74245 | 2026-08-25 04:08:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e195321a-1699-3696-9451-50a7e8bc4971 | -12.7742 | -44.26678 | 2026-08-25 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 09449e41-5a1f-31aa-83fd-9e67e37dcf84 | -14.802 | -48.76282 | 2026-08-25 04:08:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 788daa22-417f-3abc-86e6-1b4a611ce273 | -13.09388 | -43.36806 | 2026-08-25 04:08:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9b412b7-c791-3c57-87df-762c0104814b | -8.1616 | -46.69368 | 2026-08-25 04:08:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b1b732d-7c4a-3293-b882-d2a4faa318f5 | -10.80303 | -50.92543 | 2026-08-25 04:08:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2c0cb12c-5602-3369-ab5f-21199ea49c12 | -8.34671 | -42.4322 | 2026-08-25 04:08:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6a5f4af6-47e9-3d4b-a95e-5300e0ade2f5 | -11.86323 | -51.69513 | 2026-08-25 04:08:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0778160a-c061-377e-8e2e-ae26038bd69c | -12.77804 | -44.26749 | 2026-08-25 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 1908734f-bd92-3ef8-a0ea-0941e9fa7881 | -12.76664 | -48.36994 | 2026-08-25 04:08:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 367d1ce6-3b22-363e-a820-aa66808631a0 | -6.94512 | -52.79657 | 2026-08-25 04:08:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 91f5579e-17c0-3866-a251-6caa6953b0ad | -8.66113 | -47.31989 | 2026-08-25 04:08:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8a546d2-2e08-3ac6-a470-075e9b4b8cc5 | -11.98102 | -45.9089 | 2026-08-25 04:08:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d7be8245-ff0b-34c6-8a8b-5bfa1021b391 | -10.47995 | -50.44304 | 2026-08-25 04:08:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e1dbf399-966b-3a3a-82f7-d366fb05c610 | -12.71902 | -43.20082 | 2026-08-25 04:08:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81e12b98-bffd-3aa9-af3d-1f8a17db4a09 | -14.62172 | -42.53049 | 2026-08-25 04:08:00 | NPP-375D | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e0f9d70d-26e3-35a4-bfe5-f6cc0309a172 | -14.79211 | -48.76069 | 2026-08-25 04:08:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 57c379bf-706f-3098-aeef-9ad8ef25cb44 | -12.87069 | -48.50101 | 2026-08-25 04:08:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d4086fe9-ec0c-3a1d-b376-635afc5749b5 | -6.83428 | -52.50518 | 2026-08-25 04:08:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ebd57dc0-5693-3a08-b086-c61344af5e67 | -12.8556 | -48.49765 | 2026-08-25 04:08:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb3f9552-7622-330a-94ab-4079ba60ec35 | -11.14482 | -44.47771 | 2026-08-25 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 63.3 |
| b2782060-0854-3b8c-8c5a-7142783dd8c7 | -9.98141 | -48.31684 | 2026-08-25 04:08:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f3aa137-edae-3b03-ab78-d168ad425ff8 | -11.97745 | -45.90392 | 2026-08-25 04:08:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d2e45b3-0d1f-30c4-a398-df18137d6525 | -11.43671 | -44.52613 | 2026-08-25 04:08:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 52ae1e33-a29f-3518-ab22-2416c835a1ae | -11.43213 | -44.55238 | 2026-08-25 04:08:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78d797b4-3d9d-38dd-8038-982f400e4b9c | -10.87105 | -50.58762 | 2026-08-25 04:08:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70065fec-cca2-33ba-9679-8b73158367db | -12.74845 | -46.45677 | 2026-08-25 04:08:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7de140bb-96fb-356f-98e9-37d2ffc01ed8 | -8.6606 | -47.32283 | 2026-08-25 04:08:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e5e0d89-8581-3e1e-84eb-0b2b5285914e | -11.9917 | -45.93114 | 2026-08-25 04:08:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 51f8f591-6973-3324-90fe-4148927a2e60 | -11.97313 | -45.90308 | 2026-08-25 04:08:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8593d0e2-4d41-389e-80db-fecd51fe5410 | -14.00465 | -44.04826 | 2026-08-25 04:08:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 64464551-2e6d-3086-86ba-b0c21c905891 | -11.98744 | -45.92306 | 2026-08-25 04:08:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 860a3ecf-ec71-3c3f-8bcb-8a508bcf8f30 | -12.78488 | -44.27376 | 2026-08-25 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c0a0165a-7a93-33e0-85fe-33fc8f929b69 | -8.39083 | -44.77099 | 2026-08-25 04:08:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2cc9a9d8-5c20-39f9-803e-f497976e101f | -10.47616 | -50.44268 | 2026-08-25 04:08:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3ea7f253-79a1-383e-82c3-60052c3981f8 | -12.75181 | -46.45675 | 2026-08-25 04:08:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 58b29ede-8b32-3ceb-a8cb-c397e79a0c39 | -12.71839 | -48.38605 | 2026-08-25 04:08:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c1693b6-32d8-3212-84c7-e3d185fb93f5 | -12.86627 | -48.49668 | 2026-08-25 04:08:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30444f93-2f45-30f1-a475-bf4ec96c313b | -10.48301 | -50.43945 | 2026-08-25 04:08:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1958db0e-c6bf-3984-b5c1-0cf6b9f96a11 | -12.25906 | -43.11315 | 2026-08-25 04:08:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7481759d-3edb-36ac-a826-a59d817a54d1 | -12.75233 | -46.43526 | 2026-08-25 04:08:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b42c4ef-f17f-3ee0-8287-4fe2d1eb3561 | -12.75518 | -46.44479 | 2026-08-25 04:08:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1fd1ca22-abef-3545-bf62-79d7b25a3f0e | -9.82709 | -44.89261 | 2026-08-25 04:08:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 172a9c19-303c-3f3f-ad69-b81dede47c54 | -12.74504 | -46.47576 | 2026-08-25 04:08:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 550d741b-b1b7-3572-b260-e3692797b65f | -13.42213 | -40.26659 | 2026-08-25 04:08:00 | NPP-375D | LAJEDO DO TABOCAL | BAHIA | Brasil | 2919058 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cad1950e-f9e4-3096-a557-2c1253f882aa | -12.78273 | -44.26332 | 2026-08-25 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 81b10e67-bf4f-3705-b32b-aa4f3610a8bd | -8.56974 | -47.43404 | 2026-08-25 04:08:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bb75b1d2-b984-3c55-8889-770714783c0a | -12.73259 | -46.46864 | 2026-08-25 04:08:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 42051ac7-3df3-3a47-8674-8365f6119915 | -8.10135 | -47.46832 | 2026-08-25 04:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 580baa11-a519-3492-8885-2f4e665a3c72 | -12.70928 | -48.39681 | 2026-08-25 04:08:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 15770904-f9c6-3662-9160-bcfc1e3ede72 | -12.45209 | -43.40342 | 2026-08-25 04:08:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a0cadc39-c47e-3ee9-a10e-fbe6c63ee620 | -8.15972 | -46.70442 | 2026-08-25 04:08:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a7ad107-0673-3a5c-8e27-4c95d2a25380 | -9.95895 | -48.3205 | 2026-08-25 04:08:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 504207ef-8fc6-39f3-abca-cfd904c050a3 | -11.58909 | -46.75834 | 2026-08-25 04:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8bdf86b3-e476-3fe1-b259-794e5da63064 | -8.15808 | -46.69998 | 2026-08-25 04:08:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 805f5532-1f4f-3aeb-9859-bceaad09e71a | -9.53239 | -49.27144 | 2026-08-25 04:08:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25157357-ca65-3114-870a-55282af8e67d | -9.65221 | -48.3214 | 2026-08-25 04:08:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b111494-36db-3a37-9210-d1bedd9985e6 | -14.00092 | -44.04758 | 2026-08-25 04:08:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a5f91ef4-af8c-3d3c-8ff5-a947eaf4b159 | -7.90572 | -46.36002 | 2026-08-25 04:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9812d166-5980-3f80-8cff-c1981e8ccdb4 | -12.75508 | -46.43929 | 2026-08-25 04:08:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ff0d4bd6-5d9c-3e71-9b9a-c31f941d8d1b | -11.98182 | -45.91202 | 2026-08-25 04:08:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ba0fb9f-2ffa-387f-adb8-d15fc80816a5 | -10.91809 | -51.07433 | 2026-08-25 04:08:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e70738d6-277c-38b0-bebd-10a4c4c98f40 | -11.8869 | -43.82541 | 2026-08-25 04:08:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |


[Clique aqui para ver as próximas entradas](README23.md)
