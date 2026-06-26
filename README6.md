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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b5c815e9-0eba-33e6-b185-fae296ed77c0 | -14.87907 | -54.54947 | 2026-06-26 03:57:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1047ab78-8ec5-34f6-93f6-1eafd01f230a | -13.87052 | -47.12188 | 2026-06-26 03:57:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10d8566a-1d09-3b86-ae76-d0d995531268 | -18.09562 | -47.10399 | 2026-06-26 03:57:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b496b5c5-4b5b-3a29-b2f6-84ce2affab00 | -13.92309 | -47.34669 | 2026-06-26 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| de9cfd29-98c4-3699-b320-eb363e7d73f9 | -13.7348 | -54.04919 | 2026-06-26 03:57:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 5340e81f-7bff-38f2-8f1f-2896fe919e40 | -13.73049 | -54.04759 | 2026-06-26 03:57:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 6b71c5c4-1b52-3f91-8bca-e10ffb1e51e0 | -13.06091 | -53.3518 | 2026-06-26 03:57:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0c89849-178a-3ec7-b5f8-d100ab8bdbac | -17.97045 | -44.56584 | 2026-06-26 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e59ff77b-d1a7-3ece-a18d-97fe657cc25a | -13.84262 | -47.14423 | 2026-06-26 03:57:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b3a37bf6-4b8c-3e47-8dc7-43e9f09e45a1 | -14.63378 | -54.46603 | 2026-06-26 03:57:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ced5388e-b27b-3290-9490-26181707124f | -14.84329 | -48.12835 | 2026-06-26 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 632b8186-1992-3d77-900d-0ca35d06e7cb | -13.73746 | -54.04929 | 2026-06-26 03:57:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 26369fdf-9fba-3c89-824f-ea0e6011f1f6 | -14.21094 | -45.62309 | 2026-06-26 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5fb35759-ef94-33ea-b52a-9d29a67a2bcb | -13.73196 | -54.04074 | 2026-06-26 03:57:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| dded9037-9805-38f6-b507-26aacea09c13 | -17.69876 | -43.70918 | 2026-06-26 03:57:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f966a014-610d-398b-b193-5509f4a57ade | -15.64124 | -46.43373 | 2026-06-26 03:57:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6a0e2bfd-4f92-3af2-ae02-973453f90954 | -15.66268 | -49.3842 | 2026-06-26 03:57:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c0d6f11-effe-3b5d-9a85-0bea9e74ef8b | -17.96679 | -44.56516 | 2026-06-26 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 83a97d69-6bf4-3307-8bdf-2dce76903be6 | -20.03372 | -41.45479 | 2026-06-26 03:57:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fd0ed36e-56c0-3a8a-84c3-28a39d346f82 | -13.73324 | -54.05627 | 2026-06-26 03:57:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 016c255e-c80c-3cf6-90c4-dcb927f5741d | -15.63701 | -46.43289 | 2026-06-26 03:57:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2d5bca65-4d5b-3c9b-aa62-cd2663add70d | -13.7278 | -54.04762 | 2026-06-26 03:57:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b639ed66-0418-34e8-a4c4-e6e4c48d2432 | -5.7758 | -45.0599 | 2026-06-26 04:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| d01ef00a-e2a9-36c9-9f88-56f06c556789 | -13.7228 | -54.0496 | 2026-06-26 04:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 61.4 |
| be878688-a6dd-3dba-b767-ee29230bee6a | -13.742 | -54.0475 | 2026-06-26 04:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 8407d3c3-7b44-320e-8a1c-60241d984449 | -29.70823 | -52.61214 | 2026-06-26 04:02:00 | NOAA-21 | VALE DO SOL | RIO GRANDE DO SUL | Brasil | 4322533 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 5ebcdbdd-cf9b-3b9b-869e-8e2b525bd004 | -28.15374 | -48.82049 | 2026-06-26 04:02:00 | NOAA-21 | IMARUÍ | SANTA CATARINA | Brasil | 4207205 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 7fad8e34-8fe7-3d3d-a540-49e5065c1ef5 | -13.742 | -54.0475 | 2026-06-26 04:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 3c64cd5e-7544-30fe-8126-b1bf6df2363b | -13.258 | -54.4315 | 2026-06-26 04:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 2c2de073-89bb-3d03-8a0e-ada229f5a343 | -5.7945 | -45.0586 | 2026-06-26 04:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 1ab7aa48-d9c3-32ff-b2db-3ec960efff8b | -5.7758 | -45.0599 | 2026-06-26 04:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| d37a49d8-6326-308c-ab44-128d953a9f7e | -13.742 | -54.0475 | 2026-06-26 04:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 5d52180f-0a9d-39b0-acf5-661af12ce4a1 | -13.7228 | -54.0496 | 2026-06-26 04:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 7490b560-f570-3ba7-b26d-ba73b6a5946a | -5.7945 | -45.0586 | 2026-06-26 04:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 84232d0d-ee35-3403-93f9-6f524522afb4 | -5.7758 | -45.0599 | 2026-06-26 04:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 36f673fc-1a80-3562-8020-7a6e9f7746e6 | -3.04057 | -40.121 | 2026-06-26 04:27:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 2173d0b8-2ac4-38ce-bded-1416047e00e1 | -2.9515 | -39.9222 | 2026-06-26 04:27:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8499a799-56d6-3328-b24b-2a52803340d1 | -5.79318 | -43.88814 | 2026-06-26 04:29:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9dcd0ccb-3a1c-3bb3-a716-0d2fbc66be27 | -7.65019 | -37.12232 | 2026-06-26 04:29:00 | NPP-375D | PRATA | PARAÍBA | Brasil | 2512200 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d86706ff-4a93-3bbb-925c-5cc9018f0b8a | -8.13733 | -47.88366 | 2026-06-26 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 20713c75-5982-38ca-8cfc-770f3c5303f2 | -7.74507 | -44.61834 | 2026-06-26 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 333bd9e6-2507-3f8d-9231-e26f620899a0 | -6.30252 | -44.64782 | 2026-06-26 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a6d004f6-c7a7-3205-a151-6a30be070bdd | -5.78366 | -45.05946 | 2026-06-26 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 1de85d27-2e23-33c0-8637-f4727591d40f | -6.5038 | -42.21435 | 2026-06-26 04:29:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f3b59c8a-120a-3aea-9f65-fc7e36024e7f | -5.78983 | -43.88761 | 2026-06-26 04:29:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f7f45188-26e0-326f-9b99-2b3da00528a9 | -5.32813 | -44.6925 | 2026-06-26 04:29:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 520307f8-0441-396a-b04e-dfe405400774 | -6.30584 | -44.64835 | 2026-06-26 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b843286-b6b8-3091-a3c8-5bc93c047765 | -5.72621 | -49.10537 | 2026-06-26 04:29:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e1709321-ee63-3422-8466-97d70b1e7fa5 | -4.94456 | -48.24311 | 2026-06-26 04:29:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| de9cb5f7-5357-3b71-b285-08e0d79fcabd | -4.35218 | -47.7609 | 2026-06-26 04:29:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d16003e-af75-320e-ab61-6f7af83e7a31 | -8.49635 | -44.74419 | 2026-06-26 04:29:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5e487173-8d91-3db4-8b2d-f7dd07810bbe | -5.78144 | -45.05199 | 2026-06-26 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| caa69df1-3308-36f3-8701-c973f3f92f92 | -5.58364 | -42.20138 | 2026-06-26 04:29:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 40383ade-6d27-38f9-9328-3b7d9dcffcdd | -6.50674 | -42.21885 | 2026-06-26 04:29:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ab8c7a4c-3091-3822-bd10-44008931201d | -7.6274 | -47.29506 | 2026-06-26 04:29:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec8c438f-4d65-367e-9782-0ce8e59de22d | -4.63661 | -43.04944 | 2026-06-26 04:29:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5fc22538-b8e7-3666-888f-8e74d16a2514 | -7.7364 | -44.17998 | 2026-06-26 04:29:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 23864a17-e1df-3f6c-a35f-e40ce098dc87 | -6.93294 | -43.67429 | 2026-06-26 04:29:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ffeac522-ad47-37cd-9128-144b8e02294e | -8.56862 | -47.1793 | 2026-06-26 04:29:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dc314ee3-3154-3990-8641-a420e654b132 | -8.22613 | -48.17741 | 2026-06-26 04:29:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 349a3529-2371-3bcb-ac1e-fe02430c6b83 | -6.97573 | -42.89824 | 2026-06-26 04:29:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 06fd9366-3f45-3a97-b12b-471a74486500 | -6.30142 | -44.65476 | 2026-06-26 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 929e390c-a1bd-3c5a-8fa9-1919541ac654 | -7.75119 | -44.62291 | 2026-06-26 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4fb4cb91-f968-37f3-9b39-57e4c0d80a01 | -5.79165 | -43.63416 | 2026-06-26 04:29:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62200a61-5489-3017-923d-625984dca4dd | -7.7523 | -44.61589 | 2026-06-26 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b4dd85bc-1155-3312-a47d-e726eb44eab4 | -8.23593 | -47.12247 | 2026-06-26 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7f22e2d-5cc6-33cf-9202-9a60ca13baea | -6.97226 | -42.89769 | 2026-06-26 04:29:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 3adf75bc-53bc-38d7-b587-e7421743b4ab | -5.93989 | -43.46667 | 2026-06-26 04:29:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a74692e7-2fd2-37d6-a04c-f096a57011c5 | -8.06262 | -46.38165 | 2026-06-26 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 220a2362-7648-385c-bb7d-e73d24af323f | -7.57261 | -45.87858 | 2026-06-26 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27c37921-9cca-3d61-a39d-a1c41da295a2 | -7.74841 | -44.61887 | 2026-06-26 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c688929f-ca3f-33e1-a1a9-285e2fd76733 | -8.57944 | -46.89731 | 2026-06-26 04:29:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19a75c3c-6350-36ad-bd5d-717ad4a4d2a7 | -5.78532 | -45.04905 | 2026-06-26 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c18a465-4ef7-30d4-9370-2b0006c5ffeb | -5.7892 | -45.04611 | 2026-06-26 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34cacc14-ccfb-30a8-afac-e5c0590f5c41 | -8.2297 | -47.11755 | 2026-06-26 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3fbaed07-e59c-30fc-9f86-a4cd7e8585a1 | -5.78587 | -45.04558 | 2026-06-26 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 341eb786-ce34-3c67-a21e-e5efaefa5f71 | -5.78754 | -45.05651 | 2026-06-26 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 3b10dc25-cfac-3bdc-9d2a-d5d0ca43d359 | -7.72331 | -44.56102 | 2026-06-26 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44cac00d-ea2b-311a-9e43-2bd660dd9ab6 | -7.57205 | -45.8821 | 2026-06-26 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb7b6de5-5d7d-3edc-b48f-71b6c0c8be3e | -8.12895 | -47.89045 | 2026-06-26 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cbee1812-708e-3149-94c5-f6ef64d7d95c | -5.77757 | -45.05493 | 2026-06-26 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bd6a7cf0-8a69-3426-b8cf-71af39f1d939 | -7.72555 | -44.56856 | 2026-06-26 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b5e00634-fb6c-36c8-9122-09df5b1a06a7 | -6.81534 | -44.72164 | 2026-06-26 04:29:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| b1c210a2-869a-39e8-af3c-53adeb2d1531 | -8.19992 | -42.42437 | 2026-06-26 04:29:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| bdda315c-ef9c-3360-b057-63199de3bda0 | -5.78865 | -45.04958 | 2026-06-26 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6548b8ab-30bd-38a4-94c5-c7984976bf55 | -8.05868 | -46.38467 | 2026-06-26 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 976fa19c-289f-39e2-9a32-7648de90b787 | -7.62394 | -47.29451 | 2026-06-26 04:29:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3bf6850d-f67f-3a34-b7c9-bfef9fd184f4 | -6.98671 | -42.89602 | 2026-06-26 04:29:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| d7702b48-77b0-3e9e-ac88-fc5103d9cc28 | -7.64936 | -50.0271 | 2026-06-26 04:29:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5aeda038-7974-3db7-ada9-c4044804a30e | -7.40061 | -48.15415 | 2026-06-26 04:29:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bef776c4-a01d-3192-8b4a-c27f51817c44 | -4.34852 | -47.76034 | 2026-06-26 04:29:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9491042-1f40-39ec-961a-47b5929f5dfb | -8.49247 | -44.74718 | 2026-06-26 04:29:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c7202e7-6595-349f-83ec-ea718ea1214d | -4.34782 | -47.76456 | 2026-06-26 04:29:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07a5c181-3baf-3691-b294-203e123fd523 | -8.01182 | -49.64463 | 2026-06-26 04:29:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0109c785-3d42-3126-96cc-b34905bac115 | -8.23251 | -47.12188 | 2026-06-26 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1f8e33da-9c0b-3bc1-977b-853a9e931e06 | -6.81866 | -44.72217 | 2026-06-26 04:29:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f5c9d03-ca11-3f48-8a35-7ac0a082392e | -8.12828 | -47.89444 | 2026-06-26 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3402dfa6-b882-33ee-be57-9f9ea362d5af | -7.93558 | -47.81567 | 2026-06-26 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 049571d1-f02c-323d-a583-5b02fcc6389b | -8.32597 | -47.12529 | 2026-06-26 04:29:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f1c9092-0218-346d-af33-c22c651286da | -5.78422 | -45.05599 | 2026-06-26 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |


[Clique aqui para ver as próximas entradas](README7.md)
