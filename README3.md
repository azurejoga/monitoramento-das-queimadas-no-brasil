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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9851560c-122c-3d89-a1a4-e9d766edb24c | -9.41628 | -48.46101 | 2025-06-08 00:58:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e69a0c5c-1f33-3f3c-a552-a9bc863e20b7 | -12.3636 | -57.416 | 2025-06-08 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 4ca4a8ff-ded3-3ab8-a283-4d954d38e4f3 | -12.3638 | -57.396 | 2025-06-08 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 448e941e-f2b3-303f-811e-b729408c8eea | -7.0169 | -44.5954 | 2025-06-08 01:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 603248b4-ec12-305e-9dda-f3dcb8077216 | -4.41491 | -47.66664 | 2025-06-08 01:00:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 1c12d1ef-3c8b-3b31-8739-0cf2f34fce90 | -12.3828 | -57.3944 | 2025-06-08 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 175c1af4-b51f-36d0-bf60-138e7ed94a39 | -12.3826 | -57.4144 | 2025-06-08 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 673ecd6a-a2a8-3dfa-8cb0-d1cb054c5510 | -7.0169 | -44.5954 | 2025-06-08 01:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 86e7a9f1-beab-3741-b51c-f8b753ca36b6 | -13.8857 | -56.209801 | 2025-06-08 01:15:00 | METOP-B | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 86914b8b-bf70-38eb-abe7-c017337e1b82 | -12.3641 | -57.3936 | 2025-06-08 01:15:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ead1f8e9-322d-3556-99af-2baca5992ec3 | -12.3665 | -57.403702 | 2025-06-08 01:15:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ad39b52a-3bfb-3288-b190-34cc09254261 | -11.5457 | -56.447601 | 2025-06-08 01:15:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a0011b64-7b7e-3118-aa67-3d629038094d | -13.4708 | -56.840698 | 2025-06-08 01:15:00 | METOP-B | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| be63023e-b4b0-3303-8249-64f716a3d9be | -11.1172 | -54.635201 | 2025-06-08 01:15:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4be0bea9-c1af-3cc3-8761-2346dad93a88 | -13.476 | -56.861801 | 2025-06-08 01:15:00 | METOP-B | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 458e0cac-1d61-3c67-b6fc-027395204173 | -12.3738 | -57.391102 | 2025-06-08 01:15:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2328d3b1-deda-3649-a18e-d5c13aceb1ae | -12.3762 | -57.401299 | 2025-06-08 01:15:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c6d0ae9b-2b6b-367d-9445-69631d51905c | -11.5486 | -56.459499 | 2025-06-08 01:15:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7f174c90-7272-3c47-94a1-c21d0970c910 | -12.3786 | -57.4114 | 2025-06-08 01:15:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f71064f5-c526-3524-9b3c-85fb3324330d | -12.5222 | -58.3601 | 2025-06-08 01:15:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3c45d082-7e46-3f9d-b806-55087ffa4fab | -11.1212 | -54.651001 | 2025-06-08 01:15:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d40c290e-1920-38be-96cf-5a8c486f7027 | -12.5278 | -58.339802 | 2025-06-08 01:15:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6d5f8c0a-c5a7-3825-95a5-d5c12e5c32ad | -6.5692 | -51.1231 | 2025-06-08 01:15:00 | METOP-B | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f58ab54a-182c-3d86-b950-59d9dcc7eb6f | -12.5299 | -58.348801 | 2025-06-08 01:15:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e45fa296-9bb8-39fc-b976-dc65e9331784 | -6.5788 | -51.120602 | 2025-06-08 01:15:00 | METOP-B | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 202a803c-4efe-3d2b-869e-bc432c6fd956 | -13.8829 | -56.198399 | 2025-06-08 01:15:00 | METOP-B | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6ff89f35-62a3-37e2-9362-b176a00c0cca | -13.4734 | -56.8512 | 2025-06-08 01:15:00 | METOP-B | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9183e344-a152-30d5-b018-a8a2c84aa4ab | -11.3752 | -56.5532 | 2025-06-08 01:15:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d7b86c27-5ae5-3a58-a813-18b3234750ae | -11.1269 | -54.632702 | 2025-06-08 01:15:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b8a954a1-091c-3cc2-b117-33b1fbcea06b | -12.532 | -58.3577 | 2025-06-08 01:15:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 442d7de0-498a-392c-a48b-2e2aa01c820c | -7.0169 | -44.5954 | 2025-06-08 01:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 6699ffa9-dc51-3a5a-a9cd-cb895b6b46f6 | -12.3636 | -57.416 | 2025-06-08 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 8058cf97-148d-37c0-9115-ef5c8862c424 | -12.3638 | -57.396 | 2025-06-08 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 42d91742-e903-38bd-8660-0e86d183a519 | -12.3826 | -57.4144 | 2025-06-08 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 04547ad2-105b-352c-b25b-ee8f0a656795 | -7.0169 | -44.5954 | 2025-06-08 01:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 76d0677c-472b-3eb0-844a-741296c79b36 | -12.3826 | -57.4144 | 2025-06-08 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 319062df-629a-396f-b63d-074466f7c8e4 | -12.3828 | -57.3944 | 2025-06-08 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| be597d79-7fd9-3a04-a1ae-56b560537230 | -12.3826 | -57.4144 | 2025-06-08 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| f3a2b319-05bc-395e-9267-f0deea82370b | -7.0169 | -44.5954 | 2025-06-08 01:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 348d8f2d-ba5d-3678-80b8-5e379a5c0f17 | -12.3636 | -57.416 | 2025-06-08 01:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 15bb35ad-4995-3260-86e4-1702fcacf882 | -7.0169 | -44.5954 | 2025-06-08 02:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| b4cc03fe-91db-3a87-8375-f4284f06af1b | -12.3826 | -57.4144 | 2025-06-08 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 46.0 |
| da7d7485-7608-3de1-bce8-ddbda219446b | -7.0169 | -44.5954 | 2025-06-08 02:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 7a8ca201-6ddf-3267-9de6-66d930c3a95f | -12.3636 | -57.416 | 2025-06-08 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 93681090-c3fb-3caa-a4e9-609d38ce38b3 | -7.73006 | -44.16607 | 2025-06-08 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 79d19e27-c3fe-391c-b308-f4d1897aa01b | -7.72936 | -44.1699 | 2025-06-08 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7ac74c4a-47ba-3859-9716-7bb9ed2ad829 | -7.02176 | -44.59704 | 2025-06-08 03:36:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| fd580f22-c4d5-31fb-b8a9-40fddfa4ecfd | -8.4093 | -47.05189 | 2025-06-08 03:36:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6387fd1a-35de-379b-a4f7-de53bcd29c49 | -6.4463 | -45.72663 | 2025-06-08 03:36:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9e19a59c-ce9b-3b21-8d31-54f3a7a82151 | -7.73993 | -44.17603 | 2025-06-08 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| eab24c9d-e244-36c9-a72f-15a3b91dede3 | -7.72792 | -44.17769 | 2025-06-08 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 46a9a019-5e54-325e-abed-2bd2919de200 | -7.0233 | -44.58858 | 2025-06-08 03:36:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 17fd96d4-2d89-37d0-84a5-d6816e8e5733 | -6.45038 | -45.72887 | 2025-06-08 03:36:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7b2691d0-7b04-3047-8330-dde7020e5ee1 | -6.21439 | -43.34066 | 2025-06-08 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 12797c26-ebec-3273-bb55-1bf693e0c084 | -4.48854 | -43.77561 | 2025-06-08 03:36:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 968d5209-5f3f-396b-9e1c-4c6d24cdfe40 | -6.44531 | -45.73195 | 2025-06-08 03:36:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1aedc02b-9df4-3095-9183-e6136ba873f7 | -7.7343 | -44.17482 | 2025-06-08 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1c1a6a28-76d5-360e-a23a-3fb35e3c99ce | -7.01433 | -44.60441 | 2025-06-08 03:36:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 978d32c2-38e1-3442-900c-b94fe7fb8685 | -5.57646 | -45.20212 | 2025-06-08 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4a216210-97d6-3eb7-8037-1eaed5685fc4 | -5.63314 | -43.72134 | 2025-06-08 03:36:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 60b44501-b536-3d4f-a266-69b4c03999e5 | -5.07226 | -37.71519 | 2025-06-08 03:36:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8578b923-b39d-3cb3-bc81-57c271dfeb18 | -5.77998 | -43.6126 | 2025-06-08 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 03ffab1e-6018-3abe-8239-8fbbf7921eb0 | -7.73358 | -44.17872 | 2025-06-08 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d787020d-1747-3fb9-a949-97c43bbacf68 | -5.63516 | -43.72115 | 2025-06-08 03:36:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e04e6af8-532d-3f7d-afd9-c11ec5ae5689 | -9.43746 | -40.34637 | 2025-06-08 03:36:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1e1d1a6d-9f62-30be-9888-be8c811c29a6 | -6.21376 | -43.34432 | 2025-06-08 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0ea8c94e-44f0-3b9b-9002-1f109ced9db3 | -7.02567 | -44.57559 | 2025-06-08 03:36:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 47cf0560-eccb-34d4-93c2-0dcc4d6d72fc | -7.73569 | -44.16724 | 2025-06-08 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 1203ad03-dc39-349e-ba7f-3d82c4fead82 | -7.73852 | -44.18369 | 2025-06-08 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4d46fd1e-85f2-3497-9bbe-1d06565035a3 | -5.47154 | -44.70078 | 2025-06-08 03:36:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fac1d0c3-286b-3223-aa91-ea7089dfbf22 | -5.64228 | -43.71414 | 2025-06-08 03:36:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 878753dd-ede9-352c-a251-c46cbdc20e8e | -5.77859 | -43.62037 | 2025-06-08 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 02c9cf46-e35c-3f3a-8fb0-d2a5458380c2 | -6.44943 | -45.73421 | 2025-06-08 03:36:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b48e2596-6956-3f77-8062-b4ea2bf45c8f | -7.86949 | -47.89546 | 2025-06-08 03:36:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| aca3336d-d538-3452-993c-feb8526c19cc | -7.86813 | -47.90262 | 2025-06-08 03:36:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b74e0465-e5de-394c-abf6-2b0a06206199 | -6.63982 | -47.35118 | 2025-06-08 03:36:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8e8a36ff-a053-36f5-bf54-15efd511e725 | -7.00914 | -44.59956 | 2025-06-08 03:36:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 55b8b1a6-f7a8-3a8c-9910-69908d5d13f1 | -7.73286 | -44.18264 | 2025-06-08 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b6ffba7a-853f-3ec6-b087-5e4de6e12f2c | -5.63442 | -43.72527 | 2025-06-08 03:36:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6413bde3-9a6c-3049-adfc-daa652591dea | -7.86514 | -47.90237 | 2025-06-08 03:36:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0446a861-92d6-30fa-8c7e-44c3c758eb90 | -7.02488 | -44.57996 | 2025-06-08 03:36:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5728014a-26df-31fa-a7f2-2f4de53794be | -5.77929 | -43.61646 | 2025-06-08 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 62476776-addd-3d66-9ea7-de09d042fac1 | -6.88134 | -47.24105 | 2025-06-08 03:36:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8d23f19d-92a2-34cd-9dcc-aa9a03d4aa89 | -7.86242 | -47.89417 | 2025-06-08 03:36:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 54b64226-6e7b-3a2c-82f5-f5f25fdc3dc5 | -7.8736 | -47.89661 | 2025-06-08 03:36:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7cdbd177-ffbf-30b9-b518-7f8d16c3c5b4 | -6.45263 | -45.72799 | 2025-06-08 03:36:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67d2c5a6-dcb4-315b-a707-ab927cb4c188 | -7.7378 | -44.18761 | 2025-06-08 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| abfd95ef-542a-3beb-be90-1c067ab533bc | -7.18664 | -42.81364 | 2025-06-08 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b9e80c55-5e3b-358e-87a3-9b68ac40d75e | -5.63243 | -43.72547 | 2025-06-08 03:36:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4a2f3088-b766-3f55-9beb-64b214e6b58a | -7.86654 | -47.89524 | 2025-06-08 03:36:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e57c187a-8c43-3fe9-9bd3-811648bed468 | -7.86106 | -47.90131 | 2025-06-08 03:36:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d24939e8-26bf-3acb-9f37-ebc9d2a231e6 | -7.01665 | -44.59176 | 2025-06-08 03:36:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7d3d6516-2fde-331a-ae1a-76fc48e79631 | -7.11051 | -43.70212 | 2025-06-08 03:36:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e1354405-95e8-3530-afdd-7d202f179933 | -6.87324 | -47.24606 | 2025-06-08 03:36:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f9d0d6de-5607-395d-ac9c-ce21f8ff5767 | -7.02254 | -44.59278 | 2025-06-08 03:36:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ad18e894-480f-3817-9044-08006eb34e63 | -8.59022 | -45.86845 | 2025-06-08 03:36:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cede9174-163c-3891-bc33-fe7f0ab14b85 | -7.01511 | -44.60017 | 2025-06-08 03:36:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1df08f8f-7cc8-30f1-b550-3767f5393be8 | -7.01941 | -44.60996 | 2025-06-08 03:36:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9293e8ff-e0cc-3b53-ad24-84970d784ba8 | -7.01589 | -44.59592 | 2025-06-08 03:36:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d51792b7-ce5f-37c5-b83c-acc57fc08bee | -7.72864 | -44.17377 | 2025-06-08 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |


[Clique aqui para ver as próximas entradas](README4.md)
