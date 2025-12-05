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
| e492f915-4677-34b8-9ae2-aad13f63d9a0 | -5.1938 | -43.0977 | 2025-12-05 02:30:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 6a085399-4582-320e-8039-dfd6d6530259 | -5.194 | -43.0743 | 2025-12-05 02:30:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 9002ad1f-5ae2-3a23-a20f-1320089fb37f | -6.019 | -41.1521 | 2025-12-05 02:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 65.0 |
| b4c8cdd2-0a9d-3e7a-ba05-92ed964aafe9 | -6.0192 | -41.1278 | 2025-12-05 02:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 57.7 |
| c36a4edd-2921-37b9-8b4f-10a4fa759e6d | -6.0004 | -41.1295 | 2025-12-05 02:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 61.7 |
| d3bb5a51-d632-3185-9dd0-6a34dd9b830f | -5.1751 | -43.099 | 2025-12-05 02:30:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 8ce37df3-f33f-3295-97a1-e24f84e860a7 | -5.1753 | -43.0756 | 2025-12-05 02:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 767dd7bf-e25c-311d-8c48-24b25c4b6482 | -2.9049 | -45.2368 | 2025-12-05 02:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 195.6 |
| b830c5a9-3100-393d-a162-91cea9dbb02a | -5.1751 | -43.099 | 2025-12-05 02:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 094c5de0-996c-3714-965b-91edcf69cf96 | -2.9048 | -45.2594 | 2025-12-05 02:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 78.3 |
| bab52470-d707-34ab-a9b0-894b0b549b2f | -2.905 | -45.2143 | 2025-12-05 02:40:00 | GOES-19 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 9a0ca439-038b-38d9-b505-2bd261b332d8 | -2.8863 | -45.2375 | 2025-12-05 02:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 801a8e8d-33a8-3958-8c61-1f299a2e461c | -9.26221 | -35.61214 | 2025-12-05 02:49:00 | NPP-375D | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 039c4900-3542-3bbe-9e6e-3eb8ef25b115 | -9.26076 | -35.61935 | 2025-12-05 02:49:00 | NPP-375D | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| f4a6afc8-525e-393a-ae95-bff25bcca5bd | -9.25515 | -35.61041 | 2025-12-05 02:49:00 | NPP-375D | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 61437ed4-2097-36d3-ba78-aa1e965f1c84 | -2.9049 | -45.2368 | 2025-12-05 02:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 169.1 |
| 741efe87-f5d0-3b28-8e89-2c1c67979e4b | -2.9048 | -45.2594 | 2025-12-05 02:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 75.4 |
| c376afa3-9939-33e8-80ca-213e6047af75 | -5.194 | -43.0743 | 2025-12-05 02:50:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| cb5ff421-3c18-3ca1-834d-a14f62102bb3 | -5.1751 | -43.099 | 2025-12-05 02:50:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 7652dd4b-a58e-310d-ab22-38908dd8877d | -5.1753 | -43.0756 | 2025-12-05 02:50:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| b23c22bc-c028-3508-926a-7cf72bd78eb9 | -2.9049 | -45.2368 | 2025-12-05 03:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 6ecf7012-e8a1-3efb-8fda-8f2658b02ddd | -5.194 | -43.0743 | 2025-12-05 03:00:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 2305f18c-1ba8-3272-ac70-5c87fad7d896 | -5.1753 | -43.0756 | 2025-12-05 03:00:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 8b33fba8-b703-32ad-95a3-5ef5e9cb0371 | -5.1753 | -43.0756 | 2025-12-05 03:10:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| f5901daa-f3db-3dfa-acb4-b6cdd01023f5 | -2.9049 | -45.2368 | 2025-12-05 03:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 1561f206-6687-3bc9-b377-634c1b1bbe26 | -5.194 | -43.0743 | 2025-12-05 03:10:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 1a5590d8-ec44-3fe4-84cf-aece32a465d7 | -5.99746 | -41.1453 | 2025-12-05 03:10:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 43dae2c6-e073-3ffa-be71-fe615e02b033 | -4.61158 | -38.68583 | 2025-12-05 03:10:00 | NOAA-20 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a5800159-3045-3749-a71a-b01393f0edb4 | -6.00325 | -41.15378 | 2025-12-05 03:10:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| c2a819d0-78c3-36a0-9d04-66b365a82b87 | -6.00649 | -41.15546 | 2025-12-05 03:10:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 988312a5-45ea-3572-906b-22509de77196 | -3.42182 | -39.26987 | 2025-12-05 03:10:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 11d4fbde-ec91-3e4e-8ec8-92ca9e041f34 | -4.15761 | -39.25475 | 2025-12-05 03:10:00 | NOAA-20 | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c6980a98-f4da-39dd-9ae8-0aa55241b874 | -5.06188 | -40.47794 | 2025-12-05 03:10:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| ab6027ae-e5b8-3dd6-8db0-1951be786524 | -6.00785 | -41.14828 | 2025-12-05 03:10:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 7c5a176a-0839-3517-a078-1b3dd54755ef | -5.06066 | -40.47952 | 2025-12-05 03:10:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e93ee68c-b9e2-351f-a0e4-bf4f323ddd4d | -6.00067 | -41.14735 | 2025-12-05 03:10:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 16.8 |
| dffdb744-f57a-37de-96dd-d0148713e861 | -4.16416 | -39.25594 | 2025-12-05 03:10:00 | NOAA-20 | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2999b280-b95e-3822-a60b-6da5ca124c31 | -5.99611 | -41.15265 | 2025-12-05 03:10:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| c02d653d-fcce-37fc-b959-5ab18d039277 | -5.99929 | -41.1546 | 2025-12-05 03:10:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 7c3e48e7-f6e0-361e-871f-bad4f89c8561 | -3.42285 | -39.26396 | 2025-12-05 03:10:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 02ce16d6-ef9a-3d93-990e-179f614c9051 | -6.00457 | -41.14661 | 2025-12-05 03:10:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| c8dcc2a2-aff6-3d5e-a998-e3ab9299a88c | -5.99359 | -41.1459 | 2025-12-05 03:10:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 74c5b17e-b37e-3fe9-9a1e-356e456f9b7f | -6.01049 | -41.1544 | 2025-12-05 03:10:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 539d7b19-bb20-37f6-9d15-e13e92be6dca | -4.6053 | -38.68466 | 2025-12-05 03:10:00 | NOAA-20 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| ea779066-0289-36d7-b033-b8dc22abd32d | -9.25615 | -35.61311 | 2025-12-05 03:12:00 | NOAA-20 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 196ad240-b724-303c-b0aa-f89a5af0b605 | -9.3263 | -36.96355 | 2025-12-05 03:12:00 | NOAA-20 | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f747b276-a0c0-38ee-806e-9c0d94080975 | -7.35874 | -39.00562 | 2025-12-05 03:12:00 | NOAA-20 | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4e3fc213-1350-31bf-8915-3d1eab65ed40 | -9.2609 | -35.61409 | 2025-12-05 03:12:00 | NOAA-20 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4e2a9692-db5d-3288-a699-ac4315510bbb | -9.26565 | -35.61507 | 2025-12-05 03:12:00 | NOAA-20 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| aa70a997-002d-3f0e-b294-5e0a8e5ca330 | -7.35966 | -39.00074 | 2025-12-05 03:12:00 | NOAA-20 | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d8e89cb0-9568-343f-8c4f-f2a25a6f7248 | -5.1753 | -43.0756 | 2025-12-05 03:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 7adc7d19-ae71-3dc1-b3d9-e2f70527ff9e | -5.1751 | -43.099 | 2025-12-05 03:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| ce27dc95-f78c-3bed-84c1-60266bd7a1cb | -5.194 | -43.0743 | 2025-12-05 03:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| fc93d15b-d3c0-3bc2-8718-c7a7a1e5f580 | -6.0192 | -41.1278 | 2025-12-05 03:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 79.8 |
| 7d8b13e6-9c7b-3aeb-94d5-801a4162def2 | -6.019 | -41.1521 | 2025-12-05 03:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 81.7 |
| 185231fd-5e5d-3548-b88c-e3a488e7c622 | -6.0004 | -41.1295 | 2025-12-05 03:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 98.2 |
| 5e28a555-a97b-308a-88d7-00a6444322cb | -5.1753 | -43.0756 | 2025-12-05 03:30:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 8bd6c21e-db6a-371c-a23b-d5ed502b6907 | -6.0002 | -41.1538 | 2025-12-05 03:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 95.3 |
| c5aa2768-038f-3e23-bba4-9746b24af592 | -6.019 | -41.1521 | 2025-12-05 03:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 59.0 |
| b505e143-36c8-3412-95c1-d0a9a71a16d8 | -6.0002 | -41.1538 | 2025-12-05 03:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 85.9 |
| e4a75542-d5c5-3a00-bb2c-437bd76c9e55 | -5.1753 | -43.0756 | 2025-12-05 03:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 4e77656c-1d70-3d22-b08f-4cdd9ea375b7 | -6.0004 | -41.1295 | 2025-12-05 03:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 96.3 |
| 3608a962-4b20-30fe-a390-21343e4742f2 | -6.0192 | -41.1278 | 2025-12-05 03:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 60.2 |
| a467db1c-43ca-3371-912d-f81bee08edf0 | -9.9711 | -36.1719 | 2025-12-05 03:50:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 136.2 |
| b172eb2a-2c32-3af5-914d-ac2afff4358f | -9.9716 | -36.1448 | 2025-12-05 03:50:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 78.4 |
| 568823d3-b9bf-3b13-a074-77ac420b0703 | -6.0004 | -41.1295 | 2025-12-05 03:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 59.5 |
| 07e3dc22-c18a-3db6-8664-d85be0a66836 | -5.1758 | -43.08659 | 2025-12-05 03:59:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0d9fa9cf-2ef1-38fc-9806-b1bcd1772703 | -2.6111 | -47.01243 | 2025-12-05 03:59:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff990038-ca75-39ac-8746-ed8fa081eab5 | -5.17649 | -43.08228 | 2025-12-05 03:59:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 28ceb97d-769c-3f31-9198-8b9148ffa574 | -2.49495 | -47.49582 | 2025-12-05 03:59:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9314227-71b5-3cbd-9c47-f63c4da5b06a | -5.87335 | -35.381 | 2025-12-05 03:59:00 | NOAA-21 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 3.6 |
| d05f8cc9-1267-38c3-90c4-bb250d3932f0 | -5.86858 | -35.37791 | 2025-12-05 03:59:00 | NOAA-21 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 6001526c-8d4a-3306-b408-053947c283f3 | -5.47013 | -39.5209 | 2025-12-05 03:59:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3d53cd27-5494-33e5-a6f7-0851b4096a40 | -3.34852 | -42.15573 | 2025-12-05 03:59:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 99603c24-bb46-3004-b881-bdc35164fccf | -1.23928 | -46.7391 | 2025-12-05 03:59:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 639f6390-73d4-3d89-b272-3aa719f0555e | -4.91629 | -43.80167 | 2025-12-05 03:59:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 198bc24b-2aae-3b15-b063-4cc26eb4bb06 | -1.23436 | -46.7383 | 2025-12-05 03:59:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c58c7092-93e4-320e-b4e4-e3461d58c8f0 | -2.90638 | -45.23385 | 2025-12-05 03:59:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4609095a-0c40-3114-aeb4-a63743493fe2 | -3.51155 | -44.51859 | 2025-12-05 03:59:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a4718f0f-548b-3ba6-82d8-25256465981b | -5.22227 | -39.25549 | 2025-12-05 03:59:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9cd43841-513a-32aa-9d29-8bfa80cb3ed2 | -2.9027 | -45.2407 | 2025-12-05 03:59:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e1eeffa6-c345-3ba6-8014-6a1ef359c289 | -5.17718 | -43.07798 | 2025-12-05 03:59:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 231fa464-8d57-3e45-ab61-85299a9fc024 | -5.30386 | -40.70536 | 2025-12-05 03:59:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5753bde4-4507-33e6-b602-f433feeb1042 | -3.48116 | -43.5831 | 2025-12-05 03:59:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7d20a70-d24d-39c2-a251-7b1099f6df90 | -3.51095 | -44.52225 | 2025-12-05 03:59:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9358e703-d956-39c9-bd8f-116d8c35e720 | -3.66254 | -41.12936 | 2025-12-05 03:59:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b3b9d762-91fe-366a-aa40-0a62636a59ab | -3.66311 | -41.1257 | 2025-12-05 03:59:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3202a0b1-a4c2-373b-8c81-b65e3d913e12 | -1.46205 | -46.72664 | 2025-12-05 03:59:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6eb13553-bc4d-395b-924e-d33bca2aaf38 | -4.73671 | -44.43218 | 2025-12-05 03:59:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 44cd0793-de08-3259-bdef-acc8148a05bc | -5.06506 | -40.4735 | 2025-12-05 03:59:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 9e9beb8f-56b0-383b-b3ed-d3fba1e7d5a4 | -2.95248 | -40.25563 | 2025-12-05 03:59:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 93706dc6-7b45-39d7-b007-4c791475393f | -3.67043 | -44.82418 | 2025-12-05 03:59:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c328ba48-01ca-3cc2-a865-c179d3dd344e | -4.1818 | -41.44263 | 2025-12-05 03:59:00 | NOAA-21 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ff8cf9e5-f46d-3d5a-952e-ebdfb4dcabc2 | -4.73727 | -44.42875 | 2025-12-05 03:59:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 27b47b79-91c9-3234-8b04-4d456f35ff53 | -5.47067 | -39.51745 | 2025-12-05 03:59:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e1ac07cd-a290-307c-8217-c55ef4692a18 | -5.02049 | -41.00965 | 2025-12-05 03:59:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0bc746bc-ab32-37c5-bf25-87421263c0a6 | -3.50806 | -44.51429 | 2025-12-05 03:59:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ccb21051-3d3a-3c0d-a0be-9e5b39ede83b | -5.89619 | -39.25129 | 2025-12-05 03:59:00 | NOAA-21 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9ff30684-79a1-3d32-afae-de2157933899 | -4.16492 | -39.25176 | 2025-12-05 03:59:00 | NOAA-21 | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 934603e7-2523-396c-b786-ad55b6982d6f | -2.90338 | -45.23659 | 2025-12-05 03:59:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README5.md)
