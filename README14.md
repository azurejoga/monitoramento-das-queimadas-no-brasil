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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf60d226-837b-34f4-9fba-6f03c5ae173c | -1.20648 | -51.75167 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec80442f-566c-3309-8c11-ee79d9ce1e59 | 0.33048 | -49.72002 | 2024-11-25 04:31:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eeaeeb59-e353-3179-aaf2-d5cdc38ea6e2 | -1.10903 | -53.39584 | 2024-11-25 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 72a1a70b-7b8a-3587-aad8-19ea50215532 | -0.9857 | -51.72328 | 2024-11-25 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b0d391a7-51ba-395e-b71f-75c5d272cc71 | -0.96349 | -51.71942 | 2024-11-25 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dbd499ff-b1e5-346c-8999-29db3045f339 | -0.04337 | -50.82373 | 2024-11-25 04:31:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0e770d99-67b5-30f4-82ad-f46ebc9ff950 | -0.00403 | -51.12075 | 2024-11-25 04:31:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c30429e3-4808-3eed-ab09-973d5da5565e | 1.24231 | -50.72437 | 2024-11-25 04:31:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00cde62f-5af9-3f58-b69a-c86efdeaaa6e | -1.75497 | -45.5834 | 2024-11-25 04:31:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d0fbcb4-200e-3d1c-8a81-4118ae5ed6a0 | -1.1918 | -51.76691 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c8ed4b3-eaaa-3ca8-b8c1-0a634e7cfb09 | 1.41175 | -55.89212 | 2024-11-25 04:31:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc790f66-e5bb-3ef0-9a26-5ba853c453ff | 1.84788 | -55.90187 | 2024-11-25 04:31:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 40b0e55b-8957-3663-beb8-7d5b0a26252e | -0.34021 | -51.54226 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69c80c41-8b4e-3381-ab3b-2ace9b627bfe | 1.24617 | -50.72379 | 2024-11-25 04:31:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81968e29-7fbe-30ee-ab49-27583d6e5ee7 | -1.05233 | -51.74048 | 2024-11-25 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 471bbfe0-d293-3d0f-8f2b-7910bfb738ff | -1.25872 | -51.75624 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d04a6e91-14b2-3028-b64c-5b1e88d2858f | -1.20594 | -51.75508 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4d55eac6-5960-34a8-b1ac-8fcc9bd4f419 | -0.87706 | -51.72373 | 2024-11-25 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 277f204c-1bcb-3605-94f1-dcf5e3896a8c | -0.95951 | -51.7188 | 2024-11-25 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| afacd8b5-069d-311d-8d7c-f1ad52b9fdfc | -1.19308 | -51.76939 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3b915c73-9c0d-3624-8384-691c0cc0d39f | -0.32758 | -51.92109 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42115cf8-7dc0-326c-93e7-be544a965f65 | -0.27942 | -51.61816 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d1438df9-bc92-3c51-aa7d-00113aa27ff5 | -1.2278 | -51.79704 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 07570906-a10e-338c-8645-c6cea0f08082 | -1.24084 | -51.79203 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e77ed64d-2cbf-3020-aba3-8033451415d5 | -0.94513 | -51.65448 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0e6b59f7-274c-3895-be7c-8c8061e39ac6 | -0.33703 | -51.53653 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c93ea610-4664-3fb5-94f6-3a5e356eae8b | -0.34419 | -51.54287 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa01bfd4-9374-331a-91fd-538a375e7ab9 | -1.10644 | -52.34682 | 2024-11-25 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ddc74139-38e3-3717-8fd7-527d615a5cd0 | -0.95787 | -51.78207 | 2024-11-25 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c0507c6-25a2-3a16-8843-b240cff4bc6e | -0.36045 | -51.97782 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0f1464d0-2da1-3c46-8548-45eee08205b2 | -1.31185 | -51.75476 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4c9077f7-41fb-331c-8895-e5ff2cd168b6 | -0.1047 | -51.74386 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 757922af-0dc9-313a-80ec-057d9ea6ba6a | -1.19414 | -51.76257 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91057caa-54df-3445-9985-42d85308fcf9 | 1.41121 | -55.88853 | 2024-11-25 04:31:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5e0d70d-0303-34e8-9564-3aaac308814a | 1.33691 | -50.62228 | 2024-11-25 04:31:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| feb9dd08-adf1-375e-8825-638909fa3f9b | 0.96994 | -50.13078 | 2024-11-25 04:31:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7a2d848e-5e62-3aa7-b5b6-d98c1cdc0026 | -1.24591 | -51.78579 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb9cf2e8-6d01-3294-ac0f-adb3bd9b590e | -0.98102 | -51.71152 | 2024-11-25 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e4e83f9-9498-399d-ae28-e2f359079bea | -0.74454 | -51.94981 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 087d9ee4-1556-3b37-b8ac-7de44e167b7b | -0.87444 | -51.72573 | 2024-11-25 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e3edeee3-f6ce-352c-b090-18b4b860b5ee | -1.3023 | -51.73762 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ba46a090-244b-38c9-8a11-4e90ccd28dd5 | -1.2627 | -51.75684 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f7732db-2088-3cff-a52a-adaad53c828e | -0.96801 | -51.7166 | 2024-11-25 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6c44ec15-a3c8-30d7-aa06-94a313bf1b51 | -1.31509 | -51.75209 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fbdd5f34-8afc-39ea-9819-d321845542e5 | 0.63079 | -50.57323 | 2024-11-25 04:31:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5aac27f0-11e0-34a3-b25d-d3872b07e242 | -2.21842 | -46.3904 | 2024-11-25 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14a6a723-0fd8-3874-b507-f526bb05c874 | -0.99365 | -47.22075 | 2024-11-25 04:31:00 | NOAA-21 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04d5a200-517f-34b1-88a4-586ffcacc1a0 | -1.20251 | -51.75106 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 315e7a2a-f4b3-3265-b245-248a36d5f47e | -1.7401 | -46.29506 | 2024-11-25 04:31:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| abe80691-f89d-36bb-a5fb-029eedce848c | 1.40466 | -55.88611 | 2024-11-25 04:31:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a97e1140-fb38-3d07-8111-0f07ef44e9ff | -0.79579 | -51.80949 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 399d0cfe-441e-3c9c-8c22-462cb29ad758 | -0.95386 | -51.65059 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0a5ca8ba-1a22-3c3f-960d-48a52bfe4330 | -1.22834 | -51.79361 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| defeb3fe-c5e4-3955-b626-27fd7b2b5127 | -0.94832 | -51.63414 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8946821d-dd22-3d56-bc2a-962c6ed530dc | -1.24114 | -51.73865 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a010bf2c-e0ef-399c-94eb-c0bf76cdb670 | -0.95154 | -51.71756 | 2024-11-25 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0bdb8251-3c4c-3a06-987a-9fdb7bb421de | -1.2602 | -51.74683 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b71c6f2b-6061-343c-b8cd-92ec638c7771 | 1.85342 | -55.90113 | 2024-11-25 04:31:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98d619d4-ca5f-3505-a361-1811cc6c8890 | 0.28078 | -49.81556 | 2024-11-25 04:31:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c8c9335-bd3f-3a6e-aaab-f6cccd562fbe | -1.30945 | -51.74395 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| acc8fc3c-715b-3e9a-a606-e8a849298b16 | -0.16192 | -51.57091 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c97f77a-a5cd-3220-a4eb-2be214a08a3e | 0.95054 | -50.73746 | 2024-11-25 04:31:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd26c3b8-c6e9-3d5b-9f8f-2465ea8d49c9 | -2.11604 | -46.56613 | 2024-11-25 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae436b77-174c-354b-b0cc-4f7947182721 | -0.98625 | -51.71984 | 2024-11-25 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5d2d88d4-ac2c-323d-9b60-8e64f40d0160 | -0.0494 | -50.81033 | 2024-11-25 04:31:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 67d6629f-d0ef-3559-8cb5-f1da78430025 | -0.35285 | -51.9729 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7133f953-ec2b-326e-9bd9-541ad881a128 | -1.04835 | -51.73988 | 2024-11-25 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 01d614f8-26bd-352a-8208-531c5d447213 | -0.88958 | -51.72211 | 2024-11-25 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e28ae3ec-28dd-38c2-b3c7-229e008f2983 | -0.05173 | -50.82026 | 2024-11-25 04:31:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3c567131-b39c-3456-a211-744d10a59697 | -1.2443 | -51.74438 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9eb60109-56d0-3c52-9d4f-ade555a60453 | -1.10475 | -51.73476 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a09dff2-8401-3ff1-85f1-7a14658a2528 | -1.12364 | -52.11185 | 2024-11-25 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d5aa16f-9b26-3cf6-8ad6-26712002d31f | -2.22242 | -46.58244 | 2024-11-25 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d760e04-6fb2-3374-a69c-d8c317164ae3 | -0.24689 | -51.61673 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7e505794-d7dc-30a8-955e-90c0c0d98229 | -1.22128 | -51.73559 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 122779f8-3d30-3351-bdb8-9b10f121014e | -0.68878 | -51.87916 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ea18859-bf4a-3fbd-ab08-bcdf570d85ec | -1.14688 | -51.70022 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9b23b565-57f7-33f3-9645-f98e5f5f8ab6 | -0.88615 | -51.71805 | 2024-11-25 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91f9a526-8ac3-321c-991f-65fda4389541 | -0.95783 | -51.6512 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4f3ec2df-5cfa-329c-895c-202ff63135c6 | -1.22525 | -51.7362 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d991c89-cbec-37e5-a7f2-b6dbb6c5c663 | -0.95228 | -51.63475 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| d8c9701e-03e0-3614-a67e-21db25a62a37 | -1.11604 | -52.10697 | 2024-11-25 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 066ecbf0-f4a1-3ee8-8186-8792b4580fba | -0.76222 | -51.73682 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc97c7e3-8a4f-33bf-b7b8-13bbcc52ea52 | -2.23062 | -46.39938 | 2024-11-25 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7cf2991-6b6c-30f3-8931-316bd6b1bf3e | 1.50813 | -55.67118 | 2024-11-25 04:31:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f5f432f-b2ac-3a15-8a69-145d356b9bf3 | -0.39039 | -51.44812 | 2024-11-25 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 03dcae74-0393-3f32-a6df-c3cdaf4c6275 | -0.89412 | -51.71928 | 2024-11-25 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9b70754-9e1a-302f-acfd-0ee986fefa22 | -1.31112 | -51.75149 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e6d883ad-98ed-3d15-b90e-8662fee8d3bb | -1.20772 | -51.74399 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 18b57660-da35-341c-bf92-43f3da219454 | -1.28563 | -51.74027 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c72f6496-a7a6-373a-bd9c-fa93927c7e7f | -1.25225 | -51.7456 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b0ee0d41-23b3-3b08-b15b-144cc4451fb0 | -1.26561 | -51.76426 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 51be1b3e-ba1e-3e83-9d25-42f597a7f2ee | -2.21564 | -46.38641 | 2024-11-25 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f9b99ea-67a3-3ba1-b3d3-9f7bd8234fad | -1.30167 | -51.7344 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41577e73-3fc6-3d81-ba50-ff615d0a1cc8 | -1.19361 | -51.76598 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d761328b-e804-34b1-8d05-ac41f2bda3d4 | -1.19235 | -51.76349 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56091598-10d7-3e7b-87b7-5f00865e9110 | -1.24138 | -51.78861 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26dd2bcb-4c08-33fe-9a97-55d0dcb06193 | -2.22174 | -46.39091 | 2024-11-25 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 36d1c236-72a1-3b41-9e04-82fdc70edaf1 | -1.19866 | -51.77495 | 2024-11-25 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bd185695-f8f9-3556-9f8b-579becc686c6 | 1.38427 | -55.89616 | 2024-11-25 04:31:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README15.md)
