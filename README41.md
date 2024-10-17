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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bce5d792-5fa2-37ad-bf04-cd7033d84628 | -3.50649 | -51.10494 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 72df0dc9-ce0b-3ee4-881a-a5a475a6c902 | -3.50646 | -51.10761 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 7faf5695-8d22-3bed-9db9-da82fc92cfc6 | -3.50578 | -51.11218 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 3e081741-ccdb-3ed5-9b73-912e1ef8d458 | -3.50578 | -51.1095 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| d8a7e87a-cce5-3cc5-9720-b8c584ddfc63 | -3.50271 | -51.10435 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 17509e75-18c0-32e3-88b5-c6678b481edf | -3.50201 | -51.10892 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 8b1025b1-11c9-3337-bbf7-8599b45b7cbe | -3.49894 | -51.10376 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| d3d36395-4347-39d9-83e2-6159e2e8ddd1 | -3.57572 | -51.57319 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3a11c4c-cc37-3e8e-9d70-7a1b2e14599c | -3.55368 | -51.54959 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e0b1450-3c87-31c5-b3d4-37ed2968f27f | -3.54364 | -51.29465 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55ffe70e-c479-3108-8056-8d4d6fbb052b | -3.54059 | -51.2896 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ff057ccc-0065-37a9-a77b-d09b2c0a8ad1 | -3.5399 | -51.2941 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| acca785b-179f-3043-bb55-edbb73bab473 | -3.5192 | -51.60197 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98f4b965-d3ce-30f7-8d41-63e421bc8bbb | -3.50217 | -51.5905 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 09b82c16-5c55-3410-853c-f64cf0fb5d99 | -3.50061 | -51.67386 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 03ad8eeb-2c0c-3c7c-ada2-efc92262b424 | -3.49696 | -51.67329 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cbdef68f-ff06-3136-ad35-1853c2c9fc2e | -3.4963 | -51.67756 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| aff1bb3c-b401-3c7d-82b2-e2c2dabe5235 | -3.49476 | -51.31473 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d41422e0-d1e2-3e69-b72b-39f62831d2a7 | -3.4933 | -51.67271 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a82174cd-b527-30ed-8bff-10381a630e88 | -3.49265 | -51.67699 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 553ae505-2ae7-3dcc-bac4-45a260a2e975 | -3.48615 | -51.59694 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ccb3b3d-c576-35f8-a208-4704ed0115b7 | -3.46169 | -51.65911 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0983c86-b054-3af2-837d-16c36d7f5a64 | -3.30474 | -51.10918 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6859119d-084b-3c23-bc65-839c621aae3c | -3.30445 | -51.48785 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8f8feba-499b-30c9-8a8a-4edfe25b7b7b | -3.28391 | -50.93864 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6bf1dd4b-415c-3853-bcff-794996f957ff | -3.28082 | -50.93338 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| acc71a9f-a239-334b-90e3-11b476c3eb2d | -3.2801 | -50.93806 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02f95ed3-e1f1-372f-9263-0deb1e26f5fc | -3.21126 | -51.00816 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 240c452e-8402-3c3d-8fd5-8d55ec592366 | -3.16928 | -51.56211 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9086da8-e981-3f30-adae-5977274c9d5a | -3.16495 | -51.56586 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d0766dbe-728c-3148-be68-2823411e37c6 | -3.16212 | -51.05027 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d5e48e08-84e6-3181-a959-9cd10af61e5a | -3.16141 | -51.05486 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 43f56f9f-70af-3f89-871f-6fc50874bf5f | -3.16108 | -51.30388 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc9df7f4-f907-369d-b90d-e20b4918da39 | -3.159 | -51.30588 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 056800ea-c1d5-3d44-8080-c4bde6b2a5ad | -3.11253 | -51.93226 | 2024-10-17 05:04:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7e29f33-840d-3824-8028-ec6290bf08c8 | -3.10296 | -51.28601 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4056b33b-57cf-3f45-815e-3fdff1911ab2 | -3.08775 | -51.21049 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 96efd22c-6148-3d44-97b3-a121f9bdb8d1 | -3.08707 | -51.21501 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 894450d7-1448-3656-ba79-73e6a99759d4 | -3.08402 | -51.20994 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0682a79-7d7a-302e-90d1-1b3161368875 | -3.08334 | -51.21445 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3b688c72-34f9-35c2-a680-0152f8d14902 | -3.07665 | -51.62856 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bec9b75d-3280-3651-ada1-10d3499ecfbd | -3.07551 | -51.19032 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ca53dd7-b7a6-3546-9761-0c820514a45d | -3.07245 | -51.1852 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e2fd03d-dfce-3ac8-9b7e-d3ba83fb0a77 | -3.06485 | -51.05143 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b70e39c8-f7d5-358b-a170-843bf1d4d123 | -3.06372 | -51.24335 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 49d70525-5117-3caf-9ed7-18bf0814670b | -3.05873 | -51.04114 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34e6a459-f441-39b4-9f58-edb6158c2031 | -3.05802 | -51.04572 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2bf9d689-bcc4-3abc-b532-1e80179f478e | -3.03388 | -51.22674 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 77a98ad0-384f-3fd9-b249-93ac2282233f | -3.03015 | -51.22618 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3904842c-1316-3e8b-9f64-7dc49dd284a4 | -3.02946 | -51.23065 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e5a8316d-6f77-3066-a3f7-024d3ae43e32 | -3.0184 | -51.3512 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5631c7b-45aa-3324-9ff2-042c5851472d | -3.01539 | -51.34621 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 998932d3-c6f6-31c2-b181-2ad7ddde30ff | -3.01169 | -51.34562 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f45e0e23-e404-3368-9af2-c56e17fe5797 | -2.99434 | -51.00775 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 553fbe6c-5530-3f78-a66d-339fadfc854f | -2.99057 | -51.00717 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9d6adf78-011d-3fc9-8ed0-a735ab554e20 | -2.98983 | -51.00951 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0065f2ff-6928-34fd-ad05-44cbb75a5fff | -2.97199 | -51.3576 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b383fe5b-b25a-3fec-bbd0-e119531a8f92 | -3.2751 | -50.66027 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 754a1f79-b607-3187-91da-cf431e8ef226 | -3.27438 | -50.6651 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dfdffca5-9247-3376-9edb-ba5256858674 | -3.27051 | -50.66447 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf4046b2-ac02-38b5-aa74-eba1e8c6f0d0 | -3.24771 | -50.76431 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 293c4cc8-3b71-3335-895e-eb4635230582 | -3.2388 | -50.85012 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6348237e-95d4-3be7-870a-2e13ff4235c3 | -4.65907 | -50.93813 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 769f7f59-7acc-3479-baee-2c1f33663649 | -3.88489 | -51.24305 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c24288f0-292f-3666-b83f-6e9e8cced5eb | -3.88234 | -51.92149 | 2024-10-17 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 702f430d-f780-3702-811a-57d8ffcec22d | -3.88135 | -51.83043 | 2024-10-17 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14fae4bd-c8d6-3b9f-a55d-884edda299c2 | -3.87871 | -51.92092 | 2024-10-17 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 92a8f133-66f9-3b81-bb5a-21f41e85d49e | -3.87763 | -51.97642 | 2024-10-17 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2e8ce8c5-20e3-3af1-8e23-38d8f637fd8d | -3.87699 | -51.98059 | 2024-10-17 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2ce5db1d-de5e-3751-b5fa-b8d16be3717b | -3.83713 | -51.90152 | 2024-10-17 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b8c13c29-eeb9-3da4-a347-b52f7c92601e | -3.83586 | -51.90998 | 2024-10-17 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 24cc5ef0-e2c8-31e1-8a45-1ee86edb44f7 | -3.83522 | -51.91418 | 2024-10-17 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d829a44c-79ce-3e79-a000-17b2c8250138 | -3.83349 | -51.901 | 2024-10-17 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6cdf5480-dd1d-312d-bb06-45473d4c7e0b | -3.81509 | -51.69947 | 2024-10-17 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c859461e-8394-3ee1-8771-e4f17628876d | -3.81077 | -51.35269 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e96f0fd-f430-341b-8f46-85e9b33c6845 | -3.81004 | -51.30614 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b9b6919e-0a34-38b8-b20d-485f3cbdf64f | -3.80939 | -51.30316 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f01e9b35-e118-3345-bbd3-7a738a791c08 | -3.80869 | -51.30764 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0df64784-d01e-347d-a709-dc7ff7d240ec | -3.80764 | -51.2965 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 515356ad-da87-35b0-8bfc-1ead8bebeb0b | -3.80697 | -51.301 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 92159805-8483-3e6f-beaa-d20753d975f9 | -3.80635 | -51.29802 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d438205f-f061-3cbc-bfba-1cb36e81896a | -3.80631 | -51.3055 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 72e96156-5fdd-3941-8227-1701d3e8b7d2 | -3.80566 | -51.3025 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0f2e772a-7628-3a83-9dab-1647b0ecdc0b | -3.80469 | -51.20926 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 81186215-26b6-33a0-a143-8b6ad47a821c | -3.8039 | -51.29584 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 81800b87-6566-3186-b03e-e910d9af536a | -3.80323 | -51.30035 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ae6bf5e1-2e28-37b7-8257-e2c3db07c8af | -3.80261 | -51.29739 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 726b12ca-fa0e-3e6b-84f6-0fc63dadb361 | -3.80191 | -51.3019 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5e7e905a-e8a2-33be-8317-cf884bebce51 | -3.80105 | -51.3922 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 90b26c4c-8126-32b8-abaa-764cf6bc34a4 | -3.79985 | -51.38911 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a01f6954-181f-329c-bcb9-23adc25a2f58 | -3.79916 | -51.39355 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 57f9eb03-07c0-3e84-b512-25d1142ebba0 | -3.81305 | -51.15501 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e52b0e38-b5b7-3459-9675-dbd15d0496ce | -3.79889 | -51.60831 | 2024-10-17 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 717eac73-2f12-319f-a63b-e34bec99f5cd | -3.79731 | -51.39167 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8ac6c7b7-ac95-399d-9661-3423a4e54158 | -3.79455 | -51.61209 | 2024-10-17 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e31d1a8c-a239-32fa-a1ce-b0d3922d64a5 | -3.79389 | -51.61649 | 2024-10-17 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75820ff5-fdc2-33ae-a62d-d2b8b152ba39 | -3.77928 | -51.3492 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c2688b10-6f8a-35b2-8f3c-1cbf2a4b8d73 | -3.77859 | -51.35372 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 315d6e04-b768-38cb-a55c-117b589b422c | -3.77555 | -51.34861 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e0db0a1-f818-3bab-a530-0cc69625af7c | -3.77486 | -51.35312 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README42.md)
