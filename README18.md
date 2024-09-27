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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2536c66f-afb0-3956-a3d9-df32b7dc03c7 | -21.0993 | -49.1115 | 2024-09-27 00:37:03 | GOES-16 | ELISIÁRIO | SÃO PAULO | Brasil | 3514924 | 35 | 33 | nan | nan | nan | Mata Atlântica | 64.4 |
| a906171f-d831-30bc-95fa-875854f3e4a5 | -21.1192 | -49.13 | 2024-09-27 00:37:03 | GOES-16 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.5 |
| b416519a-e0b2-3163-af6f-9f39b8995764 | -3.117 | -59.082699 | 2024-09-27 00:37:07 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8192ab96-bbe2-3973-9264-f88ee37b2b96 | -3.122 | -59.105301 | 2024-09-27 00:37:07 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cc412aec-c731-31bd-befd-a18f6480832d | -3.1073 | -59.084801 | 2024-09-27 00:37:08 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2e5a276d-a725-3d1d-bfa0-bcc62faea3db | -3.1123 | -59.107399 | 2024-09-27 00:37:08 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 54e1c3de-0004-3116-8033-0646fbbd76c4 | -2.6773 | -57.544601 | 2024-09-27 00:37:09 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ce58b7ea-5fdf-3ebe-af51-7f543d7ed808 | -2.6811 | -57.561901 | 2024-09-27 00:37:09 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b73ebe40-7ada-3926-8dc0-1647c071aae1 | -2.6713 | -57.563999 | 2024-09-27 00:37:09 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 259a973d-a626-3256-9945-633d6ea502e6 | -2.6752 | -57.581501 | 2024-09-27 00:37:09 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8ef7a58e-002c-3a3e-aab4-47bfbcd2e4dd | -22.7442 | -44.7785 | 2024-09-27 00:37:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 79.7 |
| 663a7f35-e625-3dbc-a8e7-f0b5c240e159 | -23.5816 | -47.3408 | 2024-09-27 00:37:15 | GOES-16 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 135.3 |
| 32f0164d-24b4-30f0-8d60-1ee234e62e20 | -1.0431 | -53.3419 | 2024-09-27 00:37:20 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 271a3287-4fd1-3d1e-9670-b190a54bcaae | 0.9115 | -51.9785 | 2024-09-27 00:37:47 | METOP-B | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 4c2dc6b3-8b0d-3074-870b-afaacc789ae7 | 0.9098 | -51.985802 | 2024-09-27 00:37:47 | METOP-B | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| f2ed5300-667a-35c4-9a60-3812e367860f | -2.6783 | -57.5893 | 2024-09-27 00:45:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| f39fe05b-d1bc-3375-9057-f73bd62af35c | -2.8611 | -51.6699 | 2024-09-27 00:45:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| c28e5a17-4324-3f14-9859-64d863443062 | -2.8795 | -51.6695 | 2024-09-27 00:45:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 7f7bef26-f41e-3c33-91c6-51ff7130c597 | -3.0107 | -51.0652 | 2024-09-27 00:45:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 264d5379-9237-32c0-be4b-d09cd6caabd6 | -3.1317 | -59.1441 | 2024-09-27 00:45:24 | GOES-16 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| e0c63565-a09e-3c75-8d8c-476b5cd0ae16 | -5.0199 | -43.7839 | 2024-09-27 00:45:35 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 6410b60b-fa87-330b-88ee-63b139b31bbb | -5.7548 | -63.1572 | 2024-09-27 00:45:39 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 8c24b155-3c52-38c5-9cca-98d5a7b554c1 | -5.7549 | -63.1384 | 2024-09-27 00:45:39 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 84.3 |
| d9ef27f1-b8a5-3e67-a820-0467a3f99ccf | -6.1173 | -51.1185 | 2024-09-27 00:45:41 | GOES-16 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 6aea50a5-5496-35e9-931e-8c478b8be6d4 | -6.8199 | -63.1651 | 2024-09-27 00:45:45 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 125.8 |
| 36a990d5-f455-3b2e-a6ef-da8ebb3246a3 | -6.82 | -63.1463 | 2024-09-27 00:45:45 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 88f2db09-89e3-3dab-b8f5-a016df1c754c | -6.8383 | -63.1645 | 2024-09-27 00:45:46 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 1c760e81-b6a3-3aaf-b925-f8b1f42b0f4d | -6.8384 | -63.1457 | 2024-09-27 00:45:46 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 0989139b-0c7c-3ff9-b0f0-24d4f807292f | -7.0912 | -46.4412 | 2024-09-27 00:45:46 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| c87a99ee-3687-3cb1-a21f-ad999a45dcfe | -7.1099 | -46.4396 | 2024-09-27 00:45:46 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 984e5548-06ad-328d-aeaf-3ca14e7dbcde | -7.257 | -44.9623 | 2024-09-27 00:45:47 | GOES-16 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 236ccfbf-24ab-3fa2-b7fc-942ae812fa1d | -7.2905 | -61.106 | 2024-09-27 00:45:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| dd422228-591f-3e8e-8ae7-90927755a7f7 | -7.2906 | -61.0869 | 2024-09-27 00:45:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 9a382c41-e026-32fd-8b53-84fc8420c72a | -7.309 | -61.0862 | 2024-09-27 00:45:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 62cb19a7-f4d0-32c6-9d95-1fb78cf58da5 | -7.4605 | -60.4114 | 2024-09-27 00:45:49 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.1 |
| e8c8aa3e-2f16-3383-807d-0bb5c38f16ed | -7.4606 | -60.3923 | 2024-09-27 00:45:49 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 8edeef1c-225a-3da2-962f-9be55392461b | -7.5289 | -61.3825 | 2024-09-27 00:45:49 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 291862f0-f8cb-3d6a-a1ae-500eb4d6e3c8 | -7.5703 | -60.5984 | 2024-09-27 00:45:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.6 |
| b264ac36-be5c-3900-9ab2-d1cb91933ed1 | -7.5887 | -60.5976 | 2024-09-27 00:45:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 115.8 |
| e3c971c7-b552-3b9c-ae35-dcfa5e45a9f7 | -7.5888 | -60.5785 | 2024-09-27 00:45:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 02ef0dc6-3ed8-3410-822a-f44dd57046c1 | -7.77 | -61.2015 | 2024-09-27 00:45:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 130.8 |
| 927abc92-a93c-345c-9c1f-f912f57b6ea8 | -7.7701 | -61.1825 | 2024-09-27 00:45:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 128.7 |
| fa81d3ad-ef72-3a36-8c6c-1f7d2e0c1806 | -7.8156 | -54.7252 | 2024-09-27 00:45:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 93130711-b503-3ac1-a441-12965e4a711e | -7.7885 | -61.2008 | 2024-09-27 00:45:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 91.9 |
| ccc95a23-d00c-3e7b-a4f3-e0c5b02fb5f2 | -7.7886 | -61.1817 | 2024-09-27 00:45:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 218bf369-7988-38c5-9447-7138630a7628 | -7.9081 | -62.9976 | 2024-09-27 00:45:52 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| d4b44c22-2fa7-3c00-b58b-729014cf8c49 | -7.9082 | -62.9787 | 2024-09-27 00:45:52 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 71960f1f-bb2e-351c-a27a-3173f4aa3147 | -7.9174 | -61.2909 | 2024-09-27 00:45:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 91.6 |
| ceacd3a9-1d0d-3615-9471-e7271075fc93 | -7.9175 | -61.2718 | 2024-09-27 00:45:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 995e2061-4de7-32fc-9b21-c5a75f25469a | -7.936 | -61.271 | 2024-09-27 00:45:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 8308a97f-0717-3dce-a6e5-07b31915d9e8 | -8.3153 | -55.0157 | 2024-09-27 00:45:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 84c38702-a9d9-305a-af3c-f09868012876 | -8.3155 | -54.9956 | 2024-09-27 00:45:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| fea7a870-30b9-307d-a9ae-d1b32f5dfc1c | -8.556 | -49.6112 | 2024-09-27 00:45:55 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 119.8 |
| 142aafeb-5b26-3557-ae86-2176964faaab | -8.5562 | -49.5897 | 2024-09-27 00:45:55 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 28277ff3-09b8-37d6-9e7e-870deceef384 | -8.4646 | -62.6556 | 2024-09-27 00:45:55 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 8b6326e8-4f78-3e3c-94ae-f57b9fc6cf4b | -8.5748 | -49.6095 | 2024-09-27 00:45:55 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| b010eba7-33fe-3315-b3c0-23c636f563ba | -8.6101 | -63.1226 | 2024-09-27 00:45:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 80.0 |
| cb49d49b-b05b-37a8-bb39-299ee4c6dd39 | -8.6286 | -63.1219 | 2024-09-27 00:45:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 7da87baf-2229-3f35-965f-a04b8e9544d6 | -8.6658 | -63.1016 | 2024-09-27 00:45:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 74.4 |
| c8b6a6d5-ca35-31cf-8258-e6a5b54d7c22 | -8.7033 | -66.9721 | 2024-09-27 00:45:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| e0231fb2-1601-3207-8103-cb103957d63c | -8.7034 | -66.9536 | 2024-09-27 00:45:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 92d94105-c7dc-3c0c-9d47-9a26fe943f49 | -8.7218 | -66.9716 | 2024-09-27 00:45:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| a0f6de6e-d6a9-3abc-8f3d-1178cf022f59 | -8.7219 | -66.9531 | 2024-09-27 00:45:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| f18a7214-1c80-3e8a-88b5-7cb5efef19af | -8.8116 | -67.6917 | 2024-09-27 00:45:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |
| ecd7d730-0074-3405-a66a-1ca9d2fd0679 | -8.8117 | -67.6732 | 2024-09-27 00:45:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 65d8b5b9-a9a9-358c-b71b-23f911e6f35f | -8.8302 | -67.6728 | 2024-09-27 00:45:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 4d91fb88-b67a-3f83-be34-125bc467bcab | -8.979 | -67.4469 | 2024-09-27 00:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| d88984a4-7bc3-3cfc-89d3-1f1efc03cf63 | -8.9791 | -67.4284 | 2024-09-27 00:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 3528c5a8-fdad-39b9-b943-af606a03673a | -8.9793 | -67.3728 | 2024-09-27 00:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| dc0f8f95-aa05-3f1f-a110-6c144c7a166f | -8.9977 | -67.3909 | 2024-09-27 00:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| d2e12bbb-36ee-36d9-a1a4-d0a6689394e1 | -8.9978 | -67.3724 | 2024-09-27 00:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 116.5 |
| 64c7bb16-9316-370c-86dc-cbaba8367e22 | -8.9978 | -67.3538 | 2024-09-27 00:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 49eecb96-c731-3559-8194-f4f9508614f5 | -9.0163 | -67.3719 | 2024-09-27 00:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 106.1 |
| d82643b4-4ec5-36ad-ad63-2da7d1d5dfd5 | -9.0163 | -67.3534 | 2024-09-27 00:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| b05368ce-9c00-3fed-baee-10c719f89c8b | -9.047 | -61.3943 | 2024-09-27 00:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 9719aae7-1490-3868-b8ec-0ba3d69ce67e | -9.0472 | -61.3752 | 2024-09-27 00:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| aade8b1a-2c5c-35c8-b65f-4c43685d3bb0 | -9.0656 | -61.3934 | 2024-09-27 00:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 4e902564-74ba-3a9a-8fd9-2860e607bab2 | -9.0657 | -61.3743 | 2024-09-27 00:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 265baeff-4921-3ce3-99a5-50193ef65515 | -9.086 | -61.1245 | 2024-09-27 00:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| f4fca5c6-afe3-3dce-a5cb-778574c6c43b | -9.1046 | -61.1237 | 2024-09-27 00:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 92727af6-f2dc-3bfb-8d63-2b71d5fc7cce | -9.107 | -67.8881 | 2024-09-27 00:45:59 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 13161eac-188c-3d16-aefe-baeca5f5b58f | -9.1084 | -67.4993 | 2024-09-27 00:45:59 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| ffeb6284-d054-33a0-8638-24e13cbfea36 | -9.1255 | -67.8877 | 2024-09-27 00:45:59 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| f33f0a23-39db-3693-a555-d804ac3015c3 | -9.5829 | -50.137 | 2024-09-27 00:46:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 98.9 |
| ad37c578-9305-32b9-a03e-6ff6c721484d | -9.6015 | -50.1566 | 2024-09-27 00:46:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 795a6c19-142c-39c0-bae3-a1396784b9ca | -9.6018 | -50.1352 | 2024-09-27 00:46:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 129.6 |
| 5826da70-93be-338f-9b98-0905f1d468cf | -10.3672 | -53.7858 | 2024-09-27 00:46:05 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 121.1 |
| 798d81d7-4d74-3b69-8616-4679691b847e | -10.6434 | -45.9772 | 2024-09-27 00:46:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| e2b8503e-98e8-3f2e-ade5-677fb0a782a4 | -10.6438 | -45.9544 | 2024-09-27 00:46:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.2 |
| b600d0ff-c57c-38db-8408-2543b2ba3ed5 | -10.4799 | -50.751 | 2024-09-27 00:46:06 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 122f2ff5-e792-307d-b2fb-cd1443e8a27c | -10.9078 | -54.2504 | 2024-09-27 00:46:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.1 |
| e39e73b0-824e-3f45-805b-68d02a6d64e9 | -10.9264 | -54.2692 | 2024-09-27 00:46:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 311.7 |
| 2e4b9aa7-136a-3bf8-b904-daf7452ec6a8 | -10.9267 | -54.2488 | 2024-09-27 00:46:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 360.2 |
| 2a916928-2ab9-3705-a406-60a9648de834 | -10.9453 | -54.2676 | 2024-09-27 00:46:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 129.4 |
| 23e2c962-2c66-3e7c-af67-5a81187ecde6 | -10.9456 | -54.2471 | 2024-09-27 00:46:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 139.1 |
| bf40484e-bb70-31c5-8281-4c780ba06c90 | -11.1219 | -50.8328 | 2024-09-27 00:46:09 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 70.3 |
| b60ed6d1-1e5e-3fb4-b494-c47797b0e465 | -12.8437 | -54.0422 | 2024-09-27 00:46:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 122.9 |
| 5e0bb766-e158-310f-a676-0d97253a8e39 | -12.844 | -54.0215 | 2024-09-27 00:46:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 065171fb-4ac6-32a5-b2c3-4a69631ae558 | -12.8628 | -54.0402 | 2024-09-27 00:46:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 111.0 |
| 4d541740-b3de-3dd1-bfca-7e1e1c7db45e | -12.8631 | -54.0195 | 2024-09-27 00:46:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 106.8 |


[Clique aqui para ver as próximas entradas](README19.md)
