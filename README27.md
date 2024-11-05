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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff0b8e94-4119-30fc-8e0a-37f3113e7b52 | -2.88139 | -51.31058 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 618e8d14-e891-35a4-a006-199e2ab9e99e | -4.88947 | -46.71046 | 2024-11-05 04:55:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0b941f57-98aa-3874-81c3-89b8957d6152 | -2.23458 | -50.4234 | 2024-11-05 04:55:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 5c67c3ba-fdf4-3e3b-b69b-8ea8672685d4 | -3.55161 | -44.63301 | 2024-11-05 04:55:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dadf3fd2-3dfd-3ba4-8ec7-9d784f83ec14 | -3.03899 | -53.27299 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8811c0d-9541-3ff7-be8b-ecb3df6f966d | -8.49857 | -42.09555 | 2024-11-05 04:55:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 896f604f-f1f1-3b66-9628-ba2351cc323f | -2.53277 | -48.2036 | 2024-11-05 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03750425-1d3a-3c03-bff6-30a1d4959758 | -2.78896 | -51.61109 | 2024-11-05 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| df7a2ae6-e8ef-3b70-be27-497c5176ea3b | -3.05777 | -50.50315 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e3d5997-f42a-30f6-85ad-926dc921fb56 | -3.03958 | -49.52977 | 2024-11-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6421d732-dbd5-34be-8fbc-228e6d7a2657 | -4.48092 | -46.46502 | 2024-11-05 04:55:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a75f18c6-b7cf-3b59-85c0-8c6c0c5e04fe | -2.99785 | -51.0553 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 012d12f5-151a-30f8-959e-a211c9eb9016 | -3.29544 | -50.34379 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c492097c-b966-375d-b8c8-d78a5bd2e763 | -4.07598 | -48.31629 | 2024-11-05 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb431b11-7d78-3fe3-9015-6b3c1fb1e574 | -3.48125 | -50.37819 | 2024-11-05 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd5e5442-1216-34d7-9e84-7065029aa111 | -4.24759 | -48.03933 | 2024-11-05 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 945bf29c-1d82-34b5-bde5-c6de380a5859 | -4.60955 | -48.91816 | 2024-11-05 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6f01e8c3-3328-3690-9dbf-825d5030b89d | -2.23103 | -50.42287 | 2024-11-05 04:55:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| af430650-ba4e-321e-8e63-40945bbb8dd8 | -2.83942 | -51.35393 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| be28e9c4-94a1-3ce3-b073-4a03b8c8330b | -3.86492 | -50.18957 | 2024-11-05 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec7aacdb-9e13-3501-9b13-10d4e47a2309 | -2.84401 | -51.347 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8eb637c-4da5-3584-a18a-438d7081a259 | -2.91047 | -49.41407 | 2024-11-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 896d6915-cb25-3e04-b1da-1c6336ab0865 | -3.95797 | -45.82924 | 2024-11-05 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 584767df-4d43-3744-9177-e1cff8b0d7f9 | -2.77876 | -51.60951 | 2024-11-05 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9c97a1c-03cd-3245-b9b6-6501c1194817 | -3.69175 | -51.08195 | 2024-11-05 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a91bd85-27a3-37fd-9047-651d622d37fa | -2.74809 | -49.13552 | 2024-11-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 57137d41-433e-3faf-a2de-d66a9d4ab05e | -2.46014 | -48.05224 | 2024-11-05 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ab319907-2015-39e9-a6e1-e6e644db82eb | -2.8565 | -48.45481 | 2024-11-05 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88418f89-d441-35ec-a0f8-0cc4e4c71bc1 | -3.56006 | -47.38237 | 2024-11-05 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 7377274a-163d-3dae-be64-8981c4d469b5 | -2.8172 | -48.55156 | 2024-11-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b331169-0665-37ad-ab44-3f930781bd43 | -4.60087 | -45.83104 | 2024-11-05 04:55:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9fd0acda-08f6-3932-91bf-f9f15827c9f5 | -3.86427 | -50.19385 | 2024-11-05 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48c278d4-a11b-320b-b658-e178db60d64e | -2.24095 | -50.71131 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2f3f6873-6245-3722-a0ac-107e9daa92cf | -3.95977 | -45.83363 | 2024-11-05 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8824f11c-6768-33d5-bea2-ccac8481d5fd | -3.07869 | -54.50655 | 2024-11-05 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e05d056-f609-3665-b67c-da197c604818 | -4.60284 | -46.87039 | 2024-11-05 04:55:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dd2c99ce-694d-37eb-8389-afc5ca570627 | -3.63213 | -49.10023 | 2024-11-05 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e2c1f8f-5598-38b1-8c08-8876f8fb6be6 | -3.55247 | -53.31096 | 2024-11-05 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b14e45d-b135-30bc-914b-598d54a7fad5 | -4.79396 | -43.78257 | 2024-11-05 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6de4c8c-43b0-3a6e-9d28-34ab9f83dfe5 | -1.41453 | -54.78093 | 2024-11-05 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6caecfe-5ef9-32ec-b993-8e8377d011bd | -4.50007 | -45.64993 | 2024-11-05 04:55:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90ae055f-b57c-36d6-a162-381efb020fd5 | -4.59755 | -46.87449 | 2024-11-05 04:55:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 05d3da84-900a-3c1b-9959-dc28695c6e7b | -4.54392 | -48.82656 | 2024-11-05 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ebf6abb-0e83-323b-b0e5-76b7924f88eb | -2.12413 | -54.63709 | 2024-11-05 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| adc01060-9018-326d-9000-7ada6a0651c5 | -6.115 | -43.97152 | 2024-11-05 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3c2489d1-6a9a-33f8-b06b-3552628e5405 | -2.50314 | -48.74419 | 2024-11-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dcf8f118-7118-3763-9c28-01024c29d234 | -5.30298 | -46.26244 | 2024-11-05 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7b40accb-3f62-37e1-8003-ae4654ced3f2 | -7.13681 | -46.00896 | 2024-11-05 04:55:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d7e87b1d-5bc3-3721-8578-94b2873152d3 | -3.80541 | -48.87943 | 2024-11-05 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c43f1de2-0b54-3fdd-a08c-dd5024c31193 | -2.84343 | -51.35073 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 55bf7e5f-0202-3c98-862d-dcec18db5dfc | -3.06197 | -50.49963 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e735af0-e3da-33fa-8f88-ec0a13a50859 | -3.03676 | -53.26561 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 756d325c-897a-3fa4-bf6b-e215c88647ed | -2.8745 | -51.30952 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0c61c07-282c-3218-9497-74f18baf6885 | -2.92178 | -49.34002 | 2024-11-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f4c93aeb-2376-3c5c-8f78-952634056e11 | -2.83536 | -48.45879 | 2024-11-05 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4858ba8-b845-3753-9d8c-d9ca54048560 | -2.82943 | -49.43647 | 2024-11-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f9cdc81c-219c-3d48-a0d5-2daa64ff8a91 | -4.41204 | -43.10941 | 2024-11-05 04:55:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8e3f0e4f-31f6-3956-967c-5587c3c16e40 | -3.09986 | -50.25244 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 56ab480a-11e8-34b8-a041-93014588f10e | -5.43853 | -43.25979 | 2024-11-05 04:55:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e09db501-1fd3-3f0c-a137-e186b15da22e | -2.91417 | -49.3389 | 2024-11-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f2223d80-1963-3278-a5ba-e101ce4c4339 | -4.22924 | -48.54034 | 2024-11-05 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20d9ae30-50d6-3e30-b86d-1fd0c2602290 | -4.36517 | -47.89014 | 2024-11-05 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d4e17d96-ecbc-36a7-943e-3fa1ff8e2070 | -3.51893 | -51.67132 | 2024-11-05 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e04feb7-3524-3580-85a7-182ce3a97259 | -2.61329 | -51.72229 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 69807df2-ccbf-3d44-9e98-65052aae73f5 | -4.07243 | -48.3119 | 2024-11-05 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 033b71e8-2cf0-3c85-8ad6-e93137060d8c | -2.97688 | -50.29956 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2cdcebd8-34b5-3147-a87f-064813edb2c5 | -3.17547 | -49.09743 | 2024-11-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f2cff8e6-4a97-3233-bfb5-3a0b9834406c | -3.52076 | -52.84292 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0b01a00-63f6-3ffc-8b94-139001d8254b | -2.79528 | -51.48025 | 2024-11-05 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9fdf24f2-5872-3ee4-8c3b-3650d12b8d2c | -2.63515 | -47.97279 | 2024-11-05 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 461378d1-193e-320e-9ccd-0126c235e222 | -4.3523 | -45.50773 | 2024-11-05 04:55:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd546c02-7d0b-3944-8bbb-04fa6ebfad07 | -4.37392 | -47.23705 | 2024-11-05 04:55:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 17461357-c103-3dc5-ade7-b95adb2dfa5f | -2.73131 | -51.73655 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0353bf0d-7bfd-319b-90c4-99651a191e5b | -2.59852 | -51.30231 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 55804cf7-016d-3673-af40-beba5ebb326a | -3.05839 | -50.49909 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1880e339-e241-3f81-af34-1a77d2ec8e65 | -6.09894 | -43.96119 | 2024-11-05 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 5b892ce2-930a-3bda-8d60-e5fed1049f5f | -4.42858 | -46.28973 | 2024-11-05 04:55:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84bc4442-be00-3138-ada4-6a6f72447afa | -6.10464 | -43.96215 | 2024-11-05 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| df56087a-040e-3c04-a6e7-8b038214f79c | -3.03684 | -53.04726 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e03e7f15-52df-3d31-a470-f2b533852737 | -3.10367 | -50.29993 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a26d0b4-a3f6-3660-a89e-98a3c0ed8408 | -5.08936 | -47.86832 | 2024-11-05 04:55:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a1115ab-9b2e-31a6-a084-a3f945126ea1 | -3.41594 | -50.38656 | 2024-11-05 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cfc01993-c1cf-3a12-a342-78a0650fd585 | -4.25789 | -50.72326 | 2024-11-05 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97452ef3-4b30-355a-a7b9-0fe65cb54be5 | -4.94573 | -46.73542 | 2024-11-05 04:55:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98b4a7a1-c014-3b93-9769-1d5859b5c55b | -2.84285 | -51.35446 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 76dac0a8-573b-3c44-b50f-5135331ca467 | -3.21715 | -53.068 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3aac5eb6-0808-3852-963a-00efe41f87bb | -2.60646 | -51.76567 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7efc23c6-5514-3598-a8c9-1e10426fe5f9 | -5.93035 | -43.64066 | 2024-11-05 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13d7d36e-9559-3d7b-b5fb-dec49e85e17a | -2.79927 | -51.47705 | 2024-11-05 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5247174-2f88-30d0-8774-25195d42606c | -3.07814 | -54.51006 | 2024-11-05 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4dee0fa6-73af-3189-8d2d-561404796a9f | -2.65598 | -48.56255 | 2024-11-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de3fd57a-3c8b-3091-bfb8-7916d132cce9 | -5.98793 | -43.42778 | 2024-11-05 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1022317d-461e-3528-ba8d-83b092e4a5a0 | -2.72338 | -51.71294 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c039dba6-125f-3e35-9a78-c21fd9d0da0e | -3.22353 | -45.45515 | 2024-11-05 04:55:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a4761688-00f4-34af-abed-86969bed5dc6 | -3.47701 | -50.38177 | 2024-11-05 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2cf67316-ac34-3ccb-a7f4-7727ea6f5c9c | -2.61226 | -51.30442 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1eeb8533-9bef-3d55-b3b3-fb30a58334b1 | -2.7347 | -51.73708 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 26356925-93c3-3185-9972-125b9b736723 | -5.44385 | -43.26504 | 2024-11-05 04:55:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3a763709-f58d-3dae-8035-42fa0cd1938d | -7.12721 | -46.01358 | 2024-11-05 04:55:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 66421e76-10d2-303d-a941-3ad0db93bb8d | -4.79076 | -43.78196 | 2024-11-05 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README28.md)
