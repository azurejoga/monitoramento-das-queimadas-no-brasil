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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d6d37cd-7d43-32fb-bf41-3c411e532d3f | -7.07687 | -44.9327 | 2025-10-31 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3863254b-b346-3e97-aa6f-d4fbc82bcd9f | -3.94306 | -46.97436 | 2025-10-31 03:47:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eeaad532-db54-31e7-9d8c-4ded62948600 | -7.07707 | -44.93334 | 2025-10-31 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 66458ac8-0a0e-3aea-ac70-6209f05007af | -7.16004 | -39.4584 | 2025-10-31 03:47:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b6d6318b-7cce-3d80-9a3c-7a0e04540b14 | -8.08622 | -45.1365 | 2025-10-31 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1b21aea8-b9ba-3850-a5e9-d4a1ae025017 | -4.85534 | -42.73468 | 2025-10-31 03:47:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| d7c52370-774b-3db1-abff-5d935f1c6738 | -8.16581 | -45.50059 | 2025-10-31 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d98bf33c-5d80-3acc-9676-2c8a6be9113c | -13.68435 | -44.72764 | 2025-10-31 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 22.1 |
| f497932b-8e73-32bd-895e-57b92ce548cb | -10.93101 | -44.16358 | 2025-10-31 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 1f374c29-9d40-3e21-ae38-431009dc63f6 | -7.61504 | -46.47612 | 2025-10-31 03:47:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8ed6e163-2624-3267-bb04-71b508a5b70d | -10.64301 | -45.24602 | 2025-10-31 03:47:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2a9e47fa-43a8-321f-a388-66dca881741e | -10.53524 | -44.92619 | 2025-10-31 03:47:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c236ed7-6e64-3d2a-8404-7a473be11d78 | -9.42263 | -46.89342 | 2025-10-31 03:47:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f05e5e7f-4db3-391c-b520-032c0992fe15 | -7.33669 | -42.73559 | 2025-10-31 03:47:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 93d3a24f-2468-39bc-8a4e-61fbf9800a13 | -16.37434 | -45.25377 | 2025-10-31 03:47:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fa419bdf-303c-3918-a746-ac8e45cde7ff | -4.45909 | -45.76145 | 2025-10-31 03:47:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ac242d0d-a164-3ad2-9a35-13d77e68e162 | -9.52587 | -47.27159 | 2025-10-31 03:47:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e0a6fcbb-373d-3975-872c-032fb8cb8b04 | -6.51812 | -40.797 | 2025-10-31 03:47:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bf282e51-a1c8-3e2d-8828-a22f3b18a6c4 | -9.86711 | -44.86929 | 2025-10-31 03:47:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 66445401-a6d1-3f61-a1bf-f2a2a1e04a4f | -9.34424 | -46.5962 | 2025-10-31 03:47:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7e13579d-6d2f-3485-9b0c-724d3a6c1b25 | -4.47344 | -43.44118 | 2025-10-31 03:47:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ca4fa1aa-14fa-392a-972b-f11e54f7d263 | -6.1249 | -41.87286 | 2025-10-31 03:47:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 3cdabc79-43b6-3612-aaee-dbb5cd62ae71 | -7.4444 | -41.22065 | 2025-10-31 03:47:00 | NPP-375D | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 53348b86-ad68-3848-b45c-613b38f884c3 | -6.14612 | -41.6865 | 2025-10-31 03:47:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| f4146e47-e91c-3bd0-84f5-5617a32eb660 | -4.67424 | -46.52124 | 2025-10-31 03:47:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a1f00f5e-683f-375a-9001-382e73919630 | -4.83827 | -40.73903 | 2025-10-31 03:47:00 | NPP-375D | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3cf308de-9654-38f2-a05b-da6891b906bc | -6.92354 | -42.24532 | 2025-10-31 03:47:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f4423473-a6eb-3a6c-ae64-14d0ac7b0311 | -4.90465 | -45.72683 | 2025-10-31 03:47:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 964717fc-6cdb-3a48-bd66-3ba4c86f1994 | -7.60824 | -46.47939 | 2025-10-31 03:47:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 606fd25b-85f5-3fb7-9b55-117cdd35b82c | -5.25935 | -45.5183 | 2025-10-31 03:47:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dcbc0b0c-8689-30e3-b09b-3de27a1a18be | -13.89905 | -47.35185 | 2025-10-31 03:47:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 03813c12-0c9e-31cb-9480-3bfcb2749079 | -9.85791 | -44.86083 | 2025-10-31 03:47:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b6856d7c-de64-377f-b9fa-05fd07295cc0 | -7.03607 | -41.47367 | 2025-10-31 03:47:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7e4fc493-5ff1-3306-80d4-73b93c95496c | -5.44178 | -37.6037 | 2025-10-31 03:47:00 | NPP-375D | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5b984461-dfc0-3a86-9c66-7ff239dbe646 | -6.05498 | -44.86456 | 2025-10-31 03:47:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4dc715f4-b5d4-3888-a878-3397b0e3d1c7 | -6.9317 | -46.01318 | 2025-10-31 03:47:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9367d2e2-69de-3f4f-9680-18d930ed893e | -14.12921 | -44.1834 | 2025-10-31 03:47:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e3e64c6-0221-3dd6-b6e7-bffc4025692d | -8.16512 | -45.50428 | 2025-10-31 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f34b6256-f681-34bb-98b1-5d4976787ff2 | -6.13537 | -41.70621 | 2025-10-31 03:47:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 8451dafd-0a67-3bfc-9e6e-37f45e422a85 | -7.36911 | -44.63284 | 2025-10-31 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5cfb6681-2ad7-3b89-aae9-b44d81b2f347 | -9.97883 | -45.16584 | 2025-10-31 03:47:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c245787b-fda2-3a37-98a8-68d41cfa8ffc | -9.52071 | -47.26548 | 2025-10-31 03:47:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0c9e490e-45e1-3aa4-8d15-156841389947 | -11.05533 | -44.02338 | 2025-10-31 03:47:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1494d859-b0c9-3200-b0ef-8ceaaf14c925 | -9.42344 | -46.88924 | 2025-10-31 03:47:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bb300346-b164-3730-b7c0-879439f7bc95 | -13.69977 | -44.20127 | 2025-10-31 03:47:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5aef33f4-6c7a-390a-a481-e77749367582 | -7.77307 | -46.4792 | 2025-10-31 03:47:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 22a4c56b-6267-33a0-9d56-db401a3dc075 | -7.08314 | -44.93097 | 2025-10-31 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2e29aa18-d952-3064-89ea-d9bed5b746e9 | -11.05053 | -44.02243 | 2025-10-31 03:47:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a5a20e26-88f1-36fa-b07c-9f622d8e37e7 | -5.47394 | -44.32072 | 2025-10-31 03:47:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 18e6275e-96ca-39f1-9b8c-3270c6b8da43 | -7.07753 | -44.92911 | 2025-10-31 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b46ed8ce-f50e-3886-bb41-54802c1c18c1 | -8.18307 | -45.68903 | 2025-10-31 03:47:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66c77dea-0a18-3438-9fd5-a9f08e982ad7 | -5.11758 | -43.29553 | 2025-10-31 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 29aa6584-1df4-3c39-8934-a97421e08787 | -13.8942 | -47.34666 | 2025-10-31 03:47:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1b59529b-24fb-37ce-aa87-134fe07793b7 | -7.8127 | -46.3995 | 2025-10-31 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec1776da-e689-39b0-aeb2-ac792f37c568 | -7.32069 | -42.55079 | 2025-10-31 03:47:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f7e7c99e-9abd-3894-9feb-5066d5667eb2 | -9.73419 | -48.03318 | 2025-10-31 03:47:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8fef20bf-3bf2-3f53-a399-f42c6c744a44 | -16.36961 | -45.25277 | 2025-10-31 03:47:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 60bb9f14-134f-3415-8091-2050c81147be | -9.85851 | -44.85756 | 2025-10-31 03:47:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4f57d0db-d411-32cf-ae57-49a5153e09eb | -5.71773 | -44.53629 | 2025-10-31 03:47:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68d0dce9-d186-3fbb-acc6-11aa6085474a | -4.86024 | -42.73551 | 2025-10-31 03:47:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 9b534471-9d73-3864-a799-dbb3dbe23b83 | -13.38678 | -47.33999 | 2025-10-31 03:47:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ab74b74-15bc-3a4c-ba46-db115a0d3fca | -7.08297 | -44.9303 | 2025-10-31 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| df6b4ef5-009f-32ce-869d-30014ba2a001 | -5.62192 | -45.98271 | 2025-10-31 03:47:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b5c4b5e-4f77-3fb1-bce2-b5cba49140a9 | -6.07724 | -37.46601 | 2025-10-31 03:47:00 | NPP-375D | JANDUÍS | RIO GRANDE DO NORTE | Brasil | 2405207 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 007d3933-da9a-3acb-861f-379bed6ba132 | -5.9548 | -45.5582 | 2025-10-31 03:47:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4672e2da-b144-3558-9aa0-940b847deb04 | -5.44531 | -37.60429 | 2025-10-31 03:47:00 | NPP-375D | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a590fa6c-7dd9-3c21-b5f2-0b6907afbea6 | -10.88556 | -44.32633 | 2025-10-31 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de7adf7d-806b-3e61-b6bf-4ae175f21312 | -8.31884 | -45.37823 | 2025-10-31 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d77968bb-0086-33ba-8a18-364c28df695d | -4.67808 | -45.81089 | 2025-10-31 03:47:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e548405e-6a06-356b-a7ad-1d6829bc921f | -7.03952 | -41.47617 | 2025-10-31 03:47:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6560f375-49bc-36f4-881a-a7376d5c9822 | -13.78895 | -44.3647 | 2025-10-31 03:47:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 24d0959e-2266-39d4-8caa-4b2e9da5b607 | -6.21326 | -43.94248 | 2025-10-31 03:47:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b30665b4-651c-33c1-855d-65930981d2e4 | -13.5947 | -47.34373 | 2025-10-31 03:47:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a43ba77b-2dab-307a-b800-612ae8dc6121 | -8.31384 | -45.37438 | 2025-10-31 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1631eb2b-2ae9-3ebe-b25b-8eeba253c2a5 | -10.92704 | -44.76654 | 2025-10-31 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1cffffab-dfe1-35ff-81ca-4023f4464c3c | -4.30406 | -41.43671 | 2025-10-31 03:47:00 | NPP-375D | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6fec4c1c-6497-3861-9237-d231b33d5b30 | -10.93 | -44.16901 | 2025-10-31 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 077f5109-5b57-3a30-8849-4f86c75cb0bc | -9.85731 | -44.8641 | 2025-10-31 03:47:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 09828e4e-b6dc-3a33-a7b3-7ac6d6bb4ce9 | -5.25585 | -45.5158 | 2025-10-31 03:47:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cdbbd4a1-78f4-3729-aa5e-103553736978 | -9.72947 | -48.02975 | 2025-10-31 03:47:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4b7ec2b4-c5e5-34a9-8e1d-95d8ca9dd438 | -8.16033 | -45.4683 | 2025-10-31 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb8eb174-0456-3200-94f7-5d2b9ed80c36 | -6.52712 | -43.71151 | 2025-10-31 03:47:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a330f35e-5808-3436-910e-a3cce19a6540 | -3.77638 | -45.17093 | 2025-10-31 03:47:00 | NPP-375D | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 66bbfbdb-c358-36c0-9727-7824d5e453bd | -5.87974 | -44.70729 | 2025-10-31 03:47:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 228cf51b-9923-3745-8d06-271650fdf0df | -8.55852 | -40.74008 | 2025-10-31 03:47:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3961d6be-211b-3a20-a8dc-3736b8e11beb | -7.23174 | -44.32356 | 2025-10-31 03:47:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f8257bbc-2c97-3eb1-b2eb-264e07a02a30 | -5.7946 | -40.80742 | 2025-10-31 03:47:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 18870503-f712-3de6-b644-c0de626d3792 | -8.39445 | -41.84475 | 2025-10-31 03:47:00 | NPP-375D | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9a16fc12-88dd-3039-9aad-f63600f5f582 | -9.87809 | -44.868 | 2025-10-31 03:47:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d541a7b-35ea-38a1-a9da-ad797e917e90 | -14.74241 | -42.45849 | 2025-10-31 03:47:00 | NPP-375D | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0f6b2bc6-61fa-30c2-8e6e-4dad028c4a4f | -4.72458 | -44.40477 | 2025-10-31 03:47:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac98a127-72f3-3b81-80b1-c344f7f0e82d | -6.05435 | -44.86809 | 2025-10-31 03:47:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e5fc0ab-1710-3dc3-8a70-e9e6e76a8c89 | -8.18663 | -45.70143 | 2025-10-31 03:47:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60c05d0b-d36f-3055-b077-56f869a5866b | -5.70148 | -43.15148 | 2025-10-31 03:47:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 5.1 |
| ffb5df68-66c4-30aa-85d9-e60e91d38ab5 | -9.34837 | -46.59441 | 2025-10-31 03:47:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 41d38c3c-2f62-38cd-94d2-c057006eab67 | -11.35892 | -42.28711 | 2025-10-31 03:47:00 | NPP-375D | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 4ae40bc6-c5f7-337a-877e-2ccf74205323 | -13.39084 | -47.3453 | 2025-10-31 03:47:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ee48e97-a1a4-3971-b329-636976481362 | -13.8949 | -47.34318 | 2025-10-31 03:47:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 33ff1aa8-4a46-360f-83fa-cc783b462283 | -9.73048 | -48.02468 | 2025-10-31 03:47:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 416f191a-890d-3ef3-962c-20f047f30479 | -12.94122 | -47.92714 | 2025-10-31 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README8.md)
