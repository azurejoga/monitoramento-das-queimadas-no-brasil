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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72c4e111-83be-373f-97c8-4f7a51d2bb39 | -4.88802 | -43.23382 | 2025-10-26 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| faace1a3-601b-3633-b9d3-838ea68ea63b | -9.96409 | -43.86046 | 2025-10-26 03:40:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71feddca-af7a-3e42-92ea-d575012bd95e | -7.79647 | -45.3905 | 2025-10-26 03:40:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8bad445-85f4-39a8-a7b6-f6ec865931c4 | -6.43213 | -42.02828 | 2025-10-26 03:40:00 | NPP-375D | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 21250696-cf92-39c5-a3d5-b9fc983ab04a | -7.10658 | -47.95523 | 2025-10-26 03:40:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 46082fbf-21d3-311c-a58d-aa945955faa6 | -5.46506 | -40.88125 | 2025-10-26 03:40:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 06a98889-4a06-3973-bc5a-6e4c9d4939e4 | -8.32729 | -48.19043 | 2025-10-26 03:40:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2eb8001f-25bb-32fb-8731-268fdf733ea9 | -5.41095 | -46.00975 | 2025-10-26 03:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9eb5d2f5-0488-3194-adca-be271c0331ac | -10.42692 | -44.50203 | 2025-10-26 03:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 5fca88bc-e793-368f-99e9-96431c2ffc4b | -4.70998 | -46.44349 | 2025-10-26 03:40:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c983cb30-65da-3245-8f13-fce47e6dfff9 | -6.21934 | -42.53682 | 2025-10-26 03:40:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1517840b-19ee-3957-9bd0-d47c221c24ab | -6.02194 | -43.30708 | 2025-10-26 03:40:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 56c9f996-b031-383a-aa61-2f3fb45a0b9e | -4.71013 | -46.44312 | 2025-10-26 03:40:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 8b00377a-7f51-3816-a604-7177a204288d | -8.72003 | -48.00805 | 2025-10-26 03:40:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01a6f9b5-7159-3411-b3f6-0557e2436a6b | -11.46828 | -46.12418 | 2025-10-26 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f291c085-5124-3fa3-b877-c20007bbf283 | -6.63151 | -44.63561 | 2025-10-26 03:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 170a3dcb-8f89-33e8-8534-0152ded9dcc6 | -7.7789 | -42.92922 | 2025-10-26 03:40:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d126b3d9-1d78-3317-b69d-e82de4092933 | -7.35955 | -42.44011 | 2025-10-26 03:40:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 77dd9288-a91a-379a-b689-477df44959aa | -10.42765 | -44.49814 | 2025-10-26 03:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4dbc1d73-95f8-3904-96fe-d30e7661dfa8 | -6.20698 | -42.54531 | 2025-10-26 03:40:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ab14da9e-ce55-34c0-85a4-134f171fb2e5 | -7.64206 | -42.31285 | 2025-10-26 03:40:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| da010429-f84f-36a4-bcd4-42268be52237 | -10.77033 | -44.50537 | 2025-10-26 03:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a9cde694-afae-3c7e-90ba-0827e3cfc412 | -4.80981 | -43.29974 | 2025-10-26 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0aa81df9-4d40-33cb-9015-a9a887eae8b9 | -6.50061 | -38.73779 | 2025-10-26 03:40:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f732ab17-c536-3559-a57a-c06f29038f7f | -4.88533 | -43.24908 | 2025-10-26 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fdfc800d-0f81-3eba-bb8d-ee8bffd28740 | -6.15301 | -43.13612 | 2025-10-26 03:40:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7240a926-22ea-3b86-89b0-aef3066d67d3 | -7.69647 | -42.18276 | 2025-10-26 03:40:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 83f8ada9-3a6e-35d9-99d6-f82e5ad0ee80 | -9.24027 | -45.57849 | 2025-10-26 03:40:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a908c9aa-b5c5-31ef-92ce-e2aa96a65cc2 | -8.48789 | -44.72768 | 2025-10-26 03:40:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 172f5657-7419-334b-80ed-def0bb590a7f | -10.40946 | -45.313 | 2025-10-26 03:40:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d2330fb1-9490-3ebc-9193-f8105087e136 | -7.04966 | -39.74773 | 2025-10-26 03:40:00 | NPP-375D | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d194a117-51fb-3b50-97fa-2d793fd6752c | -6.83334 | -41.54924 | 2025-10-26 03:40:00 | NPP-375D | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f6451a03-d629-3c85-b6c2-60ad6c29c4a7 | -4.71116 | -46.4371 | 2025-10-26 03:40:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a9416858-941c-31e1-959a-b94bdeb71e8d | -9.43676 | -46.33178 | 2025-10-26 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3d7a0e26-7a96-3fa4-8b28-fdfe6ae83e4a | -6.71442 | -42.05056 | 2025-10-26 03:40:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 31eefb38-e28a-36f6-a5a4-bbff3b2ddf30 | -6.62548 | -44.63477 | 2025-10-26 03:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f1a5dca-1f98-332e-893c-123989f8a3b8 | -4.71127 | -46.4367 | 2025-10-26 03:40:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0a8d91cf-a610-324c-84b0-3000761cd061 | -8.15359 | -47.75578 | 2025-10-26 03:40:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2894111a-cc88-3762-aac2-2fbeeb12521d | -9.26084 | -46.41651 | 2025-10-26 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8cd72d4c-9305-3de5-955b-6652b62e2661 | -8.54322 | -47.21011 | 2025-10-26 03:40:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fcbc416f-91d9-3ef8-be47-d1e9292ee0a6 | -8.21132 | -39.34471 | 2025-10-26 03:40:00 | NPP-375D | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 001588c1-8b5b-3cc1-a371-78a6d86fd5a1 | -6.21286 | -42.54273 | 2025-10-26 03:40:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1cc7d17b-7dbb-3898-915c-6e83744120ce | -7.81652 | -40.26295 | 2025-10-26 03:40:00 | NPP-375D | TRINDADE | PERNAMBUCO | Brasil | 2615607 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ae278864-7935-3813-b46c-d2236a7e733b | -7.09621 | -39.57614 | 2025-10-26 03:40:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1ddef712-1ed1-31f4-9d82-71a5569ad0b6 | -8.03474 | -41.20129 | 2025-10-26 03:40:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1850a609-6e89-38c6-85ab-4fa6b240b032 | -5.10409 | -43.2045 | 2025-10-26 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c78cbb6e-9bc5-3524-8a56-844a4de4fe6c | -8.29943 | -42.31171 | 2025-10-26 03:40:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 6e04023f-ce6b-3c66-b0d4-2a8f3dd14a77 | -10.76701 | -44.50179 | 2025-10-26 03:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a7800e7-af90-31f2-bb26-6f0f9afa4ea8 | -9.43287 | -46.32777 | 2025-10-26 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df525490-ab4b-3c1f-9ccb-7609eb1cbdb1 | -6.21402 | -42.5362 | 2025-10-26 03:40:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 67e11e36-47bf-3b4b-935b-972b7a55055a | -6.5732 | -41.46014 | 2025-10-26 03:40:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6ec4e49d-7be4-3599-80dd-ae911273dd27 | -10.41463 | -45.31766 | 2025-10-26 03:40:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b1ea29ac-df1f-360f-b2e6-f49661743abb | -12.06244 | -43.99008 | 2025-10-26 03:40:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fadc581b-3a30-3f12-a214-5159084db5a8 | -6.57416 | -41.45473 | 2025-10-26 03:40:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e2f112af-6f86-37af-a9da-9456bbcd355c | -7.34876 | -42.44129 | 2025-10-26 03:40:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c779e4c1-fda5-3457-b18c-773ed143a208 | -4.89163 | -43.2463 | 2025-10-26 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 69fbc2a7-fae8-3536-945e-23e506264686 | -8.35335 | -40.49163 | 2025-10-26 03:40:00 | NPP-375D | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 89b50182-4b5a-398b-9ef6-8026e85eeb1f | -10.75174 | -47.90783 | 2025-10-26 03:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f5da7380-d648-3080-8552-0092aaec3357 | -6.52794 | -37.98567 | 2025-10-26 03:40:00 | NPP-375D | BOM SUCESSO | PARAÍBA | Brasil | 2502300 | 25 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 44ed8225-b5cc-3eb8-aec6-089608cc0427 | -10.4151 | -44.50346 | 2025-10-26 03:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ccd78d1-0f65-3d92-8674-ba0d9f898799 | -5.88145 | -43.93977 | 2025-10-26 03:40:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e3f782c-4d72-37ba-b966-9d6cd5de36b4 | -6.70034 | -42.04185 | 2025-10-26 03:40:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 7e0fd293-c79c-38d1-80d4-e5e58fc7f086 | -7.19703 | -39.41262 | 2025-10-26 03:40:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| f98ed166-b2ac-3c30-adf2-666126fb7129 | -6.69984 | -42.04467 | 2025-10-26 03:40:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 93b03a4a-5b05-3b09-bb77-178a5bb8a01a | -10.7725 | -44.50307 | 2025-10-26 03:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93dbc6ef-5d14-3754-b3d7-3f45194383f1 | -8.15713 | -41.10687 | 2025-10-26 03:40:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1eec524d-ea6d-38fd-b488-701145e057c1 | -5.46657 | -40.87234 | 2025-10-26 03:40:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 61acf137-ec41-3e80-9e57-0e421865a826 | -8.14314 | -47.04302 | 2025-10-26 03:40:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 37ade140-f3d6-3535-a746-67b1935b8ae0 | -6.20637 | -42.54873 | 2025-10-26 03:40:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bd6e5c55-38ed-32d6-b981-fd5205988909 | -8.07201 | -42.06001 | 2025-10-26 03:40:00 | NPP-375D | NOVA SANTA RITA | PIAUÍ | Brasil | 2207959 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 58eab95e-bc61-3374-b936-ebafecd68cd5 | -10.77105 | -44.50168 | 2025-10-26 03:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a08dbeaf-0fd3-3c88-ad43-007afc44cce6 | -5.09854 | -43.20323 | 2025-10-26 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a403eed1-f5ee-306a-a687-bc1d86a9eaf4 | -11.02369 | -47.8645 | 2025-10-26 03:40:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2dd555fb-a7f3-39e1-974a-0d5313a9d2cd | -6.7292 | -44.15213 | 2025-10-26 03:40:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f03c88b-2ebb-3e1c-835e-96dbcbb998a7 | -4.71246 | -46.43003 | 2025-10-26 03:40:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3d969528-6185-3aae-bddb-6f0d574c7e2d | -6.54691 | -41.60126 | 2025-10-26 03:40:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 305e241b-3b25-3381-9928-2512937bb439 | -7.0877 | -39.57483 | 2025-10-26 03:40:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 05e50800-fe7c-3aba-bcd7-e3394123752d | -8.14235 | -47.04076 | 2025-10-26 03:40:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9437a2f7-61e3-3f35-98b3-3afa5ab8e789 | -7.00435 | -41.07588 | 2025-10-26 03:40:00 | NPP-375D | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| e600d6ac-7a74-34f3-abe8-80bfd4a5f89e | -10.94467 | -48.07684 | 2025-10-26 03:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 07a98c0c-df50-31d6-8518-b9d9b89cbd14 | -6.13128 | -42.45868 | 2025-10-26 03:40:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8aee48fc-30ab-3219-9fe3-2054b4457836 | -7.84922 | -45.37199 | 2025-10-26 03:40:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fd95bdb6-7626-3143-afbd-68f04ea52375 | -7.19766 | -39.40891 | 2025-10-26 03:40:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 976d57c8-d6f5-3861-befb-dae36282bcae | -7.35901 | -42.44321 | 2025-10-26 03:40:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c83f592b-2b85-3048-a4c4-a53710a0862c | -8.82202 | -40.30952 | 2025-10-26 03:40:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 543fbe3c-94e4-3d59-85a6-2a1839651ea4 | -7.10598 | -47.95416 | 2025-10-26 03:40:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2df40fca-682a-3d0a-92c7-25924b97b949 | -4.8887 | -43.22995 | 2025-10-26 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c6ad7fa4-efb7-32b3-8842-f510681e4b9d | -4.90424 | -43.24069 | 2025-10-26 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bd900aec-6d3d-327a-a148-2209b8125aee | -6.82752 | -41.55384 | 2025-10-26 03:40:00 | NPP-375D | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 21c343f3-fd46-3cfd-ab4d-c8fc2243e532 | -12.02 | -43.30453 | 2025-10-26 03:40:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0fc9e21-35eb-385a-89bd-4f4c87ba5772 | -7.08837 | -39.57085 | 2025-10-26 03:40:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1a8f3c8a-0c9b-3cb0-a2e5-4a2d80fda0ee | -10.55634 | -43.85464 | 2025-10-26 03:40:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3a30a26-6ecf-3836-99f8-be79b69853f4 | -6.71043 | -42.04369 | 2025-10-26 03:40:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 690f6171-1c89-32a3-aa32-5d6582ce486b | -11.65998 | -41.4442 | 2025-10-26 03:40:00 | NPP-375D | CAFARNAUM | BAHIA | Brasil | 2905305 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ac335d5d-d381-3936-9348-f17a6622760a | -7.77787 | -45.38771 | 2025-10-26 03:40:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c81773f7-d2fc-3db5-b928-52a2cdc20c95 | -6.21344 | -42.53944 | 2025-10-26 03:40:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a7e7c662-0808-389d-97ba-909bcf2f8041 | -6.13206 | -41.71926 | 2025-10-26 03:40:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d120d139-c657-31e5-9012-0d7c8a483f9e | -10.40854 | -45.31769 | 2025-10-26 03:40:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 68936f4d-f796-3819-ad43-95fe004abfcf | -4.89433 | -43.23099 | 2025-10-26 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6079ac13-6104-3a4f-b283-292185c551be | -8.44404 | -45.12334 | 2025-10-26 03:40:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |


[Clique aqui para ver as próximas entradas](README10.md)
