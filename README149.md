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

## Dados Diários - Página 149

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f11700bc-35a3-39be-9c1e-eb72f2136504 | -8.83718 | -69.48325 | 2026-10-05 17:37:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 30.3 |
| d6b530db-c838-3a89-a8f5-1d8b54e334fc | -10.64117 | -69.16078 | 2026-10-05 17:37:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0d22cdd9-0a8b-36d0-9f5b-d964a6058032 | -9.49083 | -63.94958 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 3372aa64-c566-30d4-8f24-1b0244b8c9a8 | -9.13292 | -65.94581 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 88746aef-9499-3696-8ded-07d180cc801d | -10.12627 | -69.29873 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 21dd9f42-470f-35a6-9bbc-5ada5c863396 | -9.10415 | -65.3599 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 7fb6be79-3642-35e5-ad83-9bf551a27d2f | -9.08248 | -66.09818 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 7263e857-22dc-33fc-a7f9-4828f0ed947b | -9.37835 | -65.93666 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9895b6a6-e0aa-3615-b29e-db9b49881253 | -2.77559 | -57.67602 | 2026-10-05 17:37:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 91.5 |
| fa559a0a-045e-3e73-9feb-989c5db33434 | -10.12112 | -69.30305 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 64a6e8ca-4b83-31f8-b6e1-27f6a31685a5 | -8.5584 | -54.58205 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 929710d6-a56c-3733-9ee4-f07d359671a3 | -3.34272 | -67.98462 | 2026-10-05 17:37:00 | NOAA-20 | AMATURÁ | AMAZONAS | Brasil | 1300060 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| c72e4510-25ee-38ff-abe1-5002bfc10876 | -9.07683 | -66.09008 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f783d12f-b7ab-33d8-9883-f4cab2d865b9 | -8.47143 | -54.91646 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 2cdc6a13-00a7-39e9-b12c-64f7ef7963c1 | -10.60156 | -70.03532 | 2026-10-05 17:37:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 12.3 |
| bfa6e2b6-1626-303a-b8da-9557d7a88569 | -10.48373 | -68.62721 | 2026-10-05 17:37:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b1dfc74b-4028-341d-8817-e07e4e307352 | -8.60312 | -66.96649 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3c2ce292-98ce-3e4c-9069-0865d7d30d7c | -1.46313 | -53.608 | 2026-10-05 17:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 36471708-dfb2-32c4-90c8-8a5ba86eabd9 | -9.41368 | -67.76945 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a8138541-bdbc-3dcc-a409-e14649d0912e | -8.4288 | -55.00239 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| de433f69-193e-3172-954c-937d958fcaa9 | -9.46449 | -64.33007 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 31.2 |
| fb15acac-01dc-3680-88fc-e814fb995007 | -10.14326 | -68.39357 | 2026-10-05 17:37:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 14.2 |
| a2a0a756-44c8-3bee-87fd-3adcd68fc594 | -3.34346 | -67.98944 | 2026-10-05 17:37:00 | NOAA-20 | AMATURÁ | AMAZONAS | Brasil | 1300060 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e2249b55-0566-3850-b3d4-f06420bb9849 | 1.87151 | -55.75971 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e900ee03-851f-3764-9fe1-334a624f012d | -0.73387 | -57.97424 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 65dd04b7-577e-35df-9be7-b6b5bd277cff | -9.54214 | -68.66415 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 7.5 |
| cafcfe82-2b3a-3412-a7ab-003002fcd785 | -2.37782 | -56.12498 | 2026-10-05 17:37:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e8e5978b-f0ef-3cdc-befa-fceca1a22bc2 | -9.96789 | -65.12231 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 1abf106c-12af-306e-b4ff-06776cca38bd | -1.46491 | -53.60992 | 2026-10-05 17:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3c1db411-79a2-3871-ad9c-2f38f24959bf | -7.87374 | -54.70758 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 10c76cd9-050d-317d-bb86-6c173528090f | -9.18091 | -65.57378 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 14fa8bcf-dcda-34fb-a9e2-3edf8def611c | -9.82382 | -67.70856 | 2026-10-05 17:37:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3d50a71f-8fc9-341e-9ca2-72f15c962152 | -2.18885 | -56.83765 | 2026-10-05 17:37:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2a7a53f5-198d-3643-af2e-46d2d79d4286 | -9.1585 | -68.22172 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 79e96db1-b245-34fa-99df-afbc36d6f3be | -9.37803 | -68.79626 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 15.9 |
| fa247b53-9c2d-3fae-84c9-4f1962f65ee4 | 1.89422 | -55.72805 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4a7a3591-dde0-3984-909b-b958c330d1bc | 3.58072 | -61.36164 | 2026-10-05 17:37:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1d3c45f6-1999-3ae1-8606-0bcbf3c15845 | -8.91027 | -68.64394 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 141.2 |
| 547dcac2-b52b-35cc-9baa-6570f2a30b99 | -2.77492 | -57.67177 | 2026-10-05 17:37:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 98931074-2547-3a29-b177-ffb126e2a1f5 | -6.32062 | -54.78039 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e8cef409-04d5-3f96-b200-8502ce02023c | -8.96002 | -68.78188 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 1edd283b-cc26-33c1-8f2e-98b7134a25f4 | -9.37453 | -65.94156 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6f7d6ff9-30dc-3979-ae72-eb8d97129d5f | -8.99715 | -65.39788 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 5b0690c3-edf3-367d-a33a-cd64b00b41b5 | -9.12319 | -68.31181 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 263b7144-548f-38d3-810b-b7730d79835a | -8.75216 | -69.09627 | 2026-10-05 17:37:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 22.7 |
| b81b1b55-0b2b-3331-a9bb-788d0b2a9ca6 | -8.85083 | -68.80633 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 82aff1ea-4a3e-333a-be9f-7fabee769513 | -9.34067 | -64.71889 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4bc7831b-54e1-3b8a-9340-84bc039669d7 | -9.48693 | -67.66691 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 9de9223b-b74e-3409-a6ea-692c3742aaa4 | 0.6905 | -60.07612 | 2026-10-05 17:37:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d5265b95-c0c2-32e0-9595-20e7894ab247 | -9.23562 | -67.8896 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a4c2fd22-78a5-3977-b641-332f8c9a94bd | 2.28418 | -59.74606 | 2026-10-05 17:37:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6f1765df-3d1d-365f-8185-fb890c4ec990 | -9.40431 | -68.87333 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 15f09f0a-6427-3c27-8324-7808a70fb5b2 | -9.13806 | -67.80584 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| b97c9ea6-ab40-3b51-b9b0-0a964575ad9c | -10.61374 | -68.68138 | 2026-10-05 17:37:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3cc4b99-d865-3359-abe1-c0a2a31de1a9 | -9.48191 | -67.1573 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 513d42b4-720f-30d3-8ca6-77c11cdca0c0 | -8.88687 | -66.64401 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.3 |
| bf60934b-13ce-3e95-9a1b-28ec122facd6 | -8.8538 | -70.59568 | 2026-10-05 17:37:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2e5e512b-d66a-3e94-91bd-9eae88662d6a | -9.1088 | -67.69772 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 61c79713-bfd0-31ee-be3e-8376fafdedb5 | -8.85123 | -70.59444 | 2026-10-05 17:37:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 66dfe739-4d3c-3d9d-ab1e-cd6d93803689 | -10.36039 | -68.41636 | 2026-10-05 17:37:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d79de8e8-d257-36d7-850f-d70c0869271e | -8.84673 | -66.79363 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.0 |
| cebbf1d4-0bbc-3c77-9023-060ef044b599 | -3.14085 | -60.94725 | 2026-10-05 17:37:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 14.5 |
| d54a9061-7665-3630-9efa-2a0942f54a7d | -9.53822 | -68.58967 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a5a6b569-dedb-35b3-8346-4d5102b4352b | 0.31933 | -60.44548 | 2026-10-05 17:37:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 128.6 |
| 7ca31813-0a48-32fa-afbf-3e800be2ab2b | -9.27438 | -67.87235 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 76448eb2-670a-307f-b8d4-02b847063c0c | -10.38174 | -67.96121 | 2026-10-05 17:37:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 64b0b7bc-1927-33de-84d9-c579fccbc6c4 | -8.75588 | -66.91338 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 986f9487-e864-3427-895e-6214323cd4dc | -10.81303 | -69.54414 | 2026-10-05 17:37:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 9.2 |
| d2438e79-04af-3d27-8432-320680b101c0 | -8.56132 | -67.06082 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 59864201-4742-37cf-93f5-a43e785dfb86 | -3.28639 | -60.9873 | 2026-10-05 17:37:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 95a17271-d624-32ed-9e7f-2a5e403a7dba | -1.21905 | -54.53642 | 2026-10-05 17:37:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ad6797ce-15aa-34f1-b530-03e626375783 | -2.57142 | -57.97931 | 2026-10-05 17:37:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 86aabc85-392e-326d-a1a2-f6a57d23494a | -2.53221 | -57.55755 | 2026-10-05 17:37:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ef43e3e1-4958-3118-a587-74f4be527c2d | -9.1326 | -65.9108 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e1f466cc-b8cd-3103-aae4-b081aec5fa39 | -9.0994 | -65.48093 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 8746fbf5-2fe1-3a61-bc7f-ae606ea5c2ff | -2.76694 | -57.66863 | 2026-10-05 17:37:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 134.8 |
| db92f6dc-909d-3f6a-b8b1-5e5588c2aee7 | -9.02324 | -68.36627 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0531fd6c-2e7f-33aa-8d31-21009476be96 | -9.14649 | -65.54552 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d5c68047-5ca5-3221-9148-69c548d0cf9b | -9.06027 | -66.10118 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| c3516163-3af1-34d6-b0eb-2338ccbc3192 | -1.72934 | -54.97084 | 2026-10-05 17:37:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 458e8974-97a0-3776-801f-8981b626fb48 | -2.7702 | -57.64195 | 2026-10-05 17:37:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4af02477-5c18-3324-b309-cb5a51ef11eb | -8.80466 | -69.49521 | 2026-10-05 17:37:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 75025575-f7a6-37e7-9e43-f93a306e07ab | -8.75436 | -69.09814 | 2026-10-05 17:37:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 26.3 |
| fb3065b6-d518-3108-9fad-1035599e99c2 | -2.4981 | -57.24587 | 2026-10-05 17:37:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ceaec79d-bfed-3092-ab68-24d03a54ef2f | -10.2438 | -68.30141 | 2026-10-05 17:37:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 89aef0b3-c587-31ae-873c-d0ebfefb85b2 | -9.0359 | -72.33503 | 2026-10-05 17:37:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a95769fa-49a7-38a7-9d9e-bcd76c1f7c14 | -8.65322 | -67.45262 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1bc6dda0-9bec-39ed-96e8-354c692dca69 | -2.77424 | -57.66751 | 2026-10-05 17:37:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 134.5 |
| fad152fb-7481-3923-adce-1b6318c98672 | -10.4224 | -67.97716 | 2026-10-05 17:37:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 8.6 |
| e7a5e049-d761-390c-8e7a-84d6c011e82a | -8.66058 | -66.93334 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| a59919de-17c5-3365-8b1d-99943628ae19 | 3.58112 | -61.33644 | 2026-10-05 17:37:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ce022fcc-2239-3925-99a7-2194fdcf758e | -7.21183 | -55.19976 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| dae507c0-3b44-332d-a813-1685bcbbf232 | -9.16099 | -68.24021 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 9dd6570f-9e77-30d6-ab55-e6d3c4309e13 | 3.5022 | -60.32828 | 2026-10-05 17:37:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 82c0f8ba-8000-3a12-96ee-c41a5f7e8bc7 | -8.59199 | -66.81339 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 4820c8bf-4652-363e-9837-917ca6fb38fa | -9.48573 | -64.68731 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6df08b67-d6d4-3fb7-acd3-046842c53f9d | -10.74027 | -69.61918 | 2026-10-05 17:37:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b30ab301-b4e1-340e-8f85-bc5fb6cf47ac | -9.38239 | -68.33475 | 2026-10-05 17:37:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f8f6560f-e06c-3e7f-8b4f-834258dd6a6e | -9.12194 | -67.83761 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 4a505ab4-c555-3778-b377-5c5755e6359d | -6.81471 | -55.30051 | 2026-10-05 17:37:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |


[Clique aqui para ver as próximas entradas](README150.md)
