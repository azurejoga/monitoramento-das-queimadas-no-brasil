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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0bb332c-0e43-308a-9aed-bda03474c52a | -2.38108 | -47.71527 | 2025-09-26 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 436be7db-428b-33f7-aa45-723a3601c7b3 | -3.31014 | -41.1092 | 2025-09-26 04:12:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 39705bb3-bfa7-3daa-a971-3efbb0126fd6 | -3.30325 | -42.17812 | 2025-09-26 04:12:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 11529d5e-47f5-3efb-8793-8fecf346518e | 0.69235 | -51.46014 | 2025-09-26 04:12:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| abedfd33-3ec2-3bf2-b78c-b3b5d04d3302 | -3.29995 | -42.17761 | 2025-09-26 04:12:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a7eafb77-d888-38ef-a71e-40be5d01d2c9 | -2.45301 | -49.01651 | 2025-09-26 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 498ae6b8-d214-363b-ad05-c823663d8c4d | -4.08296 | -38.38313 | 2025-09-26 04:12:00 | NOAA-21 | HORIZONTE | CEARÁ | Brasil | 2305233 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0560b8c7-6a76-33b6-aa9c-ad717585ddab | -2.4485 | -49.01579 | 2025-09-26 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 94be2dfc-8e6b-3886-aac4-ac233b5ce04a | -3.81426 | -40.37508 | 2025-09-26 04:12:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4428f82f-4d75-3802-a195-afa3c131c3c2 | -3.41584 | -41.60822 | 2025-09-26 04:12:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fcb13299-8cc6-317e-a17e-df8b3739101c | -3.82986 | -40.34262 | 2025-09-26 04:12:00 | NOAA-21 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4a88ed67-0464-34c1-b8ca-651d5026b75e | -2.87876 | -42.86683 | 2025-09-26 04:12:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5eaa1e80-a52e-359b-a92d-886f144beb1c | -3.82928 | -40.34641 | 2025-09-26 04:12:00 | NOAA-21 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c2105bcd-4431-3432-8bdd-f0fb3de51da7 | -2.38521 | -47.71597 | 2025-09-26 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f005445-f18a-3565-b919-1699356ab96a | -2.87822 | -42.87027 | 2025-09-26 04:12:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd0a3c00-b5b6-3048-9119-d00015765224 | 0.07359 | -51.05578 | 2025-09-26 04:12:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3cbe15cd-6278-3e0c-bf15-6532c1142ad1 | -9.44451 | -40.37473 | 2025-09-26 04:14:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| eae1495c-9f28-3aad-b728-a2352abc0bb1 | -6.26148 | -42.47631 | 2025-09-26 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 58b7006c-6c26-3b78-bd7e-091ddced82b2 | -5.79782 | -42.81023 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 12d7808b-04b5-3254-ae75-42e2464d404e | -6.26372 | -42.48376 | 2025-09-26 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c5588fc5-22aa-3807-93da-f32ec35f2546 | -6.66259 | -42.05664 | 2025-09-26 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 26d15847-be6d-33cd-934d-287e0eef9437 | -8.84543 | -46.25897 | 2025-09-26 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f76430e1-a4d6-34c3-8de0-7e64482ac583 | -8.07789 | -55.22385 | 2025-09-26 04:14:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72edf950-3a8d-3def-9c2e-1602467dada1 | -9.37089 | -43.74561 | 2025-09-26 04:14:00 | NOAA-21 | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| de1185a7-0c5d-398a-9133-508e15f555bd | -9.11681 | -48.89711 | 2025-09-26 04:14:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 95802a6d-1f9b-3432-9188-93e0357dafc4 | -6.53146 | -43.88124 | 2025-09-26 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 46f58311-5c4c-3221-8201-a087252e47cb | -10.84827 | -44.80228 | 2025-09-26 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 727c162e-7bdf-31dc-8b41-4c3061fdcbab | -3.85353 | -50.97685 | 2025-09-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61324837-6939-3abf-a3ed-903bb221e099 | -7.67237 | -45.99335 | 2025-09-26 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| eb0ee8bc-5798-330f-adf2-04a6e9fc3dbb | -3.86786 | -43.7856 | 2025-09-26 04:14:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66429b10-5ace-381b-929d-cb35aee69748 | -6.85626 | -43.1785 | 2025-09-26 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 2f4d59b6-200e-3aad-9015-bfafaa83e838 | -10.12077 | -45.30894 | 2025-09-26 04:14:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 68869efd-4840-3bea-a037-c5f326bd2132 | -8.19515 | -46.39145 | 2025-09-26 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 235786ec-2765-3b2e-aa56-6100349e4995 | -5.71836 | -44.95187 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c18df14c-76c5-35c9-a6bf-f454acb3323d | -4.07411 | -48.04169 | 2025-09-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c7f2313-5857-32ca-a1af-6341d3ed2d5a | -5.63509 | -43.93145 | 2025-09-26 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ef05f016-9589-3bc1-b450-e268d708a582 | -10.39188 | -46.13339 | 2025-09-26 04:14:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dab1b079-8407-3d23-abb9-63eb37f9faaa | -3.85099 | -40.93152 | 2025-09-26 04:14:00 | NOAA-21 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 04309106-ca25-31b4-a150-057d68543d0f | -10.29083 | -45.22285 | 2025-09-26 04:14:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1ed0555b-4b8c-3c17-9af8-43ece7a50664 | -4.48861 | -47.68236 | 2025-09-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 461b7ce6-84f4-3107-9679-43d99ffdcd2c | -6.61535 | -42.93181 | 2025-09-26 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 919e3134-30be-3a8b-a24f-3f87bca62bf6 | -7.31563 | -45.77087 | 2025-09-26 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 293a73d6-b98f-3fab-a7a3-cbd19da63094 | -7.58914 | -42.33376 | 2025-09-26 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 94e13b64-b0e4-3345-b116-5b9acfea4ff8 | -5.72566 | -44.97194 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0aa12c7e-7708-35ce-81a8-c71fe04219ea | -9.75967 | -45.63025 | 2025-09-26 04:14:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f2377b1-289e-3edb-97ad-3d6aac059031 | -5.7319 | -44.97671 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 22cc6399-3ca1-345b-9553-80d8f3c8542f | -8.79045 | -46.59246 | 2025-09-26 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2a7f5c1a-f00b-3a82-bc69-ed449af8057d | -5.24717 | -43.08641 | 2025-09-26 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9186ea4c-9235-3261-94c2-6a900d9e83ce | -5.74166 | -44.95926 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 421bf960-7433-3aed-98e6-2f10753a445f | -6.22334 | -42.85294 | 2025-09-26 04:14:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1e9ce2ec-94b2-3742-953a-2d5b24cf7361 | -9.47534 | -48.23623 | 2025-09-26 04:14:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ee3ef162-3228-36ab-b6dc-fff027a3b967 | -4.19762 | -38.12239 | 2025-09-26 04:14:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3bb7b91e-b97f-32f3-b676-02e0b8c1514b | -10.58901 | -46.28194 | 2025-09-26 04:14:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd1b761c-12f8-3237-9bea-c606d4362165 | -10.00657 | -44.18218 | 2025-09-26 04:14:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 07022cd0-808a-3b8b-8bb3-1109fef621bb | -5.74332 | -44.97089 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 114.0 |
| bafe50ee-84dc-345c-ba63-d76084ed3ebf | -5.78608 | -42.75547 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f5b71b87-7aa4-3f0c-9b40-608eda87ce79 | -4.81464 | -42.74319 | 2025-09-26 04:14:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 84d15654-85a7-36f0-a851-cca29339f1dc | -10.40406 | -46.1664 | 2025-09-26 04:14:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b608cd4c-4a8b-3526-b7e5-eb51131e6f0a | -5.64173 | -43.93251 | 2025-09-26 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5945807e-27cd-3e96-862d-494f85bda4c3 | -5.77312 | -42.81695 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 98d919be-7b58-38a2-ad42-219996b2dbab | -5.80311 | -43.83686 | 2025-09-26 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c593a7c9-2fdc-34fa-b697-bf5479e7a52f | -5.37418 | -42.2947 | 2025-09-26 04:14:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 360835b6-9b30-3fbb-bcc5-d3c7d6fdcdaf | -10.94459 | -44.29829 | 2025-09-26 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a0f5f00c-a8b4-3113-9dfe-8de55bfa4ab4 | -5.71764 | -44.97835 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a4e92fcb-438a-3ce6-a840-203788cb4026 | -5.73873 | -44.97778 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 8d6ed1d4-40dc-31c6-b0df-cfc4362bad8d | -2.92354 | -48.30223 | 2025-09-26 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bf932441-5725-3efc-90c0-4ce4d48317eb | -6.26041 | -42.48323 | 2025-09-26 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 44a847a9-33b5-3d99-86b9-d8852073b99f | -5.73636 | -44.99273 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 90d68626-4a1b-3c1f-a621-05ee197cdfb5 | -5.73472 | -44.98096 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| e1c0a72d-27e5-3953-8d91-70eef50d0676 | -7.1186 | -43.74006 | 2025-09-26 04:14:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 561e71d6-ead0-3862-9fba-0a28153fd481 | -7.01391 | -41.5878 | 2025-09-26 04:14:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bd9de4ee-d9c9-3130-8f21-4a6f6da8624e | -8.78729 | -43.05771 | 2025-09-26 04:14:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8a8b81ad-841b-34e7-8ece-a7d1320d2fab | -4.8108 | -42.74611 | 2025-09-26 04:14:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0efe2fa6-ae3e-3902-86eb-d641ea67d2c3 | -4.79186 | -42.82407 | 2025-09-26 04:14:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a95770ff-070a-3f5e-addc-17cd49a52c15 | -7.59828 | -44.43148 | 2025-09-26 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10482ac7-28aa-3947-9fee-a339da063e25 | -10.41091 | -46.16749 | 2025-09-26 04:14:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad656c80-7355-3647-98b7-65514c04dfa9 | -5.73814 | -44.98151 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 38786102-d5c7-3e28-a028-a04ad82ddd41 | -10.80466 | -45.37664 | 2025-09-26 04:14:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1a4875af-dc68-3c8d-9d12-5c8aa2eb9e4b | -11.48301 | -38.99677 | 2025-09-26 04:14:00 | NOAA-21 | TEOFILÂNDIA | BAHIA | Brasil | 2931509 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2e17b8f9-6f68-3b63-993a-aeb73a3cfa21 | -6.87545 | -44.50416 | 2025-09-26 04:14:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a6c3ff2b-5671-3d03-9215-7bc460fd0eaf | -8.1958 | -46.38748 | 2025-09-26 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 98cf350f-e202-3f72-9c51-52c4d5e94189 | -10.24046 | -47.02688 | 2025-09-26 04:14:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49eca4ae-5efc-3dfa-8868-58acf01ae61a | -8.71223 | -47.13073 | 2025-09-26 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| adfc9d0f-97b3-327b-b49a-ce91b63bc0b5 | -9.47451 | -48.24102 | 2025-09-26 04:14:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 64e0eb05-85ad-3518-93c7-a8dc6c678809 | -8.14312 | -42.37956 | 2025-09-26 04:14:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7a876085-3e48-3e0e-9b74-3d0561c0a266 | -3.3108 | -48.71346 | 2025-09-26 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e635a8d4-9351-34d0-b5b4-07fb7b6c868c | -8.28127 | -44.37568 | 2025-09-26 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20b6bfe3-6f18-3100-8023-1d8fae29604c | -10.58557 | -46.28137 | 2025-09-26 04:14:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c690035d-79df-34f4-b0e2-e09c368a7542 | -10.28811 | -45.22246 | 2025-09-26 04:14:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 842857fb-4cc4-3f72-8756-74333f9b9923 | -7.67109 | -46.00115 | 2025-09-26 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 692cb721-a3a4-338b-8f9e-75d5b5ab22eb | -6.22664 | -42.85345 | 2025-09-26 04:14:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f29f4c47-a6c2-39b7-9860-9f154cec7329 | -5.74837 | -44.98317 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bf98552c-c660-3324-97a9-e46f6a723a11 | -5.78408 | -43.32964 | 2025-09-26 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 172517e7-fda2-3432-8817-22a24ed2d022 | -5.73413 | -44.98469 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 2da1e026-b3ad-3c11-9fa9-170774a227a1 | -5.72518 | -44.95295 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e004516b-891c-3949-b0b5-c7abe3e430a1 | -6.2571 | -42.48269 | 2025-09-26 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 2f0a8efc-1036-3b92-8c01-e95ad646bc85 | -9.47256 | -48.2382 | 2025-09-26 04:14:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2cf4c65d-fcbb-30ad-8a89-b2b2f0261671 | -7.00665 | -46.99728 | 2025-09-26 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7556fc7-4dc4-3050-a0ac-dd5188472f76 | -10.39531 | -46.13394 | 2025-09-26 04:14:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4dae6626-a1d6-3e5b-929f-e95e75f3a2ac | -7.1306 | -44.8238 | 2025-09-26 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README9.md)
