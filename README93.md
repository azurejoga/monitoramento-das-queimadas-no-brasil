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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37e425e8-838f-3d74-831f-07e580e0dbe8 | -9.27486 | -57.22345 | 2024-10-11 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f40b6276-a52c-38e2-9366-89d1fcdd8bb7 | -9.2712 | -56.9014 | 2024-10-11 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 19a3ef4a-c500-30aa-af5e-67936dff46ad | -9.26768 | -56.90084 | 2024-10-11 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68b0072d-98a0-394c-9418-5d37a151021b | -8.04484 | -56.3874 | 2024-10-11 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e920baf8-a9a0-33dd-a472-259208103113 | -8.04424 | -56.39143 | 2024-10-11 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5646635a-8250-3d2f-afed-3fbc4d280973 | -10.54104 | -57.71164 | 2024-10-11 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1541a48-83ae-3b48-b656-4fcc7beb80fd | -10.52555 | -57.30066 | 2024-10-11 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0493bc14-37b8-37c7-8607-cd54f2fbff7f | -10.41109 | -57.31653 | 2024-10-11 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8538914c-1f0d-3508-b4f4-899ec8cfb7a6 | -10.38894 | -57.29702 | 2024-10-11 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f06ab0e6-3081-3004-a721-a8aeae2c5558 | -10.38836 | -57.30096 | 2024-10-11 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d5fbf2ca-3701-37d5-84e5-6ca8f3ebd14a | -10.33737 | -57.50139 | 2024-10-11 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 548494f2-31b0-32dc-9609-4892affbf18e | -10.33679 | -57.50527 | 2024-10-11 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e01d6fce-e09c-3b5e-b5b6-949447f0f160 | -10.33622 | -57.50914 | 2024-10-11 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 83c55df0-15a5-3197-98ef-77018c239424 | -10.3339 | -57.50085 | 2024-10-11 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 47ec7844-7e46-3a2e-b36f-75b61d67eff2 | -10.33333 | -57.50471 | 2024-10-11 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d85fdc40-3210-3ad2-9b04-0e8af73809bb | -10.33276 | -57.50858 | 2024-10-11 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77d8deb7-ffd5-3f6d-9e8f-9a045efe1a57 | -10.32986 | -57.50416 | 2024-10-11 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d184b363-58ef-3f31-b5b7-4fe2658bb9b8 | -10.30996 | -57.967 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2c02bd8-ab55-3416-b073-a5686d807160 | -10.29581 | -57.99143 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04571fa3-9f0e-37b3-8ee1-715273c93ea1 | -10.29297 | -57.98716 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 77beabcd-57bf-3c37-b09c-5f65972bff12 | -10.29241 | -57.99089 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3def26da-6bba-3700-82df-071c674eb82f | -10.289 | -57.99036 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0c8fbe3-c580-36cb-af38-53a7ee4c78e8 | -10.28844 | -57.99409 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 01e52c64-7877-3a4e-8796-a58e8f9627b7 | -10.28007 | -57.70053 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6bc93a9b-b5a2-3046-a4b6-1f2eabdd05eb | -10.27432 | -57.71527 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 606fe1ba-646f-328c-8135-6c343b0e75d2 | -10.27088 | -57.71474 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60f1a0bc-4e78-3575-8d5a-5b33da48c67f | -10.25554 | -58.21199 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 34243d7f-2109-3456-a325-fdc51800f43e | -10.25216 | -58.21148 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b06f1fa-4229-38a9-8bc9-dbb57d996f7c | -10.22858 | -57.80879 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 521f167d-702c-3ba6-9631-d6324beaa448 | -9.96655 | -57.47826 | 2024-10-11 05:18:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 28ac185f-db35-3f2d-859c-1f7f58588c07 | -9.90661 | -57.47687 | 2024-10-11 05:18:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 327bf993-9807-3c16-939f-26985ecca037 | -9.90604 | -57.48071 | 2024-10-11 05:18:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05ec5bed-592d-3497-9e00-2c7d58b66894 | -9.90542 | -57.06559 | 2024-10-11 05:18:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08df82e5-bf18-30ab-a962-ae87e71e9af6 | -9.90258 | -57.48016 | 2024-10-11 05:18:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79718863-7e21-3b96-bf19-edfe06e3bb16 | -9.90189 | -57.06509 | 2024-10-11 05:18:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7845509e-9551-3bb7-9cf0-373a2572e514 | -9.89837 | -57.06459 | 2024-10-11 05:18:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ddd2e6ea-b7e1-3fa5-a9dc-39ef92493356 | -9.88592 | -57.49722 | 2024-10-11 05:18:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16a3171c-e28f-3903-b3a0-23f11fbb0f84 | -9.88198 | -57.5054 | 2024-10-11 05:18:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3942556d-0fb3-39ce-88d7-f31ab687117b | -9.80067 | -57.38654 | 2024-10-11 05:18:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f5a5c68-c351-319d-9bd0-7578be62131e | -9.79731 | -57.45711 | 2024-10-11 05:18:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3fab6ef5-4088-36b3-b8db-36842789cdc1 | -9.7972 | -57.38602 | 2024-10-11 05:18:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e84937f-f4d8-30db-b136-b089ec7ac3a4 | -9.79386 | -57.45658 | 2024-10-11 05:18:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 813f7fb2-af20-3d75-b659-e7b5df3d0fca | -9.68257 | -57.22292 | 2024-10-11 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 94238744-388b-3858-a559-c7f4e3649f56 | -9.68026 | -57.21453 | 2024-10-11 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6eecec07-ca18-3b52-a3c4-d700db05edf8 | -9.67967 | -57.21848 | 2024-10-11 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 75c6576a-d4de-3e75-b000-17ef3646bb57 | -9.66419 | -56.96095 | 2024-10-11 05:18:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2f9df76-171e-37c5-94b2-766ec266d783 | -9.66126 | -56.95641 | 2024-10-11 05:18:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1b53a9b-521b-34a5-9a71-e785010285a2 | -9.65832 | -56.95185 | 2024-10-11 05:18:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15ee9e48-d818-361b-b07f-6ad78196b796 | -9.65773 | -56.95586 | 2024-10-11 05:18:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06f45954-16fe-329a-ad35-8bef6d04726c | -9.65714 | -56.95985 | 2024-10-11 05:18:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a22e43dd-3b59-3232-9b29-2e4fe0e613f8 | -9.65479 | -56.95129 | 2024-10-11 05:18:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa016ff8-a96c-32b9-9418-57811a53ea2b | -9.65442 | -56.80832 | 2024-10-11 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a9cd862-da1e-3216-8a6b-162420b25b9b | -9.6542 | -56.95531 | 2024-10-11 05:18:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12ab6409-5082-38d2-b033-1175648f452a | -9.65131 | -56.70758 | 2024-10-11 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8df29b4e-f1ab-3cf7-815f-efebe7d92295 | -9.64774 | -56.70704 | 2024-10-11 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff778536-1c09-388a-9291-f5f0c32a2efa | -9.64713 | -56.71112 | 2024-10-11 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8ce4db0-93cc-3909-bbec-3bced55fd223 | -9.61901 | -56.75324 | 2024-10-11 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 09938dbd-5bfc-3bc3-a3ba-df530b76e9b6 | -9.61607 | -56.74852 | 2024-10-11 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47593d7a-8747-34a4-8316-98e039623199 | -9.61546 | -56.75265 | 2024-10-11 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ddccb8f3-ca70-3129-b240-d09c23199160 | -10.13346 | -56.77014 | 2024-10-11 05:18:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dae87d6c-9cf6-3fd7-8a36-9a0876b102d7 | -10.12989 | -56.76959 | 2024-10-11 05:18:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03543033-0167-3bf8-8a14-1e24fecef296 | -9.96023 | -58.09948 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d73f7cb-b1d3-3790-b61c-9c4dbeb2a64d | -9.95967 | -58.10315 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ccbfd11-b8af-3ba9-ba10-0c74d0480c7d | -9.95684 | -58.09895 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22c02d72-52ec-312b-8eac-ffa9c5b17cb6 | -9.95629 | -58.10263 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 563502aa-0650-3032-a80d-6c81533a2800 | -9.95573 | -58.10629 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 80e585f6-4c5f-3b20-8536-5fcf3aa79769 | -9.95517 | -58.10997 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d6f81c5e-3e83-35e0-8d30-4dc644841d0f | -9.95461 | -58.11365 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5357415a-bc32-315d-bac3-0004b1f5aabf | -9.9529 | -58.1021 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6865a68-f98f-3566-909f-cb5dad2f7dfb | -9.95235 | -58.10577 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3e7fb453-d7d0-3c4a-92ef-c73d6c518460 | -9.95179 | -58.10944 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01ff39f2-d6c9-3807-addd-6f7c283c0bca | -9.95123 | -58.11312 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 154b480e-daba-37c9-8c46-74cb8e7ff057 | -9.95068 | -58.11679 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6817fb69-6fd2-3185-a893-956521839371 | -9.95012 | -58.12045 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a2ce823-d732-31c7-a75a-7a832e7e7a92 | -9.94952 | -58.10156 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cd6b291a-5d1a-3f4e-8438-e330cdf40b4f | -9.94896 | -58.10524 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d4d6f4cc-2d9e-3d6d-9756-2bf86e826077 | -9.9484 | -58.10891 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dbdb970e-b062-3c60-8aa6-216fe3a6e588 | -9.94674 | -58.11992 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1962c08f-3fef-362c-b63a-bcabc68fdbb9 | -9.94618 | -58.12358 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f817017a-766a-375d-85a8-524b4e1f7493 | -9.94613 | -58.10104 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| daa408e3-981e-3f4e-870d-49d7900bbb60 | -9.94558 | -58.10471 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5f45ebf7-29ad-358e-9faf-5094957f4dfa | -9.94502 | -58.10839 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5a00efc0-aff4-35b2-9c6b-e2b0efd2a686 | -9.94446 | -58.11207 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8b6b0797-18b2-36c0-97ad-e4a4135d6e70 | -9.94275 | -58.10051 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb9da3ce-9a67-3e59-a646-6f573ae4f6cb | -9.94219 | -58.10418 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4adb4711-050f-33ec-a318-68ec757f2774 | -9.94164 | -58.10786 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 561d5310-07f2-3904-a3ef-c54fd61a823a | -9.94108 | -58.11153 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5d099640-390a-3157-ba7d-b200fa4435b6 | -9.93936 | -58.09998 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73c1ffb5-7716-3577-897e-d2445817a3dd | -9.93881 | -58.10365 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f0834fd4-7504-36a1-b179-e80083899ba4 | -9.91746 | -58.13036 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d79932af-2e03-33f4-ad8e-0f3d3cb7967f | -9.91691 | -58.13401 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2afaea1-4193-3206-87f7-ef00ff3e4bbc | -9.91353 | -58.13348 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc87c67b-3603-32cd-adcf-6c0d9e060415 | -9.91298 | -58.13714 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f4c83a6-83bd-37a8-b3f5-5e70af50fa50 | -9.90014 | -57.80181 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8aceb191-abb6-3cd1-b112-8a12c7e9922d | -9.89922 | -58.12747 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c3badf1-3dd4-3ea4-9ed4-ca606ef879cf | -9.8964 | -58.12328 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6d30ff6-48d8-3faf-a93c-85436b9f893d | -9.89528 | -58.13061 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d477d04d-7ebb-3225-83c8-5139383175dc | -9.89302 | -58.12277 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df44e71e-8f7f-3354-82d4-928379911968 | -9.8296 | -57.8489 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 87a32c18-b3bb-3d85-af19-861289200b7e | -9.72969 | -57.86397 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README94.md)
