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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e2c8ecb6-eb0e-3628-af38-f91a67fd0c39 | -5.80268 | -39.07123 | 2024-12-23 00:24:00 | TERRA_M-M | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 9bfffba2-b256-3de8-8b6e-c40ab6105bf2 | -10.1443 | -36.27736 | 2024-12-23 00:24:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 3cb16b89-2342-3b11-b12c-2736ebcc3ea9 | -4.51764 | -42.97095 | 2024-12-23 00:24:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 1c8a68b8-0e6c-3ec0-acc9-c7d4c02e3dc2 | -4.06634 | -44.11405 | 2024-12-23 00:24:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 449c01c5-d5dc-3951-9020-187f34267a94 | -10.62702 | -37.01653 | 2024-12-23 00:24:00 | TERRA_M-M | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 000bc734-18b2-3ae6-8e42-e52c197adc45 | -5.80421 | -39.08188 | 2024-12-23 00:24:00 | TERRA_M-M | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 6f929ee7-d0ba-3a80-99eb-f91ada2e062b | -4.10226 | -46.63049 | 2024-12-23 00:24:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 821e6c01-67df-3fd9-8e06-ef4f38683d78 | -4.6256 | -43.61611 | 2024-12-23 00:24:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bf5da4bd-71aa-3599-9883-d3c575346e4f | -11.64951 | -43.87948 | 2024-12-23 00:24:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 76e5148b-d471-3950-b7c9-fec146dd59f7 | -4.15186 | -43.65472 | 2024-12-23 00:24:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 197.0 |
| 6faf5844-ee6c-30c2-8af7-c730c261a776 | -7.17598 | -35.03761 | 2024-12-23 00:24:00 | TERRA_M-M | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| f6809a68-6330-3fb0-883d-291da9447f99 | -7.17823 | -35.05096 | 2024-12-23 00:24:00 | TERRA_M-M | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 32.7 |
| a429c62d-5135-3735-9271-8ab93502267d | -4.15316 | -43.66415 | 2024-12-23 00:24:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 0a434164-8373-36ae-8d6a-2f21b4254bc9 | -11.96946 | -44.24924 | 2024-12-23 00:24:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d6c161c9-fad5-3779-93f6-03c16b3c8aad | -11.9679 | -44.23658 | 2024-12-23 00:24:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 5c3a842f-ec72-3ec0-ab85-a47d1f59bd6c | -7.24292 | -37.43071 | 2024-12-23 00:24:00 | TERRA_M-M | MÃE D'ÁGUA | PARAÍBA | Brasil | 2508703 | 25 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 15bd9a00-d83c-36d4-a09c-d5db460d89f0 | -4.18782 | -43.65298 | 2024-12-23 00:24:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b39158a6-2655-3608-8cc0-98caa37884ea | -6.18212 | -42.62172 | 2024-12-23 00:24:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 1a47262d-c1fb-3cb2-8701-443282c1f50e | -7.24483 | -37.4438 | 2024-12-23 00:24:00 | TERRA_M-M | MÃE D'ÁGUA | PARAÍBA | Brasil | 2508703 | 25 | 33 | nan | nan | nan | Caatinga | 7.5 |
| a4cbaabf-1631-319f-8dce-482864dca49b | -3.51505 | -47.20214 | 2024-12-23 00:24:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| f1312c05-471c-325b-baea-c64a70b682f6 | -3.98216 | -46.3448 | 2024-12-23 00:24:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 4351e7f7-3dec-37a5-b4f7-21db4b534529 | -5.44605 | -44.80461 | 2024-12-23 00:24:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 23f741de-ff19-337b-8bb3-426fb14e7b7b | -4.43816 | -46.32076 | 2024-12-23 00:24:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 519a53c6-f5a8-3b90-b122-2026dee4f62f | -3.54476 | -43.59457 | 2024-12-23 00:24:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 0ce79b3b-0e2e-347d-aa5a-e31f6993ce3a | -10.53493 | -36.94804 | 2024-12-23 00:24:00 | TERRA_M-M | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 22.3 |
| b2d43239-c850-3a91-a012-e2ab5a7862d5 | -8.99978 | -36.10043 | 2024-12-23 00:24:00 | TERRA_M-M | SÃO JOSÉ DA LAJE | ALAGOAS | Brasil | 2708303 | 27 | 33 | nan | nan | nan | Mata Atlântica | 19.3 |
| 4a1d6090-29f2-3694-b86a-3583b03f1970 | -7.23435 | -37.44598 | 2024-12-23 00:24:00 | TERRA_M-M | MÃE D'ÁGUA | PARAÍBA | Brasil | 2508703 | 25 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 0ea1b93a-5dc6-37e1-8715-dc066592729d | -4.7834 | -46.40362 | 2024-12-23 00:24:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| abe84005-98fc-3fb9-83a4-825e0546e164 | -2.68331 | -42.69016 | 2024-12-23 00:24:00 | TERRA_M-M | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3e216074-38ae-3757-9a8e-11242d5d1c7a | -4.14402 | -43.66543 | 2024-12-23 00:24:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| e48932f7-2b0e-3183-ae52-9a8f6b2a1ef3 | -4.18654 | -43.64357 | 2024-12-23 00:24:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 180.9 |
| 97a53fe3-6b56-3162-8937-80966e2a03ca | -4.15056 | -43.64533 | 2024-12-23 00:24:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 6123c78d-9f19-3744-bb97-86821ad63a00 | -4.07433 | -44.10294 | 2024-12-23 00:24:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 49ae9b4c-e2fc-3598-8ab5-e5ebcbd545f3 | -3.5016 | -47.18887 | 2024-12-23 00:24:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| c9d727e4-83bc-3507-84d0-5ff1180f9b22 | -10.54719 | -36.9588 | 2024-12-23 00:24:00 | TERRA_M-M | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| 67aa080b-0c6d-3677-ae40-343718b5d683 | -12.45289 | -41.43826 | 2024-12-23 00:24:00 | TERRA_M-M | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 2b238203-5739-3669-83cf-535b6277345e | -5.45741 | -44.81441 | 2024-12-23 00:24:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 2cebfeba-cf20-3251-80f0-f08bcfbcc8f1 | -4.18525 | -43.63412 | 2024-12-23 00:24:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 1934303f-d69f-3c32-9bea-ad814490e5f0 | -3.894 | -44.06038 | 2024-12-23 00:24:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| c86593dd-5f0a-3cf1-b3f4-906ef7e12d7e | -3.64303 | -40.47326 | 2024-12-23 00:24:00 | TERRA_M-M | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 814e96b2-684b-36ea-bddc-c56e7ffcf5bc | -6.00628 | -45.41331 | 2024-12-23 00:24:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ce8dd64e-0b52-3cf1-aef8-8fbdfb9c8d22 | -4.07567 | -44.11275 | 2024-12-23 00:24:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 4b6451d8-d277-39c1-8e5e-d574a145d937 | -9.83246 | -36.35289 | 2024-12-23 00:24:00 | TERRA_M-M | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 35.5 |
| 73d539e9-fa0e-335f-9850-316ccfb4cd9d | -4.10551 | -46.82059 | 2024-12-23 00:24:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 730523cf-b4a4-32c5-be3c-aa642e6b872a | -3.54349 | -43.58526 | 2024-12-23 00:24:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 1a0de17e-c508-3176-9662-a1ea778b42eb | -3.37151 | -44.0707 | 2024-12-23 00:24:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| aa692d58-e160-30d4-9fc5-886b02d1ccbf | -3.51302 | -47.18723 | 2024-12-23 00:24:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| d3b72ab0-07ff-35f8-956a-a756a28f2a47 | -3.75472 | -47.1981 | 2024-12-23 00:24:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 0e573d8a-386c-3d4a-9b75-279d132824c2 | -4.72285 | -43.25629 | 2024-12-23 00:24:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 3078d4d7-6343-38cf-aea1-b6d0fc5cf5c3 | -2.68453 | -42.69899 | 2024-12-23 00:24:00 | TERRA_M-M | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 381c3976-a1cb-36b3-844c-2d83781f476a | -4.15969 | -43.64402 | 2024-12-23 00:24:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 4416af04-9d4b-37f9-b081-49852baff429 | -3.89267 | -44.05064 | 2024-12-23 00:24:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 6e42c798-1233-31bb-b555-19b4fe7e8c10 | -3.29776 | -45.61095 | 2024-12-23 00:24:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 54a35ae1-ff16-3c93-882a-c3db32050f61 | -3.98529 | -46.33829 | 2024-12-23 00:24:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f4832d0f-aaa1-3f70-977c-53ddc61b858d | -4.87557 | -37.82505 | 2024-12-23 00:24:00 | TERRA_M-M | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 10.6 |
| d5831f5f-1f5b-3caf-a5d8-b074c7eb4aaa | -4.05413 | -38.79141 | 2024-12-23 00:24:00 | TERRA_M-M | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 20.0 |
| 0586412c-5b97-32ee-b51c-b4b84b41ab7e | -4.23481 | -43.79179 | 2024-12-23 00:24:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b04c50b4-99f5-35f5-88dd-c23703089d74 | -12.45539 | -41.45678 | 2024-12-23 00:24:00 | TERRA_M-M | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 09513ca8-7391-36d6-aac8-cf86dee24ee9 | -3.88147 | -47.28593 | 2024-12-23 00:24:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 036dc851-7350-3c7a-b87f-a31c90ac5a99 | -4.3229 | -43.97067 | 2024-12-23 00:24:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a4066904-3503-3f1d-b5d4-d94c30bc9b2f | -7.17895 | -35.0574 | 2024-12-23 00:24:00 | TERRA_M-M | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 23.2 |
| 83f54927-42c7-32e7-b9e8-302cff337073 | -9.09096 | -40.88707 | 2024-12-23 00:24:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 4d0edef2-8eb6-3a85-a766-5f3901f9cecd | -4.32457 | -45.88375 | 2024-12-23 00:24:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 11eb0175-e6b2-3e01-9932-1d1e12c68bdf | -4.0557 | -44.10553 | 2024-12-23 00:24:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 929ac2d8-a30e-3ad5-8b50-09714ac3431c | -10.11838 | -36.41774 | 2024-12-23 00:24:00 | TERRA_M-M | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 26.3 |
| e499801f-4f67-39ad-ba1a-aca86d6e65de | -3.63266 | -45.06351 | 2024-12-23 00:24:00 | TERRA_M-M | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6e6cf9d0-b463-376c-8842-676b8e07e2cb | -4.94534 | -41.34602 | 2024-12-23 00:24:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| e5bc18c3-cc79-3a54-92d4-19f594b70ac7 | -4.44093 | -46.31468 | 2024-12-23 00:24:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 3c2bc4a7-373e-3f76-a6c9-0984ec4d2225 | -3.50366 | -47.20406 | 2024-12-23 00:24:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 73bec040-cb23-3957-bddf-1d0fa242e9b3 | -10.61673 | -37.01832 | 2024-12-23 00:24:00 | TERRA_M-M | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 2c7e704e-6d46-3441-97dd-b6a3890dcfe9 | -4.47834 | -45.42937 | 2024-12-23 00:24:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fac0703f-126d-3222-b73d-3700dfb76f60 | -5.24963 | -41.40529 | 2024-12-23 00:24:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| d439f228-edbd-3eab-8b15-d6e2ff9a0735 | -3.64441 | -40.48288 | 2024-12-23 00:24:00 | TERRA_M-M | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 96acb3b5-508e-38bd-87ef-5e818b62fc31 | -10.1421 | -36.26318 | 2024-12-23 00:24:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 116.4 |
| cb851a63-08e5-3108-bc5b-3c7b784b0926 | -4.17868 | -43.65424 | 2024-12-23 00:24:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 179.2 |
| 552b83a8-396c-3f44-8415-1dcfa861b59a | -10.5453 | -36.94638 | 2024-12-23 00:24:00 | TERRA_M-M | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| df47b727-63f4-31f7-9b22-b1814e3dc8dc | -3.71068 | -43.59729 | 2024-12-23 00:24:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 06e024fe-45fd-3d84-9008-10f8d9d6fe8b | -6.17192 | -42.61393 | 2024-12-23 00:24:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| e1179ddc-7af5-3076-828c-e2b23efa3fc6 | -10.53683 | -36.9605 | 2024-12-23 00:24:00 | TERRA_M-M | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 50.1 |
| 0f28c0e3-911d-31c9-ab8c-c9d1712e3e0e | -4.00688 | -46.33563 | 2024-12-23 00:24:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| e2e12d08-6706-308a-8206-08aebd68b172 | -4.1774 | -43.64482 | 2024-12-23 00:24:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 44081d09-0d2e-39a5-b10f-ec58e770e1a7 | -9.18377 | -43.11975 | 2024-12-23 00:24:00 | TERRA_M-M | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| b2900a4c-3ca3-33b3-8c35-ed75fcde011e | -4.25442 | -46.81824 | 2024-12-23 00:24:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c02a500d-7f0b-3789-95b7-5f6ed80e7b68 | -3.83349 | -41.5597 | 2024-12-23 00:24:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 3c1687fd-1134-3a6b-b232-90aa09d87734 | -12.44512 | -41.44872 | 2024-12-23 00:24:00 | TERRA_M-M | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| f994471a-f05a-3ed3-8889-a0ba11d2760f | -5.45592 | -44.80327 | 2024-12-23 00:24:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 72f87829-5e23-347d-af7a-f1458f0221c0 | -6.18088 | -42.61264 | 2024-12-23 00:24:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| ef30286d-cfd5-32ad-9ac1-2ffa25c136af | -6.00791 | -45.42566 | 2024-12-23 00:24:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 02f87ab4-cb5b-3a9e-98d7-445069624dd2 | -12.41432 | -43.80776 | 2024-12-23 00:24:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 24beda28-b252-30b4-9a09-37b923f88305 | -4.16099 | -43.65345 | 2024-12-23 00:24:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 59f06fea-a514-3ea3-9c74-f234591e6032 | -4.08108 | -46.80861 | 2024-12-23 00:24:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 5e53baaf-48a4-3098-98d5-a6934fc56f77 | -5.05998 | -44.23209 | 2024-12-23 00:24:00 | TERRA_M-M | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| daadf2e2-244e-37b0-9ab2-43d989fa508c | -4.17612 | -43.63543 | 2024-12-23 00:24:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d9db5150-c9f3-3eaf-8323-b05c55422b71 | -3.18257 | -43.24045 | 2024-12-23 00:24:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4bc3c244-3615-3e24-aca2-35a96fb1b967 | -5.44752 | -44.81569 | 2024-12-23 00:24:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 76530d33-4cee-30ad-b434-9578e9a0cfaf | -5.61007 | -35.34749 | 2024-12-23 00:24:00 | TERRA_M-M | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 25.7 |
| 4d6ab513-ba59-3d9b-9163-d13ce046db75 | -5.37128 | -43.08539 | 2024-12-23 00:24:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| cc679dc4-8cef-39ff-aad8-3aa6bf56ae37 | -12.44389 | -41.43953 | 2024-12-23 00:24:00 | TERRA_M-M | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 22.0 |
| 1bd97ee0-0c62-3d76-9637-4d9a4c0238fe | -3.35414 | -47.11343 | 2024-12-23 00:24:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 7406fd95-9fd0-3946-9ca6-d3f825e89c8c | -3.92158 | -46.90203 | 2024-12-23 00:24:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |


[Clique aqui para ver as próximas entradas](README3.md)
