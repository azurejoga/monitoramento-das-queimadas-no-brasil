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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0644053-e505-3feb-85b1-c75322f58e47 | -12.8552 | -44.3389 | 2026-06-23 08:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 72fde6d1-8d4e-3c69-aed5-de5a1814cf69 | -12.8548 | -44.3625 | 2026-06-23 08:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 062d7874-ddc5-3ef4-9761-afb441cdbf0c | -12.8741 | -44.3593 | 2026-06-23 08:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 48.5 |
| b0893104-8666-310f-a52f-ed08918a5c04 | -12.8552 | -44.3389 | 2026-06-23 08:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 66.7 |
| ac404819-c08d-3cc4-b453-80b265fd7f16 | -12.8548 | -44.3625 | 2026-06-23 08:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 116.2 |
| eda96fb9-4726-3cdf-8580-032c04f7f58c | -12.8552 | -44.3389 | 2026-06-23 08:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 9ccde5ad-1827-35f2-a1e2-d7618f7e8922 | -12.8548 | -44.3625 | 2026-06-23 08:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 3b6c4b0d-19ca-35e3-92ec-4920f7c4cc07 | -12.8741 | -44.3593 | 2026-06-23 08:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.6 |
| d9d9a8df-0a1c-31e7-9b89-0f7fc921731f | -12.8741 | -44.3593 | 2026-06-23 08:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 07ffcdf0-f044-3064-b70d-1d74dc65c59d | -12.8552 | -44.3389 | 2026-06-23 08:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 2ec5f320-6c19-396a-9a74-aa0c73b0ebb7 | -12.8548 | -44.3625 | 2026-06-23 08:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 4f4524d4-fd45-37e0-8821-01ceec7f6870 | -12.8548 | -44.3625 | 2026-06-23 09:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 112.8 |
| a48add28-9f5e-3ce6-b3fe-e5d5678504fe | -12.8548 | -44.3625 | 2026-06-23 10:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 12b9b3d7-b8ae-3806-b94c-7f2db00a3449 | -12.8548 | -44.3625 | 2026-06-23 10:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 55873fc4-13aa-3acb-aa8b-876345f0a7a6 | -12.8548 | -44.3625 | 2026-06-23 10:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 8e9d2e10-f0f6-39d4-868a-612cda8f62be | -12.8548 | -44.3625 | 2026-06-23 11:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 186bc3e8-6af8-3356-b087-e80c128ea896 | -7.72162 | -44.56633 | 2026-06-23 11:30:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 06031ff6-eb7b-311e-b65e-32b723ed6f08 | -5.94483 | -43.46089 | 2026-06-23 11:30:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0294e86b-bae6-3c58-bb1e-944b0012d340 | -5.3321 | -41.69855 | 2026-06-23 11:30:00 | TERRA_M-M | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| fbcd2bb3-89b1-3a06-968b-23e469efc9ac | -8.41005 | -39.77868 | 2026-06-23 11:30:00 | TERRA_M-M | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 3.9 |
| ed97a579-c1ce-361f-a10a-ea3c08a44deb | -9.06201 | -44.78435 | 2026-06-23 11:30:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 50cdafea-cd75-3d1e-a1f3-b69cdc1b2d5a | -10.63013 | -44.85648 | 2026-06-23 11:30:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2696467f-5227-3e49-9a65-68356f41f09d | -11.91557 | -43.40602 | 2026-06-23 11:30:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| a364ad03-7525-3d45-82a0-fa42c92c88ee | -11.29892 | -43.32767 | 2026-06-23 11:30:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 8b49083b-c7dd-3b1d-8639-5d8f679b38b0 | -7.49893 | -44.0571 | 2026-06-23 11:30:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 18a54f85-cea9-37af-9107-b5e081ae1728 | -6.51147 | -42.22823 | 2026-06-23 11:30:00 | TERRA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 88cc4dae-f065-36b8-9513-854238a53d22 | -11.94157 | -40.62824 | 2026-06-23 11:30:00 | TERRA_M-M | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 7ce3c86a-7e3f-3a26-91fc-29c343b4000d | -11.62848 | -45.18612 | 2026-06-23 11:30:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 8c1f20be-5413-3e86-ba9d-38818eea2200 | -5.94333 | -43.47126 | 2026-06-23 11:30:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 265924ce-fd70-3e71-95a5-2815c28206d2 | -7.0046 | -42.8954 | 2026-06-23 11:30:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 06c146e9-36e9-3f21-a4ec-7ca585e24801 | -5.30987 | -43.05613 | 2026-06-23 11:30:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 392b572f-1840-33e7-8cc4-ddd5bc0166e0 | -8.04669 | -44.1639 | 2026-06-23 11:30:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| d24692bd-a532-3fc3-8e2e-d0cc2abc877d | -3.86538 | -42.96693 | 2026-06-23 11:30:00 | TERRA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| ef086e5d-7f88-31ba-a7b9-6ffb3bde67b7 | -6.99548 | -42.89408 | 2026-06-23 11:30:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 42.2 |
| c058b5cb-33fb-3110-8647-9c752aa9dec8 | -6.31425 | -44.65306 | 2026-06-23 11:30:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 5fe20081-3f3b-3ef8-9196-6f1110f8195c | -8.79209 | -44.81306 | 2026-06-23 11:30:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ed5de2ea-2d36-3266-a89f-43c807c4228e | -7.39649 | -41.21576 | 2026-06-23 11:30:00 | TERRA_M-M | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 5442f91e-4085-3a0a-8e0a-0812e573306d | -5.79787 | -43.636 | 2026-06-23 11:30:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 87e8071d-e54b-30f4-b1dc-d23628dfc7ff | -8.79217 | -44.80655 | 2026-06-23 11:30:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| dcb70115-a494-3614-afe6-201743ae5b21 | -6.36733 | -43.59447 | 2026-06-23 11:30:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 547c10bd-35fb-3df8-8241-0acac75f13fe | -5.79942 | -43.62544 | 2026-06-23 11:30:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 15d4f308-1af6-3518-8fc8-394a5e422f38 | -8.31565 | -45.38723 | 2026-06-23 11:30:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d6935190-728a-3e90-accf-bb85116ae87c | -6.99688 | -42.88459 | 2026-06-23 11:30:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| c7198384-cdc5-3f0d-9635-2590a618ea77 | -10.63369 | -44.85241 | 2026-06-23 11:30:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| c1c71ac5-0af9-3484-91a9-46dbdaa6404e | -11.48449 | -46.68989 | 2026-06-23 11:30:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 732ea867-2768-3615-a50d-374e608bece3 | -6.31601 | -44.64108 | 2026-06-23 11:30:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| e1043607-add8-3e1b-aea7-96290b21e397 | -10.63177 | -44.84554 | 2026-06-23 11:30:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 9cd5c9e9-09ca-31a6-b10e-89c029fe44b4 | -7.39524 | -41.22456 | 2026-06-23 11:30:00 | TERRA_M-M | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| ce280cda-cf95-30aa-b2b8-0d33aec81d1c | -11.90662 | -43.40469 | 2026-06-23 11:30:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 84e204ae-84b2-3dca-ba02-8a25b98d7f73 | -9.67807 | -47.01994 | 2026-06-23 11:30:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 3e157f9d-8bfd-3ad6-bb91-36dd255ecd73 | -5.82116 | -45.05694 | 2026-06-23 11:30:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 37501e86-deb0-33f3-aa62-2e25cc491ecf | -6.51282 | -42.21903 | 2026-06-23 11:30:00 | TERRA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 4e69db54-8bc9-33cc-b99f-edb14475647f | -19.00606 | -39.93892 | 2026-06-23 11:32:00 | TERRA_M-M | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 3f87777d-84c6-3b50-b9b2-07098e4051b3 | -16.03183 | -43.41607 | 2026-06-23 11:32:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 153.2 |
| f0a6cb0d-db53-3016-a638-57b960bc92ab | -17.60123 | -44.61047 | 2026-06-23 11:32:00 | TERRA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e6d5f1ed-b377-338d-99f1-386a43a01aff | -12.8643 | -44.35316 | 2026-06-23 11:32:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 41.1 |
| d4591c33-8539-3db6-9dbc-c84a1b7f16d8 | -13.47968 | -42.09607 | 2026-06-23 11:32:00 | TERRA_M-M | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| d9fe3522-4f00-37d1-964d-29ad4228d8fd | -12.86281 | -44.36301 | 2026-06-23 11:32:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 9afc9330-633a-3433-a596-13eb887aff22 | -12.85511 | -44.35175 | 2026-06-23 11:32:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 74.8 |
| b752e754-e466-35f3-87d6-b0878b7c887d | -12.872 | -44.36443 | 2026-06-23 11:32:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| f999e61a-7439-3e5c-a1a9-ee2c7c2a89aa | -12.85362 | -44.3616 | 2026-06-23 11:32:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 92.5 |
| cd41a4f0-e171-344b-ac18-0f2883b37e78 | -16.88302 | -43.1283 | 2026-06-23 11:32:00 | TERRA_M-M | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 31e05a69-d2c5-34cd-8a5a-8fed9a278e0f | -17.50179 | -44.9018 | 2026-06-23 11:32:00 | TERRA_M-M | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0ae8700a-7f0e-3cdf-8900-6f7d7672943c | -12.87348 | -44.35459 | 2026-06-23 11:32:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 9497f57c-3a5c-36f8-b1a4-1b8523a902e7 | -17.50033 | -44.91148 | 2026-06-23 11:32:00 | TERRA_M-M | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3b8644b8-d7ba-3747-97cb-ff5407681909 | -20.81407 | -42.75797 | 2026-06-23 11:32:00 | TERRA_M-M | CAJURI | MINAS GERAIS | Brasil | 3110202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 67bc6cf3-ee06-399c-a157-8466c8fe14e4 | -14.21531 | -43.78136 | 2026-06-23 11:32:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 27.1 |
| b16339cf-9323-3925-b3f5-4df7fa5db9f1 | -16.03051 | -43.42519 | 2026-06-23 11:32:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 78f8e574-8771-3b8f-8b20-0013eafd5277 | -23.02181 | -46.15 | 2026-06-23 11:34:00 | TERRA_M-M | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| 8dcdde9a-c5e0-3608-9d67-b20199c4a58b | -12.8548 | -44.3625 | 2026-06-23 11:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 66e9a1f8-ca2d-329e-9907-0d903bfd72b5 | -12.8548 | -44.3625 | 2026-06-23 11:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 195ff19a-0608-33a2-a296-f66727c0fbdb | -12.8548 | -44.3625 | 2026-06-23 12:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 120.7 |
| a28a5a54-f2e0-314e-b267-a209fe3eb743 | -12.8548 | -44.3625 | 2026-06-23 12:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 5bc3399e-c696-313f-a877-cc9734480771 | -11.9108 | -43.4081 | 2026-06-23 12:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 178.9 |
| c76d356f-f867-3158-8f02-d9aaa5a7c195 | -12.8548 | -44.3625 | 2026-06-23 12:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 889e8186-f0ae-3abe-9e74-391b38da4768 | -11.9108 | -43.4081 | 2026-06-23 12:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 141.9 |
| 5c44dff9-9029-3e83-8820-7ed6ba5cd700 | -12.8548 | -44.3625 | 2026-06-23 12:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 4d424fa6-0e09-38bf-be7a-bbf4c8b457db | -11.9108 | -43.4081 | 2026-06-23 12:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 4812d60f-5241-3df2-8a1e-4441cc152b50 | -12.8548 | -44.3625 | 2026-06-23 12:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 65f056fb-571c-3241-96dc-bae07dfc7026 | -12.8552 | -44.3389 | 2026-06-23 12:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 82.5 |
| d479b080-b33b-32d7-97a9-5e2f90895394 | -11.9108 | -43.4081 | 2026-06-23 12:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 33f7c007-f1ee-32ab-ac13-2bfa16ebeeca | -11.9108 | -43.4081 | 2026-06-23 12:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 120.8 |
| aba9fe15-e022-349f-a1b0-be9df45d76ba | -12.7949 | -44.4661 | 2026-06-23 12:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 4952dcc2-a245-3208-825d-993d9a26b2ee | -12.8552 | -44.3389 | 2026-06-23 12:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 86.4 |
| b252631d-545d-3d34-b956-e0f1f80a23bb | -11.4892 | -46.6795 | 2026-06-23 12:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| b1d7025f-ad53-3796-8d96-d63a0df691ba | -12.8548 | -44.3625 | 2026-06-23 12:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 57b0fc39-fc83-379e-ae0b-eb7128b02b02 | -12.8741 | -44.3593 | 2026-06-23 13:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 0685a3f0-b3a2-3e78-8c8e-06be1008e0df | -12.7949 | -44.4661 | 2026-06-23 13:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 370.7 |
| 1f3da591-be1c-3559-893a-078e247eca12 | -12.8548 | -44.3625 | 2026-06-23 13:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 131.3 |
| fddf620a-e701-3f3a-b413-9a710f6c45c1 | -11.9108 | -43.4081 | 2026-06-23 13:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 43b1ab95-2587-3081-b6f8-27ce39376f77 | -11.2537 | -57.89108 | 2026-06-23 13:08:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| e55a6365-1d6e-3aae-a680-d2ac3216fc76 | -12.54819 | -57.18843 | 2026-06-23 13:08:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| c712553f-7401-3cbe-88a8-3a9d27a1dc0a | -11.9108 | -43.4081 | 2026-06-23 13:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 997349f3-b4d4-3a17-a025-e6f098a4019f | -12.8736 | -44.3828 | 2026-06-23 13:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 0ae115ce-150e-3b8a-ae99-3b001c0ff605 | -12.8741 | -44.3593 | 2026-06-23 13:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 189.2 |
| 200aa053-4ee2-39fa-a445-f72bc0e55bfb | -12.8548 | -44.3625 | 2026-06-23 13:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 141.7 |
| cef6435c-6d1e-3ae3-8b62-3095d312a208 | -12.7949 | -44.4661 | 2026-06-23 13:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 391.7 |
| f533877f-4a4c-3352-99b5-4196b66389f3 | -12.8741 | -44.3593 | 2026-06-23 13:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 217.8 |
| cc7b0e93-66d5-30a7-8db3-baf730602f9e | -11.4892 | -46.6795 | 2026-06-23 13:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 042a7cc9-17f1-3c33-ae57-40a9c8a6c028 | -12.8548 | -44.3625 | 2026-06-23 13:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 172.9 |


[Clique aqui para ver as próximas entradas](README19.md)
