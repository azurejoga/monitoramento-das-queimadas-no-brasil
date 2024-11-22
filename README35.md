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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0b360ff-23f6-3e24-afa2-c27f89a8e02f | -3.2024 | -54.25197 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d511e58f-30b3-3518-98fa-fde38ba13520 | -3.29513 | -53.85631 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e486de5d-d1e0-3a0c-8156-b34762fcd4cf | -2.21119 | -48.90944 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 636b5c69-901f-397b-b441-a4e9fd50d107 | -1.62062 | -52.61378 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d16d6130-0c4d-3329-961b-1efd9e8ac48e | -3.68509 | -54.59016 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 494a0851-7fb7-3b3f-b227-fbf152c156a1 | -5.82058 | -44.75068 | 2024-11-22 04:36:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5953e766-f2c1-3190-b71e-ce018a8e407d | -3.06308 | -53.2915 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d3f7c31-f763-301f-9a8b-b7e7ce6f214d | -1.24225 | -51.78664 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dd2b16bd-e650-3bb0-8824-1be1e8e25813 | -0.96407 | -51.71928 | 2024-11-22 04:36:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1b894ef-db03-3b4c-94ff-266882947584 | -2.93948 | -48.01593 | 2024-11-22 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 99fa6924-b9bc-3ee2-b055-3d57abf4c0a1 | -3.45766 | -45.90149 | 2024-11-22 04:36:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 189dddc5-df70-3144-a3fc-d35d7962ad7e | -3.28002 | -53.84655 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c365bd9-8e4f-3b04-81af-2694f797f336 | -0.77548 | -51.77854 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0f16c04f-b0d5-3b67-a80b-1a7a87ccefcd | -1.52507 | -51.55984 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a1e5a5ab-390d-30c2-ae8e-c06f2f13ebf1 | -3.77791 | -52.40976 | 2024-11-22 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69fb2b8b-2c31-3244-a0e6-cb88c39c09f6 | -1.78262 | -45.9672 | 2024-11-22 04:36:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f640393-18bb-36ba-b810-09310ec460bf | -2.72643 | -46.09019 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d104a75-a716-3422-8e45-ce9026c62436 | -1.20907 | -53.6889 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 12b11813-aaad-3fd5-a79c-82270cc43aec | -3.08451 | -53.25916 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb0b18a8-f9aa-3307-8dd7-0e7b5a1d4143 | -2.8224 | -54.02577 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 937f85f3-f2aa-3ba9-9c26-2ffcf25a217c | -0.93936 | -47.55505 | 2024-11-22 04:36:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| db4e2484-c9c4-3054-b8e0-afc97ed9e847 | -3.2432 | -54.24659 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 5cf09241-ec3b-3a3c-b0fa-bd9886301bde | -1.21511 | -51.79121 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 61b64a58-42bc-3f40-b62c-c89e0906ab49 | -2.70077 | -46.09422 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d512e5ae-1d1b-3084-ab33-8eb9be41bd93 | -3.2203 | -54.24718 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 6a52eab0-2c18-38ae-8223-02f3238718ef | -3.88099 | -51.16623 | 2024-11-22 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 571d9b27-54dc-39a1-b451-36acbe1e037d | -3.2775 | -53.78445 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 177ea2be-c97d-3cea-ad28-ee1ae9ab2bd1 | -2.4339 | -46.53088 | 2024-11-22 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f6c053d-6b18-3444-a099-1d4b32de11a4 | -2.69857 | -46.2472 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aabefe7c-9aa8-36fb-814b-d9cefd96f993 | -2.26281 | -50.45174 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e23aa94d-26f8-3a71-bdfc-952ade822c9e | -3.2858 | -53.83639 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5dbc5ddc-d827-3312-b1b2-1bfc85ca4698 | -2.25929 | -50.81025 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0bd9bd1-ae2f-3056-82c3-962e72cce08d | -2.28225 | -47.91661 | 2024-11-22 04:36:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7eb1c6df-87f4-3244-bd67-8fd44d76b217 | -1.78886 | -53.63338 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3ccf4a71-3399-3110-9b28-4ca900f02527 | 0.09404 | -49.85791 | 2024-11-22 04:36:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0bf79ee-2c0f-301f-acd0-8383f1c69984 | -3.23283 | -54.24919 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 0de1a5e6-b7f9-33e6-8c8f-2f9b607928df | -3.89335 | -46.65675 | 2024-11-22 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25b9d82b-1e05-3eeb-8338-7e1028353a58 | -3.84805 | -52.34965 | 2024-11-22 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e3150ab-d5c3-3580-b09d-19b954c1d93c | -3.56324 | -54.22654 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 96230865-a5e7-30a3-9057-1113a14b5e21 | -3.96268 | -51.13575 | 2024-11-22 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 660f2cbd-4d30-367b-b8c0-7bbcd57d2654 | -2.2147 | -50.46702 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31ee9c05-d48a-3405-97b7-6c2f661844c6 | -0.80565 | -51.79456 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 69f87e89-2ab9-3f4e-8f88-a9a156bd9a97 | -2.3495 | -50.37053 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6d16c93-9a6b-3cfb-afb4-2730212d0000 | -2.63303 | -46.22234 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35edd2a1-f0d7-31e2-8726-647b6fedab75 | -1.73489 | -52.37957 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1ca6a15-2a53-3cd4-8229-71fc84e062fa | -2.69923 | -46.21994 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed6a2a2e-40b8-3fbb-b7ef-d00e1a238714 | -2.8348 | -54.01629 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88f70561-ba2d-3161-a585-7837d79ff74a | -2.56363 | -46.15325 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 869903f8-8325-3a53-8203-328320ec5045 | -0.30358 | -51.5439 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 974b7de0-1e3f-3260-9574-a83efeaa9082 | -2.17686 | -49.08446 | 2024-11-22 04:36:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77e6ca35-3594-3f86-b367-9b5b5b53cc74 | -2.52763 | -46.39989 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99564186-7bcf-3861-9c5c-ca41205e0304 | -3.10998 | -53.17691 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92419519-de87-30cc-94e7-2c6fe036d451 | -3.82219 | -52.41698 | 2024-11-22 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1bbfe9c2-ebd9-3d6f-b1ff-2240f0b1c329 | -1.93195 | -49.51391 | 2024-11-22 04:36:00 | NOAA-20 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 40a1dabc-92d7-3362-85e0-fb3d4bdbfb5f | -3.55752 | -49.44281 | 2024-11-22 04:36:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46c073e3-0821-3e5a-a274-6f1b5e3a0f6b | -1.46494 | -51.11895 | 2024-11-22 04:36:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1c5bdf7f-a048-3a9d-b509-8ce7939c02f7 | -2.50587 | -49.00121 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3399a1c9-1764-361d-98ab-777dd8fb9e87 | -3.06068 | -53.28416 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d6b3796-208b-3cb4-ab34-9980786a902f | -1.05051 | -51.74037 | 2024-11-22 04:36:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10ed0670-993f-305b-b504-a9c975f02e93 | -1.06909 | -53.64723 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58ed5204-d948-3c53-a10e-8805b5134939 | -3.00607 | -51.31268 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7fcf5727-d8aa-3e1f-8c57-0047b965c902 | -3.45286 | -45.90899 | 2024-11-22 04:36:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 423f078f-6d64-3c6b-8371-491f61cc031a | -2.64591 | -45.13228 | 2024-11-22 04:36:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6098571-f745-3752-8583-4442d2116003 | -2.52476 | -46.39967 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 25a57ee5-05bf-3743-9f59-7d8103ae4670 | -3.57814 | -54.50104 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 832ad5b5-80e6-3ae1-8485-e40fe82f7bdc | -2.68544 | -46.17079 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0b92905d-49a3-3cc4-a501-a543c9588a76 | -2.35193 | -48.55474 | 2024-11-22 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 2d2be23c-053b-3b74-8594-8cfdd44ae336 | -1.131 | -54.17949 | 2024-11-22 04:36:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 032db75f-a32a-3b28-8c7e-b34bc7818be2 | -0.0423 | -50.82051 | 2024-11-22 04:36:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db0cccae-c039-3f27-82fe-0d998eb3a18e | -1.91523 | -46.44188 | 2024-11-22 04:36:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b92cb0f7-e069-38fd-93f4-6301eadc72cf | -2.37245 | -46.79227 | 2024-11-22 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd837ad6-3c1c-3a36-ab58-c0d1123d5d57 | -2.44871 | -46.54835 | 2024-11-22 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25e3776b-750d-3fa7-8ed5-98097299c6a0 | -1.57751 | -50.43858 | 2024-11-22 04:36:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49a1c908-9323-3bbf-81a6-99a724011909 | -2.44578 | -50.40409 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f04ed739-0ac0-3f35-af9d-a195f62c4efe | -1.21276 | -51.98761 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9263d435-e6f4-3824-aa9c-c5b2c5a9191e | -2.67617 | -46.16153 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea31b3b5-aef9-3cbd-a1a3-b640b2817b96 | 0.43602 | -50.77515 | 2024-11-22 04:36:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ddde327-6b4f-3292-a3b4-89fbb0d21ee1 | -2.91417 | -54.78159 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d9b404b3-205b-3fc9-9b1a-3ae85abe7475 | -2.50364 | -48.99379 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 123942f0-fcc8-352d-9b7d-3135c468d205 | -2.60818 | -54.258 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9bfe5766-0b5a-3bd7-992b-d40f150c0831 | -3.45703 | -45.90551 | 2024-11-22 04:36:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 06436fab-8e5b-3730-9856-e9ea5525e129 | -2.04801 | -49.72795 | 2024-11-22 04:36:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6f9a9bd-4bf6-3a15-b406-614db028069a | -1.1813 | -51.93415 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d95e22da-4513-3cd4-ad13-ff949d3d6588 | -3.21907 | -54.25493 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0f85ff94-9972-31f7-a43f-eeff2b37cc03 | -2.70849 | -48.66328 | 2024-11-22 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab92c8ec-e7cb-3913-8465-3467f85e9e15 | -3.23206 | -48.87954 | 2024-11-22 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b4c0ef6-9727-3ac4-86d8-d4abbbe50dff | -1.20013 | -51.95989 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 2db35190-49c9-377c-9082-e51ac94d460a | -3.94125 | -47.0215 | 2024-11-22 04:36:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bfa5c928-7069-3b25-99ac-270e81394bc4 | -0.88537 | -51.72205 | 2024-11-22 04:36:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53309639-a393-34a9-afc9-13eaab00c46b | -3.20366 | -54.24413 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 93c2c9f8-a127-337a-becd-8e016d2961f0 | -2.769 | -54.06707 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f27bb736-70fa-364e-bc81-02777b59bdd9 | -2.92065 | -48.3309 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ed70ead-a6ce-3ad0-b218-1ffa2e71b3f3 | -3.42136 | -53.28909 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b4c55e75-54b7-3f39-96e9-6b652aef217b | -4.29411 | -48.23724 | 2024-11-22 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cbab7f76-b32e-3a87-b1fb-ab12361f418a | -1.15443 | -53.67165 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff4c3e3d-8d97-39c5-9a93-4c308c338d01 | -1.22625 | -51.74417 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| abfb81ed-17d7-37a8-b419-f46c934e1587 | -0.92954 | -51.72274 | 2024-11-22 04:36:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8a32621-d5fe-3d25-8eb3-36672a7cc268 | -3.10375 | -53.98241 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff2f23f3-14d7-3539-a48b-6c7ae8144343 | -3.67526 | -52.37246 | 2024-11-22 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2ab9a17-36ac-316d-afbd-01edcc561bd1 | -3.85773 | -52.35997 | 2024-11-22 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |


[Clique aqui para ver as próximas entradas](README36.md)
