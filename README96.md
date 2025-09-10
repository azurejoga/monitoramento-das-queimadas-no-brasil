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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e8393df-7854-3e80-a33c-092c4622db2d | -7.23092 | -46.19082 | 2025-09-10 05:04:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca79bdf2-de23-3407-8c4b-c283e63a163f | -7.78134 | -46.06523 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 58b3fb2d-5b10-3e66-b38a-e463dd84d894 | -9.05252 | -50.48991 | 2025-09-10 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 08aba290-f604-3d60-a67f-4476c4433309 | -11.4425 | -43.62822 | 2025-09-10 05:04:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ea5508db-f08d-3520-83f8-5100fcb5965f | -9.08744 | -47.05986 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c1b21b53-cd60-36a5-be06-9fcd9fbfc30c | -11.53355 | -47.32059 | 2025-09-10 05:04:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d8a1c22a-f963-3d62-b329-83cc3b00ff0f | -11.19769 | -48.3852 | 2025-09-10 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c2d046a7-5963-3a3d-9406-421a2d6d4380 | -9.44735 | -46.69797 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 79dad76f-689e-37b2-9fd8-ffe10e37bffd | -9.3454 | -46.75252 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1cacbdc-a6fd-3751-8e85-12f7e7fd2655 | -10.30672 | -48.80586 | 2025-09-10 05:04:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d19b280a-c11c-3a60-896d-a9c6acfe3b65 | -12.00233 | -50.98154 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 7e21e8c2-7f80-3f32-b011-016fdd2a3116 | -9.45207 | -46.71325 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 84c3d55d-6f48-3c4a-a16a-5ead48957c6c | -7.86432 | -46.02394 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 40ee5f23-6664-33cd-b84f-5b20e146cf64 | -9.6862 | -46.89378 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 36.0 |
| ce100ecf-dbc7-3dcb-8d9f-cd9b1638e322 | -11.67923 | -46.90406 | 2025-09-10 05:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8d35ade7-d84c-3e0c-8eeb-7f9f6a401087 | -10.01018 | -51.70529 | 2025-09-10 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3719d2ff-9a94-3b70-8879-66ff6f04b7e5 | -8.0517 | -48.67944 | 2025-09-10 05:04:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e977a8de-5add-392c-8727-2855fc00741d | -13.97524 | -48.22313 | 2025-09-10 05:06:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9854c82c-0e9e-3f05-9cc1-55ad2f5f3630 | -19.2914 | -47.98663 | 2025-09-10 05:06:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 08675e36-2adc-37a5-bdea-70e549b9f930 | -15.01029 | -48.03093 | 2025-09-10 05:06:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f31f1a20-888d-3223-8232-3038049af1b9 | -18.02337 | -47.15226 | 2025-09-10 05:06:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 65b1ecbd-4547-3c5c-bd10-8fd611a50c07 | -18.34539 | -49.33545 | 2025-09-10 05:06:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 206b503b-63cb-360f-a06c-4b12f1007f00 | -17.19739 | -50.15844 | 2025-09-10 05:06:00 | NOAA-20 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e024ea7d-646a-3443-b3fa-cce1d151cfeb | -14.90332 | -50.12549 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 7e78ed97-7661-375e-a950-847602fbdc72 | -13.12603 | -54.9319 | 2025-09-10 05:06:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c69c5016-bfa4-344b-9869-1322d2eecf35 | -12.61205 | -56.96474 | 2025-09-10 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa28252e-7ea3-3f89-aa2a-647420d91a3b | -14.39174 | -47.31863 | 2025-09-10 05:06:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 987e0f47-9117-34e9-acb5-1fe929068e9d | -13.29311 | -51.72258 | 2025-09-10 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1ef68597-4802-3005-b10f-c50daba76fc1 | -13.12778 | -54.92015 | 2025-09-10 05:06:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 59a8dd82-c043-3aca-96d8-a3f526aad607 | -15.10629 | -50.09362 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 923ac641-b6b1-35f8-a4ab-1c929c204dac | -13.28839 | -51.7259 | 2025-09-10 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e3dbf854-fc97-3512-8b4d-0c435f352b81 | -15.69787 | -49.90055 | 2025-09-10 05:06:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6e74c163-0cc1-35b3-9283-7b0f9a9ad190 | -15.39564 | -52.91609 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 90a6fa77-73e7-3188-b75f-e3bee324a0da | -15.85721 | -51.82965 | 2025-09-10 05:06:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13135b88-f3f2-350b-a3e6-a86555a9060c | -16.44705 | -51.9826 | 2025-09-10 05:06:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 187220ae-a618-3031-a5ad-fb0a98503fa5 | -15.90247 | -50.18303 | 2025-09-10 05:06:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e2147bf0-840c-34d5-a0db-c314cc9edafa | -15.80026 | -52.25773 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b12715f7-0e00-3535-8484-9ff0d4565b23 | -17.30575 | -46.74987 | 2025-09-10 05:06:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 876e4006-41da-37dc-9fe8-61f273b7dfd3 | -15.81133 | -52.27038 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 028667da-8310-3886-9193-a0e3910743cd | -15.90661 | -50.1892 | 2025-09-10 05:06:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 20aec4e5-74b5-3f33-b137-8a139b466c58 | -13.12313 | -54.92743 | 2025-09-10 05:06:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 94997692-87bc-363c-8347-a510934c9f71 | -17.31299 | -46.73882 | 2025-09-10 05:06:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a5e8c77-91b4-3588-8062-fdf8f7f0936f | -12.60432 | -56.97072 | 2025-09-10 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ddf92369-16fb-3e28-a288-2dc9c085a53f | -15.86152 | -51.83021 | 2025-09-10 05:06:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 09d02910-feb6-3709-8f32-77debcb97d15 | -15.13269 | -52.38623 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa2db790-31d3-380a-b2f0-a701b6a32652 | -12.60763 | -56.97126 | 2025-09-10 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f70530d-608a-33c5-8c52-4acb1ad9f688 | -18.00785 | -47.12381 | 2025-09-10 05:06:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 145c5846-af41-3e8a-8b22-b1119abafe39 | -15.16079 | -52.32126 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5ac30d3-cb52-3ee5-b364-63a2111cd731 | -19.29114 | -47.98865 | 2025-09-10 05:06:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dbdc8ebb-0589-3377-b1e8-476c8714a566 | -18.02982 | -47.14848 | 2025-09-10 05:06:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| c5b649a8-6351-39b9-8bb6-c951c790ec42 | -14.25073 | -46.69313 | 2025-09-10 05:06:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| fb66de94-b47b-3fcb-ae66-ee36250fbd9e | -12.41521 | -63.89399 | 2025-09-10 05:06:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 86908c99-a72a-3d6d-ab5f-db8803a41386 | -15.01706 | -48.02057 | 2025-09-10 05:06:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eec72312-15aa-3681-8307-e6dbd188d75a | -15.0926 | -50.08644 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c63b68e1-40e4-37e7-a1b0-d819c344e12f | -15.80911 | -52.25525 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8a3dddc5-51a6-3d3a-9137-220fa3a7c982 | -13.29839 | -51.71523 | 2025-09-10 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ddb8bf2d-4885-38bc-8df0-4999cfcd3d05 | -15.80567 | -52.25681 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d739f98d-2647-3c77-911a-73f986792bc1 | -18.02934 | -47.15339 | 2025-09-10 05:06:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 9e16396e-57be-37b8-81f5-20827b5ccda0 | -14.86224 | -49.53003 | 2025-09-10 05:06:00 | NOAA-20 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4607d3e3-a55c-3038-affb-2e8cc4140080 | -15.80893 | -52.26463 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 98eb70b8-5a91-3ab9-8651-56494b2fc688 | -17.57411 | -51.06252 | 2025-09-10 05:06:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb3b08b4-4130-349f-9439-96540f8489d0 | -12.61592 | -56.96175 | 2025-09-10 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 836c1f18-6ca8-3899-a6a9-b78d6d3085f2 | -14.57918 | -51.4052 | 2025-09-10 05:06:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c692c8f2-ac72-3d04-af18-c63c8e55634f | -14.39085 | -47.32674 | 2025-09-10 05:06:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67b34093-fe80-35e9-af75-ea57e99b2868 | -16.32415 | -52.92055 | 2025-09-10 05:06:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ae94560-64dd-3cbd-949d-28812e757c54 | -15.27768 | -53.78518 | 2025-09-10 05:06:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6bb68a0-1a63-38c0-84af-421686c7479e | -19.51421 | -45.01523 | 2025-09-10 05:06:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b05c7584-4d47-3cd7-bcd5-e182b44cbad9 | -12.64381 | -55.9495 | 2025-09-10 05:06:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5eddb410-b258-31bc-aed2-91d195e3f059 | -17.20719 | -50.15972 | 2025-09-10 05:06:00 | NOAA-20 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae20b12c-caae-3639-91f3-385a7719309f | -14.90835 | -50.11872 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0eb76548-baae-3b38-8bdd-bc00864c37d5 | -13.1272 | -54.92407 | 2025-09-10 05:06:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 81f5ec95-a600-372e-a767-42ffd90dd35b | -14.92421 | -50.11295 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| fd49cbd6-dd8f-3d6f-9312-928725ecebe7 | -12.62254 | -56.96282 | 2025-09-10 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 07fef70b-76b7-359c-ae08-be597d12bd32 | -15.8217 | -52.2313 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 267cfd5f-8b1b-3805-aa83-a8263ce548f9 | -16.46681 | -50.666 | 2025-09-10 05:06:00 | NOAA-20 | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4b9ba9ad-e67a-39d4-a6a6-1c41e2b8f207 | -15.95549 | -50.2282 | 2025-09-10 05:06:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7362d22-09a7-38da-a428-ef124451bda2 | -12.92338 | -54.76491 | 2025-09-10 05:06:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ffc44389-3792-32a4-986c-2d2c0fcbd079 | -12.6115 | -56.96827 | 2025-09-10 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e6403bce-ded5-3305-9c2b-67f8ce0a1e3e | -15.25633 | -53.77254 | 2025-09-10 05:06:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 699a7722-af4e-3033-9e04-f95064dcf415 | -17.30624 | -46.74487 | 2025-09-10 05:06:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0429332e-9138-3766-bd30-8bbb94ef50c9 | -13.92532 | -48.24975 | 2025-09-10 05:06:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d14d2a4e-5290-305b-98cd-a5e19abdd24d | -17.2452 | -46.08228 | 2025-09-10 05:06:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5210b4da-ac44-39f7-87c4-76b67ab3ee2e | -15.13913 | -52.4003 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c884f511-86cf-337f-bc06-4471f54d0891 | -14.89876 | -50.11797 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6fd7dc23-5033-36e1-aed0-7b39fb260198 | -18.13885 | -51.72511 | 2025-09-10 05:06:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4e6e9f0-d769-3dea-8b4b-b7a907773412 | -13.12429 | -54.91961 | 2025-09-10 05:06:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4e5a7dea-71c7-3a7c-a2a8-e1d8d82d9e6c | -17.25121 | -46.08679 | 2025-09-10 05:06:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 83f81411-fab4-379d-8771-74e58aeb1eac | -15.84597 | -52.27427 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6e91009-8e5d-39f7-b78a-8248c613fd65 | -17.24339 | -46.07627 | 2025-09-10 05:06:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 96635f81-553f-3d49-90fd-fa31bbb1feae | -15.22216 | -48.24138 | 2025-09-10 05:06:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 47e55466-2e92-3ac3-86dd-0ae44dab4325 | -13.12546 | -54.91175 | 2025-09-10 05:06:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 56dbafb9-ffd5-3918-a356-6bed1e10d9a0 | -14.89941 | -50.11284 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9f91de73-1470-39d6-b310-1e4df699a34f | -15.01956 | -50.08732 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| b0159299-2cb4-3dc4-aa8e-b0afe2e35be9 | -14.90451 | -50.11565 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5964d2f7-5f80-31c6-b392-3452157b90e1 | -13.29366 | -51.71862 | 2025-09-10 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b67fd8b8-12d9-3092-850e-d5470fada600 | -16.45681 | -50.66988 | 2025-09-10 05:06:00 | NOAA-20 | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9a64c195-c7b8-3bfd-a271-060b40cec4a0 | -15.85969 | -51.82741 | 2025-09-10 05:06:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83e3a482-7a2e-32ab-8f99-ffbe1846ae9e | -15.81335 | -52.22987 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e274d745-1dde-34c0-b0ec-0c20aeedba50 | -18.46082 | -46.4738 | 2025-09-10 05:06:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f1e71e2-5c58-3761-ad3d-7274fca44dd3 | -16.05986 | -49.97002 | 2025-09-10 05:06:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README97.md)
