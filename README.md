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
| 1f8d9220-8127-323d-84da-2cf7c0e23c6b | -13.2289 | -61.7161 | 2026-09-08 00:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 125.6 |
| 96846b54-f2bb-3565-b2af-989e826fbaf1 | -4.5667 | -47.1855 | 2026-09-08 00:00:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 148.9 |
| 34998185-e70d-3a15-9f21-8bcf296d71dc | -13.2479 | -61.7148 | 2026-09-08 00:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 86.5 |
| b1c475f5-ad33-3270-8b07-498fae377462 | -3.5407 | -48.1673 | 2026-09-08 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 166.2 |
| b4270296-dc10-3ba0-a64c-e481b9da7608 | -1.4751 | -54.8356 | 2026-09-08 00:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 75a6925a-7bd5-30a3-9c98-fde13797b0c7 | -21.9721 | -56.0525 | 2026-09-08 00:00:00 | GOES-19 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 2bc116e4-b3a3-37ab-9128-55604c4cfd64 | -3.5591 | -48.1882 | 2026-09-08 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 236.7 |
| a46584e6-c310-3897-b18f-5b2108bc0dc8 | -10.8233 | -60.8019 | 2026-09-08 00:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 92f6bcca-c268-3030-a6c7-58253969f493 | -3.5406 | -48.1889 | 2026-09-08 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 295.1 |
| a039234c-5c41-31e3-ab7d-9ebf97e9c7e7 | -13.4264 | -43.8163 | 2026-09-08 00:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 56d8dab9-1f7a-3014-add7-438e60c16cf0 | -13.2099 | -61.7173 | 2026-09-08 00:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 2bce97f7-6a0c-3ea6-9930-1e043f749806 | -4.3587 | -47.7853 | 2026-09-08 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| ada55c3e-1c80-31ce-a82b-481ba995a1df | -11.3904 | -45.7412 | 2026-09-08 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.7 |
| c993ea59-9214-3924-8297-059802bead77 | -6.6357 | -59.4459 | 2026-09-08 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 58b3356f-3498-3c52-bbdf-e4a2ee1197a9 | -11.3713 | -45.7439 | 2026-09-08 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.5 |
| a9174a61-1e15-3639-978c-d3c59edc8c52 | -13.2287 | -61.7355 | 2026-09-08 00:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 36.8 |
| a16929f5-fa45-3ece-8a11-7a73256ca6bc | -6.7675 | -58.9583 | 2026-09-08 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 849f21c8-ded4-3c98-949e-405e0b7aeed9 | -4.5853 | -47.1846 | 2026-09-08 00:00:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 60.9 |
| b9816334-9431-3076-9f38-d72f026592ce | -6.786 | -58.9575 | 2026-09-08 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 579e7c34-5ec4-3943-b973-2bed062b1cca | -3.5592 | -48.1666 | 2026-09-08 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 148.5 |
| 5da8ca19-6e68-32cb-8b80-d09708fa3c02 | -14.91056 | -44.67792 | 2026-09-08 00:01:00 | TERRA_M-M | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 69425791-bfd6-38d0-bc1d-3a6755b85e34 | -18.69495 | -49.62713 | 2026-09-08 00:01:00 | TERRA_M-M | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| da61b974-1ff7-3d16-a96c-aa76d29e43c2 | -15.83463 | -56.61135 | 2026-09-08 00:01:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 079bcfa7-28ab-3d98-890a-f058acf8d8ee | -18.69625 | -49.63734 | 2026-09-08 00:01:00 | TERRA_M-M | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| c1e183da-00e6-3b47-b921-50c76678d6d6 | -18.77286 | -49.44481 | 2026-09-08 00:01:00 | TERRA_M-M | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 6bb7b6d6-d8b9-35a2-a033-531ab58fd47d | -21.97892 | -56.06004 | 2026-09-08 00:01:00 | TERRA_M-M | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 71f5e37a-e50a-3372-95e7-32813ab15655 | -21.97602 | -56.02704 | 2026-09-08 00:01:00 | TERRA_M-M | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 26b45d6b-442a-3dad-98d2-573e2e04d8b8 | -18.78203 | -49.44349 | 2026-09-08 00:01:00 | TERRA_M-M | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fa127a99-2a51-3e82-96ae-ec1d6cf13b28 | -20.49226 | -57.43343 | 2026-09-08 00:01:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 58.7 |
| 5b84440b-d2d7-3a98-bce6-36a3a77b24f6 | -18.77157 | -49.4348 | 2026-09-08 00:01:00 | TERRA_M-M | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 15.5 |
| ac32a510-f78b-3620-8635-065d1e7f18f8 | -16.13441 | -49.52192 | 2026-09-08 00:01:00 | TERRA_M-M | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0abd75df-02c4-368e-9f04-2f7ce47f3694 | -20.49789 | -57.42811 | 2026-09-08 00:01:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 69.0 |
| c9788e03-6ce2-31b7-b002-80f65c9088ee | -21.97575 | -56.05482 | 2026-09-08 00:01:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 3546b10a-9d97-3c1f-b887-8f0692d2a101 | -7.75409 | -49.54779 | 2026-09-08 00:03:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a95ba2b1-fc75-33d3-932e-705a5d9505bb | -11.33401 | -45.09533 | 2026-09-08 00:03:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 65810816-9135-33b4-b607-766a1b1cd5cd | -7.79914 | -49.20749 | 2026-09-08 00:03:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d29c3693-8f44-364d-8d4d-1261c7c6183a | -11.32333 | -45.09636 | 2026-09-08 00:03:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| afcbc6df-dcd7-3714-b295-6cdc18b2e132 | -13.44179 | -43.81858 | 2026-09-08 00:03:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 9ed6356f-3656-39fe-b524-969a17ea008d | -7.61213 | -47.29654 | 2026-09-08 00:03:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| ecc422dc-69be-3403-a539-2da56fd89d59 | -11.31068 | -45.08469 | 2026-09-08 00:03:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e533b7ae-9aa5-3701-b575-571d491c32b0 | -11.39087 | -45.74463 | 2026-09-08 00:03:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 55418572-2aa7-3eb8-8144-43a9e6ea935d | -11.31926 | -45.06986 | 2026-09-08 00:03:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a3534616-d209-31b5-97ca-cad36f051d13 | -7.7979 | -49.19852 | 2026-09-08 00:03:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| cd720126-329d-310c-8fa2-1805cc63c5ea | -7.36802 | -47.02097 | 2026-09-08 00:03:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 29.2 |
| c2eb3d7d-14fb-38c5-b369-f41ee79cb883 | -13.40191 | -44.15123 | 2026-09-08 00:03:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 613ea314-b0f6-3a30-83ea-eb2d9d786e42 | -8.77883 | -48.36654 | 2026-09-08 00:03:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e8bb1fea-40f7-383d-9b05-d89bc9070894 | -7.37624 | -47.00835 | 2026-09-08 00:03:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 2a9c2c76-6c5e-337a-acfe-14b982ffb290 | -10.24407 | -45.20491 | 2026-09-08 00:03:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 669cb694-8b47-3461-928d-6734e2e2e07a | -7.37786 | -47.01951 | 2026-09-08 00:03:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 33.5 |
| fd9b8a27-6775-34d0-8061-fb56899e4d90 | -11.3826 | -45.75809 | 2026-09-08 00:03:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| d3698685-adcc-3556-b9fe-73b9999bd98a | -11.3213 | -45.08316 | 2026-09-08 00:03:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 7394b76b-0d97-3291-aec4-8ad4f2814fe7 | -11.35031 | -45.7442 | 2026-09-08 00:03:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 8b9a0994-0b69-3eea-b5f1-d0f813df1edd | -10.25476 | -45.20316 | 2026-09-08 00:03:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a8e3e9c0-e884-3056-9ce9-1f02f97d5289 | -11.33205 | -45.36224 | 2026-09-08 00:03:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 2a4f4be3-49e4-3aa4-a7d1-4d0ee44862d2 | -8.36123 | -49.72501 | 2026-09-08 00:03:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| dcacbbac-0d45-3fae-8dc6-69a735f790e8 | -9.0889 | -47.81882 | 2026-09-08 00:03:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 30897950-95f3-3bab-9713-1631cedf2db0 | -11.34853 | -45.73222 | 2026-09-08 00:03:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| a19d0c6f-fed7-320a-83c0-5c942f27d32c | -13.43053 | -43.82032 | 2026-09-08 00:03:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 34c7c641-1299-3fe0-8227-f77dfefc1187 | -8.27795 | -46.37888 | 2026-09-08 00:03:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| d784706b-455e-3cf9-86e4-75aceaefc583 | -11.31272 | -45.09796 | 2026-09-08 00:03:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 587fa575-9b6e-3e56-ac3c-94f50979d30d | -11.37054 | -45.74123 | 2026-09-08 00:03:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 7956c2fc-19e3-3eaa-89d2-6a6b4cce6c94 | -11.38239 | -45.75153 | 2026-09-08 00:03:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 27a8e523-c2dd-3409-9875-df5ce1506e65 | -11.3723 | -45.75311 | 2026-09-08 00:03:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 67e64a9f-25a0-3564-938a-75a578aaf9e5 | -7.61059 | -47.2858 | 2026-09-08 00:03:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| d6efab7e-162c-32a2-843d-c36ad45e5ba6 | -7.36639 | -47.00977 | 2026-09-08 00:03:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 22a9812d-2a7b-328f-8368-96aa540cdf1a | -11.39269 | -45.75654 | 2026-09-08 00:03:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 2e6cc1f5-f9f0-3310-bf93-1e05e2b2d97b | -7.42678 | -49.37679 | 2026-09-08 00:05:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4254ac94-d834-3a5d-b9e2-8888a68870fc | -5.91603 | -52.49048 | 2026-09-08 00:05:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 96e16a95-b884-3e8d-8546-8e4d856d3516 | -4.48424 | -48.19461 | 2026-09-08 00:05:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ab68e613-cd39-3088-b1f6-18f2e0d1f02c | -6.64248 | -51.18079 | 2026-09-08 00:05:00 | TERRA_M-M | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 2a9c8446-eda5-3524-9eaf-5b32a066cf02 | -6.92142 | -44.94755 | 2026-09-08 00:05:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 0e65bf98-bfef-377a-9a96-7bf7bd8f08c3 | -3.55274 | -48.19677 | 2026-09-08 00:05:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 4f4d6740-06ec-3166-b45f-38b250b86824 | -3.69499 | -49.5318 | 2026-09-08 00:05:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| e520efb7-4f0e-33e9-9def-caa70a9c18be | -4.04676 | -50.87465 | 2026-09-08 00:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| fa6aec34-b941-320f-829b-a9149f62ea3c | -6.01411 | -45.80527 | 2026-09-08 00:05:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 7b09c61c-3a46-3f0d-b700-9dc19b9469cb | -6.7609 | -58.94913 | 2026-09-08 00:05:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 62e9e063-b572-3598-a341-466802287f29 | -6.61465 | -44.71869 | 2026-09-08 00:05:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 4f0dbc6e-2a8c-39e9-b4e1-710d7c721e34 | -6.057 | -57.80821 | 2026-09-08 00:05:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 34dfdf2e-3813-3825-bcb0-a1f9d9908156 | -3.75251 | -49.47985 | 2026-09-08 00:05:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 4ba264f6-4fb0-31d0-a45c-034c51e4a1be | -4.07654 | -48.95879 | 2026-09-08 00:05:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c9852dc9-44ed-3ea9-b27a-1686b79e5bbb | -6.64272 | -59.46206 | 2026-09-08 00:05:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 54a02c3e-3d9a-3c03-ace2-bb05c097d637 | -6.64127 | -51.17179 | 2026-09-08 00:05:00 | TERRA_M-M | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 149f3699-368e-3a5a-b9ea-4ce8fcc58618 | -4.03797 | -50.87587 | 2026-09-08 00:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| a2c4261d-2345-38d7-be0f-e74e76416cc1 | -6.0162 | -45.81961 | 2026-09-08 00:05:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| d29e5ccf-5235-35fc-ae56-006d47fd6239 | -4.83065 | -42.75603 | 2026-09-08 00:05:00 | TERRA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 17.7 |
| d52db535-79df-33c6-ae71-6c83c7548cc0 | -5.62843 | -44.24742 | 2026-09-08 00:05:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| a662c9b8-70e9-31e2-8dcd-a99a481b3217 | -4.34481 | -47.58207 | 2026-09-08 00:05:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 77548ab0-ff3a-3f0b-827d-69851ea976bf | -5.80308 | -49.97765 | 2026-09-08 00:05:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 28a1cd8f-b117-388a-8108-d5b6f8082ba8 | -5.93898 | -51.70423 | 2026-09-08 00:05:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| a97bd16b-5570-3c24-9dca-44a68b37fa65 | -4.07521 | -48.9492 | 2026-09-08 00:05:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 610d4c05-f26c-30cf-9457-08577aeda273 | -3.55126 | -48.18635 | 2026-09-08 00:05:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 469.1 |
| 44368faf-275e-3019-98cc-de8df1c16ad3 | -5.59502 | -45.37593 | 2026-09-08 00:05:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 6447d52e-4c2e-3a41-8c3b-70ee39afc428 | -4.3464 | -47.5933 | 2026-09-08 00:05:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 85c3145e-6e23-30e5-9926-4367897296d0 | -6.79186 | -58.9458 | 2026-09-08 00:05:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 574d7209-8a0a-3eff-8a36-128035a265f6 | -6.63855 | -59.4283 | 2026-09-08 00:05:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 468de09f-7f94-3992-a311-c74192deb90c | -7.06417 | -56.47696 | 2026-09-08 00:05:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| f78e86a9-4fd4-3e53-9f26-b3a01b3b7957 | -4.05554 | -50.87342 | 2026-09-08 00:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| c199c805-aa76-3b95-aafe-61731ce0a5b1 | -5.99433 | -57.7004 | 2026-09-08 00:05:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| fc4fc2a0-2031-3f83-a695-687ab7e9a48a | -6.05398 | -57.78424 | 2026-09-08 00:05:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 076ea2ec-88d8-3b0c-9b52-4121f760f147 | -5.49482 | -48.16895 | 2026-09-08 00:05:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 18.3 |


[Clique aqui para ver as próximas entradas](README2.md)
