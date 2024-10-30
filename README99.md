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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a9f19a6b-9d4d-38f2-ae49-03338a88b6ca | -0.69663 | -63.20395 | 2024-10-30 05:59:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 289da391-5aea-33ab-b12d-09c77010f868 | -0.15775 | -60.86567 | 2024-10-30 05:59:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 60ea5086-a47c-33ae-b4ee-3917025752a2 | -0.15406 | -60.86475 | 2024-10-30 05:59:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f9d10bd9-aafa-3038-96a4-49f1fc6c84e2 | -0.15291 | -60.86487 | 2024-10-30 05:59:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a90e1086-c41c-3243-8040-c69d0314d421 | -0.14726 | -60.86943 | 2024-10-30 05:59:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6575fd8-af3b-326c-9421-1d2b6b23b958 | -9.96331 | -64.93784 | 2024-10-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da0f831a-cece-368b-a18a-5d643a975085 | -9.81311 | -62.70662 | 2024-10-30 06:01:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| abe3f322-6a28-3497-8298-9c5771975ce3 | -9.80817 | -62.70586 | 2024-10-30 06:01:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a320d83a-e98d-3a56-85a6-6009cc07ae26 | -9.72546 | -63.22768 | 2024-10-30 06:01:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc9b507c-7d26-3c5b-ae31-282fef3f8d22 | -9.65166 | -65.74094 | 2024-10-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ff119a30-3137-3c57-a32d-32d36dadec94 | -9.64765 | -65.74035 | 2024-10-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3cf1d5cc-b2cf-3609-8819-0b229450dca6 | -9.55714 | -63.13298 | 2024-10-30 06:01:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| edc6dba8-6229-3156-99f5-17b162051016 | -9.55643 | -63.13829 | 2024-10-30 06:01:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c22ef985-1584-33d1-ac0b-ff8db6a6a152 | -9.54517 | -59.44189 | 2024-10-30 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c5d6b90-3963-371f-b806-fb5313e22e5a | -9.54032 | -66.65061 | 2024-10-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fb520c8-cb6b-3dd6-867b-e38775254713 | -9.53654 | -66.65003 | 2024-10-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37932db3-4db0-33ee-8b93-63e1b9c28597 | -9.51771 | -62.42493 | 2024-10-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d5d1618-a9c5-3183-b18e-3941954e812e | -9.51422 | -65.5981 | 2024-10-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 54a2edfd-6c11-3d06-b93e-4e2de500f37a | -9.50361 | -64.42357 | 2024-10-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d61888ac-d1b9-3348-a01a-bc745eec64a4 | -9.50026 | -62.2899 | 2024-10-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2971664-3ef8-3d39-8c2a-6cd09ca5bc18 | -9.49253 | -64.4393 | 2024-10-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fdc52e4f-3923-3572-96ea-dfa90a9e397a | -9.49195 | -64.4435 | 2024-10-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5fb0ab4-39a8-350f-8fc3-435ea3025cf8 | -9.37818 | -64.45532 | 2024-10-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| acac62bc-466b-35f1-8f41-a8b7fcd1030d | -9.32077 | -64.25135 | 2024-10-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ae014ea-c110-3976-8a63-e30699bb4640 | -9.16162 | -68.34643 | 2024-10-30 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c59d1e5-801f-3ecb-9dbb-ae2d9d7f0508 | -9.16025 | -63.17536 | 2024-10-30 06:01:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bff526e2-9e16-3647-a03e-5cd7eaba8f9c | -9.1555 | -63.17471 | 2024-10-30 06:01:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fee290a5-649f-3c88-8010-2b18efe138a3 | -9.1553 | -59.41707 | 2024-10-30 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb801d10-570e-3064-9b78-a5c4d8b1714b | -9.01257 | -64.36552 | 2024-10-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6353eee-ea15-3ad8-afcb-6472b775d3c5 | -9.00974 | -64.41664 | 2024-10-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 494875cd-6f0c-3736-a480-8b6464244b3b | -9.00822 | -64.36488 | 2024-10-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02026370-b7be-3318-82da-1a8bbdc8b782 | -8.86449 | -64.23769 | 2024-10-30 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 92d14cd7-e761-3659-b9bb-260be764ce6d | -8.8639 | -64.24197 | 2024-10-30 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| db228e28-e75e-35aa-88b6-e0439242c7ab | -8.86011 | -64.23701 | 2024-10-30 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 03368aa5-af53-3b1f-8ae6-e4ac82947c38 | -8.85952 | -64.24129 | 2024-10-30 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec36109d-f9ba-3f9a-8f6f-a72cdf18f7ad | -8.85893 | -64.24559 | 2024-10-30 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 31d9b195-8304-3cd3-95cc-1acb89a73a20 | -8.83383 | -64.26167 | 2024-10-30 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 968b6cf7-f526-3842-98fd-7596127915cd | -8.82971 | -64.26326 | 2024-10-30 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4c2e533-0241-344c-8917-0c0841115618 | -8.7145 | -63.32038 | 2024-10-30 06:01:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22ecd65a-025a-3987-b3a5-1e487a3db052 | -8.59779 | -63.86014 | 2024-10-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ccb2593-5a14-36bc-8323-e17a1e0472da | -7.88574 | -63.71883 | 2024-10-30 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf05c9b5-4e13-3106-9b08-465fffe8eb91 | -7.79552 | -72.73045 | 2024-10-30 06:01:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e502da17-b12a-37e4-91bb-ce0b97333e37 | -7.6611 | -63.4533 | 2024-10-30 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a66a3d9-35fb-3272-8d43-c4844eec9918 | -7.65656 | -63.45264 | 2024-10-30 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 835d3385-6bc7-34ca-b3f7-97607919720a | -7.53276 | -70.16402 | 2024-10-30 06:01:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 969afba7-4ba7-3d9c-8522-932b50c537c2 | -7.52946 | -70.16351 | 2024-10-30 06:01:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7eac36d-13c1-3897-9515-f2c1a7667858 | -7.39423 | -72.65085 | 2024-10-30 06:01:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1dfee991-4bd1-37e7-a892-79b241210f3e | -7.02573 | -71.79727 | 2024-10-30 06:01:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0c6f1944-6759-305d-98b8-dac4935990ac | -6.92073 | -71.49124 | 2024-10-30 06:01:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3dfb7276-3ea6-37c4-8562-8ad71e03a325 | -6.90328 | -71.51418 | 2024-10-30 06:01:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6a6be596-359b-32ed-98ca-dff94b4aadff | -6.80818 | -63.1529 | 2024-10-30 06:01:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4fb2910-25dd-33f1-a184-9aa2d1f87f38 | -3.61599 | -58.55136 | 2024-10-30 06:01:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2fdad362-ee2f-3458-8974-f647860af4ab | -10.16405 | -64.25637 | 2024-10-30 06:01:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 640606f6-e258-3119-b7a8-413a1991ae11 | -10.09094 | -62.17286 | 2024-10-30 06:01:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3777e1f1-8f70-300c-b9ea-ad4e6d1e4ac6 | -10.09054 | -62.17599 | 2024-10-30 06:01:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a86a8139-b606-3bef-b449-9c3f8511c61f | -12.03043 | -64.04396 | 2024-10-30 06:03:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8476a95-061a-3be4-b4c2-6aefdf17347e | -12.02577 | -64.04332 | 2024-10-30 06:03:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2af9af6f-f4ba-3769-866c-a879ece600b8 | -10.91889 | -69.45625 | 2024-10-30 06:03:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ddc44f4b-c849-3b23-903b-a23679d8db5a | -10.91551 | -69.45572 | 2024-10-30 06:03:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 63084c7f-f1c1-3155-b1d1-b5a1f805ff93 | -10.71699 | -69.39955 | 2024-10-30 06:03:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74c2ae87-c033-372d-b2a2-970e0fee164a | -10.68807 | -64.99955 | 2024-10-30 06:03:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 225c0b5f-00a8-3546-a8a6-fdff9abdf859 | -10.47518 | -69.74059 | 2024-10-30 06:03:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 642b0147-a1da-3a3d-a8fe-e56b60e90300 | 3.5448 | -51.2772 | 2024-10-30 06:04:46 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 9f892227-48d3-379c-b5a9-05fe65471735 | 1.7483 | -55.8428 | 2024-10-30 06:04:56 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 61c591f7-4e8d-38cc-a3c7-fd54893d65c5 | -2.833 | -49.2413 | 2024-10-30 06:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 85971395-6bc7-3dc7-a109-0c25d407dcad | -3.0913 | -54.287 | 2024-10-30 06:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| cde45a48-1dc4-3ae9-a2e8-88e1a35fe023 | -3.1097 | -54.2865 | 2024-10-30 06:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 73a571a5-025d-3125-8197-bbc7649759e4 | -3.1098 | -54.2665 | 2024-10-30 06:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| fee991ed-000f-3ab2-b7ca-b063fab198f6 | -3.1281 | -54.266 | 2024-10-30 06:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 0ba0e54a-7021-3ef2-b4d3-725bbba5391c | -3.1787 | -50.5807 | 2024-10-30 06:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 0c135619-7cf9-3e34-97ce-b5c59416e51c | -3.2534 | -50.3689 | 2024-10-30 06:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 81fa0415-0ad2-384c-b461-72a5827dabb1 | -3.2535 | -50.3479 | 2024-10-30 06:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 106.0 |
| f2817fe9-8310-350a-b1ff-4d00b4546143 | -3.2718 | -50.3683 | 2024-10-30 06:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 2b73889a-5805-3c86-8cd7-a3dcefba6673 | -3.2719 | -50.3473 | 2024-10-30 06:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 8f056373-3085-3c38-87a6-bd323f7ce797 | -3.9486 | -48.1291 | 2024-10-30 06:05:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 0644b882-d8f9-3225-b66c-9ab8404315a7 | -4.2681 | -50.6669 | 2024-10-30 06:05:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| a962eed4-582b-354a-8b94-7e1e53a0b020 | -2.833 | -49.2413 | 2024-10-30 06:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 1c911afd-f021-3e65-9e7b-761a4cbb6481 | -3.0913 | -54.287 | 2024-10-30 06:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| cb38eef5-5f40-3c5c-a8e5-534114b3c18e | -3.1097 | -54.2865 | 2024-10-30 06:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 5d51b76a-2bf5-347e-a458-c149fb6dca55 | -3.1098 | -54.2665 | 2024-10-30 06:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 60f718b7-b04b-3fe8-a03a-6b9a4806b260 | -3.1281 | -54.266 | 2024-10-30 06:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 46474331-f617-3ff1-afda-020094c6d138 | -3.2534 | -50.3689 | 2024-10-30 06:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 7fa2059d-c49e-334d-8f82-0c59399701b9 | -3.2535 | -50.3479 | 2024-10-30 06:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 126.2 |
| 84c7fecc-1aaf-3322-bbab-c11ffb86e467 | -3.2535 | -50.3269 | 2024-10-30 06:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 0508a459-e995-37d2-bdcb-f33ebdadb185 | -3.2718 | -50.3683 | 2024-10-30 06:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 169cf1e0-4c2c-3198-b59e-e7cac066b501 | -3.2719 | -50.3473 | 2024-10-30 06:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 111.3 |
| b9d1c025-4ee3-3452-8fd2-2d97b1f88ea3 | 3.5448 | -51.2772 | 2024-10-30 06:24:46 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 1a5a7c2f-6184-3e34-9eed-55a1fe9bcf2c | -9.55841 | -63.13477 | 2024-10-30 06:25:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c42b1b36-80b8-34d1-8658-1234bcde5103 | -9.55751 | -63.14209 | 2024-10-30 06:25:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9c01792-3aaf-3e51-8892-e76aa26d295d | -8.86341 | -64.23872 | 2024-10-30 06:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9730f280-0014-33ef-bd78-d9629188b95d | -8.86271 | -64.24454 | 2024-10-30 06:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c96a38dd-71cc-33f0-9974-d84bacd058fe | -7.79578 | -72.73072 | 2024-10-30 06:25:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4fd78ebd-0e6b-3af6-9488-b6d271360dbb | -7.53218 | -70.16251 | 2024-10-30 06:25:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 44d516f3-5f38-3ab4-ba3b-1788b9b69701 | -6.91925 | -71.49149 | 2024-10-30 06:25:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6cf51c61-63e0-387e-a6e9-0eab1f47a6d3 | -10.91547 | -69.45583 | 2024-10-30 06:25:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ebb4428c-c294-3389-8bdb-48a8ddcc7a80 | -10.69096 | -65.0006 | 2024-10-30 06:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c25f4797-6414-301b-a929-b5093d6d5236 | -10.68444 | -64.99963 | 2024-10-30 06:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 56e20d48-d0b9-364c-9c84-5f2fe364c678 | -10.47485 | -69.74155 | 2024-10-30 06:25:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f2c8780-21d6-3c86-a861-94adb390fb85 | -8.86041 | -64.24191 | 2024-10-30 06:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 68ed0441-e112-3b5b-8910-717dbfed4649 | -2.833 | -49.2413 | 2024-10-30 06:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |


[Clique aqui para ver as próximas entradas](README100.md)
