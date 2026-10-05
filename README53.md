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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ac92c98-10eb-3231-9105-c384d182db39 | -2.78494 | -54.09534 | 2026-10-05 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e7d13577-c641-38b4-bd55-43a03376e69a | -2.82476 | -54.11028 | 2026-10-05 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb10e2da-e735-3106-82f4-2cacfcf4d013 | -1.62707 | -55.1319 | 2026-10-05 05:42:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bded6d73-3732-3b31-869b-5ad077bd9e68 | -2.99013 | -51.04806 | 2026-10-05 05:42:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 319f3091-5948-3930-92c5-b3aafe0dd2aa | -3.10848 | -53.73523 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d4796e10-18e3-3e05-a540-8d3f9f9e7726 | -3.5206 | -54.62588 | 2026-10-05 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ccb019fe-b13a-3c44-9cb8-9876bf7c5a3e | -3.50516 | -54.61134 | 2026-10-05 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| be5746d0-85c4-399b-b27b-6a8ad72f4c19 | -3.1057 | -53.74282 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1ed9af17-261e-3278-a319-8a716cf617da | -2.21923 | -53.70668 | 2026-10-05 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5a79728f-edf9-3d58-9c85-b0f0fd55b457 | -3.04646 | -54.21843 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3cb5826a-03d1-3762-862a-bf4ff33bc92f | -2.8203 | -54.13258 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2fa4b360-8ca9-3b12-9cc3-01a832441eda | -1.98164 | -54.41875 | 2026-10-05 05:42:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| aa616f8e-e813-3df7-918d-0280dc621c98 | -3.09898 | -53.71516 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 820f3670-2929-3e04-82f8-a5cdff1fafbc | -3.09834 | -53.71968 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| e8b7438d-ebe7-3826-9a4e-606c3b8da3b9 | -3.32154 | -53.85225 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c26e817c-4502-3f89-a6f6-01517a49d4c0 | -3.11505 | -53.76275 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| c1d48b63-8f90-316e-9394-eab549df43de | -2.98864 | -54.04011 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 71ba980e-33a0-3707-91df-2ecd7745c776 | -2.54387 | -65.87245 | 2026-10-05 05:42:00 | NOAA-21 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b4538e5-40b0-35ba-9379-36f0f6d9cf15 | -3.17429 | -54.07897 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 616208a7-e149-3d19-8203-5b00698c73e0 | -3.11322 | -53.74526 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 80c2d0ed-0c24-3d31-82ab-96d368ce24a4 | -3.5903 | -54.3139 | 2026-10-05 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c007d08b-6340-3ad0-902f-c2c239919f54 | -3.10116 | -53.74334 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e3895fc5-a535-3ade-96af-4d28e8531825 | -2.9111 | -54.08633 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3ab77967-b743-3d25-ae26-c112062074dd | -1.88166 | -56.28122 | 2026-10-05 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 79f69a6a-5525-3776-9048-bb99cf53defd | -3.08072 | -54.18256 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 99b02bc7-d58e-302f-87c5-c5a507718541 | -3.1184 | -53.70896 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d0e8ccf6-a57a-36c2-82c2-6d5fabd998ea | -2.80066 | -54.11088 | 2026-10-05 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f5a5306-b052-3cf8-8cf1-e74adb2c32ec | -3.12252 | -53.71301 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 90a38120-d737-3f7f-a288-91210a3a5cb3 | -3.51546 | -54.62099 | 2026-10-05 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92fb8123-f2de-3e5b-b16b-da4cbded5fb5 | -3.05911 | -54.16603 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 70b4ed09-20f3-353c-bbc7-cd07d4fe8644 | -3.13458 | -53.72541 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 80c0b0f4-1ef0-3306-8344-d6dc81c216ed | -3.50725 | -54.60681 | 2026-10-05 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4d6307e9-995b-3fd0-a20a-975cc7672e92 | -2.89994 | -54.08033 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a9a7815e-0bfd-365f-ba4c-623566693853 | -3.10052 | -53.74783 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 906f7a55-c4ae-3d35-96f4-e3b6077253c5 | -3.10637 | -53.7383 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b6fec105-2ce2-3681-a9f5-efc3deb1326a | -3.12652 | -53.72754 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5bbfd39-5516-3550-adc5-e6f67b4b961a | -3.10526 | -53.7579 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 786ec735-a8f0-3556-9c33-d77ab4d14f80 | -3.11912 | -53.73567 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3975784-065e-3008-a46b-ed57e904c294 | -3.00736 | -53.86871 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73c8f795-a606-35ac-987a-d61fe5df001a | -3.87315 | -55.80996 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5e4c59f-72ef-3349-abcd-fdbc6f4ad777 | -3.12444 | -53.70991 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ba7e0d21-d04d-37f7-b476-6bca830972ce | -3.12184 | -53.71755 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8565d263-c6f6-3729-a2b5-4e9386a7b007 | -3.51999 | -54.62991 | 2026-10-05 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| edaaa5f8-7587-3c42-bb39-55b9b28fa8f8 | -3.86059 | -55.83276 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 730970c5-4e67-395f-b88d-5a1aacc80992 | -3.51212 | -54.604 | 2026-10-05 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0776f06a-ca87-3687-a175-7031da40b26d | -3.10502 | -53.74734 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 540db099-a796-3d87-8126-89338531e542 | -3.10908 | -53.72017 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a12def30-fa1a-3af2-a21c-fe3298652d53 | -1.61751 | -55.10639 | 2026-10-05 05:42:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0f43c9a-7b08-39b4-bc6b-8b85a19005ff | -3.10244 | -53.73428 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 34f4eec3-20bf-37b3-9195-d9c43bf4c581 | -2.95571 | -59.15702 | 2026-10-05 05:42:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a715da2-cd8d-3096-a26a-550add64b5ba | -3.1097 | -53.75731 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 51e58459-525b-3eaf-a173-854a441fc615 | -3.0721 | -54.15915 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| e520f581-e96c-32d2-b466-61562a6d6e13 | -7.22194 | -55.20052 | 2026-10-05 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aec94e28-6f29-3853-9133-b51c2e703b08 | -3.12925 | -53.70939 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| de63e530-9e66-3232-bed3-2c57f52feb69 | -2.16406 | -53.66621 | 2026-10-05 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4e506744-0ae7-3247-987b-624e0b478f08 | -3.06436 | -54.17121 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| bab63b92-07ef-3703-87be-71d80f1e683d | -3.2263 | -53.87384 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 9efa68bb-e869-3805-b57f-10e59c836d37 | -3.65433 | -55.32101 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 50e8ef5d-a6bf-3938-afd9-fe89608d46fb | -3.1232 | -53.70847 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| e38b3f90-4368-3d6b-9cb5-a3500cd5b358 | -2.97346 | -54.10329 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 70ed9191-124b-3bb9-85f3-1f0d556751d3 | -3.12464 | -53.7517 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 006374c9-e268-376d-9207-aa4537a09a9d | -3.32086 | -53.85672 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 25cbdf0f-d552-3378-86dd-9bb49df2e3e9 | -3.88003 | -55.81179 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c0b8a0a-30df-3b7c-8666-ace9df5543ca | -3.86009 | -55.83608 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d04be335-9244-360c-8c74-b80c9f00bb73 | -1.47515 | -54.52901 | 2026-10-05 05:42:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 07ede7a9-93ff-3509-9dd0-ccfdd97b7ec4 | -3.51151 | -54.60813 | 2026-10-05 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 29102157-ef26-33ff-8884-b4f64211b124 | -3.09769 | -53.72424 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 69ce2007-8181-3cd0-b260-91522c25b6f4 | -3.09705 | -53.72881 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| dcb0e046-4e5e-3ab9-bdfe-775538e7e8c2 | -3.3162 | -53.84684 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 290f21c4-3fb1-3822-b5d6-a767f758340b | -3.61486 | -54.60101 | 2026-10-05 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4dc5a73f-7653-3f51-824a-2cdabe2e466d | -3.05586 | -54.23028 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c9141020-bfba-3efb-94b7-9a06e9258ce7 | -3.52162 | -54.62957 | 2026-10-05 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 85b50160-0d8c-3b6b-81cd-37d7ba834a0b | -3.30885 | -53.85487 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aff744d8-e781-3878-83ba-4f3b710016a3 | -3.37555 | -54.11074 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7798e1e7-2e8d-39bb-bd3e-2b50e1901140 | -3.12175 | -53.75919 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 4bb465f6-3fb9-3ee8-9f27-494063ea2b5e | -3.57091 | -54.65349 | 2026-10-05 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e0bb631b-c403-384a-8f44-28d8b6e95a6d | -3.1171 | -53.71804 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 932853a5-f6cd-3258-8497-c0d4a39be7c5 | -3.0452 | -54.22682 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f0ca29f0-138b-3302-8757-88ec545da16e | -2.79666 | -54.09728 | 2026-10-05 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aeb0f31d-ed24-31e6-8e4a-46905d356438 | -2.93982 | -54.12828 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99efd03d-5d8c-3423-ae2f-d23183e3c388 | -3.1018 | -53.73882 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d740c0f3-ddc3-36c9-ade2-ed442c36036c | -2.93997 | -54.08503 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae68e44e-9352-33ce-a07a-574e3045b8ab | -3.88385 | -55.81134 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c38f6f0c-9792-3108-a7d7-27280eec30e0 | -2.48379 | -56.09468 | 2026-10-05 05:42:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab080cc0-6f73-3fcd-b0d5-e0e63b914fae | -3.11581 | -53.7271 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a3cddb0b-3ef0-3b8b-af5a-5243ab4c9e3a | -3.11512 | -53.72114 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d4d4526f-006e-371f-85d5-c06cd9ab947e | -3.87896 | -55.8074 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 753f0d36-f406-304a-9b26-abd07ec71c17 | -3.07738 | -54.16418 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 85fa7cd3-4c81-3578-81f1-b71104452456 | -2.78432 | -54.09955 | 2026-10-05 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 22ecff4f-3225-3d78-8322-113dd6367e60 | -3.32221 | -53.84777 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86666da5-090b-30f4-bd94-0d19d38878a0 | -2.94657 | -54.13077 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee346421-fbe5-3bda-9b6d-32ceb12533a4 | -2.80715 | -54.10757 | 2026-10-05 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f304f614-1871-3f15-adf5-83fd9cbe9ae8 | -3.12984 | -53.7154 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 4bfa415b-145a-3570-a9b5-7cd33966a428 | -2.95514 | -59.16087 | 2026-10-05 05:42:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd4bcfa4-738d-3be0-87be-22c3ee1268c3 | -1.21198 | -55.85926 | 2026-10-05 05:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f335e58-fa6c-3302-b746-4a6ee16fe209 | -3.12311 | -53.75012 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87b049ba-c789-3c1a-9974-c00176a74343 | -3.88481 | -55.80456 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e72e5a8-1f53-3325-a142-ebe8c19d91d8 | -4.46605 | -54.96261 | 2026-10-05 05:42:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac7c8ae6-a76b-3646-988b-d14c4a52b1fd | -3.65544 | -55.50629 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1391053a-652b-3a71-8231-0aff95a85d58 | -3.3105 | -53.85843 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README54.md)
