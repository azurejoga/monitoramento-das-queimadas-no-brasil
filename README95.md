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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 599a905f-1dc0-353d-a25b-69b10075b5e5 | -8.0226 | -45.4127 | 2025-09-04 06:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 19ac14b0-ec2d-3a03-a28a-4866a18dbeec | -10.4794 | -46.7637 | 2025-09-04 06:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 98f04f6e-7fc2-3010-b3b3-65103496020e | -6.7504 | -58.7268 | 2025-09-04 06:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 5c2c6a0b-a063-35c9-bfb8-642037521c1f | -10.4981 | -46.7839 | 2025-09-04 06:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 50.9 |
| a28dade7-5115-32f0-8db6-0c71fcdefba0 | -10.79982 | -68.26797 | 2025-09-04 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 091914ae-e5a3-3aca-bd61-fda8530932e7 | -10.15054 | -68.53111 | 2025-09-04 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 488bc1ef-3181-389a-98f0-cfec1b058a29 | -10.15367 | -68.53638 | 2025-09-04 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1e59c9b0-b78b-3578-86f8-ed332bb0c041 | -10.96442 | -68.4921 | 2025-09-04 06:10:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96642128-1795-31b4-8037-49344b004325 | -10.15434 | -68.53165 | 2025-09-04 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a023c84e-d5f7-3759-908f-edaa6adb66bd | -8.0417 | -45.3882 | 2025-09-04 06:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 4e8d8432-3ab4-3b27-8fdf-4b4fdd7d0873 | -22.6567 | -43.6825 | 2025-09-04 06:20:00 | GOES-19 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 74.0 |
| 2c44a054-ca9c-3593-81e6-e95e22ae1b20 | -8.0228 | -45.39 | 2025-09-04 06:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 109.0 |
| e7dfcf73-844c-32cb-87a6-7ec3551ad3b3 | -5.0135 | -56.2553 | 2025-09-04 06:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 88ea68fd-2649-3281-9675-6c5ae8fd9f65 | -6.7504 | -58.7268 | 2025-09-04 06:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 14cba0fc-08e0-32bf-8644-6671120bfe90 | -6.7319 | -58.7276 | 2025-09-04 06:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| e88e8f24-81f2-3a6f-bdb8-d83f2cee1dce | -4.9951 | -56.256 | 2025-09-04 06:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 4240428f-ced8-3597-b431-9c0be1e7cb81 | -8.0228 | -45.39 | 2025-09-04 06:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 117.8 |
| ecbb7bbe-57b4-37ef-bc2e-071ab5dbba82 | -4.9951 | -56.256 | 2025-09-04 06:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 7e1b48e8-c2c7-3b06-a2d1-65724a5f81d1 | -5.0135 | -56.2553 | 2025-09-04 06:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 1204534a-99ee-30f6-9fff-b00ae3df978e | -6.7504 | -58.7268 | 2025-09-04 06:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 82.6 |
| a3cbeaa3-d57e-3a16-875a-6be284ccaf88 | -6.7503 | -58.7462 | 2025-09-04 06:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 9a192625-d48f-319a-a6f8-661bcfbaf151 | -8.0417 | -45.3882 | 2025-09-04 06:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 85.5 |
| ffee4db2-ad36-365d-931a-12d03aaa32ae | -9.37498 | -71.11028 | 2025-09-04 06:35:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9be4e53-0beb-388b-84e1-7d73bd18ba00 | -7.99286 | -71.18751 | 2025-09-04 06:35:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c64a3965-e222-3ef5-97c2-163604c04755 | -10.15141 | -68.53215 | 2025-09-04 06:35:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fbb07aa-1a14-39a3-a8c5-dc3f5ddffe1b | -10.1509 | -68.5362 | 2025-09-04 06:35:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f25c93c9-098e-3a00-a9f3-6559db453d46 | -8.03045 | -71.257 | 2025-09-04 06:35:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ad5267f-be1c-3de4-9863-6bf82b8e5db9 | -8.88455 | -69.34233 | 2025-09-04 06:35:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 164b38b5-1508-3b32-95f8-f3e8849420bc | -7.99399 | -71.0068 | 2025-09-04 06:35:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 790e1e54-7265-3594-8b40-b0d2b4fc5383 | -8.8841 | -69.34576 | 2025-09-04 06:35:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3702792a-ad0d-3ce8-a57a-e2de37e3b9c5 | -4.9951 | -56.256 | 2025-09-04 06:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| f1e2b41b-1a4f-365f-bd98-f8489a1751dd | -6.7504 | -58.7268 | 2025-09-04 06:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 386d58f9-e732-37a2-8069-99acda61ad9d | -8.0228 | -45.39 | 2025-09-04 06:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 63b6b4f4-0372-34fa-88d0-afde411e2a5a | -8.0417 | -45.3882 | 2025-09-04 06:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 3e04dd01-d941-30c4-9e74-c93f43b753a4 | -6.7503 | -58.7462 | 2025-09-04 06:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 21ac7678-f480-3258-8c81-3bce440bb4c1 | -6.7503 | -58.7462 | 2025-09-04 06:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 20f35d33-0ff7-3071-b644-5bffa285a3a6 | -9.6043 | -47.0437 | 2025-09-04 06:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 20e70d96-21c7-3148-a65c-b4e063972e52 | -4.9951 | -56.256 | 2025-09-04 06:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 1730bde2-d263-3eee-bc4a-701f57e5cb8a | -8.0228 | -45.39 | 2025-09-04 06:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 105.3 |
| ec6f9e10-007b-3b62-9f0d-fe142fd4b25f | -6.7504 | -58.7268 | 2025-09-04 06:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 7f3735ac-e0b2-332d-900c-4714cf009b6c | -5.0135 | -56.2553 | 2025-09-04 06:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| c8633f0a-e431-3b0b-b79d-c3eb7f885568 | -8.0417 | -45.3882 | 2025-09-04 06:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 4ae80d3b-de98-330a-8ef7-73fd6c2f8a2f | -6.7504 | -58.7268 | 2025-09-04 07:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 17a58cee-e21b-37e2-b8d8-9a25fd896a55 | -4.9951 | -56.256 | 2025-09-04 07:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| c8865b1d-3358-3552-ad3f-d2190a6baa1c | -8.0228 | -45.39 | 2025-09-04 07:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 72e7da05-0096-3d17-b0db-a65bcceb8240 | -6.7503 | -58.7462 | 2025-09-04 07:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 3ffdda75-fb90-3c22-b7a6-3963d90e8b70 | -8.0417 | -45.3882 | 2025-09-04 07:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 84.0 |
| ccfc4846-9e43-3955-9125-ee322946eabf | -9.6043 | -47.0437 | 2025-09-04 07:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 30605cb9-28d3-3599-af23-092edcbc737b | -6.7503 | -58.7462 | 2025-09-04 07:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| b6feec17-7706-3be0-960e-48ea58df9cb0 | -4.9951 | -56.256 | 2025-09-04 07:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| fd430084-7019-333d-9cef-6412b08d1e38 | -8.0228 | -45.39 | 2025-09-04 07:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 91.7 |
| e3fbb1e3-74c5-3371-a10b-dbe7b28e9b0d | -8.0417 | -45.3882 | 2025-09-04 07:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 87.5 |
| ad0667f2-6cb2-3195-8596-a1e0be224399 | -6.7504 | -58.7268 | 2025-09-04 07:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 93.8 |
| fe0d5079-160b-39d3-b678-332fa7b6d9bb | -14.6 | -48.0142 | 2025-09-04 07:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 52.9 |
| ac93f1c4-49e4-330a-a38c-d3a5dbde0f6a | -4.9951 | -56.256 | 2025-09-04 07:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| e1427547-0fb3-34ef-b8d5-5924fc766cc1 | -6.7504 | -58.7268 | 2025-09-04 07:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 89.4 |
| db6e20c7-1f93-36a1-8a82-b0578176496d | -6.7319 | -58.7276 | 2025-09-04 07:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| a92ee99f-c140-36e4-b1f2-8f54316dea3e | -8.0417 | -45.3882 | 2025-09-04 07:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 83.5 |
| b3be585d-01fc-364b-9b0a-7cf34f1d1459 | -8.0228 | -45.39 | 2025-09-04 07:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 24eea6a7-e7e1-3669-8ae1-eb8fe494a6b5 | -6.7504 | -58.7268 | 2025-09-04 07:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 17cfac69-690c-3e22-aaa7-d5a6578493b5 | -5.0135 | -56.2553 | 2025-09-04 07:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 659f563f-1ad8-3f12-b7a5-f725f37eb7e1 | -8.0417 | -45.3882 | 2025-09-04 07:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 71.7 |
| abef504c-d209-390f-ab85-7d196f5ccd85 | -8.0228 | -45.39 | 2025-09-04 07:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 4a2c5d8e-b613-3163-85d8-1103dc1b109c | -9.6043 | -47.0437 | 2025-09-04 07:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 786dbd73-46d0-364a-b4a5-4b32d26e9cbd | -6.7319 | -58.7276 | 2025-09-04 07:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 1e844bb1-e586-3a7c-8d46-400e3489c65d | -4.9951 | -56.256 | 2025-09-04 07:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 2a5200bc-e644-363a-ae88-d523aca5b39b | -8.0228 | -45.39 | 2025-09-04 07:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 334b2032-fd8d-3796-9f2e-00b0f3f10197 | -8.0417 | -45.3882 | 2025-09-04 07:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 49b67e6d-1f4a-3eb0-9650-5d66a11ddb8d | -6.7504 | -58.7268 | 2025-09-04 07:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 88.1 |
| ad4bde27-485b-364a-8b91-95ff715b6eed | -6.7782 | -44.0876 | 2025-09-04 07:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 11dce45e-5d26-3976-80d2-18d170f7ad2b | -10.4469 | -50.3926 | 2025-09-04 07:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 62a6f695-c590-393e-9170-67a067a1a0e9 | -4.9951 | -56.256 | 2025-09-04 07:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| c17a0522-404a-3755-8d1e-6a531b071fe0 | -6.797 | -44.0859 | 2025-09-04 07:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| a1112d3a-bc72-3fcb-a59e-20155dd69393 | -9.6043 | -47.0437 | 2025-09-04 07:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 05ed6bda-0130-3157-9627-e0728cae5f31 | -9.6043 | -47.0437 | 2025-09-04 07:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 4d2494dc-41e6-350f-b054-af688352dbd9 | -5.8525 | -57.7722 | 2025-09-04 07:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 248705a5-2552-3644-a086-dbe9dea2b56d | -4.9951 | -56.256 | 2025-09-04 07:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 3964e311-571f-32e4-9e1b-067cfc6c5234 | -6.7504 | -58.7268 | 2025-09-04 07:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 626057ac-cc8b-3c34-981f-479cb21b46e2 | -5.908 | -57.7311 | 2025-09-04 07:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 06b4511f-ccd4-329b-a697-4fae56f36ade | -8.0228 | -45.39 | 2025-09-04 07:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 92642858-9fcf-32c5-b78c-70ab2cbbb424 | -6.7782 | -44.0876 | 2025-09-04 07:50:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 74cfb831-591a-39ef-9538-4c1643cee844 | -6.797 | -44.0859 | 2025-09-04 07:50:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 83f3ebd4-6042-321e-9a42-1406427d221c | -8.0417 | -45.3882 | 2025-09-04 07:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 8712b5d0-ab5f-31cd-9ca9-5839292d63b6 | -10.4469 | -50.3926 | 2025-09-04 07:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 38.3 |
| acede156-4617-3170-a4c9-3164f0568d7b | -6.7319 | -58.7276 | 2025-09-04 07:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 26b4a47b-4397-3aef-aeeb-2318fd025822 | -6.7503 | -58.7462 | 2025-09-04 08:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| a6d584d1-10db-3a34-b14e-a3b8155eab6e | -9.6043 | -47.0437 | 2025-09-04 08:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| bfc1a4f0-eebf-32b4-a420-170a02f8f26c | -5.8525 | -57.7722 | 2025-09-04 08:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 15431bbe-2efe-3531-a77e-83e6ec2b52f4 | -5.871 | -57.7715 | 2025-09-04 08:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 25cda4f6-7fa6-3c57-a589-275872b0a88a | -8.0417 | -45.3882 | 2025-09-04 08:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 58.1 |
| bf9ab9a2-7061-301a-814e-19b95b32d72d | -4.9951 | -56.256 | 2025-09-04 08:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 4f7b0efa-06fc-3586-95ba-97667cb5a8d7 | -6.797 | -44.0859 | 2025-09-04 08:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 3aa86a7b-1b4a-3ce4-9bbf-4e995ff88c3a | -5.908 | -57.7311 | 2025-09-04 08:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 726246c6-3d5b-3e7a-9846-ab564fdc491f | -8.0228 | -45.39 | 2025-09-04 08:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 63.4 |
| dc0bf2d9-c053-3181-aec4-26c52bc58c6b | -6.7504 | -58.7268 | 2025-09-04 08:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 8ae9bea0-c4f9-3046-8e0c-ce87c5497c0c | -10.4469 | -50.3926 | 2025-09-04 08:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 07755ffa-770a-3340-ab71-d461f342e532 | -6.7782 | -44.0876 | 2025-09-04 08:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| cbc4d4f3-9771-3740-ba27-55b73e5c59fa | -8.0228 | -45.39 | 2025-09-04 08:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 75061498-57be-3405-9517-9aad9b655159 | -5.908 | -57.7311 | 2025-09-04 08:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 8e1c2da6-fd24-301d-9416-35ac89dd7f1e | -4.9951 | -56.256 | 2025-09-04 08:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |


[Clique aqui para ver as próximas entradas](README96.md)
