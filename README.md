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
| 15cc1dea-92a8-3e82-8562-a2447a91659e | -3.2017 | -49.4636 | 2025-07-24 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| ab2b1071-84dc-3ad0-a19e-015200dc33bf | -3.1832 | -49.4642 | 2025-07-24 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 324.7 |
| 6147052c-7f4b-30fb-803c-b7e803232579 | -7.5444 | -44.4777 | 2025-07-24 00:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 38d84245-9033-3b16-a1dd-49b876aa139e | -7.2594 | -43.0881 | 2025-07-24 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 292.1 |
| 04bd14b7-f54e-3a2b-9ca6-9bb85e1b0c6d | -7.5256 | -44.4795 | 2025-07-24 00:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 104.3 |
| c5b6bb1c-51c9-34c7-b98d-3f17887d3337 | -3.2018 | -49.4423 | 2025-07-24 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| f731d45b-69e4-38c6-b4f1-3708d43dbcdf | -13.7169 | -45.6833 | 2025-07-24 00:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 50.5 |
| f05dd70b-0160-37a0-865d-1808f868ebf3 | -3.1648 | -49.4648 | 2025-07-24 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 245.7 |
| f3404673-dd34-3511-a0e3-8ce0a4bb222e | -7.4541 | -49.4018 | 2025-07-24 00:00:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 115.0 |
| d8422063-34ac-314e-9fad-48c7ffc41dc7 | -7.2408 | -43.0664 | 2025-07-24 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 121.5 |
| 880d4f4a-1caf-3d92-abb4-26a7221ae101 | -4.0567 | -42.5354 | 2025-07-24 00:00:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 93.1 |
| 204e58c4-ef67-3e0f-86ad-d2b462e03295 | -7.2597 | -43.0645 | 2025-07-24 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 295.5 |
| efbc8dc5-a783-3df8-8f47-b15c6773b231 | -3.1649 | -49.4435 | 2025-07-24 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 230.7 |
| a586a781-9493-3951-aa01-c26df78649f7 | -11.9516 | -58.7771 | 2025-07-24 00:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 4ed1fcfa-794f-3519-9b2d-3166708cb99b | -4.0756 | -42.5108 | 2025-07-24 00:00:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 70.6 |
| a406b353-0fd6-3922-84c1-d7476cb03fba | -13.698 | -45.6634 | 2025-07-24 00:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 43.5 |
| dbcb6874-33b6-32b2-979f-402ab26e3442 | -13.6975 | -45.6865 | 2025-07-24 00:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 58.8 |
| f318627a-3317-3cb7-89ba-3a4cc9dc030c | -7.4728 | -49.4004 | 2025-07-24 00:00:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| acdd7610-7249-3d88-8b2d-e9237d406251 | -11.2383 | -46.8699 | 2025-07-24 00:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 126.6 |
| ea193fe4-dbd4-334e-8f7f-e9a690209d31 | -7.5253 | -44.5025 | 2025-07-24 00:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 84.9 |
| c11e669d-595c-34e3-90eb-47d59ace31ad | -8.4816 | -49.5534 | 2025-07-24 00:00:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 4e484b6b-75a5-33b1-9584-bbac1776838b | -7.2405 | -43.0899 | 2025-07-24 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 115.1 |
| 0c8ab49a-f6e3-36ed-b818-2def79d364ad | -4.7842 | -45.3282 | 2025-07-24 00:00:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| f6a11184-ab00-3be2-9d07-f9f3e745a441 | -4.0569 | -42.5118 | 2025-07-24 00:00:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 174.8 |
| 7c2492a7-434f-31c5-895d-1f061bafb504 | -11.9518 | -58.7574 | 2025-07-24 00:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 5dabd846-cc29-3731-a4c5-4a8e8e47bf4e | -22.2596 | -49.5816 | 2025-07-24 00:00:00 | GOES-19 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 57.7 |
| 12d8ceb3-b1e5-36b5-8dc4-57f8f5a0704f | -11.2574 | -46.8674 | 2025-07-24 00:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 159.3 |
| b058cf85-ae18-3933-9c98-52e2f15dccbe | -3.1833 | -49.4429 | 2025-07-24 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 305.5 |
| 8d9bf290-194a-3415-9f62-cedd198f7a70 | -7.5441 | -44.5007 | 2025-07-24 00:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 0e5d416b-cf4d-38c9-9a29-5949f03f91da | -12.25134 | -44.79609 | 2025-07-24 00:05:00 | TERRA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 3cdcc8bc-e733-3c2b-bf96-7dfc3c9e8a2c | -13.70894 | -45.66098 | 2025-07-24 00:05:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 14924bc9-a9bb-3541-be8b-f478444e9bbe | -13.71099 | -45.67933 | 2025-07-24 00:05:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 264058b5-7bcd-3722-902e-619c1f8c36cf | -12.24991 | -44.78697 | 2025-07-24 00:05:00 | TERRA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 98918005-31e8-35bf-9cbb-60157e56dce8 | -21.93554 | -48.01093 | 2025-07-24 00:05:00 | TERRA_M-M | IBATÉ | SÃO PAULO | Brasil | 3519303 | 35 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 9d3440de-6a73-30ab-bd79-eb332d909a8d | -13.71006 | -45.70451 | 2025-07-24 00:05:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 2d87d9ab-dcf2-3524-bdd1-b2986e574676 | -13.64562 | -45.71832 | 2025-07-24 00:05:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 0fdec95c-68d0-3bd2-8f65-2556d3d181f8 | -12.41905 | -43.49084 | 2025-07-24 00:05:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f051d903-6e20-3132-bb25-9e448e95e0c2 | -21.92523 | -48.00537 | 2025-07-24 00:05:00 | TERRA_M-M | IBATÉ | SÃO PAULO | Brasil | 3519303 | 35 | 33 | nan | nan | nan | Cerrado | 66.6 |
| b1c754b7-353c-3ce2-8b4f-18fdc7161b60 | -13.71305 | -45.69777 | 2025-07-24 00:05:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 5935683b-f7ac-3ad7-9c76-ba77ce1eaca9 | -13.70786 | -45.68609 | 2025-07-24 00:05:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| ed352161-b9d3-3aa4-b1e4-0f8f46108f12 | -13.54175 | -44.5022 | 2025-07-24 00:05:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a3cf3c78-c8b2-3343-bc78-0b9037c662b5 | -13.65052 | -45.73085 | 2025-07-24 00:05:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 8e7aee2c-3e05-3693-aa78-bb3cee49f3a6 | -18.04879 | -42.87223 | 2025-07-24 00:05:00 | TERRA_M-M | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| d3f05b08-4de0-3848-a097-21350c3bb7b1 | -14.79256 | -42.4473 | 2025-07-24 00:05:00 | TERRA_M-M | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 2ecff2a0-7b58-35ff-a6d5-d4a517b8333d | -18.0473 | -42.85923 | 2025-07-24 00:05:00 | TERRA_M-M | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.1 |
| 161a84f5-7dee-34d0-bebd-b856702681a0 | -12.42319 | -45.3746 | 2025-07-24 00:05:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 56.1 |
| c82baca5-6178-3d23-a7ed-4e9ed77aa529 | -12.24955 | -44.78109 | 2025-07-24 00:05:00 | TERRA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 51.2 |
| bad87ef5-79ad-31ae-8776-98cdf9f5a41f | -18.84718 | -47.95689 | 2025-07-24 00:05:00 | TERRA_M-M | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 55.4 |
| 57d0fa17-9506-3a47-9888-3a3d8c23937f | -14.79362 | -42.44077 | 2025-07-24 00:05:00 | TERRA_M-M | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 0136445f-ff86-3b62-9d74-f72ec50cb3b5 | -18.85354 | -47.96345 | 2025-07-24 00:05:00 | TERRA_M-M | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 89.0 |
| cc383802-5a2c-3650-9039-83f5966bb197 | -12.42514 | -45.39114 | 2025-07-24 00:05:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 08c9f116-0b2a-3ae4-8135-b958aa9228f4 | -12.24801 | -44.77206 | 2025-07-24 00:05:00 | TERRA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| c2a4cc9b-5e08-3ff8-92c9-ff5a356839b4 | -13.70568 | -45.66774 | 2025-07-24 00:05:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 05baebb9-beb8-3d17-bcac-4ebbf8b65e22 | -18.05301 | -42.86384 | 2025-07-24 00:05:00 | TERRA_M-M | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 38.7 |
| e4d510f0-7aaf-3072-8db5-d09ee1d9288b | -7.53003 | -44.48285 | 2025-07-24 00:07:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 44e25cc4-c04d-3088-9f7a-3c36ee6e0d4a | -4.1767 | -42.02638 | 2025-07-24 00:07:00 | TERRA_M-M | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| c4c3aa71-f258-3ecc-ac48-d6f3f0c9a453 | -6.61448 | -42.4152 | 2025-07-24 00:07:00 | TERRA_M-M | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 062f1513-f200-3eb9-8c64-4a882e541d66 | -11.46826 | -48.17093 | 2025-07-24 00:07:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 28.2 |
| e3c1b0c4-0d78-30a9-9056-bf1d6f55a663 | -7.25476 | -43.07606 | 2025-07-24 00:07:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 463.5 |
| 0204f14f-0fef-345c-a683-65ad52db195f | -10.62319 | -45.22726 | 2025-07-24 00:07:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 24.9 |
| c3f0085e-fcaa-39ce-b769-4d01332eeaa1 | -6.60618 | -42.42232 | 2025-07-24 00:07:00 | TERRA_M-M | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| ea157df7-225e-3048-bb16-7447ecae32c1 | -4.77764 | -45.33413 | 2025-07-24 00:07:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 43ecce94-8d18-34c5-9e83-e505c8b50e77 | -9.20505 | -41.0276 | 2025-07-24 00:07:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| f408c543-709e-3533-b9e4-487738ff60c4 | -7.46334 | -49.40183 | 2025-07-24 00:07:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 246.6 |
| 91aca6d1-09cb-30d2-b3ae-41f98d58d70e | -10.7137 | -48.85381 | 2025-07-24 00:07:00 | TERRA_M-M | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 3a17d89a-5f14-3ca4-b803-ad23d9a47575 | -9.32924 | -44.85019 | 2025-07-24 00:07:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| cc67c622-09a0-3613-9f81-1f65e79545d6 | -7.24645 | -43.06305 | 2025-07-24 00:07:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 04bf1cad-e0b7-3311-87bd-44c17af28461 | -11.99748 | -45.14748 | 2025-07-24 00:07:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| fd8da818-51db-3c7d-9422-1c2868dc5553 | -6.96537 | -44.37469 | 2025-07-24 00:07:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| e012bbbc-f7c9-35df-b19b-2e1ab07a8c68 | -11.81162 | -44.27555 | 2025-07-24 00:07:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f9f951d8-4a97-3638-adf8-ac732b795de5 | -7.26539 | -43.08466 | 2025-07-24 00:07:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 36.7 |
| a6bff71c-2101-30b3-9ee2-dd9fcc1e33d0 | -4.05228 | -42.52719 | 2025-07-24 00:07:00 | TERRA_M-M | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 29.7 |
| fcdc7e0e-2a5b-3b87-82c1-7f89fbc97145 | -9.58533 | -46.33339 | 2025-07-24 00:07:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 0ac2e6ff-7ee5-393f-8e75-82d17810f6e9 | -7.89427 | -45.55527 | 2025-07-24 00:07:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| de356280-275a-356d-9ea8-b6211c474a9d | -8.04139 | -47.65753 | 2025-07-24 00:07:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 5d7d7dc0-af47-3f90-8cde-d9f14f899447 | -7.23983 | -43.08406 | 2025-07-24 00:07:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 7a3e799f-411c-3e90-aaf4-3cb17e7d43b6 | -6.63246 | -43.09424 | 2025-07-24 00:07:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d99ff317-3aee-39a1-a66b-65163482fc45 | -5.91215 | -43.46947 | 2025-07-24 00:07:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 873ef366-f563-3208-9e53-d48adcaf7785 | -7.53156 | -44.49479 | 2025-07-24 00:07:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 171.3 |
| a21c1e69-cbc4-38bb-96d9-74e24ba5228d | -10.6251 | -45.24237 | 2025-07-24 00:07:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 9d82f9b1-1690-3d54-8440-e562dba13b1e | -6.96605 | -44.37992 | 2025-07-24 00:07:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| e7384e3b-5618-3d24-a08f-81728f7df1b4 | -4.80848 | -43.21334 | 2025-07-24 00:07:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 85bc8742-9896-3afa-b1b4-0a43c54f7350 | -8.93036 | -47.35768 | 2025-07-24 00:07:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| f8779ef2-0414-385a-8b65-89f713330650 | -11.74089 | -48.17577 | 2025-07-24 00:07:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 2014c7ca-09d4-3ca3-a0bd-1bae93d6b4f4 | -8.47916 | -49.54122 | 2025-07-24 00:07:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| d0a62853-0345-3a06-98c4-fa8583273370 | -4.04983 | -42.50925 | 2025-07-24 00:07:00 | TERRA_M-M | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 43.0 |
| 782b0642-25f8-3071-bca6-a9f6f536b31d | -11.25575 | -46.86923 | 2025-07-24 00:07:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 170.8 |
| 2cb07921-2fc9-36d7-b4d0-84c5fdbdba28 | -7.94441 | -46.28961 | 2025-07-24 00:07:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 34cfddef-c5af-36c2-8e89-1b1ea92f8218 | -11.74382 | -48.20236 | 2025-07-24 00:07:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 488b425a-8dcd-38a4-a3bb-89d1a2bbb99a | -4.05997 | -42.51697 | 2025-07-24 00:07:00 | TERRA_M-M | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 233.7 |
| c32afa4d-86d4-3946-9e9c-2dc793e1beda | -7.24779 | -43.07287 | 2025-07-24 00:07:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 144.6 |
| 58724fc5-4a25-3ec1-bf36-e9d096cf6bd9 | -6.26649 | -45.27589 | 2025-07-24 00:07:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 804f9002-24e4-3aa4-9826-fe5e807d4d1b | -5.67833 | -43.6676 | 2025-07-24 00:07:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 629c96fd-acd5-3ee6-8809-b20533006924 | -7.25607 | -43.08596 | 2025-07-24 00:07:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.3 |
| 5915143e-9ddc-3a2c-b6aa-584a2b4f1b55 | -5.67968 | -43.67776 | 2025-07-24 00:07:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 705fc2d4-886b-3c82-8140-63a80935c509 | -5.31577 | -45.23758 | 2025-07-24 00:07:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c530fe84-d545-3594-b8e7-2f49f3c1462d | -7.25346 | -43.06623 | 2025-07-24 00:07:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 125.9 |
| db2d8e41-1d06-3890-a6a2-3579895762d7 | -5.72873 | -44.51592 | 2025-07-24 00:07:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 2ae2ba66-48c9-3108-b2bb-81acbcd17ee2 | -6.26002 | -45.26892 | 2025-07-24 00:07:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| d4fc104e-1e9d-3314-8db7-b6baa5330956 | -4.51556 | -42.08653 | 2025-07-24 00:07:00 | TERRA_M-M | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |


[Clique aqui para ver as próximas entradas](README2.md)
