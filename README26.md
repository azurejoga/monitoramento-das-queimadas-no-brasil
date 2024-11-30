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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b02bab9c-483c-37fc-a97f-1805b94f53d5 | -0.39007 | -51.57373 | 2024-11-30 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb834021-887e-3dcd-a1f1-72dc828a1070 | -0.26565 | -48.62617 | 2024-11-30 04:38:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3d859ca5-10dc-3d76-a6e9-d08cbb4556af | 1.87568 | -55.73411 | 2024-11-30 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5442c74c-0e61-37fc-b86c-fe118d1d1d8e | -3.2406 | -53.6393 | 2024-11-30 04:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 57a90995-311a-3e95-aaad-ca99972cd4b6 | -3.5876 | -49.9791 | 2024-11-30 04:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 83eca751-035b-383b-932a-741cb0b1b0f8 | -3.4791 | -53.8142 | 2024-11-30 04:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 98b319ef-4e04-37fd-9c96-a5be474a33e5 | -3.6061 | -49.9784 | 2024-11-30 04:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 13adf893-4204-3908-80fc-86ebdb86acaa | -6.8967 | -43.5436 | 2024-11-30 04:40:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 85b0cb6f-2671-3002-bdef-e0dafbac1973 | -1.6419 | -53.8731 | 2024-11-30 04:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 118.5 |
| 0785fe36-bfd0-3eee-8618-7169b5855534 | -1.0733 | -53.6378 | 2024-11-30 04:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| fc6972a3-be94-3763-97b8-e97cee4ab6fe | -6.9153 | -43.5652 | 2024-11-30 04:40:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 56.6 |
| e59d612d-eb1a-3583-aa20-9ed9e85396d5 | -3.2591 | -53.6186 | 2024-11-30 04:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| f65e3a02-826a-3ce7-965c-419d1e829ed1 | -6.9156 | -43.5418 | 2024-11-30 04:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 143.2 |
| 20013fd7-6039-3475-a696-5159eb7c2be2 | -3.606 | -49.9995 | 2024-11-30 04:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 3bc7e104-d685-3b91-ac6c-face3fe37c00 | -1.6938 | -46.7833 | 2024-11-30 04:40:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 3cde42c9-7258-35f9-9fcf-68ca5e451a5f | -3.259 | -53.6388 | 2024-11-30 04:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 7eb32056-2276-3f8b-9c98-d1837a12a555 | -0.25325 | -53.75909 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ba864d88-2620-3889-8b58-2f9af5163225 | -3.50971 | -54.53021 | 2024-11-30 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5d40cf95-0bf7-313d-ade4-84d4ddecb93a | -1.34015 | -55.90515 | 2024-11-30 04:40:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 13a0080d-9fb1-3e2d-b3a1-cb7141357dc4 | -3.26078 | -48.76479 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef9ab2bd-d169-3b08-9701-c472b534c0b9 | -2.71583 | -46.11827 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 88bc03a3-6dc1-3bab-b5a6-58e8d491821a | -3.33212 | -50.22364 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f114fb3a-868d-339e-944f-5aa7b9aec551 | -2.63188 | -46.87747 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cbf37479-1880-301c-8108-726e62834cb0 | -3.31314 | -50.27886 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16efca2c-3243-3ed6-986f-b90a84427e9c | -2.87422 | -48.10293 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90a2f803-47d2-363b-8cc8-05768e7c895b | -4.05865 | -49.05854 | 2024-11-30 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3cb62a34-aade-3fc3-aaf8-a3e37eaab2dc | -2.47669 | -50.36911 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f334f29-5708-3ee0-ad96-24467eda857f | -2.76469 | -54.04951 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2e54ad84-3a60-32fb-a134-113274fb4b15 | -3.24497 | -46.42444 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9dfb1604-e0d0-35ef-b30c-5363db36c57c | -3.28069 | -48.77139 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9c58307-f2d6-3b90-b485-9d5d78593fdf | -2.01957 | -46.40974 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e9df1ac-4f0d-3903-8857-3770e87c9c6c | -3.74949 | -54.68061 | 2024-11-30 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 119373eb-6066-376e-84ef-334feb56f95a | -2.35522 | -49.00943 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 76e30dc7-7184-3878-b4dc-34840d092f6e | -2.613 | -54.33819 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b533639f-8de9-30ea-aedb-03c1061ade1e | -4.86353 | -41.30126 | 2024-11-30 04:40:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 53171a68-9f85-39b2-8b56-7f326f662dac | -3.26958 | -50.20672 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7b03223f-2854-3e99-93f5-e5e68b3bdf2c | -3.60096 | -49.98469 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 124.2 |
| 57a57f5e-a6ac-3a47-9807-515507dda027 | -2.95038 | -48.07243 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3fc5fdd-8548-3f53-901e-b5a01d2930ed | -6.91072 | -43.5476 | 2024-11-30 04:40:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 17bc25c7-8063-3d92-b852-dd762f476326 | -2.90149 | -51.57713 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6af18f03-ec8b-3cfb-a0be-5133431b2cc0 | -6.7058 | -47.26659 | 2024-11-30 04:40:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 634d9b88-ec0c-31d9-926b-39531502e719 | -3.23506 | -50.44593 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b17e20ea-69ea-374f-956c-ccecef201ea8 | -3.35378 | -49.76015 | 2024-11-30 04:40:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d7ef0810-2a7c-37b7-b206-83e9441359b0 | -2.63593 | -46.57452 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad7be5bf-fb83-3c6c-89a9-ab4688dc6383 | -2.70792 | -51.97403 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 672bfe34-255c-3dde-bd85-654793e9c740 | -1.06203 | -51.75633 | 2024-11-30 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a93cd3bc-8885-3069-87d6-0264fcb331de | -3.97748 | -41.51156 | 2024-11-30 04:40:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| e66a69a5-18b1-3cb5-9aff-e004bb576343 | -3.80471 | -52.10197 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1c31df62-ef1f-3eff-b56b-4938dfe4ddce | -4.05056 | -48.08104 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb9d49f6-a2f7-3f2f-b3a3-66f28440d855 | -4.8686 | -41.30116 | 2024-11-30 04:40:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 8abd4316-1fa2-39a5-931b-8f48717e9bbf | -2.22692 | -50.50882 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ad69ea2-4233-3c01-b43a-d97d891a1c4f | -1.63371 | -53.86621 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 051cad50-46e6-3f07-98ee-bc687d266a5f | -3.99343 | -41.50338 | 2024-11-30 04:40:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 25a45aee-87d7-3969-b33c-99d87167f958 | -2.93783 | -48.61208 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1846b340-2250-329e-92a9-7c43688c4e70 | -2.67978 | -46.27891 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d5ac212-76e3-3efd-9f97-cdf70655ab32 | -1.13204 | -53.39108 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dad2fb35-157c-3583-8bae-b19902af683f | -4.85125 | -41.31663 | 2024-11-30 04:40:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a66f6f7d-f2ea-3c2a-9e1f-7000996cb7e9 | -3.81031 | -46.53829 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 41e9f126-9ed1-34af-ac56-176dd339f165 | -3.039 | -51.7845 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7548c21f-b929-3184-87fe-6502b6aab903 | -3.12236 | -50.17311 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab5285a9-0d4c-32c8-9418-288867e47848 | -3.09349 | -53.29673 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| be103928-3a2b-3bc3-bf65-f3895a375ddb | -3.39002 | -54.28643 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29c3214a-2b88-3aa8-a406-0afcd93a816f | -3.38412 | -53.50806 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 778a4759-7ae9-3e4e-a8e6-6b480898d2fe | -1.06566 | -51.75689 | 2024-11-30 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 47f28e97-c62b-3921-ba72-549a73c3a1b0 | -1.15014 | -48.33932 | 2024-11-30 04:40:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e49b67b-5aac-388f-a508-578e899347f5 | -4.36338 | -47.24985 | 2024-11-30 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47936bcc-43eb-303b-9620-cae2e10fc526 | -2.83326 | -48.47558 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0167c141-1924-351b-b981-382eb599df12 | -1.24847 | -51.74027 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d50b6dee-0308-3dfa-bde0-b19effa0b716 | -4.02595 | -48.87736 | 2024-11-30 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b19b7f54-2229-33b1-801e-e6cf5cd03899 | -2.89237 | -49.7522 | 2024-11-30 04:40:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1d72381-8ad3-3766-a567-3b2a7221635a | -2.14212 | -54.8888 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 4a47b4f1-61ff-3df6-b250-ff4dfe692d5f | -2.67749 | -46.27055 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7cd6dc14-46ab-33b0-a8b3-8b240f9621cb | -3.66926 | -49.89528 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4ac3e0c5-649b-30dc-8fc1-d75b4d17222d | -3.01243 | -51.85899 | 2024-11-30 04:40:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f57aa3a6-a19a-3b1a-b427-79f7c80953c1 | -3.83013 | -46.54933 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 51d24d86-bf2c-33fb-828a-8b6fce965059 | -2.60472 | -46.55502 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 42632bf8-912c-3529-a83e-b0dc72d6b778 | -3.04233 | -48.48727 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ca7af4fd-279c-3f6b-b3b8-6f8dd1624b18 | -3.55251 | -50.4038 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3995ee44-3224-38f3-bbe7-65e73d312ad3 | -2.93422 | -48.00164 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e51ccfe7-102a-3aa8-a2fb-36a6ef8b2900 | -2.56787 | -47.35963 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b70f98c-6506-3435-8ea7-7abc1906a587 | -4.04604 | -46.84875 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58a43af1-8cee-37a8-953b-96ba4dccf373 | -2.3464 | -53.92514 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 935392fd-0700-3821-b4b6-65927dd7e017 | -1.10354 | -53.39023 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1cbf4046-5776-35c1-a540-a2c54d455169 | -2.92648 | -48.0076 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a633f37-9198-37cd-9696-327a5e46002f | -2.82348 | -51.79395 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14fc62ac-a8f2-3317-816d-7ffb50332552 | -3.43695 | -50.03113 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9b035116-c31c-35f1-b75c-1e22a0c3542f | -2.44449 | -53.62481 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4402b99a-d4ce-3f36-b86b-24150ead90b3 | -2.63448 | -46.19997 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d48e3477-0a60-3c45-8d18-a2dc4d0f216f | -2.14725 | -50.9068 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb4a66d7-623f-3fa9-a2c9-11f3e0909703 | -2.6922 | -51.98006 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 05d534ce-87dd-325d-9ba9-4b70ce298db7 | -3.00731 | -53.2319 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cc67530b-2b39-3e88-91b4-196b65af988e | -1.05421 | -53.21344 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6e58881-d019-3e05-a633-5f2898316af0 | -2.20582 | -48.55001 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b76f29da-e073-3d4e-8c85-f03fa788d860 | -3.34275 | -50.51831 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 470372b1-615e-30c9-b7c4-d3142c61e253 | -3.49499 | -51.56586 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 23ad1ef9-aed7-3c81-a653-7bdc4d1116b2 | -1.8884 | -48.95061 | 2024-11-30 04:40:00 | NOAA-21 | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47f8b65b-8277-3116-ac90-e75d5638d231 | -2.4584 | -48.54743 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8fccdb9f-4574-33a9-ac51-9ee69e27cb12 | -1.59757 | -55.55678 | 2024-11-30 04:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| af8e385d-e6e4-3963-9b3c-1ee6d0202ee6 | -2.5995 | -54.09025 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8c4664b5-9ed0-3308-b964-d40868c0fdfb | -2.91677 | -48.33358 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README27.md)
