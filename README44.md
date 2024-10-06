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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 42f00bb1-44e0-31a2-890b-9ff0d07de0e6 | -17.63747 | -44.42047 | 2024-10-06 03:34:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b4fba52a-bf72-3c9c-84c3-19d201800fce | -17.63548 | -44.41654 | 2024-10-06 03:34:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bc10b50d-6f12-3f36-900a-9219392305d3 | -17.63488 | -44.40586 | 2024-10-06 03:34:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fae4c60c-f36f-3387-9e39-1fa7974b55ee | -17.63477 | -44.41988 | 2024-10-06 03:34:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6f68c013-997c-332c-a69d-3dd347849f4a | -17.63404 | -44.42333 | 2024-10-06 03:34:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e76fbe25-4d68-36f9-8df0-c68043c74151 | -17.63276 | -44.41616 | 2024-10-06 03:34:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2494b52b-0b6a-30f8-bc0a-aaeee93fa638 | -17.6323 | -44.40522 | 2024-10-06 03:34:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 57faa51e-9f33-3196-b6aa-0d869ea095d4 | -17.63207 | -44.41954 | 2024-10-06 03:34:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 860b6b36-1f1a-301f-bd1e-06b8ff06a2dc | -17.63136 | -44.42299 | 2024-10-06 03:34:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ac784ad5-c103-3e88-aecc-2354580584f1 | -17.63081 | -46.96878 | 2024-10-06 03:34:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 32aac1b3-72ca-3c06-9d47-7bf944ffa10c | -17.62937 | -44.41895 | 2024-10-06 03:34:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e185e7c6-5e9f-3ee4-b5ce-5cb7ef095d99 | -17.62776 | -46.96552 | 2024-10-06 03:34:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 55468411-ebe2-328c-b1aa-a5b627e39a23 | -17.62668 | -44.41858 | 2024-10-06 03:34:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 33d2794b-c631-3982-ae74-33e9b6712bc9 | -17.62129 | -44.41764 | 2024-10-06 03:34:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| abc791b5-59c1-3d81-ab37-9c52652a7796 | -17.61858 | -44.41707 | 2024-10-06 03:34:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0d66db26-296a-3c1e-b408-4fff51336720 | -17.61784 | -44.42055 | 2024-10-06 03:34:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 2c6881ec-9c2f-3aac-9a1e-3fd6ecd65bbf | -17.61709 | -44.42403 | 2024-10-06 03:34:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 36d3b8df-be7d-3332-a754-cc10fdeae05b | -17.61662 | -44.41318 | 2024-10-06 03:34:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 77dab828-7fba-346e-99a5-301faf465ace | -17.61589 | -44.41669 | 2024-10-06 03:34:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 23240e05-0805-37be-b294-f52fa22f11b1 | -17.61517 | -44.42019 | 2024-10-06 03:34:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 67e7e6de-b1e5-3db9-8f79-d420baa4de4c | -17.61445 | -44.42367 | 2024-10-06 03:34:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 75715435-7116-3254-b8a6-9c71d4b8ccd3 | -17.61373 | -44.42715 | 2024-10-06 03:34:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 41e1ee1f-af54-355b-883f-8e7b6a91fc0c | -17.382 | -42.65216 | 2024-10-06 03:34:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 67965f8d-1062-3108-93c2-f5c55a6d1794 | -16.96975 | -47.12661 | 2024-10-06 03:34:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 442d5d17-2657-39f9-ba0f-cc9edc57e16c | -16.96346 | -47.12484 | 2024-10-06 03:34:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 799f866d-3b49-3005-a8c8-ad70873bf060 | -16.95706 | -47.12357 | 2024-10-06 03:34:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 864cc7c6-b42e-3823-921b-84a6b547db60 | -16.9562 | -47.12125 | 2024-10-06 03:34:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 99013062-0aac-3839-b598-baffb48957e8 | -16.95493 | -47.12706 | 2024-10-06 03:34:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1f7d3e19-dcaf-38e8-bde0-43c4b6213525 | -16.95069 | -47.12218 | 2024-10-06 03:34:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c5371610-b454-3bb6-af7d-a63f4e237e5d | -16.9494 | -47.12786 | 2024-10-06 03:34:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 43995b6b-8ced-3a0d-844d-3720942262b8 | -16.94858 | -47.12551 | 2024-10-06 03:34:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| df41f73e-a1be-3638-bcb2-0f886a0d3d1b | -16.93848 | -47.11068 | 2024-10-06 03:34:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4619edc2-dd7c-3e36-b1c2-c0a187db3ecc | -16.93719 | -47.11654 | 2024-10-06 03:34:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ece5735c-f00e-3fd3-8dd0-64b688a327c5 | -16.91908 | -47.17282 | 2024-10-06 03:34:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 33fecba9-480b-37a6-bbf7-c1d793c26f7a | -16.91854 | -47.17074 | 2024-10-06 03:34:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 66cc134d-29e7-32c8-bf20-18cccaa83e12 | -16.91737 | -47.17605 | 2024-10-06 03:34:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 14.9 |
| a915e472-28ca-3f6b-aa2c-70f4fff13f51 | -16.91475 | -47.15755 | 2024-10-06 03:34:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1ae91e3e-5e07-3600-a2eb-c61548e04bc8 | -16.91342 | -47.16359 | 2024-10-06 03:34:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1fdea624-5d6e-3b2a-a44c-d0ad4aacc335 | -16.91268 | -47.17142 | 2024-10-06 03:34:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 6ce62be9-f341-3f1b-83f1-9c782440b12a | -16.91218 | -47.16917 | 2024-10-06 03:34:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d697526d-fac8-3a13-ad3f-7c70c0f5be51 | -16.91144 | -47.17685 | 2024-10-06 03:34:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 6c55ef23-36bf-3563-978c-2ca1fa805507 | -16.91096 | -47.17466 | 2024-10-06 03:34:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 681a1c56-ed41-3876-bceb-96c725ea01c3 | -16.90893 | -47.15847 | 2024-10-06 03:34:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4b6538cc-427a-30b8-8312-79c9063679d6 | -16.90838 | -47.15605 | 2024-10-06 03:34:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6cee1228-5719-3ae5-9da9-8161b7aefab9 | -16.90762 | -47.16422 | 2024-10-06 03:34:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5029c5d0-127d-3f82-8236-d4b6495aad26 | -16.90707 | -47.16198 | 2024-10-06 03:34:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 0dc983e6-4f5a-37ab-a870-455d78a5768b | -16.90644 | -47.16938 | 2024-10-06 03:34:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| ad96a756-af70-391b-a9cb-53987bd3b7af | -16.9059 | -47.16723 | 2024-10-06 03:34:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a915e2eb-edd5-38b8-972d-f22119fae38e | -16.90515 | -47.17501 | 2024-10-06 03:34:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 41d9f052-b0f7-3f5d-b993-9c263d71833a | -16.90472 | -47.17255 | 2024-10-06 03:34:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 8eebae63-de64-3864-b059-3714a73aa054 | -15.90045 | -46.87939 | 2024-10-06 03:34:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3638f415-47dd-3b19-a65a-684cebe1cefd | -15.89953 | -46.87988 | 2024-10-06 03:34:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 20c62b8b-c104-3cef-a4a6-58d272dde378 | -2.8166 | -48.6867 | 2024-10-06 03:35:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 105.4 |
| b6613536-24c1-3f9d-99dc-c7d1b14992ee | -2.8165 | -48.7082 | 2024-10-06 03:35:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| a4c0b011-14fb-3555-90b3-fb7fe041a9d4 | -2.7981 | -48.6873 | 2024-10-06 03:35:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 8b040f0b-3858-37ac-885a-f5aa30374985 | -3.1315 | -48.591 | 2024-10-06 03:35:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| e38dabc3-d9d4-3108-9806-66133772ebb6 | -3.1314 | -48.6125 | 2024-10-06 03:35:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 4249b12b-8698-335a-ae90-7ccb1220ced5 | -3.1313 | -48.6339 | 2024-10-06 03:35:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 4f09db25-0636-3b54-a919-cc6debeba0ec | -3.1129 | -48.6131 | 2024-10-06 03:35:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| daa54026-657f-316c-8a3e-d29f788d383e | -3.4195 | -50.3844 | 2024-10-06 03:35:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 1b2fdc99-f721-334e-842f-cb173b0fcdc4 | -3.8464 | -46.4714 | 2024-10-06 03:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 65.8 |
| c6fd8132-ae29-314e-a31b-4e274881c4fe | -5.0139 | -49.7696 | 2024-10-06 03:35:34 | GOES-16 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 44bf8faf-f19a-3559-b9f6-1622e8569663 | -5.5718 | -44.87 | 2024-10-06 03:35:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 31744d1d-5d0d-3b8e-9a3b-8fe460bf8922 | -5.5716 | -44.8927 | 2024-10-06 03:35:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 878b3680-748b-3d94-9562-d3285ddaa8c3 | -9.3835 | -51.0881 | 2024-10-06 03:35:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 5a4e8bb7-e5ec-3747-a52f-8aed20a4359a | -9.3467 | -46.5365 | 2024-10-06 03:35:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 107.4 |
| e15879f4-a58c-3f28-906c-19c15ad41385 | -9.3464 | -46.5589 | 2024-10-06 03:35:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 4d902331-fe70-3c9d-9538-b2e3f5fcc58b | -9.3278 | -46.5385 | 2024-10-06 03:35:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| fff77ce3-6065-3459-9ad5-d337b516d13d | -9.3638 | -64.319 | 2024-10-06 03:36:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.3 |
| dcc1eaa0-120d-37be-9cfe-cb6541770c91 | -9.7072 | -47.8068 | 2024-10-06 03:36:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 9c3448f8-e2e7-3e45-85f3-b6e866cba94d | -9.7069 | -47.8288 | 2024-10-06 03:36:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 230ffb67-f162-3ec3-b513-01aad5dce37d | -9.6883 | -47.8088 | 2024-10-06 03:36:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 60352729-902f-335c-bf63-ec316a1bac24 | -9.688 | -47.8308 | 2024-10-06 03:36:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 114.6 |
| cfc4f38e-ea14-3a14-9bdf-a33d6fb7fcfe | -9.6691 | -47.8328 | 2024-10-06 03:36:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 276551f0-620b-34f7-a887-1a39fef8babc | -9.8552 | -60.2966 | 2024-10-06 03:36:02 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 5f226c50-859d-34b8-a07f-4d9b9fae0867 | -9.6965 | -64.6262 | 2024-10-06 03:36:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 120.3 |
| cf258061-8336-36fc-84a2-de819418216d | -9.6964 | -64.645 | 2024-10-06 03:36:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 83ca75d9-71f0-34a3-845e-c2adc42c4563 | -9.6779 | -64.6269 | 2024-10-06 03:36:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 149.5 |
| f5e5b821-f8a7-304c-abbc-654b66ecaf86 | -9.6778 | -64.6457 | 2024-10-06 03:36:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 983bdc71-8909-3c4b-b0d7-6d99c5373359 | -12.6092 | -53.1129 | 2024-10-06 03:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 08766b28-e257-3785-945b-84fd7d0238f6 | -12.6089 | -53.1338 | 2024-10-06 03:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 44f80c47-91e3-3f1e-acae-fdfc5b16827f | -12.7825 | -50.5112 | 2024-10-06 03:36:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| f79efdf9-a313-386e-8361-906f02e7e3f5 | -12.7822 | -50.5328 | 2024-10-06 03:36:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 183.3 |
| b6a879d9-9c3c-3d2e-848d-8206e2c17c55 | -12.7634 | -50.5136 | 2024-10-06 03:36:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 176.2 |
| f3438bae-53d1-3281-853a-4efc6aa0aa3c | -12.763 | -50.5352 | 2024-10-06 03:36:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 504.8 |
| cedb20af-f7e3-38cb-8483-f7200bc9160f | -12.7627 | -50.5567 | 2024-10-06 03:36:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 11104115-5f2f-3505-aa0f-3dbf22df4095 | -12.7439 | -50.5376 | 2024-10-06 03:36:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 53147131-3952-30fd-9ae2-da5a37038f6b | -12.6726 | -54.0189 | 2024-10-06 03:36:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 3b82da8c-2390-353d-9729-0f2ea055a85f | -12.6535 | -54.0208 | 2024-10-06 03:36:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| dfc788ae-b8fd-3893-9e05-3d23dff8ecb8 | -12.6532 | -54.0415 | 2024-10-06 03:36:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 4e077c5f-6cbf-3a7d-89ba-0e3092a2f014 | -12.6283 | -53.1108 | 2024-10-06 03:36:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 6f0ee1b3-f781-3db9-8805-4e63249f1cf9 | -12.628 | -53.1317 | 2024-10-06 03:36:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 151047c4-08a5-30f4-b4f1-a997e2398a69 | -13.3786 | -61.9582 | 2024-10-06 03:36:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 4158c8e3-5375-3a3d-9b99-ee925ae2f634 | -13.3976 | -61.957 | 2024-10-06 03:36:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 70.7 |
| cd022add-b45e-3f58-8697-a914977696ed | -13.6724 | -51.1911 | 2024-10-06 03:36:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 4df86f31-1fa2-3c69-b376-882a89addc91 | -16.3764 | -57.3663 | 2024-10-06 03:36:38 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.4 |
| 364469ab-2797-3f26-9934-773d40597aca | -16.5739 | -57.201 | 2024-10-06 03:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.9 |
| e3021681-84b5-3da9-bbf8-d37d8f1b5429 | -16.5736 | -57.2215 | 2024-10-06 03:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.4 |
| 172e5386-7a94-3fa2-b2a7-b21f9b4b9acb | -16.5544 | -57.2032 | 2024-10-06 03:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 145.4 |
| 62d76594-15b4-37d8-8f6e-9cb65504de49 | -16.554 | -57.2237 | 2024-10-06 03:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 178.4 |


[Clique aqui para ver as próximas entradas](README45.md)
