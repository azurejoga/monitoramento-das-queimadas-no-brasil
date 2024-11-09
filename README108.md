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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ffc4b5d-25f9-3be8-a9cb-1077039fd9c4 | -3.18753 | -50.58852 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 973e3eee-7973-388f-8841-dd0cf11654fa | -0.6464 | -52.389 | 2024-11-09 05:20:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef4b8d91-8c21-3499-8e3a-2f9dc36cb5e1 | -3.21531 | -54.06001 | 2024-11-09 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4637649b-d70f-38ee-a54f-623b43fdea4d | -4.06522 | -50.01538 | 2024-11-09 05:20:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bcf8096f-211d-3a18-975a-1711e2c67dfb | -0.79066 | -52.48384 | 2024-11-09 05:20:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe77e723-683d-3e4f-8da2-1f117ddd9ae3 | -2.449 | -46.31734 | 2024-11-09 05:20:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 45a74588-df19-3d6d-a4b0-6fe6faa6df2f | -3.01027 | -53.42834 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b949a412-d032-3431-97bc-0f9f2bc2049a | -3.10241 | -53.32575 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| fc618228-f3ea-307b-aaa1-3dbf2616aa50 | -1.22968 | -51.75774 | 2024-11-09 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9d63c74-8a57-36d0-8b45-c6e2c2f52448 | -3.82532 | -49.85994 | 2024-11-09 05:20:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d6b79804-751b-36c1-b01f-f34b675ee3b7 | -3.32874 | -49.91315 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0e2af788-71ae-3445-bdca-9ccf58ba798e | -3.11871 | -50.14405 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f422d6b3-68dc-3bae-8936-416b13bb8493 | -4.06256 | -50.01594 | 2024-11-09 05:20:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e751bc1-527f-3ce1-8caf-1894a3af3410 | -1.56228 | -52.28321 | 2024-11-09 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4cdb9c29-3a11-30b4-a229-a4a339939e13 | -1.82518 | -52.02831 | 2024-11-09 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 14c515d3-bdad-31f4-8742-ca45e324332a | -1.18508 | -51.98862 | 2024-11-09 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bbba5581-df8b-36f7-9064-228d34e5d368 | -3.04374 | -50.37729 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22462cc8-3e5e-3af1-98a9-345fed261ba5 | -2.83515 | -51.80229 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 373f8bf5-7a9c-3399-9727-dfec06eee54e | -2.37073 | -46.85868 | 2024-11-09 05:20:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3122e6ce-8c74-372c-8d73-cb01e71002da | -3.09415 | -53.3202 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bfd15050-4ff5-3964-869e-2de6ed8a5bc6 | -1.52167 | -52.21976 | 2024-11-09 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d872d080-e45d-3606-bd00-03790ceae230 | -3.75837 | -51.7654 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fddb96e4-3682-3d00-aea7-551014a0e9b9 | -0.91065 | -52.56251 | 2024-11-09 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bb0cea88-e376-3029-8e9f-48c90d24f77a | -3.09284 | -53.32888 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b885f34e-2592-3123-a315-f2a2b6c04d60 | -3.95745 | -48.99843 | 2024-11-09 05:20:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92a1dd65-998c-39f0-b23a-ba771334f672 | -3.83817 | -50.04672 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9e99578a-edc9-3dfc-b8d5-b7b6a1185c89 | -3.28269 | -53.67755 | 2024-11-09 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f0caade3-c45d-30bd-9b34-ee1f878f2caf | -3.1563 | -51.12467 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b008b8db-030e-32e6-b945-2d4fe3cdc8c9 | -4.11584 | -48.50908 | 2024-11-09 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f71b34e3-a120-3be8-82b8-0d7447c97a30 | -1.59339 | -52.48533 | 2024-11-09 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e8fc1486-d8ca-336d-a176-581fc20d06f4 | -1.82627 | -53.72497 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4824415e-d288-3f41-aec7-1fddca6328c4 | -3.19247 | -50.44407 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d305ac04-92e2-397a-a481-c4f9a10354c0 | -1.48568 | -51.75076 | 2024-11-09 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 379405e9-820d-3106-b6e8-4ba22600827e | 1.78606 | -50.43316 | 2024-11-09 05:20:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ca348362-9cdc-3033-8795-753e9517626a | -3.03524 | -51.53385 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e97761a1-2788-3edd-85cc-20aecc18fe08 | -2.15773 | -53.64981 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f6d7bcf-eb24-37df-bb37-adb3cae28c92 | -2.87583 | -51.47255 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0369b7b5-ad0e-3a38-b60d-c968a27484f9 | -3.49618 | -51.14551 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b0deb02f-39e4-3a2f-9312-aac9b0cfa453 | -4.38024 | -48.58021 | 2024-11-09 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 92f9c9e1-7173-37aa-b533-a217ec437c96 | 1.30517 | -50.73425 | 2024-11-09 05:20:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1337ad62-014d-3a13-86c2-8d4c44636b36 | -3.35701 | -51.6424 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d6db5f9-938e-39d1-b944-b75bd7f9274e | -1.18837 | -52.15773 | 2024-11-09 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4d1848f4-cede-3170-9916-773387b05744 | -1.14007 | -53.65836 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d96ab329-e4b9-37cd-a982-bb205310c85e | -3.17634 | -51.31013 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5b07d89f-dece-33cb-96dd-589ed1ca3b7c | -3.06508 | -53.90604 | 2024-11-09 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32c6bcfc-9c47-390a-b962-7792ae7b485f | -1.83281 | -55.19524 | 2024-11-09 05:20:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5087e6bb-bcf9-359a-be03-9a858b8833cb | -3.88278 | -53.38956 | 2024-11-09 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26d20096-3ab1-30d3-9e4c-f3e725f87e8a | -3.23485 | -50.45786 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c1bf3364-a49a-3470-af01-8bd0c47105e3 | -2.34559 | -50.5172 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f9122e4c-9779-3cdb-9e42-6da1e2d13fda | -2.92222 | -51.67303 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 109cafbd-a437-3c15-8abd-87246ed35316 | -2.57825 | -49.14453 | 2024-11-09 05:20:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 302230cd-52eb-3953-bfee-40ca1743cc15 | -2.06561 | -53.27817 | 2024-11-09 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6967b9f-cfa4-3f15-8b70-f6f61f6d8a58 | -4.20905 | -50.62546 | 2024-11-09 05:20:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3817354b-f936-314f-8432-d46ab7626e12 | -1.44642 | -53.00471 | 2024-11-09 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 56dda4a5-b711-3638-aa58-b4b1e0f6b556 | -3.18266 | -50.5843 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c4981de0-61d1-34d4-9a43-6f57e6985663 | -1.75858 | -54.38297 | 2024-11-09 05:20:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd87dec6-cb83-3d52-b197-45d8a2cfede2 | 1.30969 | -50.73063 | 2024-11-09 05:20:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98fc723a-cefb-37a2-8501-268d2dbe2b1b | -3.60451 | -51.24799 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 163fb076-974a-3cba-8203-610a9d8aaf83 | -1.77883 | -52.35384 | 2024-11-09 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22191228-b6f6-3ed9-9fb4-4a4575910ddc | -3.0255 | -51.09521 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d196406-8b7e-390e-ba94-46d27f22917d | -3.95866 | -59.1828 | 2024-11-09 05:20:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22788435-89b0-3f26-9269-5065d80148bc | -3.11711 | -50.15489 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64dd94d9-3e05-35fc-bcc7-43e924e3d9b3 | -3.63463 | -50.75977 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c961af2-d93e-3292-9197-97a1ce3b255e | -3.59342 | -47.35831 | 2024-11-09 05:20:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 30fb70e7-3a31-34ab-9ffc-c7baf45cbca4 | -1.12752 | -51.9468 | 2024-11-09 05:20:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6ec7102f-a798-3908-a3ea-439427160895 | -2.92031 | -51.68565 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2305500d-492b-37bd-ba64-07444df2e8e2 | -3.26661 | -46.32196 | 2024-11-09 05:20:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| eb95c82c-0ce1-324e-bdfb-1b436bb6b615 | -3.58414 | -50.23694 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a42264d9-7f01-3b2b-b81a-16dccf86fd9a | -3.09729 | -53.32949 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 55265898-bf0c-3eb8-b72d-0cc99b1adf67 | -3.59004 | -47.36172 | 2024-11-09 05:20:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| fef821eb-fc29-39f7-a4be-b6c9a20bc372 | -2.97414 | -56.88573 | 2024-11-09 05:20:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a899ec94-bd53-30e7-9163-ff8480a117b3 | -3.51015 | -51.67843 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 88fffb00-5bf3-3cf1-9e94-abad31495673 | -2.67844 | -51.82791 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ab577138-23af-3c4e-95a8-fd4e574d3935 | -3.69974 | -54.62006 | 2024-11-09 05:20:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 727e4c64-1e4e-300a-ac45-3f3d34203751 | -2.98424 | -51.46021 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0489329f-583b-35e8-b7e0-7023b73b3a18 | -2.23842 | -53.77181 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 19ee2a91-cae2-3f11-832e-2775bb6ca4fb | -1.41413 | -54.76593 | 2024-11-09 05:20:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60e194a1-a348-307c-b676-79196481bba7 | -2.87537 | -51.47126 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5c9d7ce4-64d0-37f1-9d1f-51db1cbb8ed0 | -3.25724 | -51.13063 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7abf99c0-92d4-37aa-a972-5db32a3f099a | -2.77082 | -54.05374 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ebbad709-7074-30d9-a4dc-63b94b6f8c58 | -2.15896 | -53.69924 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14de75fc-3435-3154-9764-342e0d51bfee | -2.77316 | -52.86981 | 2024-11-09 05:20:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0bd3b0b-ba64-363f-9ede-7b16e6328463 | -3.76338 | -51.76619 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 406b8102-ab54-3dcd-9700-503fe40f0766 | -2.83184 | -51.80386 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85809d0d-10c8-38e9-82bb-99e3dbfce225 | -3.04019 | -50.37385 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e22bff5d-6a6a-3e54-a415-ae2656edf559 | -2.86758 | -54.09911 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2ed3640-3d30-37ea-855a-aa25b63f6252 | -3.22358 | -50.38486 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1fc5412-8526-34f7-b601-efab0af50b21 | -3.07231 | -50.56938 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 536e4cca-752c-30d9-9c6e-e93b8134493b | -2.96568 | -49.28994 | 2024-11-09 05:20:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03cfd0b6-de92-30c9-be1f-2fe5939e160e | -1.41287 | -55.38167 | 2024-11-09 05:20:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4bb8831-90aa-3b55-85c7-27c43bcbf1b9 | -2.97074 | -47.92379 | 2024-11-09 05:20:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5620ddfb-0b63-3305-bd4b-32ba3060d7eb | -1.41252 | -54.77285 | 2024-11-09 05:20:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9290ad59-c133-37fe-aadc-502cab63fe5a | -3.25584 | -51.13307 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad3ec6d8-acef-3ff7-9224-dfda93121888 | -3.33543 | -50.0872 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 35517a1a-b86a-3077-aed4-68ab257f3dec | -3.38681 | -52.3547 | 2024-11-09 05:20:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 46a62274-d2c6-302e-9f8d-48bcc278277c | -3.30251 | -50.08598 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3a2f483e-cca5-31e1-b240-cd909bfe7996 | -3.50245 | -51.02942 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8b7e7ce3-3dad-3cfb-9899-89b549d3035e | -3.92506 | -50.2505 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 342e744c-fdc0-3859-a02d-b0c9938fd861 | -3.30193 | -50.08243 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc1989f2-cdc3-3ffd-b35b-2d7c603d6519 | -2.61947 | -51.75142 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README109.md)
