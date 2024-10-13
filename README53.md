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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 326f1238-f52b-345d-9b20-72a2117b08d6 | -3.91759 | -48.34981 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e4d8c5bf-a633-346a-9a5a-982c067af5bc | -3.91706 | -48.35325 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 597fdd5c-2813-3e51-b1fb-85f0c1ced6f6 | -3.91652 | -48.3567 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 0d8ef084-91b9-3e4a-8fa2-e47823c17ec3 | -3.91598 | -48.36015 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| bfcdefda-6bad-381d-840b-6f2426daa183 | -3.9159 | -48.33895 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fb973625-18ae-34a1-a4ad-ed976527cffe | -3.91375 | -48.35274 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 906522d0-7d67-344a-bf5b-cc37c1f32ffd | -3.91321 | -48.35619 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5ad4098e-9012-305d-91e5-de245548cd4c | -3.91267 | -48.35963 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a455c820-46a7-36eb-868a-c8f82a7b7fae | -3.91044 | -48.35223 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 70c01ae8-4548-36b3-965f-dcb1e098305d | -3.90991 | -48.35568 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c1e1b2c8-b045-3b43-bb4d-7313c12d3e53 | -3.90937 | -48.35913 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 51fdc1f8-4454-3f10-ac64-0a1475662fbd | -3.90714 | -48.35172 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4e85fad9-913f-3af1-a7db-a791867f4f0d | -3.9066 | -48.35517 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c7c424f2-96c2-3f1a-951c-67d093c4fbff | -3.90606 | -48.35862 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e4d42fb-f3d1-3947-9412-7ea8842f31df | -3.89937 | -48.33639 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9c4938ed-558b-3b94-a24e-caad942f02e0 | -3.8957 | -48.33514 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9bf14fb-b31b-3d61-8bef-b1cd4d2aee7f | -3.89516 | -48.33859 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28c40df8-272a-3b2f-afc3-a5ef9912639a | -3.8924 | -48.33463 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9fdb19b8-7f5f-3fd8-81a6-77b796f93583 | -3.88909 | -48.33412 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9a83ae9-f593-3566-8c52-a6227035c03e | -3.88579 | -48.3336 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2354d45-6edb-361e-a661-0b658cf9c6e3 | -3.88194 | -48.33654 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05edcbb6-f26e-3c94-94b4-28a6b8465616 | -4.18244 | -48.02504 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e146795-f706-3d56-8ea0-992b13e60db0 | -4.1819 | -48.02851 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8480d146-369c-38dd-8e97-66b2289232ab | -4.17912 | -48.02451 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe2ea34d-f261-3d6c-ba66-191185a96fa3 | -4.11835 | -48.2393 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4848cf20-566e-3b1c-999d-1056405aaf14 | -4.11503 | -48.23879 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| dd21df26-7f1f-3b12-a940-3c9c119bf263 | -4.11172 | -48.23828 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e67ab31a-9b7a-3f3b-8ee0-6a9aae34bb1c | -4.05937 | -47.92012 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e0248f0-62b5-38c5-af78-c48fbeffedf3 | -4.05659 | -47.91613 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d9a1cc7-0bd8-310d-b3fb-f3f9b8fe7cbf | -4.05604 | -47.91962 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a8943ee-624d-3892-a71d-6bece599ca68 | -4.05436 | -48.23645 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 44991970-01e9-38ac-9a54-d400ecd1a62c | -4.05382 | -48.23991 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9161e8e7-5410-37fb-aee7-424bb17e8e5e | -4.05271 | -47.91911 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1dcab36-4237-3628-a93b-5130190fa86a | -4.05105 | -48.23592 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| af50a18e-b26d-304c-bcc4-4e12e9c38aa8 | -4.04939 | -47.9186 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3dc97ab5-333b-3d59-8010-5e617f9426a9 | -4.03781 | -47.94905 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8506d5ea-b750-302b-94ff-8f08a6e8c2ab | -3.95755 | -47.96161 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a1d1ad5-cd1e-31f3-8f5d-395396c1194f | -3.95701 | -47.9651 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a6ec4ec-b8e0-3153-9455-12027dfd3fd0 | -4.1234 | -48.27198 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4f1c02e6-5471-3845-acd2-b4ebf668d8a6 | -4.12286 | -48.27544 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8cde27eb-0a70-361a-96e2-e1f7dceaac5a | -4.12231 | -48.2789 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13a3aafd-8099-3ca1-841e-79320cd41caa | -4.12063 | -48.26801 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02610d48-0b54-30fc-a66c-38fda2f02b84 | -4.12057 | -48.24676 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 30895f64-24a5-3104-97c0-f693d337aebc | -4.12009 | -48.27146 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 89c08534-6fb8-380c-b490-147ab3fe01eb | -4.12002 | -48.25022 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 733ad696-37b9-3dc7-a5bd-0ef39e805bcd | -4.11955 | -48.27492 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0809a084-fbd6-3439-83df-6e17dd916a75 | -4.11901 | -48.27838 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b42d2a39-a701-354e-8d71-e9d31cab3175 | -4.1178 | -48.24277 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a06b79b5-7c11-3808-b651-1b6362b76022 | -4.11732 | -48.2675 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a577fe5-f6d4-3415-8e19-9f2b8015bcc4 | -4.11726 | -48.24625 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 13ca204f-6bd4-3657-b235-650ab336ca9e | -4.11678 | -48.27095 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ca62d1f4-e97d-3f4d-918e-00db34ed5d07 | -4.11671 | -48.24971 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d591d529-14fd-3710-bc87-73ad8f8d88bc | -4.11624 | -48.2744 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57fb61a8-2ae0-3aec-a8cc-c4ebed510c04 | -4.11617 | -48.25318 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94266077-18cb-3d2e-be9a-a72bc32b5274 | -4.1157 | -48.27785 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 671b45f3-85ca-392d-b0a8-9c54b164565e | -4.11515 | -48.28131 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a44f094e-f7d8-37c6-bede-d95c10b2f453 | -4.11455 | -48.26354 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 244c2289-80f5-3377-a667-a0d10a669a3d | -4.11449 | -48.24226 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 44f2492a-623f-34c8-aecc-e4cd8a395c0c | -4.11401 | -48.26699 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 93df4138-f2bd-3af8-82c8-9f0c527b086d | -4.11395 | -48.24574 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 72b8adbf-d123-3f41-9161-e191f4e3eb91 | -4.11347 | -48.27044 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 49842ceb-8be6-3d77-b838-0f279e4fb564 | -4.1134 | -48.2492 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac86190a-cb79-31f2-a8c0-a8f2b62d96b7 | -4.11293 | -48.27389 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 99bcbcaf-a1ac-3eb6-b977-34e1c0967364 | -4.11286 | -48.25266 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6263abf-5c6c-3823-8619-578b4aa69e01 | -4.11239 | -48.27734 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1eb4ecc1-1d81-31dc-a874-9bf78d647283 | -4.11232 | -48.25612 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 485c5302-4a1e-341b-8ec0-89c6460e820a | -4.11185 | -48.28079 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 281a6e9d-8a88-34e1-9037-231e45f684b5 | -4.11178 | -48.25957 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ce04d513-b957-3f04-bce7-c23262760cee | -4.11124 | -48.26302 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8671314d-d60a-38c8-90f1-16e0e42b06bc | -4.11118 | -48.24175 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 4aa3b78e-7661-32e0-a477-d0d6e24f828e | -4.1107 | -48.26648 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 32838c12-5a5f-3c57-a9a2-985f82c32801 | -4.11064 | -48.24522 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 214cd49d-bd13-366e-9740-a7a927199022 | -4.11016 | -48.26992 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c453185a-cd30-3200-a938-66aaed76bad0 | -4.11009 | -48.24868 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8d52281-9e67-3ac6-82cd-3162d04b0498 | -4.10955 | -48.25215 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 411588b0-7665-35f4-b5df-2be9b275e8b1 | -4.10901 | -48.25561 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3777283c-ee71-3c66-af63-6cb96266eaa2 | -4.10847 | -48.25906 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 32125596-7380-3c56-a352-f878f4207174 | -4.10793 | -48.26251 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ecf18cc0-932f-3c6b-a742-18a60c50ae08 | -4.10739 | -48.26596 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d4c11c6f-5d09-3062-ade9-f478573e62d4 | -4.10733 | -48.24471 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3b505a6-a6a1-3f6e-afb3-52c172d6c65b | -4.10685 | -48.26941 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a727063a-8369-3470-8c5a-275c26a07072 | -4.10678 | -48.24817 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2088d1d-cf31-3574-a935-9ee1d52c1b8c | -4.10631 | -48.27287 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f48b4eae-1b19-328e-beea-fe49e7b54b7d | -4.10624 | -48.25163 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c6d38301-c6bf-3c78-8c2f-44555acd0dce | -4.1057 | -48.25509 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9f7a46c2-a8f8-3018-9953-8fc7e16c4552 | -4.10516 | -48.25854 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 568fe60a-1182-3878-b4c1-413ff6887ff4 | -4.10462 | -48.262 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 931a573d-147a-3877-9d30-cfd4bcb65976 | -4.10408 | -48.26545 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| aa931782-17bd-340e-a8dc-bbd7bb961abe | -4.10354 | -48.2689 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8aec5560-0f6d-3765-9bfe-0caf2a88f059 | -4.10347 | -48.24766 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 378532a5-9262-3a63-b9d8-83e30c96ec4b | -4.10293 | -48.25112 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 80c00015-aebd-3c28-be79-605cd8356965 | -4.10239 | -48.25458 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 498568b5-9c77-3624-954b-5c56ba99b8c6 | -4.10185 | -48.25803 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7b73e084-0def-3525-b32e-8eed6ad8e367 | -4.10131 | -48.26149 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 90e18b79-c79c-3d66-93ff-7068b81165da | -4.10016 | -48.24714 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7418113d-f392-3198-8bfe-98544a38260e | -4.09962 | -48.2506 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04387010-086c-3f05-ba0b-3cc4e2db9324 | -4.0974 | -48.24314 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4727f41-9f12-3495-b26d-b53c6de5abe9 | -4.09686 | -48.24661 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e8f85c3-d70e-3df3-b17e-c96eb5b8c393 | -4.07537 | -48.25394 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb03ca2d-bd63-33d5-b8a0-cf42e79826dc | -4.07483 | -48.25739 | 2024-10-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README54.md)
