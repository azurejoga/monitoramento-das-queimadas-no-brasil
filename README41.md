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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 576b75b7-4fbe-38b5-965e-62967ec4a480 | -3.11441 | -54.29442 | 2024-11-01 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c5a48e50-fc0b-32ba-a1f5-e2540ee13d97 | -3.1136 | -54.29934 | 2024-11-01 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc4526f8-22df-3ef6-a649-d2df272fcfd5 | -3.11109 | -54.29621 | 2024-11-01 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c003f02d-9fce-373e-9559-76c600c3899f | -3.10674 | -54.28319 | 2024-11-01 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3eb5b054-982b-361a-afb0-439f7857cb8c | -3.10334 | -54.28493 | 2024-11-01 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c6b1a1bf-359f-396d-897c-ab4f8e244083 | -3.10209 | -54.28243 | 2024-11-01 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f37a5ba-3910-3753-a0a9-742b012b0631 | -3.09947 | -54.2793 | 2024-11-01 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fff6ca1b-eb06-31df-9c54-3c5f27975ffd | -3.09793 | -53.71537 | 2024-11-01 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0eb56719-29d0-3f50-af67-7bce348ab58b | -3.09743 | -54.28168 | 2024-11-01 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f0c31e7-e8a8-3e4a-8095-ec4bf8356812 | -3.09719 | -53.71983 | 2024-11-01 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d8fb6d05-f98c-332b-8e39-7fa8e31062b9 | -3.09518 | -53.71712 | 2024-11-01 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c4fb0002-8ba0-3ffe-a82d-2fcac62047f9 | -3.09346 | -53.71464 | 2024-11-01 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8a271b10-3597-3a3b-a357-af1c52703e4d | -3.09272 | -53.71909 | 2024-11-01 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 10e22123-3e8c-3b8a-8156-eeb7059c34dc | -3.0907 | -53.71639 | 2024-11-01 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 19432994-e99d-3e43-8ef9-c77ef617ae35 | -3.07029 | -54.16566 | 2024-11-01 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fafd81d5-6054-399f-a294-549119f97b89 | -3.06569 | -54.16484 | 2024-11-01 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e63e572b-f212-3a8a-8a60-83b38719ccc1 | -3.06491 | -54.16957 | 2024-11-01 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 36396604-1a3f-3d74-8359-09fbd7ec72b4 | -3.04643 | -54.1666 | 2024-11-01 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5f8fba7e-8462-321c-995a-baaadc6db5d0 | -3.04564 | -54.17141 | 2024-11-01 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c7ef76d7-3422-3f2a-8c42-d45e75e341f1 | -3.04485 | -54.17619 | 2024-11-01 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0a67cf51-bc80-38a0-9781-9f99a32a97ed | -2.88605 | -49.24918 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b6d0e97-72f6-316d-aa2c-d56bc109d993 | -3.39075 | -41.64568 | 2024-11-01 04:29:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7d5410d8-9e0f-3e1a-b022-bde03417af2a | -3.36708 | -41.66146 | 2024-11-01 04:29:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b5547c93-1be2-3ff6-9c5b-bc321239ade7 | -3.03193 | -53.79557 | 2024-11-01 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e6320eb6-7e1a-3d49-808c-ef6f21e1d7f3 | -2.96129 | -53.91456 | 2024-11-01 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7751292d-f407-3620-be52-f2e4345559cf | -2.95676 | -53.91377 | 2024-11-01 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96a4531c-0a7d-310c-8bfe-a4e3f7796285 | -2.94239 | -53.70853 | 2024-11-01 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45b7cb18-5199-3622-9d54-dc0e57e4cccb | -2.91894 | -54.19792 | 2024-11-01 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 129556fb-d14b-37c4-a9d0-e85675f67cca | -2.91511 | -54.19233 | 2024-11-01 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 24837ab8-db9e-3a58-a302-fb6f701d4557 | -2.91431 | -54.19715 | 2024-11-01 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4794cf3c-960c-3293-b507-ab0c8d9790b2 | -2.9068 | -53.87098 | 2024-11-01 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b444c30f-bd27-3989-917c-e50f43255a21 | -2.90608 | -53.87537 | 2024-11-01 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ef32b01-4fd0-3f6c-bef6-6d5399b13a35 | -2.10932 | -55.92003 | 2024-11-01 04:29:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d695f5c8-c29a-3aaf-940b-c402c45417c6 | -2.10878 | -55.9233 | 2024-11-01 04:29:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b01a9817-ce6d-38b6-8924-1a5283aab2c2 | -1.8115 | -57.1084 | 2024-11-01 04:29:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 97b9ae15-af32-355b-82bc-55287aa31e2b | -8.81218 | -40.17336 | 2024-11-01 04:32:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7b59e19e-198f-363c-9a6a-1dc6384ff66a | -8.8172 | -40.17403 | 2024-11-01 04:32:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 45a6a90e-467b-3d96-8d1b-6a89ca0cd39d | -8.81179 | -40.17625 | 2024-11-01 04:32:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b40e328d-e048-3de2-9126-ad7128daedc4 | -8.67971 | -40.2082 | 2024-11-01 04:32:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0b3e65fd-17cc-3804-990a-3d41a6dca641 | -11.94133 | -41.62797 | 2024-11-01 04:32:00 | NOAA-20 | MULUNGU DO MORRO | BAHIA | Brasil | 2922052 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| abacc873-253a-3850-8a23-b910fed8f7b4 | -11.94065 | -41.63314 | 2024-11-01 04:32:00 | NOAA-20 | MULUNGU DO MORRO | BAHIA | Brasil | 2922052 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 33766403-ba8e-341a-8361-8687237ec3b5 | -11.28437 | -40.95565 | 2024-11-01 04:32:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e25acb55-2354-398f-847e-391723bed5a5 | -11.28364 | -40.96121 | 2024-11-01 04:32:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 42405b14-9e39-3c6a-b0ca-f42cf2407bb8 | -7.20781 | -42.18115 | 2024-11-01 04:32:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| e22b871d-9c6e-3b7e-86bb-fcf9f4bdabaa | -6.85264 | -43.57663 | 2024-11-01 04:32:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a2c87bd4-b1a4-332f-be1b-4aada0f28d10 | -7.89178 | -43.78645 | 2024-11-01 04:32:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 26e6db03-79b7-3b86-817c-c8277375f1e6 | -7.18401 | -44.96233 | 2024-11-01 04:32:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aeaaab2e-92cd-38f1-a847-1297b55fb766 | -7.18147 | -44.97894 | 2024-11-01 04:32:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f3d174b-ab6a-39b6-ad96-d1845404a331 | -6.90575 | -44.62985 | 2024-11-01 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db26d280-66d2-3fa6-a2ca-a037aee5437d | -6.87789 | -44.76406 | 2024-11-01 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d371fc4-f817-3889-a145-800145ffde32 | -6.87491 | -44.75933 | 2024-11-01 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8cd9942a-762b-3a3b-9be6-36c03b64eb4a | -6.87129 | -44.7588 | 2024-11-01 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62093c69-2f8b-3fe0-a663-bc603ac31958 | -7.21898 | -44.01916 | 2024-11-01 04:32:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 07008cbc-7154-32b6-82f5-a82d93347477 | -7.21846 | -44.02142 | 2024-11-01 04:32:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 99038baf-ee12-3042-b26e-17eb610f3979 | -6.87428 | -44.7635 | 2024-11-01 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2b5c710-60ff-36e2-8cc1-7ff84ddbfcaf | -6.34945 | -46.33987 | 2024-11-01 04:32:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5fa5c466-c1f9-37da-a181-9e3402a190f0 | -7.28507 | -45.41398 | 2024-11-01 04:32:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d0503c4b-7585-3c53-95fb-b83c9f297880 | -7.40605 | -45.56874 | 2024-11-01 04:32:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1477ec13-be24-35c4-8877-b4e813a29675 | -7.23076 | -45.77236 | 2024-11-01 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ac57c39-c4d3-354a-8882-5d808995c632 | -7.23018 | -45.7762 | 2024-11-01 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a8685e35-719a-3a2f-8b5c-d46437ff5cd7 | -7.2273 | -45.77184 | 2024-11-01 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 90a37afa-b7a5-308f-8d35-f6daf9246065 | -7.22671 | -45.77568 | 2024-11-01 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8708d78e-fa29-3cd3-bde4-aa77325b322d | -7.18176 | -46.32099 | 2024-11-01 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 909226fb-d85d-3a53-a6dc-c1c558f70eba | -6.72508 | -46.35266 | 2024-11-01 04:32:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd1645bc-21b5-39f2-97f9-48ca3a01eca9 | -7.2296 | -45.78004 | 2024-11-01 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 641b583a-e6dc-355e-a18f-45c40b75a342 | -7.22613 | -45.77952 | 2024-11-01 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 83d5aa5c-702d-375a-a7a7-bcc4ec34c67b | -7.18119 | -46.32468 | 2024-11-01 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8300d470-775c-36f4-b8a1-31e6be3813b9 | -7.0469 | -46.31164 | 2024-11-01 04:32:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9c438c0-826c-3d86-b9d2-51787c8ee76d | -7.04634 | -46.31531 | 2024-11-01 04:32:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 62225b10-6853-3b80-be79-ce398a4057c8 | -6.36591 | -47.91709 | 2024-11-01 04:32:00 | NOAA-20 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3a5132a4-bb53-3a89-be6a-0a594d55e8c9 | -6.36315 | -47.91312 | 2024-11-01 04:32:00 | NOAA-20 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98bcaf04-813e-364c-9d9e-e0cc41bddab1 | -6.2849 | -47.41575 | 2024-11-01 04:32:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 50871c1d-6325-342f-b66b-48f86125efd2 | -6.50367 | -47.4503 | 2024-11-01 04:32:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e5215906-786e-3f09-b9af-3208d44d6a28 | -6.29348 | -47.33898 | 2024-11-01 04:32:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 737fb57f-e9bd-3363-9032-e5ebee8c0acc | -6.6454 | -47.86899 | 2024-11-01 04:32:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9ba2451c-216b-39e6-8a25-fb82a127dc2a | -6.64486 | -47.87244 | 2024-11-01 04:32:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 542edc03-ca5b-35ab-884c-965be7dd6aa2 | -6.50757 | -47.87931 | 2024-11-01 04:32:00 | NOAA-20 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0a76da03-5827-3f9e-956f-242fc6442c43 | -6.66178 | -47.11099 | 2024-11-01 04:32:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6403b257-241b-3bcf-afed-2ca9e0d6c855 | -6.60416 | -47.39472 | 2024-11-01 04:32:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5994878c-ae1e-3bc1-94ae-7faad981adb5 | -6.51087 | -47.87983 | 2024-11-01 04:32:00 | NOAA-20 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 529a91fa-229c-3f09-ae5b-7c37a89a6a4e | -6.60057 | -47.3944 | 2024-11-01 04:32:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5d8a832f-d311-3fd1-b88e-e87e51dae5fd | -6.55401 | -47.51851 | 2024-11-01 04:32:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d1cedd29-3233-373a-92df-6f2e79c521bf | -6.38646 | -49.57941 | 2024-11-01 04:32:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7c3b549-4b40-322e-b435-62bba071a61b | -6.38425 | -49.57155 | 2024-11-01 04:32:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d4ee5a2-8786-323c-b9ba-1700dd12b98b | -6.39161 | -49.56904 | 2024-11-01 04:32:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 29d5125a-f543-3925-a452-189f59612c7c | -6.38763 | -49.57214 | 2024-11-01 04:32:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 331b6968-ac88-3fde-99f4-b395f663546e | -6.38704 | -49.57578 | 2024-11-01 04:32:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| be9e460d-41ff-3a7e-8856-923d211f390e | -6.38366 | -49.57519 | 2024-11-01 04:32:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 324a9084-cd0d-3a0b-9c58-5b76a5a452a5 | -6.45138 | -49.91594 | 2024-11-01 04:32:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b46898eb-3a36-3dc1-b7d1-3783f85709f7 | -6.0156 | -51.09338 | 2024-11-01 04:32:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 057fb133-250f-3b04-a0d0-e09c546ba7f7 | -5.97315 | -49.6609 | 2024-11-01 04:32:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d1193e9-3c7f-35da-9668-0b82b17eda10 | -5.76183 | -50.09988 | 2024-11-01 04:32:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a97ecea2-de9a-384d-942d-4ac3f1d5892c | -11.8736 | -56.20892 | 2024-11-01 04:32:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e6e9fd8-badb-3aff-87b0-950c52f36986 | -19.88898 | -46.09399 | 2024-11-01 04:34:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a253c5dd-eccf-3f84-8d6c-222ba861ab5f | -19.88776 | -46.09538 | 2024-11-01 04:34:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ea826b3-9a11-328d-a3ee-9d8bd333c878 | -19.26126 | -46.86988 | 2024-11-01 04:34:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e6f56e1b-fc74-3b79-9eff-c425026799b0 | -20.42222 | -47.59511 | 2024-11-01 04:34:00 | NOAA-20 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 18f00b70-cdd4-36fb-bdbc-0199d8873329 | -16.40895 | -50.49778 | 2024-11-01 04:34:00 | NOAA-20 | SANCLERLÂNDIA | GOIÁS | Brasil | 5219001 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e41ed425-25d0-39f9-8dad-130578e1aadd | -17.36575 | -52.00369 | 2024-11-01 04:34:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| be893469-6004-36dd-86f8-f07d505e949b | -17.36237 | -52.00309 | 2024-11-01 04:34:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README42.md)
