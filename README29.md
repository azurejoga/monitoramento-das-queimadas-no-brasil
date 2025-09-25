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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df5c778d-3e7b-35ac-8852-218136507dd5 | -5.787 | -42.80623 | 2025-09-25 04:59:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 65753c05-a9c5-30b3-95e4-29c5a8fb0f04 | -1.09084 | -54.10633 | 2025-09-25 04:59:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| de0020a5-e52f-385c-84c1-d65a3d3e06a8 | -6.683 | -43.13254 | 2025-09-25 04:59:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ea772ed-b949-307e-a538-2d212f9325df | -1.08972 | -54.1134 | 2025-09-25 04:59:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8c805d13-b8d8-30c0-a404-614fe45720ce | -5.60076 | -45.36352 | 2025-09-25 04:59:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d24b0163-663c-3700-9e32-5f8d9f0be9d1 | -2.52318 | -47.25218 | 2025-09-25 04:59:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebb868a0-2483-3cb6-b750-ffe945fa5b3e | -7.25941 | -43.01993 | 2025-09-25 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2696b68e-5e98-328f-a189-4b6cd07fb5e4 | -2.92075 | -48.30628 | 2025-09-25 04:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 4b4510d6-c5bd-3fc6-9c0d-6f9b80c7b650 | -5.86257 | -45.28128 | 2025-09-25 04:59:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b655ddf-b258-396f-a589-5c58e0a04e83 | -7.32042 | -45.76554 | 2025-09-25 04:59:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96bb4f39-c350-3d31-9400-21498b7b3012 | -7.31522 | -45.76483 | 2025-09-25 04:59:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cbfb0074-edcf-34f2-bb41-924f20bb348c | -2.72398 | -48.752 | 2025-09-25 04:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22390816-7dde-3237-aa54-c842eaa0639f | -3.39969 | -47.4967 | 2025-09-25 04:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50309f33-1fbb-3841-b66b-3fe55ac9089f | -5.23057 | -43.69326 | 2025-09-25 04:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5a247c5c-3b1e-3960-909a-2c098cce61e0 | -7.26786 | -44.91376 | 2025-09-25 04:59:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 13904efe-62ae-315f-a355-59059eeff429 | -5.5283 | -43.87816 | 2025-09-25 04:59:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 3096ce16-3dc5-3e71-b868-86a2d340c658 | -3.01567 | -51.3521 | 2025-09-25 04:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06ff3293-1727-3900-a394-588505cf8b2a | -2.95306 | -54.80149 | 2025-09-25 04:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73583c49-2f45-30cb-a495-1ba6fe61fe4e | -1.14857 | -54.22055 | 2025-09-25 04:59:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8e60d27-1591-3a6e-a94b-5675a3b3ccdc | -7.26238 | -44.91284 | 2025-09-25 04:59:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4eda3fec-3834-3018-911e-3ee889e2ae79 | -6.56571 | -42.06321 | 2025-09-25 04:59:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 78c8e6fa-533f-3dc4-88d0-bf7530afef42 | -3.30437 | -42.18111 | 2025-09-25 04:59:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9d877d05-a454-3d6d-8003-e1d1367e2ae4 | -6.59249 | -44.62231 | 2025-09-25 04:59:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2780bbbc-0828-3ac1-9e19-fb56c462503a | -1.82238 | -55.28088 | 2025-09-25 04:59:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29846022-174f-3c64-a4b3-ac1004df9205 | -3.61795 | -51.79996 | 2025-09-25 04:59:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9aa7c22-e3ff-3f3e-be18-5c20c0ff8e4e | -6.07286 | -44.08278 | 2025-09-25 04:59:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5d4213a2-f780-3a46-b5ba-be7f89bda749 | -2.92187 | -48.29907 | 2025-09-25 04:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8b8662fe-d59c-3002-b620-97a51e1c80a8 | -5.63449 | -45.72414 | 2025-09-25 04:59:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4a95c94-0e4e-3382-bcd1-9434e504d4d2 | -3.80648 | -51.34902 | 2025-09-25 04:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a32147a-969e-3353-a6cc-58c71ce9bec0 | -3.82069 | -50.97635 | 2025-09-25 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 95ce6ecd-3bd4-3e09-b213-7283ccb59751 | -3.36628 | -59.5002 | 2025-09-25 04:59:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 921c117d-a9de-36a4-a83a-f07784391d04 | -5.78872 | -42.80551 | 2025-09-25 04:59:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| bac63b4b-02d0-3592-9f3e-ea55fea9a10a | -3.6151 | -51.79575 | 2025-09-25 04:59:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29975264-112b-36a3-8717-e9e5864d5ee4 | -7.77524 | -46.18925 | 2025-09-25 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9712914-c85b-34c7-9060-6ea3e5d1837c | -10.59488 | -44.08185 | 2025-09-25 05:01:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c3882eb9-2686-3920-a37f-133c18d84016 | -12.84665 | -44.68108 | 2025-09-25 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3123a61-6cfd-368a-9c4b-863c3a286c44 | -13.83122 | -45.61938 | 2025-09-25 05:01:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| bb13c1a4-f6b4-3660-bbec-d74db0c7fa1e | -12.53397 | -45.8027 | 2025-09-25 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ac19425-d2a8-38b7-bf07-5ad089ba1215 | -12.05199 | -44.82593 | 2025-09-25 05:01:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 473e6bfb-27a2-3548-a1df-820eab49457f | -8.28584 | -44.95573 | 2025-09-25 05:01:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 48384bfc-2452-3bbc-8fc9-100a74ae6482 | -11.68797 | -44.39161 | 2025-09-25 05:01:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 466594ac-712f-3f6f-92b9-0e887c062216 | -10.58972 | -44.08308 | 2025-09-25 05:01:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e92cdfc-6362-34a9-92dd-727190c07233 | -11.70081 | -44.39424 | 2025-09-25 05:01:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6b9624e-6583-355e-8d53-5811ba15a312 | -10.10832 | -45.33094 | 2025-09-25 05:01:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b353daef-f038-3f0f-8ea2-5210da9e79d5 | -8.49713 | -45.00744 | 2025-09-25 05:01:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d82efa7-7532-33b2-8f1a-7101d525a3de | -10.10493 | -45.32773 | 2025-09-25 05:01:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79e7d33d-2659-3dc9-a905-6ee9c8ea7373 | -12.85086 | -44.67781 | 2025-09-25 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 326754f0-4998-3b5e-a1aa-b2e3335125c4 | -10.82979 | -44.82457 | 2025-09-25 05:01:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83b11ade-59ac-3ffc-8460-49597ffc6286 | -8.49107 | -45.01043 | 2025-09-25 05:01:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 87502399-128a-38b7-97db-275524c6bcc2 | -11.6666 | -44.41643 | 2025-09-25 05:01:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b6112cb-9e7d-30ad-b904-229ce056821b | -10.29006 | -45.22941 | 2025-09-25 05:01:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4fbbff36-7243-32fb-85e3-7f86d32ed401 | -11.78095 | -44.87455 | 2025-09-25 05:01:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 215c31a8-da30-329f-9f43-2169fa677e5b | -11.6929 | -44.40141 | 2025-09-25 05:01:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eb11e29e-a182-3636-9943-08cc78eb4a0a | -11.78639 | -45.56814 | 2025-09-25 05:01:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c2bcae4d-7613-3b47-b6b6-571a3c9844ab | -13.83743 | -45.61598 | 2025-09-25 05:01:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3de2ce23-600d-3bb7-b88b-3ac49d83867b | -11.40648 | -44.96244 | 2025-09-25 05:01:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77d74b72-85a3-3c4f-9bcc-5736e0f96d4d | -12.41735 | -44.74875 | 2025-09-25 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 72b9e67e-4c5e-3b62-a26c-a896798440a6 | -13.8427 | -45.6207 | 2025-09-25 05:01:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6eacf7bb-c964-3f97-867a-1d8601960479 | -8.48592 | -45.00657 | 2025-09-25 05:01:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5dc3d8b4-e02b-3fb6-80b1-49c1e994f380 | -11.64083 | -45.35081 | 2025-09-25 05:01:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0001e79-0a76-37aa-8d36-15ab5a192d7f | -12.5409 | -45.79213 | 2025-09-25 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dfea39ef-760a-3caf-be1f-04fbda9d8116 | -11.4 | -44.96724 | 2025-09-25 05:01:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e1c5841-16e0-3ada-802a-9c251c7afee5 | -11.6262 | -44.44777 | 2025-09-25 05:01:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45db5048-acfd-367c-93a5-9f5c6a75c8af | -10.84271 | -44.80886 | 2025-09-25 05:01:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5566160-5b49-306b-ae4b-d7638df4a931 | -7.77655 | -46.19217 | 2025-09-25 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6635a9ad-a798-319c-a1ac-b1b172800969 | -11.70029 | -44.39877 | 2025-09-25 05:01:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ffbef5ee-0cd2-33f8-be7b-a0a00a7d1ed1 | -12.54647 | -45.7929 | 2025-09-25 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0c4e1d2f-8a4d-3fcb-93a5-b17d286e67f9 | -12.07136 | -44.86338 | 2025-09-25 05:01:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 85c00aab-b727-3f25-8ede-99632eb7aa6a | -12.06694 | -44.85062 | 2025-09-25 05:01:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e55f7a20-48dc-37ba-ad00-f6397ccd026c | -8.48078 | -45.0026 | 2025-09-25 05:01:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 467e586d-e76a-3a45-b19c-6544e402caf0 | -12.85294 | -45.29445 | 2025-09-25 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 31caa7d6-4d52-37d8-96af-0f11f8e3b692 | -11.90992 | -44.77551 | 2025-09-25 05:01:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f61f4eb-37f2-391e-9fed-b542e17b2cab | -8.48032 | -45.00612 | 2025-09-25 05:01:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 290c5dc6-4405-3958-966b-0e03f2740771 | -11.04345 | -45.89454 | 2025-09-25 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4ee24477-c790-3a0a-8e81-4db0c89cfdeb | -8.73766 | -45.42181 | 2025-09-25 05:01:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1a77d5e-5f7f-35dd-b11f-24a243ca3dad | -12.53352 | -45.80646 | 2025-09-25 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66ecb856-2167-38c5-ab49-58ad72f6f2db | -13.84365 | -45.61246 | 2025-09-25 05:01:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbc5363b-e359-3a7d-bd2d-61a88b2fa334 | -10.40041 | -46.18971 | 2025-09-25 05:01:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 445a75ea-29f8-3686-b452-ed9baae62ce3 | -10.84901 | -44.80565 | 2025-09-25 05:01:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7e1b0c7-bc12-3382-850f-f76cccbfb87a | -12.85318 | -44.67737 | 2025-09-25 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d71dcf38-5e4b-3250-a392-069fcddf2dd8 | -11.80359 | -45.56715 | 2025-09-25 05:01:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac4b7ae0-73ca-327d-ae23-6d25ab886711 | -11.67317 | -44.41268 | 2025-09-25 05:01:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 64811828-a3d2-3075-acda-275f2f473423 | -11.7828 | -45.57139 | 2025-09-25 05:01:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cb8dada3-fc3f-311b-85be-4af6c8dfc09d | -11.42685 | -44.93373 | 2025-09-25 05:01:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e59ebd76-9bda-3b30-bda8-fd59fc3789e1 | -10.84851 | -44.80973 | 2025-09-25 05:01:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4fe5d5cc-fa07-36c1-8957-0f1c7242228e | -10.58823 | -44.08568 | 2025-09-25 05:01:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9aa97d8-cc7a-3409-aa94-b2d85b303335 | -13.83169 | -45.61532 | 2025-09-25 05:01:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 9804b882-f1b8-3b0d-8144-750f8a7b41eb | -11.43292 | -44.93968 | 2025-09-25 05:01:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1aeebd95-2e21-395d-ab12-8445ad63f3b5 | -8.28689 | -44.9478 | 2025-09-25 05:01:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f99d8a1f-be08-3743-a7fa-fae3aa102415 | -11.43231 | -44.93749 | 2025-09-25 05:01:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20bb043d-e065-3c05-9d10-a0b778f27a95 | -11.42641 | -44.9375 | 2025-09-25 05:01:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 99ba69fc-2d4c-3983-b7ea-23e2470f02be | -12.06806 | -47.98976 | 2025-09-25 05:01:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 578a52e0-dd69-32a2-8684-420aad4bca7d | -13.84318 | -45.61658 | 2025-09-25 05:01:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d6fa8ef2-bf72-3a74-97ad-9c7ed5eb0fb8 | -11.67371 | -44.40816 | 2025-09-25 05:01:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6d2472ce-3379-3431-a51a-d0c398504d27 | -10.39091 | -46.13902 | 2025-09-25 05:01:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c579c3b8-7016-3f34-bc7a-a18e7f7d941d | -12.84716 | -44.67659 | 2025-09-25 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82afe1c8-f563-3caf-b383-83534e495125 | -11.66605 | -44.42094 | 2025-09-25 05:01:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e5fdbd8-dfa2-3d06-a5bc-a8c7609d6c35 | -11.62295 | -44.3187 | 2025-09-25 05:01:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 227f16b3-3700-3b11-bdbb-e94e05696d4b | -13.8379 | -45.61188 | 2025-09-25 05:01:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e32cd40-645a-3501-b576-088ce12c6564 | -11.04431 | -45.88773 | 2025-09-25 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |


[Clique aqui para ver as próximas entradas](README30.md)
