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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 15a576c5-7f5e-3585-9cbe-6cb29fbb0b8b | -4.29763 | -48.60608 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b7a4d35-4f97-33e8-bb1f-e0f2fb0053df | -3.91403 | -50.0368 | 2024-11-27 04:42:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 667c116d-2529-36ec-bc96-ca4a1948c95b | -2.79982 | -53.03973 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f66ba598-5b9b-350b-b9b4-6e8fa6fe82ef | -2.03738 | -51.18975 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15a511d2-8fe6-3574-8e23-e0842a77076e | -3.28948 | -50.27 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0074e3a8-72c3-3a6e-b4b6-e2f5b7f3250f | -2.81315 | -46.8214 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d45629b6-85c3-33e4-98f0-76bcd02ca498 | -2.86344 | -53.32119 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3624421e-e7a0-3af1-8c89-c855104a13be | -3.51514 | -50.30573 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5ea708dc-962f-38d0-a580-48f78746a3b9 | -2.84528 | -46.83382 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0d9ff80-09ca-3b13-842e-441c2c329b22 | -2.6001 | -53.97693 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cb9981fd-2bfc-30c8-a0a6-c89f994ef5ef | -3.08246 | -47.81343 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 799491a8-8eb1-3a52-9f08-7c557fc57440 | -3.78386 | -46.68507 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b1fa7ab-695c-3938-afb7-80c5f3ec2dfc | -5.72673 | -46.16544 | 2024-11-27 04:42:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 450ce662-bda5-3b84-bb81-c58d1eb19748 | -2.58162 | -53.96641 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b4dd00d-c216-3502-a65c-1c27ccf7d2fb | -3.28593 | -51.15471 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c6c48ae-b910-336a-a9f0-9a2c4c98691a | -2.57266 | -51.88799 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c52c4f8a-fcda-3005-a8a1-4aab1407b564 | -5.91802 | -42.97433 | 2024-11-27 04:42:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 27c003dd-f4e9-33de-b1ac-eda4fa2f6e7c | -2.93962 | -51.00401 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10a030db-e6e0-3172-a6a5-bd68fa3457e2 | -3.22797 | -50.31674 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7656113c-6d14-3d6d-8ccf-6d3d8531c8d6 | 0.16685 | -49.63021 | 2024-11-27 04:42:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 697683b4-e7d3-3e04-a962-05ee1b2c2a55 | -3.92396 | -46.39923 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ab91295-903e-37c1-88b0-2603fb7de430 | -1.41424 | -51.13636 | 2024-11-27 04:42:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af334f50-970a-3571-b9d6-1217b32edd47 | -1.74059 | -52.80094 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7c9940a8-1af1-3516-9272-0fbf9e44d394 | -1.58811 | -52.23586 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f59eafa6-6e25-3eec-9a6d-fd35c8959bf4 | -1.93618 | -52.09776 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef5d25d2-ef2b-3431-aa21-850d607198c8 | -2.88999 | -51.38472 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e626ac26-dedf-35e4-b360-68bd0ca3d7a8 | -3.37463 | -50.11791 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b0cd6d92-1061-330f-a407-75bdb7bc6235 | -1.65855 | -52.51964 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92ba75ef-8243-35db-8829-c5385496b445 | -3.31463 | -50.49936 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1200915-8100-3201-9bb8-b579856847e2 | -3.36458 | -50.76519 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e22188f-36c9-3a7f-8871-f240856eea2a | -3.07051 | -50.94905 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e94a3f32-31f6-365c-b7c4-e1ea2f4b831a | -2.42673 | -53.84858 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1be02323-e449-3675-9e02-c668124812f1 | -3.08885 | -53.27014 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c7d4d9bd-63fd-3dba-acb4-2182d60c1a67 | -2.36882 | -50.42153 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a84aea35-8a56-35c9-bf64-aad2f06ef21a | -3.33995 | -53.31156 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c2d6fbe-bc8b-3e1a-b5cd-9436067baaaf | -3.04843 | -48.50787 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5499dd1-47f7-38fd-87c5-de8643873647 | -3.7837 | -45.52584 | 2024-11-27 04:42:00 | NOAA-20 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7ffd22c-7803-3458-8110-c19c950b2cb7 | -3.94368 | -46.72076 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 41efaae4-1776-3c5c-83fc-59c0960c8b35 | -4.12467 | -51.07201 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2aa65024-bd1f-3227-8875-5810cd84ac92 | -3.37794 | -50.11843 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c830b74b-befd-3138-a5d5-3ad775b2d81f | -4.04808 | -46.83649 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a497fac-89d1-3b2f-a3fb-717ec29e56af | -3.42742 | -51.67574 | 2024-11-27 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a693fb7f-2735-35b2-aa35-ba51c0829b8e | -4.40136 | -47.21862 | 2024-11-27 04:42:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34e2f659-2b78-3fdf-96ef-cf9ab0a93a28 | -2.5754 | -54.05723 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0da5903b-4df0-3961-a4e1-8f43907d0ac3 | -3.72337 | -50.19007 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86e6962a-3d28-3787-afbd-9b7d306c791d | -1.2306 | -51.79521 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 478f55c6-7edc-3f66-a63a-145fe87d5c82 | -2.18341 | -52.1321 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69bf2dbd-208b-36a6-932b-92cc38643750 | -3.45057 | -49.50344 | 2024-11-27 04:42:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95558944-b958-3934-827b-fb661db5ca0c | -3.77535 | -46.51411 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ac57399-9ddc-3462-a03d-1d683c2b9eb8 | -3.34094 | -51.23864 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38b6e510-8207-3740-ab7a-492253c9fd59 | -1.73767 | -52.79635 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98b7f90e-bd23-3522-a8ea-423ece20b7e6 | -2.58545 | -50.64242 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 594ada18-c49b-3b25-87d4-b106ebeaab30 | -0.77682 | -52.3933 | 2024-11-27 04:42:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7d2823e-e84d-39fe-a387-7f3177fea9f3 | -3.23636 | -50.17727 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e94a4e06-a618-394b-b3a8-9463db0ef504 | -1.06222 | -52.4197 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 94bc1e66-cc7f-310e-9213-934b2dfa94bf | -2.81886 | -48.60993 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e9cb08d-e6a8-3da0-8d36-57ec4c56b351 | -1.62845 | -52.2737 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 941a95b2-bc35-3e71-ba8b-92b76a4f15ff | -3.02194 | -49.52942 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d0d8b39c-c7fb-39f3-90d2-26dacd6cb6b5 | -2.79833 | -52.91254 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3f7de01b-af5a-3149-badd-70be8e329f6f | -4.11811 | -48.52229 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ea452959-1712-3862-9d5a-6c672fdd580a | -1.68998 | -52.61756 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 906f0271-cf42-3f32-b96b-c384dfde6125 | -2.84105 | -49.40502 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77e10b35-bf4d-3a35-9a1b-cae8ec9840a9 | -3.08815 | -51.03051 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6409db89-c0f9-35c2-9262-adec3df914db | -3.25359 | -51.14578 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48e1f3d4-1757-31f5-ab90-33253f43a2eb | -4.25896 | -48.5396 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b44fa0d4-1c73-39a8-a15b-ec19cec383ae | -3.57637 | -41.962 | 2024-11-27 04:42:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| cf3dc714-ee09-3fa1-b140-a52661d28bda | -2.54613 | -47.97538 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ca7f549-2372-3e0a-8fed-0d1fc873af51 | -3.10419 | -53.24313 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4e3231c-5168-38dd-b347-6ef4313a5abc | -2.58159 | -50.64536 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ac0611d-c48e-3fb7-9148-3a398471c71e | -5.46568 | -46.82281 | 2024-11-27 04:42:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c1fa251b-831f-3cd9-821a-dc2dd142389e | -1.6599 | -52.25507 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| da056cfa-21e0-3712-ba36-2f7847a2222d | -3.10583 | -53.25594 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 729c4e2b-be16-3ccd-a2ce-ab7d489ab4ae | -3.56438 | -42.0411 | 2024-11-27 04:42:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bb52fc65-9271-3fbe-8af4-cfe927bf93b9 | -3.24494 | -50.61897 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6a03fae0-6538-3091-a477-d02c41da755e | -3.32299 | -50.05694 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f12da758-fbd2-3d0e-b1bc-16f9be1caaf0 | -4.94801 | -45.87684 | 2024-11-27 04:42:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ea238ca-e633-3a03-bbe1-9f15981f49c3 | -3.956 | -46.90429 | 2024-11-27 04:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31a9f065-cb48-3536-ad72-84317d5259a4 | -1.9064 | -50.59661 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46fe2909-679d-3357-8cef-3c5d5a114a10 | -3.28217 | -48.75839 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ea19bc2-27a6-3a6d-9005-12a7bd173e70 | -4.22158 | -50.88919 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b775b593-e068-3657-86fc-444265d1cb64 | -5.75697 | -46.257 | 2024-11-27 04:42:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2538cc00-069b-3b04-8af2-7907e99fc254 | -1.21364 | -54.54245 | 2024-11-27 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 892960ab-0e68-3a1f-954a-1a1688a9fd14 | -3.10609 | -48.0195 | 2024-11-27 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4062ee0f-db83-37f5-978c-767bf6df6c56 | -3.09662 | -53.73577 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fc2d851a-38d6-36bb-a01b-cc82024e83f5 | -3.24583 | -51.15175 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ccec474-d058-398d-9539-b7fdaa2d36fc | -2.84418 | -42.52348 | 2024-11-27 04:42:00 | NOAA-20 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 71a6b52f-89f3-3159-97df-bd0b3501a883 | -2.69756 | -51.98637 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 26fe0f9b-831b-3615-bc0c-63ea53399a57 | -3.9899 | -49.96381 | 2024-11-27 04:42:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4451cb8-436a-3a61-86d5-09880a7c0d96 | -2.54769 | -46.41114 | 2024-11-27 04:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 649dcc04-f519-3d72-a247-daf8a472b114 | -2.92034 | -48.58833 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb76f837-b9e6-3628-9614-7a9863bdd953 | -3.71341 | -51.79752 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f9e5a652-c3d7-307a-9aa9-85926c97478d | -3.10028 | -53.26768 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 66d9d202-b797-3ce2-99d5-c1d70f348dbe | -2.96017 | -53.72059 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5005ec8c-b043-31bc-af32-505d70f2abf9 | -2.99519 | -53.36236 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2a327683-5b7f-39de-bd98-a564690a9f68 | -2.18556 | -53.7743 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 7f789b4a-3240-3af3-acd8-abab8b5686ea | -3.98881 | -49.97071 | 2024-11-27 04:42:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e8f9b758-6f8a-3c92-a56a-6411adc9518c | -1.78922 | -52.74684 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7f0eee3e-4812-347b-b550-4df8035214b0 | -1.51096 | -52.21632 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f8493c1-f807-3b40-9c7a-c3f884643dfb | -3.0566 | -53.68338 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dcc14cd3-0980-306e-aebb-0ba1e405b866 | -1.3187 | -51.74822 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README64.md)
