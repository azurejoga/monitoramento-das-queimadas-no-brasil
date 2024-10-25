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

## Dados Diários - Página 183

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d2e2a287-68e9-3f0c-899c-c486cd126374 | 0.13848 | -51.06868 | 2024-10-25 16:54:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c630bfb0-96b9-3167-96e2-f8ff82d5c003 | 0.13794 | -51.07217 | 2024-10-25 16:54:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8e0413f0-5cf7-3b85-a517-49d37c713ea5 | 0.12411 | -51.07363 | 2024-10-25 16:54:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ba9fb88-4eaf-325c-9d72-c6131a8190f9 | 0.11078 | -49.91755 | 2024-10-25 16:54:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 5134a2c4-a0f2-373e-8db5-b7a91fa2ba23 | 0.1086 | -51.24198 | 2024-10-25 16:54:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e49d0d0d-2b3b-38f8-be0f-07b8b4dd3767 | 0.09846 | -51.13031 | 2024-10-25 16:54:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6aee3a3e-de95-32f5-a048-f7154b5fdce8 | 0.08441 | -51.17796 | 2024-10-25 16:54:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 22c96eaa-d769-3bf1-876a-a3ac1be60d5b | 0.05339 | -51.26831 | 2024-10-25 16:54:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9c07f4ac-b198-3d70-8bb0-7ea5f9078f27 | 0.01811 | -51.1885 | 2024-10-25 16:54:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| faca8713-8e92-3a72-9cc6-40eadba18179 | 0.00286 | -51.22165 | 2024-10-25 16:54:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3a652e14-139a-39ff-9c12-2764dc0a3d97 | -0.02837 | -51.33726 | 2024-10-25 16:54:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 6afa0d51-f300-3a38-91fe-7ccbcba6d5ea | -0.00079 | -51.42265 | 2024-10-25 16:54:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 38d48415-d0e8-3e4a-b44e-5af26a3b1df8 | -0.00026 | -51.4192 | 2024-10-25 16:54:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 7.2 |
| cdb86931-0558-35bc-aa09-2d4bb3836a70 | -0.56562 | -50.14141 | 2024-10-25 16:54:00 | NOAA-21 | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8828de57-8c16-3d51-bd02-593f5f963917 | -0.36522 | -50.32013 | 2024-10-25 16:54:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b5ae3dbf-b48b-318d-924a-83bb79eef385 | -0.49063 | -51.38161 | 2024-10-25 16:54:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5fe8914e-9354-3f01-b99c-4e3f929b6b0d | -0.3143 | -51.40505 | 2024-10-25 16:54:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d6e2c5a0-9b82-36b0-8d7c-44176d26bd1c | -0.31377 | -51.40161 | 2024-10-25 16:54:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5a01a0d1-bc6f-3e8a-8828-ac199fbbb7e6 | -0.25212 | -51.51027 | 2024-10-25 16:54:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6e6dfcf3-396b-376f-89f6-e0fd5a7a826b | -0.17479 | -51.38111 | 2024-10-25 16:54:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 15c18588-7f76-30fb-a207-59b8bd2fb188 | -0.16247 | -51.32298 | 2024-10-25 16:54:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 240771dc-b68d-3886-a991-0e0d126d6eb5 | -0.16194 | -51.31953 | 2024-10-25 16:54:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9372a896-1bd8-3cf5-b909-e76affed2534 | -0.13411 | -51.31759 | 2024-10-25 16:54:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f2b2a457-a4ec-3a6d-b026-a484c38935a2 | -0.10934 | -51.31075 | 2024-10-25 16:54:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4c458aff-e811-3b18-b726-98207d3cbd11 | -0.09887 | -51.3088 | 2024-10-25 16:54:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9575613c-d2f9-39a4-8bcc-db6195c13cbf | -0.08589 | -51.26832 | 2024-10-25 16:54:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f5bef593-e78c-3aeb-aa9e-4dc932bcdb6b | -1.57312 | -51.39043 | 2024-10-25 16:54:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| adef92b3-75c9-38c4-9dfb-fd8f30306583 | -1.52389 | -51.11288 | 2024-10-25 16:54:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 184.1 |
| 7897c48b-0454-3bda-834f-b72d1a77b4ce | -1.52336 | -51.10944 | 2024-10-25 16:54:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 107.0 |
| e56b6c6c-1b6e-37cb-a6c9-2cd853ce0eb6 | -1.52006 | -51.10994 | 2024-10-25 16:54:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 107.0 |
| a4b5b43b-4e6c-3662-ba8c-f312aae0255e | -1.51727 | -51.11389 | 2024-10-25 16:54:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| de420424-ecf1-30cb-8226-31bb23964a71 | -1.51675 | -51.11044 | 2024-10-25 16:54:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e65f86bf-e407-395e-884d-fcfdc8a311a5 | -1.50266 | -51.23941 | 2024-10-25 16:54:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3583d2d4-b5bd-3ccb-b766-09bccda21450 | -1.49611 | -51.06417 | 2024-10-25 16:54:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d149af5d-d8e3-3a83-8564-07bd8783b0ee | -1.49386 | -51.07157 | 2024-10-25 16:54:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 92d44b50-bf8f-308d-bf30-4631959e7094 | -1.4928 | -51.06467 | 2024-10-25 16:54:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 57007e47-2b5f-36ba-b651-855888a721ab | -1.40752 | -51.6375 | 2024-10-25 16:54:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 08aed6ce-3160-3b52-9d3f-5adf62af8cd0 | -1.31569 | -51.24055 | 2024-10-25 16:54:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6fe29534-d637-3be7-aa0f-f0475a4cbe8e | -1.30193 | -51.63607 | 2024-10-25 16:54:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 401b2ce3-11b9-31f8-9603-b098194bcabc | -1.27351 | -51.20821 | 2024-10-25 16:54:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 8c2171c1-5f0b-3735-b774-6d0596ac966b | -1.18057 | -51.04673 | 2024-10-25 16:54:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| e853a1b0-2336-32ee-9a49-d114a16a1b41 | -1.1652 | -51.03491 | 2024-10-25 16:54:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d59c96d7-93de-3413-a6e6-e7deafecdddd | -2.17008 | -50.86907 | 2024-10-25 16:54:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 14136239-1149-369a-b023-10a18f93765c | -2.10482 | -50.59924 | 2024-10-25 16:54:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 88abfff8-fd42-3221-ab54-95b6cc15d773 | -1.97183 | -50.84063 | 2024-10-25 16:54:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bbd08c8c-2982-3c12-846a-00fb3ac95fd6 | -1.93453 | -50.86407 | 2024-10-25 16:54:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| b2231ec9-beaa-3044-9a34-b90acf53edb2 | -1.81904 | -50.66492 | 2024-10-25 16:54:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 8a0b6c82-17e3-3fc5-af26-887afa0b164a | -1.66585 | -50.70755 | 2024-10-25 16:54:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 458a47a5-e2ba-3b1c-8d8d-39105a99dcfe | -1.66532 | -50.70407 | 2024-10-25 16:54:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| b9ee5f0c-03c5-36d8-b611-ee78b2bffeb0 | -1.41562 | -50.53876 | 2024-10-25 16:54:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0a6a094d-554b-3942-b99e-900f6741aa67 | -1.39314 | -50.59251 | 2024-10-25 16:54:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 559f4e69-a3a0-336f-87ae-d7f2149bf5ad | -1.3637 | -50.44573 | 2024-10-25 16:54:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d9dadbe5-41f9-3199-8d31-b31ebc5c733b | -2.15464 | -51.01347 | 2024-10-25 16:54:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ec0dbd33-e7b1-3261-be48-103ef112c1a2 | -2.15411 | -51.01003 | 2024-10-25 16:54:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| fffde0b3-c68b-310f-9d62-c4922ae83089 | -2.1508 | -51.01053 | 2024-10-25 16:54:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 21808cfe-ed30-3889-9133-4dabba7547f4 | -2.15045 | -50.8976 | 2024-10-25 16:54:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0caec65d-6b58-3b73-b385-82ce74777988 | -2.15028 | -51.00708 | 2024-10-25 16:54:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2be4f43e-73e6-336d-9dde-fff95137a0e5 | -2.14697 | -51.00759 | 2024-10-25 16:54:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9f07417c-4c21-3deb-a2b8-a44bc8c58426 | -2.14644 | -51.00414 | 2024-10-25 16:54:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 59e3f3bd-d3a2-3684-a656-fab1fb0fcc23 | -2.11468 | -50.97369 | 2024-10-25 16:54:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7ab012f9-6a3a-30ac-91ba-b4983ac34c87 | -2.11416 | -50.88192 | 2024-10-25 16:54:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 88f57f55-5a54-3122-83ec-37817d2a6897 | -2.11362 | -50.96679 | 2024-10-25 16:54:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 5ebcbc02-22a5-3813-94fe-c09adad0f767 | -2.10343 | -50.92244 | 2024-10-25 16:54:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe0c88b7-36cf-359a-ab2b-00008e5c4c48 | -2.05932 | -50.92208 | 2024-10-25 16:54:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| bb1168a1-e480-3dde-aacf-132ad908489c | -1.92517 | -51.11269 | 2024-10-25 16:54:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 08dba8c7-4056-3939-a40d-7cd1188f6fe0 | -1.92339 | -50.87994 | 2024-10-25 16:54:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c0714ca3-fb7a-3cbd-9d4a-14585248855b | -1.92086 | -50.92986 | 2024-10-25 16:54:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 023e74e6-5c65-34a6-91e3-6d9cfd6ce531 | -1.83215 | -51.12773 | 2024-10-25 16:54:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4da9fab4-2a05-335e-87c7-2b4c6982bb2e | -1.8177 | -51.232 | 2024-10-25 16:54:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7f9a67bb-efca-3948-ac96-4bfa2508fa2a | -1.81737 | -51.03126 | 2024-10-25 16:54:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7c960707-bfdd-39a8-ad8a-be5eb1992a1e | -1.80956 | -51.04656 | 2024-10-25 16:54:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| d88eb225-1195-3259-9288-4e0e5c16cc3a | -1.75525 | -51.13665 | 2024-10-25 16:54:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 972117b3-9132-36a0-bbb0-735394e0ad04 | -1.75247 | -51.14059 | 2024-10-25 16:54:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 4008008d-ef34-34dd-87b2-c12780ff6893 | -1.75194 | -51.13715 | 2024-10-25 16:54:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 2e1e0cad-57ab-3994-b5fa-4f102f623e41 | -1.75141 | -51.13371 | 2024-10-25 16:54:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| bc466182-26e4-3f8d-ac1f-0ccf4db014c0 | -2.18353 | -51.13589 | 2024-10-25 16:54:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| e5c9f233-f16c-32f4-a362-6addbdf6033b | -2.183 | -51.13245 | 2024-10-25 16:54:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| e90a07df-66a9-3945-9c50-1dc4ab9f50fd | -2.18075 | -51.13983 | 2024-10-25 16:54:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| c5c64b77-0f1b-3e92-aa38-e7dac9c59ad5 | -2.18023 | -51.13639 | 2024-10-25 16:54:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 3e4af4eb-8a49-3e81-9aeb-052323e9d654 | -2.15348 | -51.42504 | 2024-10-25 16:54:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 3ff6b1af-f1b6-35b5-8371-cd14f732d657 | -2.1507 | -51.42897 | 2024-10-25 16:54:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e2a36b97-931e-3337-880f-a4deae772cae | -2.15017 | -51.42554 | 2024-10-25 16:54:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2d7c4853-97fb-3294-92ce-2435a5e5ceb1 | 3.86847 | -51.80085 | 2024-10-25 16:54:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0a42f6c4-22fe-32dd-a505-9ca82bac0d38 | 3.81715 | -51.75719 | 2024-10-25 16:54:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 2b3ea48d-33e1-3bee-a2f4-9e9351363c66 | 3.76866 | -51.83172 | 2024-10-25 16:54:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9358fb43-1aa3-3579-bb4c-830a21fe211a | 3.76812 | -51.83523 | 2024-10-25 16:54:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| aa4b3981-fc1d-3db4-a140-e507e808f24c | 3.7423 | -51.78115 | 2024-10-25 16:54:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 6d46de1b-05ba-3921-9070-3a7c46fc0f56 | 3.69787 | -51.37936 | 2024-10-25 16:54:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 11.1 |
| cca39a97-f0d9-3e36-8835-5e762b5245df | 3.69505 | -51.37528 | 2024-10-25 16:54:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 578fe68c-03cf-35cc-8f40-b689a4252bc8 | 3.64395 | -51.29089 | 2024-10-25 16:54:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 3e7cb656-f8a1-3081-953a-eddc636781fe | 3.6434 | -51.29448 | 2024-10-25 16:54:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 87780b24-3b7a-3be7-bfbb-4c6cb1f65380 | 3.64058 | -51.29038 | 2024-10-25 16:54:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 4f8819a6-c4b1-37e4-920f-e121319bdff2 | 3.64003 | -51.29397 | 2024-10-25 16:54:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 361fb860-2343-37b4-9aa7-e4605fd15fb1 | 3.60864 | -51.29657 | 2024-10-25 16:54:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7041ce64-0e0a-390f-a85e-165942398ea3 | 3.57114 | -51.40787 | 2024-10-25 16:54:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1d19cc39-78a0-3d8a-93d3-00419da817b9 | 3.5706 | -51.41143 | 2024-10-25 16:54:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 65194422-a98d-3d0f-aa06-ae9ddfeee132 | 3.56778 | -51.40737 | 2024-10-25 16:54:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2ab7b6d6-b4f9-3a23-b6b6-b6330f2516ee | 3.47659 | -51.49464 | 2024-10-25 16:54:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 300b600c-0d0b-39df-b41f-ffecc85089d0 | 3.46774 | -51.50779 | 2024-10-25 16:54:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 67e866b0-b3ee-3a90-8f01-4b6e58dfb2a3 | 3.4636 | -51.26305 | 2024-10-25 16:54:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |


[Clique aqui para ver as próximas entradas](README184.md)
