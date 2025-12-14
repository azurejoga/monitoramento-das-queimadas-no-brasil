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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2476fa3-ea84-3ed7-99ab-3ca80bd73526 | -8.0696 | -43.1452 | 2025-12-14 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.6 |
| 876bc6ce-f7f4-38e1-bb5c-374456970275 | -2.4767 | -45.4534 | 2025-12-14 01:00:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 83.6 |
| a80794cc-094a-3442-ae08-4bd931cec357 | -2.8874 | -44.9892 | 2025-12-14 01:00:00 | GOES-19 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 40cb1e02-d53d-3fc0-b5d3-60881894eab4 | -8.0513 | -43.1001 | 2025-12-14 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.3 |
| 99447b62-c027-307e-815c-e7e84fe8bdc0 | -5.6797 | -39.2841 | 2025-12-14 01:00:00 | GOES-19 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 80.3 |
| 0c177535-a8f0-3231-99bd-69be4f47396a | -3.6277 | -45.6797 | 2025-12-14 01:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 44.7 |
| c00cd143-880d-3de8-a02b-94e04cde369d | -1.5296 | -45.678 | 2025-12-14 01:00:00 | GOES-19 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 2350b3ca-62d1-33da-b27d-59aefda1ca9f | -8.0327 | -43.0786 | 2025-12-14 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 86.9 |
| 2fd8001a-43d2-399e-bcb6-76b01f10cf38 | -8.0324 | -43.1022 | 2025-12-14 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 103.3 |
| 13b7ebdf-8ac4-30cc-9505-fae5aa410422 | -2.8875 | -44.9666 | 2025-12-14 01:00:00 | GOES-19 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 176.4 |
| 310302fc-b47f-3477-8e90-d538d0969bb0 | -3.4451 | -41.6413 | 2025-12-14 01:00:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 57.8 |
| ed8773a8-02cb-3bd4-bd0b-0d320e49b622 | -8.0327 | -43.0786 | 2025-12-14 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.3 |
| 63e7f7ec-2d35-3ac5-9a7d-83bf527ecbb6 | -5.6797 | -39.2841 | 2025-12-14 01:10:00 | GOES-19 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 63.3 |
| 04808163-674a-321d-93ca-2f18b00fb861 | -2.4768 | -45.4309 | 2025-12-14 01:10:00 | GOES-19 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 137.8 |
| e26e1a66-c24f-3c8a-90cc-f3c53e864b42 | -3.4451 | -41.6413 | 2025-12-14 01:10:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 62.7 |
| d75f7410-0c27-3959-bc2c-df887ec11339 | -5.68 | -39.259 | 2025-12-14 01:10:00 | GOES-19 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 72.6 |
| fa721430-704f-335c-a51d-54ca95595426 | -1.5296 | -45.678 | 2025-12-14 01:10:00 | GOES-19 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 36283014-584d-34c1-8ef7-ed281e13fb7c | -2.8875 | -44.9666 | 2025-12-14 01:10:00 | GOES-19 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 166.1 |
| 7ccdcd14-37d0-3eaa-b7a0-5c89dedb5d23 | -5.6611 | -39.2607 | 2025-12-14 01:10:00 | GOES-19 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 48.5 |
| 8ef5d57f-8d3a-3502-8add-9a28fccb2244 | -16.2383 | -58.8395 | 2025-12-14 01:10:00 | GOES-19 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 65.9 |
| a76286ee-beb1-32a6-a525-541f30e31c56 | -8.0696 | -43.1452 | 2025-12-14 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.8 |
| d4c6a4b5-7d6a-3b42-90f4-f80e4f651ede | -2.4767 | -45.4534 | 2025-12-14 01:10:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 85.7 |
| a4916fc4-4a65-315e-a71f-7cfbba54597d | -3.6277 | -45.6797 | 2025-12-14 01:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 739ac51d-6897-3470-b851-571a2e430660 | -2.4954 | -45.4303 | 2025-12-14 01:10:00 | GOES-19 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 37f4faed-7782-354b-934d-f807c3c1bc7d | -8.0324 | -43.1022 | 2025-12-14 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 118.1 |
| ff0dd6d6-1e58-399b-a0e2-f5f60bba97cb | -16.2267 | -58.8172 | 2025-12-14 01:15:00 | METOP-B | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 279243b0-b80c-3b62-9b6f-86d273c69f3f | -16.229 | -58.826599 | 2025-12-14 01:15:00 | METOP-B | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e84aedec-b56f-39d3-80ef-a2ed2d393b35 | -5.68 | -39.259 | 2025-12-14 01:20:00 | GOES-19 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 59.4 |
| 4cc9bd26-c42d-31bd-8979-b38ff14ebc9f | -8.0327 | -43.0786 | 2025-12-14 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 55.8 |
| 737d914d-a97f-30af-9b03-88ab956a34fc | -2.8875 | -44.9666 | 2025-12-14 01:20:00 | GOES-19 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 142.6 |
| 1ba6d97a-63e4-3bf1-9090-efc262ac2cd8 | -1.5296 | -45.678 | 2025-12-14 01:20:00 | GOES-19 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 50ecb9c6-4285-3da0-8a40-1b75969d49f1 | -8.0324 | -43.1022 | 2025-12-14 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.2 |
| d9c5630e-b421-3d22-81bf-732a34570056 | -2.4767 | -45.4534 | 2025-12-14 01:20:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 769bcf9d-b976-3365-97e3-2bc0ee385890 | -3.6277 | -45.6797 | 2025-12-14 01:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 53.0 |
| fa58146b-c8cd-3e00-8502-5d83ae9cecb0 | -2.8857 | -45.3726 | 2025-12-14 01:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 13841d23-28c3-34b1-aa2e-465c86273ea7 | -5.6797 | -39.2841 | 2025-12-14 01:20:00 | GOES-19 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 57.3 |
| 5cf77736-8276-37c3-a0d3-f4e2b0a7b0fa | -2.4768 | -45.4309 | 2025-12-14 01:20:00 | GOES-19 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 144.6 |
| 58ecce8a-2bac-3ec2-a514-330baefc78b2 | -8.0696 | -43.1452 | 2025-12-14 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 57.8 |
| 0e033d2d-84a7-3606-89ba-61f2a7ba61e0 | -16.2383 | -58.8395 | 2025-12-14 01:20:00 | GOES-19 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 68.2 |
| ab02a99f-1955-3aca-9583-42c382716ce6 | -8.0324 | -43.1022 | 2025-12-14 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 85.6 |
| 30c4a546-0eaa-34c9-a455-375777069511 | -2.4767 | -45.4534 | 2025-12-14 01:30:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 1735b406-e9cc-361e-bfc5-607f1588a5b6 | -2.8876 | -44.9439 | 2025-12-14 01:30:00 | GOES-19 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 1a308c2e-dd15-3645-9c84-dfb4a972d4db | -2.8875 | -44.9666 | 2025-12-14 01:30:00 | GOES-19 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 185.3 |
| d18e7909-4401-3402-afb7-e12fd8c7bf17 | -5.68 | -39.259 | 2025-12-14 01:30:00 | GOES-19 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 58.1 |
| 7eae53fc-0af1-382a-9733-03bfc20e470b | -1.5296 | -45.678 | 2025-12-14 01:30:00 | GOES-19 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 8628fa8c-e74d-3d47-8058-c800eb77a117 | -2.4768 | -45.4309 | 2025-12-14 01:30:00 | GOES-19 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 721eeca6-e008-301a-91fb-3674def60e92 | -8.0696 | -43.1452 | 2025-12-14 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 51.5 |
| b5762280-2939-3562-9787-5538564a1e18 | -8.0327 | -43.0786 | 2025-12-14 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.1 |
| 71cca1f3-d169-3a10-968c-ecc70740b769 | -3.4451 | -41.6413 | 2025-12-14 01:30:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 62.9 |
| cbf600ba-78a0-3bec-9573-4dc0d1d79a54 | -5.6797 | -39.2841 | 2025-12-14 01:30:00 | GOES-19 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 63.7 |
| d54c7a7a-1987-37ca-ab2b-ec95717cbc11 | -16.2383 | -58.8395 | 2025-12-14 01:30:00 | GOES-19 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 55.7 |
| 40ff9ba2-4326-3a3d-87a3-5b30f2d56de6 | -8.0696 | -43.1452 | 2025-12-14 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 56.8 |
| 44372a15-4cb0-30a5-9bff-e5067c9ed7bf | -8.0324 | -43.1022 | 2025-12-14 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.5 |
| 434c679b-8431-3652-a56b-7b939f08b12d | -1.5296 | -45.678 | 2025-12-14 01:40:00 | GOES-19 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 64.6 |
| fb67eb7a-38a1-3b18-bc79-179c6ec2396e | -5.68 | -39.259 | 2025-12-14 01:40:00 | GOES-19 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 65.6 |
| 7c5a9a2b-4427-37b7-9bbc-c004cf044ebf | -2.8876 | -44.9439 | 2025-12-14 01:40:00 | GOES-19 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 44f8ecc1-108b-3785-83a3-ef141d025a8a | -2.8874 | -44.9892 | 2025-12-14 01:40:00 | GOES-19 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 69.9 |
| a466d740-4a7a-389d-b3ba-dc514b4d9786 | -2.8875 | -44.9666 | 2025-12-14 01:40:00 | GOES-19 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 271.1 |
| be8514a9-e2c8-30d6-9842-caaf18d91fb5 | -5.6797 | -39.2841 | 2025-12-14 01:40:00 | GOES-19 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 53.4 |
| e8fc3889-f1ac-3c7d-9767-0d50bc1cd794 | -8.0327 | -43.0786 | 2025-12-14 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 54.6 |
| 367a717c-9d37-3218-8082-858715e32fc1 | -5.6611 | -39.2607 | 2025-12-14 01:40:00 | GOES-19 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 41.7 |
| 7293ea94-dd0e-3cb9-9370-c15d6328e49b | -2.8857 | -45.3726 | 2025-12-14 01:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 63.6 |
| dfd06264-b522-361e-aad1-00a69a59192c | -2.4768 | -45.4309 | 2025-12-14 01:40:00 | GOES-19 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 74e45c8e-f027-3eb5-8be5-2ea215ed7dba | -2.9061 | -44.9659 | 2025-12-14 01:40:00 | GOES-19 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 4d68c074-8d3a-3c31-bea1-cb209689c14b | -8.0513 | -43.1001 | 2025-12-14 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 52.6 |
| 69a5c9c9-c47c-3c44-bf74-54bb1c873fa6 | -2.4768 | -45.4309 | 2025-12-14 01:50:00 | GOES-19 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 86.5 |
| a002dcf1-3ad3-3f7a-906c-0e0cf49294cc | -8.0327 | -43.0786 | 2025-12-14 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 49.9 |
| 1fb06a9d-3d1f-30a4-9cca-20c0ab7769b1 | -8.0696 | -43.1452 | 2025-12-14 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 60.4 |
| a42cd482-a035-3512-8509-b3228d46b0de | -2.8875 | -44.9666 | 2025-12-14 01:50:00 | GOES-19 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 178.2 |
| 2f830cec-0316-3034-8bcd-215ffcf506fd | -2.9061 | -44.9659 | 2025-12-14 01:50:00 | GOES-19 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 31922103-214a-3c10-921e-edfdff8d7763 | -5.6797 | -39.2841 | 2025-12-14 01:50:00 | GOES-19 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 54.3 |
| c887a1b4-da79-3ee7-91e8-71193a6020ec | -2.216 | -45.6848 | 2025-12-14 01:50:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 82.3 |
| a6341f44-d317-300a-9013-f462ce08d723 | -8.0324 | -43.1022 | 2025-12-14 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.0 |
| dac173f2-84c2-3a1d-be5e-d92a99393fb1 | -2.8876 | -44.9439 | 2025-12-14 01:50:00 | GOES-19 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 55879693-cd9a-34de-a27e-d978b010b322 | -5.68 | -39.259 | 2025-12-14 01:50:00 | GOES-19 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 60.5 |
| a639956a-7170-388e-bf28-d079e1d8fb72 | -2.8875 | -44.9666 | 2025-12-14 02:00:00 | GOES-19 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 187.2 |
| 60bf8aed-465a-3267-9c1b-5221ec60e6d1 | -2.8857 | -45.3726 | 2025-12-14 02:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 1e50287c-e921-3996-9dc7-5060ff0842a3 | -2.8876 | -44.9439 | 2025-12-14 02:00:00 | GOES-19 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 60.7 |
| db67aa09-0679-3142-8a9c-3f6ebd0bb606 | -8.0327 | -43.0786 | 2025-12-14 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.2 |
| 2acc9232-b49a-35b7-9c7a-d90fdb158809 | -8.0696 | -43.1452 | 2025-12-14 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 55.6 |
| f502ddcf-4a3b-3858-a0be-5540392a10eb | -2.216 | -45.6848 | 2025-12-14 02:00:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 41819dea-1152-33ca-924e-f591bc6636de | -5.68 | -39.259 | 2025-12-14 02:00:00 | GOES-19 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 64.0 |
| f8bc3cdf-b5bb-3815-9b29-dae1bff31b5f | -8.0324 | -43.1022 | 2025-12-14 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.7 |
| 2dd82609-a231-31ce-a1f0-b120da3515bd | -1.5296 | -45.678 | 2025-12-14 02:00:00 | GOES-19 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 5975d9ff-175d-31ea-abb4-a7d8bc647216 | -5.6797 | -39.2841 | 2025-12-14 02:00:00 | GOES-19 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 62.6 |
| 1ddbb98a-c459-3555-a439-de4e8c8b4793 | -2.4768 | -45.4309 | 2025-12-14 02:00:00 | GOES-19 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 10264a26-0b72-3548-bb02-8f1326d7e849 | -8.0327 | -43.0786 | 2025-12-14 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 56.6 |
| 7c3e9059-bdbb-314b-913e-cc5cd4a92d4b | -5.68 | -39.259 | 2025-12-14 02:10:00 | GOES-19 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 46.1 |
| 0b21b210-6d89-3345-bac2-4dba8e5d5238 | -8.0324 | -43.1022 | 2025-12-14 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.4 |
| bf67aed8-6fa6-3c81-a5f2-dff79b1249ad | -8.0696 | -43.1452 | 2025-12-14 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 52.7 |
| 5fd57476-a622-3d4b-b97b-f72ece4561eb | -2.4768 | -45.4309 | 2025-12-14 02:10:00 | GOES-19 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 2885ad64-a140-35b4-87a6-291a6562a9a3 | -2.8875 | -44.9666 | 2025-12-14 02:10:00 | GOES-19 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 91af5f80-0932-3e3a-a6f4-04c5704f5f01 | -5.6797 | -39.2841 | 2025-12-14 02:10:00 | GOES-19 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 51.1 |
| 27890e6d-3f6f-30ef-b769-c7a75ae7220a | -5.6797 | -39.2841 | 2025-12-14 02:20:00 | GOES-19 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 47.0 |
| 33170d50-253e-3ee3-b633-6220ba7d570a | -8.0696 | -43.1452 | 2025-12-14 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 50.5 |
| d61e2d1d-8ba8-3b88-be8f-bb6aea13a1c5 | -2.8875 | -44.9666 | 2025-12-14 02:20:00 | GOES-19 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 77.0 |
| b73374bc-1930-3f60-8355-cca50793dc5d | -8.0327 | -43.0786 | 2025-12-14 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 57.3 |
| 1bcf9ddb-f33c-3c60-849a-2a36fe1321e6 | -5.68 | -39.259 | 2025-12-14 02:20:00 | GOES-19 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 51.7 |
| d50a859c-280c-3dc6-bda3-3d2b5ff78e49 | -8.0324 | -43.1022 | 2025-12-14 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.3 |
| fa2f220e-afe1-3b6f-b5c7-1370b0e35322 | -2.4768 | -45.4309 | 2025-12-14 02:20:00 | GOES-19 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 51.3 |


[Clique aqui para ver as próximas entradas](README5.md)
