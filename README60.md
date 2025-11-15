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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73fed8d3-60b9-3108-bce6-f95286bdb723 | -12.7982 | -46.38307 | 2025-11-15 11:59:00 | TERRA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 888de300-64ab-3dca-a015-6724ee3c5124 | -9.01597 | -44.17648 | 2025-11-15 11:59:00 | TERRA_M-M | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6af2fd8b-bdb0-32f3-9c1c-51ae4951450f | -11.96012 | -46.74051 | 2025-11-15 11:59:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 976cb19b-56ce-3a58-ab68-8100ed8ded98 | -16.2105 | -45.4798 | 2025-11-15 11:59:00 | TERRA_M-M | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| bc723d8d-5e8e-3efc-82de-e7b86582c9dc | -8.18417 | -45.00497 | 2025-11-15 11:59:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 284c6585-74e2-33a0-8225-4b054ec2e0a4 | -13.42021 | -42.22725 | 2025-11-15 11:59:00 | TERRA_M-M | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 18.1 |
| 0f7f36b0-662f-322f-95da-907775aa2574 | -7.56259 | -45.83374 | 2025-11-15 11:59:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 3c771c4c-8a0a-3c3f-be81-adcd3d93c15f | -13.99027 | -43.18292 | 2025-11-15 11:59:00 | TERRA_M-M | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 698946d3-dc0c-313c-b1e4-3a83a12f4084 | -8.19828 | -45.03228 | 2025-11-15 11:59:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 45.3 |
| abb790e6-3794-35a6-9d5e-04fa7253c602 | -7.96628 | -38.64234 | 2025-11-15 11:59:00 | TERRA_M-M | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 36.4 |
| 801085ac-f7e3-3597-95e0-c7c5dfe8bda4 | -12.86468 | -46.44379 | 2025-11-15 11:59:00 | TERRA_M-M | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 27.1 |
| ee0ff7ab-75d3-3b09-adc9-f6c49fbfd502 | -9.0255 | -46.88256 | 2025-11-15 11:59:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 57eb1848-9289-3c1b-bb77-b997e4c84be9 | -14.38741 | -43.7122 | 2025-11-15 11:59:00 | TERRA_M-M | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 22.2 |
| b5a86bb3-1cfe-3e99-99b6-165638f2bdb2 | -8.06353 | -43.09949 | 2025-11-15 11:59:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 25.6 |
| 504d9743-5fbd-3d35-8b77-78bab686f6c3 | -9.14824 | -45.1664 | 2025-11-15 11:59:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 9bc1984c-527c-3b88-936c-f3753037be55 | -12.16404 | -46.67762 | 2025-11-15 11:59:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 7cbd5381-b853-3c24-b2c8-866b3b22b7a0 | -8.16675 | -44.11682 | 2025-11-15 11:59:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 41229ca0-0033-37fc-b894-e99ff03bc6aa | -7.32995 | -44.03243 | 2025-11-15 11:59:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 98ddc5f4-3d97-3e10-a2ee-1185f285adac | -8.18919 | -45.03098 | 2025-11-15 11:59:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 28822bec-0300-3cb5-a1ed-5ef3860035dd | -9.15595 | -45.17693 | 2025-11-15 11:59:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 357e2c91-115d-33a6-a6c4-79456016a9c4 | -8.79459 | -41.31797 | 2025-11-15 11:59:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 7c19560e-4de9-3258-8494-2f52c2eaacaf | -7.96601 | -38.63653 | 2025-11-15 11:59:00 | TERRA_M-M | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 44.0 |
| c2d4010a-a45f-3db7-ae28-9156c3653bd7 | -10.52934 | -46.17706 | 2025-11-15 11:59:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 1c5b6b7f-5d64-3c82-a137-a167e98d3a19 | -8.01804 | -37.79393 | 2025-11-15 11:59:00 | TERRA_M-M | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 18.6 |
| 56f6233a-1fd8-324a-9c3a-56ebac8fb78b | -12.82856 | -43.1892 | 2025-11-15 11:59:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 0d217bf6-ca9b-3ab6-90b9-9f5dc0cff079 | -11.93577 | -46.22771 | 2025-11-15 11:59:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 403.3 |
| 81a71787-30ba-314e-af05-45fa964b1c7b | -12.1546 | -46.67614 | 2025-11-15 11:59:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| f30ce008-29f2-3fda-b696-52fdcfef6b94 | -12.43936 | -47.89754 | 2025-11-15 11:59:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| aa3fc340-81c7-31e7-8992-ba8da353b0dc | -12.38626 | -48.1037 | 2025-11-15 11:59:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 0f6277f4-a456-30c2-bf84-84fecae986a9 | -8.67037 | -45.46727 | 2025-11-15 11:59:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 399b31f9-7e0a-3297-b2b7-c64dcd5734c1 | -15.34201 | -47.85347 | 2025-11-15 11:59:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 73329194-2b42-3755-a4e1-679409d96bc2 | -8.16183 | -45.03083 | 2025-11-15 11:59:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 08064c29-354d-37a9-b946-d8c077f5d3c4 | -7.37831 | -43.37275 | 2025-11-15 11:59:00 | TERRA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 17.7 |
| c425faac-1366-3085-b841-38fdd39d6754 | -9.02727 | -46.87112 | 2025-11-15 11:59:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 572f2566-624b-33af-89e9-be44ff24b653 | -16.21183 | -45.47066 | 2025-11-15 11:59:00 | TERRA_M-M | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f885e2c6-2e0f-30cb-a122-e35058c00032 | -8.65333 | -45.455 | 2025-11-15 11:59:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| dc7565e9-d408-3bae-8233-6499e1a0a316 | -7.97717 | -38.63794 | 2025-11-15 11:59:00 | TERRA_M-M | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 198.1 |
| 593203b4-f914-3ab1-b845-0b093a02e259 | -7.8221 | -44.45416 | 2025-11-15 11:59:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c65a7730-da25-30f8-986a-f0281dfe6b66 | -7.97518 | -38.65258 | 2025-11-15 11:59:00 | TERRA_M-M | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 18.3 |
| a086bd21-d276-3242-9626-298185776d31 | -16.01665 | -45.23303 | 2025-11-15 11:59:00 | TERRA_M-M | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 84a66e40-fa3b-3233-94a0-4199d434bc72 | -11.93728 | -46.21768 | 2025-11-15 11:59:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 25.6 |
| aaa76bea-c7b0-3cd1-87f9-bf2bbb38d47b | -7.88689 | -41.60865 | 2025-11-15 11:59:00 | TERRA_M-M | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| a69ebbdb-44b7-3ac5-81ea-daf736971b7d | -7.88555 | -41.61826 | 2025-11-15 11:59:00 | TERRA_M-M | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 4b944662-d677-3972-809d-45294531bc04 | -9.45072 | -44.86816 | 2025-11-15 11:59:00 | TERRA_M-M | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 6a199926-40a4-3bac-83c6-69cb0298b219 | -7.58922 | -43.06446 | 2025-11-15 11:59:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 435db7e8-be76-3beb-8949-0b6e58a8083f | -17.66878 | -39.75957 | 2025-11-15 11:59:00 | TERRA_M-M | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 26.0 |
| 67b6ffb0-d505-3735-ad68-21829e0e934c | -12.25692 | -42.45337 | 2025-11-15 11:59:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| c66a4255-f931-3d0d-92e5-2fd956ccfb29 | -8.21927 | -45.01597 | 2025-11-15 11:59:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.4 |
| ad4ff95a-158c-3dee-9b6e-e6fbccbd3418 | -12.65902 | -46.74972 | 2025-11-15 11:59:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| cadf4b03-f851-3d45-a665-d5b723cd94e3 | -14.78694 | -43.2859 | 2025-11-15 11:59:00 | TERRA_M-M | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 93dd6406-c2e9-3c94-9ac1-8cb294b097e2 | -10.53855 | -42.62217 | 2025-11-15 11:59:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 35.7 |
| d1a21353-1146-3ddd-bad2-064a01deab6a | -12.92385 | -42.28457 | 2025-11-15 11:59:00 | TERRA_M-M | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 107.1 |
| a42df45d-4a34-3296-9799-c9f17bd6949f | -13.80968 | -41.74348 | 2025-11-15 11:59:00 | TERRA_M-M | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 16.7 |
| eb138c21-ea1d-3bdd-9202-1d9a38a3c261 | -11.05294 | -45.15028 | 2025-11-15 11:59:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 29d1fabb-432a-3514-9e76-fcef2f72eb1d | -8.22236 | -40.05496 | 2025-11-15 11:59:00 | TERRA_M-M | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 10.3 |
| b1194cfb-fff9-3125-9ae1-5550d71a3bfb | -9.85654 | -44.17139 | 2025-11-15 11:59:00 | TERRA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 27ff2d77-c1e0-3f23-a9f5-6ba6d3dcf498 | -9.96626 | -44.94346 | 2025-11-15 11:59:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 45935dcc-db42-33e5-8ff4-0d3b3c0d2146 | -13.68756 | -41.82156 | 2025-11-15 11:59:00 | TERRA_M-M | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 73977c88-1933-3e61-abe9-c535076a26f0 | -15.48126 | -44.19003 | 2025-11-15 11:59:00 | TERRA_M-M | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| cfebd534-58c1-323b-badc-245edfe856d6 | -17.58398 | -46.68528 | 2025-11-15 12:01:00 | TERRA_M-T | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| bea6870e-4867-32cb-b86f-a6e3a8124869 | -18.2442 | -44.13075 | 2025-11-15 12:01:00 | TERRA_M-T | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cd0f8583-b30e-34f8-9d21-a09409d7f5e9 | -20.32557 | -46.24597 | 2025-11-15 12:01:00 | TERRA_M-T | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 1a3ad973-4bf9-3a46-9d5e-fa2c0a2b1fed | -17.58541 | -46.67572 | 2025-11-15 12:01:00 | TERRA_M-T | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 22fe9a1b-d766-3c24-963a-06985de1c2ae | -20.05325 | -45.63405 | 2025-11-15 12:01:00 | TERRA_M-T | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 15.3 |
| e428e21f-2768-3e03-a539-99615ac02b7d | -17.83712 | -44.68443 | 2025-11-15 12:01:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 644b6cee-6711-36cc-87eb-359b5efb3944 | -20.20459 | -44.94771 | 2025-11-15 12:01:00 | TERRA_M-T | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ebb4d6db-7715-3e63-a43c-3dbcc282a5ee | -20.32422 | -46.25531 | 2025-11-15 12:01:00 | TERRA_M-T | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| fc731de9-3459-3584-8d08-5dc91a44cc67 | -17.41734 | -47.65215 | 2025-11-15 12:01:00 | TERRA_M-T | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 5654516f-bc31-3a57-8fb7-99a267f41045 | -19.17824 | -44.97824 | 2025-11-15 12:01:00 | TERRA_M-T | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 8db45e5e-ca52-3ea1-9d4d-45d6d39cdc6b | -23.26608 | -47.27241 | 2025-11-15 12:01:00 | TERRA_M-T | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 7cc029f7-45ee-3128-8405-b1e6a2bfa082 | -19.95315 | -44.35712 | 2025-11-15 12:01:00 | TERRA_M-T | JUATUBA | MINAS GERAIS | Brasil | 3136652 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| b129bdf3-3cc8-3c69-a2b1-6a05d181a992 | -19.96226 | -44.35841 | 2025-11-15 12:01:00 | TERRA_M-T | JUATUBA | MINAS GERAIS | Brasil | 3136652 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 92c70c48-7f41-370e-b93a-33f037c2b0f5 | -20.27877 | -45.99333 | 2025-11-15 12:01:00 | TERRA_M-T | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 6df40503-cd5f-3624-93ba-edbf91f0d9c7 | -19.25737 | -44.60086 | 2025-11-15 12:01:00 | TERRA_M-T | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8bf02b3f-8c50-3bd9-9e7f-d4bf621b289e | -1.2294 | -47.6214 | 2025-11-15 12:30:00 | GOES-19 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 130.6 |
| 3f8bd627-3f87-3c95-ac30-3f160073be7c | -3.9895 | -44.2813 | 2025-11-15 12:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 0dcf6639-4cc0-300a-9255-489cd58fcf6a | -3.6663 | -42.1781 | 2025-11-15 12:30:00 | GOES-19 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 160.9 |
| 7a209b9b-5b7c-31fc-b4c6-25be70ceabae | -4.1048 | -50.0647 | 2025-11-15 12:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 07b1ede9-8ea6-3ee7-adf1-6e7b868325d8 | -4.3621 | -44.353 | 2025-11-15 12:30:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 0e49cfdb-3581-3991-85a3-e2237ea371fb | -4.1048 | -50.0647 | 2025-11-15 12:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| b8ccfbb8-0883-34a5-acc1-e4623ee7f9b9 | -3.5914 | -42.2056 | 2025-11-15 12:40:00 | GOES-19 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 83.2 |
| d68d7dc7-30df-3c12-87a2-90f2aa0ba36d | -7.1129 | -42.7254 | 2025-11-15 12:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 83.9 |
| cabda24d-40d0-3c4c-94ac-01e5c9ff4c7f | -3.9897 | -44.2584 | 2025-11-15 12:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 57089926-3012-3096-9481-f518c47259ac | -3.6663 | -42.1781 | 2025-11-15 12:40:00 | GOES-19 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 75.8 |
| 907d38ca-a113-356d-b05f-fc1856bc7294 | -7.1126 | -42.749 | 2025-11-15 12:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 80.5 |
| 3061a202-45e8-37e8-bb82-39b28a556055 | -6.7339 | -42.9498 | 2025-11-15 12:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 74.3 |
| f903fc9c-4d4d-3483-a7cf-c4b67d80d757 | -3.9895 | -44.2813 | 2025-11-15 12:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| cacfc811-9faa-3d4c-af31-78c1538bd313 | -4.0083 | -44.2575 | 2025-11-15 12:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 3dd30ff6-4db3-36c8-aab8-bb8a623a8b98 | -7.1129 | -42.7254 | 2025-11-15 12:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 75.3 |
| ea3437bd-65f3-3905-9419-7834bec86873 | -7.492 | -42.5452 | 2025-11-15 12:50:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 90.3 |
| 89921f0e-33cb-3bc9-8f61-d65d91364481 | -7.9792 | -38.6285 | 2025-11-15 12:50:00 | GOES-19 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 131.4 |
| cca34d84-b8c8-325c-b580-a78f3ccc4d26 | -5.5127 | -40.9765 | 2025-11-15 12:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 80.5 |
| 012614e5-4aa6-3f36-bf3a-97b464e6a51d | -4.0524 | -40.3975 | 2025-11-15 12:50:00 | GOES-19 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 91.3 |
| 840b3581-9236-3cb7-af3c-c6cef66906c5 | -3.9897 | -44.2584 | 2025-11-15 12:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| b3aee545-8c6e-368e-9690-53656c5a2efe | -8.225 | -40.0581 | 2025-11-15 12:50:00 | GOES-19 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 82.6 |
| a407029a-05f9-3b05-8a3a-ae5820c86fcb | -7.4917 | -42.5689 | 2025-11-15 12:50:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 92.0 |
| 73fd9f9b-045e-3100-be2d-18c743b31354 | -3.6652 | -42.3675 | 2025-11-15 12:50:00 | GOES-19 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 95.1 |
| cfce6768-a858-3801-9098-448279851939 | -4.105 | -50.0436 | 2025-11-15 12:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| f8012557-d6f1-3195-b243-82db68f01325 | -7.1126 | -42.749 | 2025-11-15 12:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 64.7 |
| 6272fee5-ac0f-30dd-a62a-fde82714b583 | -6.7339 | -42.9498 | 2025-11-15 12:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.2 |


[Clique aqui para ver as próximas entradas](README61.md)
