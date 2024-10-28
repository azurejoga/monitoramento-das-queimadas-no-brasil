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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 187c099b-a1d8-3724-a3e6-8ff96fa7cdd3 | -3.4014 | -46.3131 | 2024-10-28 01:05:25 | GOES-16 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 106fbaef-69d2-381c-85ba-b14bbffaa7a7 | -3.6911 | -51.5622 | 2024-10-28 01:05:26 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| a7e0ddb8-4de9-303f-8e5a-df10e4e9e443 | -3.9949 | -46.4867 | 2024-10-28 01:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 5f11ae03-f1bf-3c08-8c01-d57502db3845 | -4.0681 | -50.024 | 2024-10-28 01:05:28 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 2a40615d-3a98-3d5b-ae24-98117260e824 | -4.2611 | -45.5372 | 2024-10-28 01:05:29 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 3e2608b3-f5cc-348b-90d8-beee72fa3537 | -4.2797 | -45.5362 | 2024-10-28 01:05:29 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 225.3 |
| dafa1214-7eac-3ccd-ab30-32704d38ad96 | -4.2799 | -45.5138 | 2024-10-28 01:05:29 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 88.6 |
| abadfa9e-d1ea-3d27-bb0c-8eee1de77c85 | -4.4093 | -45.6641 | 2024-10-28 01:05:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 133.7 |
| 924fce0c-b435-3569-a953-7680a17bf509 | -4.4094 | -45.6416 | 2024-10-28 01:05:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 215.2 |
| fb9f0191-2592-3e92-bb09-5de91bf9694d | -4.4279 | -45.6631 | 2024-10-28 01:05:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 90.6 |
| a922b978-daed-3279-8c9e-9a3f03450e45 | -4.428 | -45.6406 | 2024-10-28 01:05:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 183.8 |
| 24265527-4de4-3114-9ab3-ee4c4351de55 | -4.758 | -46.4033 | 2024-10-28 01:05:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 73.0 |
| b713c3b3-e1b7-3b3c-a2c5-e975260d6987 | -4.7581 | -46.3811 | 2024-10-28 01:05:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 49.5 |
| b32874d9-30dd-34cd-a44a-61ba7508fdc7 | -4.7766 | -46.4022 | 2024-10-28 01:05:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 115.9 |
| 282706eb-ff8d-34e5-b9dc-d0e99793609d | -4.7768 | -46.3801 | 2024-10-28 01:05:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 77.6 |
| ca2336e4-3dd7-3372-af6a-62767ab40f04 | -9.9497 | -36.2836 | 2024-10-28 01:06:00 | GOES-16 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 77.4 |
| 23ad6f3b-fe11-363c-aeb6-a3b6b3288ed0 | -1.1836 | -53.5158 | 2024-10-28 01:15:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| df28902f-c0ed-3985-bad3-3dcfd0510b5e | -1.1836 | -53.4956 | 2024-10-28 01:15:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 3ba8cedf-8055-390f-9a65-f3ad9ea11992 | -1.5349 | -52.0874 | 2024-10-28 01:15:14 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| bdf44eb4-e617-3602-9ad5-c44fec72c525 | -1.5532 | -52.1076 | 2024-10-28 01:15:14 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| a9e9403e-c3fc-32e8-b370-e2b5e7bef9e8 | -1.5533 | -52.0871 | 2024-10-28 01:15:14 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| d469cb51-dc22-39ba-9aed-21937da7acf3 | -2.2662 | -53.8027 | 2024-10-28 01:15:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| a8b74b9d-664f-3300-a974-de9f0104e3bd | -2.2662 | -53.7825 | 2024-10-28 01:15:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 184.0 |
| b9bd83e5-9d33-3784-bd7b-c20308f97be1 | -2.2663 | -53.7624 | 2024-10-28 01:15:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 3939277f-1754-3057-aa25-b52055ca3187 | -2.2845 | -53.8023 | 2024-10-28 01:15:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 831909dd-7f20-3ecb-bedf-98457aa94ee5 | -2.2846 | -53.7822 | 2024-10-28 01:15:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 250.9 |
| ffa81ad6-8432-3860-8ed9-0c16b4a34acc | -2.2846 | -53.762 | 2024-10-28 01:15:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| ede1e024-01d4-332f-92b2-7886c15ef327 | -2.3919 | -48.5484 | 2024-10-28 01:15:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| a33c3662-0194-363a-9859-51cd9fc7e75a | -2.4104 | -48.5479 | 2024-10-28 01:15:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 107.7 |
| 73b1d691-ee5e-3aa1-917a-d3b4f6314394 | -2.5127 | -51.1821 | 2024-10-28 01:15:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 1816867a-0c3c-3926-9e64-313b1c255e02 | -2.5251 | -47.442 | 2024-10-28 01:15:20 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 51f1dbd9-28f5-3da6-b065-b6b2c5ba42d5 | -2.531 | -51.2024 | 2024-10-28 01:15:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| c3974310-51f9-3682-aee8-5bb84b027121 | -2.5311 | -51.1816 | 2024-10-28 01:15:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| b603d1ae-e1c6-362c-ace7-74445a6f9364 | -2.6399 | -51.7374 | 2024-10-28 01:15:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| d51242cc-7fca-36a7-95d8-cf9913382aee | -2.6583 | -51.737 | 2024-10-28 01:15:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| bb39129c-77dc-3b33-a199-2b3d7af0ba44 | -2.7033 | -49.33 | 2024-10-28 01:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 0116bb74-870a-354b-80aa-9c1500a417b1 | -2.7034 | -49.3088 | 2024-10-28 01:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 93d6be35-ac8d-3696-a6ae-e8dbbe5d442d | -2.7219 | -49.3083 | 2024-10-28 01:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 6f691c0b-519e-3b0c-b5f2-99ab567d6e8a | -2.8555 | -53.3459 | 2024-10-28 01:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| f0abc72a-5127-3ed2-a290-7fcc52da31b3 | -2.8556 | -53.3256 | 2024-10-28 01:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 1a9bafb8-1774-3774-a393-6f922d0addb8 | -2.9047 | -45.2819 | 2024-10-28 01:15:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 91.0 |
| c1805510-7637-36f5-80f4-953ccf002ea7 | -2.9048 | -45.2594 | 2024-10-28 01:15:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 149.8 |
| 07e94842-db89-34e7-b315-39e87a21a61c | -2.9234 | -45.2587 | 2024-10-28 01:15:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 2d0f8ae0-a323-392a-b616-82abc5ba955a | -3.0538 | -49.4895 | 2024-10-28 01:15:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 31f51e71-667b-327f-a851-f4cb2bf9367b | -3.272 | -46.2072 | 2024-10-28 01:15:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 9d002c10-8d95-3362-bf76-6c8cdf40c458 | -3.4014 | -46.3131 | 2024-10-28 01:15:25 | GOES-16 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 1784339f-800d-3d7d-bb03-08e3e46c20c8 | -3.6911 | -51.5622 | 2024-10-28 01:15:26 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| b784a62a-f4f5-34dc-9a4c-309bf8a48176 | -3.9949 | -46.4867 | 2024-10-28 01:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 02e7fa64-e9b9-369d-ab0f-d41b7da9e25b | -4.2611 | -45.5372 | 2024-10-28 01:15:29 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 7fb58486-b7b9-3b6b-b519-38e7b72182d8 | -4.2796 | -45.5587 | 2024-10-28 01:15:29 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 77d44cbc-b0d8-38e1-991e-e9e0140e64a8 | -4.2797 | -45.5362 | 2024-10-28 01:15:29 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 371.9 |
| 0cf71f72-ff07-30e9-af6e-81a02b748889 | -4.2799 | -45.5138 | 2024-10-28 01:15:29 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 132.7 |
| 4b23f18f-faf2-3b2d-89b4-e547df854edf | -4.2984 | -45.5353 | 2024-10-28 01:15:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 949e80e9-27fb-3141-8549-c601c880bba3 | -4.4093 | -45.6641 | 2024-10-28 01:15:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 107.7 |
| 14d99eec-57a5-366d-86e5-9c2728a31e8b | -4.4094 | -45.6416 | 2024-10-28 01:15:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 176.3 |
| c48e99a6-d934-3e85-828e-ff032f7e1ed8 | -4.4279 | -45.6631 | 2024-10-28 01:15:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 494f336c-7c7f-3999-adfd-19eb5714d9cd | -4.428 | -45.6406 | 2024-10-28 01:15:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 207.0 |
| 865c9366-d5a7-30a4-9f1d-9abaf9e1f348 | -4.7766 | -46.4022 | 2024-10-28 01:15:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 6a0be205-38b8-3128-bd70-5668b4c2ff2c | -15.3686 | -40.1745 | 2024-10-28 01:16:30 | GOES-16 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 98.7 |
| 18c3387f-a919-3ea0-a59c-743695cbfb52 | -1.1653 | -53.4957 | 2024-10-28 01:25:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 2844c389-cc7e-3714-9401-6cc5614b00b3 | -1.1836 | -53.4956 | 2024-10-28 01:25:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 1e024ccc-d8b2-31c2-91db-f406bcf72194 | -1.5349 | -52.0874 | 2024-10-28 01:25:14 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| a03c99a8-7e3e-3332-be9d-980ce49cf5d3 | -1.5532 | -52.1076 | 2024-10-28 01:25:14 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 529f2879-e151-3e64-9458-bfae3127528b | -1.5533 | -52.0871 | 2024-10-28 01:25:14 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| e9fedd69-666a-3ed0-be3f-f750d08a48fe | -1.9763 | -52.0804 | 2024-10-28 01:25:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| c304fa13-0cc7-30da-a95b-8a86a18c8b47 | -2.0499 | -52.0791 | 2024-10-28 01:25:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| a13e0950-51e1-3a77-bac7-81b81af20f33 | -2.1826 | -50.6065 | 2024-10-28 01:25:18 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 8c47731c-eb4f-3742-883d-006f94392a3d | -2.2662 | -53.8027 | 2024-10-28 01:25:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 380c27d8-2a16-3bbc-8ed2-3f27f853e2df | -2.2662 | -53.7825 | 2024-10-28 01:25:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 284.1 |
| 9f0dcb59-c2f9-3ea8-8454-5f3721fd0ff6 | -2.2663 | -53.7624 | 2024-10-28 01:25:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 694a7bcd-7dfe-301e-abb7-5bd7f890c3e8 | -2.2845 | -53.8023 | 2024-10-28 01:25:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 7a6c9a50-5244-34ad-9bf6-3aee0916ef7a | -2.2846 | -53.7822 | 2024-10-28 01:25:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 162.8 |
| 5f6f3784-aee5-3a1f-a3bc-8b91a11fe350 | -2.2846 | -53.762 | 2024-10-28 01:25:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| a7ee916a-77bd-3d3a-90e2-cd136e7ab7a0 | -2.3919 | -48.5484 | 2024-10-28 01:25:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 16611bc8-5a81-3369-8fe9-3aa25e6bfb37 | -2.4104 | -48.5479 | 2024-10-28 01:25:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 9339ea0b-4dc5-3e40-b009-f0af863bb3b1 | -2.5127 | -51.1821 | 2024-10-28 01:25:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 4e5719e1-58f0-3413-9a0e-50e1465738c3 | -2.5251 | -47.442 | 2024-10-28 01:25:20 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| b32fe87d-60d0-3772-b36f-2689dfd31bb0 | -2.531 | -51.2024 | 2024-10-28 01:25:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 5e712d23-74bd-30eb-b3d1-6b873e4012f0 | -2.5311 | -51.1816 | 2024-10-28 01:25:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 1a4db6b4-b620-34b0-b22a-c5bc17405410 | -2.7033 | -49.33 | 2024-10-28 01:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 95646fa0-67d9-35eb-aef1-0891dfedf4a1 | -2.7034 | -49.3088 | 2024-10-28 01:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| f20e3625-178b-3d92-ad3f-cd57a3ca84d3 | -2.7219 | -49.3083 | 2024-10-28 01:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 3c65735e-108e-3b1d-a0cf-6f204cfde78d | -2.9047 | -45.2819 | 2024-10-28 01:25:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 182.8 |
| bb202a1a-cba2-3877-9e9b-0e4e19f5a801 | -2.9048 | -45.2594 | 2024-10-28 01:25:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 284.8 |
| 153ad347-7c17-3715-b9bc-f2ddd52664ea | -3.0317 | -50.4176 | 2024-10-28 01:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 66f15ac5-d747-309f-9712-3a15337383e6 | -3.0538 | -49.4895 | 2024-10-28 01:25:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 81ffb0e7-450d-36e3-80cf-7f51b21e5453 | -3.4014 | -46.3131 | 2024-10-28 01:25:25 | GOES-16 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 6e64b64f-7ebe-30d0-9cd5-92516d61a1ae | -4.0681 | -50.024 | 2024-10-28 01:25:28 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| d1d5398b-d8b5-3642-b169-c0747ac382fd | -4.2797 | -45.5362 | 2024-10-28 01:25:29 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 187.5 |
| a55c3d15-7467-3905-9be2-31d61b906543 | -4.2799 | -45.5138 | 2024-10-28 01:25:29 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 80.5 |
| d70cf9e3-faea-3b06-a50e-8150ebef4cdd | -4.4093 | -45.6641 | 2024-10-28 01:25:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 6715ab1d-9836-3fa4-bee0-78a4efdf248b | -4.4094 | -45.6416 | 2024-10-28 01:25:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 136.1 |
| 83a26360-3fb9-395f-a215-daaffc082c8b | -4.4279 | -45.6631 | 2024-10-28 01:25:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 90.5 |
| b50b1000-2965-3f96-a0b6-9b3b96d82178 | -4.428 | -45.6406 | 2024-10-28 01:25:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 200.1 |
| 8094b7c2-4551-3d4f-b26f-2122e7594b40 | -4.7768 | -46.3801 | 2024-10-28 01:25:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 0f634123-dd7c-320f-a02f-7cc0e9e075f3 | -4.758 | -46.4033 | 2024-10-28 01:25:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 41.0 |
| f5c768a0-765e-3562-8170-0bfcf9f40b99 | -4.7766 | -46.4022 | 2024-10-28 01:25:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 96.4 |
| c1bfa056-77e1-315f-bcc9-e1e5e4285146 | -9.4323 | -44.4803 | 2024-10-28 01:25:58 | GOES-16 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 5627e9fb-5325-3fcb-b9e2-0d631ec19ab7 | -10.5308 | -59.421398 | 2024-10-28 01:32:32 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1f06425f-b339-33be-8863-fb2d759a26c2 | -3.4065 | -54.488098 | 2024-10-28 01:34:08 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README19.md)
