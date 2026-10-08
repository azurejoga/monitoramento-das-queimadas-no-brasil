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

## Dados Diários - Página 331

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07189b6d-b108-3a60-9a0b-20f5fa471eab | -10.43961 | -47.27932 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 1b6adc62-d678-3bff-ae92-991c4cb2a7f3 | -13.16384 | -54.32832 | 2026-10-08 16:37:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 95faa8a6-bd5e-3bc9-91a2-29fe52d5e4e2 | -6.53713 | -45.39641 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 99389359-aa0e-34fc-9c75-ceae4ba71870 | -18.86926 | -48.26094 | 2026-10-08 16:37:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7b22dfe3-4147-38e3-8b16-d5a95b6fce35 | -10.76343 | -46.58389 | 2026-10-08 16:37:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| e1228162-d713-38c1-b512-62f1f648791b | -6.18677 | -44.01951 | 2026-10-08 16:37:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e8adab75-bab6-3a18-8e23-913bf5296697 | -8.67242 | -50.20576 | 2026-10-08 16:37:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 2594d175-f3a9-3667-b7be-58901b745387 | -8.50295 | -41.25994 | 2026-10-08 16:37:00 | NOAA-20 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 41.7 |
| 42baeaa4-5073-3633-8c4a-355a017d846a | -7.98285 | -37.99715 | 2026-10-08 16:37:00 | NOAA-20 | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 19.2 |
| 47c50c07-017d-35b1-be0d-e35271a0b924 | -8.9675 | -47.56252 | 2026-10-08 16:37:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d6096b46-15ef-382f-968a-9bdc729cacd7 | -10.67474 | -47.82698 | 2026-10-08 16:37:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 999610e6-a2e9-3c57-8631-7e11a5441ce5 | -11.31586 | -46.67797 | 2026-10-08 16:37:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 3b25b648-5607-3835-bbe2-a56810126c96 | -12.51557 | -41.94296 | 2026-10-08 16:37:00 | NOAA-20 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| d464dc4d-ab12-3e06-b539-4f5dcfe2e601 | -13.11818 | -46.35582 | 2026-10-08 16:37:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 941bffdd-e31f-305d-b4be-2cd51143a31c | -8.62128 | -48.34923 | 2026-10-08 16:37:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c547297c-b4a5-3586-8147-3183bb6db7bb | -6.90138 | -44.91884 | 2026-10-08 16:37:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 330d252f-3155-3b6c-bfb2-7354fde0fbf1 | -6.32064 | -37.75033 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 0c39af88-d930-34f5-b2e8-cd7f5300d4aa | -12.50939 | -42.29018 | 2026-10-08 16:37:00 | NOAA-20 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 8c218c3f-e9cd-3d29-8fce-d72c802f211d | -10.77309 | -46.55561 | 2026-10-08 16:37:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 282d1e73-726b-3b58-ab26-0dbc8dcee889 | -6.33198 | -43.80413 | 2026-10-08 16:37:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fb193e82-cb5a-372b-99f9-4bcfa2446b0f | -11.96789 | -47.7652 | 2026-10-08 16:37:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 4fb68155-8c7f-3d02-b939-0fe4a0f90ddf | -7.53705 | -45.87514 | 2026-10-08 16:37:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 72deaa5e-8e93-362c-a44f-d8e2cea781a7 | -10.90578 | -45.54253 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3571371d-9d9c-36b8-adc9-ba6a840e2d7e | -9.90443 | -44.82533 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 7ec1d23d-49ae-3a44-9f8d-7a6f5e30e942 | -5.99128 | -40.93275 | 2026-10-08 16:37:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 30.5 |
| b81149a0-e653-351c-9f16-e166e2ebd6df | -8.81106 | -49.41968 | 2026-10-08 16:37:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 58de7636-0818-35c8-a1f4-2ea8303ac67e | -6.50336 | -42.03336 | 2026-10-08 16:37:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 27.6 |
| be0753fe-6358-3ad9-96c3-cd9472c5e0f1 | -11.59426 | -43.66048 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 5657f92a-2603-3d3a-8e67-0ed62e659b5f | -13.58965 | -48.58638 | 2026-10-08 16:37:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 28bcd645-0d6a-3248-87ee-3e97fc3e6319 | -8.93662 | -45.15387 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| f9533728-7b0a-3b1c-9b37-d7beef46a20d | -19.2302 | -40.68227 | 2026-10-08 16:37:00 | NOAA-20 | PANCAS | ESPÍRITO SANTO | Brasil | 3204005 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 9bf3e8d7-ff75-3fd7-be45-fa06c6987fe0 | -6.84264 | -41.75499 | 2026-10-08 16:37:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 75.8 |
| 2b2b2501-bdf7-3614-8d4f-0c910742edb7 | -7.53675 | -42.08949 | 2026-10-08 16:37:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 676b94a3-3682-35cc-919d-1ff759ae64b8 | -10.07187 | -45.99677 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 0a1410f0-0e4a-3dfa-b07e-b6c03b57f7ba | -10.57359 | -46.29168 | 2026-10-08 16:37:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 3a237177-afd8-35c1-bc6c-78d63291f088 | -9.35093 | -45.42183 | 2026-10-08 16:37:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b3e281eb-55f5-3411-bfa7-a3333ee24080 | -10.15862 | -39.2473 | 2026-10-08 16:37:00 | NOAA-20 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 772bacef-cccb-321c-88aa-057ba344a24c | -6.0691 | -37.02879 | 2026-10-08 16:37:00 | NOAA-20 | JUCURUTU | RIO GRANDE DO NORTE | Brasil | 2406106 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a4a7cfe7-ed15-333e-aaa8-ad946f023d3b | -12.24344 | -44.74379 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 771c4761-0caf-3acb-91c2-7c64ff8ad67c | -19.06433 | -48.63919 | 2026-10-08 16:37:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ce7dd6ed-670f-3716-83dc-50016640c532 | -8.93715 | -45.15735 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 742ef8f8-f9c5-3c58-b0c0-a4db22ec27e7 | -8.28798 | -45.72714 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| d7d135e7-97ad-3636-8ae1-3e6a1d12bcc4 | -8.88516 | -45.39319 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 4d8e2248-20f4-3b9c-921e-c02ad9f7741d | -8.99322 | -42.33937 | 2026-10-08 16:37:00 | NOAA-20 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| fc8d4a41-db05-32c9-8d05-79af09d44707 | -11.06893 | -54.51366 | 2026-10-08 16:37:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 48b2711e-9302-33da-98af-3168c80e7004 | -12.18597 | -44.65567 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 12540287-7b84-32ae-a8b1-ee824a70ee95 | -9.77775 | -45.88779 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 0d9276ba-4c40-3c8f-b54c-30c4f44b4c1a | -14.32901 | -52.07411 | 2026-10-08 16:37:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 998c8225-5890-3c9a-8e9f-0de417c815a9 | -8.9397 | -45.19613 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 52.6 |
| b65fe534-7bbe-3ccf-b629-84646b62d22a | -6.75963 | -45.14345 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 1a1dc7a1-261c-3fbf-9d2b-08198dda9052 | -6.33456 | -35.12397 | 2026-10-08 16:37:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 2264f818-f870-3029-afeb-3bb5e7228fe9 | -11.71292 | -43.65925 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 436f39ff-32e7-3276-b05d-ba1a4bea914e | -11.31446 | -44.83654 | 2026-10-08 16:37:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa0cdb98-6c0a-3ea9-9d17-272e995ef9f5 | -5.70566 | -41.72876 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 74086539-e14a-355a-96db-69f87916a354 | -7.04455 | -45.42869 | 2026-10-08 16:37:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| bb4fa0e2-5bda-37c1-aa57-111e9303bc04 | -10.21637 | -48.04911 | 2026-10-08 16:37:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| cd0c992e-aa4e-3559-a02e-77b53e6a9d2c | -12.15913 | -44.74626 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| b5a9cf98-5e10-3bfe-9557-58c58bfa7e13 | -12.0289 | -43.44136 | 2026-10-08 16:37:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 59.3 |
| a3d5c4d4-7176-343e-835c-5be79228a935 | -8.8407 | -45.45768 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| cf650bec-7a69-3dc3-809f-fc133f9918c9 | -7.32383 | -39.82268 | 2026-10-08 16:37:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 35.8 |
| fac77709-6f9a-3d76-a79f-88e66718b68a | -7.62902 | -49.52887 | 2026-10-08 16:37:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| d8cef2d7-1590-3b91-9c63-21817235c0c3 | -11.45296 | -43.38738 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 40652569-4318-3de9-89f8-aec083fbc184 | -11.79106 | -46.77354 | 2026-10-08 16:37:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e51ce6c6-15aa-3dfd-904c-0580f502dec8 | -6.21405 | -43.83435 | 2026-10-08 16:37:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| dc6c37d1-be54-3511-a926-b34aefbc6be8 | -13.84895 | -44.81932 | 2026-10-08 16:37:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| cdeb5ebb-11b3-30bd-9aed-08163ea3b98b | -18.27656 | -42.62449 | 2026-10-08 16:37:00 | NOAA-20 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 411c6da4-7840-3230-ae4b-9f69533d5f40 | -13.69277 | -49.11692 | 2026-10-08 16:37:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 49cba684-83c1-330e-9dba-a72bb7063db3 | -6.69387 | -44.95971 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 681f5eb7-faed-3c09-a89a-d4350cbc084d | -7.53377 | -42.09446 | 2026-10-08 16:37:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| a9713407-b82a-3d78-bd8e-35de7fc2d501 | -6.69653 | -45.28532 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 8acf859f-16de-3cca-80e2-08aaa53c08c4 | -9.24699 | -45.65254 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 02d9b60d-50f2-39df-8fc0-ba705bb0836d | -7.87248 | -38.89551 | 2026-10-08 16:37:00 | NOAA-20 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 9.7 |
| cae76dfd-b2fb-3ab6-ab70-f5aa11c9fcef | -10.99102 | -45.40999 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 6a35af3a-7396-3a8b-9ccc-edf1c08856a4 | -8.33507 | -45.03674 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 8cbcf76a-69f9-36a0-aec2-1cf648ba7b2c | -6.3256 | -37.74934 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 24.3 |
| 3d53e92c-cfcb-3b0b-8e5e-e6b12c055a08 | -6.18736 | -44.02327 | 2026-10-08 16:37:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 32a6e4e5-f804-3e90-ad8a-6ca9a462f665 | -11.10725 | -41.31129 | 2026-10-08 16:37:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 68c3529f-3a78-343c-9986-4d390eff1eaf | -6.18321 | -44.10789 | 2026-10-08 16:37:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e403f25d-7710-3b4e-8885-0693f8a65056 | -7.57651 | -46.69962 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 84a68e17-0f1e-39bd-b332-3c364ad651f4 | -11.76839 | -45.52876 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3dee0786-47ff-3019-8a60-bc182db05b17 | -6.88943 | -45.90069 | 2026-10-08 16:37:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| e6616be3-d7c7-39b8-8fca-a56f6fa13372 | -8.29301 | -45.7157 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 110.3 |
| a77a05dc-cfc9-3b66-bc5c-8f065f06d1df | -8.0735 | -39.56679 | 2026-10-08 16:37:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 8fb6c635-9530-3d6c-9030-6a8b18804331 | -6.50825 | -42.03417 | 2026-10-08 16:37:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 32.4 |
| c208b3ea-ad79-37f6-8f1f-7cc326f48946 | -6.98416 | -43.9653 | 2026-10-08 16:37:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e7b10834-b35e-3de4-ac0e-40ad5981bb3d | -11.08194 | -44.03387 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 7ea8bf0b-243e-3fa2-ad60-7fcf8528c8cf | -7.40618 | -44.44931 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f59346bf-dee6-3649-8e69-c86e0a23bc58 | -10.45809 | -47.28455 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| a0ebcb59-34b1-3888-bdbf-3b291ed833b2 | -7.74276 | -45.44515 | 2026-10-08 16:37:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 23a49a19-b05f-3b53-955b-5a85b5224c7a | -11.11026 | -43.99659 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 604e0040-3174-3e27-8af8-e3e2fc7d03b7 | -6.67255 | -45.37164 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 3cd35804-c46d-3e9c-8709-77f4d13519fb | -5.81803 | -42.50377 | 2026-10-08 16:37:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 221140f0-a67c-3fc2-9cac-c28eed36fd51 | -6.63237 | -44.89348 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 44df952d-fc86-3398-8a2c-9ec9f0f213c2 | -6.75159 | -46.89637 | 2026-10-08 16:37:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 0d499aa1-c2c6-32bd-9e90-8e2308d2f4cd | -6.43113 | -44.82061 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 05444da6-c12c-301d-8816-ad197acfc103 | -8.08371 | -55.2969 | 2026-10-08 16:37:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 98b1fa81-71e5-37fa-80c3-7b553c3c14e0 | -14.65546 | -54.97074 | 2026-10-08 16:37:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5543d0ef-28f7-3c6f-88d5-a3208008d11b | -10.8177 | -47.33888 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e8620985-9c34-3ddc-880c-b5c9c037b66e | -9.02698 | -44.3734 | 2026-10-08 16:37:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 20.5 |
| a12359b0-de41-31ad-b3d3-c511c3bb290f | -7.98366 | -37.99998 | 2026-10-08 16:37:00 | NOAA-20 | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 15.6 |


[Clique aqui para ver as próximas entradas](README332.md)
