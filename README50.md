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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8faf6a02-5b83-345e-8b75-85ced257636f | -1.61205 | -47.46756 | 2024-10-08 04:32:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52f47ffc-0773-30f4-a698-17ced4b2333d | -1.59119 | -48.0334 | 2024-10-08 04:32:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 24d84568-cd4d-3ac9-9021-fd72e21dec00 | -1.56539 | -47.33308 | 2024-10-08 04:32:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc4f8120-6373-3634-a4ea-cb40e62eceac | -1.26057 | -47.64717 | 2024-10-08 04:32:00 | NOAA-21 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1fa7897d-69b4-3bae-9f8b-c073bf270ff5 | -1.05815 | -48.00447 | 2024-10-08 04:32:00 | NOAA-21 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24206196-634c-394c-995c-5b5d23e6e0d4 | -1.34932 | -47.21423 | 2024-10-08 04:32:00 | NOAA-21 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4d2280bb-e68f-34c4-a671-25566c518c77 | -3.49698 | -48.89256 | 2024-10-08 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16bd2ac2-8c9e-3d48-86fe-12ec47948710 | -3.49641 | -48.89617 | 2024-10-08 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7c067c2-f818-3c08-afc6-f5143600dbe0 | -3.49632 | -48.91852 | 2024-10-08 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8e6eb81-e78e-3169-a9f1-cf9b69676207 | -3.4936 | -48.89201 | 2024-10-08 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 083a7a21-1325-3307-9862-7b25b591ab88 | -3.49302 | -48.89564 | 2024-10-08 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98a12b46-1190-3667-a0a6-d69c87afd9ae | -3.49293 | -48.91799 | 2024-10-08 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 084dfa04-5e94-3c72-b363-37ff2b213b79 | -3.48963 | -48.8951 | 2024-10-08 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae04dd7c-516c-387d-b081-5407745da3c4 | -3.48905 | -48.89874 | 2024-10-08 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b2f3ee52-8d18-35ba-8457-557832ec71a9 | -3.48567 | -48.89821 | 2024-10-08 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a216cb00-a43e-3018-978d-1e101f0c6ecb | -3.48508 | -48.90185 | 2024-10-08 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7cee5db3-6d56-3b02-8303-f8531611fa3e | -3.46423 | -47.66109 | 2024-10-08 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1a87c67c-21fd-3fa3-836f-cfcccb829f06 | -3.46369 | -47.66453 | 2024-10-08 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 625c4162-2f20-3d1c-8522-7f5c66e5c30b | -3.46184 | -48.82046 | 2024-10-08 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eab6a009-4cb5-3d9e-9d40-987b957d2887 | -3.46039 | -47.66402 | 2024-10-08 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 77ced97e-4888-371c-afe1-ebfdc678bad2 | -3.45846 | -48.81993 | 2024-10-08 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0c7895b-5166-3088-b2db-ee3e58b79c26 | -3.2208 | -48.92422 | 2024-10-08 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d2229f10-1e16-3f33-a762-60ca4a1588e6 | -3.22022 | -48.92789 | 2024-10-08 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e596943c-1c59-3f22-835e-36815735cbd3 | -3.12029 | -48.63025 | 2024-10-08 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38070fdd-158e-3c08-9f09-8d2842a270b2 | -3.11692 | -48.62972 | 2024-10-08 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9908fa48-0036-3c98-ae6d-0490a5c3c8a6 | -3.11635 | -48.63332 | 2024-10-08 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 439093b9-4468-3068-8b75-a95346cf642e | -2.84162 | -48.0889 | 2024-10-08 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f3f4399-1888-370d-977f-9a59c2af8b03 | -2.83836 | -48.79363 | 2024-10-08 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1a0e06a5-1c88-326f-8f4d-32c88376d29d | -2.79301 | -48.56806 | 2024-10-08 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| dd99415f-6f4f-3ed5-a049-5013c837ca98 | -2.79244 | -48.57165 | 2024-10-08 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3a755472-ba8f-352b-acbd-062018279813 | -2.79187 | -48.57524 | 2024-10-08 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 4de0aa17-335a-33f4-8f94-0d598721ed1f | -2.78964 | -48.56753 | 2024-10-08 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f143f324-915a-315e-a443-ab040dfe8d7a | -2.78907 | -48.57111 | 2024-10-08 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7e7c69e5-7784-3d8f-8df2-3b75a81739ef | -2.7885 | -48.57471 | 2024-10-08 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7f218d7c-19b8-3904-82a7-c1197883ad8d | -2.54669 | -48.40845 | 2024-10-08 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b91029ab-e010-3b42-acb5-8ca6c973d98f | -2.40874 | -48.59343 | 2024-10-08 04:32:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8f497341-3a90-30fa-a184-6278bcba3b4c | -2.40817 | -48.59705 | 2024-10-08 04:32:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2a1bde80-aeae-305f-80a8-d744a712e84e | -2.40536 | -48.5929 | 2024-10-08 04:32:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ebd897c4-ee5b-345f-85bc-7946e417a636 | -2.40479 | -48.59652 | 2024-10-08 04:32:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00e73a33-f9a2-36e1-8bff-853e3ddf6cd5 | -2.38895 | -48.63118 | 2024-10-08 04:32:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7336d09a-db41-3d4b-accf-78ffc9e73fa3 | -2.35207 | -48.49223 | 2024-10-08 04:32:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ff667c1-f577-3826-978b-d35bd1023279 | -2.34254 | -48.83743 | 2024-10-08 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66cde9e5-7e85-37b3-b313-22e9f29b3dbb | -2.29593 | -48.48664 | 2024-10-08 04:32:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce1da318-6978-3c86-86c9-b5e589638079 | -2.29536 | -48.49024 | 2024-10-08 04:32:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 800f3fda-09d2-31bc-91eb-47c69a1c3444 | -4.78136 | -49.2093 | 2024-10-08 04:32:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d4a0cff6-50bb-3a06-9f11-c511cef6abf9 | -4.92184 | -48.62286 | 2024-10-08 04:32:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83c0fa52-6496-3d9c-92c8-58bee3af5926 | -4.78763 | -48.09724 | 2024-10-08 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bea0b0bb-af8a-3bfd-8c80-fc7d08fcfe25 | -4.7798 | -48.89441 | 2024-10-08 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 730ad68f-7e11-3f96-b6f1-3fced35c6f8c | -4.77923 | -48.898 | 2024-10-08 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc9391d5-c9a0-3c76-8136-517020516d95 | -4.77807 | -48.90518 | 2024-10-08 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c51acbea-5985-356e-a7c9-9667d1c30b7f | -4.39647 | -48.69524 | 2024-10-08 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0b40b62d-0bfe-306c-874a-7362a38e74c0 | -4.39368 | -48.69119 | 2024-10-08 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 93a4845e-9003-31ae-9d17-65e7c8aa4d0e | -4.39312 | -48.69472 | 2024-10-08 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5f9a8104-cda5-3dc8-8192-d52a1c1b3619 | -4.39033 | -48.69067 | 2024-10-08 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 009c4526-7fa7-3fdd-8eb3-c0fe7ab2a111 | -4.38977 | -48.6942 | 2024-10-08 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46727bed-852a-353d-8e35-3db8ce7384af | -4.38194 | -48.70024 | 2024-10-08 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| e70bf6b2-93d9-3c8e-ac64-068eb6a3c726 | -4.37581 | -48.69563 | 2024-10-08 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c0421fa-a597-30ae-a040-ceb59b51e4b1 | -4.37524 | -48.6992 | 2024-10-08 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f2f6b664-613c-3c96-a9c6-f132dccc30cc | -4.36265 | -48.22198 | 2024-10-08 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 702ec7c0-ccfa-3bb1-b09b-700a81e77c1e | -4.36044 | -48.2145 | 2024-10-08 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a80a7b5-bb12-33b7-9b30-dd79ee3dbd39 | -4.35989 | -48.21797 | 2024-10-08 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d924203c-b4f6-3892-a851-d00dc34eda73 | -4.29756 | -48.33274 | 2024-10-08 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aacf745c-afa0-397e-8f0c-1b8e276cd627 | -4.2812 | -48.64833 | 2024-10-08 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58a5c4d7-0ba1-33e0-b58c-aa33a6466733 | -4.21547 | -48.87535 | 2024-10-08 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0da43503-350d-3d78-8ebf-f37241071aeb | -4.19136 | -48.57194 | 2024-10-08 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 23397adc-f409-3c41-b7d6-3626e010b379 | -4.18857 | -48.56791 | 2024-10-08 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a0e75d94-6468-32b8-9326-69b827dce503 | -4.18801 | -48.57143 | 2024-10-08 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bf11c64a-cda0-333d-b7ed-60182e1445df | -4.16393 | -48.61489 | 2024-10-08 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a36b6f4-31b8-334f-853a-f20ccb5a1087 | -4.16001 | -48.61791 | 2024-10-08 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80faa269-d216-3df1-8fde-ca2a835d6dbe | -4.1423 | -47.87079 | 2024-10-08 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a44b8176-c762-337a-93f8-7eb782960ff9 | -4.09882 | -48.25496 | 2024-10-08 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6d5c7e1d-1e5f-31db-9afb-fed8a57bb13b | -4.09827 | -48.25845 | 2024-10-08 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9781c700-7627-3599-83a9-89c4672350f8 | -4.09772 | -48.26195 | 2024-10-08 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c7bf1359-aa91-3104-9a86-0b041a9aaad1 | -4.09717 | -48.26545 | 2024-10-08 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dd3d6af8-11ed-3fb3-b2d3-cc11af9cc2d6 | -4.09662 | -48.26895 | 2024-10-08 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6b7f6c05-202b-3c2a-9085-c53c0cff56f1 | -4.09605 | -48.25096 | 2024-10-08 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 814d227c-d511-3e62-8615-805e787eda7b | -4.0955 | -48.25444 | 2024-10-08 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 270c6c3f-fcf1-3450-bae1-ab907b850071 | -4.09495 | -48.25793 | 2024-10-08 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2a67b827-2674-32d6-acbd-fb76cadca68d | -4.0944 | -48.26143 | 2024-10-08 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 00490d06-441e-3688-bb0e-b2ab0e1ed48f | -4.09385 | -48.26492 | 2024-10-08 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e209e2b7-0fea-330e-93ba-99965d1293e1 | -4.0933 | -48.26842 | 2024-10-08 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| eda505de-81c5-3f50-ae17-9d6abe1487c0 | -4.09164 | -48.27892 | 2024-10-08 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc79d1f9-4565-347a-8174-6b2f5215fbd2 | -4.08832 | -48.2784 | 2024-10-08 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 607c2557-3cba-3381-acfa-5d73eb5c6b4b | -3.91383 | -48.3476 | 2024-10-08 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ad6391cb-1754-3798-a9b7-c3ec9f38783e | -3.9105 | -48.34706 | 2024-10-08 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| babe7467-c740-3aa0-8532-c99e9f50f5de | -3.90994 | -48.35058 | 2024-10-08 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cad3f843-c8fb-370e-8ffc-1b644467edf9 | -3.90939 | -48.3541 | 2024-10-08 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8e26abb7-dbcb-3d0a-b3de-0b2e54fa1979 | -3.90773 | -48.34302 | 2024-10-08 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 75ae0b8c-a549-39d8-b08d-4361d1018c27 | -3.90717 | -48.34653 | 2024-10-08 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 17116987-7f8f-3736-9cc2-e752b40356e5 | -3.90662 | -48.35005 | 2024-10-08 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92f69da2-56f4-33e0-8709-b7b57ce907b0 | -3.9044 | -48.34249 | 2024-10-08 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f2eb6d4a-5d8f-3c74-a264-22c3fffef415 | -3.90385 | -48.34599 | 2024-10-08 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f0a059f0-1ca7-380b-9dfa-e04ddbbad67d | -3.90329 | -48.34952 | 2024-10-08 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e89975c5-c0ae-33dd-b5bc-89e262f1ca5c | -3.90272 | -48.35305 | 2024-10-08 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10f39794-ee28-33ef-8148-544177041f4c | -3.90107 | -48.34197 | 2024-10-08 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 691070e8-c385-34df-84f3-5ccd96fb382d | -3.90051 | -48.34547 | 2024-10-08 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4ed1953-c8b1-3817-a785-43907d43bcfe | -3.89939 | -48.35252 | 2024-10-08 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5812f19-a36b-3342-b84e-754b822a0061 | -3.89774 | -48.34146 | 2024-10-08 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0156166a-a831-3382-910c-1b6442907264 | -3.88827 | -48.358 | 2024-10-08 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ded47d59-9064-359c-845d-64099a1f6600 | -5.46168 | -48.91127 | 2024-10-08 04:32:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README51.md)
