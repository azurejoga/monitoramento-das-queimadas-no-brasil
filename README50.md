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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a41b4c3-e669-347d-9174-c93c6733e9b2 | -10.9293 | -47.1553 | 2025-10-11 12:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 44e43d0a-0bf1-375f-a8ab-200a6843a938 | -13.8501 | -45.7992 | 2025-10-11 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 232.7 |
| fa64dd5e-a32b-388d-bc71-3113b3a698ad | -11.6282 | -47.5115 | 2025-10-11 12:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 5e921203-81bf-3152-9e7a-f3df1e51bacb | -13.8004 | -45.3917 | 2025-10-11 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| da53f73e-8519-3398-b7c7-216a0a07b6b1 | -15.0021 | -45.5725 | 2025-10-11 12:10:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 295.1 |
| d4ee065d-4d97-394d-8de2-cad4adcf3982 | -13.8491 | -45.8454 | 2025-10-11 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 347.1 |
| 0508e28a-8fa0-3bc4-bde3-14700b49384f | -13.8496 | -45.8223 | 2025-10-11 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 594.5 |
| 2f3febaf-feda-3215-80e3-9f5f9e15f7cc | -15.0021 | -45.5725 | 2025-10-11 12:20:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 194.3 |
| 90cdb590-e31d-3c19-a5a7-57adde4aae66 | -10.9293 | -47.1553 | 2025-10-11 12:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 73f2ea64-fc57-3794-a422-f7ce7ecbee6e | -13.8501 | -45.7992 | 2025-10-11 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 295.5 |
| 6acd22f0-f343-3e37-80ca-cd5955508a60 | -13.322 | -47.1144 | 2025-10-11 12:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 106.6 |
| c934a468-1726-33cc-bb45-6fda65a295aa | -10.2088 | -44.591 | 2025-10-11 12:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 40f504a2-b7bc-3c34-b6a0-8d4123eed80d | -10.5274 | -47.3601 | 2025-10-11 12:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 83cbb6bf-fd77-3b50-8823-528989a414a8 | -10.5084 | -47.3624 | 2025-10-11 12:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 57d8920c-8b61-39a4-bf30-cb2eb88e0f3b | -11.6282 | -47.5115 | 2025-10-11 12:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| d409d1fb-4c1f-3e2e-86d2-955a06264a5c | -13.8686 | -45.8421 | 2025-10-11 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 732.6 |
| b1d81479-7ecb-327e-85f1-c8391f2e5792 | -13.3026 | -47.1174 | 2025-10-11 12:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 114.4 |
| bab02c56-5e42-3792-a521-f0dfb266c4a5 | -14.9825 | -45.5761 | 2025-10-11 12:30:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 2c2dbc18-6e92-39d1-be5c-03cfc7a79ff7 | -13.8491 | -45.8454 | 2025-10-11 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 396.5 |
| fa6b4289-a326-3137-80aa-11e314470b28 | -13.8686 | -45.8421 | 2025-10-11 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 549.5 |
| 9b000a7f-876e-3866-bdfa-f129731d2c76 | -9.4137 | -45.7861 | 2025-10-11 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 32a62f9f-d41d-38cd-bfcf-90fdd023ce73 | -10.9231 | -47.5564 | 2025-10-11 12:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 4fd2b2ec-e362-3ab3-8af6-c3b940d061ee | -13.8501 | -45.7992 | 2025-10-11 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 648.6 |
| dd27981c-233b-3723-a00a-66469ca8ec87 | -12.5097 | -47.3913 | 2025-10-11 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| ff746889-8fdc-33bb-a772-64bf92a7730a | -10.9041 | -47.5588 | 2025-10-11 12:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 160.9 |
| f92f09b7-8f3c-3db0-9445-81c53470fe3a | -9.3947 | -45.7882 | 2025-10-11 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 89dc3d90-c7a8-39a7-a03d-6468ee191307 | -13.8496 | -45.8223 | 2025-10-11 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1095.2 |
| 1e021076-36cb-30e2-9f06-bbde99a46f7e | -10.5087 | -47.3401 | 2025-10-11 12:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 104f847f-a0fb-365b-a43e-7e8277097879 | -15.0016 | -45.5958 | 2025-10-11 12:30:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 890d8aae-f83e-3851-98ed-3ce5cdbceacf | -11.6282 | -47.5115 | 2025-10-11 12:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 5e1d2e65-ff54-36ea-8616-708465abcb4c | -10.5274 | -47.3601 | 2025-10-11 12:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 8e0a2256-3d32-359a-86b4-2444455c989e | -10.5084 | -47.3624 | 2025-10-11 12:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| de36d037-46c7-313a-83d4-78bcda4de2c9 | -12.5093 | -47.4138 | 2025-10-11 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 30e7255f-3665-3260-b01e-b71aacc57904 | -13.322 | -47.1144 | 2025-10-11 12:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 6b2b4db2-bf3f-314e-9fe2-aa9111e44536 | -11.892 | -45.4868 | 2025-10-11 12:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 213.9 |
| e508d991-4b8a-3968-91d2-e1dc44e56160 | -15.0021 | -45.5725 | 2025-10-11 12:30:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 446.8 |
| ab02da64-0fbf-3e49-abbb-bf062f72578e | -10.5084 | -47.3624 | 2025-10-11 12:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 399e48c7-4ab7-34c2-a86b-1a3ffe1163a9 | -10.8341 | -47.1671 | 2025-10-11 12:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 01c56a6b-c673-3096-b0c0-14bf3af36c8d | -13.8491 | -45.8454 | 2025-10-11 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 332.9 |
| 429d4b3d-7fcc-3495-b970-617f5169c2e6 | -11.6282 | -47.5115 | 2025-10-11 12:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 146.0 |
| c70b1d82-b791-351f-839c-3521def6d31d | -10.5277 | -47.3379 | 2025-10-11 12:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 01ca72c1-251c-3f6d-ba9c-02e2ce0c0e98 | -10.0747 | -45.9121 | 2025-10-11 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 5e856e61-bda6-3a4c-aa03-4ae686405c9e | -13.2833 | -47.1203 | 2025-10-11 12:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 8f2119dd-d281-3794-aa09-e476b3be35d3 | -12.5093 | -47.4138 | 2025-10-11 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 22737d2f-02a5-305b-950d-7c1acdeab1a9 | -13.8686 | -45.8421 | 2025-10-11 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 754.6 |
| 680e14d1-b03d-3683-9da3-f127569edc8e | -9.1028 | -45.0248 | 2025-10-11 12:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 773551d7-db2c-3a0a-8648-29194ace2d37 | -10.9293 | -47.1553 | 2025-10-11 12:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 75c09afe-594b-3ef7-bdd3-73b241937d15 | -9.1024 | -45.0477 | 2025-10-11 12:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 73.9 |
| c2073f2f-e9f8-3b46-bc35-5a58e26001ea | -10.5654 | -47.3556 | 2025-10-11 12:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| a7c6af85-23a1-3851-8d59-3eeb60bac48e | -15.0016 | -45.5958 | 2025-10-11 12:40:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 165.1 |
| 718f5fa2-1788-3bba-a4d1-36051fcf17da | -13.8501 | -45.7992 | 2025-10-11 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 324.9 |
| 374bab46-117e-3208-b365-522d6170b835 | -13.3026 | -47.1174 | 2025-10-11 12:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 111.7 |
| af2c28aa-82d9-3e14-adb2-696a600edb1e | -11.6469 | -47.5313 | 2025-10-11 12:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 6837adc1-146a-32e8-97c7-e35849392196 | -11.7809 | -46.3687 | 2025-10-11 12:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| f50644d3-ff67-3814-b72b-233b9f65b1ba | -11.7622 | -46.3487 | 2025-10-11 12:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 01240a64-8358-37fc-a2de-fcbe994e2e55 | -13.322 | -47.1144 | 2025-10-11 12:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 6c0fd408-268d-3074-878f-5b583e7238fa | -9.3947 | -45.7882 | 2025-10-11 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 83.5 |
| d9635230-0a81-3aeb-9a2d-37b07f06f234 | -15.0021 | -45.5725 | 2025-10-11 12:40:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 288.0 |
| 769602eb-0e5e-3e8a-ab88-24ba2c8c0555 | -10.5274 | -47.3601 | 2025-10-11 12:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 7db537d1-92d4-38f1-98f6-1338f420aaf7 | -13.8307 | -45.8024 | 2025-10-11 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| d331b852-2d2c-3f96-89bb-6687070bd5bb | -11.6278 | -47.5338 | 2025-10-11 12:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 03cc5ff1-f69d-306b-914f-81bca3374521 | -9.4137 | -45.7861 | 2025-10-11 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 173.8 |
| ca68b2b0-967a-32da-8487-38a51f6db108 | -13.8496 | -45.8223 | 2025-10-11 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 824.3 |
| 2d445511-ba57-34a3-b598-027005dd4a9a | -11.892 | -45.4868 | 2025-10-11 12:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 87cbd43c-07fa-3c5c-a9ec-8c3df01f14eb | -10.5084 | -47.3624 | 2025-10-11 12:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| c2c9d9fd-2a1d-3fc3-81ce-857f860427de | -11.6278 | -47.5338 | 2025-10-11 12:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| e509cee2-14b3-3398-a288-0622e8337276 | -11.6282 | -47.5115 | 2025-10-11 12:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 140.0 |
| 5562505a-be8a-30b0-9817-23b72a5be5f9 | -11.7622 | -46.3487 | 2025-10-11 12:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 0ad513d1-2fde-3988-a364-39609cf8d3ee | -9.1028 | -45.0248 | 2025-10-11 12:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 63ceeca1-df97-3a33-a0e2-b229059ecf45 | -13.8491 | -45.8454 | 2025-10-11 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 100.0 |
| e995bdfd-6647-3c82-8e6f-dcd793d7b487 | -10.5277 | -47.3379 | 2025-10-11 12:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 45e3734b-2e90-31d4-b8f1-60bce482cda9 | -13.8496 | -45.8223 | 2025-10-11 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 242.3 |
| 1e4b4b89-fd89-33ec-bc52-94f38d41fe7d | -9.1024 | -45.0477 | 2025-10-11 12:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 78.0 |
| aa646b60-5ba4-3244-9d62-29e64b850b11 | -15.0021 | -45.5725 | 2025-10-11 12:50:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 320.6 |
| 6bed0216-955f-3d3b-b97f-e6b861237cce | -13.322 | -47.1144 | 2025-10-11 12:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 3e84a152-53c2-3dae-8c9d-c42f64350f95 | -10.9293 | -47.1553 | 2025-10-11 12:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 7b83da66-5a94-352f-82a1-e07ef7af6b83 | -11.7618 | -46.3714 | 2025-10-11 12:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| c8aa2eb4-65ab-35c9-8b89-9b13a684cd56 | -13.3026 | -47.1174 | 2025-10-11 12:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 452f83f5-c42b-3673-8444-fa89d225a6c6 | -10.0747 | -45.9121 | 2025-10-11 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 106.3 |
| db146333-b342-3fe6-96d0-6a2a306a6fdb | -13.7999 | -45.415 | 2025-10-11 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 6a5a0adf-dff2-3e84-a872-eb72937dea71 | -10.9041 | -47.5588 | 2025-10-11 12:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 99973a87-18e6-3a54-81b3-32fadef0b8cd | -13.8004 | -45.3917 | 2025-10-11 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 106.7 |
| aef803bf-57e0-3e21-8dc1-72fc82217681 | -10.5654 | -47.3556 | 2025-10-11 12:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 63827ef2-3ab4-3011-9e98-27c2cf278177 | -11.7809 | -46.3687 | 2025-10-11 12:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 8e2fc302-df3d-3d3b-a1d6-a0ea35715480 | -10.5274 | -47.3601 | 2025-10-11 12:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| a3bd4c6e-6f18-3ff9-8532-9a71f982b932 | -10.2543 | -46.5892 | 2025-10-11 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 160.1 |
| a7bd92d6-bd9f-302c-afa4-2207506cab6a | -10.8341 | -47.1671 | 2025-10-11 13:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 12cdc4e5-7cac-3ec3-91c5-685d83d72b6a | -10.0747 | -45.9121 | 2025-10-11 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 185.3 |
| c5bfda7c-98fc-31d4-b86d-e6995ea34061 | -12.5097 | -47.3913 | 2025-10-11 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| eed39831-1ce3-3979-83f4-dd58bbf9ba23 | -10.6703 | -46.6954 | 2025-10-11 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| eda62fd5-9c60-32d8-ae4c-8a33f1dd6d75 | -15.0021 | -45.5725 | 2025-10-11 13:00:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 240.5 |
| 961e35c2-4d7e-3045-8bee-95bc2ccd7f21 | -8.9008 | -46.0007 | 2025-10-11 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| de975aab-7e34-3dee-9ef7-fab689f754dc | -13.8004 | -45.3917 | 2025-10-11 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 177.8 |
| 13908c6c-b4e4-3631-aefa-f1a793dad142 | -15.0016 | -45.5958 | 2025-10-11 13:00:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 66c22314-99f7-3ec0-a81a-865704bd5ad1 | -12.5093 | -47.4138 | 2025-10-11 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 136.8 |
| 5aa51c45-89f3-327f-80a4-4997cae62bbf | -10.5274 | -47.3601 | 2025-10-11 13:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| a4dbafc6-cdb2-36d4-b21c-1d7167ead169 | -12.4705 | -47.4416 | 2025-10-11 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| c811bba6-eee6-3a16-ad05-ac74e760363d | -9.3951 | -45.7655 | 2025-10-11 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 4d4b2d6e-bf1b-3d04-9430-896eee64ba87 | -11.6278 | -47.5338 | 2025-10-11 13:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 6757e166-5f86-35ac-953d-fd48308def5d | -10.5464 | -47.3578 | 2025-10-11 13:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |


[Clique aqui para ver as próximas entradas](README51.md)
