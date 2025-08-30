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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f945ac32-80ab-3974-b987-a56e76fcb5ff | -13.3456 | -46.885 | 2025-08-30 07:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 703eef2c-3f69-3408-b6df-8dd46e23a46f | -11.876 | -46.4007 | 2025-08-30 07:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 15f60d60-5081-358a-86f1-428bf1ef3815 | -9.1155 | -65.7699 | 2025-08-30 07:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 41.4 |
| ec6e8e3f-7d85-348c-86f9-259e627efc61 | -11.8956 | -46.3753 | 2025-08-30 07:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 850d284e-a756-3573-b083-405b78c595cb | -11.8556 | -46.4714 | 2025-08-30 07:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 138.2 |
| 5b47b810-e0b9-34b7-adc2-61fb1367f86e | -11.8365 | -46.4741 | 2025-08-30 07:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 56c08d3e-441d-3d6b-a12c-e2d8c037b243 | -9.4433 | -60.5499 | 2025-08-30 07:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 47.9 |
| e5f0df01-f92e-3e3e-b971-24bebf4be6ff | -13.3843 | -46.879 | 2025-08-30 07:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 60.8 |
| fbb03292-7694-3aaf-8f35-90f8bf48b268 | -9.4498 | -62.3294 | 2025-08-30 07:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 254.5 |
| 33aaa138-227e-37d7-bcc7-000d9a5749e0 | -9.4497 | -62.3485 | 2025-08-30 07:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 131.9 |
| f6b965a9-ed53-345e-9fb5-5684b69b8ced | -13.3452 | -46.9077 | 2025-08-30 07:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 85.0 |
| d4e13b20-e61c-3484-acff-1fc7e0373ce3 | -11.8764 | -46.378 | 2025-08-30 07:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 68b904af-b91e-3e64-ba6d-490dfd5e9434 | -6.1853 | -43.3257 | 2025-08-30 07:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 8a70e7d6-90d9-3a22-bde0-cf68fe665eee | -11.8952 | -46.398 | 2025-08-30 07:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 50b3d572-fd5c-39db-925b-74f763f4763f | -9.0614 | -65.4355 | 2025-08-30 07:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 24336eab-4798-368f-9f74-ee5c6eafb0bd | -11.8369 | -46.4514 | 2025-08-30 07:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 122.2 |
| ae8d22ec-fdf1-3a3e-a542-c787d1c4af17 | -9.4683 | -62.3476 | 2025-08-30 07:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 7ccdcbc1-8269-37f4-a6e3-87793caee88b | -6.1665 | -43.3273 | 2025-08-30 07:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 481e9a39-a726-3be2-a929-1c1ad41ed0f0 | -11.8572 | -46.3807 | 2025-08-30 07:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 097b5d4b-ebca-3e18-84e3-4bd1708e5266 | -9.4684 | -62.3286 | 2025-08-30 07:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 264.7 |
| 2f2d6545-3c87-3918-b572-3ec9ca18cd23 | -13.3645 | -46.9047 | 2025-08-30 07:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 138.6 |
| b98edc55-0d70-37c8-8bbb-67e4a6216f29 | -13.3649 | -46.882 | 2025-08-30 07:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 198.0 |
| d003e5d9-781c-3b86-bd2a-8fae9bd9c7a6 | -9.4684 | -62.3286 | 2025-08-30 07:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 208.0 |
| 8b0d88ab-5d31-3fc4-b47e-c9dcd2a631b8 | -11.8365 | -46.4741 | 2025-08-30 07:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| c0b0e254-2057-359a-9901-c2dd52eb938d | -13.3821 | -46.9924 | 2025-08-30 07:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 6967e6c1-92f9-3acc-8b64-5de741520088 | -13.3817 | -47.015 | 2025-08-30 07:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 38b4b68b-5422-3161-bf31-9718aad114a8 | -13.3452 | -46.9077 | 2025-08-30 07:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 90302c55-2a61-360c-882a-fb4c551e9f55 | -9.4433 | -60.5499 | 2025-08-30 07:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 147991d1-2414-37e1-85c6-f1a658e1a2d9 | -13.383 | -46.947 | 2025-08-30 07:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 74.3 |
| f1d1fe2f-086e-38dd-b911-017b8035aad4 | -11.8556 | -46.4714 | 2025-08-30 07:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 1ca39100-dfb3-3c7b-bd62-562d64be23b1 | -13.3649 | -46.882 | 2025-08-30 07:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 176.9 |
| 2d040739-032d-367c-b7bc-c18d45488069 | -13.3825 | -46.9697 | 2025-08-30 07:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 038fbfe5-a165-3a9d-8091-eaae318753ed | -13.3632 | -46.9727 | 2025-08-30 07:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 120.7 |
| b9001049-3fe4-3de0-bcd2-2353d40cd17c | -11.8956 | -46.3753 | 2025-08-30 07:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 060584c6-7ffc-32a4-a906-720ed2e0c2b2 | -11.8952 | -46.398 | 2025-08-30 07:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 310706b4-c405-39d6-8df6-745f2c1986fb | -13.3456 | -46.885 | 2025-08-30 07:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 80.5 |
| ded5d847-4a6b-3edf-91c5-be9f12b218e2 | -13.3628 | -46.9953 | 2025-08-30 07:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 300.5 |
| b277716f-25d6-36c2-a230-9c2563c849c8 | -13.3623 | -47.018 | 2025-08-30 07:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 63de05ab-13f3-3c8d-b19f-9e1394eaaf59 | -11.8752 | -46.446 | 2025-08-30 07:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 91177ef1-a8c0-3608-ba38-64c504d8d906 | -11.856 | -46.4487 | 2025-08-30 07:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| aa358186-a618-3c89-ad4a-6af39a5bfb26 | -9.0614 | -65.4355 | 2025-08-30 07:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 8ad6c49a-cbde-3bae-b7f2-aac77da56dbe | -12.0153 | -43.9818 | 2025-08-30 07:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 9903655c-8158-33eb-936b-70e6cf4f1510 | -9.4683 | -62.3476 | 2025-08-30 07:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 121.2 |
| cba310a4-9678-3c4a-a34d-33964f161da0 | -11.8369 | -46.4514 | 2025-08-30 07:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| b1850f8e-51bd-31a8-bc19-65659bc836bb | -9.1155 | -65.7699 | 2025-08-30 07:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 755b465d-0e62-3f21-a443-7030bb75b862 | -9.4498 | -62.3294 | 2025-08-30 07:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 238.4 |
| d519a5b6-91ce-34d0-ad8c-17830040615d | -13.3645 | -46.9047 | 2025-08-30 07:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 816d18e6-2e7a-3aa7-9eef-05aa2db7ef7e | -11.8748 | -46.4687 | 2025-08-30 07:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 184.3 |
| 36c6712a-8670-3b9a-ab4a-7d133a5b4328 | -9.4497 | -62.3485 | 2025-08-30 07:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 155.9 |
| f47f2ace-11c5-31d8-a996-3981cfd8300d | -11.8764 | -46.378 | 2025-08-30 07:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 8a929e0e-43da-38ca-b13c-c762f41a3229 | -9.4498 | -62.3294 | 2025-08-30 07:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 249.9 |
| b695295e-659c-3cba-a4ff-4ab906af452b | -13.3452 | -46.9077 | 2025-08-30 07:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 111.9 |
| d8fd6e9d-a361-3e4d-b155-802842fea52d | -9.1155 | -65.7699 | 2025-08-30 07:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 5997e58c-ccc2-3097-a63d-65eb752beb90 | -13.3623 | -47.018 | 2025-08-30 07:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 03d67538-f442-37c7-8aaf-9c3beaa394dc | -13.3628 | -46.9953 | 2025-08-30 07:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 230.8 |
| a80d28cb-690b-3828-ae5f-45ebee374a75 | -9.0614 | -65.4355 | 2025-08-30 07:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 57e8bc3e-0b04-3df8-9d98-6a716b85ce69 | -13.3649 | -46.882 | 2025-08-30 07:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 185.5 |
| c31cba6e-71b3-3ec6-b373-97678319a132 | -11.8764 | -46.378 | 2025-08-30 07:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| ef4dfad5-ff06-3c7b-bdf7-9ec890b13ffa | -11.876 | -46.4007 | 2025-08-30 07:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| f54e6403-7097-31b0-98a1-5e7187f8266b | -13.3645 | -46.9047 | 2025-08-30 07:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 0d63156b-622c-37fe-84db-6288a015e8bc | -13.3632 | -46.9727 | 2025-08-30 07:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 8bfa44bf-0afe-3515-a2c6-0bed75865eec | -9.4497 | -62.3485 | 2025-08-30 07:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 135.0 |
| edfc66f1-1849-3c46-a33e-df7a4addaa32 | -9.4433 | -60.5499 | 2025-08-30 07:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 2e2d96a1-ec70-3611-a108-f7a15332fc43 | -13.383 | -46.947 | 2025-08-30 07:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 167.1 |
| 9912bd5b-031b-319f-bb7f-330d51686f1d | -11.8956 | -46.3753 | 2025-08-30 07:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| d0199489-c034-3076-8dc6-7d588214bc4e | -13.3821 | -46.9924 | 2025-08-30 07:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 79.5 |
| ca06f463-8e40-3cc6-8e47-ac2ea4ec1ce8 | -13.3456 | -46.885 | 2025-08-30 07:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 0b986991-71de-3cc6-8981-3eb46cea4a76 | -9.4684 | -62.3286 | 2025-08-30 07:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 204.9 |
| 2ca13783-1fd1-3318-871b-aaf84762a25b | -9.4683 | -62.3476 | 2025-08-30 07:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 93.6 |
| a26e4514-06d9-315c-9972-9bcb4fcbb198 | -11.8952 | -46.398 | 2025-08-30 07:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 163.9 |
| a6764b44-9a43-345c-97b6-592130e9bbbf | -13.3825 | -46.9697 | 2025-08-30 07:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 207.1 |
| 34a12851-5c67-31d0-a88a-7a5023571057 | -9.4433 | -60.5499 | 2025-08-30 07:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 86.8 |
| aed3af8f-6a9c-3d65-9127-64c4f7a4c4cb | -13.3452 | -46.9077 | 2025-08-30 07:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 2bc458e1-c370-3df9-9a57-2700c2072e7e | -11.8764 | -46.378 | 2025-08-30 07:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| e59aeea7-f61a-3921-9f90-f5a09de9f977 | -9.4432 | -60.5692 | 2025-08-30 07:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| d2eae925-321d-389c-ae0d-f4353f382983 | -13.3645 | -46.9047 | 2025-08-30 07:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 5a1ca0a9-9609-3866-8a2a-560c2f506348 | -13.3649 | -46.882 | 2025-08-30 07:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 229.0 |
| cf42708e-3e5b-3344-bf45-68ed587bacb6 | -11.8952 | -46.398 | 2025-08-30 07:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 52318a6e-7188-3a9d-8115-c90499fe6c36 | -13.3456 | -46.885 | 2025-08-30 07:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 5520aaeb-8c0a-3239-bbfd-36d8dd06f40f | -13.3843 | -46.879 | 2025-08-30 07:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 97.7 |
| eb935d49-d9cb-38b7-8e70-3e713ce8e63f | -9.0799 | -65.4349 | 2025-08-30 07:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 8011c078-36cc-3b5c-8905-81539efda7a5 | -9.0614 | -65.4355 | 2025-08-30 07:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 000260b6-fec0-31b3-9c02-fece08f331c4 | -9.4497 | -62.3485 | 2025-08-30 07:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 119.5 |
| 6e73fc92-3f64-3133-9325-6db92e27800e | -9.1155 | -65.7699 | 2025-08-30 07:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 92cb8bae-58a7-3380-9558-2fa27f569309 | -13.383 | -46.947 | 2025-08-30 07:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 64142b6a-8879-323d-a2ae-9c995eb518aa | -11.8956 | -46.3753 | 2025-08-30 07:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 2f20046a-f43d-361b-8aab-3f9276c2cc7a | -9.4683 | -62.3476 | 2025-08-30 07:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 49a69e0c-ea2e-3f3d-b90e-aac77ad1fd7a | -9.4498 | -62.3294 | 2025-08-30 07:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 245.6 |
| 35383f3f-830a-3df4-a8b4-0fa68893cf8b | -11.876 | -46.4007 | 2025-08-30 07:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| f4ca33a0-3884-3c04-84a3-3e64294be214 | -9.4684 | -62.3286 | 2025-08-30 07:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 170.0 |
| 3a8e276c-b92d-37ae-a868-31b536634e1b | -7.89637 | -63.00069 | 2025-08-30 07:33:00 | AQUA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 27439bd0-5a68-38a7-a33e-637fd5daaac1 | -9.44376 | -62.31673 | 2025-08-30 07:33:00 | AQUA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 23a66463-22b9-3860-a147-03b6a832671e | -9.45572 | -62.35616 | 2025-08-30 07:33:00 | AQUA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 59.9 |
| b461e111-3037-31ad-974c-d968785fb5d5 | -9.0609 | -65.42975 | 2025-08-30 07:33:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 51a8f71c-bd14-360a-aba9-113340db4389 | -9.4646 | -62.32693 | 2025-08-30 07:33:00 | AQUA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 1e42d164-affa-38c5-bbe3-4d0a86e60713 | -8.60927 | -72.38893 | 2025-08-30 07:33:00 | AQUA_M-M | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b7ae3ef9-6dad-395a-8135-d54ee88a9190 | -9.44785 | -62.32497 | 2025-08-30 07:33:00 | AQUA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 308.2 |
| 1afe9f4c-805a-3539-8ad3-90fcd8fabcc2 | -9.46052 | -62.31859 | 2025-08-30 07:33:00 | AQUA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 263.7 |
| fbea59ae-36b6-3a13-9b69-0bdd02999260 | -9.11136 | -65.74969 | 2025-08-30 07:33:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 22937dfc-6e72-339b-9d94-f006ac61fb94 | -9.44338 | -62.36224 | 2025-08-30 07:33:00 | AQUA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 47.7 |


[Clique aqui para ver as próximas entradas](README90.md)
