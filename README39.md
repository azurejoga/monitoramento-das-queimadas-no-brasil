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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc107f7f-d933-3562-ac2d-131c5c73161e | -12.79964 | -48.43518 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ad6ee43c-53c5-3eba-967a-b5728d7eaf71 | -14.45405 | -45.62149 | 2026-08-20 04:21:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 41d2fcba-204f-3ab0-85ab-d8f1575691ff | -12.8143 | -48.43844 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5459c916-665e-38cd-a83a-938a677ce579 | -13.4353 | -57.07441 | 2026-08-20 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d3a727a-15fb-3195-ba54-1123f296bbd8 | -18.8828 | -41.09604 | 2026-08-20 04:21:00 | NOAA-20 | MANTENÓPOLIS | ESPÍRITO SANTO | Brasil | 3203304 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 06e94ea1-0757-3c8d-9551-a499fbece1bd | -12.14156 | -48.26593 | 2026-08-20 04:21:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e44ff99-664b-3a04-a492-f302744503d8 | -15.85391 | -56.09012 | 2026-08-20 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 68b79772-1b7f-3b12-b589-cd9e14e11c86 | -13.54626 | -52.23169 | 2026-08-20 04:21:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9ef3c2c7-2d1b-3331-ae7e-bd5f3bdd5994 | -17.77704 | -49.13395 | 2026-08-20 04:21:00 | NOAA-20 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 151900af-e1d7-34fb-a02e-15c9972b7f5c | -14.44468 | -45.61625 | 2026-08-20 04:21:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a5b9c8f-9cf5-3027-83c8-31996929d8bb | -17.33241 | -43.62576 | 2026-08-20 04:21:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 4d11835a-3b43-3b1d-9dc8-efbc66df73b7 | -19.35785 | -42.92297 | 2026-08-20 04:21:00 | NOAA-20 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 125e1392-39db-3963-8089-b000a77e4686 | -13.26494 | -51.63418 | 2026-08-20 04:21:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5a9b7bc2-67c1-36e8-be31-11c18f16e540 | -14.45074 | -45.62093 | 2026-08-20 04:21:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 23744763-6d7f-342c-89f2-508e577075a3 | -11.19708 | -54.01854 | 2026-08-20 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9f778162-5d3b-342a-9cf1-17ec7a550429 | -18.55716 | -48.29143 | 2026-08-20 04:21:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4a6e83af-7832-3841-830b-e9152b8778d2 | -17.93263 | -44.24557 | 2026-08-20 04:21:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1b50ab11-30ce-3772-ad0c-98b5beb1471d | -13.93953 | -53.87147 | 2026-08-20 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 84f08183-63a3-3433-b8e5-4af7609fba5d | -14.45462 | -45.61793 | 2026-08-20 04:21:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c676c338-1ebe-33b0-a4b2-00ee062ff2c2 | -18.03535 | -44.61315 | 2026-08-20 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 12836a29-a205-369a-a476-02aa8dee4fe0 | -12.83712 | -48.43071 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e4c934e-9fa2-39d5-ac57-183c2ea7af78 | -14.01557 | -53.6693 | 2026-08-20 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d634421-0ddd-3d71-a12e-f0f4f408a77c | -17.95767 | -41.93686 | 2026-08-20 04:21:00 | NOAA-20 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 75e389b6-0932-319b-96b2-06da366016a5 | -17.93565 | -42.80056 | 2026-08-20 04:21:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fe97850d-f821-35d8-99e1-0612504241ca | -17.32953 | -43.62132 | 2026-08-20 04:21:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d7a38739-13c1-3dc9-a6da-54b754fb77ee | -14.01896 | -53.65169 | 2026-08-20 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4e373672-4076-3b78-8603-008f9b36fa07 | -13.44022 | -43.84231 | 2026-08-20 04:21:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 595ae86f-8c13-3b25-ad89-7f77ebf8c401 | -15.36036 | -52.78234 | 2026-08-20 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d7fd745c-2dac-3fa7-9ff3-7852af9f7f90 | -12.75749 | -48.45915 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1d5e283-0a33-35ed-9046-a2cd4c2f0e46 | -11.21165 | -55.05801 | 2026-08-20 04:21:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 7ac2b806-be53-392a-b6e1-39fd529dbd7a | -14.45519 | -45.61436 | 2026-08-20 04:21:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f5da0d0d-4a87-35bc-b5d3-c4a4767671be | -11.42354 | -54.32164 | 2026-08-20 04:21:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ecfdc220-374e-3f67-8c8a-7cda8f7c2031 | -11.21742 | -55.05922 | 2026-08-20 04:21:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 03c31e2f-910a-320f-8759-8678223a1306 | -12.48882 | -54.72585 | 2026-08-20 04:21:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e1efec0-1b15-3da3-bc78-05d094c093cd | -17.679 | -40.26221 | 2026-08-20 04:21:00 | NOAA-20 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| aa803b10-3c56-3762-8d01-59c2346056b0 | -12.78064 | -48.41288 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 94590926-50a3-3ed8-8fd9-53b57436192f | -13.45327 | -51.42611 | 2026-08-20 04:21:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c15718a2-57c1-3a9d-b786-f32d9fbec52f | -11.21822 | -55.05514 | 2026-08-20 04:21:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 53b13bce-3199-3049-aa8c-3fb3b8c89ca2 | -14.08346 | -40.95963 | 2026-08-20 04:21:00 | NOAA-20 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| aa03a771-59a0-3604-8075-b69a358c7dd3 | -13.443 | -43.84647 | 2026-08-20 04:21:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| cbf7e7ce-872b-35fb-9bb7-d04669c0993b | -13.47795 | -51.43808 | 2026-08-20 04:21:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e5a9921f-c472-396a-904e-19dcac026d6e | -15.36084 | -52.7546 | 2026-08-20 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2887ea9-9704-3d3d-92e8-48cc9c6b5e04 | -15.5847 | -43.74041 | 2026-08-20 04:21:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fd82699f-a7e9-3749-97b1-97f4f31b7d64 | -20.35094 | -41.54921 | 2026-08-20 04:21:00 | NOAA-20 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e5f68a8b-23a6-33e5-8c26-d63109ddb691 | -12.81955 | -48.42257 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f2a39338-c413-3ead-a084-81d4d7b1379b | -14.45017 | -45.62449 | 2026-08-20 04:21:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9b704718-71fd-35ea-b675-b20d3019b34a | -19.65907 | -45.90401 | 2026-08-20 04:21:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| bcce3aad-2b26-3b00-892a-e9af64617ffc | -15.56417 | -43.434 | 2026-08-20 04:21:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6af76dbb-d73d-3185-8772-0a9afd03602f | -10.90582 | -56.36954 | 2026-08-20 04:21:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2cac437b-acf7-3943-9986-afa611f6e872 | -18.03479 | -44.61692 | 2026-08-20 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 20.0 |
| b226fb64-5947-30e5-af7f-148e3b9c9c24 | -11.19168 | -54.0174 | 2026-08-20 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 455d487d-9114-31f3-b9b5-ec64aab2af0e | -12.77322 | -48.4119 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 82f93b03-85fe-38e0-a9f2-96618693eeb8 | -18.03422 | -44.62068 | 2026-08-20 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 2fb14977-716f-3866-8961-210a8fe273ed | -12.7945 | -48.42073 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 736cecd4-176f-3ed1-8265-f0356843f797 | -17.33529 | -43.63021 | 2026-08-20 04:21:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 2711bb31-9ca1-3c97-a3b2-3b20f70e8cee | -12.00438 | -53.44567 | 2026-08-20 04:21:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9d8b9a4-fda3-3af8-bc1e-58c615ea11dd | -12.78434 | -48.41343 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f13a03ba-fe94-3a0c-a095-49f592e9d89f | -20.52927 | -47.54148 | 2026-08-20 04:23:00 | NOAA-20 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b57b83d6-d43c-3d04-a476-0352e892dad2 | -20.26418 | -46.7425 | 2026-08-20 04:23:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f3003ac-edf0-3d20-b0c5-1c77db0f4af7 | -23.41867 | -46.9553 | 2026-08-20 04:23:00 | NOAA-20 | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1635408c-3c89-3cd6-b0e4-21a52cc40c78 | -21.86983 | -46.57241 | 2026-08-20 04:23:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| e5ce23da-2f76-31d5-805c-0ffdd6ee16a8 | -20.29773 | -46.68052 | 2026-08-20 04:23:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb0b0e7e-891f-345a-a8b0-fa75fcb65d10 | -21.58454 | -45.89461 | 2026-08-20 04:23:00 | NOAA-20 | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3372f12b-cca0-3abd-b5a6-2a46afed115f | -23.47144 | -46.28386 | 2026-08-20 04:23:00 | NOAA-20 | ITAQUAQUECETUBA | SÃO PAULO | Brasil | 3523107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2d0d0f3e-f4b9-3f7a-887d-c1d1e94e51af | -23.00494 | -50.02773 | 2026-08-20 04:23:00 | NOAA-20 | CAMBARÁ | PARANÁ | Brasil | 4103602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d08d97e3-4e17-3c20-bb78-c2f13ed5b68f | -21.1113 | -45.61036 | 2026-08-20 04:23:00 | NOAA-20 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bd3b3faa-aace-3363-8a73-630a7bcc9645 | -20.29237 | -46.4573 | 2026-08-20 04:23:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7b6570fe-e367-3837-bad3-4af5e8e067e8 | -20.2597 | -46.74926 | 2026-08-20 04:23:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df207fb7-97e9-359e-a4c1-7c93ac67d9fc | -20.28995 | -46.68666 | 2026-08-20 04:23:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7cfa3d38-9e4e-3415-b690-56e278bde079 | -21.3581 | -43.69773 | 2026-08-20 04:23:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e806deac-7889-39e5-8274-c1e25431b64c | -20.28585 | -46.71237 | 2026-08-20 04:23:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b0d99ef4-940d-3c50-b776-9cd158329db4 | -21.87041 | -46.5687 | 2026-08-20 04:23:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 225ef48c-6d80-3147-afc1-79da778c02dc | -21.44572 | -48.51506 | 2026-08-20 04:23:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8cf019fa-7c5f-3e60-9cc2-0d69cde130a7 | -21.87762 | -46.56616 | 2026-08-20 04:23:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 93f3d803-9069-3d92-98a9-41e34507ef13 | -20.96641 | -44.12098 | 2026-08-20 04:23:00 | NOAA-20 | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ada0974e-f17d-3091-b9ef-833cf52eb779 | -20.80214 | -43.85769 | 2026-08-20 04:23:00 | NOAA-20 | CRISTIANO OTONI | MINAS GERAIS | Brasil | 3120409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f38b33dd-c61a-3782-9016-551a904c3ac5 | -21.71534 | -47.14322 | 2026-08-20 04:23:00 | NOAA-20 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8519b51c-e4c5-35ae-896c-34ee7515fe91 | -20.41925 | -45.43793 | 2026-08-20 04:23:00 | NOAA-20 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| db67b6f6-ad83-3fac-98a7-b15089a63d67 | -20.89831 | -50.50521 | 2026-08-20 04:23:00 | NOAA-20 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 83806c22-bb7d-3912-b335-5ac8e7227b71 | -21.3759 | -43.74345 | 2026-08-20 04:23:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2492c4d8-b4e2-3560-a4e5-5f742730c414 | -20.27644 | -46.72964 | 2026-08-20 04:23:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6397c64-88cd-3997-9bc7-92dfa6ad391e | -21.87993 | -46.5513 | 2026-08-20 04:23:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 047e0ed6-baa2-34b4-8c66-d6982dadad90 | -20.68578 | -45.2689 | 2026-08-20 04:23:00 | NOAA-20 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d51f3e6c-f01f-3c51-bba1-9fb3ea8f5ce7 | -21.71203 | -47.14261 | 2026-08-20 04:23:00 | NOAA-20 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cf48efc6-21ee-382e-b547-bcad866feca9 | -22.20695 | -44.62394 | 2026-08-20 04:23:00 | NOAA-20 | ALAGOA | MINAS GERAIS | Brasil | 3101300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| bf183b93-fcce-3c4b-b00e-da27126a1fec | -23.25492 | -47.67096 | 2026-08-20 04:23:00 | NOAA-20 | BOITUVA | SÃO PAULO | Brasil | 3507001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1931aaed-7582-398b-ac3f-9a310da7c17c | -23.11965 | -48.66761 | 2026-08-20 04:23:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 98e07193-9188-3fd1-a532-da269ec3c603 | -21.87314 | -46.57301 | 2026-08-20 04:23:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| fedcc562-600d-3e4d-b7fe-515a7bcb1e06 | -23.12098 | -48.66705 | 2026-08-20 04:23:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 47ad3eb8-7672-3362-b2cc-0fe93b78b0de | -21.83025 | -48.41978 | 2026-08-20 04:23:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bb06e7ce-18ff-3725-b0bf-39f98fa8d6d6 | -23.41925 | -46.95153 | 2026-08-20 04:23:00 | NOAA-20 | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ba1c2640-2ed7-3c36-bfbe-88c9cacb7304 | -20.26301 | -46.74986 | 2026-08-20 04:23:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| faa8f5ee-07ff-3aeb-b3dd-74f7310ce06b | -23.40598 | -46.42121 | 2026-08-20 04:23:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 197a29b0-fdde-3986-93a9-947dbcc27503 | -21.8743 | -46.56557 | 2026-08-20 04:23:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 3695e176-7839-3e6d-822f-51596cd6c700 | -21.36168 | -43.6983 | 2026-08-20 04:23:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 114fec56-4252-3755-842d-33eee025e0eb | -20.52644 | -45.37865 | 2026-08-20 04:23:00 | NOAA-20 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d2a9f85f-bfa7-3a40-801b-6d4e1c190e91 | -20.26359 | -46.74617 | 2026-08-20 04:23:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a331da0-1737-3ecc-8ba5-e03789582d0d | -20.52594 | -47.54087 | 2026-08-20 04:23:00 | NOAA-20 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| caf7f106-d581-3219-b0b2-278c0d9dbfa4 | -22.70074 | -43.36079 | 2026-08-20 04:23:00 | NOAA-20 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c4329c3a-e37f-38b8-a71e-c3d34f776deb | -21.87372 | -46.56929 | 2026-08-20 04:23:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |


[Clique aqui para ver as próximas entradas](README40.md)
