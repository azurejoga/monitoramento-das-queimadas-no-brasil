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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0792b248-63bf-397a-adfa-63856a934f23 | -1.47808 | -54.20569 | 2025-11-28 05:22:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 59ec0750-3a75-3674-a747-61b466abd7e6 | -3.68518 | -51.69995 | 2025-11-28 05:22:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d62fb848-8761-36e2-8668-ee1ded11ace1 | -3.22907 | -50.1494 | 2025-11-28 05:22:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0947b96-11f9-3811-8526-b2adc7d1587e | -1.33923 | -53.22498 | 2025-11-28 05:22:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7bdaf59a-105a-351d-ab9c-e74155c17370 | -2.95911 | -53.28607 | 2025-11-28 05:22:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0792445-7842-3590-bf33-449661199136 | 0.46076 | -60.44961 | 2025-11-28 05:22:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c89c84b5-edc8-3297-9070-bbe2301af561 | -1.47397 | -54.20508 | 2025-11-28 05:22:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a51eb14e-4a5e-3ca4-8bf2-ebed194b5a81 | -1.24695 | -54.06366 | 2025-11-28 05:22:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b45d9559-6091-3e3b-99a8-994e5257f2dd | -4.2333 | -55.67381 | 2025-11-28 05:22:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1659433f-451d-395d-a108-7c83a8e46bb4 | -2.56302 | -54.76116 | 2025-11-28 05:22:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f566d076-e0d7-3d9d-9681-85256a5e6b79 | -3.92931 | -50.16851 | 2025-11-28 05:22:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df3041c8-44b9-36e6-808a-d636c51fa2b9 | -2.95483 | -49.56378 | 2025-11-28 05:22:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 09ea86fe-f7c8-3ec9-ac69-f12b48780ecd | -1.82047 | -54.33493 | 2025-11-28 05:22:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 975c491e-df61-33ec-ad78-3cb65ccd4019 | -2.42115 | -47.23663 | 2025-11-28 05:22:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 10a31750-ef56-3ab4-a2d1-5fa7146b702d | -3.38712 | -50.25898 | 2025-11-28 05:22:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 87621de7-afa4-308d-8a5a-9f94686be534 | 0.7164 | -60.53815 | 2025-11-28 05:22:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 68236371-22f0-3d30-9303-bc889d50737b | -2.71807 | -53.18016 | 2025-11-28 05:22:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4c982785-5e45-340e-b105-ded4593b5a2c | -2.72811 | -51.83839 | 2025-11-28 05:22:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e2f9ece-a2d0-361b-9a1d-3b70febe838b | -3.27789 | -53.76636 | 2025-11-28 05:22:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cad0b5c5-3627-3bd2-ad3a-73ad03d73ecc | -4.43669 | -55.60324 | 2025-11-28 05:22:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2e3fb7a-7716-3132-aefd-2bbeb84bddb7 | -3.58838 | -47.27381 | 2025-11-28 05:22:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1b3553ad-0dc1-379e-ad81-d2505d833ef3 | -3.34952 | -54.09629 | 2025-11-28 05:22:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f5cff2d-88c1-34cb-8ee8-bb0ccad216bf | -3.59133 | -47.27763 | 2025-11-28 05:22:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac0f42e3-b9a2-3d0a-8c95-e31ca6bb1e85 | -3.58753 | -47.27978 | 2025-11-28 05:22:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4fba1f57-e852-3360-8eb8-a47a6f3c92ec | -2.41747 | -47.23199 | 2025-11-28 05:22:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d358a1f8-16c6-321d-81ed-a33b89326df6 | -1.41247 | -55.38959 | 2025-11-28 05:22:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 672fcbcf-5e5b-32a4-af78-9cb24aabbb20 | -3.35876 | -50.48948 | 2025-11-28 05:22:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 081b4780-a511-322d-8f80-43508361c01d | -3.35075 | -54.08813 | 2025-11-28 05:22:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dba61100-606c-3b81-b74a-91bd01191941 | -3.41018 | -53.3098 | 2025-11-28 05:22:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 881a20be-6278-32c1-a4cf-22835ffc1bf4 | -1.64998 | -52.0407 | 2025-11-28 05:22:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f660786b-75f5-3b8f-8f2d-49dc8fd701a6 | -2.7136 | -53.17939 | 2025-11-28 05:22:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 88d8f6aa-5123-3082-a3c2-e314546d9cbe | 0.46469 | -60.45267 | 2025-11-28 05:22:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 386a23c1-bc2b-3cbe-b5ad-7102f765537f | 0.46133 | -60.45318 | 2025-11-28 05:22:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e5995ae-8ecb-3c81-a2be-86d1daa3df59 | -1.33615 | -53.21593 | 2025-11-28 05:22:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8695f6ba-1fe3-3e88-9dd9-c3f9c43aec97 | 0.46356 | -60.44552 | 2025-11-28 05:22:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ab155adf-31ba-3bff-91a6-9309d7fa764c | -1.82103 | -54.33129 | 2025-11-28 05:22:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a256c3f1-b0a0-3303-b705-bc3800f73331 | -1.26176 | -54.68105 | 2025-11-28 05:22:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e493478-7f2e-3e19-821e-096994d0b3ad | -3.2264 | -50.31684 | 2025-11-28 05:22:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b2e29995-e997-3379-8167-7e9f3e91f3cb | -3.38383 | -51.49963 | 2025-11-28 05:22:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0380738-7426-36be-b420-5c7f811217d9 | -2.96304 | -51.02297 | 2025-11-28 05:22:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 306250ac-f834-3a24-9b01-766ebf718297 | -3.34069 | -50.26698 | 2025-11-28 05:22:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc02b73d-6db5-3fd6-ae15-eb60130cd3c8 | -2.939 | -54.80347 | 2025-11-28 05:22:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 782f1f96-0817-31d3-97fe-4ab6823aaefc | -2.01354 | -51.94008 | 2025-11-28 05:22:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| edd0be24-c747-3307-a753-52843ea06127 | -3.40666 | -54.57525 | 2025-11-28 05:22:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 627a4e1f-a22f-3cd0-89dc-b1fadb0f804f | -3.83152 | -50.18564 | 2025-11-28 05:22:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26093b0d-ac47-322a-8539-ab2bfb451d69 | -2.96208 | -51.02932 | 2025-11-28 05:22:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 33ae6a45-4e1c-396a-854a-5317a3529259 | -4.05556 | -46.56834 | 2025-11-28 05:22:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2cd27352-f564-3d20-9c4d-246792a0bc85 | -3.82647 | -50.18104 | 2025-11-28 05:22:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0992a06d-2082-3701-87c1-4df3fdd32b14 | 0.4602 | -60.44605 | 2025-11-28 05:22:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d36a195b-244d-381f-a098-ecaa2e06eb24 | -3.4061 | -54.57898 | 2025-11-28 05:22:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a899bef-9f13-3764-8a14-1d7c46f9448a | -1.49776 | -54.70387 | 2025-11-28 05:22:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 29f7a35d-cbad-3e5f-9fa9-ec909ce6942f | -3.03409 | -50.97922 | 2025-11-28 05:22:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 86b3b72a-92d1-3326-acb0-b542e2407749 | -3.22592 | -50.31989 | 2025-11-28 05:22:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f830efb5-a12e-3293-a34c-b2f1cc697a5b | -3.10357 | -53.13639 | 2025-11-28 05:22:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea38f7ae-20a0-3b7e-b84a-c91fac7794e1 | -3.59969 | -50.42234 | 2025-11-28 05:22:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b4e55b5-e781-3cff-9ec0-8b94bdf28411 | -3.17735 | -48.60802 | 2025-11-28 05:22:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4dfd759e-64b2-3caf-85ca-067f53c7b3e3 | -3.27415 | -53.76162 | 2025-11-28 05:22:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fb2e668c-6e99-3d5a-80e0-bbe32b439735 | -1.304 | -54.55475 | 2025-11-28 05:22:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0462e778-f3ce-3770-8c55-12492924b505 | -3.17052 | -48.61184 | 2025-11-28 05:22:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f97380f5-3d7b-319b-931a-1a9e1a39a83c | 2.04931 | -60.87331 | 2025-11-28 05:22:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ac721f9-482a-3574-96ea-dd150d7bfc3a | -1.67891 | -55.6215 | 2025-11-28 05:22:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e4b18df7-b068-3a87-90d3-db2950fa960c | -1.33485 | -53.22435 | 2025-11-28 05:22:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f447860-ef6e-3ca8-9b14-88e853afee66 | -3.22962 | -50.14575 | 2025-11-28 05:22:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ccd0b0a8-1ce7-3510-934e-efc705db99ca | -9.93793 | -60.71692 | 2025-11-28 05:22:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5b204b4-fb03-3068-a185-0718b17850ea | -2.36615 | -56.11445 | 2025-11-28 05:22:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ede9d75e-ba9b-3211-a85d-1689191bcdc0 | -1.24339 | -54.0594 | 2025-11-28 05:22:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 599d7de6-3133-3bfe-8e00-f4492727bcb7 | -1.6786 | -55.61932 | 2025-11-28 05:22:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ffcbc9fa-5c0d-367c-b451-481643869e48 | -1.82626 | -54.32462 | 2025-11-28 05:22:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9a87b2e9-be0e-3246-9953-60512855ba21 | -1.4816 | -53.47328 | 2025-11-28 05:22:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27f4e7f4-df39-38cd-8c10-36c15a2685f7 | -3.02884 | -50.9784 | 2025-11-28 05:22:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9660035c-7abc-3efb-b325-74e4036b25fd | -3.40197 | -54.57839 | 2025-11-28 05:22:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ab05a0f-97d6-3c6e-8c64-41bad55d18b9 | -2.93914 | -51.42509 | 2025-11-28 05:22:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2ed8864-e9c1-3d8e-9a10-d23482cd84de | -3.35014 | -54.09222 | 2025-11-28 05:22:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f7b694d-7f67-3bd3-96c0-6a3b73b2ed08 | -3.40637 | -53.30464 | 2025-11-28 05:22:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cf94069f-4e1a-3ad1-857c-785d443a0222 | -3.59219 | -47.2719 | 2025-11-28 05:22:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e96d2431-8cea-3323-983d-9c549580ce14 | -3.38818 | -50.25178 | 2025-11-28 05:22:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3b83649d-0036-3465-86b5-ce632ed47ee2 | -2.92707 | -48.23925 | 2025-11-28 05:22:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3dec5cb7-b6c0-36a6-b22c-a486b3cb2c78 | -1.44677 | -55.29425 | 2025-11-28 05:22:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 802f1512-7287-3acc-8299-45e38a7e9deb | -2.92157 | -48.23333 | 2025-11-28 05:22:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59a3a359-8a49-38e3-b00f-3d20426f0901 | -2.95733 | -51.02537 | 2025-11-28 05:22:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85adfa88-f16e-3019-88be-2b9c8c83aceb | -4.05644 | -46.56222 | 2025-11-28 05:22:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d0a7905c-b3cb-3f2d-8447-e55788303868 | -9.93738 | -60.72044 | 2025-11-28 05:22:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 438cac1f-d2c0-37da-b3d5-63ddbc9e798d | -1.82569 | -54.32823 | 2025-11-28 05:22:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bc5cf00f-711c-34ca-8a25-3e5041e764cf | -3.5582 | -52.07545 | 2025-11-28 05:22:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 71d7f0f8-04eb-3356-9f1d-ee76ecebdc67 | -1.35832 | -55.44068 | 2025-11-28 05:22:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3ed2bc8-3f00-3bf5-b801-c1fb0f4ef7a0 | -3.38337 | -51.50261 | 2025-11-28 05:22:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 273b806d-f918-3859-bdb6-ec71102cf549 | -1.49867 | -54.7083 | 2025-11-28 05:22:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1eb3c89-8fdf-3e5e-883f-5d92d37bca85 | -2.41661 | -47.23757 | 2025-11-28 05:22:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e752d6fe-1596-3123-aac0-3ca883e3ffc9 | -2.71293 | -53.18383 | 2025-11-28 05:22:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0327ad78-47dc-31c0-b63d-e1f461dcc6dc | -2.42413 | -50.28954 | 2025-11-28 05:22:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3521462-a304-3e9b-9868-589dcb702e0c | -3.02844 | -50.98042 | 2025-11-28 05:22:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9156be7f-cfad-31a9-b04a-2dc56c6da3b5 | -3.47252 | -52.99104 | 2025-11-28 05:22:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 105388de-2a20-3fd5-8cee-38b068bc6135 | -2.7939 | -52.95418 | 2025-11-28 05:22:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6f0404ca-07f3-364c-831b-af521e58a1ca | -3.38205 | -51.49951 | 2025-11-28 05:22:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f5b857d-569e-35ea-a265-d656a59e969f | -3.24872 | -50.0187 | 2025-11-28 05:22:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a94b2817-f580-3323-8379-01a5c39f0a07 | -1.3355 | -53.22014 | 2025-11-28 05:22:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fbbca3c0-dda0-3fb2-8f34-b2b118216cb7 | -2.82375 | -52.40015 | 2025-11-28 05:22:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 97579641-b96c-3b58-837d-960b51331edc | -3.35928 | -50.48595 | 2025-11-28 05:22:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a14fe460-6fd0-32f1-91cd-a2d036cca15a | -2.56704 | -54.76178 | 2025-11-28 05:22:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68d30a23-f240-3469-b526-ae5e7f997940 | -3.38765 | -50.2554 | 2025-11-28 05:22:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README22.md)
