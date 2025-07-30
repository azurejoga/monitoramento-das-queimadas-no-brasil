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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 45098a98-2628-3c7f-b986-366c6e79f388 | -5.68096 | -43.68273 | 2025-07-30 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2431542-1020-3267-b42b-5656767d3c30 | -9.05233 | -45.07251 | 2025-07-30 04:27:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6210387-085f-3c73-958b-344339735d50 | -6.3766 | -53.33001 | 2025-07-30 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d61df2e2-aab0-3267-a461-e990235edbf4 | -7.3692 | -43.76558 | 2025-07-30 04:27:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e2a73b5c-edfa-373f-bd87-91f0ce9578a6 | -6.40602 | -53.36692 | 2025-07-30 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2b58c043-97ee-3dff-8530-0e154cf604c0 | -6.46404 | -44.57397 | 2025-07-30 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 64311dbc-32fc-3881-ba2d-2c14c33d7ba4 | -9.75268 | -37.00266 | 2025-07-30 04:27:00 | NPP-375D | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 33fbfa01-e36a-3a53-ba3f-4c95172ceeec | -7.0903 | -40.60225 | 2025-07-30 04:27:00 | NPP-375D | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d2c56056-9277-391e-8877-55fa975cfbac | -5.756 | -43.94339 | 2025-07-30 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54b6d759-185a-3541-b3ef-98ff75e5afba | -7.85878 | -46.73375 | 2025-07-30 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 124519c1-2f71-33e1-bd60-1f7feba51c0e | -8.95347 | -46.74472 | 2025-07-30 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83516375-36cd-350d-b2f6-35ce8a2c012a | -9.14939 | -49.84503 | 2025-07-30 04:27:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 39d50200-d630-3be8-8ac4-ba382bf6b72e | -2.91977 | -48.67255 | 2025-07-30 04:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c6029754-851f-345e-907e-7e9b3df46e9e | -6.95859 | -56.38313 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d2b1764d-b138-3775-af69-57c99bb3623a | -8.62431 | -45.88548 | 2025-07-30 04:27:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a8021cfe-8046-306e-9823-df0bab5c48e3 | -10.46142 | -46.73037 | 2025-07-30 04:27:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2bf7cbe5-1fda-3ac1-ac43-cb09505e27e6 | -9.04578 | -45.07216 | 2025-07-30 04:27:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f84d27a-d6c3-35bf-be4d-6a703dbe52a3 | -4.19242 | -49.36412 | 2025-07-30 04:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d2c08af-bc01-37ee-9a97-b9f5382b55fb | -7.10489 | -44.96435 | 2025-07-30 04:27:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79b9e4b9-2725-319d-a7bf-80eee2e7d1bf | -3.94918 | -41.48458 | 2025-07-30 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e80e840e-2cf3-30da-8b33-225b7fc40a35 | -4.65414 | -43.12171 | 2025-07-30 04:27:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| ae35d41c-e422-3a7a-86e5-8a2c10067a55 | -9.22854 | -50.04561 | 2025-07-30 04:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b64d6d34-182a-3845-8861-2e5bd7c58557 | -10.62503 | -45.23668 | 2025-07-30 04:27:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0a51df54-2403-3dcc-9a22-dc24ff3873ec | -6.5627 | -56.18498 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f4d849b-6b50-3c84-8dac-8ab496029c92 | -6.61725 | -44.04674 | 2025-07-30 04:27:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0815b82-a2dd-3401-afd8-68a8e6c700b5 | -2.91337 | -48.24238 | 2025-07-30 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eb9ddd72-4b13-3585-9360-f73f3ad29933 | -7.08482 | -42.14958 | 2025-07-30 04:27:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9ab79c06-2381-3727-a505-fb2034ab6267 | -10.61473 | -45.23508 | 2025-07-30 04:27:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fed258cf-b505-3f33-93cf-fb8009c0fd1f | -4.05516 | -48.83045 | 2025-07-30 04:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b55e9b12-c98d-38f2-a95f-951126f42f58 | -10.61873 | -45.23186 | 2025-07-30 04:27:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e14f95cb-97f6-3ea1-bffa-c780181579c3 | -5.75938 | -43.96709 | 2025-07-30 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c058780d-4006-3dde-99d9-83832cebe9b8 | -2.90204 | -48.24472 | 2025-07-30 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 404a6e77-cd5d-3b40-aefe-fc8f7eabd286 | -7.93597 | -44.08921 | 2025-07-30 04:27:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 61227ad7-0d8e-3288-99ef-1c8e01bc6c2f | -8.51682 | -43.31547 | 2025-07-30 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 33.8 |
| 76aa253b-c27c-360e-8e11-873553a8dde9 | -2.9191 | -48.67675 | 2025-07-30 04:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f06b5e4a-9d95-3615-b350-1b43b9acc0d2 | -5.68504 | -43.67945 | 2025-07-30 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3659ea8-0621-3557-be6e-05674ec63bbf | -4.06786 | -48.26099 | 2025-07-30 04:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de790b72-8db6-36cd-88b1-ce3bb6dd2515 | -9.17839 | -48.84677 | 2025-07-30 04:27:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ce613430-b00d-3ce6-9da8-79cc9117330d | -6.71009 | -44.3574 | 2025-07-30 04:27:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb50b1d3-195d-3d85-9a4a-4115c862dca5 | -7.1569 | -44.04409 | 2025-07-30 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 299d8a6d-e8ac-3c8a-b7cb-6df85a78bf90 | -3.29921 | -49.19625 | 2025-07-30 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53dea2ec-6a60-354f-941b-656a07a98fb2 | -5.75997 | -43.96334 | 2025-07-30 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc92ba0a-0b3e-31e0-9d63-6e3da9fadaad | -9.57199 | -43.88055 | 2025-07-30 04:27:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 47167347-1b29-335f-bb73-5e32cbf1914a | -7.13363 | -44.3472 | 2025-07-30 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb05e858-a594-3bb6-bc32-4a66c85d1c09 | -8.03353 | -46.91179 | 2025-07-30 04:27:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 49855b0b-7e7b-3a49-9042-6ed5c710d18f | -7.14051 | -44.37146 | 2025-07-30 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2796c318-520b-3073-a048-0031c08860cc | -5.40875 | -44.42511 | 2025-07-30 04:27:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d7ba950-616e-3e4f-9bab-8b66dc990dbc | -9.1918 | -43.15435 | 2025-07-30 04:27:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d452dd8f-db99-3b89-83ec-bca5fdf9e569 | -5.2419 | -45.21747 | 2025-07-30 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1fd44c38-400e-323a-866e-e2d6fe61535f | -6.25149 | -44.07483 | 2025-07-30 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ea4cadbd-f491-35f5-af5b-1a108e9e9ac3 | -8.6394 | -45.50937 | 2025-07-30 04:27:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16584071-bd4d-3556-9dfd-8574c258ad4c | -10.61816 | -45.23562 | 2025-07-30 04:27:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 62c2d216-124e-3fee-939a-d70efe7892bc | -6.56204 | -56.18874 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 816aaf6e-dc90-3b69-9982-96aaca8dd888 | -4.59926 | -43.31446 | 2025-07-30 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e6b66b88-a3d8-3409-8eb1-c0138b893c39 | -9.23304 | -50.04497 | 2025-07-30 04:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 190da9ad-2439-361f-b791-e3263c097b0e | -7.28544 | -44.54208 | 2025-07-30 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b41a7624-4aef-3f35-a8dd-d90969db8b36 | -9.59547 | -43.84621 | 2025-07-30 04:27:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 76da9319-33c4-3a19-9526-185e95f9afdc | -2.94707 | -48.0518 | 2025-07-30 04:27:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| acfc4b3a-f3a7-3a67-b0d7-276d87fdb1c8 | -4.65353 | -43.12568 | 2025-07-30 04:27:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 670f87b2-af8a-3769-946f-1a1c2c96d8b2 | -6.3911 | -53.3576 | 2025-07-30 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 90d281ac-b9e1-31af-af68-6f2b1adb36de | -5.48106 | -42.15364 | 2025-07-30 04:27:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d6b2a29a-f37b-3763-9cd4-f4c4e370253a | -3.1116 | -47.00877 | 2025-07-30 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 15e07f52-a514-393a-a642-cffdb909641f | -6.52642 | -43.33487 | 2025-07-30 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3dd4606d-4720-3483-bee0-85ab6e0417e4 | -8.95292 | -46.74821 | 2025-07-30 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2385082d-7496-3165-996a-f9140211d05f | -3.99565 | -43.23103 | 2025-07-30 04:27:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2dd88138-c59b-38b6-a87b-9d0a15a7c373 | -6.54324 | -56.1968 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d0e2087a-d7ff-3c94-b28f-4512f0361c0a | -8.63604 | -45.50883 | 2025-07-30 04:27:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b816dc73-836c-3d12-ab38-f0733b2222d9 | -6.47971 | -41.62978 | 2025-07-30 04:27:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d5881803-8eed-395d-899e-272e51f31712 | -3.27791 | -49.13839 | 2025-07-30 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a87c7219-1815-3988-b56b-85d7284ecdce | -9.0218 | -47.97832 | 2025-07-30 04:27:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af36057a-bc01-3d5b-af3f-61bb088ec7eb | -7.77661 | -45.00003 | 2025-07-30 04:27:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 47e0afaa-2fd7-3143-b0a5-d67635d664be | -3.0343 | -47.86498 | 2025-07-30 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 963277c2-b38a-3bd5-a488-d8daf72c4889 | -5.06298 | -43.72455 | 2025-07-30 04:27:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 88bc6cdf-6bf7-3316-87c7-0a04aa83af13 | -7.11822 | -44.47135 | 2025-07-30 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2a4739f-577d-395b-bce5-e05bd3d32f28 | -6.38126 | -53.33079 | 2025-07-30 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 503e8334-aad5-3099-a5c3-a855b5609d21 | -7.13823 | -44.36327 | 2025-07-30 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3972b883-6c7b-351e-ad28-6944a075a6c5 | -7.1563 | -44.048 | 2025-07-30 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fba40a1d-acf0-3e52-ad64-789216127dde | -6.62275 | -59.9848 | 2025-07-30 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2fe79b57-b352-3bcd-aa10-da6e00af6783 | -8.62875 | -45.87888 | 2025-07-30 04:27:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 7d5f4b5a-042e-3b3c-b332-f8a867dca16f | -10.42739 | -47.24953 | 2025-07-30 04:27:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f833abaa-df98-3e4b-9f0a-4ced50428e2e | -9.58151 | -44.44691 | 2025-07-30 04:27:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d78b2e4-6b85-34a4-a484-42b1a6681a61 | -7.15773 | -44.04731 | 2025-07-30 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d3bc487-31a0-3323-bb26-d84499a2a1fd | -2.80935 | -48.66471 | 2025-07-30 04:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ac7ea4c-d2f3-3d84-8291-5cb325cae390 | -7.10509 | -44.37802 | 2025-07-30 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b9b080c-404b-35e7-b130-6e6c11a44ec9 | -6.50053 | -56.20856 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b80e81a-91ce-346c-9710-8a07d5cd44ad | -3.03868 | -49.42673 | 2025-07-30 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8722f1bc-dd86-399c-ba7f-54a2a7c182c1 | -6.50817 | -56.19827 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 283eb981-73c6-3c26-84bb-f85d6d84d40c | -10.61359 | -45.24258 | 2025-07-30 04:27:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| d472536f-800c-3491-a400-5f478f0ba4b4 | -9.57809 | -44.44483 | 2025-07-30 04:27:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 59d80d6d-5cde-38ad-9b43-2f9c76663087 | -6.70093 | -44.34842 | 2025-07-30 04:27:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 369ed376-14ea-3425-98c1-03778a36cde7 | -6.12189 | -43.96241 | 2025-07-30 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62f6da49-b8f9-3c12-8984-f4a947acf49a | -6.24343 | -44.82541 | 2025-07-30 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b459f4e-ffa3-3e7b-a82e-66f3828f5b75 | -10.51286 | -44.89135 | 2025-07-30 04:27:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 09b7e099-bcfd-3734-89aa-f34c9250b0a4 | -9.57801 | -44.44633 | 2025-07-30 04:27:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 872107a5-1e07-3a4c-8571-9e7975f23cb8 | -6.54724 | -56.1885 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a03e2e60-2f12-3b99-b81e-0eb6dd568207 | -4.59047 | -47.98077 | 2025-07-30 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af21bc09-8b74-333f-8221-518c447e1103 | -6.4124 | -53.35785 | 2025-07-30 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b511b4aa-c459-3bb0-8cdd-33c9541557cf | -5.79782 | -43.62845 | 2025-07-30 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 127838cf-0de4-3874-a6b2-3e5543748226 | -7.11879 | -44.46764 | 2025-07-30 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d2ed075-d752-3607-a1d5-2dc0379e29a9 | -7.06432 | -44.95813 | 2025-07-30 04:27:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README19.md)
