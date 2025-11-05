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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 88598bd5-a01f-30c6-a158-bd469df0f80f | -4.4633 | -43.2152 | 2025-11-05 03:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 76e9534e-8014-3a4e-ac42-b560068018e8 | -5.4705 | -43.5906 | 2025-11-05 03:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 2408d8d6-37e6-300e-8f30-71c8453fe854 | -5.4553 | -45.3988 | 2025-11-05 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 074049ef-6f21-3365-8e37-7f720379deb1 | -5.0399 | -43.6205 | 2025-11-05 03:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 429499f8-c1d5-3545-83c0-e16b0abdeb5a | -4.4073 | -48.9474 | 2025-11-05 03:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 273.6 |
| af2075f5-040e-332b-90e5-367e2fe67a69 | -5.2453 | -48.4966 | 2025-11-05 03:20:00 | GOES-19 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 85.1 |
| f81a9b8c-903e-3d2b-949e-ae3c38d5ff42 | -5.4707 | -43.5674 | 2025-11-05 03:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 13715ba7-cfbd-3894-b747-3261d08f57a7 | -2.6508 | -48.52 | 2025-11-05 03:20:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| c2a8d40a-89ac-3d37-8784-2c6389b68422 | -4.426 | -48.9251 | 2025-11-05 03:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 79ca7e17-4b2c-3db8-b4d1-5bcb1ede3069 | -3.3135 | -53.839 | 2025-11-05 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 025fc16d-eabb-3a53-ac16-27bcfd6bbea8 | -2.6509 | -48.4985 | 2025-11-05 03:20:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| e1be6771-5d6d-3a8b-ba54-ac55975788f2 | -4.4446 | -43.2164 | 2025-11-05 03:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 8abde70e-912b-3300-9bd1-99c87387834b | -4.4075 | -48.926 | 2025-11-05 03:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 97ec2291-dbb1-355b-9fe4-a090a68fb21c | -6.73613 | -44.14817 | 2025-11-05 03:21:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 29.3 |
| baeb8cb5-f48c-3c56-a22f-8611461778ab | -4.0465 | -43.48312 | 2025-11-05 03:21:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 37e9e158-c1ae-3968-a5ff-db6e1ecf9d2a | -5.92846 | -41.36316 | 2025-11-05 03:21:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d3b00726-cd83-3a02-99be-670d56dc0c30 | -6.476 | -35.25508 | 2025-11-05 03:21:00 | NOAA-21 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8af975ac-f7ef-3179-9fdb-487d725bfe38 | -4.58189 | -43.3348 | 2025-11-05 03:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 29513624-3208-3b1f-ba67-7d9f384acb69 | -6.70256 | -40.83376 | 2025-11-05 03:21:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 237041b8-c245-3427-b50a-e0c3ac5405ab | -5.77459 | -40.80664 | 2025-11-05 03:21:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 3c252a19-1ad7-36e4-9e7e-c58cbf6998ce | -4.58769 | -43.34238 | 2025-11-05 03:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1baae862-d5ef-391e-bd61-f40feb62848e | -4.56805 | -43.33882 | 2025-11-05 03:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b1ccf09-5c20-3e96-ab97-863716010227 | -5.92606 | -41.37677 | 2025-11-05 03:21:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9e43cfbc-c7f8-3499-b2d9-79fe3f5e28df | -8.69347 | -40.54207 | 2025-11-05 03:21:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 51c1404d-d760-39de-ba76-1341f3439595 | -6.20932 | -43.27194 | 2025-11-05 03:21:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 50dd9280-302c-32ca-b456-f24aa301f23b | -6.27067 | -42.56702 | 2025-11-05 03:21:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| e63df742-11dd-3308-8fea-1b99ea1f1a29 | -7.1646 | -40.10147 | 2025-11-05 03:21:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 405b0b62-b6ed-34eb-976e-077b066a441d | -5.57348 | -37.89208 | 2025-11-05 03:21:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ffddf7f4-b4ca-3d1d-9800-58c4c8192d57 | -8.67509 | -36.69267 | 2025-11-05 03:21:00 | NOAA-21 | VENTUROSA | PERNAMBUCO | Brasil | 2616001 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e594faf7-16c3-39df-b712-c396b78b4207 | -7.54912 | -39.58966 | 2025-11-05 03:21:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 495a480c-121a-3dce-920a-3b9a7acfe767 | -6.50126 | -38.20961 | 2025-11-05 03:21:00 | NOAA-21 | LASTRO | PARAÍBA | Brasil | 2508406 | 25 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 5ae5eaf1-0494-36aa-9563-eb8f90236b4f | -6.3916 | -35.20758 | 2025-11-05 03:21:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bbf30f5a-483f-322a-b791-792fdd30938a | -4.46869 | -43.21886 | 2025-11-05 03:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| afadba8e-7f8e-3b06-a2da-6f619566cda7 | -5.46994 | -43.57887 | 2025-11-05 03:21:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 87e7e0a0-852b-3ea7-9640-1350eb712c30 | -5.47696 | -43.57992 | 2025-11-05 03:21:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| a0047bc6-e6f5-325e-ae50-1d59fd3b71cb | -4.45478 | -43.21655 | 2025-11-05 03:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 92ed4ad0-cf57-3d5e-9722-4deb7e515ef5 | -4.58068 | -43.34134 | 2025-11-05 03:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6db26e93-2ea4-3eae-833c-4db49af2f68b | -7.07236 | -41.58361 | 2025-11-05 03:21:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 8d9e7a27-2b9a-346a-a076-c28808c920ca | -7.03689 | -41.46231 | 2025-11-05 03:21:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e944df3e-3e37-324a-9b71-7312007e65e4 | -6.7348 | -44.15516 | 2025-11-05 03:21:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 87b81296-7e42-344e-8176-b361a58de1a6 | -5.15184 | -41.21863 | 2025-11-05 03:21:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b32014a9-f921-3997-9fbc-7af79d35d7a2 | -6.73218 | -44.14661 | 2025-11-05 03:21:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 57478433-402e-3275-bfdb-49a9e390d938 | -7.54764 | -39.59366 | 2025-11-05 03:21:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 00acd7c7-c82c-318f-b076-17b9fbb77f11 | -6.47658 | -35.25163 | 2025-11-05 03:21:00 | NOAA-21 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b72233ad-7854-3b96-a859-c47fb4edf8c2 | -5.47576 | -43.58649 | 2025-11-05 03:21:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| e80d876a-4cd6-3f21-9860-9d608593738b | -4.4733 | -43.23311 | 2025-11-05 03:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 01308931-a55b-34ce-985a-6003719a128c | -7.54853 | -39.593 | 2025-11-05 03:21:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 33cfb6a4-0fa5-36c2-a9f1-0c5234029e18 | -7.54307 | -39.58886 | 2025-11-05 03:21:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b584e2df-5c84-35e1-9f36-1310f8778634 | -7.03836 | -41.45427 | 2025-11-05 03:21:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 8f87311e-f0f4-3284-9a70-3525818d2109 | -4.46519 | -43.2384 | 2025-11-05 03:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 916c0356-9282-3aba-8552-5e6f3204937c | -5.92687 | -41.37216 | 2025-11-05 03:21:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3305387e-6e52-38f3-9697-c20d2ac6e4e2 | -5.92106 | -41.29872 | 2025-11-05 03:21:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f13ef835-8d25-3b2a-9a2c-2465871bbbef | -6.07115 | -43.25102 | 2025-11-05 03:21:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 4efbb2e8-5e0b-3733-8a31-81370ac0e74f | -5.61755 | -41.08618 | 2025-11-05 03:21:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7e46f62b-f372-3bc6-993e-01777a422636 | -7.15908 | -40.10064 | 2025-11-05 03:21:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7ddc71d2-7a1b-32ad-b9bc-63eadbf5cba5 | -4.5832 | -43.33459 | 2025-11-05 03:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 4bdcf4c1-e318-3950-a400-a52edc2ea8e5 | -7.07326 | -41.57877 | 2025-11-05 03:21:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 785cfe6c-2808-37f8-853b-bafeee8bfeed | -7.14052 | -40.45927 | 2025-11-05 03:21:00 | NOAA-21 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| ec34c598-181c-3677-ad57-1c609cbfc8d8 | -6.10239 | -41.70251 | 2025-11-05 03:21:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 419f955c-15eb-3b28-9c8e-02b93a6b156a | -5.51745 | -41.15057 | 2025-11-05 03:21:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 73ec2798-bc30-392d-8276-2c83a4b18941 | -5.9271 | -41.37517 | 2025-11-05 03:21:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 163f8f59-10d7-350b-a4fb-08a1f0764b70 | -7.07057 | -41.58538 | 2025-11-05 03:21:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| ecb3b224-3aa3-3d18-a3cf-597b3d82aafe | -5.92794 | -41.37061 | 2025-11-05 03:21:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9392fa5f-54da-3073-8547-af00267a647c | -7.23348 | -37.15395 | 2025-11-05 03:21:00 | NOAA-21 | CACIMBAS | PARAÍBA | Brasil | 2503555 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 89dc5a33-d47e-3d10-bc00-22769250da26 | -6.46727 | -39.1647 | 2025-11-05 03:21:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e77bb26c-11bd-37e6-9736-6c77a6c4a1e8 | -5.92186 | -41.2942 | 2025-11-05 03:21:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0a1f9530-c9c1-3de2-ad45-cb8a9bf415a4 | -6.45541 | -39.11031 | 2025-11-05 03:21:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 4aa30e9a-9bb3-35b8-a4a8-6eeceb25bab0 | -4.4594 | -43.23072 | 2025-11-05 03:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 3cfded85-f3a3-396b-b0cc-ca4ff872f4d4 | -7.54336 | -39.59149 | 2025-11-05 03:21:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 1810af57-f0d2-3ff8-a700-b6704a55ccd1 | -6.52078 | -39.69287 | 2025-11-05 03:21:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5414bcb8-4213-3b58-93e4-5ba0e066e582 | -7.54825 | -39.59031 | 2025-11-05 03:21:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 32367f69-bd81-379d-8d53-4c3f011ca0b5 | -5.82279 | -39.20409 | 2025-11-05 03:21:00 | NOAA-21 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a5466c62-68f1-3504-99d9-05038a79fd8d | -6.1279 | -41.62617 | 2025-11-05 03:21:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| f55c3f35-0ea0-349b-ae0f-691ea73a5a21 | -6.74051 | -44.16363 | 2025-11-05 03:21:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8b93a442-382e-35b3-bf0f-577b232b43af | -5.92767 | -41.36764 | 2025-11-05 03:21:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ac3b099b-53e4-3c16-ad70-5e1b11807c16 | -6.52683 | -39.69017 | 2025-11-05 03:21:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| db82d171-593a-3206-b634-e6d14ab84ac3 | -6.73087 | -44.15373 | 2025-11-05 03:21:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 825b57fb-5fa6-3802-94fa-4a35df897d62 | -6.13946 | -39.76504 | 2025-11-05 03:21:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 11b6c31a-b03d-3faa-8713-9cbad1794123 | -4.58203 | -43.34113 | 2025-11-05 03:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a42c678e-35ce-3f94-8903-00b986e56bc3 | -6.70915 | -40.83048 | 2025-11-05 03:21:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| dd52185a-433a-37df-b08d-69ad73501830 | -6.63508 | -34.97934 | 2025-11-05 03:21:00 | NOAA-21 | BAÍA DA TRAIÇÃO | PARAÍBA | Brasil | 2501401 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 0b047b5c-bfaf-3fb8-ab27-46c00d6c1789 | -5.10944 | -35.96719 | 2025-11-05 03:21:00 | NOAA-21 | SÃO BENTO DO NORTE | RIO GRANDE DO NORTE | Brasil | 2411601 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a0cf5ede-5f22-31df-96cb-382dc7b4be47 | -7.0436 | -41.4595 | 2025-11-05 03:21:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 4e5468fc-394b-3968-9d95-3d0c29150ab5 | -7.03762 | -41.45827 | 2025-11-05 03:21:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 39781094-d87c-3da4-9f97-1c78d04954f8 | -7.3323 | -38.84961 | 2025-11-05 03:21:00 | NOAA-21 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 0758a18d-9a19-34a8-b2fa-afc1e503db41 | -5.57625 | -37.89431 | 2025-11-05 03:21:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6fb361d6-9c9f-3f8c-ae78-68b549748fb7 | -5.8281 | -39.20492 | 2025-11-05 03:21:00 | NOAA-21 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9527cd10-54ab-3907-a081-ee056d82c1f3 | -5.03402 | -43.63017 | 2025-11-05 03:21:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 252d7171-3987-3fe1-85d7-d9fc8e13d8dd | -7.07756 | -41.58121 | 2025-11-05 03:21:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a54f5962-4650-32f1-ba6d-f85c9013813a | -6.45486 | -39.11341 | 2025-11-05 03:21:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 44193269-6411-3a00-afd3-7fe49db9f364 | -5.51057 | -41.15434 | 2025-11-05 03:21:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 33a34514-8de9-3a02-8517-5247d66456fe | -5.51904 | -41.14152 | 2025-11-05 03:21:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| da41b66b-6cea-3637-9fc2-7f0c9221fdaa | -4.46057 | -43.22421 | 2025-11-05 03:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 13619097-f873-3590-a4a7-eb98a9751823 | -8.68798 | -40.54102 | 2025-11-05 03:21:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ea5480e3-17ae-30bf-ac7e-d35f92a70276 | -6.63424 | -34.98436 | 2025-11-05 03:21:00 | NOAA-21 | BAÍA DA TRAIÇÃO | PARAÍBA | Brasil | 2501401 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 7988d028-c381-3b6e-90da-c899170fecda | -7.07144 | -41.58054 | 2025-11-05 03:21:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 849956e1-dd0c-3b1e-8afc-ab6c95640fd3 | -7.33682 | -38.85345 | 2025-11-05 03:21:00 | NOAA-21 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fedae25a-b84c-388b-97ac-ebd69afbd767 | -4.46752 | -43.2254 | 2025-11-05 03:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 2fa5cc48-0ec1-3ba1-acb1-7b30fd3b216f | -5.92875 | -41.36614 | 2025-11-05 03:21:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e7341061-0d6b-36bb-833c-71a319d2cf76 | -5.92865 | -41.29108 | 2025-11-05 03:21:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |


[Clique aqui para ver as próximas entradas](README8.md)
