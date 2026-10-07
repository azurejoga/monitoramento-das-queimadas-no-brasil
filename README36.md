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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa9f9cfb-646d-3425-86a3-d1012d25613f | -6.37231 | -42.91171 | 2026-10-07 04:00:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.8 |
| b483bf4f-aa7d-3d03-9ed9-1e9c58a53101 | -3.80798 | -47.49079 | 2026-10-07 04:00:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 92152192-72f6-3c05-9885-2c339025f7f4 | -6.59441 | -41.55555 | 2026-10-07 04:00:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 25b142df-11dc-30f8-9010-6af4b0ac96dc | -5.7212 | -41.68657 | 2026-10-07 04:00:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e35e2163-4d7c-378c-9c79-3dddb2e01bd1 | -5.72034 | -45.15461 | 2026-10-07 04:00:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d3cae7cb-2768-381f-a03a-e3301b12bcc8 | -3.47943 | -50.08959 | 2026-10-07 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0e9e7175-ae81-372c-aae1-63d6bdd0e3e8 | -3.46616 | -50.07997 | 2026-10-07 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ec4cfbe7-e42b-3f15-bf58-94ee5bd17f4e | -3.80717 | -47.49546 | 2026-10-07 04:00:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 837fc9d2-3945-3be5-a2f8-4fef5b5951ac | -5.02917 | -44.71016 | 2026-10-07 04:00:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fb93e997-2799-3ac1-ad96-4b2374a1fe0b | -3.3614 | -43.39441 | 2026-10-07 04:00:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c247cae-e33e-3c81-9eba-e13f40186b9b | -5.97295 | -40.93297 | 2026-10-07 04:00:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| e362cf83-5758-3ce8-9d40-e1c97c5c74f5 | -4.35518 | -47.77623 | 2026-10-07 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b04de29-a49a-3c16-82c9-319944198d2a | -5.73419 | -45.16678 | 2026-10-07 04:00:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4ca33e17-a419-3ab1-94c2-ebb6a5db2a0a | -5.72361 | -41.66484 | 2026-10-07 04:00:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4e2d4ea9-1f7a-30cc-b152-8f714412332e | -5.74005 | -43.27623 | 2026-10-07 04:00:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f3e9b376-d70f-3450-9ae8-01eca811a5cd | -5.74989 | -43.27332 | 2026-10-07 04:00:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b9c30605-511b-36f5-9eaf-6309544b3b7c | -4.45673 | -47.91969 | 2026-10-07 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 492df8dc-d4c7-39bf-b2be-4fb4226ef5d2 | -3.3895 | -42.71159 | 2026-10-07 04:00:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1966bbc-5b32-3d12-a9ad-5bf30c620cbf | -5.06033 | -44.86513 | 2026-10-07 04:00:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5678c0d7-a277-35bc-9def-b4ff87fe5d0e | -5.10712 | -45.88478 | 2026-10-07 04:00:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11f9cf2c-53bc-3eb4-b714-20fff47142ab | -5.74458 | -43.27707 | 2026-10-07 04:00:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 3b5782be-d435-3dd6-8148-647e959edfe8 | -6.18816 | -35.30116 | 2026-10-07 04:00:00 | NPP-375D | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 809d6593-a847-3eb3-8781-1947bbea596a | -3.11753 | -44.35189 | 2026-10-07 04:00:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d40d16b7-5f8c-32cf-81c9-9f0b5bf3726e | -3.81254 | -47.5013 | 2026-10-07 04:00:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9d3dfea-4325-3590-9a3d-4084a4bdbab3 | -6.59527 | -41.55038 | 2026-10-07 04:00:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7bac4b74-e5ee-3864-85fb-03162a32c043 | -3.28124 | -50.14708 | 2026-10-07 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b4ac5f28-244a-3af0-83c9-781ed93d3eef | -6.84902 | -41.77292 | 2026-10-07 04:00:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 66983ca3-98e1-30cb-984d-d15f200738a9 | -5.72792 | -45.17221 | 2026-10-07 04:00:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 4da84792-74d4-3a0b-98ce-5fb07cad9206 | -3.2753 | -50.13832 | 2026-10-07 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| dccb9130-16a5-34eb-a448-e2e4dd20ebe3 | -6.88556 | -42.22264 | 2026-10-07 04:00:00 | NPP-375D | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7dbdd5f8-3572-39cf-9dbd-193617123b14 | -6.37329 | -42.90955 | 2026-10-07 04:00:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b6b4a804-a679-37f5-960d-15f6a5b42ace | -5.73364 | -45.16994 | 2026-10-07 04:00:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 29aa6d45-5b4c-31c1-bd12-873eb34854fe | -5.96988 | -40.92752 | 2026-10-07 04:00:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 940ba062-18bc-31f5-b186-b06b1d2b1f49 | -6.92407 | -41.23104 | 2026-10-07 04:00:00 | NPP-375D | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f4e7dc68-71f1-397d-ab9c-c1aecfdfd4fd | -6.01888 | -42.26384 | 2026-10-07 04:00:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 91766a03-affa-3c18-bb76-c2c3ebc9996f | -5.02172 | -45.53028 | 2026-10-07 04:00:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be74bcf6-337d-3651-be10-9cedbfcf9857 | -3.48798 | -50.08987 | 2026-10-07 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33b8e1b0-6b5d-3f08-b0b4-136f6ed4d0b5 | -4.3606 | -47.78222 | 2026-10-07 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c1f9998c-cfbe-3202-8c18-1be1b5524bf8 | -5.97824 | -40.94886 | 2026-10-07 04:00:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| ada8601c-d3df-3a89-8b31-30e44d16c76f | -4.44957 | -47.92355 | 2026-10-07 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 4e188c58-fe33-3fdc-8953-ab45724f0b72 | -4.24039 | -42.66073 | 2026-10-07 04:00:00 | NPP-375D | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 626a0546-23c0-3ab8-b83a-44b6741d33f5 | -5.69149 | -40.88908 | 2026-10-07 04:00:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 36d798a3-daf6-3d9c-bc80-ef0704c0aba5 | -4.02371 | -42.47507 | 2026-10-07 04:00:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3f6db134-709a-3028-8376-158f5c5046f4 | -5.78081 | -41.92788 | 2026-10-07 04:00:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8aa67371-cfe3-374a-857f-53929904684e | -5.74537 | -43.27242 | 2026-10-07 04:00:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a6e0cea2-c8cc-3b5d-8427-7617af5627d5 | -5.2752 | -43.36393 | 2026-10-07 04:00:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| df62a0f3-11c5-316f-ba4b-966c6b06741f | -3.27394 | -50.14579 | 2026-10-07 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 0f4a738f-e2e6-3d9f-bb92-0303dd03b83c | -5.72603 | -45.15247 | 2026-10-07 04:00:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 63c87dcb-6bb8-36f9-8da9-02c0ae27a0c3 | -6.84082 | -41.79689 | 2026-10-07 04:00:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c6e8363d-83b2-3ac3-b6c5-703760c3fbf4 | -6.4286 | -43.72062 | 2026-10-07 04:00:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 264d1b02-9bb2-34b2-9352-1736cc098fd4 | -4.02813 | -42.47581 | 2026-10-07 04:00:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 960c795b-8bd9-324f-918b-6c33828194ab | -5.73011 | -45.15963 | 2026-10-07 04:00:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| e1f01ea9-febb-3bed-aba3-bca85e110019 | -5.73474 | -45.16361 | 2026-10-07 04:00:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9ac094a0-f54f-3fd9-b31b-676424a98824 | -3.28119 | -50.14385 | 2026-10-07 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 85f584ed-f5c5-349e-bf59-29bdb0a0e01a | -5.72439 | -45.16189 | 2026-10-07 04:00:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 82bf6ef7-87f3-36d4-8eaf-6b03d359bea8 | -5.29382 | -42.75385 | 2026-10-07 04:00:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 17b5095c-8800-39c7-9ace-118887aa9a51 | -4.75488 | -45.76876 | 2026-10-07 04:00:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d2c675d-839b-3226-a32c-4a2d4c9eb310 | -3.42198 | -44.33003 | 2026-10-07 04:00:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c46ab13-3dda-36c0-ae3e-22c79efb176c | -5.97936 | -37.8293 | 2026-10-07 04:00:00 | NPP-375D | UMARIZAL | RIO GRANDE DO NORTE | Brasil | 2414506 | 24 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 232b0f3f-e8bb-3534-8e27-427b5e29752e | -6.23033 | -41.9869 | 2026-10-07 04:00:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 23.2 |
| adb30070-2b29-3375-ad5e-47bdb6c8f4af | -4.51129 | -42.89188 | 2026-10-07 04:00:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 00486cf0-d034-3e50-9923-a3d5fdf45c94 | -6.8456 | -41.76858 | 2026-10-07 04:00:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 44228a94-eb7e-32ae-acd3-75d6994fec66 | -5.27441 | -43.3686 | 2026-10-07 04:00:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 541e6d3d-67bb-3583-b678-11b9b7ae2b60 | -4.34994 | -43.79782 | 2026-10-07 04:00:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64614d7a-ceaf-3daa-acac-ddacaa194d2c | -5.98232 | -40.92466 | 2026-10-07 04:00:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b0f9ee2f-86d3-3393-8670-32082576c4b8 | -1.25649 | -49.05892 | 2026-10-07 04:00:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 64819b12-8674-3ec8-b9c3-1a15618fe02b | -5.97989 | -40.93908 | 2026-10-07 04:00:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 73d44703-6356-3ca0-8111-4db51a3bbd3f | -5.9713 | -40.94268 | 2026-10-07 04:00:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 6a17b927-9fcc-3791-86c0-3c45d0ec2c43 | -3.30665 | -42.27518 | 2026-10-07 04:00:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2de3d242-efe5-3a49-9c5b-096862eef091 | -5.72384 | -45.16504 | 2026-10-07 04:00:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 9a596525-5d22-3457-b8f0-7bf965676039 | -1.25759 | -49.05219 | 2026-10-07 04:00:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48eee7f3-3f49-3b61-a0ca-8066128aedeb | -3.44278 | -49.25408 | 2026-10-07 04:00:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 127878d9-22a6-340c-baa2-3a5c614943ac | -3.30593 | -42.27954 | 2026-10-07 04:00:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 86ac244c-a85c-32b3-98d1-3381bfe9387f | -5.10685 | -45.88473 | 2026-10-07 04:00:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe0ed5fd-0b72-394f-8aa7-73d7fa9e125b | -5.0475 | -44.75544 | 2026-10-07 04:00:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2c51650a-274a-3654-bcee-4303150ebc85 | -4.84081 | -45.98793 | 2026-10-07 04:00:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 75821dc9-70a6-3bc1-a1c0-01a737ac5758 | -3.44167 | -49.26051 | 2026-10-07 04:00:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e99c5a75-8263-3caa-9644-8440189594d9 | -5.91071 | -35.47078 | 2026-10-07 04:00:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 71f340cd-25bb-3b3b-a374-c22e98681f08 | -5.96907 | -40.93233 | 2026-10-07 04:00:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 7b6b84ec-754f-332f-91c1-c295b9a87a0e | -5.19249 | -35.6156 | 2026-10-07 04:00:00 | NPP-375D | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 10b34c88-a3ce-37d5-841a-2c6632c76f18 | -3.1196 | -44.35251 | 2026-10-07 04:00:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9de15b4b-b63d-3d4f-b9e6-29cd3a9314df | -6.02311 | -42.26452 | 2026-10-07 04:00:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 34ddaffb-8b27-3075-a330-7482c9600983 | -4.34513 | -43.79694 | 2026-10-07 04:00:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5b0a443-a910-3a13-9b39-9651b2c3de44 | -3.95209 | -38.33866 | 2026-10-07 04:00:00 | NPP-375D | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 636fd5c8-92b3-3c7e-bdf3-4be36ee8e2fa | -4.31578 | -42.99785 | 2026-10-07 04:00:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a5ff5f13-ba3d-363a-8b0b-4114a2659375 | -5.75066 | -43.26872 | 2026-10-07 04:00:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| da30e522-0130-39af-991f-e73dbca1f2f0 | -6.83004 | -39.54884 | 2026-10-07 04:00:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 7a4ef222-b3d8-37ca-8d06-295618a20e4c | -4.82659 | -38.68962 | 2026-10-07 04:00:00 | NPP-375D | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bd3acb85-ca6e-3fcf-b13f-c9e295d36b2a | -5.06932 | -45.58598 | 2026-10-07 04:00:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 18be93ec-92d9-3789-8c9d-d43ae4c1a894 | -3.41089 | -39.28617 | 2026-10-07 04:00:00 | NPP-375D | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8cb4bfb0-502e-38fa-8d11-86facfbe96e8 | -5.73063 | -41.7221 | 2026-10-07 04:00:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ad204db7-7960-38b6-9996-931decfdbb9a | -5.19411 | -35.61619 | 2026-10-07 04:00:00 | NPP-375D | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 68fdebf5-a0da-3a23-97c5-b7d61aff09c2 | -5.72956 | -45.16278 | 2026-10-07 04:00:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 5e41f8a2-a183-3d02-9b0f-89ff2f3e57c5 | -4.35435 | -47.78106 | 2026-10-07 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e5c4ec38-983a-3f1b-89a5-ecdec85d14cd | -5.97617 | -40.91388 | 2026-10-07 04:00:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6f08e28e-5afe-3718-b405-fd0fddf753ac | -3.46489 | -50.08717 | 2026-10-07 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| af1876aa-ab5b-3f0b-9fbd-275d7a46be50 | -5.7218 | -41.68293 | 2026-10-07 04:00:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8ae3563a-7b1a-3cf7-b46c-0f7d001a45f7 | -3.12264 | -44.35273 | 2026-10-07 04:00:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b1ce73d3-d954-3b9a-9dc2-8b5abd379d4a | -5.41472 | -39.10917 | 2026-10-07 04:00:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ecd7af4d-49a7-3b04-9606-566e05f86f8a | -5.7252 | -41.68008 | 2026-10-07 04:00:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |


[Clique aqui para ver as próximas entradas](README37.md)
