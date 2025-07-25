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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 32f37849-0e87-36c0-a27c-00832fdd71bf | -3.07407 | -52.43866 | 2025-07-25 04:21:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 774043cf-4f69-37f8-80f5-f97df6ed59fe | -8.51356 | -43.31877 | 2025-07-25 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 30ff3256-29e8-361d-ac6e-cdc6031bab75 | -7.26428 | -43.06963 | 2025-07-25 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 6ec72df7-d534-36f3-a225-f5ba49a960f2 | -8.08491 | -43.15556 | 2025-07-25 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 229f4a67-097b-315b-83eb-e8e997b667c4 | -9.02457 | -45.3344 | 2025-07-25 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29c4a2cf-2481-35bd-8ddb-3ba9eb8adfff | -7.24835 | -43.05959 | 2025-07-25 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| f5566d59-4d75-3cc0-a756-70701c5d9160 | -8.06334 | -49.72049 | 2025-07-25 04:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9abc28ef-448a-37c3-8fd4-f26ee3bacd69 | -7.10942 | -43.32695 | 2025-07-25 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 91ac58e7-c3c5-32b9-b313-4a42eb29a1d3 | -9.00799 | -45.33175 | 2025-07-25 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02e2c16a-5285-3456-b25d-e2a669d6354e | -6.91813 | -44.2907 | 2025-07-25 04:21:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2dd44497-9912-39e4-b726-d5e65a79eb4b | -8.3001 | -44.97271 | 2025-07-25 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 677adfda-167c-393a-bce5-08976c0d3dc6 | -7.89672 | -42.63893 | 2025-07-25 04:21:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1f60df64-1cee-34cf-980a-c7ee106b122a | -8.51071 | -43.31453 | 2025-07-25 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| e64a4dd5-8c47-3340-a30e-15f5d73fd0ff | -6.48201 | -44.99676 | 2025-07-25 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f2a24f3-637c-38c7-96cb-5f990e08bcab | -8.83161 | -45.59345 | 2025-07-25 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b1933d2a-dbc4-33fc-a8b0-35d79f09853d | -6.82395 | -43.98952 | 2025-07-25 04:21:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 651e956c-bdf7-340a-b2c7-0ddc47769434 | -8.13054 | -49.58786 | 2025-07-25 04:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 997b2a78-f13e-3e95-ad44-c7bf0fca705b | -11.44532 | -45.12757 | 2025-07-25 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6343c303-1d97-31fe-803e-ae1bbfe6392f | -7.25404 | -43.06805 | 2025-07-25 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| e60dab06-66cf-317b-9662-2d8b0bd9286b | -4.31199 | -47.98202 | 2025-07-25 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4cea834f-c96e-3889-aa6d-7ffdbb5b5b0a | -7.91432 | -44.08434 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 833764af-e0b5-336c-8991-16eda30a4895 | -9.85191 | -44.70201 | 2025-07-25 04:21:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb60602d-c104-33ce-ad79-90726f95ea31 | -7.91213 | -44.09848 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| eb26c5dc-d661-3983-a4a9-531478266313 | -7.35228 | -43.43029 | 2025-07-25 04:21:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0edd18a7-a861-3ae1-a99e-66759227ef06 | -3.30803 | -51.66623 | 2025-07-25 04:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 04cabffa-baf3-3334-bcfe-8cf819f3dd68 | -4.34808 | -47.68809 | 2025-07-25 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ccd2edc9-f742-3ab1-a96c-d374f37631a0 | -4.02836 | -48.06178 | 2025-07-25 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c716505e-e289-3fbb-80bd-6d148b7c7c8c | -8.897 | -45.58604 | 2025-07-25 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1e7ab75-9d7f-3588-81a6-a5ad5a4f57ea | -9.59382 | -43.87361 | 2025-07-25 04:21:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7d1d2d48-14d1-3e9d-b9c5-d4c97ffd9e13 | -3.30557 | -51.66435 | 2025-07-25 04:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e71e81c-5aec-3b9d-9b50-60e9d9f7f755 | -7.23563 | -44.79258 | 2025-07-25 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f830775a-4bc6-3246-9466-5f44b124acf4 | -7.30223 | -44.02092 | 2025-07-25 04:21:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 00288a00-13af-3f55-81fc-571a2f5269e6 | -9.42976 | -44.73651 | 2025-07-25 04:21:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d32f5ed3-23c8-39c6-affa-e7ed5ebb7fac | -7.92046 | -44.08893 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7f46abb4-3d7e-382d-b16e-9a48019334ed | -11.44089 | -45.13412 | 2025-07-25 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1057784-08f4-3c83-a0ec-c35345ff3b4d | -7.9266 | -44.09351 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0521ab81-9fb7-3ebd-aa5a-20c0474a863d | -6.95129 | -44.55592 | 2025-07-25 04:21:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 830f9535-ddd0-3bb2-b04b-d69df1d53e31 | -4.57697 | -48.01891 | 2025-07-25 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 95e45f52-7432-3d79-9d3a-511657c2f8b3 | -3.74448 | -49.04747 | 2025-07-25 04:21:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 75ee7b6a-5c33-37c5-be9b-dcdb3a18c927 | -10.44776 | -49.05529 | 2025-07-25 04:21:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cd27dda3-efe8-30f0-95e8-9915d9efb14f | -8.51014 | -43.31824 | 2025-07-25 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.0 |
| d769c754-81a2-3f11-a9d9-e15788ad6619 | -11.45697 | -45.11853 | 2025-07-25 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 37655951-45b2-37b8-902c-86b51169c6ca | -9.07804 | -46.63344 | 2025-07-25 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 33aa6989-a305-31bc-bece-f8161f648bc0 | -4.64672 | -46.46545 | 2025-07-25 04:21:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d17cdbf8-08f9-3ad5-ae66-8bff097cb73f | -7.85641 | -48.21783 | 2025-07-25 04:21:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| feecf1da-8cf6-324a-983f-c569e71be33d | -11.44587 | -45.12403 | 2025-07-25 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9696762e-b1ed-32a9-91ba-a697efac0649 | -8.85601 | -45.60812 | 2025-07-25 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 246f4b08-ca7b-35fc-8386-fd272f90537b | -9.0008 | -45.33417 | 2025-07-25 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 939cf6dd-ae6a-3da8-8ca8-63e9426aad3e | -7.86437 | -48.21479 | 2025-07-25 04:21:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1a352f1-02c2-33c1-ab40-652d124e889a | -10.46407 | -52.73145 | 2025-07-25 04:21:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 562a0234-ccea-3b54-aa3c-3e0da403d1b1 | -6.98824 | -43.31969 | 2025-07-25 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 69fc5afb-be67-38f0-800a-79e7dd16036f | -10.4289 | -44.18348 | 2025-07-25 04:21:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8eb09a55-17ca-3f28-abe8-2326bfe59cd6 | -10.61304 | -45.24109 | 2025-07-25 04:21:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2e845709-0b28-3b2c-bb85-5d6040f44493 | -10.74552 | -48.18984 | 2025-07-25 04:21:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c430ee2e-4261-3507-b5af-ffa1145f26bf | -7.94051 | -44.09208 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd8e962c-3546-301c-a66c-868e7a2ce634 | -11.45587 | -45.12562 | 2025-07-25 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 347a04b5-25bd-320a-ad1d-c1a184f20614 | -9.37871 | -48.00388 | 2025-07-25 04:21:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 671175fd-b178-3570-ae95-8a662abe4ce7 | -6.95075 | -44.55939 | 2025-07-25 04:21:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 66e96408-2b24-3278-a8c9-de1627e8b4ec | -6.94688 | -44.56234 | 2025-07-25 04:21:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 12fddf78-3910-3093-aaeb-d0761997ed10 | -6.22553 | -44.53083 | 2025-07-25 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 11acff94-670f-383e-adc0-5879d72292de | -7.1457 | -46.09429 | 2025-07-25 04:21:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ddd6556a-e2b0-37ce-a641-acdd6a4c88f8 | -10.80763 | -48.93303 | 2025-07-25 04:21:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 66c22808-3bb9-3e68-8c9f-3d4ecea831b7 | -7.66309 | -44.50431 | 2025-07-25 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d0470351-da6c-320a-8f08-fa606fedb469 | -6.88854 | -44.20044 | 2025-07-25 04:21:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dbdd6c4a-6480-3a2e-94db-d0c731162a86 | -7.10998 | -43.32334 | 2025-07-25 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 52309eb8-6fea-3e4f-b316-149fd63c4907 | -9.02734 | -45.33841 | 2025-07-25 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3e75673b-f2b7-3348-b961-458883d8813f | -7.14628 | -46.09072 | 2025-07-25 04:21:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90354005-8b32-3631-b78c-e9950d02c64d | -7.94161 | -44.08499 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4fe9dac-aab4-361a-b6c4-04e888c957a4 | -8.3349 | -44.94619 | 2025-07-25 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f558b6bf-c0ed-39fe-b47f-4b74e00ccb88 | -10.60917 | -45.24407 | 2025-07-25 04:21:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8535d562-38ce-38c5-bc51-05d9d73e0676 | -10.64017 | -44.7606 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| de2ae75f-599f-3501-a86f-6ba66e61aaa7 | -5.48502 | -42.14946 | 2025-07-25 04:21:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6850ce32-e56f-3fbb-b6d9-6e1b4fe172ec | -7.23673 | -44.78564 | 2025-07-25 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c3537e1-74ce-3e64-ae19-d0b70bc13eca | -7.48028 | -49.23457 | 2025-07-25 04:21:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16808c6e-467f-345e-ba78-c9ac0457eb89 | -7.16619 | -43.47937 | 2025-07-25 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7a6e9a63-46c7-3358-8307-e3e2b4c5c01a | -6.91758 | -44.29418 | 2025-07-25 04:21:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35272aba-2f86-30f0-9d6b-c12a41371738 | -6.95406 | -44.55991 | 2025-07-25 04:21:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 624dab1f-8c53-3eff-b5d1-9321e361987d | -7.09037 | -44.87636 | 2025-07-25 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db5114b8-77b1-3467-bd17-257b95e7035a | -3.74505 | -49.04392 | 2025-07-25 04:21:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 44faf9ef-d472-3480-95a3-1d2eff0c469f | -7.98859 | -43.82651 | 2025-07-25 04:21:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b489e9e6-a260-3c4b-9e80-61982b43688f | -11.4603 | -45.11906 | 2025-07-25 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 9c6e17db-b1e2-3559-8ae8-bc74062d6621 | -3.74139 | -49.04311 | 2025-07-25 04:21:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 120a3fa1-b673-36a5-bbdf-a85500850591 | -7.91991 | -44.09246 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 11977e6a-d8e4-3a31-a804-82e58330b1a9 | -6.87412 | -43.08956 | 2025-07-25 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4bf86057-30c8-33de-bb9b-d6d1656ef3ab | -4.57322 | -48.01831 | 2025-07-25 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8d27fc60-81d9-3c8e-8990-de080013b9ae | -5.5748 | -45.74976 | 2025-07-25 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 678ab90b-0bf0-3151-9bc2-b370b9eba14c | -6.6499 | -43.05343 | 2025-07-25 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bfe742b4-9b19-38ed-be2c-09c2ecc98972 | -10.50006 | -44.87966 | 2025-07-25 04:21:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70c8f031-582d-3bff-868f-4fd87455b2cd | -9.59334 | -46.33807 | 2025-07-25 04:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5811a19-dc40-3479-92b4-463d50015416 | -7.84809 | -44.2114 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 879b180c-e71e-3417-9efe-dbd09ba20f31 | -11.44865 | -45.12811 | 2025-07-25 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| cf10d4ce-e4ab-37b8-b6ca-f3f5ee4a44ac | -6.57657 | -41.48941 | 2025-07-25 04:21:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 22bff9ac-433b-3ea1-9b98-999fdd2a992b | -7.53365 | -42.42256 | 2025-07-25 04:21:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| aedb5f2d-f681-3ef2-b65e-4f85458e61d7 | -8.89201 | -45.59599 | 2025-07-25 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 844c8a92-8237-34ab-8640-eabac68bd813 | -8.06542 | -49.7191 | 2025-07-25 04:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 60070009-882f-31b9-bcf0-d5947dc3da1a | -8.08548 | -43.15184 | 2025-07-25 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 61a445fc-5aaf-3906-9171-3de6b1594dbb | -7.88983 | -43.54297 | 2025-07-25 04:21:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98551434-0ef1-3b4f-9058-e9f01a07330c | -8.07121 | -43.15341 | 2025-07-25 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 0ee8d730-2aa5-3601-b4bc-b82116a54aef | -5.89829 | -45.18716 | 2025-07-25 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8dcbef29-98e3-330d-bc64-79dff5bc825e | -7.90988 | -44.0909 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README16.md)
