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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7caa74aa-a39a-3693-90ee-01bb1054ca9d | -13.76016 | -41.86607 | 2025-03-12 00:18:00 | TERRA_M-M | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 17.1 |
| a9881796-ed22-3577-acb4-c3659a8fb590 | -11.94374 | -43.92637 | 2025-03-12 00:18:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f7dea788-b986-3cf3-9c51-cfe3677cb5a6 | -17.90267 | -42.62144 | 2025-03-12 00:18:00 | TERRA_M-M | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 4db75d83-64ec-3fde-841f-0e57a4c4b10f | -15.82686 | -41.99866 | 2025-03-12 00:18:00 | TERRA_M-M | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 1a89670c-53d2-312a-9b62-748bef653c2f | -12.20336 | -39.31439 | 2025-03-12 00:18:00 | TERRA_M-M | IPECAETÁ | BAHIA | Brasil | 2913804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| a48336d0-622f-36ce-8ea4-d779548cd4ac | -19.39424 | -42.75914 | 2025-03-12 00:18:00 | TERRA_M-M | CORONEL FABRICIANO | MINAS GERAIS | Brasil | 3119401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| e19657fc-a513-3d5b-9c31-f9ca0fee3c13 | -15.93398 | -42.04203 | 2025-03-12 00:18:00 | TERRA_M-M | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 25facb0a-a092-3d11-a132-0af58d1abed5 | -11.94528 | -43.93842 | 2025-03-12 00:18:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| fd030595-f24f-379b-841f-fb59596873df | -10.83714 | -38.11027 | 2025-03-12 00:20:00 | TERRA_M-M | TOBIAS BARRETO | SERGIPE | Brasil | 2807402 | 28 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 880b6c7d-3664-3cb8-808f-7d4b62bcfea4 | -9.82898 | -40.57283 | 2025-03-12 00:20:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 1197f8e0-77f0-3f40-b920-2474a19fe164 | -10.34863 | -38.48092 | 2025-03-12 00:20:00 | TERRA_M-M | NOVO TRIUNFO | BAHIA | Brasil | 2923050 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| a94761c0-8411-32f7-a44e-278fcd7edc6f | -10.3473 | -37.98461 | 2025-03-12 00:20:00 | TERRA_M-M | CORONEL JOÃO SÁ | BAHIA | Brasil | 2909208 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 02c963ff-8749-3ba0-ae53-7e1a1aee7883 | -10.44152 | -38.35362 | 2025-03-12 00:20:00 | TERRA_M-M | ANTAS | BAHIA | Brasil | 2901601 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| e2fdd5e6-6b42-3d0c-b9c9-6ba828c6832e | -17.9202 | -46.684399 | 2025-03-12 00:44:00 | METOP-C | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 076b373a-4883-3e1b-a79f-61d7b139efad | -13.7941 | -41.861198 | 2025-03-12 00:44:00 | METOP-C | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c10e3597-f4a5-3ec5-9ca3-b4652accb58d | -17.8645 | -46.124401 | 2025-03-12 00:44:00 | METOP-C | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 36196f7a-7d66-3384-87dd-c422e2492930 | -20.189301 | -47.384602 | 2025-03-12 00:44:00 | METOP-C | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 43ad3e8f-e17b-3a3b-80cd-fa74da0ec489 | -13.7907 | -41.8479 | 2025-03-12 00:44:00 | METOP-C | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 941ffb8a-762c-3af2-a998-252b4e7f3a81 | -20.190901 | -47.391899 | 2025-03-12 00:44:00 | METOP-C | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e6928487-0876-3dae-a4f2-e467e806d57a | -19.315701 | -46.1936 | 2025-03-12 00:44:00 | METOP-C | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 22057407-32af-388e-8790-3c198a536236 | -17.932899 | -42.608299 | 2025-03-12 00:44:00 | METOP-C | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a6d27cae-f8ef-37c4-89f7-0d03ca2f55a7 | -20.2782 | -40.239201 | 2025-03-12 00:44:00 | METOP-C | VITÓRIA | ESPÍRITO SANTO | Brasil | 3205309 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 949e0e6d-a927-3064-b6ef-04dda1e2e55f | -15.2915 | -51.470402 | 2025-03-12 00:44:00 | METOP-C | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 77e2ff85-630f-3f18-9948-3574e2fa64ad | -6.9795 | -35.1642 | 2025-03-12 01:30:00 | GOES-16 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 91.1 |
| 23da0790-0250-3ec8-bf12-ea29fdfd2e10 | -6.96275 | -35.14753 | 2025-03-12 03:10:00 | NPP-375D | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 547ec45b-6373-3242-8c57-d596e95d44ca | -9.9396 | -37.16727 | 2025-03-12 03:13:00 | NPP-375D | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Caatinga | 0.4 |
| a149e38d-6fa7-3302-a1b5-a7340b0e7294 | -9.94494 | -37.168 | 2025-03-12 03:13:00 | NPP-375D | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 61d7be57-2b04-3415-91c6-1e23bbe3b5f8 | -9.939 | -37.17055 | 2025-03-12 03:13:00 | NPP-375D | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e01f762d-f424-316d-995f-f76db4c12acd | -9.94234 | -37.17074 | 2025-03-12 03:13:00 | NPP-375D | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Caatinga | 2.0 |
| db0c5c1f-350d-3b6c-aa18-3a9ea3545f66 | -9.94296 | -37.16748 | 2025-03-12 03:13:00 | NPP-375D | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e2c7785f-00f7-3760-8cb2-ee58d9db5f2e | -13.7595 | -41.86377 | 2025-03-12 03:15:00 | NPP-375D | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ed3c9782-2d22-360d-b138-a0656acdbb4c | -13.75502 | -41.86856 | 2025-03-12 03:15:00 | NPP-375D | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0bcdbe78-2bbe-36cb-abb8-5cfd1dccffac | -13.75828 | -41.86958 | 2025-03-12 03:15:00 | NPP-375D | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2b4c6684-d082-3026-a4f3-35ed2e3353b4 | -13.75628 | -41.86276 | 2025-03-12 03:15:00 | NPP-375D | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 70284973-dcd5-3267-ba99-701e81e3fe85 | -10.6964 | -37.05016 | 2025-03-12 03:34:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| cd7c1669-6425-369c-b06f-4fab1ef8d03a | -6.96299 | -35.14669 | 2025-03-12 03:34:00 | NOAA-20 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 37.2 |
| df334b25-a93d-30a8-8a52-84bd7ec39677 | -9.94055 | -37.16944 | 2025-03-12 03:34:00 | NOAA-20 | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 348b73bf-3bef-3f9f-9d37-ec8eb59b714f | -6.13581 | -35.29612 | 2025-03-12 03:34:00 | NOAA-20 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 84439cf5-3930-357a-9df7-2026b57f59b2 | -9.83237 | -40.5685 | 2025-03-12 03:34:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 722d6e72-beb1-3f0e-a238-2d3d092c8b06 | -8.07441 | -34.97618 | 2025-03-12 03:34:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 004e4775-83f3-3e0c-b152-04828702dd6e | -6.95962 | -35.14614 | 2025-03-12 03:34:00 | NOAA-20 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 8b05ec99-46dc-3062-a3f2-73dcb43ea4e0 | -6.96356 | -35.1431 | 2025-03-12 03:34:00 | NOAA-20 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 56e9cf0b-a8d3-3a6a-9c4b-49340363ead6 | -9.82729 | -40.57192 | 2025-03-12 03:34:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c23206c4-529e-3794-8eef-00370bb7fbba | -9.2639 | -36.85557 | 2025-03-12 03:34:00 | NOAA-20 | BOM CONSELHO | PERNAMBUCO | Brasil | 2602100 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 43221abd-2284-3a03-9c0b-84c437ebd5aa | -12.80444 | -42.73193 | 2025-03-12 03:36:00 | NOAA-20 | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 681df43f-b212-3021-987b-b2e93c9052ec | -12.0487 | -40.47235 | 2025-03-12 03:36:00 | NOAA-20 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a8b62b8a-c37d-3651-87c4-443ac69dfcec | -13.75507 | -41.86329 | 2025-03-12 03:36:00 | NOAA-20 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 81094b93-8bca-32ed-b059-48bb142373ed | -11.94093 | -43.93547 | 2025-03-12 03:36:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f2c38ff-271d-3161-872a-98a243b39e8b | -11.9085 | -38.09038 | 2025-03-12 03:36:00 | NOAA-20 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 92fbca2c-2af2-3596-98b5-577c6d272aaa | -16.67895 | -43.88543 | 2025-03-12 03:36:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 30f1d27a-468f-377c-ad79-6551cc5a1bee | -11.94156 | -43.93217 | 2025-03-12 03:36:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f186d74-4ed5-3662-994d-fa67fb23d42e | -12.19929 | -39.31508 | 2025-03-12 03:36:00 | NOAA-20 | IPECAETÁ | BAHIA | Brasil | 2913804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5f72d4b4-6cc2-35d3-b0f8-d61a60b57716 | -13.75948 | -41.86417 | 2025-03-12 03:36:00 | NOAA-20 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e0fee343-3bcf-3196-8f93-e873279cc0a1 | -11.75834 | -40.41632 | 2025-03-12 03:36:00 | NOAA-20 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a20aa7ca-fd02-3df8-b455-e56d5846f432 | -13.75867 | -41.86861 | 2025-03-12 03:36:00 | NOAA-20 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cfbd9200-dc7b-3ee2-b557-b63ed10548e3 | -12.20401 | -39.31085 | 2025-03-12 03:36:00 | NOAA-20 | IPECAETÁ | BAHIA | Brasil | 2913804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 49206126-517b-3a9a-85ea-80ddf4e5dc27 | -17.00944 | -43.32217 | 2025-03-12 03:36:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 939dd587-dc90-3268-86dc-92363d120f0d | -16.67986 | -43.88358 | 2025-03-12 03:36:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0a72e846-4444-332e-b017-459a3c10904e | -21.51625 | -41.09146 | 2025-03-12 03:38:00 | NOAA-20 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b8bb48dc-7991-3c59-bae0-7b3527d6c55e | -22.69578 | -43.34697 | 2025-03-12 03:38:00 | NOAA-20 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a8d43643-6310-3acb-9fc8-018c3eadb185 | -17.88834 | -46.69123 | 2025-03-12 03:38:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03a0d452-6839-3181-9915-287d827bc89c | -19.83344 | -40.11254 | 2025-03-12 03:38:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ed45f787-5aa5-3382-a575-c2cfea97bc5c | -20.85218 | -45.53625 | 2025-03-12 03:38:00 | NOAA-20 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 517cd3fc-0282-38e4-8961-f591105fe671 | -19.83891 | -40.08158 | 2025-03-12 03:38:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 24c9e815-eb0f-3ad9-a9ac-f046d56794cf | -17.88752 | -46.69503 | 2025-03-12 03:38:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4231a69e-64ae-36df-b23b-6f9573b792d4 | -22.69992 | -43.34781 | 2025-03-12 03:38:00 | NOAA-20 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8304a8f1-a5fb-3654-b53c-1872e9e660b1 | -32.36099 | -52.38044 | 2025-03-12 03:42:00 | NOAA-20 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 2.4 |
| 161fecd6-b11e-30d5-ac48-6e5cb1b734b7 | -32.3598 | -52.38503 | 2025-03-12 03:42:00 | NOAA-20 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 2.4 |
| 004d5f9b-b515-3499-b284-67383ea3f917 | -16.68281 | -43.88673 | 2025-03-12 04:27:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 86764d2e-4bf5-3a91-99c9-195f206c7dda | -12.19883 | -39.31535 | 2025-03-12 04:27:00 | NOAA-21 | IPECAETÁ | BAHIA | Brasil | 2913804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b240a22e-5369-3a12-8143-403e12691619 | -11.94416 | -43.93303 | 2025-03-12 04:27:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 61ec0d4f-176a-39b4-9a02-93e5d62d9ba2 | -13.75958 | -41.86002 | 2025-03-12 04:27:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 30d5a225-4b4e-3cad-893c-88b41bb875e9 | -9.82998 | -40.57124 | 2025-03-12 04:27:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 86032459-af59-351e-9600-703e97375f16 | -13.75848 | -41.86839 | 2025-03-12 04:27:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e949b45c-7e0f-3f4c-bacd-abdce1fde5e6 | -12.80892 | -42.73029 | 2025-03-12 04:27:00 | NOAA-21 | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5b9298f5-7d25-3caf-8349-8e8550e29300 | -12.20418 | -39.31316 | 2025-03-12 04:27:00 | NOAA-21 | IPECAETÁ | BAHIA | Brasil | 2913804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| eeede088-b03d-3b57-add9-3d7ba938bbce | -17.00843 | -43.31981 | 2025-03-12 04:27:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a0727c5d-a40a-37b5-890c-f9751ba503ba | -16.34849 | -43.69813 | 2025-03-12 04:27:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bafdd249-c631-38e9-a192-42fc0502f9db | -12.89573 | -45.05554 | 2025-03-12 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 07f7475b-388f-3881-a97f-210af452b7d3 | -15.56889 | -47.85518 | 2025-03-12 04:27:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 16898e48-5d82-3d8a-b85b-626837011cd5 | -9.34188 | -43.08901 | 2025-03-12 04:27:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 83dd5735-0a84-3e4e-95bf-50490ae69311 | -13.75903 | -41.8642 | 2025-03-12 04:27:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 28992b16-c615-37dc-9f83-566b37e7b836 | -14.15256 | -43.92138 | 2025-03-12 04:27:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa20b4c1-f470-3d7d-911a-5377971e960e | -14.19613 | -43.04361 | 2025-03-12 04:27:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0d55990d-ae82-3369-96c8-418df219936e | -10.82424 | -37.16465 | 2025-03-12 04:27:00 | NOAA-21 | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| acf5b7c6-5784-3fff-b23c-08767fce4f76 | -17.7828 | -42.80912 | 2025-03-12 04:29:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ef7c779-40e9-3546-ab9c-fb2337743249 | -17.88866 | -46.69297 | 2025-03-12 04:29:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e0cac988-3dff-386d-93f5-da6ee4b03e05 | -17.56401 | -50.2129 | 2025-03-12 04:29:00 | NOAA-21 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f7239ac9-a2e7-34fd-af2f-45497e2bcf76 | -17.6763 | -42.74184 | 2025-03-12 04:29:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5ed667cb-2217-3be5-a39b-e96ec2a4a09a | -18.63743 | -47.97969 | 2025-03-12 04:29:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 273378ce-2336-31ce-9bfc-be7492ce7ee1 | -17.89212 | -46.69353 | 2025-03-12 04:29:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2061cfb-b4e7-39cd-bbce-4c9b69fd7c12 | -20.16261 | -47.39274 | 2025-03-12 04:29:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d29be42a-dbd7-3e2f-a02a-dcf55ceb07d0 | -18.97861 | -46.96548 | 2025-03-12 04:29:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9e9ede77-3132-35ad-932a-82e89e58d53e | -19.61313 | -44.14222 | 2025-03-12 04:29:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 687694ec-d0c1-3181-abe1-e50651f30ce3 | -20.85809 | -45.53231 | 2025-03-12 04:29:00 | NOAA-21 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d1d1704-31e2-3587-9887-175d28a4f3e1 | -22.76072 | -47.12518 | 2025-03-12 04:29:00 | NOAA-21 | PAULÍNIA | SÃO PAULO | Brasil | 3536505 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d8529b10-da2b-3c9a-9d85-735cc2cf4077 | -20.16204 | -47.39664 | 2025-03-12 04:29:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f664ea2-b489-388d-8b9f-4af9db9ac9bf | -18.98207 | -46.96602 | 2025-03-12 04:29:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2dd89c5a-d52c-39ac-a248-89c93609ce44 | -19.28765 | -46.20164 | 2025-03-12 04:29:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3c4d9cd-553a-3c5a-a470-b0cf5a6c713d | -20.89912 | -46.27943 | 2025-03-12 04:29:00 | NOAA-21 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |


[Clique aqui para ver as próximas entradas](README2.md)
