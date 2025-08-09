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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 95eef115-f17f-30b5-b69d-e5b550e63673 | -8.9215 | -60.7297 | 2025-08-09 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 39.7 |
| b69a78b8-da8b-33fd-a0a5-43bbc1e84f53 | -8.9399 | -60.7481 | 2025-08-09 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 9417b443-bead-30f3-9b53-7b3f90759feb | -8.9401 | -60.7288 | 2025-08-09 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 39.7 |
| a04e584a-bdfa-322d-910d-848745071950 | -13.6144 | -49.0079 | 2025-08-09 06:40:00 | GOES-19 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 28d81ccf-bb95-358c-b931-d381bd8962d9 | -8.9399 | -60.7481 | 2025-08-09 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 85d258a0-bcca-3e98-9b70-d06f0148736d | -8.9213 | -60.7489 | 2025-08-09 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 49e68e8b-1977-38ab-9652-7f687fa91ac2 | -8.9215 | -60.7297 | 2025-08-09 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 8e8533cf-0d73-3448-9127-4c6788bb7944 | -8.9213 | -60.7489 | 2025-08-09 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 147dd664-d136-31d2-b0c6-6710befe9458 | -8.9399 | -60.7481 | 2025-08-09 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| bd91f734-4140-343c-abc1-c2c00e6a38b3 | -8.9401 | -60.7288 | 2025-08-09 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 206f4ae8-e713-3bb8-9ed9-2913bea067b0 | -13.6144 | -49.0079 | 2025-08-09 07:00:00 | GOES-19 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 3e1abdba-61b9-31d9-b8e8-d35f1a5e757f | -8.9399 | -60.7481 | 2025-08-09 07:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 9770197c-87f6-342b-b76e-c90806a70a54 | -7.0615 | -59.1779 | 2025-08-09 07:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| d6e01cf3-6c78-3ca1-8b0c-dee2aa0e74d5 | -8.9213 | -60.7489 | 2025-08-09 07:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 6d1ad6f1-be9d-3120-99b6-b11be37af11b | -8.91924 | -60.73112 | 2025-08-09 07:07:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 0e3f00ae-40e2-342c-ae68-a84d96fe7e2d | -9.93757 | -60.4873 | 2025-08-09 07:07:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| e8bf8af7-03f8-3ddd-8f9c-080029cc2890 | -8.92849 | -60.74764 | 2025-08-09 07:07:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| e2d8b4a5-b05e-3838-974b-adb29b70955f | -8.93052 | -60.73267 | 2025-08-09 07:07:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 742a825b-b027-31dc-9973-2f52bc0ead24 | -8.91721 | -60.74612 | 2025-08-09 07:07:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 992477ae-54cc-38a3-aecf-07b0a76a4f7c | -9.54604 | -62.71738 | 2025-08-09 07:07:00 | AQUA_M-M | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 45559275-56b1-3fca-b3ac-0c07ff027a9b | -13.6148 | -48.9859 | 2025-08-09 07:10:00 | GOES-19 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 65cb09ea-83cb-3d0e-8a20-fb18f8bda122 | -8.9213 | -60.7489 | 2025-08-09 07:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 73228172-bf4d-3b78-9bec-81c4988c7a3d | -8.9399 | -60.7481 | 2025-08-09 07:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 15ef1122-990d-37c7-ab56-8aae0baa848e | -8.9215 | -60.7297 | 2025-08-09 07:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 60902ad9-7fd3-3a96-930f-e8da260c61ef | -13.6144 | -49.0079 | 2025-08-09 07:10:00 | GOES-19 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 9e2b00ba-af0b-3a32-93ca-18b2f4391c36 | -19.8124 | -47.0634 | 2025-08-09 07:10:00 | GOES-19 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 88e28a83-66d5-3fdd-b11a-903204332cdc | -13.6144 | -49.0079 | 2025-08-09 07:20:00 | GOES-19 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 91.2 |
| d1e3bf0d-841f-348f-a975-b6d683dcfcc6 | -13.6148 | -48.9859 | 2025-08-09 07:20:00 | GOES-19 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 381e1f8a-a3b7-38bf-b702-80f7828bb7b6 | -13.6341 | -48.9831 | 2025-08-09 07:20:00 | GOES-19 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 0659d62f-5f79-3453-98a6-5812b335d31b | -8.9399 | -60.7481 | 2025-08-09 07:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 52b7e496-5ec9-3c12-8188-68562b3ddec9 | -8.9213 | -60.7489 | 2025-08-09 07:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 5458f92c-4350-3e42-b464-07923cdc5e75 | -13.6337 | -49.0051 | 2025-08-09 07:20:00 | GOES-19 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 856ffd5a-c195-326a-ae73-8e748f0e694e | -19.8124 | -47.0634 | 2025-08-09 07:30:00 | GOES-19 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 261ca337-a8a4-3dd9-9ca5-6cb73179f755 | -13.6144 | -49.0079 | 2025-08-09 07:30:00 | GOES-19 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 0dc3b94f-c243-3a7d-bd8b-e45f20d917ab | -7.0615 | -59.1779 | 2025-08-09 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 111.0 |
| 7e5aabbd-dbc8-3038-b877-b0df53a3207e | -19.8124 | -47.0634 | 2025-08-09 07:40:00 | GOES-19 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 55.3 |
| e47644d3-2cd6-30ab-87b7-0d54ff71ba29 | -7.0616 | -59.1586 | 2025-08-09 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 4e918b04-e638-3ded-869f-066354c86117 | -7.08 | -59.1771 | 2025-08-09 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 0f989f1e-66e3-33b3-806e-006ef9dc985c | -7.0801 | -59.1578 | 2025-08-09 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.3 |
| fba9a822-fa56-3bb1-8354-e20b8d57966c | -7.043 | -59.1787 | 2025-08-09 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| dd8c7cad-287a-37d8-a850-04758440545f | -7.08 | -59.1771 | 2025-08-09 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 44e7090d-2c68-39df-986a-125c90bfa20f | -13.6144 | -49.0079 | 2025-08-09 07:50:00 | GOES-19 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 8818f853-2445-3a6c-9244-7db8425d5419 | -19.8124 | -47.0634 | 2025-08-09 07:50:00 | GOES-19 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 9b2b01a8-0577-300a-868c-0d18546bac68 | -7.0616 | -59.1586 | 2025-08-09 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| f6f7bb30-080b-3e89-a3ab-a9f351d3d4d3 | -7.0615 | -59.1779 | 2025-08-09 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 110.0 |
| ab39ddff-edb5-3148-b23f-7a37cfc3b57f | -7.0801 | -59.1578 | 2025-08-09 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 4a930a00-4851-3207-9317-9339c849819a | -13.6148 | -48.9859 | 2025-08-09 08:00:00 | GOES-19 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 7ffe47d1-7fe6-3a83-aa19-27a84605f38c | -7.08 | -59.1771 | 2025-08-09 08:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| dc7b9b19-84aa-3c4b-8faf-d83887aec29c | -7.0615 | -59.1779 | 2025-08-09 08:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 8342dd75-33a4-3b53-a23e-bdba2e4aeb1b | -7.0616 | -59.1586 | 2025-08-09 08:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 97903b07-3859-33c9-bf03-93e7a886b062 | -13.6144 | -49.0079 | 2025-08-09 08:00:00 | GOES-19 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 6fdca2d9-3c20-34b0-915c-a0d00889954a | -7.0801 | -59.1578 | 2025-08-09 08:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 3fcaf248-86a5-378f-b823-070397709878 | -13.6144 | -49.0079 | 2025-08-09 08:20:00 | GOES-19 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 9434c8cc-8d58-337d-ba47-57120ebde53d | -19.8124 | -47.0634 | 2025-08-09 08:20:00 | GOES-19 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 48d6e53a-757f-34ae-a210-38dfef8df1bb | -6.5856 | -44.564 | 2025-08-09 08:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 6a6dbb39-6801-3e7f-8e5d-768624012327 | -7.0986 | -59.157 | 2025-08-09 08:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 19312f15-9f80-3f97-802a-57ba662ae6e6 | -7.0801 | -59.1578 | 2025-08-09 08:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 22b46a5f-28a3-335a-ae70-cb49e0ed2004 | -8.9399 | -60.7481 | 2025-08-09 08:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 9e23a37a-430b-3e66-bb15-c749f1b26453 | -8.9213 | -60.7489 | 2025-08-09 08:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 38.1 |
| ab2a83db-eafd-336f-b88c-a7f5a47012d1 | -7.043 | -59.1787 | 2025-08-09 08:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 1f3e8c69-6350-34eb-a0ce-3956ca9da153 | -7.0615 | -59.1779 | 2025-08-09 08:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.2 |
| c860c83b-075e-368c-82ba-eb4ba2924360 | -7.0801 | -59.1578 | 2025-08-09 08:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 5e4a5d10-0898-3820-83fc-4d46335288d7 | -13.6144 | -49.0079 | 2025-08-09 08:30:00 | GOES-19 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 5195b217-dd77-3025-a866-52efbdbab084 | -7.0616 | -59.1586 | 2025-08-09 08:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 47632688-94a9-317c-bdfa-085348982cc5 | -7.0616 | -59.1586 | 2025-08-09 08:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 25fec3b9-6ae7-35bc-b949-467941ec7ffe | -7.0801 | -59.1578 | 2025-08-09 08:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 120.5 |
| 3a28be73-b20e-3b28-84d3-73000aedb2b8 | -7.0615 | -59.1779 | 2025-08-09 08:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 228.6 |
| b20466a5-3990-377f-baf6-e6d8d5ea90dd | -7.08 | -59.1771 | 2025-08-09 08:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 156.9 |
| 3cc494db-31e9-312d-a1e2-60177cc64259 | -7.0614 | -59.1972 | 2025-08-09 08:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 17d5496e-3f92-3403-b0cc-9fa87802fd88 | -19.8124 | -47.0634 | 2025-08-09 08:50:00 | GOES-19 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 79f22c94-3fe1-36ce-86aa-9eab59b8fbc8 | -13.6144 | -49.0079 | 2025-08-09 08:50:00 | GOES-19 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 13beb995-f4db-3cbb-b7fc-5634189b725a | -7.043 | -59.1787 | 2025-08-09 08:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 7eb62baa-8a62-3a2c-a228-39e8aaa9721b | -8.9213 | -60.7489 | 2025-08-09 09:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 192902de-ee82-321c-b0a9-190240115996 | -13.6144 | -49.0079 | 2025-08-09 09:40:00 | GOES-19 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 1263b4b7-0dd4-3fe3-addf-ddeca9548967 | -14.1103 | -45.4077 | 2025-08-09 11:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 78f9fce1-e35c-3784-8ddb-762f077976b5 | -14.1103 | -45.4077 | 2025-08-09 11:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 206f5da4-5160-3690-8000-286681cdf99f | -14.66243 | -40.36612 | 2025-08-09 11:34:00 | TERRA_M-M | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 9d0925e2-bfd0-3215-9922-118d7c2f8521 | -4.9791 | -37.78142 | 2025-08-09 11:34:00 | TERRA_M-M | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 14.7 |
| a986cc95-9e79-3f0f-a46a-c68f8a447381 | -6.66235 | -37.43956 | 2025-08-09 11:34:00 | TERRA_M-M | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 4408dbe1-4e92-34a1-b629-d1e901562199 | -4.98906 | -37.78282 | 2025-08-09 11:34:00 | TERRA_M-M | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| cdd0ea06-57ce-3d74-8f01-2242840069dc | -5.68667 | -36.50453 | 2025-08-09 11:34:00 | TERRA_M-M | ANGICOS | RIO GRANDE DO NORTE | Brasil | 2400802 | 24 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 263dbd6f-902c-3243-80e2-4fe255c1fd38 | -6.13808 | -42.96336 | 2025-08-09 11:34:00 | TERRA_M-M | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 34.6 |
| 0f4918b3-3529-3c99-b27e-7c59289741f8 | -11.31804 | -39.44901 | 2025-08-09 11:34:00 | TERRA_M-M | VALENTE | BAHIA | Brasil | 2933000 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 5563b8c6-549d-34d8-ab0d-c733df633bf0 | -13.14593 | -42.54857 | 2025-08-09 11:34:00 | TERRA_M-M | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 31.1 |
| bb17ae6f-6dc2-304d-a52b-7972478fa5c5 | -13.82476 | -40.61017 | 2025-08-09 11:34:00 | TERRA_M-M | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 11.7 |
| de07da41-7d74-3f7c-8471-d5f935c229b0 | -13.65755 | -42.70632 | 2025-08-09 11:34:00 | TERRA_M-M | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 49.1 |
| a2b9682d-e35b-33d7-b5d0-2e4c2c0a4303 | -13.66195 | -42.69439 | 2025-08-09 11:34:00 | TERRA_M-M | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 34b9f5b2-84f0-3b29-884f-605808b11481 | -6.98778 | -43.85104 | 2025-08-09 11:34:00 | TERRA_M-M | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 588c49f9-372a-35f8-a5c8-e4622ac07b0d | -13.65864 | -42.71337 | 2025-08-09 11:34:00 | TERRA_M-M | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 30.1 |
| 1f87bf51-7ff5-3955-a3d3-f9e20207c4e9 | -7.28911 | -39.64512 | 2025-08-09 11:34:00 | TERRA_M-M | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 3a79afac-bae5-355b-b07e-78bfc7137a73 | -19.00576 | -40.55309 | 2025-08-09 11:36:00 | TERRA_M-M | SÃO GABRIEL DA PALHA | ESPÍRITO SANTO | Brasil | 3204708 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 28ef29d2-c498-3f72-ae19-fc3cc8263938 | -19.19343 | -42.04902 | 2025-08-09 11:36:00 | TERRA_M-M | ENGENHEIRO CALDAS | MINAS GERAIS | Brasil | 3123700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| ceaffc15-1024-3883-8d25-e7178c08fe57 | -15.15882 | -41.43411 | 2025-08-09 11:36:00 | TERRA_M-M | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| d171f9d3-2a92-38a7-92c4-1a857dbb7ca8 | -18.5901 | -44.66294 | 2025-08-09 11:36:00 | TERRA_M-M | MORRO DA GARÇA | MINAS GERAIS | Brasil | 3143609 | 31 | 33 | nan | nan | nan | Cerrado | 29.5 |
| c93c63b3-7569-3327-9fed-72c0d64a9d93 | -19.74473 | -42.0703 | 2025-08-09 11:36:00 | TERRA_M-M | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 38.2 |
| 94941868-9dce-3d2c-8c57-014e226ea321 | -18.58056 | -44.65501 | 2025-08-09 11:36:00 | TERRA_M-M | MORRO DA GARÇA | MINAS GERAIS | Brasil | 3143609 | 31 | 33 | nan | nan | nan | Cerrado | 26.4 |
| f3905ef7-6029-3005-8f31-dc22af9c4f85 | -14.1103 | -45.4077 | 2025-08-09 11:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 54437b6b-65fd-3b46-ae7b-134e92683aa0 | -14.1103 | -45.4077 | 2025-08-09 11:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 97cf68db-9662-3209-b4db-cf1d1f5e0007 | -14.1103 | -45.4077 | 2025-08-09 12:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 116.3 |
| d339fda5-38e0-31bc-9e7b-8ba0cbcad198 | -14.1103 | -45.4077 | 2025-08-09 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 102.3 |


[Clique aqui para ver as próximas entradas](README32.md)
