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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea2c674e-12a3-3d9e-98eb-e9efa3173a9b | -1.48448 | -54.51653 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8a3856b8-b5bc-3a43-8a48-2776121626ce | -2.75815 | -54.10901 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 537ff257-3620-3816-9c81-2f3821d2ce48 | -3.21153 | -50.55263 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0bf77c01-6a99-3901-bf79-df0a40ccecd1 | -5.72523 | -41.61468 | 2026-10-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 243329b8-1294-3a40-8ed0-b28df6b1420c | -4.05061 | -46.90651 | 2026-10-09 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 49f42b4c-e4f9-3f8b-b6f1-0458fbcb2fdf | -1.15361 | -54.23058 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4bf9a550-7452-37f4-936d-115683abf1d4 | -6.71242 | -44.11735 | 2026-10-09 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0eb403c5-1f3f-3773-8db4-79aa47e0ac9c | -3.56328 | -54.664 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 57688626-ec50-3ab6-adc1-fe3ff7204eae | -2.99742 | -54.06125 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f36ec8c5-c6e1-3cfa-b457-9949d38a68d1 | -5.09229 | -46.21074 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba001f61-06b3-39e8-9e34-5cbe9d48e11a | -3.29093 | -51.54075 | 2026-10-09 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 05fd5c1d-2e28-3484-9af0-3dae81bf87ff | -5.95471 | -40.93403 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 23008942-f691-3ff1-a8df-266f6e2312cf | -1.19504 | -54.2077 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f58e5a8a-1e3b-340f-bd0c-c005a2af8b78 | -4.93817 | -49.21665 | 2026-10-09 04:25:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5d5d8c98-32c7-3d72-8ea2-ecce88589d61 | -2.99913 | -54.08272 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1486e72a-9a90-354c-8819-996aeafc6408 | -3.01637 | -54.09739 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 37b299e2-31a0-3bc0-80b8-3f66825d0b47 | -3.42372 | -54.06377 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf3377cd-62a9-374d-afce-3fe93c681184 | -3.31355 | -54.70347 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 854cef5c-a630-31fe-a3e8-6f81a9aab002 | -5.75649 | -43.85196 | 2026-10-09 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 11df5c98-1a5b-3014-b62d-fe1b13144c2a | -4.84396 | -44.0905 | 2026-10-09 04:25:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 58d9285d-9d3c-3a72-a335-4d5553216b95 | -3.00974 | -54.07515 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8bf0f5b-8516-3d43-b7ec-e12229c55069 | -6.01125 | -40.98042 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 44c7123c-872a-3cfe-9816-9b6d4a23dbf8 | -6.82929 | -39.31739 | 2026-10-09 04:25:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4c2886b7-b4d6-3f92-b662-59e16423deb7 | -2.74193 | -54.1125 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b69e809e-80bd-35b6-91ca-a9be5206f79f | -1.47638 | -53.61161 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01f90e64-f543-3966-9f02-1d6078d966b2 | -6.8812 | -45.90856 | 2026-10-09 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0bfff243-5f67-3ca1-8001-401a2e57ebb3 | -5.19301 | -46.21951 | 2026-10-09 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c253a91d-2d64-3a94-8a44-ecb61fc78a48 | -3.27052 | -54.05631 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5cbc9098-c34f-33ca-8203-917237a8fb1f | -3.0974 | -54.28957 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ec0ccd5-ccba-3449-bafd-637e5848b9b2 | -3.58721 | -54.68074 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 45a26604-0f27-34b6-a8c9-d64ef80d0622 | -3.11759 | -54.16967 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 35807026-a4c5-3292-815a-069cc5842a5e | -4.15182 | -47.9865 | 2026-10-09 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 54c0308d-5cba-3005-ad1b-753bd229d5df | -3.66246 | -49.18964 | 2026-10-09 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7fd1ddd-d9aa-385a-9e22-8fa695802dee | -5.70826 | -53.44826 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec48b112-f848-32ba-8e2b-a8ed006991bd | -5.75732 | -41.64127 | 2026-10-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| dc8d5e41-5f59-3e50-aa07-9fb026f856ff | -6.88066 | -45.91205 | 2026-10-09 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b1ee6f00-6644-32f6-b2f6-dd9824c4dada | -3.53839 | -59.40108 | 2026-10-09 04:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| de4f5fa4-7e0a-3f84-9a0a-681ae3f9461c | -3.80116 | -50.61359 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3cf7aed1-0194-37d1-ac5f-1bbde1c2c581 | -2.83099 | -49.51103 | 2026-10-09 04:25:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 160448af-b31a-3112-add6-5d26c8be3f28 | -3.07784 | -53.94572 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c3206aa-f91d-3599-b71b-dea05cfc49bd | -4.74026 | -55.67506 | 2026-10-09 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e506b27a-e56d-3ceb-a5dc-9ffd0297c5f3 | -2.75401 | -49.52798 | 2026-10-09 04:25:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7256b79c-9934-365f-9195-cd304f420916 | -2.47363 | -56.06845 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| be6ef528-8ec3-300f-b7ef-96e8ffd64164 | -2.2285 | -53.69901 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e499dfd-7b23-345e-8e09-003a77cc1bc1 | -5.3789 | -45.94262 | 2026-10-09 04:25:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89b38f8c-0d2a-356d-8f2f-6bd1c4fb34f5 | -2.41217 | -56.53919 | 2026-10-09 04:25:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 45b3f469-f269-3394-8f41-33959283acdd | -2.77366 | -54.07767 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b3c6276-3dd2-388c-9c55-f6107320fa5c | -3.18437 | -58.64398 | 2026-10-09 04:25:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fea3ed48-b743-3717-a135-95ae3401c80e | -2.9364 | -54.17969 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e85ab44c-2c65-39a4-ae85-7557b14642fe | -5.37628 | -48.97665 | 2026-10-09 04:25:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed783617-1af6-3f9b-8f2f-0a144198a9ac | -3.89304 | -58.95559 | 2026-10-09 04:25:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dee68e2f-503b-3018-b29d-464acbc3ad72 | -2.99045 | -54.07227 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e49e2fa-08fc-3347-8dfa-ac20793eaba5 | -3.01331 | -54.08475 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c7688d0-4439-3efa-9a01-f60d4f445749 | -2.94653 | -40.50006 | 2026-10-09 04:25:00 | NOAA-21 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 17db1ad5-58e7-3ee3-9615-b4d59f15f3d1 | -3.20722 | -58.84724 | 2026-10-09 04:25:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3a577178-826a-390c-9103-180b9c91e7a6 | -3.02785 | -54.05993 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b30c68a7-9a4a-3272-b548-1822f7e4bb11 | -3.60448 | -54.67363 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 312412e5-2a6a-3bb4-99b7-8a4ac2cdf6f9 | -2.73536 | -54.12069 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e995a897-7770-3610-bdc7-443bb84dd515 | -5.45441 | -42.89033 | 2026-10-09 04:25:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 77ca9b2f-341e-3470-8342-9d19be6c6f8f | -5.88637 | -43.42182 | 2026-10-09 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1a1d5149-76c6-350f-b88a-a8c32ddcdcc4 | -3.12166 | -54.17649 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| b0eb7587-2fe4-3f78-bbcb-84fd696eae2b | -4.02485 | -40.64557 | 2026-10-09 04:25:00 | NOAA-21 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e54d677f-9220-39fa-a329-847270c2107b | -3.12265 | -54.17056 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 3df5b64d-1188-38ec-962d-0257a8e376a2 | -2.98517 | -48.91526 | 2026-10-09 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cfc78969-a148-3d32-8180-48c88223a839 | -6.69901 | -45.30489 | 2026-10-09 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ba8243e-31d8-3909-af8a-8e054d94eb4a | 0.50096 | -50.78251 | 2026-10-09 04:25:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 6acb6c18-25bb-353b-84e1-e88d63e27698 | -3.30501 | -53.71399 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 49cad8dc-ba52-3f88-87ab-36330165b973 | -2.50852 | -56.14521 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b04664ae-4130-32b9-bb83-392e76fe4a53 | -3.8206 | -47.48145 | 2026-10-09 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9bbe4f40-4534-3301-b72a-1f18fcd2072d | -7.40699 | -35.18864 | 2026-10-09 04:25:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| a9d80f78-c430-3680-a460-b3198054935a | -3.58823 | -54.58031 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 482d5212-a8db-3d20-8181-c0a1b9cb2e82 | -1.11407 | -54.17433 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 00398066-3758-35df-9a03-46d54e8ac6e6 | -3.5689 | -54.69389 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 6b30748a-55bc-34e6-ac37-f900c8872cbd | -6.51337 | -47.3899 | 2026-10-09 04:25:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6197c247-2e0a-3e5c-9bba-24d2d19f8e1d | -5.25401 | -44.64072 | 2026-10-09 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7194bda6-6ea9-3238-a819-9d4514583132 | -3.271 | -54.05342 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e2b4fda-b0c9-3360-8773-89253e589744 | -6.00353 | -40.97563 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2554ae92-0af3-3fa7-b03f-129ae0973901 | -7.18749 | -44.27348 | 2026-10-09 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 07b1535d-2eee-3d41-a37d-ad4085300533 | -2.86531 | -40.01003 | 2026-10-09 04:25:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e06499e6-b653-3416-8f98-d13d6b0dc1b2 | -2.98805 | -54.08706 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| df02cf60-a0cd-3360-991a-47e34424257b | -3.02222 | -54.18676 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c262a11e-0f77-3534-a02c-32a96961fe2e | -3.07596 | -53.95709 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d0f935d-dc00-3279-bb00-ff99125504b3 | -3.02428 | -54.05039 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 296c496b-8063-3ffa-b02c-a3e441aa723a | -3.07549 | -53.95995 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 97d6a8c4-da78-3235-868f-0bd1bb7e2d66 | -3.26489 | -50.39569 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 12726c0b-ecc9-31c1-a142-125f7714e2ce | -2.34145 | -48.86007 | 2026-10-09 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 48ae372f-6cad-302b-a4c0-21ebc6d26450 | -4.28348 | -49.08914 | 2026-10-09 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1a9bcfd2-90cc-35d3-a1af-47d1ad1bd743 | -1.55195 | -54.56231 | 2026-10-09 04:25:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 35fccf61-bed1-3532-80ac-56f52b5bcb3e | -3.17284 | -54.73874 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc6f3ec3-a748-35ea-9177-1174396ba066 | -1.3673 | -55.60524 | 2026-10-09 04:25:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 6a334db0-089d-3759-a555-4d1653776562 | -3.8977 | -55.88823 | 2026-10-09 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 22549cef-26b5-3f85-8b4f-d8d7045bc08f | -3.08224 | -54.26755 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 507eb28d-1291-3587-9008-9b4ae1c2c889 | -4.08409 | -44.15096 | 2026-10-09 04:25:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5cab2ef-53a7-3d9f-9cea-15fa45677c5b | -6.87842 | -45.90458 | 2026-10-09 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 83dd08be-7291-3375-9678-f39002d7888d | -2.74701 | -54.11333 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b3ebfc2b-8e56-3a49-81d9-30c60fa9ddc9 | -2.33756 | -48.86686 | 2026-10-09 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0e77369-679c-3f73-9d7e-a6b49c534635 | -5.09888 | -46.21177 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e60b9232-9857-3c71-8807-c9dd6778b6fd | -3.25884 | -54.03368 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b267cb42-cf0c-3f59-8afb-f94144c0d929 | -2.50784 | -56.1493 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bb0c3ec4-800c-36c1-a68f-56102e9d1b78 | -4.29984 | -48.60321 | 2026-10-09 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README76.md)
