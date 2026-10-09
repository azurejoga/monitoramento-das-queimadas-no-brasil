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

## Dados Diários - Página 277

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1274c5a5-c326-38c6-97cf-7b513169702c | -6.95179 | -43.94571 | 2026-10-09 16:01:00 | NPP-375 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ea5ce230-ca73-3147-a83a-8c52723f5684 | -8.9153 | -45.17209 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 6fc2a0d8-6c2a-3a1d-8232-6e8ab99027b3 | -6.11722 | -44.14765 | 2026-10-09 16:01:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 49d3ae16-cb2c-39af-bbdd-524bdd778ab6 | -5.81527 | -42.62551 | 2026-10-09 16:01:00 | NPP-375 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| e1e29688-69e3-3a2f-a7b9-13f130a0ec88 | -5.74071 | -41.77615 | 2026-10-09 16:01:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 9ee09a75-f73d-3a82-8041-bbe1f7b03484 | -9.83652 | -44.78288 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9689b58c-c520-3fac-8081-27e31b499794 | -5.50762 | -42.83086 | 2026-10-09 16:01:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 95d014af-17e3-3996-95c4-a15503a6aa65 | -11.09273 | -43.99397 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e6a4d350-695f-3922-9fe3-8270cc83a80e | -7.41875 | -44.76451 | 2026-10-09 16:01:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 3f470002-eda2-327b-acae-7ed0126371dd | -7.37385 | -44.0389 | 2026-10-09 16:01:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| e8ec9321-cfef-3edb-b784-64b707cd5e7b | -7.48136 | -42.83891 | 2026-10-09 16:01:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 03a85755-2b7d-30be-a862-ddcae99f7bb4 | -10.9966 | -45.40551 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 083ea36c-836e-325b-9220-edf0f8755ede | -6.84604 | -41.74521 | 2026-10-09 16:01:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 9a509ead-7119-388f-b3ae-927983a08cf1 | -10.64279 | -45.2227 | 2026-10-09 16:01:00 | NPP-375 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 780ebd9a-8397-3f17-abb8-8658974ac71b | -10.46891 | -47.19167 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 038b1348-9128-39bf-b251-8e693527dd83 | -7.07522 | -41.60333 | 2026-10-09 16:01:00 | NPP-375 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| b65137cd-5142-370a-8018-67fadfcc1089 | -9.84269 | -44.79017 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 87329d28-4ce1-3ab4-a557-faa6a16c657c | -8.52286 | -36.52408 | 2026-10-09 16:01:00 | NPP-375 | SÃO BENTO DO UNA | PERNAMBUCO | Brasil | 2613008 | 26 | 33 | nan | nan | nan | Caatinga | 5.3 |
| c3923e0e-3e77-3d01-8edd-32803d594cc0 | -10.33441 | -39.4913 | 2026-10-09 16:01:00 | NPP-375 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 12f9dac4-1a0e-3b4c-884a-785d4aced35a | -7.01618 | -47.69118 | 2026-10-09 16:01:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| a855d6d0-4a3c-386f-9f13-7c19e7cdb970 | -5.36514 | -43.20069 | 2026-10-09 16:01:00 | NPP-375 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b8ac6cfc-9a19-3156-92c7-e8cef954df8b | -9.91852 | -44.78759 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 3c8cf992-33e9-355b-aa9f-b55979e76daf | -8.90925 | -45.17614 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 63e77030-460b-370e-a556-9be2253c89b8 | -10.48131 | -47.23758 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 4e5072b0-1b58-3f02-88a9-490b21cf5e5a | -7.37794 | -44.02733 | 2026-10-09 16:01:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7c2f916f-a90e-3480-bfe8-7beed9e497b6 | -9.86466 | -44.86253 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 64.5 |
| e72797ae-73d6-33d3-80e3-5574bb336f14 | -5.71119 | -41.66775 | 2026-10-09 16:01:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 4094ae72-da13-3bfd-a7be-69b163d58320 | -7.90548 | -44.17013 | 2026-10-09 16:01:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 37da0cb7-0c7f-3507-83c0-24dd3147a5a5 | -7.00137 | -44.13601 | 2026-10-09 16:01:00 | NPP-375 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 23a72dc2-e7f0-3ac6-aab1-3bc74494fd04 | -6.01599 | -40.9758 | 2026-10-09 16:01:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 36239cbb-08a5-37d6-9077-3de052b204cf | -7.293 | -44.02702 | 2026-10-09 16:01:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 4d07683e-27ac-391b-b6ac-a2d5b72bc57a | -6.82993 | -39.56565 | 2026-10-09 16:01:00 | NPP-375 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 4ef83d75-b1d1-31cc-ba69-560cc1243806 | -6.48157 | -42.69783 | 2026-10-09 16:01:00 | NPP-375 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 26.7 |
| 4f3ca502-fd2b-30ac-8520-26c9f76a975b | -7.59192 | -47.03727 | 2026-10-09 16:01:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| eafe880d-fef4-3f4d-bc6a-8246cda5b2b3 | -7.24344 | -43.74491 | 2026-10-09 16:01:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b47ac3ce-e3b7-357f-bcab-0c98934ad712 | -5.75553 | -42.09114 | 2026-10-09 16:01:00 | NPP-375 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| ed40ba2a-3f64-342f-9172-5e2fe89f78e5 | -7.68789 | -45.44482 | 2026-10-09 16:01:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 72.1 |
| cea4714d-8ff2-3af7-a95a-0be7f87c496d | -7.81963 | -38.85106 | 2026-10-09 16:01:00 | NPP-375 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 48c86d8f-1bfe-3b21-a0af-32d7f043588d | -7.47865 | -42.8577 | 2026-10-09 16:01:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 19.8 |
| 9da250dc-5fa0-3c6b-ba59-de63ff899a81 | -7.27763 | -37.32575 | 2026-10-09 16:01:00 | NPP-375 | MATURÉIA | PARAÍBA | Brasil | 2509396 | 25 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 2be419fb-aa07-343b-b6b4-7fbe919af0f7 | -7.82934 | -44.57061 | 2026-10-09 16:01:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 565107f5-df7f-3790-b082-095b0e9da5c4 | -5.51288 | -43.04622 | 2026-10-09 16:01:00 | NPP-375 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 72f9c0a7-a8fc-31a5-94ee-214ba9e8387b | -8.97555 | -45.15669 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 4c9304f0-65ee-39b3-8d0c-1540fcf2d434 | -6.22413 | -42.67878 | 2026-10-09 16:01:00 | NPP-375 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| cefc2d4e-5d54-31da-9a2a-442bf7d8dc5e | -10.88728 | -45.53372 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0d4fe1c1-4105-324a-badb-92f18ffdd839 | -7.07409 | -41.60638 | 2026-10-09 16:01:00 | NPP-375 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 28dcfa08-e83d-39fd-80e7-3e644f1729af | -9.92864 | -43.57475 | 2026-10-09 16:01:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 3ebbf861-8839-3721-a022-ef1e329f1810 | -7.80082 | -44.57988 | 2026-10-09 16:01:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3ffa05f6-e71c-3a8b-8ee1-444afbb5dd42 | -6.00329 | -40.95073 | 2026-10-09 16:01:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 946ed0f4-044a-30c7-aaa3-7d4843a007db | -11.23455 | -45.30954 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 03a60200-dfc4-3871-a391-a14b3044770c | -9.93168 | -44.79485 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 36b5daa9-97c9-341d-ae2b-1918dd82542c | -11.26036 | -45.17536 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| dad5b713-0a77-3008-a0fc-8e1c21da6aaf | -10.96679 | -45.38463 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1b788456-cd73-345e-a5e0-ad663fe53f97 | -11.22819 | -45.3103 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 7e7c4142-7ab7-3017-bf62-aa9ed08595f8 | -11.04434 | -44.07987 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2ed2394a-4ca1-39c0-a6cf-21ef633ff0d0 | -6.04509 | -37.57647 | 2026-10-09 16:01:00 | NPP-375 | PATU | RIO GRANDE DO NORTE | Brasil | 2409308 | 24 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 5d9b7d63-7ac1-3dbf-9048-bf7962c73244 | -10.61203 | -43.27583 | 2026-10-09 16:01:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 11.9 |
| d5956f3f-ba80-360d-bc25-e395d8029c13 | -7.60109 | -42.36863 | 2026-10-09 16:01:00 | NPP-375 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 68c3f5e3-a2a5-3382-b11b-ed39719c5be3 | -10.88594 | -45.52212 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 8e3f224d-a45d-31fb-8606-5992b93e2ef3 | -7.02146 | -45.30892 | 2026-10-09 16:01:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 30f8f7f6-ff87-3349-bb5b-b0363fb65f8a | -11.21004 | -45.26558 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 8ee05833-2d4d-37d4-8931-f80603d1b102 | -11.09907 | -43.99751 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3abba98d-84fa-3936-99be-165c93a8adce | -11.04182 | -44.05883 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 12f24325-9477-3a79-a729-8bae0621d1e2 | -11.21229 | -44.86081 | 2026-10-09 16:01:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e975f64d-b3a1-380b-bf60-3c4a55257045 | -10.7443 | -46.61618 | 2026-10-09 16:01:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 9dec7f02-1184-3c6b-89a7-cf989c023c42 | -7.31646 | -43.99075 | 2026-10-09 16:01:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c260bf91-3db0-3327-9c19-eb42aa762fae | -7.08264 | -43.08445 | 2026-10-09 16:01:00 | NPP-375 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| bc869922-6f4f-305f-b428-037c2810d718 | -5.52311 | -43.99041 | 2026-10-09 16:01:00 | NPP-375 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 89f261c8-6f24-3433-9ed0-29e0f94fd969 | -10.9758 | -45.3934 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b21eeda9-b499-3b1b-aa82-f715e2541b94 | -5.66332 | -42.9925 | 2026-10-09 16:01:00 | NPP-375 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 3ca8608c-ba7d-3b11-8853-1a1b4b531845 | -5.23965 | -40.58917 | 2026-10-09 16:01:00 | NPP-375 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 8.7 |
| c6b1ce4e-7b2c-3242-a2ab-5032fcd301b6 | -10.74356 | -46.60985 | 2026-10-09 16:01:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| e9c5aff3-d8b4-3e34-9d08-876bca4eba52 | -10.43259 | -47.31457 | 2026-10-09 16:01:00 | NPP-375 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 11eca19f-bcf7-3dd4-85ef-78e5b256cdb1 | -7.47564 | -42.79647 | 2026-10-09 16:01:00 | NPP-375 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 445019b1-1cc8-3ec8-99c5-74443fbc69f2 | -7.79338 | -44.56862 | 2026-10-09 16:01:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 77c82114-240f-3fea-be58-3786e8177988 | -8.91032 | -45.18223 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 048d42d1-b72c-3d12-941c-bac63ff4b3ca | -6.14034 | -44.15229 | 2026-10-09 16:01:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 96e60085-c5f8-3327-9eb6-b4413ada3914 | -9.99253 | -45.98065 | 2026-10-09 16:01:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| feae09a6-8071-3ac3-8cfb-2eaf08d60373 | -10.47498 | -47.50063 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 5b984f08-5e70-31d5-8825-51696bb13e6b | -7.48961 | -42.8225 | 2026-10-09 16:01:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 29714e3a-1ca9-354c-8946-23780b94dfa7 | -11.12024 | -44.01971 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| cc9c0599-3006-31f1-ada2-25b53d7bda6a | -11.20669 | -44.87307 | 2026-10-09 16:01:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0a6bd811-d0ce-3fe9-ac1d-ed36f4b9c9c0 | -7.49044 | -42.82859 | 2026-10-09 16:01:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| fa35ee21-db3d-3250-b3de-8b773468dab1 | -6.13245 | -42.89239 | 2026-10-09 16:01:00 | NPP-375 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 869db818-cbb8-3ade-95fe-9b0a96b21221 | -11.21124 | -44.85807 | 2026-10-09 16:01:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 36808dab-ae08-3822-af91-69cad2216f08 | -11.07041 | -44.09821 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 30.0 |
| f2fa058d-c8ce-364a-84a4-819ddc1ad9e4 | -7.22625 | -44.15735 | 2026-10-09 16:01:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| da36a99f-d290-32c4-8162-6931f762b688 | -8.25801 | -44.20452 | 2026-10-09 16:01:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9143ab16-c038-38e8-bf17-fa2b1cbe428a | -9.72276 | -45.69959 | 2026-10-09 16:01:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 97b7df54-349f-3f6c-901a-24921a58fbaa | -5.47513 | -41.22672 | 2026-10-09 16:01:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 7cee334e-856e-3e7e-96bd-ae3553bdefdc | -7.12739 | -41.80843 | 2026-10-09 16:01:00 | NPP-375 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 23.5 |
| 44db689d-be8e-365b-b3ab-b523b976e77c | -6.83837 | -35.14022 | 2026-10-09 16:01:00 | NPP-375 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 77079a79-f07f-3c93-9c5b-a8dbba482e40 | -10.49166 | -47.20312 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 8973846c-8523-38e7-818e-10056c8226e6 | -6.37582 | -38.26104 | 2026-10-09 16:01:00 | NPP-375 | JOSÉ DA PENHA | RIO GRANDE DO NORTE | Brasil | 2406007 | 24 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 9e9d802f-0bce-3585-b549-5c7fb9553718 | -10.49482 | -47.23053 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 158.5 |
| 47f38591-e0de-3a1c-a2df-de3399eb2ab4 | -11.05687 | -44.03577 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 4a8dc277-9d44-3d6c-97c2-d56dbb2e830b | -11.08217 | -44.0968 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 97fc6949-d9c7-3922-8e4a-2bdf921a9972 | -7.90599 | -44.17398 | 2026-10-09 16:01:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d1bd24ca-cf4c-3a7b-839a-e76680483052 | -5.85688 | -42.67086 | 2026-10-09 16:01:00 | NPP-375 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| aaf96405-afa3-3d16-b737-23fbc908669d | -9.17995 | -43.39822 | 2026-10-09 16:01:00 | NPP-375 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 19.8 |


[Clique aqui para ver as próximas entradas](README278.md)
