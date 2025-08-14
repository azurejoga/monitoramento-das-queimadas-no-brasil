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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a7c31f76-0c51-3140-8962-33a1345c7f38 | -12.32387 | -46.06733 | 2025-08-14 03:30:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76976723-2030-389f-916d-fb1253b51dd3 | -9.32898 | -37.98272 | 2025-08-14 03:30:00 | NOAA-20 | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b8fe5c4a-61f6-313b-9d5f-59516a852cae | -8.51952 | -43.29329 | 2025-08-14 03:30:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| dbdab281-4e43-35eb-9123-6585f4df93e8 | -6.95245 | -44.55529 | 2025-08-14 03:30:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e834c83a-7719-38d4-9d70-2a5622054a2d | -12.31738 | -46.06606 | 2025-08-14 03:30:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc6e98d1-7d2b-3c40-97c1-670353cb4caf | -12.31205 | -46.05924 | 2025-08-14 03:30:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 363efe0f-173b-3ef2-91dc-35bb2613a2ff | -8.74207 | -44.03592 | 2025-08-14 03:30:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 15f528f1-3979-32c5-b814-56c98de00848 | -12.31828 | -46.06363 | 2025-08-14 03:30:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e67b5467-b366-314d-a985-7080403dfaf9 | -8.74253 | -44.03415 | 2025-08-14 03:30:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c6dedaf5-d81b-33dd-8277-71afb35bc3e7 | -12.3194 | -46.05811 | 2025-08-14 03:30:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 608bf360-1245-34e8-a2db-e1d2fada9141 | -8.52658 | -43.32077 | 2025-08-14 03:30:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 994e5832-b782-36ff-951f-bba49ea57670 | -9.56317 | -40.35125 | 2025-08-14 03:30:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 76.2 |
| 37b223cd-5926-3ef2-b473-bb267659a076 | -12.31855 | -46.06046 | 2025-08-14 03:30:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aaad6a92-8f92-3762-8793-e5efbcde08c3 | -12.32052 | -46.05257 | 2025-08-14 03:30:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 07ae761d-48b5-382e-9147-9c0bed064164 | -9.04981 | -45.08071 | 2025-08-14 03:30:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6dd61003-13d8-36f1-91f2-5de245be74a0 | -12.31179 | -46.06237 | 2025-08-14 03:30:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a4bbbb4-7037-3012-8aba-463c27a1b224 | -8.74475 | -44.02197 | 2025-08-14 03:30:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d12469ef-89b1-39ff-9c82-edc2e0221912 | -12.3197 | -46.055 | 2025-08-14 03:30:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 265cfe6a-8f35-3e09-b8bd-36173a26164e | -8.74294 | -44.03138 | 2025-08-14 03:30:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d749a8da-e1eb-3012-8d24-a2e42872f339 | -8.5187 | -43.32301 | 2025-08-14 03:30:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 5058b263-48e3-3d92-834e-0c506d009b18 | -8.74424 | -44.02484 | 2025-08-14 03:30:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ab948b8e-c2d6-3a00-a679-a48bba4297ef | -8.52375 | -43.32833 | 2025-08-14 03:30:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 61a51ec1-c90c-367c-8c8b-0720a55cc62e | -8.7399 | -44.01419 | 2025-08-14 03:30:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34a328fc-28a7-3d68-a994-001c8f697140 | -8.52353 | -43.29782 | 2025-08-14 03:30:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| a23d231d-e2e0-3bfa-92a2-163c6b4388ea | -12.31088 | -46.06482 | 2025-08-14 03:30:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| db251301-9141-3a28-9204-5de7d3833055 | -8.52383 | -43.30278 | 2025-08-14 03:30:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0cc5d258-b345-30b9-b884-9401f11d1c73 | -8.52456 | -43.32412 | 2025-08-14 03:30:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 515c597c-4cd2-3f79-b603-b42636390065 | -11.80425 | -44.26912 | 2025-08-14 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 002b2dfc-08cd-3956-a59e-04b2da543dde | -8.52536 | -43.31991 | 2025-08-14 03:30:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 784cac0b-f502-34b9-84f7-26c8a28dd5dc | -12.68689 | -44.95496 | 2025-08-14 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eb3f97eb-c631-3c9e-9479-cc99e2092349 | -9.04914 | -45.08373 | 2025-08-14 03:30:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f1468bee-1d5a-3531-b349-15661a36bb6e | -12.31713 | -46.06932 | 2025-08-14 03:30:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 83400063-4490-34f6-8a3b-29a8eb8ea882 | -13.88826 | -45.56892 | 2025-08-14 03:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d221d1cc-07d5-31e7-9409-279980887857 | -14.79464 | -42.72402 | 2025-08-14 03:32:00 | NOAA-20 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4e44e60-36ad-3d9a-ab18-84131b38a6c4 | -19.63248 | -48.84602 | 2025-08-14 03:32:00 | NOAA-20 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e8e46d9f-11cd-34ec-b643-9a25439b2f6b | -15.55277 | -43.15187 | 2025-08-14 03:32:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8baae5af-58b2-3fef-bb74-56be8e62c1e9 | -18.62468 | -40.00311 | 2025-08-14 03:32:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3d8de379-e6c1-360d-b86b-b41d8d7aaf7c | -20.24368 | -42.30552 | 2025-08-14 03:32:00 | NOAA-20 | MATIPÓ | MINAS GERAIS | Brasil | 3140902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7d492df6-3547-3abd-a6f4-339ad9a99ade | -19.06059 | -42.92561 | 2025-08-14 03:32:00 | NOAA-20 | DORES DE GUANHÃES | MINAS GERAIS | Brasil | 3123106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b89f9ad4-c87c-32fe-b017-ba65d7080f76 | -19.08289 | -48.15743 | 2025-08-14 03:32:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9fb4fc6d-bcd9-3c0e-83f0-6a20bc1b79b4 | -17.63535 | -44.49993 | 2025-08-14 03:32:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 648801fb-1c6d-34ec-baf3-dcc1901cd7aa | -18.5385 | -46.05429 | 2025-08-14 03:32:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4e0a1d28-f3be-30e8-98a4-397a6229f142 | -18.53759 | -46.05846 | 2025-08-14 03:32:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6fb54799-910b-320f-9c01-9583e7325bdb | -16.67241 | -41.36107 | 2025-08-14 03:32:00 | NOAA-20 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 4f2f4f54-73c0-31e4-890b-9d1e58d127cf | -20.27037 | -44.11144 | 2025-08-14 03:32:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 42a71747-24d4-3f82-8d7a-525fb525af71 | -19.25584 | -44.17212 | 2025-08-14 03:32:00 | NOAA-20 | ARAÇAÍ | MINAS GERAIS | Brasil | 3103207 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5776ea27-09d6-316a-8c1f-1ca36940ec29 | -18.72588 | -39.87125 | 2025-08-14 03:32:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| c27653cc-d5af-3b70-a206-326a31a6a6b5 | -18.61501 | -44.26689 | 2025-08-14 03:32:00 | NOAA-20 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0acf229e-b5e5-39cd-9a7f-ab64d281961a | -20.34945 | -45.99234 | 2025-08-14 03:32:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4a0f8fb-5418-3c62-bef5-c8ed370e66cf | -19.63097 | -48.85235 | 2025-08-14 03:32:00 | NOAA-20 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c083380d-7e99-34b8-8dc7-07596c2525dc | -15.39967 | -43.06974 | 2025-08-14 03:32:00 | NOAA-20 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a64f8ee2-138e-36bc-81dd-ef80c4a93a56 | -20.19954 | -41.28932 | 2025-08-14 03:32:00 | NOAA-20 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b8c3b196-4d10-3b21-b474-4e337d27679c | -19.07648 | -48.15569 | 2025-08-14 03:32:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67000388-5edd-3dd1-9f96-c9a5e4f13777 | -20.88252 | -43.06457 | 2025-08-14 03:32:00 | NOAA-20 | SENADOR FIRMINO | MINAS GERAIS | Brasil | 3165701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 43e963df-c0f7-32ec-9076-a1c08bb304aa | -14.21943 | -42.43486 | 2025-08-14 03:32:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 26a079a2-9fbb-30a7-a2da-43cad9912adf | -18.37848 | -44.48389 | 2025-08-14 03:32:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ad362fc-af0e-3f06-9cee-8442af8716be | -20.34582 | -45.99162 | 2025-08-14 03:32:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 12ec90ee-f682-3cf9-a9f2-b89170273a25 | -14.23886 | -44.59086 | 2025-08-14 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c5235ff-06c1-3482-99f1-19ff5a69a05b | -18.54425 | -46.05577 | 2025-08-14 03:32:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 97026841-62df-3f29-8c04-1cbc434006af | -14.23971 | -44.58675 | 2025-08-14 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c36a817-ef58-384a-8ae2-2b61e8d97e6c | -20.34385 | -45.99121 | 2025-08-14 03:32:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43d5d603-8954-37a5-9605-92db136c8503 | -20.20297 | -41.29408 | 2025-08-14 03:32:00 | NOAA-20 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0dfb365b-ff02-3c66-99fb-e8ef210319cf | -18.53182 | -46.05706 | 2025-08-14 03:32:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 40aee6b0-1c47-3177-8852-d2a62d71dabd | -15.40029 | -43.0666 | 2025-08-14 03:32:00 | NOAA-20 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8e0eb504-f06a-339c-9932-c50f64b33518 | -18.24407 | -47.26296 | 2025-08-14 03:32:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8be1bd61-f8ad-36b3-a818-44cc9335b93e | -18.6202 | -44.26798 | 2025-08-14 03:32:00 | NOAA-20 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cec9f48f-7cfa-329f-8b4e-68afb1914720 | -18.61569 | -44.26357 | 2025-08-14 03:32:00 | NOAA-20 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e212f2c3-dc76-32e8-8c35-8dd7965e3cac | -14.79401 | -42.72729 | 2025-08-14 03:32:00 | NOAA-20 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78a54a5f-1d87-3dfe-93b2-d7cf32e487e4 | -13.88925 | -45.56416 | 2025-08-14 03:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da3eadbd-cdf0-31b5-8915-c8a865338369 | -18.54333 | -46.05999 | 2025-08-14 03:32:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fdf5628f-88f5-39b7-b58a-024d006e2126 | -19.25143 | -44.16775 | 2025-08-14 03:32:00 | NOAA-20 | ARAÇAÍ | MINAS GERAIS | Brasil | 3103207 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 676fdca1-8624-364f-8799-028b7f305cfe | -20.20371 | -41.29013 | 2025-08-14 03:32:00 | NOAA-20 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 501cf36c-aeeb-3dc4-9ef0-a388c03b0908 | -18.24524 | -47.25779 | 2025-08-14 03:32:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 183b4a16-e0be-396c-abe2-4c968113952b | -18.53275 | -46.05285 | 2025-08-14 03:32:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ee239c0d-439f-389b-9134-1ad9ea8080a5 | -18.72681 | -39.87005 | 2025-08-14 03:32:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 18640bd9-a638-3ffc-a7aa-dc57c2c814bf | -14.21882 | -42.43792 | 2025-08-14 03:32:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e304883c-898a-3b24-80b4-c1326c948dbb | -19.06538 | -42.92625 | 2025-08-14 03:32:00 | NOAA-20 | DORES DE GUANHÃES | MINAS GERAIS | Brasil | 3123106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d3966eae-996b-386b-977b-d33cf29d753a | -17.63442 | -44.50431 | 2025-08-14 03:32:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e23a1e7c-dc46-396f-b33f-3d2887e02305 | -19.25649 | -44.16899 | 2025-08-14 03:32:00 | NOAA-20 | ARAÇAÍ | MINAS GERAIS | Brasil | 3103207 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d56a189-859d-33cf-a31d-58d6278d9bca | -15.55216 | -43.15493 | 2025-08-14 03:32:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f60dcf2d-6132-35cc-bd5b-85ae4fe9b3f5 | -18.62088 | -44.26468 | 2025-08-14 03:32:00 | NOAA-20 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4720c6a4-8f75-3180-9018-3e709421a2a7 | -17.63974 | -44.50566 | 2025-08-14 03:32:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17f28c6e-2328-3fa9-af30-2b7b42f012bd | -14.23891 | -44.58837 | 2025-08-14 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 71ff04f1-9924-3447-a5d0-5d2cf248326a | -20.19878 | -41.29332 | 2025-08-14 03:32:00 | NOAA-20 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 718216df-6ed8-3eea-aaf9-b73888772f48 | -19.0643 | -42.93164 | 2025-08-14 03:32:00 | NOAA-20 | DORES DE GUANHÃES | MINAS GERAIS | Brasil | 3123106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bfe73433-a4e3-38da-b597-4ef86868df98 | -22.67566 | -47.45889 | 2025-08-14 03:34:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 26f9e6ca-8640-3864-98b5-f62987f4db17 | -23.18553 | -46.5931 | 2025-08-14 03:34:00 | NOAA-20 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| bac80f0b-7ac3-3623-80f8-fa5da8ca34d3 | -23.02599 | -50.37412 | 2025-08-14 03:34:00 | NOAA-20 | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| e3c5c8d7-dc0f-30f6-95fd-7152b0504eb1 | -21.21971 | -48.79834 | 2025-08-14 03:34:00 | NOAA-20 | ARIRANHA | SÃO PAULO | Brasil | 3503703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 33.1 |
| c443e516-7cab-389b-87c7-60528be4ffc6 | -21.31542 | -48.57083 | 2025-08-14 03:34:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4a0d2b91-099d-3d88-96b5-06b933c7c373 | -22.62411 | -47.39207 | 2025-08-14 03:34:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a9895bbc-37ad-3f77-ac0b-e1549a415da2 | -23.54507 | -51.61628 | 2025-08-14 03:34:00 | NOAA-20 | CAMBIRA | PARANÁ | Brasil | 4103800 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 62d83453-e059-3a61-a5bb-017828a7d1c5 | -21.36059 | -45.04571 | 2025-08-14 03:34:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 649ba608-90fe-3398-82cf-4f2702ddb4f9 | -22.66896 | -47.46137 | 2025-08-14 03:34:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 10.6 |
| b61d4709-7014-34b4-bfe0-c7f5add2ccc0 | -21.21791 | -48.80634 | 2025-08-14 03:34:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.8 |
| 9b720ed3-55de-37ed-80b1-d57946c4ec2f | -22.85342 | -49.22538 | 2025-08-14 03:34:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6e0a840f-6dec-3b79-b4b9-797521c32fb0 | -22.59727 | -46.72397 | 2025-08-14 03:34:00 | NOAA-20 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| ac0f8df6-99be-3f4b-8d7f-37e22803f41d | -21.21655 | -48.81189 | 2025-08-14 03:34:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.8 |
| 486b1818-73a6-34c8-b448-ae5e045ad5ea | -22.6643 | -47.4551 | 2025-08-14 03:34:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 5666fb3b-1d5a-38d7-98fe-93d382f2440a | -22.89479 | -43.58562 | 2025-08-14 03:34:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |


[Clique aqui para ver as próximas entradas](README11.md)
