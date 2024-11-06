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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b6ad2ecc-aa09-3ea4-9406-7379e907411d | -4.6068 | -48.0653 | 2024-11-06 03:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0e739f4d-1c7e-3afe-a8bf-05f3a3859a2b | -9.04759 | -38.23704 | 2024-11-06 03:49:00 | NOAA-21 | PETROLÂNDIA | PERNAMBUCO | Brasil | 2611002 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 168266ff-882a-3f2b-b764-6ff6a1d5c84f | -2.84268 | -49.48138 | 2024-11-06 03:49:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 25c2682f-307d-3b02-bad9-60a7290d54dc | -6.12897 | -43.97821 | 2024-11-06 03:49:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 2ef063a5-4a86-3b53-b2d1-c59c69617f43 | -2.81647 | -48.55637 | 2024-11-06 03:49:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ec88e0a-c2c4-36de-8678-5c63d9d84ba8 | -5.64627 | -40.14449 | 2024-11-06 03:49:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 17e680a5-bccd-36b3-91e1-0fd4a65e9156 | -3.95558 | -48.15012 | 2024-11-06 03:49:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4d0cb8a7-bc74-3937-9a04-d528cd2c5e22 | -6.5135 | -41.42471 | 2024-11-06 03:49:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| caa8d5c9-f8a4-32f7-b424-4bbfd793ac59 | -6.50834 | -44.67633 | 2024-11-06 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 25bff356-1b82-3ed8-8507-fe94b40a76c7 | -7.82485 | -35.23976 | 2024-11-06 03:49:00 | NOAA-21 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 6eca3836-4f3f-3bc8-801c-bd0a47a9427d | -6.48225 | -44.68284 | 2024-11-06 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c268a6db-556d-3b79-8f6d-47b659001da1 | -7.43869 | -42.88667 | 2024-11-06 03:49:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 391182fa-246b-3088-a80b-f7ce193f270f | -7.65038 | -38.99403 | 2024-11-06 03:49:00 | NOAA-21 | JATI | CEARÁ | Brasil | 2307205 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 2cc65a43-29a6-3bab-813a-20bc36c6a75f | -7.54472 | -42.85151 | 2024-11-06 03:49:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cd4ad859-f8af-368b-bee3-1bb96e62ad12 | -2.85124 | -49.47918 | 2024-11-06 03:49:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 964d762c-e9cb-36e3-802c-1116dc568a99 | -2.84383 | -49.47475 | 2024-11-06 03:49:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| d9296ba1-2fe3-3d15-b562-9ccf1db3cbc7 | -4.65545 | -43.82302 | 2024-11-06 03:49:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 42113069-99f5-30d4-b906-e6bd40c1ac1a | -7.32317 | -39.14948 | 2024-11-06 03:49:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b1e1c611-de4c-30ab-acee-c9e4e09d1c7f | -7.49148 | -35.10244 | 2024-11-06 03:49:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f4597347-d460-3eb8-9b63-bed520b5e124 | -3.71746 | -49.43033 | 2024-11-06 03:49:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a831367b-3041-3579-826e-646b31083f8f | -11.06415 | -38.43733 | 2024-11-06 03:49:00 | NOAA-21 | RIBEIRA DO AMPARO | BAHIA | Brasil | 2926509 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e6698111-96da-3c13-8c77-16b78bf54099 | -6.93149 | -47.78646 | 2024-11-06 03:49:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a38ed19d-8507-376f-8eef-d24fbe19b40d | -6.77331 | -37.5355 | 2024-11-06 03:49:00 | NOAA-21 | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f53fa033-1087-30b4-9226-534350aa2ea6 | -5.62841 | -44.17877 | 2024-11-06 03:49:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 833c7dae-9c46-3915-a3d2-51920a05e037 | -4.35373 | -46.53372 | 2024-11-06 03:49:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b8c89ec5-c27f-35c4-9911-97b68e35a10b | -9.87022 | -44.97454 | 2024-11-06 03:49:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 04c57343-4fad-387e-9098-347ed2f5f7c5 | -6.4983 | -47.49932 | 2024-11-06 03:49:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| dbcae0ca-6a4b-357e-b29b-ba124ee30793 | -3.75965 | -47.60596 | 2024-11-06 03:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 51a706f4-6d4e-3605-b6b6-ab3d85d679c4 | -6.12676 | -43.98155 | 2024-11-06 03:49:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 47cd71dc-ed83-36ed-8fac-547e93bb166f | -4.62807 | -42.81162 | 2024-11-06 03:49:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 29a13c06-b89f-399b-9b2c-0205c62ba4dd | -6.05109 | -39.43332 | 2024-11-06 03:49:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 1d6f6ecd-b7f2-325b-8293-ccb77694b6f1 | -6.48708 | -44.68378 | 2024-11-06 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| ae8ef9a8-6d40-33ea-b864-b6b74f3a9c0d | -6.51129 | -44.68824 | 2024-11-06 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 911eeb59-d073-39ea-9a8f-5c3cf4891ec7 | -4.13527 | -43.58241 | 2024-11-06 03:49:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| f2e0761d-99b4-3f69-b23b-4f58f348a845 | -2.82764 | -49.77772 | 2024-11-06 03:49:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 00ac484a-ecfc-3498-8061-1718b021131d | -7.33471 | -35.07236 | 2024-11-06 03:49:00 | NOAA-21 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7892ce99-aa9a-3313-a042-82d2e6665794 | -6.49944 | -47.49864 | 2024-11-06 03:49:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| be573868-d0c0-3830-bc2c-bedd54dc3629 | -5.47735 | -44.85885 | 2024-11-06 03:49:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86d0ceb9-f8c7-30eb-bdaf-c669466b1ace | -3.06919 | -47.77503 | 2024-11-06 03:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 42fbb47f-8010-3298-8879-face437f40fb | -3.95465 | -48.15548 | 2024-11-06 03:49:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7455902-a922-3d3f-b530-b11ce48efaf5 | -3.75093 | -44.56786 | 2024-11-06 03:49:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4fbd78b9-2817-3509-bdbf-6524e6920078 | -6.62525 | -41.65221 | 2024-11-06 03:49:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 3dc39ba9-b66a-3a0b-a35f-f594a08b08df | -8.50908 | -42.09428 | 2024-11-06 03:49:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6b2443a8-dbff-304c-a1a2-33b0a369e89b | -6.08792 | -44.77931 | 2024-11-06 03:49:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4eafdc18-5a41-39e7-89f1-8e707a461c61 | -10.26179 | -36.50792 | 2024-11-06 03:49:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ed0a1b96-d2ec-3241-8d4b-44a60bfff104 | -4.69268 | -45.64924 | 2024-11-06 03:49:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8cde6928-6e2e-3335-87f7-145024c889b2 | -8.49859 | -42.10858 | 2024-11-06 03:49:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 5f434f03-c314-3a36-a070-13dfc07a7076 | -4.62743 | -40.17965 | 2024-11-06 03:49:00 | NOAA-21 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 435fa702-2c66-36a9-b108-471a3c33b1c1 | -5.98786 | -45.3685 | 2024-11-06 03:49:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 0fc766d2-9b92-386d-a70b-bbc1bdf477d9 | -6.11114 | -43.97042 | 2024-11-06 03:49:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 51.5 |
| a12c9da5-b14d-3f69-8458-bd2e3ba3e789 | -7.4949 | -35.10297 | 2024-11-06 03:49:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a723e463-3639-3b60-9a3c-0d5e731549db | -4.1296 | -43.57268 | 2024-11-06 03:49:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 30e37344-3c6e-3abf-872e-43e7afb05ab2 | -5.94164 | -43.77415 | 2024-11-06 03:49:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 29d9ee30-c0e8-3081-a1f3-936bafd85ef9 | -7.43936 | -42.88277 | 2024-11-06 03:49:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| ea3bf967-3c67-3901-a69e-ef8182a89d5a | -6.6444 | -37.38018 | 2024-11-06 03:49:00 | NOAA-21 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1e249a31-8903-3bbc-ab3f-35a16326abc5 | -4.13186 | -43.58834 | 2024-11-06 03:49:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 90e49ad7-8b10-31a2-8a0c-759408d0bacc | -3.2163 | -50.391 | 2024-11-06 03:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 8688309f-58d3-32d1-9f14-6922923177ac | 3.6184 | -51.3162 | 2024-11-06 03:50:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 43.3 |
| dca71e16-024a-30e8-9dcb-dde5bc7c8671 | -6.4906 | -44.6862 | 2024-11-06 03:50:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 20b9e1dc-000a-37a2-8e08-761fa5a5ff80 | -6.1041 | -43.9593 | 2024-11-06 03:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 44b5066f-877f-31fd-bff3-b9f4b462f98a | -4.1246 | -43.5833 | 2024-11-06 03:50:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 157.6 |
| 1d0ff6be-6910-3f32-a8af-5b5fb78b49ea | -3.0396 | -53.2805 | 2024-11-06 03:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| dfb32acd-274e-3155-bc94-a747b2177e35 | -3.2348 | -50.3904 | 2024-11-06 03:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| ab8de3f0-9cc5-3701-b332-14d05bd305d4 | -3.1617 | -50.2038 | 2024-11-06 03:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 1c8bca2a-896f-37df-8975-aba71d9e9022 | -3.5446 | -47.3855 | 2024-11-06 03:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 188.7 |
| 70e5a268-a563-3883-8f1c-426db0a15415 | -2.7243 | -54.1552 | 2024-11-06 03:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 6b296973-73d4-35fb-a48a-b76e7c04c88e | -6.4827 | -47.4827 | 2024-11-06 03:50:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| c0e86d3a-a537-355b-957b-e69b75838f4c | -2.7244 | -54.1351 | 2024-11-06 03:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 4f7088f0-32f4-34f8-8e4f-4eeb14eda1bc | -2.8608 | -51.7731 | 2024-11-06 03:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 149.3 |
| 55fc01d0-c8ae-3cc8-9d04-7f3323a2d66c | -1.2922 | -54.5585 | 2024-11-06 03:50:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| f3f8e8dc-4663-38ed-949f-be40c4ff7acc | -6.5014 | -47.4813 | 2024-11-06 03:50:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 266e4945-25df-3510-b414-a4f150280109 | -2.8506 | -49.4744 | 2024-11-06 03:50:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 8172b2b9-aa7d-3f3e-ad8d-3a02b5786ad5 | -3.0207 | -53.443 | 2024-11-06 03:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 095cf670-0ff6-3ca5-b6eb-38f3ff75a6bb | -3.5631 | -47.3847 | 2024-11-06 03:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| c885d0ce-f896-3d01-a30e-8dae30694db2 | -6.4825 | -47.5046 | 2024-11-06 03:50:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 7ff4361b-c67b-391b-8390-877105b675e2 | -6.1226 | -43.9809 | 2024-11-06 03:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 68f6fc49-a22f-33fc-a86f-c1df371c4073 | -6.5094 | -44.6847 | 2024-11-06 03:50:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 3e128a28-f530-381f-80b0-10aadf3cfb32 | -2.8607 | -51.7937 | 2024-11-06 03:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| fb550eab-e4ac-3be6-a1be-0d0eb5ab1b6b | -2.6764 | -51.8189 | 2024-11-06 03:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| e74da7cc-5550-3590-8039-ffda688a70a2 | -2.9371 | -51.0465 | 2024-11-06 03:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 656b5ef1-f98c-33c0-afc8-b41227da4366 | -3.2164 | -50.3701 | 2024-11-06 03:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| ff2a2aa6-171d-37d4-afb4-69c2901a9186 | -4.1432 | -43.5822 | 2024-11-06 03:50:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 42f46276-45c6-3f38-aac4-ee687de769f6 | -3.0397 | -53.2603 | 2024-11-06 03:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 5fcb0992-991a-3c81-bcc8-911dcacddf39 | -2.8423 | -51.7942 | 2024-11-06 03:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| d91cb135-93ec-370b-821b-7178322df0f9 | -3.0207 | -53.4227 | 2024-11-06 03:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 602a73f7-afc1-3292-bbab-7c8ef3997b62 | -2.8423 | -51.7735 | 2024-11-06 03:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| f0c180fc-0363-3bab-9703-30bf2bf2a4fb | -3.5447 | -47.3636 | 2024-11-06 03:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 88ee452a-dd82-39c1-9d5c-4bfe3af77f85 | -2.9186 | -51.047 | 2024-11-06 03:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 30682b91-807f-3cf2-af9a-d6985b59c382 | -3.967 | -48.15 | 2024-11-06 03:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| a471c383-845a-3fac-b5f0-e997d804cd78 | -6.5012 | -47.5033 | 2024-11-06 03:50:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 440c16a2-20c9-32c4-be1f-d2d2aeef7baa | -3.526 | -47.3862 | 2024-11-06 03:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| aeb52540-cc5f-33e5-9968-0a7e4468b513 | -2.937 | -51.0673 | 2024-11-06 03:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| a79e0fc9-dfce-38ff-a2ff-f1888fdd3bad | -3.1616 | -50.2248 | 2024-11-06 03:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 2fdc885a-012c-3afe-8fdd-675798e4a9fa | -3.2349 | -50.3695 | 2024-11-06 03:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 65871d53-0823-3103-b737-d0327a855468 | 3.6 | -51.3168 | 2024-11-06 03:50:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 62977f76-00e1-3cb6-b936-b4a12ffb7dd5 | -13.47865 | -42.22401 | 2024-11-06 03:51:00 | NOAA-21 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 08975590-26cd-3334-89c8-9f21b3b5a598 | -11.13455 | -44.95044 | 2024-11-06 03:51:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5bbc6ad0-c552-3ccf-a198-3cb26b24cd34 | -12.1624 | -44.62587 | 2024-11-06 03:51:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eb4d8eb6-a747-31e8-a428-156233d0d12e | -12.12459 | -39.40419 | 2024-11-06 03:51:00 | NOAA-21 | SERRA PRETA | BAHIA | Brasil | 2930402 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c9a074fc-0b8d-35ea-8de5-0609274b74b5 | -13.57435 | -43.65887 | 2024-11-06 03:51:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README28.md)
