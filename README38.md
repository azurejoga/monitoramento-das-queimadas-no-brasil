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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 19678566-45ce-3071-8cf6-d206ab2c05af | -17.0985 | -57.4062 | 2024-10-07 03:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 107.8 |
| ba3adcb3-94e7-3bc9-9d72-4655cbe5e027 | -17.1078 | -56.8304 | 2024-10-07 03:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 117.4 |
| 7a9f51e3-3fb5-37d4-bb7e-28d5a65f9da6 | -17.1178 | -57.4244 | 2024-10-07 03:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.9 |
| f9ef0211-d622-3a80-94b0-8e3cabc61db4 | -17.1274 | -56.828 | 2024-10-07 03:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.2 |
| d041a593-5d3c-39ee-81e3-aa20831bd62d | -17.1278 | -56.8074 | 2024-10-07 03:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.1 |
| 86251dfd-3713-380a-a2de-df75a7a3abf8 | -17.1375 | -57.4221 | 2024-10-07 03:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.5 |
| 595f5c4b-b9f9-3327-8401-f43f4ae62890 | -17.1581 | -57.3582 | 2024-10-07 03:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.2 |
| 3697f79d-540e-36d3-893a-55d911437298 | -17.1584 | -57.3377 | 2024-10-07 03:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.2 |
| 1ca376d0-0db6-33cf-b720-a12b6acd3e3d | -17.6279 | -53.1094 | 2024-10-07 03:06:45 | GOES-16 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 79.1 |
| d9ab1f99-eef3-33a5-8903-64ea29766fb3 | -17.6283 | -53.088 | 2024-10-07 03:06:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 1f79973c-2727-30c5-b784-682ba09d5aea | -18.4718 | -53.5134 | 2024-10-07 03:06:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 2ff984ab-686e-3de8-bf09-571d7442fa8e | -18.6391 | -57.2578 | 2024-10-07 03:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.7 |
| 6f3ff2b8-4d7d-3414-8d57-0228afabeb1b | -18.659 | -57.2552 | 2024-10-07 03:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.2 |
| d5dd4eb2-10c3-37d6-bc9a-665fa2ca8bec | -18.7176 | -57.3097 | 2024-10-07 03:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.5 |
| 3b0464fc-01db-3688-bc53-1a365aa27982 | -18.718 | -57.289 | 2024-10-07 03:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.5 |
| 9d29209b-5b56-3470-8c21-652c355f0b20 | -20.1229 | -49.0518 | 2024-10-07 03:06:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 9a8212dd-91f9-39b7-b325-724e852ab26d | -20.4449 | -47.6875 | 2024-10-07 03:06:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 306.2 |
| 2eb486f6-f8ba-3548-9469-99bc3da63147 | -20.4456 | -47.664 | 2024-10-07 03:06:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 175.9 |
| 3aa27088-dd5c-3a14-8551-ad20dabf76b0 | -20.4655 | -47.6827 | 2024-10-07 03:06:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 486.0 |
| 4ace7f50-8bb8-3da3-b081-58aa680cd34d | -20.4661 | -47.6592 | 2024-10-07 03:06:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 375.0 |
| 56c0f6c3-15d8-3901-a2fc-f230e033ee23 | -20.486 | -47.6779 | 2024-10-07 03:06:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 97.5 |
| b34afa8a-5e0a-3a9b-a24f-f6dd86c74735 | -20.4866 | -47.6544 | 2024-10-07 03:06:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 2c037773-b7c1-3306-bd3f-16af295d5d59 | -20.5848 | -48.5137 | 2024-10-07 03:07:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 150.7 |
| c0f78c59-776f-37c2-8f88-0aff4d7c5f32 | -20.5855 | -48.4904 | 2024-10-07 03:07:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 211.9 |
| ea036136-5abb-3a0e-b0ef-e56bb3558712 | -20.6053 | -48.509 | 2024-10-07 03:07:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 148.1 |
| ab526393-c5df-3ce4-a84b-0f4b767256e6 | -20.606 | -48.4858 | 2024-10-07 03:07:00 | GOES-16 | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 292.8 |
| 70994379-5caa-38fd-9451-bef214e140d7 | -21.5691 | -47.7696 | 2024-10-07 03:07:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 100.2 |
| c537944e-e39c-301a-b802-cb8e6c05b49a | -21.5698 | -47.746 | 2024-10-07 03:07:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 265.1 |
| ef7a1aa9-e701-3768-91d4-1ed9ea878756 | -21.5705 | -47.7223 | 2024-10-07 03:07:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 123.4 |
| b671768c-f6e7-3324-b5d5-e6fa4d2513a0 | -21.5906 | -47.7409 | 2024-10-07 03:07:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 251.8 |
| c1823399-4597-31f5-bb25-96cdac158bc1 | -21.5913 | -47.7172 | 2024-10-07 03:07:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 197.3 |
| 7acfb65e-9549-32f4-8b98-02ccc43e296a | -21.605 | -47.9485 | 2024-10-07 03:07:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 38909890-ee0d-3ea7-864f-082a636bfbbd | -21.6121 | -47.7121 | 2024-10-07 03:07:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 84.3 |
| ed86fdf0-cafb-3f18-88a7-3243e61e5e23 | -5.90253 | -35.43097 | 2024-10-07 03:10:00 | NOAA-21 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 07dc5dbf-8644-3d13-ad94-eec967d7ca72 | -5.90204 | -35.43384 | 2024-10-07 03:10:00 | NOAA-21 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c73f8acb-13ba-34aa-8ec6-f4bd30d67e9a | -10.82358 | -37.16622 | 2024-10-07 03:13:00 | NOAA-21 | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e6d3ff1f-8be0-3605-ba96-9d2ed7ca79e2 | -8.64222 | -40.55377 | 2024-10-07 03:13:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3baf96a2-651d-3410-9881-cedf78a5af14 | -9.63036 | -40.61579 | 2024-10-07 03:13:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 15.5 |
| f8fb886b-1c01-34f1-bf6b-c3b8d9bb3118 | -9.62967 | -40.61393 | 2024-10-07 03:13:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 07371d77-b265-3bdd-845f-5254d314c22e | -9.57576 | -40.345 | 2024-10-07 03:13:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 4a77cb92-470b-3492-ac5a-ce362a72383b | -9.57576 | -40.34281 | 2024-10-07 03:13:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0d2e974e-0b07-30fa-94fb-97b20fa274f4 | -9.56932 | -40.34154 | 2024-10-07 03:13:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0c3f8a3e-7dbb-305a-a892-4f7063a27d13 | -9.56931 | -40.34376 | 2024-10-07 03:13:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a1212450-d048-3f3e-9daa-7751ebf59f2a | -8.85318 | -38.87873 | 2024-10-07 03:13:00 | NOAA-21 | RODELAS | BAHIA | Brasil | 2927101 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 18f6e31d-e3e3-3f48-9ef8-f7a019e22170 | -8.85234 | -38.88324 | 2024-10-07 03:13:00 | NOAA-21 | RODELAS | BAHIA | Brasil | 2927101 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 99177c4c-380f-3a82-ba6d-78d3ebc777d2 | -8.85149 | -38.88774 | 2024-10-07 03:13:00 | NOAA-21 | RODELAS | BAHIA | Brasil | 2927101 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b6077fdc-15a0-3edb-9590-b9fc40ed38a3 | -8.84466 | -38.89116 | 2024-10-07 03:13:00 | NOAA-21 | RODELAS | BAHIA | Brasil | 2927101 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ceaf9af1-4d56-3595-980e-759ca0e84f18 | -8.64336 | -40.54782 | 2024-10-07 03:13:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 548f62e3-d6f3-3d93-973a-45e4e60aa117 | -7.12443 | -35.13795 | 2024-10-07 03:13:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 39.7 |
| ee535938-8887-3cd9-98de-58e0065f1416 | -6.87926 | -39.20447 | 2024-10-07 03:13:00 | NOAA-21 | GRANJEIRO | CEARÁ | Brasil | 2304806 | 23 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 767ce4c1-6c89-30d9-804c-230abaa8834e | -6.87833 | -39.2094 | 2024-10-07 03:13:00 | NOAA-21 | GRANJEIRO | CEARÁ | Brasil | 2304806 | 23 | 33 | nan | nan | nan | Caatinga | 15.7 |
| a393aa8d-ed60-3ad4-b99b-c924c2af9a19 | -6.87579 | -39.20465 | 2024-10-07 03:13:00 | NOAA-21 | GRANJEIRO | CEARÁ | Brasil | 2304806 | 23 | 33 | nan | nan | nan | Caatinga | 22.6 |
| a756b56b-e5ee-37c2-9d2b-9fad82f585f9 | -6.87488 | -39.20967 | 2024-10-07 03:13:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 2db131aa-0ffc-3905-8dd1-2de76dbb7a6a | -6.87296 | -39.20339 | 2024-10-07 03:13:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6a94c7f4-1807-3190-a7f5-823e80548a9c | -6.70095 | -40.88699 | 2024-10-07 03:13:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 27a21461-efd0-355d-9b4e-2532e94e75d5 | -12.71237 | -40.2188 | 2024-10-07 03:15:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| f3eae8f3-bead-3d58-9c87-87dc912c8a8a | -12.71272 | -40.22131 | 2024-10-07 03:15:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 219a1619-dad8-3c46-b32f-aca6f8ce9210 | -12.71369 | -40.21664 | 2024-10-07 03:15:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 46de2ef3-2094-3e84-8fa1-5c7cd1125fa5 | -12.71751 | -40.22459 | 2024-10-07 03:15:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| df581ae4-b15b-3461-9440-6f3cb174d6a6 | -12.71784 | -40.22706 | 2024-10-07 03:15:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| c104b376-d6c3-3993-93e6-dc302df8ea92 | -12.71845 | -40.21995 | 2024-10-07 03:15:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| f23ca41f-3f5d-3cb2-ab05-636c2b2ab871 | -12.71881 | -40.22243 | 2024-10-07 03:15:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 3d9a8d1c-1b35-3362-af33-65aa9422ed89 | -19.33321 | -40.87501 | 2024-10-07 03:15:00 | NOAA-21 | PANCAS | ESPÍRITO SANTO | Brasil | 3204005 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| faa2ed50-e286-3192-94f7-faf7bec32185 | -19.33147 | -40.87359 | 2024-10-07 03:15:00 | NOAA-21 | PANCAS | ESPÍRITO SANTO | Brasil | 3204005 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 342cb185-e298-3705-ad28-d34643b8a244 | -19.33068 | -40.87712 | 2024-10-07 03:15:00 | NOAA-21 | PANCAS | ESPÍRITO SANTO | Brasil | 3204005 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 66cdf1ff-6e30-31d3-a725-3216f1b6683c | -19.31135 | -42.57427 | 2024-10-07 03:15:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d1d6f1d3-5272-3d67-9828-adb7f82eb449 | -19.30565 | -42.57079 | 2024-10-07 03:15:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 41520f0a-4dff-3062-b164-8dbc1e9ac55c | -19.30484 | -42.57433 | 2024-10-07 03:15:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2e3bc841-751e-3667-b840-f7e29501fc29 | -19.28782 | -42.57047 | 2024-10-07 03:15:00 | NOAA-21 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 2588503f-193e-3998-81f1-8786de863341 | -19.28679 | -42.57507 | 2024-10-07 03:15:00 | NOAA-21 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 4b6444bb-5b52-324e-9a58-3214e07aeb3f | -19.28586 | -42.57214 | 2024-10-07 03:15:00 | NOAA-21 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 81c65eee-d40a-32e5-806e-8dd8314c113d | -19.28578 | -42.57955 | 2024-10-07 03:15:00 | NOAA-21 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 9284870b-e640-39dd-b6cb-433df39c33a2 | -19.28478 | -42.57676 | 2024-10-07 03:15:00 | NOAA-21 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 835927ec-81c9-3d37-b988-499b2d4eddda | -19.1998 | -42.52952 | 2024-10-07 03:15:00 | NOAA-21 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 23a54fe5-cce0-38eb-b0da-96dc8facbe11 | -19.13883 | -42.73639 | 2024-10-07 03:15:00 | NOAA-21 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2bc54c38-2e77-33ad-a244-756c8dbe9c09 | -19.13744 | -42.7424 | 2024-10-07 03:15:00 | NOAA-21 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 692fc451-490e-310b-b260-29bb0c95a994 | -19.13591 | -42.73307 | 2024-10-07 03:15:00 | NOAA-21 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 780c8c58-77ae-35bb-b6fc-1d8281d31bf8 | -19.13452 | -42.73925 | 2024-10-07 03:15:00 | NOAA-21 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| b32d1677-6eb0-3620-a94d-976db82a2bf0 | -19.13408 | -42.72859 | 2024-10-07 03:15:00 | NOAA-21 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 2dc5cd1b-bfae-39d5-b99d-04b1990b3245 | -19.13268 | -42.73455 | 2024-10-07 03:15:00 | NOAA-21 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 3e978f97-05c5-39a5-9312-3f55eb7b028c | -19.1314 | -42.74004 | 2024-10-07 03:15:00 | NOAA-21 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 79d58efe-4145-375d-823d-3f31ef818956 | -19.12958 | -42.73201 | 2024-10-07 03:15:00 | NOAA-21 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| a43ba029-651a-3ee1-8121-b24100e20c12 | -19.12837 | -42.73738 | 2024-10-07 03:15:00 | NOAA-21 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 61b5a4d3-ee73-355a-8e4d-8b9fc14d2a01 | -19.12638 | -42.73336 | 2024-10-07 03:15:00 | NOAA-21 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 45e58af9-5952-3d2c-b62b-a43c92727185 | -19.06956 | -42.54577 | 2024-10-07 03:15:00 | NOAA-21 | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 6bb19142-cf0b-3ea3-97dc-abb61a312591 | -19.0678 | -42.54469 | 2024-10-07 03:15:00 | NOAA-21 | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| dead8a98-0d62-331a-bf93-c076046cbc0f | -18.86317 | -42.89958 | 2024-10-07 03:15:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 7da48797-22a5-3102-a391-cbfecd6ba612 | -18.86185 | -42.90522 | 2024-10-07 03:15:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 2d434dd7-1b17-34c7-8d80-972764e6e9eb | -18.86157 | -42.89716 | 2024-10-07 03:15:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| c65b489c-d554-3f30-8429-d50fd0b8eef2 | -18.86025 | -42.90292 | 2024-10-07 03:15:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 009e56d6-c166-3540-bcc8-74fa3ce0af73 | -18.84604 | -43.57781 | 2024-10-07 03:15:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 4ff7202c-aaf3-30e4-9fa5-fb1ed967dcec | -18.84503 | -43.58211 | 2024-10-07 03:15:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| bc183d01-c6b5-310c-8489-71ae11a7c5f1 | -18.66848 | -43.29264 | 2024-10-07 03:15:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f11dcb4f-a799-390b-a1f1-73b9cea7db8c | -18.66839 | -43.29716 | 2024-10-07 03:15:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 2934eae7-8675-37a9-9139-3cce86e9340e | -18.66711 | -43.29844 | 2024-10-07 03:15:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 2df7b2ff-f026-31c6-be9e-dd9bf3bdf49d | -18.4684 | -42.42432 | 2024-10-07 03:15:00 | NOAA-21 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 46798128-aa5e-3fb7-9052-c485a5108b90 | -18.46723 | -42.42942 | 2024-10-07 03:15:00 | NOAA-21 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 5d360bff-d364-3620-aae2-190509a9483e | -18.24748 | -42.21788 | 2024-10-07 03:15:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d80656a2-a5ea-3306-a066-982078f90faa | -18.24561 | -42.21955 | 2024-10-07 03:15:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0a8ce9ec-3d54-3a69-956b-31e04fbd1c17 | -18.03618 | -42.07504 | 2024-10-07 03:15:00 | NOAA-21 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |


[Clique aqui para ver as próximas entradas](README39.md)
