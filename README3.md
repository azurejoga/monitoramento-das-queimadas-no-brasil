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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d377326-4351-37a4-947f-6219efb803b0 | -9.3048 | -45.4581 | 2026-06-09 01:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 56.6 |
| d13dba37-fafb-3b4a-a9a6-a3e797d64161 | -10.6498 | -49.3834 | 2026-06-09 01:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 0a1318a8-a7c4-3cf9-b657-25ecec6dd208 | -11.5499 | -52.7867 | 2026-06-09 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 1fcc61b5-adbd-390c-818e-b74d79237e89 | -17.5961 | -46.6415 | 2026-06-09 01:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 12027665-310a-3e9d-905e-eb17a14aa4f8 | -5.8128 | -45.1026 | 2026-06-09 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 5c50f40f-e930-3a69-ab48-f3f034a8d642 | -9.2855 | -45.483 | 2026-06-09 01:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 835d847a-fedc-3aa6-9ac6-6623cfd645ad | -10.6498 | -49.3834 | 2026-06-09 01:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 2c43dfdb-dae9-3f13-b352-de210678390e | -9.2858 | -45.4602 | 2026-06-09 01:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 1199b188-dacd-34cb-8c68-1b0431bd596b | -5.8128 | -45.1026 | 2026-06-09 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 562e6853-80b1-3a2d-b635-f7be6996a0f3 | -17.5961 | -46.6415 | 2026-06-09 01:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 68.7 |
| e6dc997d-44dc-314c-9222-5f64711e4411 | -12.0498 | -49.7612 | 2026-06-09 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| ee01055b-d5f7-3366-af49-46c5122a2299 | -9.3048 | -45.4581 | 2026-06-09 01:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 975a7b09-493b-30be-9c13-d81b8b0b5744 | -9.3045 | -45.4809 | 2026-06-09 01:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 117.5 |
| c33ee6ee-2325-3f0f-94b5-3d88d6d4b0c2 | -11.5499 | -52.7867 | 2026-06-09 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| e3a38439-3de0-3645-81bd-bede7fbc251d | -7.1092 | -46.5065 | 2026-06-09 01:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| d17ff667-8b35-3fe0-b3f9-9552937bd634 | -17.5961 | -46.6415 | 2026-06-09 01:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 4eab44e2-c8cc-3173-a073-85ffc68aea2b | -9.3045 | -45.4809 | 2026-06-09 01:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 146.6 |
| df3ec1fe-a1b7-3f7f-b666-46f51d1b4d95 | -9.3048 | -45.4581 | 2026-06-09 01:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 89.5 |
| d79130af-beb3-3941-8444-2cf1f0e57b83 | -7.1092 | -46.5065 | 2026-06-09 01:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 7bf48c3e-3c4a-3441-86eb-7771a1387867 | -10.6498 | -49.3834 | 2026-06-09 01:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 2b7d6d39-db30-3754-94d1-eacefc2b5596 | -11.5499 | -52.7867 | 2026-06-09 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 87a5bcf8-5f02-351d-aaf9-7019807995b5 | -12.0498 | -49.7612 | 2026-06-09 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 0f3542b8-a4c4-3a3b-8a14-cb6f54766a34 | -5.7941 | -45.104 | 2026-06-09 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 7054f2e7-75d3-3a85-9ae8-b56bae1932a4 | -12.0689 | -49.7589 | 2026-06-09 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 6164ee4d-d2ca-38c4-9311-e79d648d8185 | -7.1092 | -46.5065 | 2026-06-09 02:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 2f1121e6-e303-3afe-aca5-4445b046de69 | -11.5499 | -52.7867 | 2026-06-09 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 9a3391d7-58eb-3081-8e91-e5ec354e27d3 | -5.7941 | -45.104 | 2026-06-09 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 607b86e0-bd30-33f2-92e9-4d50b17c4e71 | -9.3045 | -45.4809 | 2026-06-09 02:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 165.3 |
| 3b65a0c3-0dcd-3033-a90b-5ec714a49c4e | -10.6498 | -49.3834 | 2026-06-09 02:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| b2fb4a41-48ea-3403-8966-fa27a4223dcc | -9.3048 | -45.4581 | 2026-06-09 02:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 3351fbc4-04c6-355c-8b8e-4f0c0033669d | -9.3234 | -45.4787 | 2026-06-09 02:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 59.2 |
| d9915b68-16ac-3010-8bcd-6aa4069a75c4 | -10.6498 | -49.3834 | 2026-06-09 02:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 56f97fbb-72b9-3e00-99e7-d4ee4e6f599b | -9.3045 | -45.4809 | 2026-06-09 02:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 154.9 |
| 892e0a1f-4fe4-3b04-bd79-3da720877c18 | -9.3234 | -45.4787 | 2026-06-09 02:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 947bc2a8-3149-31b9-bef3-cc138848d66a | -12.0498 | -49.7612 | 2026-06-09 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 46.1 |
| d6026c14-1a56-3ded-a047-c5b3680f3aea | -7.1092 | -46.5065 | 2026-06-09 02:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 03dfb6dc-b765-3dea-8bee-fb04ce621d1a | -11.5499 | -52.7867 | 2026-06-09 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 46e24036-4ed7-34ed-96ae-27cb40201c85 | -9.3048 | -45.4581 | 2026-06-09 02:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 9daf78f3-1bfd-3e6e-b416-013227760e80 | -10.6498 | -49.3834 | 2026-06-09 02:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 08459e45-e81b-38e2-9c2e-a59b352fa369 | -12.0498 | -49.7612 | 2026-06-09 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 0d4839fb-ae86-356d-8c81-6f071e564682 | -9.3045 | -45.4809 | 2026-06-09 02:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 145.7 |
| 3d2b161e-bde2-3dba-85f3-8867b410bf71 | -7.1092 | -46.5065 | 2026-06-09 02:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 75b9531b-97a3-3486-ad2e-7433f25e426f | -11.5499 | -52.7867 | 2026-06-09 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 205ce0d7-f8da-3cea-8a4d-33fe753d1587 | -9.3048 | -45.4581 | 2026-06-09 02:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 79e6f0d2-2853-362d-aa23-c7dd31367951 | -9.3234 | -45.4787 | 2026-06-09 02:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 5b408bb8-6621-3407-b47c-e82638a6cff3 | -11.5499 | -52.7867 | 2026-06-09 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 5dc50e6d-4727-37f6-b7af-000bc3c74c7b | -10.6498 | -49.3834 | 2026-06-09 02:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 44822fde-5c49-37cc-a45d-5cc9a71be230 | -9.3045 | -45.4809 | 2026-06-09 02:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 149.0 |
| d1506871-fec3-3d85-b0c8-8d7620116b9a | -9.3048 | -45.4581 | 2026-06-09 02:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 6a098a38-9c2b-3f6a-8bd1-d78eb6a44aeb | -7.1092 | -46.5065 | 2026-06-09 02:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| fc0ebdfb-b6c1-3515-a328-624ae000bd25 | -12.0498 | -49.7612 | 2026-06-09 02:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| b05749a5-31a0-3095-a5d6-ce0e987dbc85 | -9.3234 | -45.4787 | 2026-06-09 02:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 76.5 |
| fb654c6b-30ca-3d17-b56c-e08a13208d37 | -9.3045 | -45.4809 | 2026-06-09 02:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 3236f85f-b6f6-3572-978b-a0cc59551e38 | -7.1092 | -46.5065 | 2026-06-09 02:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 9d18e507-52a3-3a7b-8886-aa6715117218 | -10.6498 | -49.3834 | 2026-06-09 02:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| b89fac45-bda9-3693-bee6-192320cacaa5 | -9.3234 | -45.4787 | 2026-06-09 02:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 5754626d-05a9-3998-b24a-8f2dee6dad4f | -9.3048 | -45.4581 | 2026-06-09 02:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 48.3 |
| d6bd2148-ba76-378b-a660-f7f3793ce240 | -11.5499 | -52.7867 | 2026-06-09 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| e5d7f2de-1fe9-3673-9d82-6f91adf3e292 | -9.3234 | -45.4787 | 2026-06-09 02:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 73.3 |
| f47f5a94-f80e-3cca-be97-7ce45e69ae37 | -10.6498 | -49.3834 | 2026-06-09 02:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 1369c3d9-760d-33a9-b839-47741a43c430 | -11.5499 | -52.7867 | 2026-06-09 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 60844151-492e-393b-81a7-1a095fbaaa1e | -9.3045 | -45.4809 | 2026-06-09 02:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 50a03a86-07ba-3402-8d88-0e35bb14965c | -12.0498 | -49.7612 | 2026-06-09 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 49.7 |
| bdac3187-f92e-3c00-b1c2-bf399aecc894 | -11.5499 | -52.7867 | 2026-06-09 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| fb6ba2fa-56d0-3717-83b9-d8e0a42bdadd | -9.3045 | -45.4809 | 2026-06-09 03:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 44f14b3d-0e68-3dfd-9775-fbe67fb2c4b6 | -9.3234 | -45.4787 | 2026-06-09 03:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 08b7f140-d99e-3e30-9683-ff7c904f1e9e | -9.3045 | -45.4809 | 2026-06-09 03:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 28113cb6-bedb-3936-8e8f-73c75a7600a7 | -11.5499 | -52.7867 | 2026-06-09 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 6a4ca31c-d1c5-3cd7-971f-abc5d9bc33dd | -9.3045 | -45.4809 | 2026-06-09 03:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 46.8 |
| d91881b7-3b41-366d-baaa-4892560db31f | -7.1092 | -46.5065 | 2026-06-09 03:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 1ecec07c-e241-3ed4-b4a5-ac2c6def3da8 | -10.6498 | -49.3834 | 2026-06-09 03:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 50.3 |
| d7e0edc7-248d-3e69-a560-417ae206bee8 | -11.5499 | -52.7867 | 2026-06-09 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 46.2 |
| a491269e-c386-34d6-ad79-a33c896d7bdf | -5.28263 | -43.9659 | 2026-06-09 03:25:00 | NOAA-20 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1106eb65-c702-3070-94d5-672e1de420c3 | -5.04609 | -43.26647 | 2026-06-09 03:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6ca4f89f-7be0-33c1-8ac3-efd0f9d3a4da | -5.28061 | -43.95957 | 2026-06-09 03:25:00 | NOAA-20 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 773ff1a9-aea3-3367-9b9f-b238a7fe5184 | -5.27555 | -43.96464 | 2026-06-09 03:25:00 | NOAA-20 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1ae33cb5-59ce-33dd-beff-b58f94997ed7 | -5.60943 | -37.53037 | 2026-06-09 03:25:00 | NOAA-20 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 9eed1b85-e25f-3d2c-beb6-7d9302c915f9 | -5.2793 | -43.9666 | 2026-06-09 03:25:00 | NOAA-20 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c6b4963e-ae26-3fc1-b115-b9fab1d4c98e | -5.83779 | -43.48652 | 2026-06-09 03:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9d3dde50-3f1f-3185-a141-72625cce28aa | -5.51823 | -37.48656 | 2026-06-09 03:25:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d25e0d30-ae27-3f09-89d0-1c118b9796eb | -5.03925 | -43.26531 | 2026-06-09 03:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0704ac8b-1872-3bea-8a56-901e8b283cea | -5.8366 | -43.49296 | 2026-06-09 03:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 94ef4fa5-3929-34b4-b18b-25809b0270e5 | -13.25946 | -44.39539 | 2026-06-09 03:28:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a2d0c049-1eee-3ac2-aa3c-35fb291cf0f4 | -11.27606 | -44.5312 | 2026-06-09 03:28:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0e764a1-efcd-3794-a648-3234a5390b50 | -13.96341 | -46.18845 | 2026-06-09 03:28:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ebd510a-c390-35c1-bdb3-f26d373d1fe4 | -12.85386 | -44.36871 | 2026-06-09 03:28:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b397d79f-b7b8-3885-8472-41c441b0b991 | -13.25208 | -44.3988 | 2026-06-09 03:28:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6d8ef4b1-2c22-39f7-bb6c-ab7c1e9cc5b1 | -11.26604 | -44.52914 | 2026-06-09 03:28:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a552c929-459d-3f8f-80ec-913c4867b98e | -11.02866 | -44.31801 | 2026-06-09 03:28:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e9004a46-a5a1-3dc1-87e1-2d7d11cb2ad7 | -12.48083 | -46.27648 | 2026-06-09 03:28:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a30cb80e-5d0d-3ab5-b47e-67fd9faae8d8 | -12.84632 | -44.37276 | 2026-06-09 03:28:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6a769f50-1b9d-3db5-9415-02b4ff168472 | -13.36558 | -43.20527 | 2026-06-09 03:28:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a61904fc-767c-3391-bad8-575fc400d8e2 | -13.35967 | -43.20396 | 2026-06-09 03:28:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9aaf70ed-92b3-3635-a2c1-37bcfaa145d3 | -13.36199 | -43.20813 | 2026-06-09 03:28:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 199dc8db-e2ba-3213-a4d7-3fd36cfdc01d | -11.26945 | -44.52962 | 2026-06-09 03:28:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 71c9fd0e-4623-3d49-b64d-10d0ea253bf6 | -12.84926 | -44.39074 | 2026-06-09 03:28:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e883feaf-8009-3aa4-881c-354346f9aace | -13.95656 | -46.18639 | 2026-06-09 03:28:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17ce78d6-ad1c-34f4-86c5-6b93646b6bc6 | -12.85271 | -44.3742 | 2026-06-09 03:28:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 25b57972-598c-3668-988d-15b6d21a2fe2 | -13.25316 | -44.3937 | 2026-06-09 03:28:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c29b13c4-1b87-339c-b48e-96693f5867c1 | -12.47902 | -46.27423 | 2026-06-09 03:28:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README4.md)
