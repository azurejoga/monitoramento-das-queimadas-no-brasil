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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 25739f54-e1cb-3688-bc46-b5ffc7ec6595 | -8.8903 | -46.8081 | 2025-10-07 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 31e28212-7ffb-3d36-a190-8db0663eeabf | -14.2949 | -45.8613 | 2025-10-07 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 61b47b86-f57b-357d-af17-334054956f51 | -10.8922 | -47.093 | 2025-10-07 12:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 1209a97a-59fc-356f-83db-9c355f341f2c | -16.2946 | -50.965 | 2025-10-07 12:30:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 93.1 |
| a574fb0e-3b37-3e6c-8358-4d418972a7e4 | -12.9619 | -46.808 | 2025-10-07 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 642dbd13-0d17-336a-9ad6-e094a2e5f1b7 | -18.0187 | -44.9725 | 2025-10-07 12:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 4751eca1-adb7-3dc3-aa1a-9a79f7badb1a | -10.428 | -50.3946 | 2025-10-07 12:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 30f3477a-9908-33bc-b622-10566a97afdf | -10.8919 | -47.1153 | 2025-10-07 12:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 224.0 |
| ecbf2851-5304-3f75-a93f-f5de74899db4 | -11.6859 | -46.3366 | 2025-10-07 12:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 578b6691-c55d-3b3b-ac42-5d1830bb7bb3 | -15.3737 | -47.3201 | 2025-10-07 12:30:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 89d63287-090e-352e-a335-078b85b53dc9 | -10.1569 | -45.493 | 2025-10-07 12:30:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 182.6 |
| eb29ad6d-41db-3105-8911-be22b9aba3f1 | -10.2693 | -44.3745 | 2025-10-07 12:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 61eda671-dc56-3a54-a616-4a9399fada2e | -10.9109 | -47.1129 | 2025-10-07 12:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 81192b44-72f6-3d59-9fd9-078c4313a8e8 | -14.5057 | -46.9242 | 2025-10-07 12:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 6365ac36-08a7-347b-8e1a-4a35d78d7427 | -14.2953 | -45.8382 | 2025-10-07 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 307.9 |
| f39c0554-32d3-350d-b627-0a7d67ee18fb | -13.3237 | -48.0547 | 2025-10-07 12:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 08ccb954-278a-305e-b446-d911062aeb82 | -12.9422 | -46.8335 | 2025-10-07 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 96d5435b-3d99-3ef9-a712-b2d30c7cfa75 | -12.9615 | -46.8306 | 2025-10-07 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 157.9 |
| 45ec67bc-0b5c-373d-ab15-4a2855d5863d | -10.2696 | -44.3513 | 2025-10-07 12:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 94.0 |
| df152d7d-569a-3d21-b498-ea979ce98cc2 | -10.1383 | -45.4725 | 2025-10-07 12:30:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 46e9d3d7-eedb-3b4c-90ee-4b63ad7478a8 | -13.3044 | -48.0575 | 2025-10-07 12:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 65c018bc-5ba5-34d5-8e6e-df959f73a0aa | -10.1573 | -45.4701 | 2025-10-07 12:30:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 829ae469-e49c-33ea-9b60-1bd04efd0d51 | -8.4821 | -46.3136 | 2025-10-07 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 8994461b-c745-3ffc-ab78-3dc9086d2f76 | -8.5007 | -46.3342 | 2025-10-07 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 6c46ee13-98c9-3b13-a2ff-e6fa9284b131 | -9.6098 | -46.6416 | 2025-10-07 12:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 06f73aa0-bc98-3fa1-b2ee-48a097fdd938 | -12.7637 | -50.4921 | 2025-10-07 12:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 195.6 |
| 846060f9-5760-36f9-b101-7882537c8c31 | -12.8913 | -54.7372 | 2025-10-07 12:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 224.5 |
| ee544489-097c-378f-84c8-abd898944918 | -14.7384 | -46.037 | 2025-10-07 12:30:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 9af11e62-9b3c-359a-9c67-33229f3eaf3e | -14.7389 | -46.0138 | 2025-10-07 12:30:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 4f0ba23d-f073-3c97-8b8f-0dee95619290 | 1.3816 | -50.62152 | 2025-10-07 12:34:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 57b5c2b6-9b8b-3e00-a617-2920916736bb | 1.19108 | -50.70504 | 2025-10-07 12:34:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 4eda539b-af44-3ff5-b7ea-6c81a83a84c0 | -1.4632 | -48.98925 | 2025-10-07 12:34:00 | TERRA_M-T | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4c73a81b-3672-3516-ae8d-9d79a498a248 | -1.4982 | -48.99042 | 2025-10-07 12:34:00 | TERRA_M-T | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 1c18a915-1ae6-3378-9bab-74a1fb01e365 | -4.05753 | -44.51485 | 2025-10-07 12:36:00 | TERRA_M-T | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 52.0 |
| c47ad9b1-542c-30fd-86c5-d8efc90a8199 | -8.1838 | -43.3366 | 2025-10-07 12:36:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 130.5 |
| 6eb0696c-473f-3c10-8bd4-73507f4b18e2 | -4.71055 | -43.35185 | 2025-10-07 12:36:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| b10eafb5-bc46-3e23-a84d-def179f597b5 | -9.74219 | -47.71776 | 2025-10-07 12:36:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 28.0 |
| c5025eda-b6d1-3c58-8591-e08a182199c6 | -10.25404 | -44.35634 | 2025-10-07 12:36:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 2b404715-d257-30a4-b15c-185d34d7af75 | -8.44283 | -47.20804 | 2025-10-07 12:36:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 33.4 |
| afb2b7d0-1c40-3169-9989-1769f107b356 | -5.02161 | -43.64235 | 2025-10-07 12:36:00 | TERRA_M-T | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 35.1 |
| e2c9f85b-8620-365d-b428-1bc7b12db684 | -8.62912 | -47.27731 | 2025-10-07 12:36:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 39.1 |
| ae0bc484-d8b5-36b3-a03d-a952c858a95c | -4.28821 | -42.0329 | 2025-10-07 12:36:00 | TERRA_M-T | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 70.1 |
| 5ff54eaf-3b8d-3a68-a100-c5f848439880 | -8.5471 | -46.24891 | 2025-10-07 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 1bd3f8d8-7330-3198-90a0-07a568340f7f | -8.89173 | -47.64717 | 2025-10-07 12:36:00 | TERRA_M-T | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 9b5eccb1-7838-3441-81ec-5a09134e75ac | -2.88205 | -52.1436 | 2025-10-07 12:36:00 | TERRA_M-T | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| c762cfc4-9b54-36ca-9dcf-00d9a2c4f784 | -10.15226 | -45.48927 | 2025-10-07 12:36:00 | TERRA_M-T | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 315.5 |
| 84e54dc0-1661-30dd-b7a4-48ec4c9b23cb | -8.6621 | -46.27648 | 2025-10-07 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 5b3589a3-cf8a-32be-8df8-5ed5b65444ac | -9.17253 | -50.8331 | 2025-10-07 12:36:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| b9cae734-dbbc-319f-835a-984acf60280a | -10.20535 | -46.0311 | 2025-10-07 12:36:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 40.8 |
| a81d9c06-4f59-3755-a06b-36b31e2c1eb3 | -8.41804 | -50.70339 | 2025-10-07 12:36:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| e7a44645-dadd-3268-9e61-fd6f5a3e47ab | -8.65904 | -46.28888 | 2025-10-07 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 155.8 |
| e58b559d-4572-31ca-a9f3-2d470add10b0 | -3.40759 | -52.72297 | 2025-10-07 12:36:00 | TERRA_M-T | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0ef1ffa1-15d9-359f-a806-f147ca068135 | -3.9965 | -43.23974 | 2025-10-07 12:36:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 25.2 |
| cbeeb417-b210-3341-a63f-880dffab684f | -4.74224 | -43.21432 | 2025-10-07 12:36:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 489edb79-ce49-3864-8115-c477dfb99f0e | -8.87115 | -46.76626 | 2025-10-07 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |
| ce86cc9b-f142-3af7-a80e-30bdf3514397 | -3.09774 | -50.58051 | 2025-10-07 12:36:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| dca18d05-adf7-3b09-9435-10e829b366f2 | -8.21659 | -44.17357 | 2025-10-07 12:36:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 346.3 |
| e456b7d8-c85c-3107-98a9-56dfaee88137 | -4.04794 | -42.53403 | 2025-10-07 12:36:00 | TERRA_M-T | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 33.9 |
| b233c30b-ee0f-33d8-bcde-e2bd8d7fe9b3 | -4.86998 | -50.89532 | 2025-10-07 12:36:00 | TERRA_M-T | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c9531e93-975a-3ab1-876d-61d0e22ae795 | -3.09329 | -51.25271 | 2025-10-07 12:36:00 | TERRA_M-T | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 07da9cea-7a20-340d-88e3-d09f47e4e54f | -8.87291 | -46.7904 | 2025-10-07 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| dc5e6fe7-a428-3642-9808-59fa2de59193 | -2.89176 | -50.72993 | 2025-10-07 12:36:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 23363ff8-c32d-320b-ad54-bfde96b8e3c2 | -9.75136 | -47.72514 | 2025-10-07 12:36:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| bfe364d9-71cf-3850-b3f4-dc858df3761a | -5.44194 | -44.3548 | 2025-10-07 12:36:00 | TERRA_M-T | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 58106051-2ed8-3a04-ba2a-f37008c0aa2d | -8.86877 | -46.78433 | 2025-10-07 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 44818cd9-2ca9-37da-a8e1-82d734454fd2 | -5.89446 | -49.3717 | 2025-10-07 12:36:00 | TERRA_M-T | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0c2c5212-7041-30ea-86e5-40e1770c39a2 | -3.08885 | -50.57928 | 2025-10-07 12:36:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 984f84fb-dc3f-3954-906d-a23fcb132c97 | -4.29276 | -41.99726 | 2025-10-07 12:36:00 | TERRA_M-T | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 48.9 |
| f428e1f1-e5be-3d69-aafc-c8da2982f853 | -10.25077 | -44.38538 | 2025-10-07 12:36:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 2222668c-198d-38bf-89d7-8e432f009c27 | -8.48461 | -46.33784 | 2025-10-07 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| b44785c9-e504-3fe7-b576-2dd1bb55dc66 | -4.74478 | -43.20952 | 2025-10-07 12:36:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 9241770c-6a0d-363b-bda6-6cad9e07dfd1 | -8.96709 | -50.79631 | 2025-10-07 12:36:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 411dc6ff-55af-31f2-8f51-0b0930740f62 | -4.04556 | -42.50806 | 2025-10-07 12:36:00 | TERRA_M-T | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 121.7 |
| 64946e21-4ac8-315e-99dd-596b3bc32987 | -8.65977 | -46.29544 | 2025-10-07 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| bf86063c-8872-3762-b3e2-b411706c87e3 | -3.46307 | -50.0918 | 2025-10-07 12:36:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 720f167d-49b8-396c-a3b5-4a54cce01fc4 | -9.73778 | -48.27921 | 2025-10-07 12:36:00 | TERRA_M-T | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 040a64a2-15d2-3c5f-8328-212aa6e68e5a | -8.48836 | -46.29351 | 2025-10-07 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 186b2e0d-6d9a-3353-a182-d9b298fc054c | -3.01503 | -44.41587 | 2025-10-07 12:36:00 | TERRA_M-T | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 3bfbc918-3c7c-3f84-96d8-c90c9f1b5db5 | -8.22019 | -44.14552 | 2025-10-07 12:36:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 2aa6918e-c733-3fa7-a7e9-8b2b08082ac9 | -2.90063 | -50.73116 | 2025-10-07 12:36:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| ab901758-1c8b-38b0-b1a4-6e9c7704f8a1 | -4.06145 | -42.51012 | 2025-10-07 12:36:00 | TERRA_M-T | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 65.0 |
| dc4521c6-52ab-32a2-ace5-df3ab91ac962 | -8.1774 | -43.34157 | 2025-10-07 12:36:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 117.6 |
| 41b63d5e-b3b0-3bfe-a4ae-442aeb7ab980 | -6.72933 | -42.82631 | 2025-10-07 12:36:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.3 |
| 480c514b-9389-3d2e-8ea3-afe05cb56acb | -10.14598 | -45.48297 | 2025-10-07 12:36:00 | TERRA_M-T | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 2b55cd39-87d1-34a9-a065-b3145c528030 | -8.48045 | -49.21829 | 2025-10-07 12:36:00 | TERRA_M-T | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| f46e1c95-2547-3a4b-a566-b88b3613f656 | -10.25243 | -44.37988 | 2025-10-07 12:36:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 0fe9b199-c564-3c6f-9f68-36ff91434775 | -3.70145 | -49.70562 | 2025-10-07 12:36:00 | TERRA_M-T | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d45e7759-04c6-3f96-8f48-810697665f94 | -4.2825 | -42.02524 | 2025-10-07 12:36:00 | TERRA_M-T | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 71.8 |
| 6b29a71b-22b2-3b0d-a0ae-e67379db3ab3 | -7.47054 | -43.10138 | 2025-10-07 12:36:00 | TERRA_M-T | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 87.7 |
| 3cf1b547-56cc-3b30-919f-600a5878b211 | -3.09143 | -47.01731 | 2025-10-07 12:36:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 9bf974d5-0337-35f8-82cd-0355a20146aa | -3.48941 | -48.93046 | 2025-10-07 12:36:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| d269e095-b413-339a-9f1f-1820c4ea7c76 | -7.4637 | -42.60768 | 2025-10-07 12:36:00 | TERRA_M-T | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 37.5 |
| f7f60eb5-a2a0-31ce-8647-1b1698a6d601 | -8.48929 | -46.30025 | 2025-10-07 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 3d8ee98b-8eed-3e6e-a0e0-054a8aed81ea | -8.57483 | -46.23368 | 2025-10-07 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| f459e10f-4ea6-3eef-96c9-85414e02bcef | -5.64822 | -45.43576 | 2025-10-07 12:36:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 21e1838a-825e-33fa-b0bc-3834857498da | -3.43604 | -52.338 | 2025-10-07 12:36:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 896d6390-cc66-3c8f-80bb-99c6657d1f53 | -3.09013 | -50.57037 | 2025-10-07 12:36:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 5ea8aa27-170e-3ae3-b9c8-f8959b4e5152 | -5.43256 | -44.36042 | 2025-10-07 12:36:00 | TERRA_M-T | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| cb459366-6982-3802-8fe4-cef6784745f1 | -4.25818 | -48.55822 | 2025-10-07 12:36:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| a731858f-7a9b-3291-b39a-1e40aa206ce0 | -6.31842 | -49.3241 | 2025-10-07 12:36:00 | TERRA_M-T | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |


[Clique aqui para ver as próximas entradas](README114.md)
