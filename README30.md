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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f97ffb2-0999-3bf0-9d0c-45eab6cecd6a | -7.59655 | -46.64053 | 2024-12-10 04:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bbace2f8-a0df-3516-9c0e-0ded5c96bfbd | -15.44151 | -57.81366 | 2024-12-10 04:55:00 | NOAA-21 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| dff06aa0-1882-3cca-91d3-328e874562bd | -15.99077 | -57.1646 | 2024-12-10 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 50eb008f-f045-302d-915a-c9952a3403f3 | -13.32264 | -52.41743 | 2024-12-10 04:55:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 38af0338-e3d9-34da-9e1b-d30923c2f7dd | -14.53372 | -45.48059 | 2024-12-10 04:55:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6741e8f6-6d9d-3330-93ff-64d1d3d75730 | -12.53852 | -57.73034 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b09f26f-3a29-3d36-a193-35b5ae067937 | -15.26279 | -53.57436 | 2024-12-10 04:55:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b89ad7f2-48c7-3a53-921a-4c24b1ca17ba | -8.62421 | -55.26028 | 2024-12-10 04:55:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f83d79a5-e758-3201-834c-a1999a5a98b7 | -13.20685 | -56.88673 | 2024-12-10 04:55:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b4c94982-07f2-3a3c-a448-a47bbab0a02a | -12.04679 | -62.79043 | 2024-12-10 04:55:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d162f8b-fa57-3d0a-88ea-52e99791b575 | -15.25662 | -53.56964 | 2024-12-10 04:55:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7cc3f2d-300b-3dfc-99d9-8ff2d9364048 | -15.07871 | -48.94657 | 2024-12-10 04:55:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| acc45ff4-b51f-3715-bba9-750a5baa96fe | -12.56618 | -58.36644 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c5a90fd-eafb-34d2-a5d8-53bfe45fa93a | -7.62518 | -47.04966 | 2024-12-10 04:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97c190f2-38db-3de1-9df5-25cae62f1ffd | -14.3854 | -46.79676 | 2024-12-10 04:55:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ce0c0d0-6202-3d48-b5da-08800e0b6bd4 | -15.3701 | -53.13333 | 2024-12-10 04:55:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 543024d1-72ea-3e26-badc-55712391dc79 | -12.56261 | -57.76594 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d02d9142-b9c7-3c18-a975-907fcf6a89ce | -12.54296 | -58.34298 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 18e1caa4-ee4c-3cdf-88ef-6b1dc1ad63c9 | -8.86405 | -47.66981 | 2024-12-10 04:55:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f97a2ec-0fd2-3700-9357-c03635aaad93 | -12.54353 | -58.36237 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 776ab80a-4292-337a-8d70-bb84d2a9e71e | -16.37659 | -47.40126 | 2024-12-10 04:55:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8aa26127-7827-3e2c-9dbf-fe7bceaea195 | -15.09453 | -59.63493 | 2024-12-10 04:55:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2cfece52-9fb3-32d3-9440-1ebe48f2a9fe | -13.75153 | -53.28148 | 2024-12-10 04:55:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 878aeb0f-ebfd-30e1-a7c5-8a87614759c3 | -12.90353 | -55.05073 | 2024-12-10 04:55:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb6392f9-1bbf-3b86-95f7-3ad56a600a80 | -15.26224 | -53.57806 | 2024-12-10 04:55:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 18c55e9e-8073-3c01-bcbe-8ba483ec0409 | -12.5615 | -58.3546 | 2024-12-10 05:00:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 9ecaceff-b0f2-3e37-a7d5-14bb39b26d28 | -4.3959 | -47.7618 | 2024-12-10 05:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 53cfccf2-063e-3c61-a163-a9e13cb73b69 | -12.5425 | -58.3561 | 2024-12-10 05:00:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 1801046e-d00e-3713-aac9-d3c99712ee94 | -12.5427 | -58.3362 | 2024-12-10 05:00:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 75.4 |
| ce8210aa-6ad9-378b-a6b0-729086e9e013 | -12.5615 | -58.3546 | 2024-12-10 05:10:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 4ca76a01-8611-3c17-8068-35bcda3d96fa | -12.5425 | -58.3561 | 2024-12-10 05:10:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 07e21692-6405-34db-96f8-2d12547da7a0 | -12.5427 | -58.3362 | 2024-12-10 05:10:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 338193ac-a422-3604-be6e-a56a8ed1274e | -4.3959 | -47.7618 | 2024-12-10 05:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| b1eb03f2-5767-3050-bb85-a2c818b696d0 | -4.3774 | -47.7627 | 2024-12-10 05:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| e1b3125d-f2b4-3886-86ea-0ec686de511e | 3.22143 | -61.19389 | 2024-12-10 05:14:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 694632e4-ae84-3833-984a-08ef8918dfe3 | 1.97655 | -60.91206 | 2024-12-10 05:14:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b79ee50a-a72d-3e1b-b12e-12557e366ae4 | 1.07123 | -59.24799 | 2024-12-10 05:14:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9f2bd9cd-e793-360e-86cc-f49b48354567 | 1.07825 | -59.25525 | 2024-12-10 05:14:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3526c826-14d6-30d0-bef4-875405a88169 | 1.07481 | -59.25578 | 2024-12-10 05:14:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3a70351f-9814-34d3-83e4-6f0c434b9bdd | 1.07585 | -59.25489 | 2024-12-10 05:14:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27b6d817-0b52-384a-96f6-19fd523de788 | 1.12059 | -59.53663 | 2024-12-10 05:14:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f36be4ee-183e-3c54-a370-1b81f6af99e0 | 3.22096 | -61.196 | 2024-12-10 05:14:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a84a53d5-1e28-366d-89c5-1628600ff25c | 1.12186 | -59.53734 | 2024-12-10 05:14:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fe95d573-4a88-30a1-9978-a82fc82e7551 | -1.63902 | -45.90845 | 2024-12-10 05:14:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61599c61-030c-3ee4-9c9c-ddbadc239e79 | 4.12597 | -59.95654 | 2024-12-10 05:14:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 357ccdbd-031d-36ed-a4ae-0f55774793a6 | 2.73843 | -60.751 | 2024-12-10 05:14:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ffe5f517-6bd0-3d2a-94d6-ca3327fef44b | 3.22531 | -61.19328 | 2024-12-10 05:14:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00f1e1a8-bd08-3974-a6c7-b50c9497c0e4 | 2.42592 | -60.65176 | 2024-12-10 05:14:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3fbb8388-9299-36bd-b2a6-a921d43d8aa8 | 2.90135 | -60.93463 | 2024-12-10 05:14:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85b427ba-938f-3ab9-b7c0-b59094ca28af | 3.2292 | -61.19268 | 2024-12-10 05:14:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fcc7983f-8de5-36d0-9152-0d873a2ba073 | 1.9769 | -60.91447 | 2024-12-10 05:14:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b748a859-2bda-3852-8d2a-43c27fe9d13e | 2.47755 | -60.68912 | 2024-12-10 05:14:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4bdb8e12-d965-3b06-934a-9a6f54f07129 | 2.42896 | -60.64674 | 2024-12-10 05:14:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c39629c1-644b-3932-9d22-e893ec528b93 | -0.72872 | -48.57717 | 2024-12-10 05:14:00 | NPP-375D | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e1496834-b2f7-35fc-b2d6-26a5912ddc5e | 2.47825 | -60.69357 | 2024-12-10 05:14:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 233d7b10-d826-3b73-9a0b-b362ac7ddbbc | 3.15395 | -60.71907 | 2024-12-10 05:14:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7ed6b97f-1d6e-36cf-88e7-ada2caba9422 | -1.64548 | -45.90945 | 2024-12-10 05:14:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a24f023-d8b6-3bde-a00e-cf200a8b2ee1 | 3.15464 | -60.72363 | 2024-12-10 05:14:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9b394c66-089c-361e-b7de-dac9060bea4d | 1.08169 | -59.25471 | 2024-12-10 05:14:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| eae7ed5f-2e13-3dfc-9eab-2f456a6f32f2 | -1.64578 | -45.90909 | 2024-12-10 05:14:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f578a88-8ad0-3d68-8fb8-54d59ed0ca9c | 2.42964 | -60.65118 | 2024-12-10 05:14:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7eea4478-6c95-3e50-be65-8e45dec2d312 | -1.63931 | -45.90814 | 2024-12-10 05:14:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 01ad26ab-e5b2-322f-8a80-188cff7ce80c | -0.72821 | -48.58053 | 2024-12-10 05:14:00 | NPP-375D | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 71e1148c-221e-3f07-a123-3907ce30796d | -2.62551 | -48.06057 | 2024-12-10 05:16:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e5f9028c-8861-388d-a56d-a2d6006dc77b | -1.88332 | -53.28919 | 2024-12-10 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e76cd5d7-0a05-352e-929c-8b3b02e6a6a7 | -4.54786 | -48.00179 | 2024-12-10 05:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6dc13b9c-7890-3776-a7d8-6013a6d449bc | -2.90539 | -54.15265 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 900b0a45-b218-3146-8a13-e47ae2a34583 | -4.54726 | -48.00606 | 2024-12-10 05:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0f0a528f-2709-35f4-a6c7-3b384d309c9f | -4.13957 | -53.67376 | 2024-12-10 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c07b9ffb-00cd-3577-bd4c-fe117b134cf2 | -4.0483 | -54.09933 | 2024-12-10 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d97700a5-9c5d-3508-9f60-960ffa27dfef | -8.44152 | -49.62671 | 2024-12-10 05:16:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0f5f650f-74e9-318f-b2e1-d59470228d01 | -2.24951 | -53.8746 | 2024-12-10 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 06e7626b-4db6-3553-93de-d85e239ced59 | -2.95139 | -53.11494 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b4ae82b1-db1a-3fe1-9ed7-ed190c726195 | -1.52945 | -54.02293 | 2024-12-10 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95d7db02-ee60-36d7-b642-cf5a28512ca4 | -3.10942 | -53.24852 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 70c5e8fd-891c-3906-a39a-4b6758b873ae | -4.04813 | -54.09757 | 2024-12-10 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f0d9eeb-b2e5-32d5-a459-2d663d447254 | -2.96701 | -54.22501 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52863227-3c5c-34dd-ab2e-11903d8c06ff | -3.78263 | -50.05462 | 2024-12-10 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed452028-5b1b-3a4e-9a25-ed880c5e7fba | -3.61325 | -54.30907 | 2024-12-10 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5478194-9cc2-3d4a-b818-960c7fc1d2ee | -3.62819 | -52.68128 | 2024-12-10 05:16:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6077a444-033a-36dd-abb3-a7e8e8543519 | -3.11861 | -54.04085 | 2024-12-10 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f3183b2-6a57-3e3c-be88-feb0b7e6ebc6 | -2.55799 | -53.41738 | 2024-12-10 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6886f538-5c5f-3738-adec-8bf60bd9c309 | -2.81605 | -53.05114 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 743678de-deee-3c5e-95a9-5de5ba0a9521 | -2.75485 | -54.15757 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6dd9226f-f602-3e2a-838e-c960714b0516 | -2.8272 | -53.0602 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f586fd8-047f-3ac3-a4cd-221924b835f0 | -3.63241 | -52.68199 | 2024-12-10 05:16:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fa9881c0-a25b-3126-8537-2bbd396bcfec | -3.57171 | -53.02296 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c5c7100-e374-3905-8d10-aa2db99269a6 | -2.98381 | -54.06152 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9163f535-7ffc-3f9d-a3c3-b1a2752371c7 | -3.63299 | -52.67807 | 2024-12-10 05:16:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a2943c4a-c0f1-3a42-92b0-df34182d732a | -3.27584 | -51.0846 | 2024-12-10 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 890d78d2-479d-3c96-8df5-3da2df62398c | -2.55722 | -53.42242 | 2024-12-10 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e1e02cc-58bd-32c4-81f5-9af0819816f5 | -5.92078 | -48.04677 | 2024-12-10 05:16:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bed484a9-92b3-368b-8981-e6a98a64f65d | -2.37369 | -53.86019 | 2024-12-10 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b7a7307b-c4b9-36ed-a4e4-8085204f4994 | -3.14742 | -54.48468 | 2024-12-10 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3abdab0-e620-3e59-8918-67468b95f46d | -3.08931 | -53.35575 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd1f2e1a-f969-3653-bba7-2d18957b56ef | -2.8302 | -53.06799 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7bc28ee2-629e-31e0-8f4f-6d12d269e13c | -2.41307 | -53.6874 | 2024-12-10 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0f8be86-afc1-3060-8d13-32f6a116776a | -2.96303 | -53.12051 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 25d43d93-ce38-389b-87e4-0e3cc2ed3f78 | -1.73795 | -54.16999 | 2024-12-10 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b73b532-1e05-373b-bfab-ff1d73d9e48f | -2.99226 | -52.8451 | 2024-12-10 05:16:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README31.md)
