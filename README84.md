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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 761a5001-1b8c-3a9c-bb44-428b627298ea | -3.5032 | -41.3024 | 2024-11-27 13:30:00 | GOES-16 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 82.8 |
| 91b83458-98e6-3a64-b8ed-a10130cbcf88 | -3.2692 | -43.0441 | 2024-11-27 13:30:00 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| e9524db9-b337-3174-8a29-5742f03e2395 | -3.7994 | -44.9285 | 2024-11-27 13:30:00 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 17950b0b-83dd-308c-b7f6-707e04ba8aec | -3.5742 | -41.9452 | 2024-11-27 13:30:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 128.2 |
| b4cc99e7-d588-3d76-a8cd-b137b081907c | -4.1419 | -43.7905 | 2024-11-27 13:30:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 391e05a9-4523-3332-b3f5-ef10e5f8dfd7 | -3.4093 | -41.3552 | 2024-11-27 13:40:00 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 89.3 |
| 580af29b-9550-36ee-9039-097cb339c650 | -3.1246 | -42.1327 | 2024-11-27 13:40:00 | GOES-16 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 161.8 |
| 75216458-2260-3248-8c64-e51c670dfdc5 | -4.1604 | -43.8125 | 2024-11-27 13:40:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| b901a1ef-cfbf-3886-9057-bd07edcb8f9b | -3.3451 | -50.5126 | 2024-11-27 13:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| dbccc772-48b2-3710-8e29-cb423e910b17 | -3.5929 | -41.9442 | 2024-11-27 13:40:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 110.3 |
| e1398986-be11-32ac-9c3a-c9ecd902c4cb | -3.2692 | -43.0441 | 2024-11-27 13:40:00 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 124.4 |
| ed0e894a-9123-3183-8415-1e12aa5e66f0 | -4.1419 | -43.7905 | 2024-11-27 13:40:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 1af53445-b4ea-3215-9069-9f3232e8abb9 | -3.5741 | -41.969 | 2024-11-27 13:40:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 137.1 |
| 708f43bf-4540-323b-be32-576ec3780699 | -3.6963 | -43.4199 | 2024-11-27 13:40:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 5f5664d4-80cf-3a2a-a34b-c012eb3ff401 | -5.4131 | -37.5999 | 2024-11-27 13:40:00 | GOES-16 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 90.9 |
| 9a3eeb83-f708-3574-982a-869e6e3cfa2a | -4.1417 | -43.8135 | 2024-11-27 13:40:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 78d9bbb3-8d03-361a-ac1b-5f868b2014f8 | -3.2694 | -43.0207 | 2024-11-27 13:40:00 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 65f2dc6e-4de3-3b71-8303-de1ac7779cb7 | -1.1161 | -49.1913 | 2024-11-27 13:40:00 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| c8f86bf4-440a-3d1e-af38-50f80594fad1 | -5.9788 | -45.3621 | 2024-11-27 13:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 115.3 |
| ff910a12-ee59-3e42-b50f-c3626c6c48a3 | -3.6963 | -43.4199 | 2024-11-27 13:50:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 945de4ab-b957-38a6-82d1-21b0da3d7ef5 | -3.1246 | -42.1327 | 2024-11-27 13:50:00 | GOES-16 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| bb533441-1715-3310-8835-ee7729d70d00 | -3.5741 | -41.969 | 2024-11-27 13:50:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 132.6 |
| 5cfcf8fc-ad13-321e-a81b-e9b583bc934a | -3.3451 | -50.5126 | 2024-11-27 13:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 126.0 |
| e69ab52f-ab51-3218-855f-1d0ff2205006 | -17.3021 | -58.1791 | 2024-11-27 13:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.3 |
| e9c32ae4-18af-3b74-81c9-f8a2b9380a69 | -3.1065 | -42.0148 | 2024-11-27 13:50:00 | GOES-16 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 100.9 |
| c98b3415-225a-3ba2-bd1f-61574700ae0e | -4.1604 | -43.8125 | 2024-11-27 13:50:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 3a9bf371-0cb0-3a38-8c7b-1df86b9eb9e0 | -3.5929 | -41.9442 | 2024-11-27 13:50:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 121.0 |
| 14eeebc8-7ab7-3092-b3a8-ed0949d5c980 | -4.1419 | -43.7905 | 2024-11-27 13:50:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 25a12bfa-e657-3af9-9063-3d769c18caa9 | -3.6962 | -43.4432 | 2024-11-27 13:50:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 18a5f028-1e53-3f28-8819-b14d476ee1c4 | -3.2694 | -43.0207 | 2024-11-27 13:50:00 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 804fa3d7-ef63-3b51-bbb3-4c322aa794eb | -3.2692 | -43.0441 | 2024-11-27 13:50:00 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 45f8c2af-3e73-328f-abbb-0bf7b73c755a | -3.6962 | -43.4432 | 2024-11-27 14:00:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 165.5 |
| 51fb21c7-2cd6-31f9-968d-62371645b705 | -3.6043 | -50.3571 | 2024-11-27 14:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 0805ee27-c3bb-38fe-9d83-7efcdb18cb3d | -17.3626 | -58.0703 | 2024-11-27 14:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.6 |
| 02de8915-2971-31fe-af2b-5de86249ee59 | -3.5929 | -41.9442 | 2024-11-27 14:00:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 108.8 |
| e9e2ea39-aa12-3cf2-99a9-b21a45c4ebfb | -17.5865 | -57.5739 | 2024-11-27 14:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.5 |
| fb531bc9-275d-3603-aeba-9afe382360e6 | -3.5741 | -41.969 | 2024-11-27 14:00:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 160.6 |
| 37cabfbc-0152-3323-989a-ed87c4f64ef0 | -4.1419 | -43.7905 | 2024-11-27 14:00:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 103.1 |
| c83d3980-402c-38b3-8ab8-f61621e220ba | -3.2694 | -43.0207 | 2024-11-27 14:00:00 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 80d363a1-0dd0-3144-97ed-c480e68d855b | -17.3021 | -58.1791 | 2024-11-27 14:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.2 |
| 04fce26d-668a-340d-b682-c33c6780cd2d | -5.9975 | -45.3607 | 2024-11-27 14:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 284b9507-ccac-37b5-b6f8-30ca77fc2e52 | -3.6963 | -43.4199 | 2024-11-27 14:00:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 249.6 |
| 4c51026c-0651-32f3-98af-cfba821726b4 | -3.9027 | -43.2467 | 2024-11-27 14:00:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| b7d1b36d-e799-30cc-9531-89bbfea5c5e9 | -3.2692 | -43.0441 | 2024-11-27 14:00:00 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| fe71cf9e-92ce-34c4-8cec-2d1a36d5fda3 | -3.3451 | -50.5126 | 2024-11-27 14:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 122.2 |
| 210673ab-0475-3506-8ee3-de83d485f3a4 | -3.1065 | -42.0148 | 2024-11-27 14:00:00 | GOES-16 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| e5754f4d-9793-366e-a5d3-ba44c0240800 | -6.12 | -43.95 | 2024-11-27 14:00:00 | MSG-03 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 55fbf071-be18-3eef-aa38-51d9393db499 | -6.12 | -43.99 | 2024-11-27 14:00:00 | MSG-03 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a9518a9c-61a1-326f-84dd-9de2fa72200d | -6.09 | -43.94 | 2024-11-27 14:00:00 | MSG-03 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dfbe377f-f0a4-3b66-b304-a815381a8688 | -3.493 | -50.4658 | 2024-11-27 14:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 0e84a608-34c6-3793-a9a6-547c3d5564dd | -17.5865 | -57.5739 | 2024-11-27 14:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.0 |
| d649aee3-b2bb-3e38-a40e-3671790a055d | -4.1417 | -43.8135 | 2024-11-27 14:10:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 131.5 |
| f6a56a51-a3dd-3e61-8ae9-747d710fb768 | -18.3368 | -57.544 | 2024-11-27 14:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.9 |
| 7328b5fa-87fe-30c5-8b34-0b2feffa192a | -3.6963 | -43.4199 | 2024-11-27 14:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 229.7 |
| a4fa20a8-d721-3cc4-9e67-8d49a60321bb | -3.9025 | -43.27 | 2024-11-27 14:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 9c428774-5ac5-394b-a1b3-eedeab5cad43 | -4.1419 | -43.7905 | 2024-11-27 14:10:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 110.2 |
| a77f8201-7176-3d6a-af66-d0b7fb8787ab | -3.7994 | -44.9285 | 2024-11-27 14:10:00 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 71.9 |
| e9e28ec5-3ca3-3a20-9bd7-8555b310fa6a | -3.5094 | -43.4753 | 2024-11-27 14:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| f814d8b9-041f-3c20-aab1-cab0f4c47ecf | -4.1604 | -43.8125 | 2024-11-27 14:10:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 2a91c97d-baed-3a9b-8f78-cd9909a9a10f | -3.2692 | -43.0441 | 2024-11-27 14:10:00 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 213.5 |
| 2e70966f-5c5a-375d-b586-3f682ef6d3c9 | -3.5929 | -41.9442 | 2024-11-27 14:10:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 125.6 |
| 066bd971-a628-3b9f-b586-0292f7543b1a | -3.9027 | -43.2467 | 2024-11-27 14:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 213.2 |
| 7e8b3af7-c3b5-3737-95f5-6735ed519045 | -3.3451 | -50.5126 | 2024-11-27 14:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 55244869-7fef-3937-8fe2-db0c31a652c4 | -3.5741 | -41.969 | 2024-11-27 14:10:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 149.9 |
| 3a8c219d-ba25-3387-a27d-c43cd0f02119 | -3.6043 | -50.3571 | 2024-11-27 14:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 0b9f32fa-6ad4-398d-902e-b93da2f6182f | -3.2694 | -43.0207 | 2024-11-27 14:10:00 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 205.2 |
| 2349fa81-3aa5-3270-bdd6-27bbb923cf04 | -3.6963 | -43.4199 | 2024-11-27 14:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 203.1 |
| b2f17225-96a5-3a2b-9226-90bb66e566db | -3.6962 | -43.4432 | 2024-11-27 14:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 163.7 |
| d448bd75-7193-37ee-8a8e-a7d203af8836 | -3.5115 | -50.4652 | 2024-11-27 14:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 6f2d798e-1247-30b3-b183-ca5ffeef063f | -3.7994 | -44.9285 | 2024-11-27 14:20:00 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 4a82a7e3-0cae-31a3-9793-125b7532e057 | -5.9788 | -45.3621 | 2024-11-27 14:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| f920cee9-2e15-3f52-900b-1a15d71cd982 | -3.8209 | -44.427 | 2024-11-27 14:20:00 | GOES-16 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| e0713701-8194-3d1b-a761-379d8d948075 | -4.1604 | -43.8125 | 2024-11-27 14:20:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 5df6837e-828d-36ae-90a0-28be93b397ed | -3.2692 | -43.0441 | 2024-11-27 14:20:00 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 173.1 |
| da0a97a4-1675-3ac8-bfe2-8026169d2661 | -3.6226 | -43.2608 | 2024-11-27 14:20:00 | GOES-16 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 133.4 |
| bfbd2785-78d7-33c9-8c43-4da19721c109 | -3.9027 | -43.2467 | 2024-11-27 14:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 01ce7960-13a4-3585-b418-09c710efbfa5 | -4.1419 | -43.7905 | 2024-11-27 14:20:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 131.7 |
| d3b3fcec-97cd-36e7-adb6-1c376fe05abd | -1.9062 | -50.5911 | 2024-11-27 14:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 18f7221f-645b-3634-915f-7c57566745f5 | -18.3368 | -57.544 | 2024-11-27 14:20:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.2 |
| 624f85d4-58ee-30a8-8420-979cda9a4c0f | -3.2694 | -43.0207 | 2024-11-27 14:20:00 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 143.0 |
| b80eaf4d-4f31-311f-9c26-bf01ab84138a | -17.5865 | -57.5739 | 2024-11-27 14:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.1 |
| a2306493-f1c7-3628-bb8e-d9a272b583e9 | -4.1416 | -43.8366 | 2024-11-27 14:20:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 137.4 |
| fcc441d7-71eb-3cb9-ab18-252bac5770f9 | -5.3762 | -35.6182 | 2024-11-27 14:20:00 | GOES-16 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 90.1 |
| 49cfa683-8082-30e6-84d7-a5a2adb2ea0a | -3.493 | -50.4658 | 2024-11-27 14:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 111.1 |
| a4464feb-9b7c-3986-ae47-49545d2052ba | -3.2694 | -43.0207 | 2024-11-27 14:30:00 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 127.5 |
| d687b908-e9b3-39f4-a5f4-e1b6ad5691b6 | -3.9025 | -43.27 | 2024-11-27 14:30:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 181.3 |
| 0ae17260-e489-3c69-8d83-b61754e5b32c | -3.2164 | -42.4362 | 2024-11-27 14:30:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| ac4cc3d8-92a6-3bf2-85fd-70386fb73144 | -4.1419 | -43.7905 | 2024-11-27 14:30:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 6b176f43-bb74-349f-82ed-c8c2aee96e5c | -3.9027 | -43.2467 | 2024-11-27 14:30:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 246.6 |
| 739bc691-106f-39ff-883f-e6afcb87a44e | -3.6963 | -43.4199 | 2024-11-27 14:30:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 302.7 |
| 11cc0085-bc5e-31eb-bf20-e5b7856b0f22 | -17.5865 | -57.5739 | 2024-11-27 14:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.4 |
| 1cae6776-02ab-33c3-9573-7abf75c66cdd | -18.3368 | -57.544 | 2024-11-27 14:30:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.6 |
| a02084cb-22dc-3edf-b70d-0fb8eeaddd1b | -3.8208 | -44.4498 | 2024-11-27 14:30:00 | GOES-16 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 8853dc19-8f6c-3f51-a43f-d774777312ab | -3.6962 | -43.4432 | 2024-11-27 14:30:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 237.1 |
| c0d7d8db-e62c-3236-b004-3c3cc08f8589 | -3.2721 | -42.5044 | 2024-11-27 14:30:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 152.0 |
| b73a0d52-44ed-395e-8afb-4ab71495b02a | -3.1978 | -42.437 | 2024-11-27 14:30:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 68f7bdf8-4abf-3538-bfeb-ec883a6ea6dc | -3.2692 | -43.0441 | 2024-11-27 14:30:00 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 132.2 |
| f9300575-9a8a-34fa-9e2f-3da747c16448 | -4.1604 | -43.8125 | 2024-11-27 14:30:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 96.0 |


