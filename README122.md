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

## Dados Diários - Página 122

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2bcea592-b22b-32b1-a6db-08aecd36176e | -9.93927 | -50.24089 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2c92b590-b620-3084-85b6-9518fc4d3247 | -9.9702 | -50.1269 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 566fbd55-0b60-3f3c-a75f-11a6b6c0aea1 | -7.64043 | -45.5218 | 2026-09-28 16:26:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| b1366ce5-f32e-3956-a302-a8c3bb734aeb | -7.21045 | -45.07318 | 2026-09-28 16:26:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 2598e9ff-a019-39be-86b0-de851f02a137 | -10.98007 | -50.69752 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| f353c1c8-4c65-3581-a347-90b84472e7ec | -10.1169 | -50.19577 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| e2542dd1-b50b-31c9-b7c3-210987b29c4f | -7.86506 | -36.88055 | 2026-09-28 16:26:00 | NOAA-20 | CAMALAÚ | PARAÍBA | Brasil | 2503902 | 25 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 7ab7268b-dbdf-3ee1-926e-ac7ca88e9d9c | -11.36911 | -47.4406 | 2026-09-28 16:26:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 51c498e6-a41f-3a62-9fcc-7832420506ce | -5.33213 | -46.19438 | 2026-09-28 16:26:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 4b01a4cb-080d-30df-995b-6e8f6573193d | -9.99164 | -50.13574 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 5ac8259f-b85e-35eb-8cf8-88d5613b20b1 | -11.12892 | -50.06047 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 326910c6-bf34-3e17-ac52-4e090c9400a0 | -6.59389 | -42.93312 | 2026-09-28 16:26:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 788f6bbb-6825-3399-9986-d0997c7828ed | -5.62818 | -45.53828 | 2026-09-28 16:26:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c92a3b83-1d83-3b4e-842e-10369ccb92a4 | -8.98011 | -44.1524 | 2026-09-28 16:26:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 36.4 |
| c30231aa-32db-39ee-99aa-c4cdae10d5b9 | -10.91596 | -43.85899 | 2026-09-28 16:26:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| ac1a82c6-2861-31d0-a3cd-78a4cc13342f | -4.52015 | -49.86819 | 2026-09-28 16:26:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| a1713587-726e-3b79-a1d3-cfb7a3435949 | -10.91885 | -43.85468 | 2026-09-28 16:26:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| bbc11a75-156c-3513-8e27-b925218b2a1a | -9.53842 | -46.8998 | 2026-09-28 16:26:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| fd0a4f7f-6876-3e12-8caa-f2d90e359fcb | -11.45994 | -49.7457 | 2026-09-28 16:26:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 2e107ee4-b053-3074-b601-98ff86626afb | -3.80944 | -44.10294 | 2026-09-28 16:26:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| f22f70c8-046c-3f82-9885-9464b7f4f00e | -6.67327 | -46.11724 | 2026-09-28 16:26:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5d9b44ee-3b9a-3c4b-afb5-4140e3c4e20a | -10.94537 | -50.67565 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 9da0bb02-7df1-334e-bcd2-316e9cbf1325 | -7.50345 | -44.5723 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 398cb135-d9f8-3197-bb05-63c700dc3f84 | -7.06858 | -41.73283 | 2026-09-28 16:26:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 33be8e3a-3941-3281-bb00-1ff92160981f | -10.92284 | -50.66544 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 27c1dcaa-2afc-3ae6-bd16-65b205d6e489 | -5.79962 | -46.09097 | 2026-09-28 16:26:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| fd1f886d-a824-32c3-9862-b38717f0f9f2 | -8.37418 | -45.46932 | 2026-09-28 16:26:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 36a83465-89a6-3992-ac67-041ff29be19d | -10.79402 | -48.7402 | 2026-09-28 16:26:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 018c01d0-64d2-3f61-bd8a-2595903d459e | -8.60645 | -48.35039 | 2026-09-28 16:26:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| aee69cca-2b93-3d06-a7fe-b25498975cc4 | -7.50825 | -44.58334 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 09b34b4b-3601-34a7-a6e9-a9ec67af2597 | -7.07475 | -40.39211 | 2026-09-28 16:26:00 | NOAA-20 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 39.7 |
| a8ed553d-edda-3203-a8cf-dac006d85c0a | -7.52562 | -45.07889 | 2026-09-28 16:26:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0c944d02-0af9-3140-9e4d-1119f128f774 | -9.35156 | -46.53827 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b2a80eff-637f-3779-91d6-a7658fa4721c | -6.76455 | -43.72366 | 2026-09-28 16:26:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7e08b31f-a0ae-3caa-8716-060e95fa8dd0 | -10.71833 | -44.44024 | 2026-09-28 16:26:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a669da1a-8a47-3f15-9d1a-c34faeffa322 | -9.19008 | -46.95562 | 2026-09-28 16:26:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 3f3c5ac8-4076-30c4-9b5a-f3ebb8ce6db6 | -10.07391 | -48.76653 | 2026-09-28 16:26:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 33cd96db-de08-3a15-b3fc-11673548d27b | -10.93821 | -43.89081 | 2026-09-28 16:26:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5f4eb8e5-020e-343f-a816-de3221eb5e82 | -8.73573 | -44.90833 | 2026-09-28 16:26:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 3046a7de-8cfc-381b-9e8d-adba0358d993 | -7.08652 | -44.4035 | 2026-09-28 16:26:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 869ed038-e2df-3e3e-9080-12d77c977626 | -7.51746 | -44.57425 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 7fb0e6ad-ae7e-3fc5-927d-98ffeeb9e689 | -6.35424 | -45.80525 | 2026-09-28 16:26:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 225c9365-b5e1-38b4-877b-5d2f14d689ab | -9.98015 | -50.12558 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 40.9 |
| db3692e4-dd5e-3302-b7ff-6fd60ca987c7 | -7.30688 | -44.19359 | 2026-09-28 16:26:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bdae7ef0-6adb-30d7-b3e0-8198c4112546 | -7.6587 | -44.75125 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bf49da75-9fcb-3146-afa8-7456da6fc23c | -11.15565 | -50.06905 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 908f6c4e-65dd-37b8-b068-a61f0b195911 | -7.49007 | -45.95874 | 2026-09-28 16:26:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 21623ea7-994f-362d-9726-d886bbc51ece | -8.10181 | -47.182 | 2026-09-28 16:26:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 1aa321b2-bdf7-383f-afe4-11aec992b91f | -6.74607 | -50.92759 | 2026-09-28 16:26:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 41c496f3-7c87-39db-954b-594dba519b15 | -7.04231 | -43.87706 | 2026-09-28 16:26:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 9369a7f0-e86e-3eea-b61e-0f1869d6b2ab | -9.9389 | -50.23798 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b52f9099-2450-3ffe-bb4d-3d42ccaa402b | -8.64796 | -45.75743 | 2026-09-28 16:26:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 5207d155-7429-3779-b9a4-2326783da9c6 | -10.91541 | -43.85518 | 2026-09-28 16:26:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 5f7db71c-d420-3303-829c-c17ef334bfde | -10.90553 | -50.70065 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 34b84de2-d924-365c-9019-e06d5dce856f | -9.30257 | -46.44135 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e24973cc-e2a0-3c2d-94f2-694462cdf82a | -6.14196 | -52.74904 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 97eab061-d228-39e3-a89a-ea1c25153fa9 | -10.20214 | -49.99375 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 92ff960f-3cb0-351e-8021-6c936249fe77 | -6.14921 | -51.56475 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 14a5c7aa-d867-3736-ba91-dc6090f4b308 | -7.75549 | -37.6221 | 2026-09-28 16:26:00 | NOAA-20 | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 49.8 |
| b4726b08-7451-3b43-9ada-337b54917fba | -12.19673 | -53.40371 | 2026-09-28 16:26:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 148800f2-950a-34fd-b125-288d007e3fdc | -11.7622 | -50.76484 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 208f70ea-c80c-3c22-8623-15a849b1d872 | -10.04506 | -50.15099 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 70a5d3d6-d44a-3bbe-b50d-59f3ce27d1bd | -7.45261 | -45.80632 | 2026-09-28 16:26:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| bfe7e76e-e988-3019-a53e-2a58aad857d2 | -11.12968 | -50.06638 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| fe1cfff5-7402-337c-b9aa-ef55a37cdde8 | -7.644 | -45.52123 | 2026-09-28 16:26:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 8051a893-da59-3890-84d8-e01872f9e1ff | -9.30363 | -45.36332 | 2026-09-28 16:26:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0f596331-6f5b-32a3-a67b-82365521894e | -7.4905 | -45.9616 | 2026-09-28 16:26:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| c763503a-a3af-3442-9491-c87024dbd87e | -8.36026 | -45.39957 | 2026-09-28 16:26:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 46e78d07-3873-3682-b4d3-5bb446554f4a | -9.16058 | -43.08106 | 2026-09-28 16:26:00 | NOAA-20 | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| fb467550-d0df-31ad-9e3c-53be7952bf6b | -6.32953 | -44.44275 | 2026-09-28 16:26:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 31a6046a-3af2-31c4-aa88-34def54ef115 | -11.86532 | -50.47768 | 2026-09-28 16:26:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 83c34e31-198c-3d1d-b86b-6e572ec95717 | -8.7264 | -44.89382 | 2026-09-28 16:26:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 677c5d3b-9d59-3ce0-9a15-c93b765d9ab7 | -10.97844 | -50.68455 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| b39e9122-0ae1-3128-b2f4-edd2035a2e54 | -10.2049 | -50.00383 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 931c77f5-856a-3542-8b20-e47098e2aa95 | -9.07941 | -46.50283 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 01ba49f2-be60-393e-b3c0-d9deadaaa5c8 | -11.16175 | -48.31652 | 2026-09-28 16:26:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a8a702d0-513a-381c-a6b5-09ded08b069d | -8.37058 | -45.46988 | 2026-09-28 16:26:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 385a973c-f535-3211-99fb-397b98a516fb | -11.14518 | -50.06738 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 6e3ec9c2-63e5-324a-91f0-9acbbc23a32f | -10.92166 | -50.65576 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 55ee3654-fd5a-398b-93ff-4376e8e0378b | -10.97198 | -50.67551 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 9f60b88c-921a-3a79-8fb7-5b2f8d133e8f | -5.98339 | -53.52824 | 2026-09-28 16:26:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cb9847ce-86ed-3774-8133-7c3caff842b5 | -7.50551 | -44.56462 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 1c6ce0e7-ad54-3560-bece-a83236317af9 | -4.44493 | -42.48478 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 97855d48-bf7c-3a75-ba86-1dc5373ea781 | -5.57521 | -45.30051 | 2026-09-28 16:26:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 267f2370-4fe1-30f0-a3d8-5ce0cac4e004 | -10.92756 | -50.70427 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0d746509-21ac-384a-9275-091b846a6ca6 | -9.07391 | -49.87373 | 2026-09-28 16:26:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| efd154f2-215d-326a-be95-ae9a1dceaf92 | -10.98532 | -50.69685 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 7aff0958-94d1-3121-9fbc-109abd2aa396 | -10.16412 | -46.57224 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| d0fdb86b-65b0-304c-9488-70c20c04d5fe | -10.95181 | -50.68468 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 01ea1d61-acef-34a4-af6d-c59d89aa4355 | -7.90506 | -44.83251 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 27.6 |
| d8508c40-f60e-343f-992c-ea2d1da9714b | -9.30005 | -46.45152 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| edcfa605-60f4-32c0-9897-7137e58bfa4d | -10.60454 | -49.98727 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6b59f8bf-06cf-388c-b9d4-4187a6bf478c | -8.38375 | -45.45935 | 2026-09-28 16:26:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 37.4 |
| ef7f4d78-8abe-34db-91a9-e2c242ce087b | -8.37479 | -45.47343 | 2026-09-28 16:26:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| c907421a-be15-3cbf-91fe-7982b5a5d942 | -2.33551 | -45.30481 | 2026-09-28 16:28:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5ba53df2-2d53-3e25-96ec-aae639310826 | 1.84267 | -55.59351 | 2026-09-28 16:28:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 7ff71cc3-99ee-3761-bb85-09a1461d24a9 | -2.25107 | -48.74744 | 2026-09-28 16:28:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7a61c734-2994-3608-b5c4-c17459ab1e30 | 1.87788 | -55.56668 | 2026-09-28 16:28:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 568f091e-1d92-31ff-91c9-83e23a07a9e5 | -1.47509 | -48.92354 | 2026-09-28 16:28:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1358a775-6f48-3a8b-851b-e9a4f14be76a | -0.47571 | -51.8217 | 2026-09-28 16:28:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 18.0 |


[Clique aqui para ver as próximas entradas](README123.md)
