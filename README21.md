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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb6507c5-4347-3ba0-ac57-b7a02c40a26d | -4.72607 | -49.0908 | 2025-10-26 04:00:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e5c9e62-71c8-3320-ac6c-d0e6b899b32e | -7.79754 | -43.16115 | 2025-10-26 04:00:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 85073459-5469-38e0-8fb4-62c60db12c86 | -8.53937 | -47.20348 | 2025-10-26 04:00:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 056d20f5-d1ec-3b13-ad9b-d54d508d0a5f | -7.03747 | -45.7213 | 2025-10-26 04:00:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a98e4ad-251c-3ac4-98ba-4a25995552a7 | -6.22368 | -42.54739 | 2025-10-26 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7dbf5a73-f2df-389a-94e2-47c439126c17 | -4.71983 | -47.42108 | 2025-10-26 04:00:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 06c9e18a-0981-355c-b9d2-dd2079eced03 | -6.01987 | -43.30067 | 2025-10-26 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 606a2961-a1a5-318f-807a-5f50b94a8226 | -6.43329 | -42.30544 | 2025-10-26 04:00:00 | NOAA-20 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 90226755-ae86-3e38-a17f-6c74aaff5498 | -6.38931 | -45.7826 | 2025-10-26 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a75d0225-32c2-3328-b8f1-0bd874dbce10 | -4.61784 | -46.03502 | 2025-10-26 04:00:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39f62868-c3b6-3219-9240-7f6d0316d2a8 | -3.74065 | -43.381 | 2025-10-26 04:00:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 04c89758-3d52-3b9a-ab59-7e08cc2bc265 | -4.8186 | -38.65922 | 2025-10-26 04:00:00 | NOAA-20 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3f5669ee-d675-3caa-b6f4-170f751432d2 | -2.81606 | -49.14946 | 2025-10-26 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1402e284-0a48-341e-847e-b407b18562b4 | -6.54678 | -41.60241 | 2025-10-26 04:00:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f83d55eb-b6e4-3627-9ed6-7690c5152401 | -5.60724 | -41.1217 | 2025-10-26 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 69098ec4-e625-3798-b3e6-3a9faddf7fdf | -7.41809 | -48.77567 | 2025-10-26 04:00:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0eeffd3d-4ed1-3d14-bbef-3cc557f6839a | -4.72474 | -47.42199 | 2025-10-26 04:00:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 446c5950-72ca-3010-880b-3d192bc598d1 | -6.33699 | -44.31925 | 2025-10-26 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 49152f9e-4dd2-363b-adee-7c707d8c8335 | -5.69265 | -48.49176 | 2025-10-26 04:00:00 | NOAA-20 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c9a4501-c291-33e3-9821-9ee57d48d6d9 | -9.34861 | -40.48478 | 2025-10-26 04:00:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.1 |
| a1a0f5f8-6db3-3181-89dd-6cd11d9513e6 | -4.59828 | -49.58947 | 2025-10-26 04:00:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bccea7f4-c845-32d4-be82-d719940e4fdf | -4.39427 | -43.32103 | 2025-10-26 04:00:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e5a691f-0a3b-3c83-8b0c-1744077de6a4 | -5.58232 | -37.28256 | 2025-10-26 04:00:00 | NOAA-20 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c6f28ec7-b5c1-3288-92bf-e14f97cb1378 | -6.6004 | -42.66037 | 2025-10-26 04:00:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fdf22edf-724c-3bd6-a55f-c4c93c2b592e | -7.34725 | -42.44012 | 2025-10-26 04:00:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 84d3ff0b-c114-3d5d-9adb-d2de63585c84 | -6.13344 | -42.45655 | 2025-10-26 04:00:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 245eb497-2bc0-3255-83a1-26f4635a3420 | -8.53777 | -47.21266 | 2025-10-26 04:00:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e735c747-4e4d-356d-b4e6-d17f9557fc3c | -6.8412 | -44.01292 | 2025-10-26 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 29c626c0-b7d0-3b93-b0a6-3152a58fe5f1 | -4.35869 | -48.65952 | 2025-10-26 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 07d3c35a-cbd4-3904-8cc9-16c2ed771e1d | -8.32568 | -48.18821 | 2025-10-26 04:00:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe07670a-7737-3e49-a39c-d2795e065363 | -5.46762 | -40.8724 | 2025-10-26 04:00:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5f675436-05ad-3b29-86fa-5b2d67097305 | -4.02837 | -46.07295 | 2025-10-26 04:00:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b059707f-e931-3692-8223-aee6a40f2d19 | -4.90466 | -43.24051 | 2025-10-26 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1134c5f3-3773-3e96-a5d3-ab47458bacf6 | -3.8336 | -50.19975 | 2025-10-26 04:00:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 11322149-f8e2-3616-9ed9-79623e862ab8 | -6.39287 | -45.78761 | 2025-10-26 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b2ffa96a-66f3-361c-8e3c-e55834b2df9c | -7.8454 | -46.43631 | 2025-10-26 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| c584f159-d4e3-3299-b6c7-052040aa8ee1 | -5.56481 | -43.61082 | 2025-10-26 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c3711fbf-c183-3e6d-9210-a630fcbe5e43 | -6.06306 | -42.14881 | 2025-10-26 04:00:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c09fe41c-a86d-3595-8251-f755c17d25c9 | -5.02551 | -41.20516 | 2025-10-26 04:00:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4b28a8a9-f396-3c88-929d-e248d5ec538e | -4.91365 | -48.56605 | 2025-10-26 04:00:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ecc6b17-686c-3b3a-817d-2dfe00e63132 | -6.22436 | -42.54329 | 2025-10-26 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c706c581-039a-3572-b241-86a4e47116a1 | -6.5501 | -39.31545 | 2025-10-26 04:00:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e3f999ea-94a0-30ff-a624-9e8fe489f052 | -5.29816 | -41.14339 | 2025-10-26 04:00:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| a83cb137-9883-3e94-82a8-e0dc4cfe8fd8 | -6.22654 | -42.55206 | 2025-10-26 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 62bcaa2c-19e1-3c5e-98b6-79fcc0bbfa46 | -4.73187 | -41.48164 | 2025-10-26 04:00:00 | NOAA-20 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 296499e6-1507-3871-bc62-7727d762e5e4 | -5.22003 | -40.93146 | 2025-10-26 04:00:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2608e77b-411a-3389-8007-a67a05b102d2 | -6.16911 | -38.90615 | 2025-10-26 04:00:00 | NOAA-20 | ORÓS | CEARÁ | Brasil | 2309508 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d30e81e5-2ea2-3178-a885-64363a48d364 | -5.61303 | -42.67189 | 2025-10-26 04:00:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 71c5e298-cb4e-3d63-95d4-738e55008d38 | -4.88951 | -43.23093 | 2025-10-26 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 84af3333-ac8b-3800-8b3c-78527f6894a6 | -4.26427 | -50.50902 | 2025-10-26 04:00:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4034134e-be00-3026-a026-9de2f9335468 | -6.21431 | -42.53893 | 2025-10-26 04:00:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| df3ed50a-b455-3ef5-8263-569a000667ed | -6.84195 | -44.00832 | 2025-10-26 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aeeb31ac-ddb5-31c6-bf4c-34ca90e77545 | -7.77443 | -42.92915 | 2025-10-26 04:00:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 54485fd3-e67c-311b-a804-47ad890d6544 | -5.87323 | -42.61084 | 2025-10-26 04:00:00 | NOAA-20 | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d46226c6-616c-32ca-b689-bab8fd6d96d3 | -7.04166 | -41.64719 | 2025-10-26 04:00:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1eadbe14-2bfe-34e5-ac37-20b0abc57eca | -3.31013 | -50.1159 | 2025-10-26 04:00:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a92ae63-eb97-3496-bc91-7f929f985617 | -5.44249 | -37.62135 | 2025-10-26 04:00:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 011b04c6-defb-339a-9e43-11326a99a2ba | -8.82282 | -40.30806 | 2025-10-26 04:00:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3cc2ce7b-b5f1-399c-981a-663c50beccac | -7.69571 | -42.24036 | 2025-10-26 04:00:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8728778b-5a0d-3fda-bea7-bf81254c2762 | -5.50148 | -49.58098 | 2025-10-26 04:00:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11427c96-f5cd-391a-97d3-cfd9a97037c0 | -6.72951 | -45.38121 | 2025-10-26 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 405df3b7-44f3-3d5d-b29e-ef40c9cf2150 | -5.56863 | -40.92028 | 2025-10-26 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d7111af0-5aa7-364a-be06-101d5afcbec4 | -5.88614 | -41.30748 | 2025-10-26 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f84ca8c2-9715-3231-846a-d3f034f0af3e | -5.87906 | -43.9355 | 2025-10-26 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 36a05725-eec4-39d5-8bfa-0c19d0a4c8a7 | -7.09344 | -39.57515 | 2025-10-26 04:00:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9afaf270-223d-3a14-9c14-6ef4c0cafd3b | -8.15092 | -43.38567 | 2025-10-26 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f926fe89-d823-3b2c-878b-0fb0a7101e8f | -6.06654 | -42.14939 | 2025-10-26 04:00:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ce7b0a29-9fc2-3700-8eee-cafbc401acae | -5.89125 | -49.6605 | 2025-10-26 04:00:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f038ad84-2073-3876-8302-43a53fcbd856 | -5.70727 | -49.31352 | 2025-10-26 04:00:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3972506-17d5-3d6c-89b0-2fd6290ae868 | -6.1478 | -41.81408 | 2025-10-26 04:00:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| de31af35-4a78-3d32-acd9-783019c360d7 | -7.35357 | -42.44516 | 2025-10-26 04:00:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| d34e0bc3-ac91-3288-ab28-0093063c1bd2 | -6.30259 | -40.87711 | 2025-10-26 04:00:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1485dfea-03c2-3df4-8f09-8eec23b845f3 | -8.03597 | -45.1534 | 2025-10-26 04:00:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 25698ad9-0fbb-3955-85d1-846430b0cde1 | -3.13844 | -50.16642 | 2025-10-26 04:00:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 24ab2f5b-cfee-395d-a6df-a9588bca4e55 | -4.68237 | -42.72812 | 2025-10-26 04:00:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 63de0df1-2574-3b3e-aa63-a36a288b1e30 | -7.84756 | -46.42351 | 2025-10-26 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7995c7c0-500c-30c9-8b2a-c9d9cb407a6d | -3.26593 | -50.04832 | 2025-10-26 04:00:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2fe06786-afd5-3012-a371-26a3d49e0c43 | -6.38862 | -45.78666 | 2025-10-26 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a1ef4726-9ace-33fe-bf11-66f9fc0d2430 | -5.26447 | -45.3781 | 2025-10-26 04:00:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b039736-c139-3074-bea3-f6278f9529eb | -5.54959 | -41.3925 | 2025-10-26 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3642e184-6c7c-3e44-ab04-a2cfd1838dee | -5.5478 | -41.40351 | 2025-10-26 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1f383e74-89c9-3bca-8a06-87c979679ee8 | -4.84306 | -40.71911 | 2025-10-26 04:00:00 | NOAA-20 | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cd744f80-f1cf-3114-b7e3-81fa93a11dcd | -7.69693 | -42.18997 | 2025-10-26 04:00:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 8cadfe76-c782-394c-b514-4c11f97ac0d1 | -4.32382 | -41.79272 | 2025-10-26 04:00:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1764f2c1-92c1-3be3-808b-0e283874acac | -7.68722 | -42.18905 | 2025-10-26 04:00:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a3497e11-be2e-301b-98e1-d271b75fb561 | -3.09934 | -49.45222 | 2025-10-26 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 48b24b71-b592-3ac9-a494-f9aad569f8d7 | -5.47543 | -40.8881 | 2025-10-26 04:00:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 26534333-36c0-3688-9ec1-b7a1163dae76 | -6.57368 | -41.45663 | 2025-10-26 04:00:00 | NOAA-20 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8512d337-62ef-3ba2-9a0d-c520bc7ce0b2 | -6.98504 | -44.00939 | 2025-10-26 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 011ae24b-51f9-3f80-ae03-999e81bb5878 | -6.39425 | -45.77942 | 2025-10-26 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 7211657f-9a29-392a-82a0-64b1d1b0ac20 | -5.82344 | -40.81533 | 2025-10-26 04:00:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 263335ba-a1b8-35ba-81ee-0237ffc1a9aa | -3.10187 | -49.47346 | 2025-10-26 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 127bf3df-51cf-3c9a-bbd1-c875c76bbbc6 | -7.84817 | -45.37469 | 2025-10-26 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e788a006-2ca6-328a-ab37-c0b2df4a07ea | -7.87609 | -45.71991 | 2025-10-26 04:00:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 345e208b-78a1-3278-8de7-03c81b02683e | -6.43424 | -42.03662 | 2025-10-26 04:00:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ac201ccc-b616-3515-94f4-e038505be170 | -4.65439 | -41.61208 | 2025-10-26 04:00:00 | NOAA-20 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e97f65e0-b70c-34d2-9da1-f362053b8139 | -7.99883 | -39.62904 | 2025-10-26 04:00:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 2fbfd879-ed81-33f4-803a-b177bcc22364 | -8.66859 | -44.77035 | 2025-10-26 04:00:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7f33240b-f3fd-3029-8c39-20083a5fd76c | -6.12823 | -41.71866 | 2025-10-26 04:00:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 831d3e2b-c380-3373-83b9-72be7ad37662 | -4.70637 | -46.43613 | 2025-10-26 04:00:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README22.md)
