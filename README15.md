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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1bcd0a40-4b95-371c-ba2e-990b5ae5d087 | -17.2933 | -57.4857 | 2024-11-10 01:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 173.3 |
| d82cffd6-f112-3cb8-97f6-328ad63a7d11 | -4.8472 | -46.9508 | 2024-11-10 01:20:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 444c4d5f-778d-37d7-8595-d1b9b9b9686b | -1.5163 | -52.1901 | 2024-11-10 01:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| ceac2ba4-831d-30d5-888f-e801c1cf7a0c | -2.5696 | -50.6812 | 2024-11-10 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 1cf9595c-e75c-3f1a-8a61-d4a44126b3d3 | -1.5531 | -52.2101 | 2024-11-10 01:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 42c8d917-966f-3cef-9ac3-de1c30688907 | -2.9494 | -52.7748 | 2024-11-10 01:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| ea4c1945-9479-3e35-871b-056e9a773458 | -3.2244 | -53.0524 | 2024-11-10 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 5cc7d9df-dca5-3323-8c1a-6852e88734ef | -3.091 | -49.4247 | 2024-11-10 01:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| e68ae4c8-d9d0-3b77-ab9b-a207e99d0648 | -3.1277 | -45.2961 | 2024-11-10 01:20:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 76.5 |
| b7a7b9e1-714c-3bf0-8d1e-11c6ee7b64a8 | -3.2169 | -50.2651 | 2024-11-10 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 0d8336c7-2dce-322c-af28-1346c96cd345 | -2.7587 | -49.3497 | 2024-11-10 01:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 68c9b22b-003a-3555-9068-ad32032e50c7 | -3.1422 | -50.4562 | 2024-11-10 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 206.4 |
| 7c23ab1f-dad4-3886-a288-1111e8600dfa | -3.9483 | -48.1724 | 2024-11-10 01:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 133.3 |
| 2d16851e-8ac6-33ba-8931-b90547212342 | -3.1091 | -45.2968 | 2024-11-10 01:20:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 8ac2e1b2-bdfa-34b2-8eeb-b86cf25f64f1 | -3.5064 | -44.0294 | 2024-11-10 01:20:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 31123f6b-f149-3029-96e0-0c44ac93d180 | -3.6003 | -47.3614 | 2024-11-10 01:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 127.1 |
| 0978bce5-58e5-3b6b-8020-11b5cc81e62a | -1.5346 | -52.2308 | 2024-11-10 01:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 88f48845-68c0-3447-a943-f5acf8c49f2c | -1.5163 | -52.2106 | 2024-11-10 01:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 105.4 |
| b0cc7189-94ce-34e5-9f5f-4a1ad10cda0a | -1.5347 | -52.1899 | 2024-11-10 01:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 52cf93ae-7777-3581-aae8-840d555705ff | -3.2352 | -50.2855 | 2024-11-10 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 233.7 |
| 29d23a51-02da-318f-a3fa-f07421b0b412 | -2.0768 | -48.8342 | 2024-11-10 01:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 364a6661-127f-3d47-ab3f-5c42c43dac0a | -3.5249 | -44.0516 | 2024-11-10 01:20:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 2a44eb0e-e0bb-3aaf-aa8b-6df1bafea5e3 | -3.1095 | -49.4241 | 2024-11-10 01:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| db8858bb-bd6b-38ac-8cc0-2c00ad935c13 | -3.6004 | -47.3395 | 2024-11-10 01:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 222.4 |
| 3f898ede-72d9-38bf-9a47-57d662cbb227 | -2.8802 | -51.4835 | 2024-11-10 01:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 7482db81-a7f5-3aea-8e15-068dac9c12e5 | -3.9671 | -48.1283 | 2024-11-10 01:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 98e11485-f20c-3438-a59b-2710be83126b | -3.9668 | -48.1932 | 2024-11-10 01:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 789c850d-8d6b-3b4c-b048-eb602bc0ba90 | -2.9171 | -51.4825 | 2024-11-10 01:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 73302cf3-bd5f-3b46-a39d-16a14a50579c | -3.967 | -48.15 | 2024-11-10 01:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 0730b7de-de75-302a-a65a-28279ecbd218 | -10.9419 | -40.8053 | 2024-11-10 01:20:00 | GOES-16 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 80.6 |
| 74ead003-931e-3753-82e1-dad052eeb756 | -4.8471 | -46.9728 | 2024-11-10 01:20:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 393.7 |
| 96ba2966-b46e-3fac-9bab-3750143194de | -3.525 | -44.0286 | 2024-11-10 01:20:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 1d1f0e76-7e56-3071-bfca-ba63bb99260f | -3.5819 | -47.3403 | 2024-11-10 01:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 01c7bd99-2eb8-3053-9d2c-84c514f8e1e9 | -2.6388 | -46.7597 | 2024-11-10 01:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 9cd4b7ad-e4e0-3825-8e30-69a088a48360 | -17.293 | -57.5062 | 2024-11-10 01:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.6 |
| 08d7b3f6-72a8-38c8-b7ae-e23848e1e3fc | -2.0953 | -48.8338 | 2024-11-10 01:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 141.6 |
| 8810a6f9-9f0a-352a-8742-b75767232a52 | -3.1239 | -50.4358 | 2024-11-10 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 154.0 |
| 4793f540-f7ab-3e9f-9b01-dd0007e95586 | -2.2076 | -48.3596 | 2024-11-10 01:20:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 6e8d480e-eb18-3300-b453-d63765d6cd96 | -3.1238 | -50.4568 | 2024-11-10 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| c9f80c1c-d649-3e9c-9c49-2dc83bb89e2c | -3.1423 | -50.4352 | 2024-11-10 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 267.5 |
| afe0ad70-0573-3a3b-89ef-f41bce58b1a1 | -2.2095 | -47.733 | 2024-11-10 01:20:00 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 9863cd8c-54a3-32f9-8750-8622322ce3b0 | -1.5347 | -52.2104 | 2024-11-10 01:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 243.8 |
| 5926fd5b-eca0-303f-a9e2-aae9ec4e4137 | -3.9485 | -48.1508 | 2024-11-10 01:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 111.5 |
| cbf2a6d2-49fa-3e32-a741-a8bbc5dc21d1 | -2.7586 | -49.371 | 2024-11-10 01:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| c08405cd-44ef-35bf-96eb-3c5484215560 | -3.4383 | -50.2999 | 2024-11-10 01:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 22423a49-ce89-3aee-b8e5-cda9c932108c | -3.5818 | -47.3621 | 2024-11-10 01:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| e7a5df0f-0b39-3f58-bfb4-65118f915315 | -2.4183 | -51.9484 | 2024-11-10 01:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 2be821f6-0281-3039-933a-6edf4e2c3864 | -4.8469 | -46.9948 | 2024-11-10 01:20:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 149.8 |
| 64797219-ebba-378f-97e6-bdfedb5d3dff | -2.9355 | -51.482 | 2024-11-10 01:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 127.3 |
| 7fff3be7-b258-32f0-b221-e45e3da94f74 | -3.2167 | -50.3071 | 2024-11-10 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 2d8a057d-dbbb-3935-bd75-77b41d064ddd | -4.8655 | -46.9938 | 2024-11-10 01:20:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 83.6 |
| f4ce2acf-835a-30d7-8f87-6d55a39f1973 | -3.3117 | -45.6706 | 2024-11-10 01:20:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 81.4 |
| d51781d8-6410-3b89-b04d-9c3dc7d8ace3 | -2.0954 | -48.8125 | 2024-11-10 01:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 875b0142-9a8b-39ae-b581-56bd33559e4b | -4.8657 | -46.9718 | 2024-11-10 01:20:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 216.0 |
| 925d42c5-0519-38e7-82b8-61b81ac26451 | -3.8413 | -44.1283 | 2024-11-10 01:20:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| b66a2835-6cc9-3b54-89be-ec2a84a34077 | -3.2984 | -52.9486 | 2024-11-10 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| e443c007-0e57-345f-a1be-0c4b710ded44 | -3.9669 | -48.1716 | 2024-11-10 01:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 187.1 |
| 1cd73e1d-9cbe-3da7-9a79-bcd87520205e | 3.81346 | -51.78768 | 2024-11-10 01:21:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5fc1ac8b-c191-3ce1-bbdf-e0e5594af878 | 2.84783 | -60.07845 | 2024-11-10 01:21:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 36.2 |
| b278bfa3-ab81-30ef-88bd-0a8594d92b33 | 3.81546 | -51.77333 | 2024-11-10 01:21:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 44400c6c-1a89-38f6-9c0e-66d954f91570 | 3.73321 | -51.62106 | 2024-11-10 01:21:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 10.5 |
| ce5ef88c-162c-3b6d-9403-78a69680c968 | 3.73438 | -51.61259 | 2024-11-10 01:21:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 8.4 |
| dcfe74ff-a284-3593-b32a-d7c69e67de9b | 2.85827 | -60.07998 | 2024-11-10 01:21:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 26fd9e9c-56e4-34c2-b130-394621daa180 | 2.84598 | -60.09106 | 2024-11-10 01:21:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 8.6 |
| c181774b-9357-36da-8845-2647348bd9c6 | 3.8155 | -51.77908 | 2024-11-10 01:21:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 32ec4533-1240-3bf5-9ea6-5658c195d405 | -2.8802 | -51.4835 | 2024-11-10 01:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 167c7708-8b82-39f0-8887-f951fd4bfd39 | -4.8469 | -46.9948 | 2024-11-10 01:30:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 128.8 |
| b1dde8df-8eff-323c-ab72-6e7adbdca572 | -3.2243 | -53.0727 | 2024-11-10 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 8b74df73-77c6-3eb2-879c-7819b09bc3a2 | 2.8552 | -60.0853 | 2024-11-10 01:30:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 7f66857f-8507-3ffd-84e1-b0953233e931 | -3.1422 | -50.4562 | 2024-11-10 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 145.6 |
| 0ae751c7-7853-313a-9f40-3a0ce262f9fa | -3.2167 | -50.3071 | 2024-11-10 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 4c714c9c-5b4a-3895-aba3-76a9eab28520 | -3.9485 | -48.1508 | 2024-11-10 01:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 70f41eba-e948-3940-9dc7-273e10cc1ab4 | -3.2352 | -50.3065 | 2024-11-10 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 147.3 |
| 4b07a55d-bbae-3d1a-9a87-071138ce3a4e | -3.2169 | -50.2651 | 2024-11-10 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 765b3451-3b3c-3a7a-b729-10b3b329d07d | -2.0954 | -48.8125 | 2024-11-10 01:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| e3b20b60-7a6b-3354-acf8-062c75f039ff | -2.9356 | -51.4613 | 2024-11-10 01:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 48b6ba52-57db-3cdb-a264-5a4288f7e3b4 | -10.9414 | -40.8301 | 2024-11-10 01:30:00 | GOES-16 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 79.0 |
| 207482aa-0740-3010-a2c6-d2fa4be2e868 | -17.6266 | -57.5281 | 2024-11-10 01:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 404.6 |
| e6ea5d7a-101c-3078-8477-e4465e7b1f23 | -3.5818 | -47.3621 | 2024-11-10 01:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 2c5dfda3-424c-31ea-bf32-7e5aa48a6d5f | -17.6069 | -57.5304 | 2024-11-10 01:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 471.0 |
| e7eef0fd-59cc-3103-a280-02585c1ceaac | -3.2168 | -50.2861 | 2024-11-10 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 236.7 |
| 42946f4a-1944-33f6-b88d-fe7c94a7ed3b | -3.091 | -49.4247 | 2024-11-10 01:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 74f28dbd-fd3d-310a-80e7-c98909cbeb75 | -3.0911 | -49.4034 | 2024-11-10 01:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| f42b69c0-c722-32e3-938b-2572e3c68c51 | -3.9483 | -48.1724 | 2024-11-10 01:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 122.0 |
| fa50c160-aaa3-3db8-b36c-2967232d5f86 | -1.5163 | -52.2106 | 2024-11-10 01:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| a3a43ba6-2b1c-3a58-86de-d6bbfcba04a0 | -3.1423 | -50.4352 | 2024-11-10 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 242.7 |
| 32f9813f-f7c2-3d58-b2c7-9e838b168f58 | -3.6004 | -47.3395 | 2024-11-10 01:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 189.8 |
| f0dc5926-5192-36b3-aff8-fd83e85d049f | -3.6003 | -47.3614 | 2024-11-10 01:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 127.7 |
| 109dfa3e-8757-334f-abb4-a2502f88251c | -2.2075 | -48.3811 | 2024-11-10 01:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| c295ff63-6267-31cc-ae7a-36c085d5b3bf | -2.9043 | -45.3719 | 2024-11-10 01:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 49509d8f-db55-345a-9f37-cc88c32415bb | -2.931 | -52.7753 | 2024-11-10 01:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 9ee8f104-0dff-36d7-a759-86e31e56ef23 | -2.5513 | -45.3837 | 2024-11-10 01:30:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 85eebc8d-2fd4-39ad-aad3-33e91d7622f1 | -2.0953 | -48.8338 | 2024-11-10 01:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 162.9 |
| bc8ae17c-5942-3775-a5dd-c122ffb7e3fd | -2.9494 | -52.7748 | 2024-11-10 01:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| fb4eb365-b1c3-30b7-8f63-a7ce2dbfa332 | -3.8413 | -44.1283 | 2024-11-10 01:30:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| e697ae62-a7cc-3aa3-8448-411c9e403995 | -3.5819 | -47.3403 | 2024-11-10 01:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 6cc1e893-394b-3a9b-8e6f-b9abdd287e30 | -2.9355 | -51.482 | 2024-11-10 01:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 102.1 |
| fe1f309c-6ab3-3ede-a166-24ace21eb285 | -17.6073 | -57.5099 | 2024-11-10 01:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 366.8 |
| 48413841-f7cd-3194-9453-7814642e095b | -4.8657 | -46.9718 | 2024-11-10 01:30:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 161.1 |
| 1289c784-2d96-3870-bf1e-34f349194b9c | -3.3117 | -45.6706 | 2024-11-10 01:30:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 74.5 |


[Clique aqui para ver as próximas entradas](README16.md)
