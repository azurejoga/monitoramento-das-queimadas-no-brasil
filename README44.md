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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b30a094-7f4a-347e-9401-174bc7041d4b | -9.97464 | -46.35048 | 2024-10-05 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8b766d2a-bd14-365c-8a83-2a6dfd2d2d85 | -9.97404 | -46.35366 | 2024-10-05 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb3a1d38-84e0-3fe0-af3a-70a9118de651 | -9.96904 | -46.35199 | 2024-10-05 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ed997ac-b861-38cd-8eec-c7bd21881c07 | -8.97709 | -40.85059 | 2024-10-05 03:49:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 47c34643-9868-3932-9e38-3990357b7e9a | -8.96205 | -40.57772 | 2024-10-05 03:49:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a05afd9d-94a5-3118-bb06-7249f75c4d27 | -8.93418 | -42.59654 | 2024-10-05 03:49:00 | NOAA-21 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 1f8e471f-38b7-39d3-895d-78cec4b4b634 | -8.93012 | -42.59581 | 2024-10-05 03:49:00 | NOAA-21 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 17317998-123d-31d0-88c0-3fb912841be9 | -8.77475 | -44.81599 | 2024-10-05 03:49:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 17.5 |
| c1fcd8f1-a5db-3621-b392-edf799c437f5 | -8.77383 | -44.8212 | 2024-10-05 03:49:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 111.2 |
| fb09c956-1df8-3a4a-b113-5301253494bf | -8.77291 | -44.8264 | 2024-10-05 03:49:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 04f1841b-1ea3-365e-97e4-c93f1d629245 | -8.77002 | -44.81514 | 2024-10-05 03:49:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 37ec29e5-726b-3e83-83f6-317968c40b8e | -8.72157 | -41.58457 | 2024-10-05 03:49:00 | NOAA-21 | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 0029c0e2-5aff-34e1-9789-2c81de94ecdb | -8.71975 | -41.58664 | 2024-10-05 03:49:00 | NOAA-21 | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 5a9aaddc-dd3b-341f-8b2e-0fd22d025320 | -8.37122 | -43.65576 | 2024-10-05 03:49:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 335b9b4d-61b5-3774-9210-191416124958 | -8.3705 | -43.66001 | 2024-10-05 03:49:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 20aa9a8f-d6f6-3384-b0c3-6980e44ff0a4 | -8.37048 | -43.65834 | 2024-10-05 03:49:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4c01df4b-3295-304f-9d70-16649f385643 | -8.36687 | -43.65311 | 2024-10-05 03:49:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8e176c0e-7b4a-39c6-a982-9c96ba84335b | -8.76437 | -44.8195 | 2024-10-05 03:49:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 4f1b55ea-8d95-3bdb-8bb6-baad5ad441d8 | -8.76344 | -44.82474 | 2024-10-05 03:49:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 20.9 |
| e04fc048-be90-3e8f-b1ec-ea54c7227c54 | -8.7625 | -44.83002 | 2024-10-05 03:49:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 63a7cb9a-ba7c-3049-819f-a24eb800f869 | -8.75871 | -44.82388 | 2024-10-05 03:49:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 1b63f174-2c9e-31da-851b-edf4ec7c676d | -7.79055 | -43.10566 | 2024-10-05 03:49:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 378dd460-9f10-38f5-85b0-e8055a6a1c28 | -7.78985 | -43.10978 | 2024-10-05 03:49:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 67ed3688-3adf-300f-a71c-44d277110c81 | -7.7555 | -43.07855 | 2024-10-05 03:49:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2a63db94-f0c7-345b-b93d-247789cb81fb | -7.75122 | -43.07781 | 2024-10-05 03:49:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 812dd19e-3ab4-37d4-95a7-1e557ce33f73 | -7.74769 | -43.07275 | 2024-10-05 03:49:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 172bac82-bb2d-3348-a145-40be2a3f3a68 | -7.37522 | -35.22083 | 2024-10-05 03:49:00 | NOAA-21 | JURIPIRANGA | PARAÍBA | Brasil | 2507903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 24ceac27-0609-3c28-84d8-cc3fc5051cc9 | -7.56491 | -39.03817 | 2024-10-05 03:49:00 | NOAA-21 | PORTEIRAS | CEARÁ | Brasil | 2311108 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1b6f2e02-34c1-3a43-a2c9-a5266a104e91 | -7.3526 | -41.94946 | 2024-10-05 03:49:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a93a5446-cde4-3a3f-9c29-7f512b7161ea | -6.99705 | -39.49889 | 2024-10-05 03:49:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0d288a6e-95f5-393f-ab12-c417d4dd6a28 | -6.99595 | -39.49894 | 2024-10-05 03:49:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cbde23df-28c4-37a1-9ec8-04190e9b5c2f | -6.84356 | -41.68963 | 2024-10-05 03:49:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5705771c-7a57-3eb6-9eed-d6b1879f245d | -7.12532 | -42.61555 | 2024-10-05 03:49:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4b49b735-31f4-3af2-bbb5-55d56131a3bf | -7.12112 | -42.61491 | 2024-10-05 03:49:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 347f0d0b-100c-362a-8c6f-14de05d1e2b9 | -6.84677 | -42.82663 | 2024-10-05 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 5d3fe331-d804-3956-b8ba-88c8a50601c4 | -6.8461 | -42.83061 | 2024-10-05 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3bb44c70-b912-3292-b805-598d29bf1297 | -6.84317 | -42.82192 | 2024-10-05 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 1ff657d7-af6a-36ab-bc25-a289cb0ff2f5 | -6.8425 | -42.8259 | 2024-10-05 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4cfd2d13-f792-321f-9b47-ad0f0633aebf | -6.83958 | -42.8172 | 2024-10-05 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2c863729-1101-3be6-9ed8-c154e4ac5401 | -6.8389 | -42.82119 | 2024-10-05 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 02f06789-6d3a-33f1-80ad-72886ca558f2 | -6.83463 | -42.82049 | 2024-10-05 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 91c3601d-fd20-3e2a-9def-293d1bcb677c | -6.83103 | -42.81583 | 2024-10-05 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 12f778cb-b708-3b6b-9a8d-5eed81ce131e | -6.83036 | -42.81979 | 2024-10-05 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| d05887c7-9775-33da-b70f-3c983e2d296a | -6.49563 | -41.38173 | 2024-10-05 03:49:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1b6d7df3-775d-3fb8-9ead-2b07d36706c6 | -6.6836 | -43.5202 | 2024-10-05 03:49:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8961c883-0797-38a9-b484-f8b47e0e1ea0 | -6.65963 | -43.05463 | 2024-10-05 03:49:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae60b1d1-be90-3dfc-9479-83a670597a6f | -6.65891 | -43.05882 | 2024-10-05 03:49:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29f1db7f-2f90-3759-8101-adfe9197fdca | -6.65455 | -43.05809 | 2024-10-05 03:49:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a9c14d59-106c-37a8-905a-ab5da3ee39a6 | -6.6502 | -43.05735 | 2024-10-05 03:49:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b7546e43-c99b-335b-b77f-a4edf940cbc7 | -6.64948 | -43.06153 | 2024-10-05 03:49:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5a3321fe-3a68-3083-8477-a6865d779267 | -6.47409 | -43.42239 | 2024-10-05 03:49:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 35247cf4-7a8d-3d3b-99c3-5797f77dd189 | -6.47168 | -43.35673 | 2024-10-05 03:49:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 598a712e-16ca-39e3-b46f-24d1f81ae803 | -6.47087 | -43.36138 | 2024-10-05 03:49:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f16771ee-63a8-329b-9c13-17ad401f8fc3 | -6.47039 | -43.41719 | 2024-10-05 03:49:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6e698364-0e4e-3f7c-b1a9-451347694660 | -6.46798 | -43.35165 | 2024-10-05 03:49:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a0efe24-97e3-3751-954f-034d53b81909 | -6.29601 | -43.85187 | 2024-10-05 03:49:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 52b1aca8-b713-3cf4-b120-4e30fc7d9983 | -6.28555 | -43.44399 | 2024-10-05 03:49:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 81c423a9-c8f4-3382-a5bf-d256d51062f2 | -6.28552 | -43.25622 | 2024-10-05 03:49:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cbdba21c-b7b4-310f-b926-2d2f3b5efa88 | -6.28475 | -43.26069 | 2024-10-05 03:49:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c806396b-838e-3b25-86f7-7d4d1138d91d | -6.20552 | -43.2767 | 2024-10-05 03:49:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 616d972f-f9ed-3554-9151-1ff33838da0d | -6.20107 | -43.27594 | 2024-10-05 03:49:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d46cf8f-6163-341b-a815-a7b1fd3dfda9 | -14.03448 | -41.70309 | 2024-10-05 03:49:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d0da3e8b-fbe5-3484-b161-810b2eda95bc | -13.53627 | -42.02784 | 2024-10-05 03:49:00 | NOAA-21 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4bc4c6ae-6e45-37ec-804a-8cc6140ecd5a | -13.53551 | -42.03233 | 2024-10-05 03:49:00 | NOAA-21 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2da13be6-ecf8-33fe-b4bb-6d35a9347ebe | -13.53261 | -42.02712 | 2024-10-05 03:49:00 | NOAA-21 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a0ac1bff-6570-30f5-8233-56dabb1f3b5f | -13.45283 | -42.42752 | 2024-10-05 03:49:00 | NOAA-21 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d0d8db9b-963b-3262-a78a-0823832b52f5 | -13.16207 | -44.06718 | 2024-10-05 03:49:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11a4acdb-913a-3099-8e27-6d8b34ec4920 | -13.10759 | -46.33655 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4a03a424-4800-3a74-b26c-9041bea2ebbb | -13.1206 | -46.32118 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cd1edda6-52c9-3904-b9c2-3c71f43201f7 | -13.11934 | -46.32772 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 8a4b4771-b256-33d1-b503-6eedc161ebfe | -13.11768 | -46.3626 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 077aa3a5-ed6f-31fd-9e19-f9249949de06 | -13.11661 | -46.36821 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9556fe88-74e9-33f0-9b84-e33620cb059b | -13.11582 | -46.3199 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ec6a3e61-4378-3157-bbfe-639aa5d33b79 | -13.11554 | -46.37378 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2281029e-7d61-31e2-aece-5451776b3a44 | -13.11453 | -46.32658 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| f4e43645-fc11-3bd7-b732-9e83638dbcdf | -13.11336 | -46.33266 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 95bb6e5a-3fb9-3bed-85ed-223b8e66f49f | -13.11281 | -46.36171 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 160.1 |
| 14625964-ed9e-3867-b7a4-676ecfdba33b | -13.11222 | -46.32189 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 5d309ba0-85a2-3542-b808-a1ee7d56ef66 | -13.01511 | -44.76038 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5950ba6f-2736-37bf-8905-4689f240df4a | -13.01431 | -44.76474 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1aa23d8f-fe15-32ab-ac89-4be40d9ad739 | -11.67492 | -45.2567 | 2024-10-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c8b9abad-e6ac-31e3-8fa7-f23664951580 | -13.1075 | -46.32028 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 394b2009-7ffa-39c6-a91a-4d55922b96dc | -13.1069 | -46.36628 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 160.1 |
| 5ba46550-0092-38bd-a0e2-9f053823af17 | -13.10681 | -46.35123 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 25.3 |
| e9508ad0-7b9c-3f98-9d17-131867194ea9 | -13.1065 | -46.34219 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ee5bc424-1eff-323c-a8c4-6aa78cad98f1 | -12.88175 | -44.62388 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b06c59e1-e936-31d6-be0a-dd970e297b3e | -12.87741 | -44.62303 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5d135283-2ec0-3ea0-9a42-65f1753bfb82 | -12.87607 | -44.6244 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| da37e509-bb57-30bb-b9f9-39cf673eb3b8 | -12.86518 | -44.61628 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 24c7dacb-9b39-3f0b-9ece-8bf9542aeceb | -12.86379 | -44.61765 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e5e2cb5b-20d6-3767-9e73-e2f85a2c8677 | -12.71631 | -40.21405 | 2024-10-05 03:49:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 54d1f6ca-e006-3bb6-898e-ad6b7e6bace7 | -11.68784 | -40.58939 | 2024-10-05 03:49:00 | NOAA-21 | PIRITIBA | BAHIA | Brasil | 2924801 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ddea4954-c06f-3cdf-a3fc-116d0168ff27 | -12.07539 | -42.31359 | 2024-10-05 03:49:00 | NOAA-21 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9a801d27-9783-34f0-8aba-fec3e23e5da5 | -11.75889 | -42.93109 | 2024-10-05 03:49:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b2bb83aa-33ba-31ec-af37-1d6dd8e1ca06 | -11.75677 | -42.9295 | 2024-10-05 03:49:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 8b09fca7-b015-3411-871a-028503e5f4a6 | -11.75492 | -42.93037 | 2024-10-05 03:49:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 80e74c88-7916-3dbd-ac67-167eec9586f8 | -11.76123 | -44.64945 | 2024-10-05 03:49:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d06e88b-0649-3df8-9a0d-ca3dc4643bbd | -12.73358 | -43.48185 | 2024-10-05 03:49:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e48ff0c6-fd66-3e2c-99a9-4e67fe588d58 | -12.73017 | -43.47747 | 2024-10-05 03:49:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c0ffc7b8-b2d9-37be-8246-548fe2d0de96 | -12.35031 | -44.62427 | 2024-10-05 03:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README45.md)
