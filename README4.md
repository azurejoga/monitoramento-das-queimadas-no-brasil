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
| d8451db5-f636-31a1-9f13-0a635cb59ab0 | -6.33276 | -43.36835 | 2025-05-28 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 38933907-6d01-33ad-a85f-9e642b9ec6fa | -5.97089 | -43.75849 | 2025-05-28 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 049d7af3-eea1-32cb-bd68-21134e6eb4fc | -7.20696 | -43.11851 | 2025-05-28 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 5325c777-4cfa-36ea-9c5a-c0cff9b2d254 | -6.12469 | -43.95435 | 2025-05-28 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ed1a9aae-9a74-3578-bb7d-f33c246098e0 | -7.18774 | -43.11517 | 2025-05-28 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| cc83bd1b-0d63-3d94-aa13-b757732f234a | -8.00906 | -46.15884 | 2025-05-28 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4f718ac-f90e-3cb9-af27-e17b0e61a2b0 | -7.99787 | -46.1541 | 2025-05-28 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bbea6238-e950-3068-a080-071a0dd064da | -6.33772 | -43.3692 | 2025-05-28 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0a28f65c-4b12-3c63-b2ea-1cd25327c49b | -8.00378 | -46.15455 | 2025-05-28 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 37cacdf0-9830-3195-9865-61728f480084 | -5.78411 | -43.61963 | 2025-05-28 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aace604c-c90f-396c-b1d2-1d94c18260f2 | -6.62149 | -48.02346 | 2025-05-28 03:42:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36ee7950-27bc-3156-8dab-6096917fa063 | -6.32681 | -43.3733 | 2025-05-28 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b87df6c-edfe-3992-9596-83933475ab18 | -6.31635 | -43.37466 | 2025-05-28 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7c3aa954-8a46-3571-b2d5-1bb1a12730a7 | -6.83569 | -43.41365 | 2025-05-28 03:42:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7ac7a6ef-76b6-38f5-8a62-e111bc48fbbb | -5.77199 | -43.48679 | 2025-05-28 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48faef2f-055a-380e-ae98-14ba1227020a | -6.31585 | -43.37755 | 2025-05-28 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e4d37a09-1289-391f-b6fe-69b175e59025 | -7.68396 | -46.10099 | 2025-05-28 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 71625cb0-4a5e-3409-a768-18e9a6ce7294 | -6.65024 | -41.99554 | 2025-05-28 03:42:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 523ebe6e-4689-336a-963f-4c8f2bf1334f | -8.01775 | -43.18748 | 2025-05-28 03:42:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 83539354-0ac9-322b-ae8e-4205934b0324 | -5.76285 | -43.47943 | 2025-05-28 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe44282c-3618-352e-abff-8517e0831893 | -8.00402 | -46.15376 | 2025-05-28 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac1c5714-08e7-3ced-a0fd-d014b2d25106 | -7.74569 | -44.01289 | 2025-05-28 03:42:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc31b011-44b6-3eb9-b90d-bc84d63785d5 | -7.2175 | -43.11483 | 2025-05-28 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 19eb3dc8-18b9-35b5-8937-cd862f838946 | -7.96658 | -45.93569 | 2025-05-28 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d23186b0-e6e2-3b64-9263-41e2b0bc894f | -6.5083 | -43.6379 | 2025-05-28 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e30182d6-a21d-313b-8922-a6e2725c4997 | -7.67828 | -46.10051 | 2025-05-28 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 629bbb82-5ebb-3b00-96ef-00063d95665e | -7.99737 | -46.15722 | 2025-05-28 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9d1c655f-6f5d-305b-919c-4452cd523023 | -6.63934 | -43.20958 | 2025-05-28 03:42:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 529f508a-dc8c-3f50-a0f0-f60a44eab97e | -6.03283 | -44.05134 | 2025-05-28 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 89d25885-b50b-3fed-a118-8c467bc9cac0 | -8.01848 | -43.18568 | 2025-05-28 03:42:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 3ee23de1-7ea4-3190-aa57-410cf86e9bad | -6.62858 | -43.21364 | 2025-05-28 03:42:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.1 |
| a596a269-e843-367e-9afd-94a9b20c73b9 | -6.32133 | -43.37544 | 2025-05-28 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2726b4b7-ddc5-3a57-9c7d-7fda3f87467b | -6.2124 | -43.35022 | 2025-05-28 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 14b65a78-3445-3c53-bf70-9886aefc9c95 | -6.20789 | -43.34669 | 2025-05-28 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 573d421a-6c7f-38de-bb6d-2dfb7104cdbf | -9.18311 | -40.30799 | 2025-05-28 03:42:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 9c5b3f23-1057-39de-9f2b-9d1fc52b7b27 | -6.21192 | -43.35301 | 2025-05-28 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 17f91fe7-b116-34de-a8bf-3214a7ee4971 | -6.21288 | -43.34742 | 2025-05-28 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 193b0a1b-53d9-3085-b5e7-e636597e2035 | -6.20741 | -43.3495 | 2025-05-28 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 6ca1e86f-08d4-3ffa-ba49-bac22291086a | -6.75223 | -44.6345 | 2025-05-28 03:42:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5f11b61e-b692-326c-9789-a73818cfdc9b | -7.08233 | -46.04977 | 2025-05-28 03:42:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| e7ccb42e-16de-3941-9c15-f38bccf72051 | -5.96578 | -43.75754 | 2025-05-28 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 40970479-2abd-354a-8793-1cde8218e26d | -5.64671 | -43.58796 | 2025-05-28 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dcb713de-e428-3666-b420-f985e65b7e1e | -6.12002 | -43.95046 | 2025-05-28 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d8e517a1-6261-3d54-aeac-64d8a1137d08 | -7.68408 | -46.1016 | 2025-05-28 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| a4abac18-adfd-3311-a185-42fd4d987d46 | -7.18293 | -43.11432 | 2025-05-28 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 5c1b9013-b9ff-347c-9b74-df6fba1ab45f | -7.62655 | -45.75654 | 2025-05-28 03:42:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f1d984db-5fcc-3580-916d-b8d1d6119c12 | -7.67904 | -46.09631 | 2025-05-28 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| f3896476-904f-3317-b28c-9516442f6b1b | -8.16862 | -43.39801 | 2025-05-28 03:42:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a17e0097-2716-30ef-a49b-36ac7614dfcd | -5.65131 | -43.5918 | 2025-05-28 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 478e7e0c-2ae1-3922-be17-dd1ad1f20c3a | -7.20215 | -43.1177 | 2025-05-28 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| a503671c-9f9a-3c7d-a785-5d56bfa476aa | -5.65181 | -43.58879 | 2025-05-28 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dfa5a634-baf5-35c9-8e26-1adcd644d2f5 | -7.63156 | -45.76133 | 2025-05-28 03:42:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 33822691-227f-3cdc-af0d-3bf93cb521ad | -7.18865 | -43.10994 | 2025-05-28 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 51d81452-07c2-3a51-92b1-65a89232ac0e | -5.97142 | -43.75549 | 2025-05-28 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26bc53d5-c7d0-3d80-87ac-e09456a935ea | -6.2174 | -43.35089 | 2025-05-28 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| f2d47c7b-c653-3be5-9892-14ba6b73dd9f | -7.66743 | -46.09422 | 2025-05-28 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e35ed086-0d5b-3263-b8dd-3e9a981e0a46 | -6.12107 | -43.94436 | 2025-05-28 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ae6854f9-933f-3c94-97bf-c4355b3d4252 | -5.77249 | -43.48384 | 2025-05-28 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc6f320f-8a42-3833-9296-d5d51a3db900 | -7.67172 | -46.10361 | 2025-05-28 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 5649e0c7-273f-3289-bc82-0ab53f60596b | -8.14617 | -46.48897 | 2025-05-28 03:42:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b43ff63f-6c2c-3aea-8114-ede503f1b3a1 | -7.0882 | -46.0507 | 2025-05-28 03:42:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| f0962e63-94f3-3757-ace7-4a81f207d13a | -5.97196 | -43.75245 | 2025-05-28 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 202ad12b-4fd3-3630-98a2-c204eca2aeca | -7.67096 | -46.10783 | 2025-05-28 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| a9d0cd44-dd47-3d7e-bb48-b234a3daba70 | -6.32083 | -43.37836 | 2025-05-28 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fc658559-7f15-38c8-852c-ea7cbd19249f | -7.67323 | -46.09529 | 2025-05-28 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 2564a5e9-af6b-304d-a9f7-fceba2f45aad | -7.4758 | -34.84456 | 2025-05-28 03:42:00 | NOAA-21 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cad230eb-a6ce-3df1-9cb2-8fcbe7000c40 | -8.07434 | -34.97781 | 2025-05-28 03:42:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f7f863c9-7156-3ced-abbd-77fc1aa44f85 | -7.19437 | -43.10556 | 2025-05-28 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 825cda23-8eca-3889-bae5-69327081cc50 | -6.33227 | -43.37123 | 2025-05-28 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96ff36c1-1c76-3583-8ea0-83113f037aca | -14.69163 | -45.09273 | 2025-05-28 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 869a8bb9-9671-3295-8708-3f2cba07ca4e | -12.40547 | -50.00039 | 2025-05-28 03:45:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8ee04a97-c9dd-3a6a-9e2e-5392adb2696b | -11.80962 | -44.27625 | 2025-05-28 03:45:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fcad42be-3f3f-3dca-8059-5998d7418c91 | -11.81345 | -44.28248 | 2025-05-28 03:45:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 254cedc1-0a76-34cb-8834-3ca7c3c121b6 | -9.02935 | -47.73564 | 2025-05-28 03:45:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c7ffe123-42bd-3036-a99c-561482e6d5b1 | -9.1499 | -49.65016 | 2025-05-28 03:45:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 53559c63-9b19-347f-9472-d16c5b4b14fb | -15.51831 | -41.96952 | 2025-05-28 03:45:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7342bbf6-eede-3558-b5e2-28cdc7946ea7 | -12.70423 | -40.18111 | 2025-05-28 03:45:00 | NOAA-21 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4ad1d4fb-01bb-350d-80ec-8d1eb33552f5 | -11.40261 | -44.83158 | 2025-05-28 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| a9822b1d-e1e9-361a-954a-408c54bcc295 | -15.42643 | -39.47708 | 2025-05-28 03:45:00 | NOAA-21 | CAMACAN | BAHIA | Brasil | 2905602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f985008b-25d7-3d06-8f95-080db99b800d | -10.6963 | -37.04897 | 2025-05-28 03:45:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 99db82d2-7829-333c-88c9-21f2d5e58096 | -15.69622 | -43.42268 | 2025-05-28 03:45:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 96404fdb-cb75-33b7-a88d-11ae2e4c53c8 | -13.08825 | -45.2744 | 2025-05-28 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea29178c-afe9-3458-82a8-f71c212de0d8 | -11.81954 | -44.27433 | 2025-05-28 03:45:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 34.1 |
| f1b443fc-f97b-3954-8be6-f1d557c8895d | -10.46826 | -47.94652 | 2025-05-28 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8b01206f-149d-3b8c-b747-c9fb4aef1425 | -11.5746 | -47.62107 | 2025-05-28 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 02b98e25-dcef-321f-ab8b-ab53621d5ca6 | -9.0421 | -47.75542 | 2025-05-28 03:45:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 38a017c8-102e-3528-a471-018edd0380f0 | -11.81853 | -44.27968 | 2025-05-28 03:45:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 34.1 |
| d168247d-ba96-31b0-94a4-d0d686e99a61 | -10.95358 | -48.15149 | 2025-05-28 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 961bfbb1-e731-3d6d-a15c-8d4d8905dd68 | -10.95052 | -48.14591 | 2025-05-28 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 31cb10d0-113d-32af-8d89-2699fb2b2721 | -10.46927 | -47.94991 | 2025-05-28 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 594852e4-c990-3bd7-9748-4d237f8a94cb | -12.86338 | -38.36712 | 2025-05-28 03:45:00 | NOAA-21 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3986362d-b7bc-32d4-9d00-472e286fc0c7 | -10.45479 | -47.94934 | 2025-05-28 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0bab826a-4407-3320-ab93-3950beb99f34 | -12.26815 | -44.60069 | 2025-05-28 03:45:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 69cc4ce6-cc5c-35c7-a787-5edef335a41c | -11.10916 | -44.62988 | 2025-05-28 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6bc61cc-abbf-3634-b99c-753cc3ed5185 | -12.82163 | -47.39446 | 2025-05-28 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37c011b1-5514-3474-8c73-ad60922a1503 | -9.04307 | -47.75039 | 2025-05-28 03:45:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5640a06b-e5d0-307e-b803-466f48b7d575 | -9.1548 | -49.65158 | 2025-05-28 03:45:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 327a371d-9582-3587-a925-7bad80854492 | -9.19963 | -49.47067 | 2025-05-28 03:45:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 602a3342-c8ad-34d9-af26-cb40afd622e0 | -10.66341 | -49.44674 | 2025-05-28 03:45:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 016febd9-0d3e-3f9a-9c32-2519f15d98c7 | -8.72783 | -47.98588 | 2025-05-28 03:45:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README5.md)
