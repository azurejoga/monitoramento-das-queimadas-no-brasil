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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb755aee-9396-320d-90bd-68239bfaf2a7 | -0.05744 | -51.65185 | 2026-01-13 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2fe6f480-b77a-376d-b4c4-b573aaceab2e | -0.04694 | -51.65853 | 2026-01-13 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5ffa24a-acb3-3758-90df-7183bed6f8b4 | 0.62158 | -50.77388 | 2026-01-13 05:10:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 770b7c35-f4c9-368d-85a2-28b5f95be462 | -1.95179 | -53.46924 | 2026-01-13 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ab0ebe0-4d6a-305f-95d6-784a91064c53 | -1.92771 | -53.46711 | 2026-01-13 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dd146b96-6715-38dd-a413-9cf636e29e63 | -2.45777 | -48.2295 | 2026-01-13 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37961aa9-46f0-362c-9c95-a74737e4df0f | -0.1071 | -51.43232 | 2026-01-13 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d0eddd9-4d86-3b7a-a129-535be94c4144 | -1.92413 | -53.46655 | 2026-01-13 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c16fa6e-51ea-345d-bf9c-6887b9055a8d | -2.87747 | -45.22287 | 2026-01-13 05:10:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f37bf20-89cb-390b-bcc2-0b4132cc9b0a | -3.48997 | -54.78689 | 2026-01-13 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| caf84dce-ea0d-3acd-8a70-afa24ec27995 | -1.854 | -54.02849 | 2026-01-13 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c1e08485-f759-35eb-a24f-fb38146c9b14 | -2.87672 | -45.22781 | 2026-01-13 05:10:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8b86b45c-201f-3e06-a423-2ba213f61b6f | -1.92349 | -53.47064 | 2026-01-13 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f507cef6-421b-3b81-96d6-98fc80fa0b37 | -11.23776 | -54.00958 | 2026-01-13 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9af53740-6248-3e83-960d-ae3b7e188a95 | -11.17102 | -54.14706 | 2026-01-13 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 690b3dd3-7daa-3ccb-8bef-8e2d293594e5 | -10.35723 | -48.91293 | 2026-01-13 05:12:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a642836b-1304-3a47-a9bb-1b35ea530988 | -10.36266 | -48.91377 | 2026-01-13 05:12:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa9b8f99-a7f0-3edf-94f0-660cd7cff0eb | -11.1704 | -54.1405 | 2026-01-13 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf49990a-8b14-3e12-bd32-3b742311782f | -11.16969 | -54.14538 | 2026-01-13 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a926a7f-205b-32c9-b787-d19b5e45c23c | -11.1717 | -54.14216 | 2026-01-13 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 745ce19b-aa37-3cee-a8df-1ee466188393 | -10.35852 | -48.91686 | 2026-01-13 05:12:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc11155d-3e1c-392b-8cbc-00606afed8eb | -10.36219 | -48.91738 | 2026-01-13 05:12:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db7d16c5-2380-366d-9a03-973a23eaab7e | -11.17745 | -54.14641 | 2026-01-13 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| baa70c35-2a89-3a54-8b43-b56fe775a088 | -11.1749 | -54.14757 | 2026-01-13 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73d2e657-bfbc-34fa-8c91-3acb40e18efa | -10.35896 | -48.91324 | 2026-01-13 05:12:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0fd9899c-5dfb-3b15-9e46-ab515b3f234a | -11.85373 | -57.36545 | 2026-01-13 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce7f83d8-49e3-3027-9a45-854738b63144 | -16.44441 | -58.16235 | 2026-01-13 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 53043a1b-85e0-38b6-b242-177429ed5eed | -16.10175 | -56.75768 | 2026-01-13 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 82e975db-bac7-3711-9631-fa5095e868c6 | -11.86382 | -57.36703 | 2026-01-13 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00d52c7b-813d-3db7-8089-49b08eb4cb76 | -18.81341 | -51.61383 | 2026-01-13 05:14:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e2416b2-7122-3e58-9ea6-8713c0ba07d2 | -16.21673 | -58.16216 | 2026-01-13 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 895ee1d6-62cd-3670-98dd-e856ba672c47 | -11.85598 | -57.37325 | 2026-01-13 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 91e9bef3-92de-3c32-873d-3b70f566a18f | -11.86045 | -57.3665 | 2026-01-13 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6eb2e944-797c-347e-aa46-b5d71f34208c | -18.81815 | -51.61782 | 2026-01-13 05:14:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 014dd04a-e67b-386e-b39b-2e431b0c7f86 | -11.85317 | -57.36909 | 2026-01-13 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b865d709-3c8e-3e73-a6b7-82b78428fc02 | -11.8599 | -57.37015 | 2026-01-13 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20928637-5527-3300-ad19-b46fc533747f | -11.84981 | -57.36856 | 2026-01-13 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3056e9a8-eb8d-3b44-9e6d-97c6cac2eedf | -11.86326 | -57.37067 | 2026-01-13 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 573ba2d1-febd-3530-8270-f01a5e250e0c | -16.44553 | -58.16225 | 2026-01-13 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 88e27ae0-f8eb-349a-9fa5-28c57874808a | -18.81849 | -51.61464 | 2026-01-13 05:14:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8fcb8842-201d-3e05-9d2a-571763964359 | -11.29614 | -54.88468 | 2026-01-13 05:14:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e2453970-a738-397f-aadd-53c7fae7fc7e | -13.38042 | -53.56394 | 2026-01-13 05:14:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e36dc3c-cb10-3471-9e38-52d60e9c36cd | -15.53459 | -58.80619 | 2026-01-13 05:14:00 | NOAA-21 | FIGUEIRÓPOLIS D'OESTE | MATO GROSSO | Brasil | 5103809 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d11c9a16-98c3-3f78-b15c-1107d783707c | -15.9707 | -58.23835 | 2026-01-13 05:14:00 | NOAA-21 | GLÓRIA D'OESTE | MATO GROSSO | Brasil | 5103957 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f96187e9-4f97-37dd-929d-1be7f3fe9cfa | -21.09464 | -54.17176 | 2026-01-13 05:16:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 280e4cb0-ba58-3dc8-926f-87d9892360df | -5.0992 | -43.2211 | 2026-01-13 05:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 9bed528a-5e0c-3dd4-9b88-562bd551849c | -5.099 | -43.2444 | 2026-01-13 05:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 438bcf4f-36c1-3962-86c7-6d3d314dd293 | -5.099 | -43.2444 | 2026-01-13 05:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| d62aef5c-22ee-314c-bb68-e5ef2e6cdab2 | -5.0992 | -43.2211 | 2026-01-13 05:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 4fc65949-8551-30a3-86c9-8feb7b329a9c | 4.22455 | -61.0344 | 2026-01-13 05:37:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3983c9c9-1fd3-3169-bc8d-58235ee7df09 | 2.55356 | -60.36246 | 2026-01-13 05:37:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e6446985-3dfe-3f96-a7c0-deaf410eada9 | -5.099 | -43.2444 | 2026-01-13 05:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 2ee99245-49a2-3090-8b14-e3b496285f81 | -5.0992 | -43.2211 | 2026-01-13 05:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 95a82e44-6622-380d-8d6c-aa598827da50 | -1.61399 | -54.14344 | 2026-01-13 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ddf2f0c3-c529-3e38-9129-b0ab44c5652a | -1.28797 | -53.68806 | 2026-01-13 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 372b0847-2bbb-3bc5-b542-33c0c8978450 | -1.61358 | -54.14345 | 2026-01-13 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3e8025a7-85e4-3caa-812b-d9e541d0a1e3 | -1.29324 | -53.68925 | 2026-01-13 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4730399-81d7-37c4-88c5-b4914b57d7d8 | -1.8507 | -54.02732 | 2026-01-13 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6dcf4c2d-d0a7-380f-aad2-ea9b38bbe514 | -1.61408 | -54.14034 | 2026-01-13 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 86445ba1-6171-3a8a-92eb-1a6c92dc18b4 | -1.29376 | -53.68587 | 2026-01-13 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a91ba694-e664-3b8f-8d44-1ed90b2ccb8b | -1.61446 | -54.14032 | 2026-01-13 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 325e70e6-cfe2-35a9-aa31-aad1d11a0b8c | -1.85594 | -54.0282 | 2026-01-13 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea9a5cd6-c762-3a7c-bfe6-15e4b1d5a26a | -0.08953 | -51.2802 | 2026-01-13 05:40:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9082f43f-c317-3a50-a570-11a504156fbc | -5.0992 | -43.2211 | 2026-01-13 05:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 30ac1ff2-9bd1-392c-b237-73a04c478d12 | -5.099 | -43.2444 | 2026-01-13 05:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 693604ba-6334-388f-9484-b81986a5d382 | -5.0992 | -43.2211 | 2026-01-13 06:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| e241b1e2-9037-33fe-b12b-362d42d1ca5b | 4.38581 | -60.6664 | 2026-01-13 06:01:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 824ac1c4-4839-3187-9896-2baf8301dcc2 | 3.07762 | -60.12552 | 2026-01-13 06:01:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70069673-446c-3ae6-a4ce-a91427466447 | 3.08819 | -60.11592 | 2026-01-13 06:01:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69299064-e550-302b-9b6c-54320bafa078 | 3.08163 | -60.11915 | 2026-01-13 06:01:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53f03fdb-cad8-3552-b3d2-43b7b6a2277a | 3.07931 | -60.1231 | 2026-01-13 06:01:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 59360bda-8051-305d-9e6a-5ecd9c9b8476 | 3.06784 | -60.18904 | 2026-01-13 06:01:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b442751b-07ba-3da3-87d6-060ff434c9dc | 3.06385 | -60.19535 | 2026-01-13 06:01:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fdef05e3-d836-30a9-b294-c82ba3290820 | 3.06295 | -60.18985 | 2026-01-13 06:01:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3697081b-8ea1-334d-8071-1b107d02e0d5 | 4.3866 | -60.67106 | 2026-01-13 06:01:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8bfb06ae-56d6-34ee-aea4-9f822c1b6b25 | -5.0992 | -43.2211 | 2026-01-13 06:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 0c2a4ad9-bb87-3600-9e96-2436e37296fe | -5.0992 | -43.2211 | 2026-01-13 06:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 37c242bd-efc8-301b-80dd-1ee7eae3360c | -4.42029 | -43.09569 | 2026-01-13 06:24:00 | AQUA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 43e8ba69-e030-35d2-8a9c-1aded7167097 | -5.1083 | -43.21594 | 2026-01-13 06:24:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 44b482fb-b7f0-3a56-b553-b1ae353a8da7 | -5.09467 | -43.21446 | 2026-01-13 06:24:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| b68b00bd-2084-31e8-9f49-7fbf0b130254 | -5.10007 | -43.20991 | 2026-01-13 06:24:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 52.4 |
| c7cd6dec-4cd9-33f4-acdc-b7d003f22650 | -3.29439 | -42.52992 | 2026-01-13 06:24:00 | AQUA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| d62fd6b2-d9ee-320d-9333-10698e9ecade | -3.30358 | -42.52406 | 2026-01-13 06:24:00 | AQUA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| e4be4126-6a9b-3734-99e4-82585fd55197 | -5.09167 | -43.23693 | 2026-01-13 06:24:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 34.4 |
| e1ae162b-849b-3138-b6ad-b30a6e02f992 | -5.09687 | -43.23244 | 2026-01-13 06:24:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| e0f39f0c-5046-3eea-9a7e-c85aa0540396 | -10.3607 | -48.90972 | 2026-01-13 06:26:00 | AQUA_M-M | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 15318744-99e3-3ab4-baf7-ef7ec0dd2b71 | -10.35117 | -48.90836 | 2026-01-13 06:26:00 | AQUA_M-M | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 89a67069-e1ca-3496-b244-3fee161997df | -10.35918 | -48.92034 | 2026-01-13 06:26:00 | AQUA_M-M | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 50356087-acf8-3949-94ba-fd6da748917f | -20.84349 | -51.73928 | 2026-01-13 06:29:00 | AQUA_M-M | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 57193a28-5921-3de3-8a27-963dee7581d0 | -5.0992 | -43.2211 | 2026-01-13 06:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 7c3be9d2-cf72-3775-a9ac-f7ef77def912 | -6.5029 | -35.1689 | 2026-01-13 06:50:00 | GOES-19 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 53.7 |
| b6a632ee-1d58-3246-a388-2b070b5d74cb | -6.4838 | -35.1712 | 2026-01-13 06:50:00 | GOES-19 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 202.0 |
| 31fd962f-f356-3c1f-a056-c833bdcb1b68 | -6.29798 | -37.65372 | 2026-01-13 11:14:00 | TERRA_M-M | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 35c77de4-731d-379a-9796-4e9053c70ee2 | -5.44198 | -39.22456 | 2026-01-13 11:14:00 | TERRA_M-M | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 6338126a-9c69-3120-8675-df152e554e1d | -7.17213 | -35.23315 | 2026-01-13 11:14:00 | TERRA_M-M | SOBRADO | PARAÍBA | Brasil | 2515971 | 25 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| a17ea854-f945-3e90-ae75-2a345800cb19 | -5.75387 | -39.34951 | 2026-01-13 11:14:00 | TERRA_M-M | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 079a835e-0134-3e3a-9ac0-b442f9017980 | -10.19849 | -36.6607 | 2026-01-13 11:17:00 | TERRA_M-M | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 10.0 |
| ff5f4ab4-de93-3d4c-8dfe-09dd3fbc0db9 | -11.63331 | -38.07404 | 2026-01-13 11:17:00 | TERRA_M-M | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| b2989e80-4bdb-3037-8af4-58408a21e243 | -8.46394 | -36.60179 | 2026-01-13 11:17:00 | TERRA_M-M | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 10.4 |
| f72060ec-a956-361a-b715-bf7744dbf33d | -8.28764 | -36.74269 | 2026-01-13 11:17:00 | TERRA_M-M | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 7.4 |


[Clique aqui para ver as próximas entradas](README9.md)
