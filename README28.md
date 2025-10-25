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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 856c935d-4aef-3db3-90ff-dbf9150d2433 | -4.25395 | -44.57665 | 2025-10-25 04:17:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 36d49cbf-6b59-3b16-b7bb-bdcbbde5437c | -3.87059 | -51.89222 | 2025-10-25 04:17:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1cb5d4ba-7fb3-350c-b20b-8d5ec462ef2c | -3.23457 | -48.75752 | 2025-10-25 04:17:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 19e81fbe-ffae-39bb-a50a-7e13736fe116 | -4.60002 | -49.58879 | 2025-10-25 04:17:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3d2a9a83-b171-384f-b3d4-34b52d1cdc82 | -2.86407 | -50.72608 | 2025-10-25 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bab54ec3-d28d-3cee-993b-793b98aa8430 | -5.46114 | -46.47663 | 2025-10-25 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 320ba1c6-846b-3ada-b0e4-d4042a7a1d69 | -3.40481 | -42.48047 | 2025-10-25 04:17:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5a739c44-9b08-30c1-9470-4ca3d08407e6 | -5.93586 | -43.36819 | 2025-10-25 04:17:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ffefb9dc-4032-36c0-afcf-9ea1a3043bd4 | -4.22642 | -48.61968 | 2025-10-25 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 79cb837b-eac9-3a32-9f35-47be583acefb | -3.13375 | -49.52087 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aff2439e-6335-3373-95bc-0e379f1a3189 | -3.69249 | -49.9407 | 2025-10-25 04:17:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f55059c6-6833-3aa8-be34-aa43fcb545d3 | -5.93209 | -43.51879 | 2025-10-25 04:17:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ac368fe8-a3ab-362b-921c-319ea859a981 | -5.58886 | -41.32342 | 2025-10-25 04:17:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 16bb3fb3-8cd8-3415-9788-c5170bf1ebeb | -4.83287 | -48.55074 | 2025-10-25 04:17:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2913c9bf-d7fe-3bb1-b9d0-ef7bac187c51 | -6.2013 | -41.52603 | 2025-10-25 04:17:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ce58b34a-5923-3ef3-b82c-878add1d79a6 | -2.22494 | -48.37214 | 2025-10-25 04:17:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7c8eed9-31c7-3b4d-ab2d-8c12d2841959 | -4.99945 | -47.7632 | 2025-10-25 04:17:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 90eabf12-f841-3194-908e-7d6ac7ff49d9 | -2.73643 | -48.68705 | 2025-10-25 04:17:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c8dc2d1-a88d-3dba-8b72-87fe5c8dbc08 | -4.2534 | -44.58011 | 2025-10-25 04:17:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f4b8b01e-3027-347d-acfe-32a77a8b7988 | -1.92079 | -52.14434 | 2025-10-25 04:17:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 35264750-9e9f-382d-a0a2-1b7b27269cff | -4.55141 | -46.60283 | 2025-10-25 04:17:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8725ca46-ca31-3dfa-8263-82259495ba12 | -2.72679 | -49.16398 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| acdfb597-f38e-3844-84f6-394b04b3c1c7 | -3.56029 | -39.08948 | 2025-10-25 04:17:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2af46005-58c6-3625-b19a-f9db9ab63ab9 | -5.54721 | -41.37983 | 2025-10-25 04:17:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d5cf1bb0-3758-361d-a3b6-5fe520f8c5b6 | -5.37606 | -40.70886 | 2025-10-25 04:17:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 133d7d72-2b02-397c-8b5f-0b9982968c8a | -2.86176 | -50.74026 | 2025-10-25 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 90f0a5ed-fe8b-345b-938d-dcf2e1313077 | -2.72737 | -49.16028 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bd8b0ee9-2b01-3c3a-8a83-e5333c1a55d8 | -4.86808 | -48.65172 | 2025-10-25 04:17:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88d327c4-aacc-38e0-b39c-74182336aff8 | -4.9007 | -48.97082 | 2025-10-25 04:17:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 331712d9-44c5-33ca-b7ff-d47698246310 | -5.68286 | -42.76913 | 2025-10-25 04:17:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c9e6a4d2-d697-3dbd-8291-5550fefff0ef | -3.10922 | -51.21021 | 2025-10-25 04:17:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50c6096a-01fb-3296-b43e-c7415d7acb34 | -5.57264 | -46.35233 | 2025-10-25 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f39ecd3-a5bd-31f9-8160-83bdbee9a79c | -4.55332 | -46.68625 | 2025-10-25 04:17:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 389f9b06-7377-348e-babb-cdd071e9f3ba | -4.24954 | -44.58305 | 2025-10-25 04:17:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75f93b66-55d0-35b4-951f-7bc328363b1b | -5.55281 | -41.34323 | 2025-10-25 04:17:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 35491bcf-bc9e-3e3b-9d59-bf08cf8fd29e | -3.11963 | -49.10042 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| af0c3525-8d27-3b56-af32-58428de84d05 | -2.26729 | -51.93073 | 2025-10-25 04:17:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3500c609-7d4a-3de1-98b5-11cfa1fc0b56 | -6.11348 | -41.74395 | 2025-10-25 04:17:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e3bf9c6a-4978-3877-8485-013289332de2 | -5.61107 | -43.94328 | 2025-10-25 04:17:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14464e5b-94cc-3a35-ac88-3de54b8bcd46 | -5.59973 | -47.09274 | 2025-10-25 04:17:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bdfcfe4f-ba41-3052-8ff4-9fe2fa9219dd | -4.85772 | -46.73263 | 2025-10-25 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d101c5b-6ac8-396c-b789-e3c496a6243a | -4.86683 | -49.17863 | 2025-10-25 04:17:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9c914df-0311-33e1-9318-21bcc6ad9dad | -5.44336 | -40.88517 | 2025-10-25 04:17:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 10f2fec8-8fe1-3f5d-854e-76a7f0e6e739 | -5.84812 | -40.82836 | 2025-10-25 04:17:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6bca2379-dd65-319f-90ab-65c8e47a3959 | -5.3791 | -40.71382 | 2025-10-25 04:17:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3ef52b89-d16f-305c-b152-8235286a57aa | -4.89361 | -43.23172 | 2025-10-25 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b72c344a-4cf6-397c-8ef6-c2dd293e1a4d | -3.394 | -51.5386 | 2025-10-25 04:17:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7bfa6b5a-19df-332f-b78e-fc8661071705 | -3.1628 | -48.60856 | 2025-10-25 04:17:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9de978e9-9ffe-3856-ab91-bb4291dbc09e | -4.55207 | -46.60604 | 2025-10-25 04:17:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c34d7ea-7aa3-39d0-9cb7-4770631addfc | -3.43159 | -50.25788 | 2025-10-25 04:17:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8b225a0-c8af-307c-8128-24478fd64de3 | -6.13125 | -41.72218 | 2025-10-25 04:17:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2b671576-1df5-34ce-ba94-f0d57d898e52 | -4.27303 | -44.39221 | 2025-10-25 04:17:00 | NOAA-20 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a3714f8-e4d0-38ee-98cc-6bf17f93406c | -3.51146 | -51.10077 | 2025-10-25 04:17:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 746e8ef4-a2ed-3d0e-89ce-010e2c81de96 | -4.25285 | -44.58357 | 2025-10-25 04:17:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b00bc278-53f0-36a1-9746-6a2130bc3acf | -3.18755 | -49.04105 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94f7c977-612f-3fa0-89fc-789558046974 | -5.14508 | -43.73132 | 2025-10-25 04:17:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4b7eb1f2-fa92-3a5c-ba12-8d531f3f3d1c | -4.15562 | -46.79134 | 2025-10-25 04:17:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e07e8bd0-50a9-3b3a-a427-30caec4542ad | -5.14123 | -43.73428 | 2025-10-25 04:17:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9a35a523-81c6-306a-b725-14f0c88d9e7d | -4.95943 | -47.59355 | 2025-10-25 04:17:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c66a804b-3bcc-3892-8dac-99a35e22c0dc | -4.4055 | -40.48548 | 2025-10-25 04:17:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7f892308-5d4b-35a1-9f89-4426d61554dd | -6.28676 | -42.35582 | 2025-10-25 04:17:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| dc1ffe4f-d6e4-316b-aca9-577bb4b3c5eb | -6.31906 | -41.86629 | 2025-10-25 04:17:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 073fa560-736c-3c64-94d5-05b01efde1af | -2.80608 | -49.13377 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 925208f1-b357-3539-8531-cb6b44f6f3f7 | -4.60702 | -47.0235 | 2025-10-25 04:17:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd9f867f-fc27-35e3-a82d-c4a62b00dd38 | -2.80609 | -50.27758 | 2025-10-25 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 37377743-fa48-3d41-bf00-fe4b65ccbd6b | -3.15827 | -49.17472 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 33aae3c5-e854-307e-8ac1-f311c4669050 | -5.6888 | -45.62176 | 2025-10-25 04:17:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ba961537-690c-3d16-ac41-2774135a07f2 | -2.81254 | -49.14632 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d88ab96a-3bbb-3622-aeb2-83b9099453cc | -3.08552 | -49.46952 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d184fe7d-5c77-3fd2-9556-cb42844282be | -5.6077 | -45.18998 | 2025-10-25 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b21e5c3d-3200-3084-b55f-e3a19aae983e | -2.85255 | -50.73877 | 2025-10-25 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9d02535-3ac6-32a5-8a28-c0437dc75f0f | -6.09286 | -46.23707 | 2025-10-25 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 470a5da9-94d6-3aae-acf2-b4d0c7ff668b | -4.55489 | -46.60343 | 2025-10-25 04:17:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78c25f0c-da22-3d39-ab99-bed726cd05a5 | -4.72798 | -49.08866 | 2025-10-25 04:17:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9bfff702-d77b-397b-8f57-54c7489c14ee | -3.29346 | -50.194 | 2025-10-25 04:17:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e24422b3-ba19-3151-b522-57f6f745ffd8 | -4.82957 | -50.93246 | 2025-10-25 04:17:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b799a7e9-1975-3e11-9dc5-506a1761d037 | -6.10996 | -41.74329 | 2025-10-25 04:17:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a8adab47-a5ad-3126-ac9d-26e87f21ebef | -2.79917 | -54.38763 | 2025-10-25 04:17:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54e26d8a-35ed-350d-953f-4a0b8bcae62e | -3.11903 | -49.1041 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 13f503a7-1191-3e8c-9980-af2a4dfecda7 | -3.15694 | -49.17452 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 746a4b90-dace-3c7b-a167-748828300da9 | -4.90734 | -48.56505 | 2025-10-25 04:17:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7361e30-5ec5-30d0-b1ba-d8414ba1575c | -3.02168 | -45.39738 | 2025-10-25 04:17:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22c3f298-8f96-3d4d-ac10-09881abef1d2 | -5.40352 | -44.41925 | 2025-10-25 04:17:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02f2ad8e-9c14-33a7-b7ee-b2b7e0dc085e | -4.228 | -48.60976 | 2025-10-25 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 140f3784-0bea-33ae-b4e0-417d92141895 | -4.65867 | -46.03789 | 2025-10-25 04:17:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a2d197a-8d4d-3922-9b58-8520fd054f5d | -4.70163 | -46.44399 | 2025-10-25 04:17:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b5a6803e-5ca3-3f3b-bd48-cd665fd47438 | -5.28612 | -38.29221 | 2025-10-25 04:17:00 | NOAA-20 | SÃO JOÃO DO JAGUARIBE | CEARÁ | Brasil | 2312502 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 48d4ee56-f93b-3880-896c-c19d3277761f | -5.67665 | -42.76443 | 2025-10-25 04:17:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4e30988e-2f72-3aaa-ab0f-42ce523f20aa | -6.30096 | -40.87576 | 2025-10-25 04:17:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9d2ef409-5130-3ab9-afaf-d707f49e7b35 | -3.86569 | -51.89139 | 2025-10-25 04:17:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ebbe901c-5d13-3979-8ca6-6c5832573b9f | -4.8431 | -50.93479 | 2025-10-25 04:17:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 123d5dbc-d37f-375d-a5f3-882a8d1fb029 | -4.61126 | -47.0199 | 2025-10-25 04:17:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0249894d-7f6d-3a98-8bcd-6f3114806d64 | -2.30112 | -48.5696 | 2025-10-25 04:17:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 213e960d-4131-36f8-a3ed-798019f7fd40 | -3.98421 | -48.00011 | 2025-10-25 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe27777f-ba91-3c15-a3cb-b20fd5d18e41 | -3.13587 | -50.61993 | 2025-10-25 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f9bb062-c035-3c32-8602-d9b1729740bf | -3.436 | -50.25862 | 2025-10-25 04:17:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 330c7ebf-4dc6-3d64-90a1-bbbf74bebb3e | -3.11953 | -51.20661 | 2025-10-25 04:17:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ead42188-0ece-3dd1-916b-afe38eeae46c | -6.36537 | -44.26754 | 2025-10-25 04:17:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5079d1e-93b0-3112-ab86-b3e7f0f6acd9 | -5.02088 | -47.15225 | 2025-10-25 04:17:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 637a303d-c3dc-3316-bc22-a17503de1fce | -6.83768 | -41.54837 | 2025-10-25 04:17:00 | NOAA-20 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README29.md)
