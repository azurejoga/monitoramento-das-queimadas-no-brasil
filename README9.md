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
| b48d37a8-b50c-3e6d-a076-78d396683ea2 | -6.41268 | -49.5834 | 2024-10-15 00:20:00 | TERRA_M-M | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 46bc85fa-632f-34ad-9b89-de3d509c8c25 | -6.4094 | -44.36365 | 2024-10-15 00:20:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| a48ab237-00f0-373d-84bf-0cf45a6e9479 | -6.37392 | -44.09296 | 2024-10-15 00:20:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| d3e1b3d6-0b38-35a2-8e0f-90a4f013c526 | -6.04471 | -46.60112 | 2024-10-15 00:20:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 10154c67-6266-34d3-84b5-38b1ec5810aa | -6.03749 | -46.60748 | 2024-10-15 00:20:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 32.1 |
| ada5ddf3-ee18-3c8e-8cc0-a6184f1ad7b6 | -8.01065 | -44.8031 | 2024-10-15 00:20:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 21.9 |
| f2c3733a-401a-3d81-9f60-6731db852c30 | -3.94938 | -46.44539 | 2024-10-15 00:22:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 5de5d3ef-b6ea-304b-909a-d0d268ed6fd6 | -3.85525 | -46.90211 | 2024-10-15 00:22:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 26.5 |
| c4b0d39a-c27c-38f1-aaaa-05591d76917a | -3.85276 | -46.91961 | 2024-10-15 00:22:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 4e2f73f8-9155-3d8e-99d2-a1937d3aa804 | -3.8499 | -46.89735 | 2024-10-15 00:22:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 96f92cc7-9417-3a2e-aad2-e31a577f1225 | -3.72767 | -49.00171 | 2024-10-15 00:22:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 246.1 |
| 5886423d-a138-3a5c-8903-e99e7c5dcca6 | -3.71843 | -49.00938 | 2024-10-15 00:22:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 265fefaf-f559-3bc2-8b59-1284b9179ebb | -3.15888 | -50.46248 | 2024-10-15 00:22:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 2396bffa-4eed-3669-96b0-881f7afd23bb | -3.1583 | -50.46952 | 2024-10-15 00:22:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 0323afe1-82fb-3b76-b842-809cac6f2c97 | -2.81881 | -45.286 | 2024-10-15 00:22:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 26d94e6f-afa5-39c1-afb0-89a0e683fa7e | -2.81743 | -45.29589 | 2024-10-15 00:22:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 5014827d-325d-34d4-83d3-9b7e9b7ffa5f | -2.81535 | -45.28012 | 2024-10-15 00:22:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 62df7ec7-1554-3953-a753-6a3c31b8db70 | -2.80722 | -45.28758 | 2024-10-15 00:22:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 722f4cf4-0c9b-33b2-92a9-a2eff7a77363 | -2.62532 | -49.28734 | 2024-10-15 00:22:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 8eed4bc8-2e67-3adc-9e37-c5ff767900d1 | -2.43915 | -50.24049 | 2024-10-15 00:22:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 118.3 |
| 472fafc2-dbcb-341d-a33a-7cb6602ae9b1 | -2.43639 | -50.248 | 2024-10-15 00:22:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 101.9 |
| d3d550a2-1266-35d2-ade7-e84bc148ac60 | -2.40143 | -44.84059 | 2024-10-15 00:22:00 | TERRA_M-M | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| ef036aaa-f627-3b4c-bac0-05b3f8f33d8b | -2.39882 | -44.83278 | 2024-10-15 00:22:00 | TERRA_M-M | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 3a4cf751-9417-392f-b73f-03b2e0a6cb07 | -2.38793 | -47.59381 | 2024-10-15 00:22:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| fef97f4a-813d-3da1-a83e-84eff52eae0f | -2.11838 | -46.05837 | 2024-10-15 00:22:00 | TERRA_M-M | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 1dc3c65d-c128-3ec3-bd07-41a8524435d7 | -1.86904 | -47.85469 | 2024-10-15 00:22:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 35924834-cc1c-3749-9338-cf43aa67286f | -1.86563 | -47.83032 | 2024-10-15 00:22:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 04b0b7b3-d925-3719-a351-3b2cf750f35a | -1.6826 | -46.43171 | 2024-10-15 00:22:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 3227065a-079c-38f1-8754-4a9026460661 | -1.47071 | -47.16391 | 2024-10-15 00:22:00 | TERRA_M-M | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 465f0f82-4b5d-32e3-828c-3bc3c39a0370 | -5.2244 | -43.7298 | 2024-10-15 00:22:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 166.2 |
| 5f1fc14e-b9d7-3702-9f41-5c0e0e043880 | -5.22264 | -43.71666 | 2024-10-15 00:22:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 02965982-37ff-3f0b-a177-575eb34a0474 | -5.21376 | -43.73134 | 2024-10-15 00:22:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 429868fa-4687-31de-9702-b0d5e023290a | -5.12249 | -41.68304 | 2024-10-15 00:22:00 | TERRA_M-M | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 75c675d7-153f-3d1b-b673-0615520c7500 | -5.12115 | -41.67321 | 2024-10-15 00:22:00 | TERRA_M-M | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| bb0f2bf4-dc32-3926-a05f-aa566bd8cdda | -5.05222 | -40.89952 | 2024-10-15 00:22:00 | TERRA_M-M | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| d0e39e94-de92-3241-b5ca-127b89017c4b | -5.04384 | -43.67313 | 2024-10-15 00:22:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 1abee52a-0123-3715-9ae4-1f1dbd532e29 | -5.04211 | -43.66024 | 2024-10-15 00:22:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 39.7 |
| 0262bc21-8e7c-3d0d-95f9-d73169d53c64 | -4.7862 | -39.77752 | 2024-10-15 00:22:00 | TERRA_M-M | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| b6bf7111-4b72-399c-88c7-d3044d9bb980 | -4.52024 | -42.89632 | 2024-10-15 00:22:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| eeadde5b-a923-3d5f-90e3-f19022ae4ae0 | -4.51875 | -42.88511 | 2024-10-15 00:22:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 2f1a3519-cc39-35e2-977c-2bac39603aaf | -4.51856 | -42.89147 | 2024-10-15 00:22:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 431bc42e-1a99-33d1-bdc0-af00d73c4db0 | -4.23565 | -40.39261 | 2024-10-15 00:22:00 | TERRA_M-M | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 0a4e79ad-f7bc-36d5-9195-c3799f248c10 | -4.23442 | -40.38374 | 2024-10-15 00:22:00 | TERRA_M-M | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 3e0a7482-38b9-3035-8413-cc0e8c68823f | -4.22679 | -40.39387 | 2024-10-15 00:22:00 | TERRA_M-M | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 540ac121-fc18-30cf-87e1-8098f0ab2577 | -4.22556 | -40.38499 | 2024-10-15 00:22:00 | TERRA_M-M | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 5cc3b78d-9ebf-3a48-b64a-660415b798d0 | -4.10156 | -42.29805 | 2024-10-15 00:22:00 | TERRA_M-M | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| a6d6cc73-f3f1-3719-a39f-72ec9288c6b3 | -4.10016 | -42.28777 | 2024-10-15 00:22:00 | TERRA_M-M | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| ed91f70e-920d-346c-b09f-b92510445702 | -4.09204 | -42.29933 | 2024-10-15 00:22:00 | TERRA_M-M | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| d4a21600-5667-34c9-9f45-57a2a6b781e8 | -4.02549 | -43.24643 | 2024-10-15 00:22:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7d646e01-72a3-33a3-8969-7baa36fefb43 | -4.02393 | -43.2348 | 2024-10-15 00:22:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 108acc5f-844e-3675-b004-bbfe7e5a0171 | -3.51483 | -43.24678 | 2024-10-15 00:22:00 | TERRA_M-M | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c0c4d25d-3ee7-3ef0-b9bf-021c2c1a6867 | -3.42634 | -43.34786 | 2024-10-15 00:22:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 809e2024-8e00-3748-999a-819ca24365dc | -3.41626 | -43.34925 | 2024-10-15 00:22:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 6a26983b-4799-3a05-9e3b-b3dfff3ee6da | -3.17732 | -43.24755 | 2024-10-15 00:22:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| cfc6ebfd-99ea-3a7e-99aa-ea37d6c9c562 | -5.5853 | -44.88727 | 2024-10-15 00:22:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| b4dd21cb-bd93-3aa0-bb4d-8a7f5e86e587 | -5.49113 | -46.24486 | 2024-10-15 00:22:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 333494a3-6bd7-36d7-88fd-a5b5a2f14577 | -5.30023 | -46.3882 | 2024-10-15 00:22:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 07822508-dd63-374c-a92b-4e9019855bad | -5.28697 | -46.38983 | 2024-10-15 00:22:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 26bffc59-1136-3a27-96f3-b139b3b8492e | -5.27451 | -46.3755 | 2024-10-15 00:22:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 09c0ae03-b3fd-37d9-be59-523b84a076f7 | -5.27375 | -46.39167 | 2024-10-15 00:22:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 19.0 |
| bd837995-202f-3e0f-9a71-76ea0ca752eb | -5.27106 | -46.37064 | 2024-10-15 00:22:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 2f5b7e99-dec6-3ccb-bd1b-d97fb6aa5c0c | -5.2152 | -44.8624 | 2024-10-15 00:22:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 4ba49ce7-c74c-35e5-93c0-28714560292b | -5.21307 | -44.84655 | 2024-10-15 00:22:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 182.1 |
| 2bb6ef8a-8cd3-3a24-8633-244da783d691 | -5.20138 | -44.8478 | 2024-10-15 00:22:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| b19a0e24-6517-342b-a9a5-855b34e06cba | -5.16395 | -45.07439 | 2024-10-15 00:22:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 5c68de7e-ce2a-39b9-9cbc-e204f1c01346 | -4.72233 | -46.16521 | 2024-10-15 00:22:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 20.2 |
| f790dab2-2cb7-306f-a41e-70a1188c2091 | -4.70943 | -46.16671 | 2024-10-15 00:22:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 43.4 |
| f1f13b94-1a78-34db-a9f9-155a621a3bf9 | -4.68654 | -45.79811 | 2024-10-15 00:22:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 27ac20eb-0939-3a87-89b8-fae3b770abf3 | -4.68411 | -45.77989 | 2024-10-15 00:22:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 7c2fb6bf-3fa2-3baf-8c79-8a83510a314b | -4.54097 | -46.56384 | 2024-10-15 00:22:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 32.0 |
| fc0efaf9-8d95-35d4-939a-2ac6db06e501 | -4.53997 | -46.58009 | 2024-10-15 00:22:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 17438103-6417-3f90-a7e8-9a702b8e938f | -4.53728 | -46.55888 | 2024-10-15 00:22:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 57d2d1bd-37be-3802-8f6a-dedcd94a21d7 | -4.46553 | -45.8974 | 2024-10-15 00:22:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 20.4 |
| d6744e26-22c4-37fe-bc94-8830be77c18a | -4.46315 | -45.87897 | 2024-10-15 00:22:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 17.5 |
| ab0a608e-2ff1-3f61-8f3d-31af054e18c7 | -4.46157 | -45.88465 | 2024-10-15 00:22:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 28.5 |
| d4763360-7b48-34ab-9643-b9ac2aeec50f | -4.38718 | -47.78562 | 2024-10-15 00:22:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 1c4bd6e2-3afe-34f3-8a84-0b6509d56d86 | -4.38368 | -47.75895 | 2024-10-15 00:22:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| c69dfc82-22ce-3b81-9169-41d36742098b | -4.02454 | -47.21672 | 2024-10-15 00:22:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 23.5 |
| c6d0a6c3-d8b8-36d2-a4b3-078f5a8287e3 | 1.0199 | -52.2162 | 2024-10-15 00:25:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 52721355-1a21-3b10-8ea5-75b9de624a39 | -1.5493 | -54.3557 | 2024-10-15 00:25:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| d79c7702-f2bb-3bd4-a3fb-c601a71f81e2 | -1.5493 | -54.3357 | 2024-10-15 00:25:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 4bd87f7d-36dd-3024-a899-520c392911c6 | -1.8577 | -47.8493 | 2024-10-15 00:25:16 | GOES-16 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| da03b621-a975-3451-941f-aa6de9abf50b | -2.4418 | -50.2447 | 2024-10-15 00:25:20 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 4624aecd-241f-3671-b1d6-bbbf48e5d631 | -2.501 | -49.0802 | 2024-10-15 00:25:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 0f2ef375-1469-38b2-bfc4-83f938593590 | -2.5028 | -48.5455 | 2024-10-15 00:25:20 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 9a94f46c-ccb8-3290-9f5e-fe573cc0224b | -3.0581 | -53.2598 | 2024-10-15 00:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| d5152b9f-d888-3dd2-ae62-4d8ae6dd81e9 | -3.1099 | -54.2263 | 2024-10-15 00:25:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| fd3ae062-b8e1-372f-82a2-750ace140147 | -3.1282 | -54.2459 | 2024-10-15 00:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 16bb0700-7b16-39cb-8ef2-c552720b23c4 | -3.1283 | -54.2259 | 2024-10-15 00:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 129.5 |
| b2283de9-ee46-3503-b9dc-35044a8ca486 | -3.4883 | -51.5483 | 2024-10-15 00:25:26 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 563b90b1-50bc-34ec-a6ad-98f7b1059be3 | -3.7218 | -48.9979 | 2024-10-15 00:25:27 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 155.2 |
| f42b2d29-0c87-36f2-98dd-21d5ba005555 | -3.7403 | -48.9972 | 2024-10-15 00:25:27 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 124.4 |
| b32f44e3-f800-3f13-b94e-24256133f6d1 | -4.3774 | -47.7627 | 2024-10-15 00:25:31 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 22aaec5c-3c8b-3a29-b4c8-885e77e856af | -4.3959 | -47.7618 | 2024-10-15 00:25:31 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| ecb30fc3-1746-3d44-9e5d-a067eb7e8717 | -5.1983 | -44.8497 | 2024-10-15 00:25:35 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| b73d5b24-2a8b-368b-905c-759064bc3cd0 | -5.217 | -44.8485 | 2024-10-15 00:25:35 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 139.5 |
| 044fec61-0b12-304a-a264-7248dbe1d17c | -5.2982 | -46.3936 | 2024-10-15 00:25:36 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 164aa31c-1ff1-3181-a718-cc43f135e1ab | -5.5732 | -49.3995 | 2024-10-15 00:25:37 | GOES-16 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| be342bc1-f478-3a3a-bf02-b8213086c43d | -6.5505 | -48.2408 | 2024-10-15 00:25:43 | GOES-16 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 559dcba9-e64c-34cc-b5c3-8cfde74fa27c | -7.5093 | -49.4831 | 2024-10-15 00:25:48 | GOES-16 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |


[Clique aqui para ver as próximas entradas](README10.md)
