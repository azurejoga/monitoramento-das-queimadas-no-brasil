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

## Dados Diários - Página 151

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ffb714a-8c89-331f-aa5b-17fceb7a8ae4 | -10.52143 | -47.28666 | 2026-10-07 16:01:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 39.3 |
| e41e25f8-30ea-39a6-b4a5-f26ecf618070 | -9.58055 | -46.20667 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 5e8670f4-df4b-3e65-8ac3-56d511a1229b | -14.75794 | -49.25544 | 2026-10-07 16:01:00 | NOAA-21 | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | 20.8 |
| ae7b8d71-d07d-384c-99b3-5f819df9b287 | -9.44775 | -45.81676 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| e7c7d24a-06d0-371b-bebc-181f392570d0 | -11.84473 | -43.53288 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| d5a2c8e0-9577-3e3b-8403-b8e05f5a072c | -10.30393 | -36.41113 | 2026-10-07 16:01:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| b58908f3-f92b-31b1-93dc-1ad1199453dd | -12.59308 | -47.21974 | 2026-10-07 16:01:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1739d349-d085-31b4-b73d-0f15a6d06627 | -7.67904 | -37.59959 | 2026-10-07 16:01:00 | NOAA-21 | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 083e9068-641d-38ee-94a3-19239be26bf3 | -10.70001 | -40.9169 | 2026-10-07 16:01:00 | NOAA-21 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 2cc3d18f-f6aa-3ec3-9237-662415812a13 | -8.80152 | -49.01135 | 2026-10-07 16:01:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| dfbf478f-075d-3345-9cf2-2a063e01af59 | -9.90201 | -44.8022 | 2026-10-07 16:01:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 62c05025-0b9a-30b8-b302-02e9278783c8 | -8.07443 | -35.78391 | 2026-10-07 16:01:00 | NOAA-21 | CUMARU | PERNAMBUCO | Brasil | 2604908 | 26 | 33 | nan | nan | nan | Caatinga | 4.0 |
| b9507a53-cdcb-3ec4-b2b0-0637f8ab62bd | -11.10707 | -47.58733 | 2026-10-07 16:01:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| fde07064-5ffc-3110-a9a8-9d91fe9ab556 | -9.87244 | -46.31353 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 7961301d-1c9a-358b-8b8c-cc431478dfb4 | -10.52191 | -47.29058 | 2026-10-07 16:01:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 39.3 |
| cbb209be-15b0-327a-8ef7-8a386e6dd8fc | -11.10759 | -47.59171 | 2026-10-07 16:01:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| bd5b94c9-7492-3ee5-892f-0acb198b3cbc | -11.08817 | -45.65073 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 449d5676-b1f9-3c01-8816-d29036bcb3c3 | -10.17506 | -46.71244 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| c305998d-6c98-37f2-b92f-9d9e35985d16 | -11.09606 | -45.67184 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| ed95543e-cd9f-352f-a787-dd05c08dcbe1 | -10.25127 | -44.63981 | 2026-10-07 16:01:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 17.7 |
| acf67158-6f21-3bc2-8c23-59bdbada2974 | -9.99463 | -46.01726 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 07884c5d-c2aa-30ff-8076-e938c8eb5d99 | -9.96104 | -43.49389 | 2026-10-07 16:01:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 544bb777-7fb1-3d88-8452-b15dba82774e | -11.09991 | -47.62682 | 2026-10-07 16:01:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 1babdcdb-438a-31e5-92ca-889b302bd283 | -9.96852 | -43.54903 | 2026-10-07 16:01:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 000cc46d-7897-32df-9906-fb713310b7c1 | -11.22444 | -45.27619 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a69e354a-96a8-3026-9cc0-95939117168c | -10.88913 | -46.66858 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b68b7f73-e589-3be6-911c-03db6840b52f | -9.39633 | -45.81843 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 9823428b-ab27-3bac-a282-38669b10708d | -12.83809 | -44.62879 | 2026-10-07 16:01:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 232ef7de-5e1f-3925-808d-7a9b3c7ef426 | -11.22516 | -45.28195 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| a864d941-9955-3406-b2a0-d5d06a7a2d17 | -11.84695 | -43.55043 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 7cd16a02-7541-3a9a-b1d0-2b147c204fdb | -10.10445 | -40.16694 | 2026-10-07 16:01:00 | NOAA-21 | JAGUARARI | BAHIA | Brasil | 2917706 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 58de171d-7ef7-3b0d-9f73-65571333e278 | -10.11502 | -36.44239 | 2026-10-07 16:01:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 5.4 |
| c22d340a-0205-3a65-9a2a-88e2716a869c | -11.64398 | -43.68103 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 169b6ba0-26a6-3ae3-af8b-2a9a95286f1d | -11.62248 | -43.66922 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.8 |
| c87691df-ea1b-395e-aee3-482e35a1f122 | -8.59307 | -45.6869 | 2026-10-07 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 555afe01-4dd5-31b1-81c7-3bf24e6ed56c | -11.60916 | -44.14415 | 2026-10-07 16:01:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 0269a004-39d7-30c4-af77-a45b08620031 | -10.8832 | -46.6657 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 26.6 |
| eae44d44-c2f1-37a4-881d-22dc5742ab40 | -11.81903 | -47.31481 | 2026-10-07 16:01:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 33.4 |
| f3046277-cfcb-3598-b2ff-d462a3ae65b9 | -12.16444 | -44.72056 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 6fb0a30b-7cd2-3f16-ae70-9d586b3d4415 | -11.8497 | -47.37474 | 2026-10-07 16:01:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 558a70ed-4782-37e7-9898-a5b523ff8149 | -9.42081 | -46.33598 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 19c807a0-fefc-3611-9b0e-1aaf002c3cdd | -9.1473 | -45.82143 | 2026-10-07 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| fface4ad-e0d8-3429-a081-8a481de53d6c | -8.96268 | -47.55963 | 2026-10-07 16:01:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d5a245cd-cff4-3e7b-9798-19b12b0c991c | -11.14099 | -46.15988 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.9 |
| e65ef0af-1dae-38cd-930e-12de6edf09d9 | -10.99961 | -45.4301 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b225936d-1c17-3a2f-b72d-0a56ccf4b155 | -9.87203 | -46.31027 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6ebabedc-b75a-3de1-8f69-eec9520b468b | -11.47376 | -43.39584 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 47fdd8b5-20c2-32a2-811c-eaf6d41ec455 | -12.13881 | -43.30766 | 2026-10-07 16:01:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 69bc31b2-f90b-3c3d-9cdc-20a8e8a79dee | -11.72888 | -43.42262 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| fb0fc2f5-0544-3d8e-8dfa-7552af519593 | -9.40563 | -45.88966 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ce69f8ff-d95f-3485-9ce6-7ef2640482e9 | -8.99983 | -45.94527 | 2026-10-07 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 53.3 |
| d1f41aa7-e3fb-32a7-a3fe-3ab55b65ac91 | -9.42562 | -46.33198 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a14c6a34-766c-3579-b46c-41d8ec563e91 | -12.21381 | -44.69666 | 2026-10-07 16:01:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 114ea257-ee35-3574-bd12-72694b00b188 | -8.79231 | -47.58036 | 2026-10-07 16:01:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 058e50ed-88b9-3d8f-af14-e5a31eae16c2 | -10.85093 | -42.8059 | 2026-10-07 16:01:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| da38fa19-e1a4-3d87-886f-22fdaa52ce23 | -11.05559 | -45.82175 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 3a21075d-ae42-395d-b134-4c29b6f9b439 | -9.91598 | -46.80027 | 2026-10-07 16:01:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| d9948161-b29b-3957-8a65-ef6b670549c9 | -12.26287 | -44.42096 | 2026-10-07 16:01:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 3019e0dc-caf7-3303-8f3b-c2d3e08bed2a | -11.6113 | -44.14755 | 2026-10-07 16:01:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 29.0 |
| b02bc588-b185-35e5-9cfa-0b9c6e251c1f | -12.21655 | -44.71901 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 25.6 |
| ae7e8b1a-78bd-3191-8852-c8d6b3c6b28d | -13.77962 | -42.67616 | 2026-10-07 16:01:00 | NOAA-21 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 2c27a727-cd16-3a79-acef-7e3ce6ae86f9 | -11.00538 | -45.43499 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a0b4f5c5-b45a-30d6-81c4-8aa8c3c14165 | -11.84737 | -43.53571 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 99a61c1f-4661-37e0-b74f-6f1b5deea9c9 | -11.82727 | -47.33483 | 2026-10-07 16:01:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| c26b7efc-f9ca-302e-817c-89d2ed39e4f2 | -13.73592 | -48.48105 | 2026-10-07 16:01:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6b73f1db-ebc8-340b-84c9-deabd7d148d4 | -12.16235 | -44.70404 | 2026-10-07 16:01:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 26.1 |
| cdc08e98-d59f-392a-97a6-afe17ddf35b6 | -11.84916 | -43.54907 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 405d1226-5575-39a3-bc20-003dfff87c01 | -12.73918 | -47.00178 | 2026-10-07 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b5aae17-3428-3ba0-9dca-39fcca0aa805 | -10.99802 | -45.41787 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| fef9b04e-bda3-3b23-9979-9adc8aba36dc | -9.03618 | -46.90836 | 2026-10-07 16:01:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| cee68a08-e073-39ba-acc8-638b053e2cc6 | -11.0871 | -47.61903 | 2026-10-07 16:01:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| ba4d3d04-0c39-36f5-bd2c-a86c0e8c68a7 | -8.76669 | -45.76679 | 2026-10-07 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ac8f632f-f405-34fa-b076-eddb67ad9719 | -11.0874 | -45.64457 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a7959302-7a8c-3d0d-bfb5-e7bb4ff01d20 | -9.56163 | -45.6779 | 2026-10-07 16:01:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0742be59-a3bc-30a2-9e12-ac3068fab1ce | -11.37454 | -43.25419 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d7c084a8-5744-3d55-9800-131e8c7755e6 | -9.41109 | -45.89175 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 328f0e77-0989-35f7-85ed-d43b04955189 | -13.44972 | -43.45098 | 2026-10-07 16:01:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 3456e8a2-3ac5-36ff-98a1-61f9399e1d14 | -11.62643 | -43.66436 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 30ba89fe-4eea-3a99-a9fe-f9bc3c0b8765 | -12.83068 | -44.44445 | 2026-10-07 16:01:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 7c301697-1638-3b9c-b983-d104e22f5eeb | -12.20961 | -44.70292 | 2026-10-07 16:01:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 24758826-2003-38d0-8583-87926aeff50b | -10.37825 | -46.25571 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c367d5e3-6092-3e1b-a2fe-7fa369426e1a | -11.37511 | -46.69577 | 2026-10-07 16:01:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 7ad356a9-c3b8-3007-9f97-4284f0598827 | -10.52094 | -47.28263 | 2026-10-07 16:01:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 2e088cf2-f752-3e6f-babc-b6e63564cf18 | -11.85202 | -43.55435 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 50cee62d-3693-3665-a927-55051025384a | -11.01124 | -45.44045 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 8985934e-54c8-3e38-b51d-38021786af19 | -11.23197 | -45.2548 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 46.0 |
| da2e86fc-c0c9-3368-a7a0-8bc70572918e | -11.14264 | -46.17328 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 121.0 |
| e0a5cd8b-2f61-3906-b369-e8ed12ecba59 | -11.84981 | -43.55387 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 246c48bc-ab19-3a87-8215-6d2ca8bfcbb9 | -10.88451 | -46.67632 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 825e651c-b66f-3e6d-96f8-db41b9f60d1e | -14.07801 | -43.77045 | 2026-10-07 16:01:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 0de230d2-5934-306b-a867-ab2f280dcc2a | -12.22418 | -44.7407 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 150.0 |
| 51cdb3f8-0805-304f-9ffa-f0c7ef15cf9f | -8.956 | -47.5524 | 2026-10-07 16:01:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e0430381-5e5d-3f62-b356-39b31ce24bc7 | -10.03595 | -45.5562 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3184ed15-d1c8-3564-a4c1-0369eec8d2d9 | -12.22618 | -44.73595 | 2026-10-07 16:01:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 062a18fa-52c1-3b72-929d-0096f6b4883f | -9.87287 | -46.3169 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| f0aedfc1-fdf2-3c06-957d-35d913606570 | -11.61446 | -44.14851 | 2026-10-07 16:01:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 6ab4d46e-f9f5-3256-b7da-828b6f9ba048 | -11.84021 | -43.55052 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 64a32994-ee83-34a2-ab6d-8497c6196a81 | -13.59197 | -43.17377 | 2026-10-07 16:01:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 66.5 |
| 0e14eca1-1916-3e83-84ab-07f258a61f77 | -10.88407 | -46.67275 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 9d12b701-9cbf-3977-af27-3a74d0d20a1d | -13.78519 | -47.2689 | 2026-10-07 16:01:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |


[Clique aqui para ver as próximas entradas](README152.md)
