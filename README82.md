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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 67845425-5834-3189-be73-a61eb2ef2b37 | -10.0545 | -47.3042 | 2024-10-15 13:26:03 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 30557e10-da1a-3472-bc81-f8f143b79986 | -10.2442 | -47.2824 | 2024-10-15 13:26:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 459d3aea-c764-39e9-8ee0-bac7a7bb6448 | -10.2632 | -47.2802 | 2024-10-15 13:26:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 206.6 |
| 17326a56-aa3f-3241-867a-79526439b5df | -11.7946 | -44.5072 | 2024-10-15 13:26:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 95f5cb8c-266d-375d-b8c8-7b40827b99c2 | -11.7753 | -44.5101 | 2024-10-15 13:26:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 235e4014-320a-3291-ad6e-3c3bdb090881 | -12.3552 | -45.3255 | 2024-10-15 13:26:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 117aa057-0b87-3324-bc5d-195ff5229bb0 | -12.3359 | -45.3284 | 2024-10-15 13:26:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 105.2 |
| f76a1452-5bbd-39af-85b4-70a960ef6a5b | -9.01 | -54.5042 | 2024-10-15 13:35:57 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 64d4bf8b-26aa-3368-9c18-ef842b79630f | -9.4175 | -45.5134 | 2024-10-15 13:35:59 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 198a843f-84b0-3159-8261-1b9985dd68b2 | -9.5185 | -47.8049 | 2024-10-15 13:36:00 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 159.7 |
| 5bdc670d-d212-3bb3-a385-ad58691e2bf4 | -9.5798 | -43.4835 | 2024-10-15 13:36:00 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 91.7 |
| 17b35b89-2efe-31ee-b0b0-56b69ba3ada5 | -9.5188 | -47.7828 | 2024-10-15 13:36:00 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 2c856a0f-431e-300b-a3cb-0f7815169866 | -9.4996 | -47.8068 | 2024-10-15 13:36:00 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 392927db-2cb6-30ef-ba8f-57bdf175a26c | -9.5795 | -43.507 | 2024-10-15 13:36:00 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 139.0 |
| 652489c0-3387-363d-b80e-9c60b9389cea | -9.888 | -47.0342 | 2024-10-15 13:36:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 96.9 |
| d3a0bc34-2771-3186-934e-12b2e6a98328 | -9.9777 | -47.3795 | 2024-10-15 13:36:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 109306fc-fe84-3af2-a044-8d0846841372 | -9.9604 | -47.2705 | 2024-10-15 13:36:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 1d923295-72e1-3710-a835-0a109c2d4c88 | -9.9781 | -47.3573 | 2024-10-15 13:36:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 27f6c9e9-5656-306e-bb3a-937116e6d7a1 | -9.8883 | -47.0119 | 2024-10-15 13:36:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 9a434f61-58e2-3e75-b904-be09899f297a | -9.997 | -47.3551 | 2024-10-15 13:36:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 136.8 |
| 11de8b50-1790-3a33-b5b5-69eaf7417c0a | -9.9793 | -47.2684 | 2024-10-15 13:36:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 140.3 |
| e494c26e-79e9-3e99-ac99-b4f2f116da18 | -10.0443 | -44.1717 | 2024-10-15 13:36:02 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 95.4 |
| d1e41f37-dbc6-3f30-a60f-5c989057fef6 | -10.0633 | -44.1692 | 2024-10-15 13:36:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 6d709b25-2143-3129-ac4a-7a7f5640bf95 | -10.2632 | -47.2802 | 2024-10-15 13:36:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 200.4 |
| 09c06dbe-2799-3cad-aa4f-2e747c8eb6b2 | -12.3167 | -45.3314 | 2024-10-15 13:36:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 110.3 |
| f3adb426-b3f4-350d-ab4c-731c1d19e3e6 | -12.3552 | -45.3255 | 2024-10-15 13:36:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 116.7 |
| fa228ef2-5c10-3d55-aaca-d0d91b82db39 | -12.3171 | -45.3083 | 2024-10-15 13:36:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 06f100a9-5f02-39e2-979e-cd01539ce97f | -12.3359 | -45.3284 | 2024-10-15 13:36:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 108.5 |
| a867c5c9-c44b-3016-a504-fdd60c0d285c | -9.01 | -54.5042 | 2024-10-15 13:45:57 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 109.0 |
| 29e2aaaf-5f28-346e-9ca7-961625f4d2fa | -9.4556 | -44.1763 | 2024-10-15 13:45:59 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 199.3 |
| a5878314-d9dd-335b-a3c2-51e21e3ed9f7 | -9.4702 | -45.8023 | 2024-10-15 13:45:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 83a7999c-766b-32fa-b6b4-522a5b16b198 | -9.4699 | -45.8249 | 2024-10-15 13:45:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 33737542-016c-376f-acc4-92578589ab05 | -9.4696 | -45.8476 | 2024-10-15 13:45:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 03ee5d13-f387-391d-9c09-589170331fb8 | -9.4368 | -45.4884 | 2024-10-15 13:45:59 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 46dc6f8d-a39a-36a8-ab93-ac81fe524e85 | -9.4175 | -45.5134 | 2024-10-15 13:45:59 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 87.9 |
| a8a96871-d4a5-3972-ba3e-70bfb281362d | -9.4513 | -45.8044 | 2024-10-15 13:45:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 5219f3fe-d312-3c5e-a1cd-b442d1ab54b9 | -9.5374 | -47.8029 | 2024-10-15 13:46:00 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 46198cee-d407-3b4c-8e04-d6849daab393 | -9.5912 | -46.6213 | 2024-10-15 13:46:00 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 9ecde7ae-706e-3aa9-82aa-b09a310121da | -9.5798 | -43.4835 | 2024-10-15 13:46:00 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 112.1 |
| a06dfe56-6b84-3a75-bf80-e899234483c0 | -9.5185 | -47.8049 | 2024-10-15 13:46:00 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 137.2 |
| e353926d-ed47-3f47-bf59-0fb6ec8e1f83 | -9.5188 | -47.7828 | 2024-10-15 13:46:00 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 121.5 |
| e068f01f-1536-3cc4-9700-f7262c18c1ea | -9.5377 | -47.7808 | 2024-10-15 13:46:00 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| d67c44a2-9b84-30b7-b27b-9377e2541e4b | -9.5795 | -43.507 | 2024-10-15 13:46:00 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 191.6 |
| dd83512e-1e6f-335d-9baf-adcfa1f27f6e | -9.5909 | -46.6437 | 2024-10-15 13:46:00 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 83e6bdc0-74e9-3741-9b1a-87110d3cb936 | -9.5791 | -43.5306 | 2024-10-15 13:46:00 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 94.6 |
| 8c63465e-9a01-32e9-953c-5a8a5f97aea5 | -9.8495 | -45.7579 | 2024-10-15 13:46:01 | GOES-16 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 88.9 |
| db9e5e42-005c-3390-afa8-7f40b265eb23 | -9.8492 | -45.7806 | 2024-10-15 13:46:01 | GOES-16 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 85.8 |
| de961a65-ee50-399d-810d-2a68cabd6739 | -9.997 | -47.3551 | 2024-10-15 13:46:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 141.5 |
| d93e1f7f-bc65-3200-8774-7c781429e868 | -9.9777 | -47.3795 | 2024-10-15 13:46:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 7c6d11d4-d169-3948-956b-702c218e7bde | -9.888 | -47.0342 | 2024-10-15 13:46:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 150.6 |
| 564ff250-5943-3084-b62b-5623141ef0ee | -9.9781 | -47.3573 | 2024-10-15 13:46:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 140.4 |
| a838d320-bef3-3e0f-843d-3abff24b0ad7 | -9.8883 | -47.0119 | 2024-10-15 13:46:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 253.6 |
| 8ef9cb6e-9cda-3ec1-ac1c-e6a18ec3cd72 | -9.9597 | -47.315 | 2024-10-15 13:46:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 143.3 |
| 87ae7ce5-9802-3b38-b321-e09086a416a3 | -10.082 | -44.19 | 2024-10-15 13:46:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 153.5 |
| 20dda3df-1acb-305f-b39a-ebf2cb04bdd6 | -10.0536 | -47.3709 | 2024-10-15 13:46:03 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 147.6 |
| 091ea5f6-20d1-38aa-b0d5-f6490f8c7d59 | -10.1007 | -44.2108 | 2024-10-15 13:46:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 2a00d6d5-1524-32b9-a6af-383ce1fa5138 | -10.2632 | -47.2802 | 2024-10-15 13:46:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 204.3 |
| baf1bc14-9dee-3f7c-a6d3-dd8b2ab85d5a | -10.2635 | -47.2579 | 2024-10-15 13:46:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 134.1 |
| d0f802f5-a24f-3759-8c27-6be4ebeba87a | -10.9506 | -44.653 | 2024-10-15 13:46:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 973409c8-b8e2-34c9-b47b-e7e78ec93f37 | -11.1304 | -44.1857 | 2024-10-15 13:46:08 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 8bc339a0-44d0-3347-9be7-9f041d82796f | -12.3552 | -45.3255 | 2024-10-15 13:46:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 296890cc-570b-38e9-85cf-b5c182e03651 | -12.3167 | -45.3314 | 2024-10-15 13:46:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 111.2 |
| ba9317ef-f692-3e1f-86f9-3094d0ab157f | -12.3171 | -45.3083 | 2024-10-15 13:46:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 4ae9ace1-affa-3359-926e-a8548867a0b6 | -12.3359 | -45.3284 | 2024-10-15 13:46:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 110.2 |
| afc8066e-425c-3e37-8132-6d1d5d31514b | -4.0148 | -43.2408 | 2024-10-15 13:55:29 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 037e535d-221a-3a02-93e1-6cf9da46ff42 | -9.2012 | -47.5516 | 2024-10-15 13:55:58 | GOES-16 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 83c75e11-591e-3acb-a2cc-2fa870f9d43e | -9.4699 | -45.8249 | 2024-10-15 13:55:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 107.7 |
| bb3dabff-db12-314e-9cff-5f55f9000eff | -9.4696 | -45.8476 | 2024-10-15 13:55:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 38167084-bc5f-3d58-b4b6-bd746ef90d8c | -9.456 | -44.1531 | 2024-10-15 13:55:59 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 2892c7af-b056-3e1e-89c4-97f9159abd10 | -9.4175 | -45.5134 | 2024-10-15 13:55:59 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 9f9a9645-ae72-3b62-ac2c-359518caee0f | -9.4702 | -45.8023 | 2024-10-15 13:55:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| e80488c3-b957-3036-ab3f-c623ad4f8792 | -9.5798 | -43.4835 | 2024-10-15 13:56:00 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 105.8 |
| 66dfc9a9-3a28-37c5-9e2e-91259d4027f5 | -9.5915 | -46.5989 | 2024-10-15 13:56:00 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| b8cf0f61-560b-3181-ad6d-3c6935cde5fc | -9.5075 | -45.8433 | 2024-10-15 13:56:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| ee8d754f-0d85-3d92-a9cc-950f542bd077 | -9.5909 | -46.6437 | 2024-10-15 13:56:00 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 31d47905-ebce-3472-99d6-1fce86232062 | -9.5791 | -43.5306 | 2024-10-15 13:56:00 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 86.9 |
| 8f4a8e8c-a7bf-3fb9-96dc-5b51a93be0a2 | -9.5912 | -46.6213 | 2024-10-15 13:56:00 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 100.9 |
| a70a1380-6e78-3db3-8549-d8896b03b8fb | -9.5374 | -47.8029 | 2024-10-15 13:56:00 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| a74821b2-889c-3c6a-9f9c-c232bc3eebd6 | -9.7064 | -46.4963 | 2024-10-15 13:56:01 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 108.0 |
| f069d31d-eef3-3619-80c8-12568a19dfeb | -9.7067 | -46.4738 | 2024-10-15 13:56:01 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 2fe84bff-49cd-3ffe-88f6-23e2b0492692 | -9.8685 | -45.7556 | 2024-10-15 13:56:02 | GOES-16 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 921ee150-bc43-33e4-9958-8ffe812fee98 | -9.8883 | -47.0119 | 2024-10-15 13:56:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 0101c1f7-e535-3465-9c44-2956a2354c41 | -9.9777 | -47.3795 | 2024-10-15 13:56:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 140.1 |
| df856800-077e-3395-97bf-b335a9349e08 | -10.0492 | -47.6811 | 2024-10-15 13:56:03 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 215957f9-e3b1-31c5-956c-c5aff5f22ff1 | -10.0495 | -47.6589 | 2024-10-15 13:56:03 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 1a1bea15-d32d-36fd-a486-8493403eb67e | -10.2442 | -47.2824 | 2024-10-15 13:56:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 459d3567-7018-3815-aa42-140d4c50471a | -10.2825 | -47.2557 | 2024-10-15 13:56:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 2dd07584-e72c-37c2-bb5a-6a4e8b493533 | -10.2635 | -47.2579 | 2024-10-15 13:56:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 5153e515-4177-34a4-9250-07c99ea6d2f7 | -10.2632 | -47.2802 | 2024-10-15 13:56:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 228.8 |
| 469fa5d5-a639-3f1b-9aef-691b1bd45d7d | -10.9311 | -44.6789 | 2024-10-15 13:56:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 7104f3bb-72a8-3381-83c5-189416586529 | -11.1304 | -44.1857 | 2024-10-15 13:56:08 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 43d5c8d4-be73-3078-81c1-ead53cf79406 | -10.9506 | -44.653 | 2024-10-15 13:56:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 543dfc36-e10f-31ab-959f-6de711a46549 | -12.3552 | -45.3255 | 2024-10-15 13:56:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 126.5 |
| add4ce82-6015-37d2-824b-1af83bbf75c2 | -12.3167 | -45.3314 | 2024-10-15 13:56:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 114.1 |
| de32e52e-da4e-332b-bd6b-4ff7e6055e9e | -12.3171 | -45.3083 | 2024-10-15 13:56:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 6bedaed0-cc00-3736-b89c-12ad9de25a6d | -12.3359 | -45.3284 | 2024-10-15 13:56:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 79fac010-78e3-332a-b041-fd8686eb255c | -12.2974 | -45.3343 | 2024-10-15 13:56:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 8a44e845-9887-3daa-8389-810bcba2aa04 | -1.0796 | -48.8721 | 2024-10-15 14:05:12 | GOES-16 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 171f6ed7-df1c-3621-92bf-6b3e0be7a2ff | -3.2398 | -41.5554 | 2024-10-15 14:05:24 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 102.9 |
| ed996c88-3975-31c7-946e-d16c92ca385b | -3.2211 | -41.5563 | 2024-10-15 14:05:24 | GOES-16 | BOM PRINCÍPIO DO PIAUÍ | PIAUÍ | Brasil | 2201919 | 22 | 33 | nan | nan | nan | Caatinga | 89.7 |


[Clique aqui para ver as próximas entradas](README83.md)
