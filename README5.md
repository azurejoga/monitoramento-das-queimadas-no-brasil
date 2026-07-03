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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe47d5d9-04ac-374a-b2e3-91f08776d3e0 | -17.3242 | -42.6381 | 2026-07-03 02:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 26ad61e6-c66e-3bcf-9312-fa6d171f8e65 | -17.3041 | -42.643 | 2026-07-03 02:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 11a94748-b66f-3233-8cb2-e8751b0c7c24 | -10.9397 | -43.0593 | 2026-07-03 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 307.1 |
| ab0e7ad2-86cb-3335-81fc-24cd2617ac8a | -17.3242 | -42.6381 | 2026-07-03 03:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 6c078a07-fb24-3d82-acfc-066ecbce2606 | -12.7359 | -44.5225 | 2026-07-03 03:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 1d2684cd-11f4-3375-ab63-7f36d4afd741 | -17.3041 | -42.643 | 2026-07-03 03:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 64.1 |
| cf443dfe-e915-303c-9965-33fc1d79eceb | -5.7945 | -45.0586 | 2026-07-03 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 346b1650-5f89-3a84-84fd-3aec06afe5e0 | -12.7548 | -44.5428 | 2026-07-03 03:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 1f5d7a20-37df-36be-be32-4deb058f55d3 | -12.7557 | -44.4959 | 2026-07-03 03:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 55.3 |
| b3c21565-7d3e-301b-a64b-870b0fdecc33 | -12.7553 | -44.5194 | 2026-07-03 03:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 244.7 |
| e2e8fa19-de4f-3e9d-a1e7-dcdaf77429ea | -10.9588 | -43.0565 | 2026-07-03 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 0dd6e58b-2a1b-3925-8f8b-b5f5597abbcf | -10.9401 | -43.0355 | 2026-07-03 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 206.4 |
| 3a6bbb64-3112-3671-98bc-d5ebde8fe47e | -12.7359 | -44.5225 | 2026-07-03 03:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 53.5 |
| a50e0b94-530a-3f53-9bb5-23afc0220f3c | -10.9397 | -43.0593 | 2026-07-03 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 216.5 |
| 489a3a54-962e-3a97-a872-0691e4aa3b0f | -12.7553 | -44.5194 | 2026-07-03 03:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 226.2 |
| 19f11a85-bc10-3c1c-a33e-ef28f1b27b0a | -5.7945 | -45.0586 | 2026-07-03 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| c63b5da3-c983-3a17-802a-f32d9dfc2512 | -12.7548 | -44.5428 | 2026-07-03 03:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 625d66c4-8f7f-34b4-b0ab-c3f0f1d4f1a3 | -10.9588 | -43.0565 | 2026-07-03 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.8 |
| fcf63bbe-22a3-36d4-b1a1-22064d9bd346 | -12.7557 | -44.4959 | 2026-07-03 03:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| fcaa0925-b58f-3330-a024-ec472c291b50 | -17.3235 | -42.663 | 2026-07-03 03:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 44.4 |
| fa739288-6313-3970-84af-d88ade9a7f64 | -10.9593 | -43.0326 | 2026-07-03 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.8 |
| ad8ee501-3688-3a41-88ca-3304672e9c8d | -10.9401 | -43.0355 | 2026-07-03 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 166.9 |
| 955bb533-8540-3692-87fd-32cf6d49d641 | -17.3242 | -42.6381 | 2026-07-03 03:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 82.6 |
| a691f622-5ec1-3e84-85b2-ea442232370b | -12.7548 | -44.5428 | 2026-07-03 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |
| d3816d00-fd28-39db-a31e-5a8141f04de7 | -17.3242 | -42.6381 | 2026-07-03 03:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 30a20196-94a2-31b8-ba71-821f3cd1fecb | -12.7557 | -44.4959 | 2026-07-03 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 6f36b6a0-062f-3cfa-aec6-df8f9a1164ac | -12.7553 | -44.5194 | 2026-07-03 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 211.7 |
| 9323a3ec-61a8-329e-91bf-5b09caeed8c4 | -5.7945 | -45.0586 | 2026-07-03 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| bf59ee87-a111-3593-866e-d7fb14491d6c | -10.9588 | -43.0565 | 2026-07-03 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 99d99695-ba11-3e17-ab60-2268f874fcb5 | -10.9401 | -43.0355 | 2026-07-03 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 186.1 |
| 0c7b8fcc-fdf0-34f4-886f-57db49563fed | -17.3041 | -42.643 | 2026-07-03 03:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 53.8 |
| d4c131b1-270d-32f9-b1fb-38eb0d00f71b | -10.9397 | -43.0593 | 2026-07-03 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 240.0 |
| da59daf6-8374-3ad9-ba83-79119e6cec74 | -12.7359 | -44.5225 | 2026-07-03 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 4bd45b14-25e2-344f-9051-1f6fccdd3bcb | -3.41548 | -41.71527 | 2026-07-03 03:21:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| a967292a-4122-3a29-a136-1da935a766e3 | -3.42282 | -41.71103 | 2026-07-03 03:21:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3c7176f1-966a-3836-9c3b-d6a1a2d24bbe | -3.4158 | -41.70512 | 2026-07-03 03:21:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 21.6 |
| ed94d367-fbf4-3528-a0a1-021e8d6c2841 | -3.42374 | -41.70573 | 2026-07-03 03:21:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9706f104-b8d3-33f1-b391-f2bd82eaccd0 | -3.41491 | -41.71045 | 2026-07-03 03:21:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 17a46364-9c4a-3da6-9bd1-00f4aebb3322 | -3.41734 | -41.70456 | 2026-07-03 03:21:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 24.6 |
| 58297aa6-333f-3b6e-b237-7e1596457bc0 | -3.41642 | -41.70989 | 2026-07-03 03:21:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 2feb8785-7968-3ab7-b516-02848368851a | -3.86989 | -42.9768 | 2026-07-03 03:21:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 18ef2bd2-cf97-31b1-a127-571d9ebf6871 | -3.42221 | -41.70629 | 2026-07-03 03:21:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| cde476a2-7fd0-3ae8-bb62-ed646eb6beba | -3.50488 | -38.98423 | 2026-07-03 03:21:00 | NOAA-21 | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| dfcefcb6-2e15-3c60-9270-468fc11ba423 | -3.42132 | -41.71161 | 2026-07-03 03:21:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| a37c3073-3e95-3a11-9751-bcb2e17933fd | -3.50545 | -38.98082 | 2026-07-03 03:21:00 | NOAA-21 | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5e6706ed-5e27-309e-9b3e-cc96b3b6647e | -5.80474 | -43.80767 | 2026-07-03 03:23:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| c43d00d5-3e2b-3cf7-a105-5bbd07b8670d | -6.90884 | -43.72429 | 2026-07-03 03:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 738320a8-162c-3421-8bce-5b526127cbde | -6.92988 | -43.72888 | 2026-07-03 03:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c8749709-04c8-36d5-b684-2a10959c35fd | -5.81028 | -43.80793 | 2026-07-03 03:23:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f502d480-a295-321b-837c-5417be2676b5 | -5.80325 | -43.8069 | 2026-07-03 03:23:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f51f0ea8-d863-3e5b-afe0-5af3ff445ac9 | -5.81155 | -43.80118 | 2026-07-03 03:23:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 38551627-4ef0-35b5-9e1a-e23aa9d485fb | -5.9368 | -43.47282 | 2026-07-03 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 260eeacf-db12-39e8-bbfa-3d85cd149594 | -6.90111 | -42.84914 | 2026-07-03 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 631654b3-8dbd-3613-82b9-638e676b552e | -6.92488 | -43.714 | 2026-07-03 03:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 62a1644e-4064-3a0d-925d-421029a5e241 | -6.90881 | -43.65372 | 2026-07-03 03:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1a9e868f-a71f-39b7-87c8-879672eac8fd | -6.92426 | -43.72115 | 2026-07-03 03:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e1ba7d5c-8e5d-3264-81a0-0304edbd1fee | -5.94364 | -43.47412 | 2026-07-03 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ac7c6d90-762a-3060-857f-725c2075cc91 | -6.20418 | -42.52054 | 2026-07-03 03:23:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| db89cd17-64bc-3c55-81fa-b65e0604e617 | -5.93798 | -43.46637 | 2026-07-03 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e07f62cb-ac6e-3838-8e88-30dd0fb73178 | -6.92547 | -43.71478 | 2026-07-03 03:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 41ecbe07-ac9c-395c-bf73-34aa04d1ee1a | -5.80451 | -43.80016 | 2026-07-03 03:23:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 672ef670-0f7e-39c4-a396-46acb0a2317c | -5.79317 | -43.6345 | 2026-07-03 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f1e0c75e-ea1d-3a8f-aca1-448274a7313a | -6.90004 | -42.85492 | 2026-07-03 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b08415f6-de92-3523-9595-e6a299686b8a | -6.92304 | -43.7276 | 2026-07-03 03:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3156a92b-b2fd-30c2-9413-ed19286be984 | -6.20532 | -42.51427 | 2026-07-03 03:23:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 08efbbb7-b24e-3c2a-b5a2-452fb680e79f | -6.9323 | -43.71609 | 2026-07-03 03:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f510afb8-2bc5-3fad-9108-d360ee548490 | -5.80596 | -43.80094 | 2026-07-03 03:23:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 96fc4b08-f46f-38e7-9652-e53ce29009cc | -5.90967 | -43.62086 | 2026-07-03 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7ba5ac83-f1ab-3c38-bb74-af0c82ea2ce9 | -6.91742 | -43.71988 | 2026-07-03 03:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a38d30af-c828-3d18-b42f-70532d5c0d89 | -6.91002 | -43.71784 | 2026-07-03 03:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a907bca1-bea8-3fc2-8d07-1e0f8e66d0d4 | -7.27994 | -44.50111 | 2026-07-03 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f6c4f0d8-da48-3d3d-a5a7-0d37dee1257e | -6.9311 | -43.72244 | 2026-07-03 03:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9b7323df-697d-3397-8e58-59d40ae0922d | -6.91687 | -43.71908 | 2026-07-03 03:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 62af82ae-4a57-3134-9dd1-c84749382503 | -6.92371 | -43.72039 | 2026-07-03 03:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ccaf84f4-c3b9-37ac-8ae4-aa00c7fba616 | -7.27283 | -44.49976 | 2026-07-03 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 45a21aac-ba5f-3630-821b-9bb4f6369ab2 | -5.90844 | -43.62754 | 2026-07-03 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b1bbee55-8aea-3ec7-9b06-6c5c68fc71ea | -6.91057 | -43.71865 | 2026-07-03 03:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| bb2ea270-3d2c-3797-a50f-24197fd2e761 | -6.90934 | -43.72509 | 2026-07-03 03:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 5b916471-a8ef-305e-b2d2-adf8d70e598a | -12.74465 | -44.53695 | 2026-07-03 03:25:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| dac09a5a-cb9b-3a9e-88f5-3ced8bcaeea8 | -12.74999 | -44.54402 | 2026-07-03 03:25:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| d447e34d-ec95-38dc-b0a6-21c67bcf5a61 | -12.74645 | -44.52422 | 2026-07-03 03:25:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 1d7b8bd6-5676-3072-ad0f-8959c06cf943 | -10.93703 | -43.04871 | 2026-07-03 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.0 |
| fabbdaaa-cd58-34d3-8be3-52fd115f17b3 | -17.31329 | -42.64919 | 2026-07-03 03:25:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 8800b02c-9355-3d35-8dfe-3750c1b1f36c | -17.26052 | -42.66041 | 2026-07-03 03:25:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 02888049-fea1-30d9-81b1-f789d4fa6b17 | -12.50471 | -43.80634 | 2026-07-03 03:25:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 04be4bdd-fc3a-3f9d-bd6c-1ccd8b9bee1f | -12.49843 | -43.80511 | 2026-07-03 03:25:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7021bb60-872c-3700-9850-0929e0508e36 | -10.94126 | -43.05971 | 2026-07-03 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 1e3832d2-9505-391b-b236-998be58fd4c6 | -12.75116 | -44.53833 | 2026-07-03 03:25:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.9 |
| eb62b9d5-4fbd-3cad-abff-b526f5b72f50 | -17.31252 | -42.65286 | 2026-07-03 03:25:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 53.8 |
| eaa00c93-9274-3aa4-938a-d1a2c8aab940 | -11.92231 | -43.39018 | 2026-07-03 03:25:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fa44facb-0d61-3dab-81ea-04031f502a8c | -12.85139 | -44.41102 | 2026-07-03 03:25:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a04969ba-ed5f-30de-8219-da654ff5b7c1 | -14.41293 | -44.59307 | 2026-07-03 03:25:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f795ccfe-c029-30d8-b3dd-364fd9167e50 | -12.74815 | -44.51988 | 2026-07-03 03:25:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 36.3 |
| e693d27c-58d1-3be8-b13b-e4563e684684 | -12.75232 | -44.53266 | 2026-07-03 03:25:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.9 |
| c54d581c-a601-3762-a073-9729f424aad2 | -11.92384 | -43.38895 | 2026-07-03 03:25:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 00ec87eb-e801-34d1-aaeb-e45b85d24675 | -12.75296 | -44.52559 | 2026-07-03 03:25:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 758fe6d5-dd57-3938-91d7-4c373afc17f9 | -12.74698 | -44.52558 | 2026-07-03 03:25:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 36.3 |
| dea566e7-dd77-3c63-bdf4-abfdf44e5070 | -12.74405 | -44.53554 | 2026-07-03 03:25:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 221e97af-5ede-3213-b738-e5fd2258efff | -15.69282 | -43.29113 | 2026-07-03 03:25:00 | NOAA-21 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 713e80be-ca03-3126-a6fe-118e03c54fa8 | -12.50366 | -43.81144 | 2026-07-03 03:25:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README6.md)
