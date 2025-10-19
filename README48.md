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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4ad431a9-58e7-32db-b2af-e99f127e0eb4 | -8.31436 | -49.48683 | 2025-10-19 04:32:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 668bf828-23fa-34bd-a334-72f93a46e43f | -11.89415 | -45.44279 | 2025-10-19 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6730e2e2-a93a-34e1-af56-9e070d6252c1 | -9.24967 | -44.34051 | 2025-10-19 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e3200067-c675-3e4c-9794-e6416edd4a22 | -7.15974 | -42.38417 | 2025-10-19 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e8f5ce66-85e9-3430-b291-3f4adb1702ea | -4.83539 | -48.07938 | 2025-10-19 04:32:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0183c35b-17f8-398d-8ea9-e579edc6f15b | -9.18767 | -61.39436 | 2025-10-19 04:32:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e809818a-badd-3bde-bbc2-929e11a04fed | -5.782 | -44.88692 | 2025-10-19 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a5ac1b2-a654-3901-be4e-29798b17d2f9 | -9.984 | -47.05863 | 2025-10-19 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3e2ea19-d536-3003-80fd-5e505b5fe35e | -5.67502 | -47.99131 | 2025-10-19 04:32:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 252759a4-abe0-3bc1-83da-d0974d8087d5 | -5.23711 | -50.95233 | 2025-10-19 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd5a4e4e-7708-33cd-8caf-20860a37fd89 | -7.65641 | -46.66106 | 2025-10-19 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c6cae5bc-3ab8-3f1d-b745-9903ebc043c5 | -7.97786 | -45.8855 | 2025-10-19 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5bb84b22-76fe-36ea-98b5-d1ce47f07feb | -11.65197 | -47.31802 | 2025-10-19 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 51ba1180-a72b-34f7-b7e1-cfa759fc99b8 | -11.87699 | -45.45786 | 2025-10-19 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a9e1942e-5780-346f-8cda-cf5cd1a08456 | -9.2262 | -46.0583 | 2025-10-19 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f681f78-78be-3a5d-9142-872ceab98364 | -9.72144 | -48.91451 | 2025-10-19 04:32:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 40ecb5d1-8729-3380-9704-ec4a1be771cd | -8.36072 | -46.20016 | 2025-10-19 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b0c5981-7b64-31c4-8ab1-190762c030da | -10.3614 | -47.47436 | 2025-10-19 04:32:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8101a86-0eaa-3c72-8da7-098a8c4bfc73 | -9.71474 | -43.37925 | 2025-10-19 04:32:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 93587076-2460-3064-be1f-5a420842695d | -11.34929 | -44.28437 | 2025-10-19 04:32:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4847c0e-2811-3c68-91fa-e9682b417b35 | -9.21618 | -61.83611 | 2025-10-19 04:32:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 41c90d71-f742-3b9c-b015-e2b6c7b427a3 | -5.95819 | -44.19545 | 2025-10-19 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b14a67b2-df34-3255-ba86-4f25723a518e | -5.30748 | -44.79448 | 2025-10-19 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1601d870-1aea-3f03-a3eb-c9395c1c3cfa | -10.75322 | -46.15319 | 2025-10-19 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b9075a10-50c1-38a4-8b5d-ef7c9a4f1367 | -10.6781 | -47.42095 | 2025-10-19 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 33e48fad-b941-3947-b6a7-78eacd144ae0 | -8.0786 | -47.09387 | 2025-10-19 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4694912-48f1-36e2-ad2e-7cf7635183ae | -5.87064 | -44.85075 | 2025-10-19 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0366c94-0fe1-3100-87aa-01daa9ec6660 | -8.04424 | -41.10553 | 2025-10-19 04:32:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6c01e787-fe0c-3563-a71b-0c551bb0e7b8 | -7.31352 | -42.46264 | 2025-10-19 04:32:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1c28c38a-840a-32ef-be0f-f67435695944 | -12.65771 | -41.25465 | 2025-10-19 04:32:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0e0599d1-876c-3314-9d82-83b8ed954205 | -10.36974 | -47.4647 | 2025-10-19 04:32:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4f15e3b-bb6b-3be4-b5c6-76b425c08b58 | -11.9976 | -46.77164 | 2025-10-19 04:32:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 42597132-173e-3143-a56e-fca249187b54 | -9.93407 | -47.12492 | 2025-10-19 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 391b620b-10d0-3451-801a-9646e21df385 | -5.55125 | -44.95323 | 2025-10-19 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6c0952c1-74b6-3606-893b-83e81b317699 | -9.21693 | -46.0726 | 2025-10-19 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c816482-9ffd-36cf-b3d9-925517a1c436 | -7.58474 | -46.97005 | 2025-10-19 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e07b6c8-815d-3e01-baa8-85d753cc48b8 | -7.95379 | -48.12755 | 2025-10-19 04:32:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 53cec430-3fac-3a56-928a-5d9c1cccdc81 | -8.43211 | -44.1447 | 2025-10-19 04:32:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1ef7fa38-16cf-3029-8d87-efcff47dfc5e | -10.15091 | -44.52055 | 2025-10-19 04:32:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0185d6d9-e5d3-3ba9-906f-cd5a882d1e48 | -8.64939 | -47.06993 | 2025-10-19 04:32:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b4d6de3-22ab-30d9-91bb-b162518ebee9 | -5.77893 | -42.72593 | 2025-10-19 04:32:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| bbaa22fe-1321-3b82-8660-55b95e514a70 | -7.41796 | -40.06892 | 2025-10-19 04:32:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 289c1a05-8e7a-3ac9-ab09-445c08376035 | -8.25153 | -44.00843 | 2025-10-19 04:32:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f04c08fa-98ab-38b6-b728-64e99b6272ce | -6.7636 | -44.97027 | 2025-10-19 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f5c59735-d942-39e4-a97b-38cdc7ebeb3f | -12.14568 | -45.06886 | 2025-10-19 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9f163ea8-d8ad-3c5b-bffd-1f8c55776037 | -7.02511 | -46.66235 | 2025-10-19 04:32:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a3333e5-85a2-303e-953c-cae76dae03e2 | -6.60301 | -48.05386 | 2025-10-19 04:32:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c47e86e9-fd15-3642-8762-14ad8ea4e37d | -4.96733 | -56.26278 | 2025-10-19 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c2502f88-d017-3b26-ae84-666b292ba875 | -5.6029 | -43.64624 | 2025-10-19 04:32:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 12be00a7-3517-32d2-baa4-345f349953b5 | -6.10551 | -44.85166 | 2025-10-19 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c6224122-1c81-3573-91ea-5f7e7a310590 | -7.28402 | -45.40325 | 2025-10-19 04:32:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 29cbd9a8-e965-30ea-b8b7-b43ae0600d7a | -6.72133 | -46.31889 | 2025-10-19 04:32:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90f1eca6-b38a-3808-8388-7d38fba31f69 | -12.14503 | -45.07343 | 2025-10-19 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c58df740-a321-3ee6-9b73-2ac561f82850 | -12.32317 | -43.43627 | 2025-10-19 04:32:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fb688f32-cc0f-3790-9b23-729999073007 | -5.89389 | -44.76898 | 2025-10-19 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e5ecc5e-2986-3cc0-b2b9-1092ce16af9d | -8.44439 | -44.16555 | 2025-10-19 04:32:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f61ecade-145f-3f0c-8cb0-f8fcf456bc31 | -9.05079 | -49.51287 | 2025-10-19 04:32:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8ed00302-685d-3d8c-8352-beabf6006582 | -5.71311 | -46.45179 | 2025-10-19 04:32:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1663fc1a-c270-3e8b-9734-89c2fbc36701 | -5.77026 | -42.72967 | 2025-10-19 04:32:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c02ec93a-d346-394d-b864-9a0717bb4169 | -10.1351 | -44.52323 | 2025-10-19 04:32:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c7102a16-a8db-3fb3-ad41-c185c65667c0 | -10.68393 | -44.54541 | 2025-10-19 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8c0579e2-67be-3a10-87cd-a120d56a8842 | -8.54041 | -50.08277 | 2025-10-19 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b95d52a-9394-3d2b-b108-2d3587f58f35 | -9.62552 | -49.13272 | 2025-10-19 04:32:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bec03044-ba69-3209-8857-d1950e570aca | -6.96136 | -46.98455 | 2025-10-19 04:32:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ca9bb9a5-6de0-3d25-9352-579205c0d769 | -7.80293 | -46.79274 | 2025-10-19 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa4f33b7-2410-3594-b721-7a7b52f5d516 | -6.37298 | -45.75842 | 2025-10-19 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9406d13d-a8a0-3704-90c4-64413e0abf6f | -8.58924 | -49.52695 | 2025-10-19 04:32:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5cf8568-bffb-3cec-8abb-8690d5a51f1f | -5.88833 | -44.6857 | 2025-10-19 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0595ada-6536-397d-86c5-3f631b88af9c | -7.42048 | -40.07067 | 2025-10-19 04:32:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1c3cae31-77b8-3667-b63f-3de9448f2056 | -7.83707 | -41.75245 | 2025-10-19 04:32:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 43cd3746-61f3-3cd7-b75a-a9c99b8e8121 | -12.47053 | -45.43434 | 2025-10-19 04:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8634d9e3-6434-3095-a14e-549c4981be48 | -8.43519 | -44.14985 | 2025-10-19 04:32:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3b018bb8-d6c0-31ae-872a-3b0757412ed9 | -9.60304 | -49.01733 | 2025-10-19 04:32:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6d2f6de-5f30-34e7-bfce-2403891f995c | -5.3563 | -47.21243 | 2025-10-19 04:32:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 91e3d4a9-7115-3dd8-ad07-880fa40666eb | -7.49853 | -42.13655 | 2025-10-19 04:32:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bea689d6-faca-366c-b924-6b7c21241bb5 | -7.15614 | -42.37992 | 2025-10-19 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6eac900e-3cee-33ed-b7d2-710ece770683 | -10.93965 | -50.10986 | 2025-10-19 04:32:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 353eb9b8-2619-3e12-afbe-63a266b7221c | -10.89015 | -46.0805 | 2025-10-19 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 9abecf5f-893a-3235-ab22-b9f69f728fbf | -6.85458 | -46.92811 | 2025-10-19 04:32:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a6f3681-9003-3a35-ad4d-a68bc7d9c2d7 | -5.17292 | -46.10815 | 2025-10-19 04:32:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 277c4c12-10f0-376c-b5f5-49e5b0302050 | -5.99658 | -42.79878 | 2025-10-19 04:32:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e517b066-1c9a-3647-9980-4c7e319faf10 | -10.9539 | -45.469 | 2025-10-19 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| be9520d0-81a4-35f4-aae3-25c39919f4f7 | -5.17572 | -46.11224 | 2025-10-19 04:32:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 545117de-cd59-3f4e-956d-27ecdfabfe86 | -8.43993 | -44.16958 | 2025-10-19 04:32:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f32b74de-7012-39fa-aae4-5e86bf93e4c8 | -9.92876 | -47.66143 | 2025-10-19 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 15e42d60-ca1b-35ec-ab99-ea9f4acc096c | -10.42561 | -47.73939 | 2025-10-19 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9c5e309-4e7e-35a2-a813-024438e7c995 | -10.70305 | -45.31845 | 2025-10-19 04:32:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cedf2876-438d-3ef4-a9d7-68c08e514aaa | -5.36852 | -44.93946 | 2025-10-19 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dfaa5675-2e57-37e7-acb1-6e2ca920b5ec | -8.55879 | -49.55554 | 2025-10-19 04:32:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9598d076-c7e6-39c7-a7ff-12cdd6bb162d | -9.90494 | -45.95431 | 2025-10-19 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ebe8d5f2-786f-3b73-8992-a93bfdded896 | -10.88956 | -46.08448 | 2025-10-19 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 4d5f4eb0-7920-3769-9c3f-fd049b0c6f1e | -7.19813 | -42.21099 | 2025-10-19 04:32:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b39a7a68-f90f-3d1a-91ae-8cc7f2d30697 | -5.60919 | -42.73899 | 2025-10-19 04:32:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 46e85ae0-8a30-3ea6-9336-72a01db4b463 | -8.24774 | -44.0079 | 2025-10-19 04:32:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 98f3a0aa-41d0-33c1-9f4a-dd63aed33ff6 | -5.9278 | -45.44352 | 2025-10-19 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e2f40311-b06b-3288-8e1e-6d1f680b6226 | -10.6884 | -44.54126 | 2025-10-19 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb67a158-db6c-3b40-a590-4d6226adf3c4 | -7.23312 | -46.85393 | 2025-10-19 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d06514d-fc5f-33ff-b7ee-7095d4e9418f | -9.61851 | -49.02704 | 2025-10-19 04:32:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2aad7429-c0e6-3413-addb-4983fbe89b64 | -9.21524 | -46.0605 | 2025-10-19 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c4217563-1f53-3396-9383-2d0c15a58b9e | -10.98594 | -47.93682 | 2025-10-19 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README49.md)
