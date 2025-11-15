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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 293e1e37-fb58-3bd5-aa6e-581301fb4c1a | -3.62715 | -52.11522 | 2025-11-15 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7baa6cc8-5122-389e-8b41-b51357f29e23 | -6.27065 | -41.74947 | 2025-11-15 04:25:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 4bb3f3f6-2d75-31aa-86d4-e9783884e836 | -4.2446 | -48.39079 | 2025-11-15 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e961ab1-db9c-385a-9ddb-a26509a41c70 | -4.57897 | -43.16988 | 2025-11-15 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85e3ffb4-f190-31bf-8034-75fb41006dd3 | -3.70324 | -47.63202 | 2025-11-15 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dc5b289c-271f-3849-95f0-667c4f9b0581 | -9.02056 | -48.04045 | 2025-11-15 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c737247-c528-3441-8f6d-b3f1ce034fce | -4.37502 | -47.2518 | 2025-11-15 04:25:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf2eb9f9-1e1f-3784-bb76-e39a27138822 | -7.40294 | -41.00823 | 2025-11-15 04:25:00 | NOAA-20 | BELÉM DO PIAUÍ | PIAUÍ | Brasil | 2201572 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 5fc96259-d1a7-3ff3-96c3-3b6022c24e2d | -6.63963 | -46.54146 | 2025-11-15 04:25:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e650b0e8-6ef8-3a49-9897-5502f854b383 | -2.43371 | -48.04807 | 2025-11-15 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 39279115-34ca-3ecf-9fdb-1e6a4569ebd1 | -3.27966 | -45.46279 | 2025-11-15 04:25:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f33bb0d-7ce5-3deb-a9ad-686f4fd4a7d6 | -6.16945 | -48.0443 | 2025-11-15 04:25:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0507aa8d-7cf7-3326-a3f4-0877bece6db0 | -3.17179 | -48.6143 | 2025-11-15 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3dc62f3-77e7-3cae-9bf7-53563a975abf | -4.85539 | -40.75972 | 2025-11-15 04:25:00 | NOAA-20 | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 2c7cd3bf-0665-3849-9063-58b4be2da40d | -6.63852 | -43.91993 | 2025-11-15 04:25:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 902bdc81-889b-3598-8978-7530133cb4d5 | -8.32519 | -45.41077 | 2025-11-15 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ff4b8541-83bc-34ef-bb36-443923345281 | -9.0963 | -47.78328 | 2025-11-15 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3fd3952a-f3f6-3f43-afa7-89c7fbddc04c | -10.05477 | -45.35032 | 2025-11-15 04:25:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cbbddcd1-8aa7-395d-a552-7f58f94ed3fe | -6.17397 | -44.34998 | 2025-11-15 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4a94e4e6-3822-3078-b209-1e2ea9fe9fba | -3.2802 | -45.45935 | 2025-11-15 04:25:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c084374c-5cbd-3758-bca8-52a669291cf5 | -8.33759 | -46.6983 | 2025-11-15 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21e2a8dc-30b8-35aa-96ae-a0d863d976b5 | -4.86906 | -47.27071 | 2025-11-15 04:25:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3a6ab2eb-42d1-3535-86e6-278db678b82b | -5.93245 | -47.20702 | 2025-11-15 04:25:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8f06ec96-8bd8-3202-a597-f109136ac5c1 | -6.58394 | -47.53538 | 2025-11-15 04:25:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a15cc5cc-fd8b-30f7-b1cd-f02aeb2d8e37 | -4.72758 | -48.56452 | 2025-11-15 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45e7447f-4f69-3583-9c41-54e4dd7c0414 | -4.02167 | -46.78478 | 2025-11-15 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0933e53e-8f8f-3937-bc03-4e06987bb198 | -4.91409 | -44.78968 | 2025-11-15 04:25:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c6a4af48-7aa1-3449-960b-01b1c0aa1ea4 | -6.73245 | -42.96794 | 2025-11-15 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 561e0747-ab42-38c5-bb21-f6aa4020af89 | -4.72961 | -47.1609 | 2025-11-15 04:25:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 3f53f535-3df2-3190-b68c-4769a6ca1c95 | -10.10815 | -40.89951 | 2025-11-15 04:25:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3b21d28b-89e0-3312-a24c-7cfdf0038648 | -5.58217 | -47.10001 | 2025-11-15 04:25:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e73a9c3a-6db8-304f-9d92-ec2eeec5cb09 | -6.7082 | -42.95546 | 2025-11-15 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6a02bc99-a4ec-3444-9a30-8c87d11ee3e9 | -9.94058 | -44.93011 | 2025-11-15 04:25:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc88ca06-5bdc-3536-a475-d7a4aa6c7875 | -9.13798 | -47.75748 | 2025-11-15 04:25:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7eb0f215-5e9e-3747-a508-f24b866e66b6 | -4.60452 | -45.96115 | 2025-11-15 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 773301bf-d5f6-3643-ab31-cfe7db7c8170 | -6.28075 | -44.75161 | 2025-11-15 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f60e3dd4-d28b-30a3-8515-a0375b63d194 | -5.51796 | -40.97273 | 2025-11-15 04:25:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 406012d3-9be5-3936-857c-36a60acb6d54 | -3.93881 | -47.56245 | 2025-11-15 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2e15d7d4-c84f-3b53-9682-0698474f4ebb | -6.2601 | -48.24549 | 2025-11-15 04:25:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 593fddc6-4c99-3b0c-88cf-e3a1f5fff8bf | -4.65823 | -46.84234 | 2025-11-15 04:25:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 39784ca0-f5de-39e6-b233-4d352d377bb9 | -4.65899 | -45.05261 | 2025-11-15 04:25:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 538fbd8b-3ee5-34a1-983b-69ce29b92824 | -4.76255 | -50.68343 | 2025-11-15 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b724b8d-17f2-3d9d-92fd-a8ec68964280 | -4.59646 | -49.62467 | 2025-11-15 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8db80729-932b-3d38-8f75-b5f95270c9e1 | -4.57273 | -45.709 | 2025-11-15 04:25:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d2e016e-eaa0-3208-af16-28653154cb8d | -5.62484 | -45.04468 | 2025-11-15 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dedb005d-1def-3d21-933e-e8dffbd73a9b | -9.66365 | -43.90046 | 2025-11-15 04:25:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 334db0aa-de44-3ddc-9696-1592b6745b7d | -6.72408 | -42.94923 | 2025-11-15 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 3a25ab83-4e8a-35b9-b74e-73c925b2eff3 | -3.6924 | -45.71075 | 2025-11-15 04:25:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 827d3f08-c6d8-3cd6-9fb6-c9768e25245c | -5.48144 | -40.96784 | 2025-11-15 04:25:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 37ccce28-e9f3-38d2-ad53-93684ec68f1e | -2.88244 | -51.42677 | 2025-11-15 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0515bec2-6c52-30b5-b5d4-f23d88bd2db4 | -7.87905 | -48.41051 | 2025-11-15 04:25:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d806936f-e2ea-37ca-af08-2e40761152df | -3.7107 | -52.09921 | 2025-11-15 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bcd9bb9a-9e53-362f-836a-7abf79f90ec5 | -4.19383 | -51.02485 | 2025-11-15 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42d7af35-d5d5-3bb2-9200-0b7f0b3f1802 | -3.47706 | -50.03973 | 2025-11-15 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a233ffd-0dae-324b-a660-c3a523d8cc7b | -1.29603 | -53.76384 | 2025-11-15 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3daf5e8b-4a39-3d6c-aade-cb49bef92173 | -2.51756 | -47.81384 | 2025-11-15 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 99ae7605-3da1-37d2-b141-bf9da8d558d4 | -5.8413 | -47.56041 | 2025-11-15 04:25:00 | NOAA-20 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e05e58e9-bf3b-3499-b65c-11fced4b5b39 | -4.04914 | -48.09847 | 2025-11-15 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab32dab4-63e8-32a0-bc3c-2d3b1fdcb7f1 | -6.05923 | -44.16117 | 2025-11-15 04:25:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3957f2bb-62d0-3345-97ae-5509460d343f | -2.95328 | -48.58786 | 2025-11-15 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8413f547-27a7-347a-b3ca-e0dfb33e25c7 | -6.15807 | -48.04993 | 2025-11-15 04:25:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e3eb2d85-aaca-3cff-85e8-b5a0cdcf7947 | -8.85156 | -47.33669 | 2025-11-15 04:25:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62651a4f-a718-3040-a55d-520db0d3d30d | -7.45695 | -42.76564 | 2025-11-15 04:25:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 062de024-6da2-3e6b-a296-59439b6330ac | -3.45944 | -50.12185 | 2025-11-15 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d0321182-eec3-3705-b7f2-3318364c6581 | -3.15427 | -50.26561 | 2025-11-15 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d9001c8-31ad-31d9-8e49-fbe4ba1f5be4 | -2.68953 | -49.86042 | 2025-11-15 04:25:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4977ce58-0175-3808-9874-be597acc9f6e | -1.82967 | -53.79448 | 2025-11-15 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ded02b4-c874-3582-b584-79f00927f721 | -4.54578 | -43.21857 | 2025-11-15 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 7d953b6a-3a73-325c-9160-a975e05ae8ed | -5.24919 | -44.86377 | 2025-11-15 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d378ab9-cbbd-3b83-9589-6e0c15898e8f | -5.33776 | -43.03648 | 2025-11-15 04:25:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a961583f-b4a9-3686-b29c-a518194afa21 | -5.5949 | -45.79967 | 2025-11-15 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7b9dfabd-a581-3b40-9c41-9cb6fd958f05 | -9.12986 | -47.12461 | 2025-11-15 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97c121c1-e3d9-3ff2-87d7-e9b59e1be712 | -2.8578 | -51.28338 | 2025-11-15 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 971078da-c415-3b0a-9c74-ad11ee996917 | -1.86988 | -50.96326 | 2025-11-15 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca3dccd0-8745-3cdd-8eaf-c15fbce0960d | -5.74143 | -42.72509 | 2025-11-15 04:25:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 77509252-1877-3e1c-bcdb-40a6f15eb854 | -4.2232 | -51.20408 | 2025-11-15 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20e60f30-465e-3cdb-91d4-8cdaf3b51333 | -4.00157 | -47.67411 | 2025-11-15 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 9786482c-72b2-3a00-9a8c-17d6fcc2678c | -1.33983 | -54.61194 | 2025-11-15 04:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 081223ba-f74c-39a1-81b5-ea26e143bfe4 | -4.47502 | -46.62752 | 2025-11-15 04:25:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47f0163b-ff4c-365e-87f8-9cd28095df0e | -4.00103 | -44.17459 | 2025-11-15 04:25:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f75eac3c-5eaf-372a-bca7-ea00c269a41d | -3.13848 | -49.23737 | 2025-11-15 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 283ce6af-9bae-3f90-ae33-b9058d75b89e | -3.99158 | -44.28001 | 2025-11-15 04:25:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1379217-cbdf-347c-9b64-88e1ee399a46 | -2.71614 | -47.39964 | 2025-11-15 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97ccb894-0c87-3e25-8d33-dde96e4ab24f | -9.66135 | -43.90334 | 2025-11-15 04:25:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| aa6b68fa-a8af-3e43-a28f-89b6314f9863 | -3.08253 | -49.5145 | 2025-11-15 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 921acb5d-d6df-3e4f-8c75-cc6fdcd14221 | -1.33943 | -54.60885 | 2025-11-15 04:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8665a952-7670-3dd3-b06a-7a75af995b08 | -4.10197 | -47.28592 | 2025-11-15 04:25:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 39bbf686-db57-3e46-8930-4ac3cc8f47c1 | -5.74155 | -43.04214 | 2025-11-15 04:25:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f9c7da33-9ad0-388d-99cf-14c690bf3e4d | -5.42239 | -43.25866 | 2025-11-15 04:25:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e760bde7-ced2-3804-8eff-7bd30b5b2c25 | -3.47075 | -45.65145 | 2025-11-15 04:25:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af694659-226d-3719-9006-553c3f90eabf | -7.07743 | -41.58369 | 2025-11-15 04:25:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| a02760fb-2811-3a6d-a72b-3f62e3881993 | -5.33713 | -43.04056 | 2025-11-15 04:25:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ee87c623-b35f-39d5-b29d-6c169b149317 | -6.1095 | -44.22242 | 2025-11-15 04:25:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 49e016d5-d453-3c94-a14c-f4987d4b99ff | -3.9358 | -42.74205 | 2025-11-15 04:25:00 | NOAA-20 | PORTO | PIAUÍ | Brasil | 2208502 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f9b39c75-01ce-3dff-86fc-bc9109ce1919 | -4.15525 | -48.22499 | 2025-11-15 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b25415c-0c8f-3b79-a1bf-699fb7c8377d | -9.20721 | -44.16868 | 2025-11-15 04:25:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4865a628-c7ce-3dc2-9488-4896351956c9 | -5.50776 | -40.54886 | 2025-11-15 04:25:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| fbc1ded8-fd3d-34ca-ae6f-8d4cc63f8aa3 | -1.87051 | -50.95937 | 2025-11-15 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9439c92-22ae-3e23-b035-1b1a11aead91 | -5.99772 | -45.39721 | 2025-11-15 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9cf101c4-66c6-3614-861e-3a531851dcad | -4.84083 | -44.76098 | 2025-11-15 04:25:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README36.md)
