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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e76883ad-4777-3348-97b6-abc32cd76d11 | -5.71289 | -42.67172 | 2025-09-29 04:06:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 67f841a9-c746-3bba-88aa-b5c5c0119670 | -5.71706 | -42.86148 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e7449554-b4b7-3040-9ae9-9e5fdcc48076 | -6.11928 | -43.47777 | 2025-09-29 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7a7f6b42-e901-3c20-af45-0b562e4f85a8 | -7.18957 | -41.69984 | 2025-09-29 04:06:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4b512fc9-e59e-3b8a-80f7-3524b121589d | -4.70918 | -41.97884 | 2025-09-29 04:06:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f5071b2e-1a3f-37cf-a893-d1c35469d255 | -8.29797 | -45.49305 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 05696b7b-3441-365c-8306-904e1609688b | -6.83469 | -44.08752 | 2025-09-29 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5230aeb7-ac6a-3e38-9509-932b3c96920d | -5.6968 | -42.62157 | 2025-09-29 04:06:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9f27fed8-e730-3985-874e-7b97fdde5081 | -7.51404 | -44.30125 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3363d684-efe1-3012-81d6-753c9412538a | -8.1609 | -46.39729 | 2025-09-29 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8310cdaf-fc92-32f0-9b2c-7e5a5509e122 | -5.90293 | -42.92831 | 2025-09-29 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6f5acd2e-fa3d-3d4f-bcfd-1221380dff1b | -6.14397 | -43.47804 | 2025-09-29 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| acc2eb54-808d-3985-ac88-5d145b74a1a0 | -4.14355 | -40.01314 | 2025-09-29 04:06:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f70cc05f-6d1d-39b9-b680-c37d2348f889 | -5.89408 | -45.88203 | 2025-09-29 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be36b71d-8e92-3c9c-ad94-98aee76c383a | -5.6449 | -39.31148 | 2025-09-29 04:06:00 | NOAA-20 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6f37bc9f-e3bb-3655-ad5f-1ce9b1f86bc7 | -3.49824 | -52.46793 | 2025-09-29 04:06:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9f447cc-564e-36fa-8344-7b61dd76f3bc | -5.9502 | -46.40611 | 2025-09-29 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1dfea8d3-f5cc-33f1-8c9e-ec11f441fab9 | -5.82637 | -42.79343 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2c80a998-3970-3023-9f4f-ad9897b09b6a | -5.28204 | -43.14784 | 2025-09-29 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fe8ff1de-9758-342e-a8e8-642755e49f81 | -6.44944 | -44.03047 | 2025-09-29 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 356cc2cd-b098-35d0-b497-55bd35581b6d | -3.61714 | -42.77075 | 2025-09-29 04:06:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 972a2567-55cb-3f56-abba-ed5626dcde40 | -2.58211 | -48.41181 | 2025-09-29 04:06:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 84840d92-3281-3783-b389-13ef648154ca | -5.38519 | -42.30259 | 2025-09-29 04:06:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a44b73ed-6adb-3b7f-9fda-f9ce25e8b5d6 | -7.7495 | -46.9996 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 76508bf3-57ce-3e00-bd9d-aaec0b60ae95 | -4.45661 | -40.98045 | 2025-09-29 04:06:00 | NOAA-20 | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9a840c74-b5e2-3a7e-b701-8f3e8c146b41 | -7.22145 | -47.86967 | 2025-09-29 04:06:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d0292db-54ed-346f-b048-d6e5447151aa | -5.17577 | -41.24556 | 2025-09-29 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ca41125f-bb11-3bc8-afb3-5ee9f8c3359a | -8.29269 | -45.43431 | 2025-09-29 04:06:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 642b109f-577f-3dac-a993-464dd11d08ef | -6.11423 | -43.46535 | 2025-09-29 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4b767393-f0b7-3b67-97d4-75bb4e10bacb | -4.93673 | -45.59346 | 2025-09-29 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d90f6d88-95db-3694-84f3-cdc0124cfd51 | -8.25458 | -45.48938 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c3850dcf-90ca-344d-a7fd-a844e0973db5 | -6.19955 | -42.84512 | 2025-09-29 04:06:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| c01bf679-2999-3290-b6bd-4795563f190c | -5.72259 | -42.76206 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cecd9f94-232c-37fd-b3cf-ca1ae91e9be1 | -8.32478 | -46.2121 | 2025-09-29 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 95473994-5731-3d90-815c-b013d3fdac57 | -6.26919 | -44.0677 | 2025-09-29 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9b5db22-943b-33f6-b504-a0a51b04f3d8 | -8.0103 | -47.03551 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 88526e3f-7598-3a65-a735-ef61abd8e099 | -6.75451 | -45.62194 | 2025-09-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c03d92ac-952e-30b7-b4bd-37e4528ff9d3 | -4.75761 | -38.4795 | 2025-09-29 04:06:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3a1ba33e-5b87-3ca5-8981-455810020e42 | -4.31674 | -47.59792 | 2025-09-29 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f3d0fc3f-7698-3d78-9d52-a02ce5a56cce | -6.14683 | -42.80695 | 2025-09-29 04:06:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e33a9b39-e758-3d6c-80e9-f17ea7aaab50 | -5.73679 | -42.86842 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 9b025f5e-efa6-394d-9a96-0a76f3e42c6b | -6.11021 | -41.82268 | 2025-09-29 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 049116e8-88f3-3956-a866-b49ed2159883 | -8.29491 | -45.46609 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e2c87b56-22cf-338c-afd7-06dcb0db464e | -4.39283 | -44.08535 | 2025-09-29 04:06:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 11d3d981-33b9-3407-9225-14213db959bb | -4.93751 | -45.5887 | 2025-09-29 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c15adc46-f46a-3786-86a4-873314f98cbc | -6.82895 | -44.83731 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| d9a0c05d-5533-37d3-9d4a-2f989cad8d79 | -8.2824 | -45.4952 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 0fe95073-c93f-34dd-993b-682f6e592d68 | -6.4727 | -44.24224 | 2025-09-29 04:06:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7955f457-6910-3c6b-88e7-4c472d1b8da6 | -8.15534 | -46.33567 | 2025-09-29 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 29c64756-a7f6-3752-adc4-ae2c2c0b3677 | -5.28003 | -43.15882 | 2025-09-29 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 140cd673-8297-3e2c-a129-19223c3a1b07 | -7.73662 | -47.00126 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 36156e11-cd39-3d2a-8a82-b41a170a32ad | -7.82365 | -44.80203 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e70c0940-36b6-34d3-b52a-eb6ad458cccc | -6.62276 | -44.95034 | 2025-09-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 4088ce51-312c-304b-b8f0-97caf3ae9060 | -5.31229 | -43.13337 | 2025-09-29 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1dfb18d3-c809-3c5b-af7f-540a36a22bdc | -4.40431 | -44.08294 | 2025-09-29 04:06:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 315d116b-43dc-3a62-90ee-6d98781b17ae | -5.15292 | -46.08166 | 2025-09-29 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0215866f-0888-31aa-9172-a97cf65441d4 | -6.42945 | -43.51089 | 2025-09-29 04:06:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 55dc04cf-e3eb-378c-9b13-698c81476e9c | -7.54578 | -46.10908 | 2025-09-29 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe738178-090e-376a-817d-d852877dc86e | -5.7251 | -42.83295 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cf0f1c40-8125-3e1c-9d9c-1f1e930ad0d0 | -8.00495 | -47.04214 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b8b3558f-c7fa-3d6f-9d02-d6caf08d2376 | -8.27236 | -45.49679 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| bcdab69f-7b99-3bf8-8584-1fc9b9a0294a | -6.49158 | -44.12608 | 2025-09-29 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1dd367e2-497b-3605-b7ca-8dd62ad65079 | -8.52604 | -44.62682 | 2025-09-29 04:06:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ced48f2d-58fd-3d25-8df5-fdd78a37736c | -8.29498 | -45.4882 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3917d921-cfad-3814-8a9d-e398400c7a04 | -6.83101 | -44.82471 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 831638d6-3fcd-3605-b353-7699663e6a1c | -6.4106 | -42.81966 | 2025-09-29 04:06:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 871427d6-d5c7-33ed-96d8-ec31d97a24b7 | -4.15401 | -40.00767 | 2025-09-29 04:06:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0ece821a-e89a-3937-93db-d32ca9a6f535 | -7.37299 | -47.0496 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d49a2893-3e24-3e81-83e9-5fc7fde1b586 | -5.7922 | -42.855 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| b1af330c-f042-3eba-942a-96c66bffaa6c | -7.2209 | -44.78095 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d3abf8ce-9532-39ac-bb57-a6181a4d4dcb | -2.54867 | -45.15602 | 2025-09-29 04:06:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 90da576d-bde3-3172-abb8-dc7cdc2bd929 | -6.14053 | -43.47746 | 2025-09-29 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7786d7d4-dcd6-399c-bed2-136922fe9198 | -5.28026 | -43.15905 | 2025-09-29 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 240f9fa2-e187-3f00-a287-d39ddda476c9 | -5.72267 | -42.86981 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| d8666e43-eecc-39d2-8591-b363c9e18dd7 | -5.36536 | -42.84779 | 2025-09-29 04:06:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4be6f5ba-b767-37b2-964d-8cb407f4d782 | -6.29208 | -43.38631 | 2025-09-29 04:06:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 952ed75a-7b62-397b-9b66-d21ba365c009 | -6.21803 | -44.20277 | 2025-09-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 390baec4-f9ed-3b50-bf87-e54c27050485 | -6.35572 | -42.64582 | 2025-09-29 04:06:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8ef10c41-2f58-3fe0-8db2-134d8ff76796 | -6.05832 | -42.46712 | 2025-09-29 04:06:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 29692032-a879-3835-8e7e-b90d17aad63c | -7.01622 | -44.77111 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7f721eef-8275-31a1-ab7a-6fcd87c4b5f7 | -2.82871 | -45.62729 | 2025-09-29 04:06:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66008630-9f37-3e30-874d-38e2659bd454 | -7.31357 | -44.72146 | 2025-09-29 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc170c39-7672-3881-b345-51091a7d111a | -6.86047 | -47.35588 | 2025-09-29 04:06:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| df95c865-30ae-3869-8c90-93ead3defc78 | -5.30886 | -43.13283 | 2025-09-29 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 07f5e18b-ca19-3110-9b02-dc8898d40cf1 | -6.07447 | -44.06197 | 2025-09-29 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0bd34aa6-8861-3a26-8fcf-4abf8488e15d | -8.28759 | -45.48698 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f015f39e-aff1-3a16-902e-fdec6bf59036 | -5.47723 | -45.55869 | 2025-09-29 04:06:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cbcd470f-a9c1-3279-9808-72754237fe95 | -5.14707 | -37.71664 | 2025-09-29 04:06:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 775c9234-3358-39e1-b782-576a77288890 | -3.83578 | -40.32816 | 2025-09-29 04:06:00 | NOAA-20 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 432733ce-0f9b-34eb-a691-0a402a0cdbdc | -5.82299 | -42.79287 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ba712c13-be3d-3932-b5eb-736b7eafe644 | -7.56314 | -42.40805 | 2025-09-29 04:06:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5cab02f6-5534-3aee-b200-00e1323ef773 | -6.61788 | -44.93781 | 2025-09-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8cd3aee3-ed3f-3ce9-96e6-5eaa205fb093 | -6.7509 | -44.7402 | 2025-09-29 04:06:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 328e814a-0442-3b88-a252-4db6dcf4413b | -5.76627 | -42.83581 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| be1154b2-9c82-3e9b-8cc6-8040fef1d56f | -6.50271 | -42.96783 | 2025-09-29 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9df4985a-bc68-3550-91cd-153a40f1bc59 | -6.46782 | -43.94073 | 2025-09-29 04:06:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 97bc59e4-5082-3887-a871-e759d64fca34 | -5.46396 | -41.07583 | 2025-09-29 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 59b7f506-eaee-3903-9723-5fa16d3ec9c2 | -6.21584 | -44.19393 | 2025-09-29 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b6f6adcb-009a-3733-ae2a-bb892045ccd1 | -6.61907 | -45.90067 | 2025-09-29 04:06:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b0107c89-f2ae-3aa2-84a1-40404b07fe22 | -8.06094 | -44.11964 | 2025-09-29 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README33.md)
