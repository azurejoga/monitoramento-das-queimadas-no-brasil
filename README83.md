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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1082b28f-a384-39ce-90b2-046e10f259ad | -1.52895 | -52.66408 | 2024-12-01 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1422aaa9-06d2-3ce8-82c2-30d7cbc482bb | -3.11174 | -54.03976 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8b0d2ea-1def-3205-a39f-3ec78e742291 | -2.40399 | -53.86536 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 308fcd06-ee28-383c-bc97-4816c6ed743c | -3.33011 | -54.14714 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57f01fb4-10e3-3c0c-b9cf-b17eba0cbb04 | -3.10825 | -54.0392 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d84a53af-e40f-3613-a609-b5d9807e2c38 | -3.51406 | -62.76207 | 2024-12-01 05:08:00 | NOAA-20 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eff7bd45-60d5-3a7d-8677-82f0202ca782 | -3.21746 | -54.174 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 07a1762f-94b8-3fab-97d4-9fbdbdbeca63 | -2.58165 | -53.67773 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f49637e-00ca-3321-a088-b510e01f66c1 | -3.02412 | -54.06676 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 97f988ab-e268-3306-9285-8915713e240e | -6.18554 | -44.42664 | 2024-12-01 05:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fea16598-d273-38fb-a2ef-1d5489449803 | -5.42559 | -45.11016 | 2024-12-01 05:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4bdf918-7635-3fdf-8910-578a2b0715be | -1.82644 | -50.90375 | 2024-12-01 05:08:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 0452f102-873d-3eb3-8e60-7571a926efb2 | -1.63337 | -53.86239 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8475e174-8042-3681-a928-4be9c91a88c7 | -3.09424 | -53.13358 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| adbaf2ff-b2da-3e7b-9ef0-c5cf3fe67a2e | -3.2824 | -53.34827 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b6cb21a-0e50-36f6-a850-1cd1a0952017 | -3.41365 | -50.16409 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d50ae8c-d1c9-3b03-bf42-39aef523f899 | -2.89496 | -53.96809 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 238d544e-8534-33a0-bd48-b39318ca4ff5 | -2.83814 | -54.09517 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1b26b806-28b2-399a-bd97-f4f9fe31f2f0 | -3.6378 | -54.44629 | 2024-12-01 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3a86d6a8-c456-3612-bec1-b932a397061d | -3.14681 | -53.8361 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce58d37f-57da-3e39-bbfe-728a7d8e312d | -1.16594 | -53.77774 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b982c96-77c7-3148-b621-2deaba9a4f2f | -2.95767 | -64.99767 | 2024-12-01 05:08:00 | NOAA-20 | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 85a0734e-7ed2-3ffa-97b1-424527839112 | -3.25296 | -53.63911 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5c134982-b22f-33bd-853a-20e4834c5a1b | -2.5868 | -54.22131 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1e07ee5c-2cd0-3a1f-b388-5dc5c19f0dc6 | -3.18913 | -54.5143 | 2024-12-01 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 611638da-4aba-3122-bef9-ca609e3c428d | -2.59774 | -53.99259 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e525cba1-5e9a-32f5-9800-48d56c8a32ed | -4.26427 | -48.35929 | 2024-12-01 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9d4e23a0-6cde-3690-8e83-bddf75b162f0 | -1.92066 | -53.00821 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90bd62e8-c43a-3018-bf09-2badf4075d33 | -3.29166 | -53.28244 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6bc44e43-047e-333a-b2ef-7beee775d939 | -3.33657 | -53.30944 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ba7024e-f568-339e-ae8b-02500b38c241 | -3.10566 | -53.18197 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b4c813ce-a49c-3fec-8287-fe3ccf02de2b | -3.99069 | -47.91315 | 2024-12-01 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f81e2d93-02ab-3ece-a2a5-676aee61068e | -2.5917 | -46.94295 | 2024-12-01 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a71332db-3da0-3c65-b8ab-1ba97dae031e | -2.41693 | -53.85141 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2eca443-6f7d-38b1-afd7-ee1539a97dcf | -2.63265 | -53.99771 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ee1f0c3-6d36-3c30-b194-e5ac471cb11b | -1.68261 | -53.94781 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0270ee31-bc6a-35ef-818e-4a0d6518c801 | -1.60195 | -52.29956 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21dfbe34-d2de-348b-8fec-a1ec30ddaa81 | -2.6184 | -51.76363 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5ac44a18-85ae-327b-a329-1092212c6617 | -2.43509 | -54.01874 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1aae9de5-13ab-3348-929d-c880084fd71a | -3.32952 | -53.54615 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6bb03894-f4e7-30fd-a6b2-ce3cbf365f4d | -2.65303 | -51.87836 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 213f181d-47c7-3a87-ac45-929e4679469f | -2.19211 | -50.57257 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cea80843-94a6-3c53-8d1d-92d95b4f20f8 | -3.10355 | -54.04643 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f91f327e-29cf-3e91-9bb7-90d5428bb153 | -3.2632 | -50.2048 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9e2e09d6-0b75-358d-92ff-6eab15fcfa2d | -2.87448 | -53.98483 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a736eb01-651f-3b0f-a1d4-5278f2c3e68f | -3.06414 | -50.32992 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7106aba-ce96-3797-8bf1-20e239b49a0d | -1.36333 | -55.15377 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ccb9ece-674d-3845-9bc5-ee919633681a | -2.99827 | -53.36845 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cddcecc8-3ac8-32dc-bc85-9b3fe220a006 | -4.07281 | -50.02587 | 2024-12-01 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 671a2c8c-db87-3366-9c98-54b4fc237ece | -1.73185 | -52.80145 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b758c04a-6bc9-34b8-badc-a676264aed19 | -3.09388 | -50.34648 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b0e3e37-bf02-3129-9671-ca1a038e0b77 | -4.99493 | -50.74411 | 2024-12-01 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d93d4d69-f547-3c90-a09e-ce60fa528b0e | -3.25125 | -53.62631 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ae9eac5e-8b0d-33a0-af0d-365115bf0815 | -5.31317 | -50.56833 | 2024-12-01 05:08:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67a5eba4-a539-3604-8692-bab7d2c859ad | -2.97364 | -53.28773 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 855c7c33-1716-3ad1-9aba-91742e5073dd | -3.50648 | -53.82747 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a6e2d364-b2ff-3381-9b62-a9b517e577fb | -1.41061 | -54.52508 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7b5f3cc-790d-3667-8eb9-be13dbec9aec | -4.61445 | -50.36452 | 2024-12-01 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c8c952c-e052-3f96-aa18-ed6d9f56fd10 | -3.27979 | -50.60829 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ee56bdf0-8ce4-3bf4-bd94-b577ab89629e | -3.29205 | -53.66971 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc74e6b9-a5b4-3cbf-a0fc-1489ccc6b407 | -2.991 | -53.88633 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5d233b91-a85b-3c7a-b299-e4d935fb3d74 | -2.76591 | -54.19329 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98e8249f-cb65-34e7-8954-be82154570f3 | -1.7537 | -55.41424 | 2024-12-01 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f8a02c0-b2d6-31b0-8e0a-a7df3c212ff6 | -4.00324 | -44.75627 | 2024-12-01 05:08:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 1f20fd5c-d360-30c4-9e00-8c573a609c36 | -3.36582 | -51.12622 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c6c92c8d-1eba-340b-af9a-4724cf8b1f01 | -2.84346 | -54.04734 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2bdc64fe-b9ba-324f-a2df-dfc64590b462 | -2.88184 | -54.21391 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 76a3773b-1caf-35bf-af96-a4e1c46b82f7 | -2.04699 | -54.66904 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a9785e14-3452-310e-8a7a-1d729e2037b8 | -2.63022 | -51.76541 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8fd203dc-88ed-3e1a-a230-3a3f2e24aca0 | -1.44567 | -54.52269 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4744d1e3-56aa-3049-a7bb-f86e689625e2 | -2.58799 | -54.21376 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c302bedb-3fb2-3052-95a4-afea7f6bdd66 | -1.42511 | -55.27779 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 175fbcda-0bf8-3e20-bb3c-06771c0bc32a | -2.60079 | -54.08705 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 32cf3f74-1f03-36b3-8b1c-7a9645fbf494 | -3.18028 | -53.25688 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d4ac4ea5-caee-3396-b82c-176ac73256e7 | -2.63256 | -51.75034 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c12ef46-a76e-3403-949e-1ecf013bc046 | -3.26428 | -51.62849 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d56e8a7f-5af7-399c-afd5-044e30f8677f | -2.14736 | -54.87595 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 00bca4fd-8596-3216-9557-387bb8025f8b | -2.57763 | -54.21215 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 061a995b-0684-3f12-85dc-de6a7ce1a950 | -1.21045 | -54.16928 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95c0e210-e32a-368f-8f68-1fa33db5b30b | -3.47905 | -50.44207 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54678233-3cb2-3990-ab80-3e9ee930c0e2 | -3.41919 | -50.18718 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b880ee81-273e-324d-b2ee-d2e99b050b4a | -3.25482 | -53.6269 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5b8a13d3-2afe-3f01-b879-94a154b4912a | -2.76328 | -55.34122 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3bd705ba-454a-3352-ba85-2b37e96a0a37 | -4.31685 | -48.21329 | 2024-12-01 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6335b482-994c-3539-916c-d26699a56efd | -2.34329 | -53.86405 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc996a1f-2c30-3ab9-95fd-fdf154790413 | -2.48726 | -54.02682 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2364630-741b-39c5-a33d-473c7d25a9a8 | -2.86742 | -54.00754 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 34035b42-ac04-3426-b135-2bc771571466 | -3.1462 | -53.84002 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ebf0132-d5e8-3182-99b3-4a79fe556c1e | -3.49399 | -53.83776 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c043ddc9-8a42-36c7-b478-0f7074bd2f49 | -3.27137 | -54.10324 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aa0a7ae4-6c86-3e19-9e56-6026488aae45 | -2.92217 | -54.26622 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9258c5cf-f5d3-3089-8847-2c2348c0c459 | -2.973 | -53.29192 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2dfc043d-c2ce-3ff8-8b64-79b0bb20d6cd | -2.80753 | -54.06297 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ddfb20ee-326a-35d1-8593-cc36746f3b17 | -2.98675 | -45.57492 | 2024-12-01 05:08:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 239d2380-9328-3153-a1f4-220770cb58a6 | -3.49181 | -53.80496 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 558bca59-e7b9-31a4-8ba7-7ebb3c583bea | -3.03532 | -54.04076 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa741d76-6708-3622-adc2-88c752de2a5a | -1.64078 | -55.07096 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0b4a312-13a5-3a29-8756-82a7ea8f56aa | -3.70839 | -51.06382 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7f878aec-423d-3353-957c-e90bbf866258 | -3.02496 | -53.41047 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bdfdab5e-8aaa-3c34-a04e-40eb406b9fc3 | -1.42897 | -54.94782 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README84.md)
