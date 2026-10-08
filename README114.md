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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf29f69c-9580-32ff-9884-f213b2a3fec0 | -3.30425 | -54.03967 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 30f4d963-2bf4-35ec-9372-5c7aec37e8c7 | -3.48513 | -59.46085 | 2026-10-08 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 24d7c617-e877-37d5-b8ac-ed360d2a8325 | -9.37301 | -45.93963 | 2026-10-08 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0596a2b9-074e-354a-a8cb-e29dfffa90c8 | -3.89716 | -59.44807 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86036834-3b24-3395-8d2d-7de713c7d162 | -4.77435 | -55.74362 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 237f0f33-43fc-36ae-8ae6-53c764880c20 | -3.11504 | -54.16894 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| da09a622-d904-3ba4-8112-43e02f011fed | -2.76399 | -54.08688 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 591cdeb4-7fc1-3b75-a09f-7115a7564cdf | -3.17641 | -58.63799 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 62d17ca6-4ac5-32a2-bb40-9dd63f77527f | -3.99088 | -59.21616 | 2026-10-08 04:46:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 392b6869-730c-31c1-9bd1-734ef56aa2d8 | -6.31813 | -43.3543 | 2026-10-08 04:46:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 00544a57-179e-38e1-9c16-ca13d6265e64 | -3.48138 | -59.58022 | 2026-10-08 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1a9389ec-97ca-394f-bf71-540f340779ea | -6.09289 | -53.49843 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3d5fb0cb-18da-3a60-bba0-0843fe63c5b7 | -3.06137 | -54.21931 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| feb936b5-e496-3983-a34c-344e1f12fa84 | -3.2803 | -54.07137 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a2a82201-dba9-33e5-93f5-bb70884ff0be | -3.59374 | -54.67548 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6621bfb2-0cb4-3498-8829-9b2012181d3f | -4.11092 | -55.17325 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c3dd283-8d35-3361-bb3c-bd51ca311f91 | -3.83674 | -55.9777 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c84c72eb-f1b1-30c2-ad61-e5a15717be05 | -3.5869 | -54.66966 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| cfb92f0e-51b2-33db-9e28-f49f5637ef98 | -9.90509 | -44.79432 | 2026-10-08 04:46:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 981bf1cd-32f3-3290-a254-44acd174d05b | -3.0618 | -54.1696 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9cc28bc6-e2c4-3748-a345-cc815463f9b9 | -3.77797 | -58.52374 | 2026-10-08 04:46:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d0c83771-c744-3acb-9429-5639191a9e70 | -7.22364 | -44.28368 | 2026-10-08 04:46:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f66afdb4-4513-309e-9b97-2d1a5959253f | -4.30162 | -50.78492 | 2026-10-08 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25106fd5-b824-3c72-a562-985e64ebeeb2 | -4.77831 | -55.74434 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| a6cb9f3a-492c-3cf7-bbff-d26455d90b2c | -3.02658 | -54.08924 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9224919c-f5d3-343e-8438-9de96c1ce8af | -4.15053 | -47.98708 | 2026-10-08 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66831678-ef32-3e87-b407-34f61c2ea745 | -8.07969 | -55.29713 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47a56120-b8d8-3e18-85f8-6766409b03bf | -3.26233 | -54.02129 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 996288d9-b7be-3af0-897a-9f66e3df4a9d | -3.00304 | -54.09456 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| f50916aa-569d-3a5a-8a4a-7e5de61d7901 | -3.191 | -53.94978 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dde7e1ec-6888-31c3-8c2e-fd3e9fc18adb | -3.5894 | -54.55695 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b70a2761-fdc2-3842-937c-472b90ce6ad8 | -9.08707 | -61.13722 | 2026-10-08 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 19c0bd83-cac8-33d7-9f30-c3d5acd90eb7 | -3.10853 | -54.18608 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| ae429a9f-b69c-31c2-970f-5e51a665674c | -2.93706 | -54.17442 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 14189a9d-d68b-3077-83e9-caa1a0527c4a | -8.21921 | -46.36612 | 2026-10-08 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 013f3a83-0404-3a1c-a2dc-d1d863b9ca7e | -6.28929 | -43.65772 | 2026-10-08 04:46:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ef32313c-cb3b-3b20-a194-60178663f83a | -3.02803 | -54.23685 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aa91ede9-b714-38b1-b959-4ea12a55cbd0 | -5.7561 | -42.06822 | 2026-10-08 04:46:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 7262272a-f701-3541-8d18-40290274b193 | -3.08098 | -54.26337 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 92bd52ce-685c-387c-a3f4-80e7920a6526 | -2.76257 | -54.09571 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 970605dd-ebf3-31ed-afe7-039c27014af2 | -7.25729 | -48.06515 | 2026-10-08 04:46:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8049f289-bda6-308a-b4ee-94b0ce429a4f | -2.99107 | -54.07479 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| aab41484-b562-33d3-ba4b-7c60f5efadee | -3.32884 | -58.14932 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 082ea45b-92a2-3a62-aa62-e6f72a49ad82 | -3.01074 | -53.90526 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 089c78db-cc48-368a-8ee7-129e6dbb9479 | -8.23987 | -48.58017 | 2026-10-08 04:46:00 | NOAA-21 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e56132dc-45ae-3733-b69b-1050b3087531 | -3.36527 | -58.19808 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9aa10be9-3c7a-3c97-9f54-ebad47f1b660 | -3.03154 | -53.93921 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1539089-2f63-3b66-bd11-23766a444a46 | -3.07792 | -53.95387 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 1032f400-5801-3a96-aaf0-9b837fb0aca9 | -2.57292 | -56.15664 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e343ea69-ccdf-39c3-b0e7-10d7ea4ff4af | -10.42881 | -47.27638 | 2026-10-08 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a31811b4-0cf1-3e12-a1c6-c25109e7b245 | -4.81277 | -46.82592 | 2026-10-08 04:46:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4a85ee76-b68c-3623-b5c8-20eef9bff2df | -3.10104 | -53.75882 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 127b3ad4-dafa-377f-9c33-3535f939121e | -3.10753 | -53.77155 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1938ba53-d1f8-3aa9-bd57-9803f1bf0bf4 | -2.98053 | -54.04637 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b761a0c-18c3-3056-9111-76c4a9f6ce74 | -7.23011 | -55.16523 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ca26bb19-04c6-35a7-aa7b-b3915a52fb7a | -3.31266 | -53.86743 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a6d89733-894e-3dda-82e1-1d94349eaf9a | -3.53843 | -54.65715 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 126a97ae-321b-3972-a2e0-88d2c2cad15e | -2.97963 | -54.12249 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 466e6ae4-fc56-3f0c-bd2e-6ac86732c358 | -3.27157 | -54.05809 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f4552ffa-6299-379b-81c3-f4d03e8ea476 | -3.59301 | -54.6801 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 15a6c3b8-84b6-3825-b803-31c0fdbb8764 | -3.66828 | -60.61972 | 2026-10-08 04:46:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 69565c79-82c2-35b4-bcf7-894cb9a93b59 | -3.63331 | -55.51025 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 269efdad-4698-38d7-ae54-1eced26a57ac | -3.26898 | -54.02673 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ff2d7432-7afc-3345-82a2-98e79dc1834a | -4.06303 | -54.03622 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ce4b02c-4e69-3bd6-9e48-d16772dde604 | -3.36942 | -58.20067 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72d296d7-03df-3699-9797-add64e6f3482 | -3.99206 | -56.26323 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c40a43d-fa5b-30ae-a121-5988929b1c8b | -3.53241 | -54.67032 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c66b36da-5cb1-3a8d-b881-0d6476b65a08 | -2.98864 | -54.13729 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 73c813a0-c82e-3ad3-96e6-c6e7e3359a81 | -3.61558 | -55.4687 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 72022490-095a-30c0-92f8-9ca2fdb5bda2 | -10.42617 | -47.26615 | 2026-10-08 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c461f46c-2427-3a3e-b128-daa5f82fc918 | -3.30405 | -54.01767 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| be57b6bb-3fd5-3b66-aa6f-19439cadd0b9 | -2.8834 | -54.09114 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e8b963c1-8622-3373-bd31-19007d7c848f | -5.01474 | -49.94108 | 2026-10-08 04:46:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 87445ea7-8d3a-3986-adc9-8a567bc2ad40 | -7.88657 | -55.01436 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64f3004b-7c3f-3372-a20e-3d04bbfcf71e | -4.07334 | -59.84294 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f7eee423-415d-37ad-9173-3f9cd7ba3463 | -3.56953 | -54.48898 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c6822c87-9741-3b1c-9e37-f09392b2446f | -3.29255 | -54.04225 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3fe3915d-8725-3a79-b97f-c58ea83566d3 | -3.83826 | -55.97322 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eb203676-867a-396f-8ac2-5e199c50d046 | -8.22288 | -46.34042 | 2026-10-08 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 838c51e6-b66f-36d0-a2fe-bc7ff3a12bef | -8.07469 | -55.28891 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 502e406f-f9de-3094-97a2-483e804e0b41 | -6.63516 | -43.73662 | 2026-10-08 04:46:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| f63fabd8-0b26-32d6-bb0d-04df5b2b5e6a | -7.86877 | -54.9631 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b84b1f43-8a29-3b89-9645-7bc5ef909ceb | -2.84039 | -57.47899 | 2026-10-08 04:46:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5e212fcb-1d4f-3d20-a915-3715ebef8e6b | -3.59996 | -54.56329 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5f64d326-d28c-3336-91e1-e54178b213d9 | -5.97295 | -55.38297 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 84b2364c-ee61-3552-a72d-0a8b27c679a2 | -3.07123 | -54.25277 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4003c5b0-7b56-33b7-8d82-dce7bdab3ee0 | -3.10038 | -53.76303 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7b51e45c-c442-3f19-abd9-428c06f47047 | -7.2253 | -55.11113 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 47745ac1-88ef-3881-8969-f7f1d1ef2848 | -4.14017 | -54.92195 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 204733b9-16af-30e1-8ca0-6af3226f6e9b | -8.2609 | -54.67596 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b9ad9a9-d920-3de7-bdd8-c4a7f018c70a | -5.69276 | -53.4761 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3e156d20-9bea-3652-9914-63f3649d2e04 | -5.82055 | -53.83209 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 05e25b32-4dd2-388e-8f37-ca27ffe83d97 | -3.86182 | -56.00419 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4f90674d-f73e-3931-8916-342073860c0d | -2.798 | -54.08766 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0e4e60ec-ca8f-3fb6-9dc0-2bb226b8df6c | -2.49314 | -56.16803 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4c03b4a3-f754-30f9-b5e0-82aa76c9eed3 | -11.38396 | -47.09755 | 2026-10-08 04:46:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 38faa6ba-daf3-3691-b04e-7805454ecc3a | -2.93532 | -54.04995 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| e1c0c71b-b9a2-3133-99de-b92ba3d6e510 | -3.26695 | -54.03968 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7d546ee0-1a60-3ec4-af20-c957e2b1b80b | -4.27251 | -54.8729 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f631d9b9-a911-3eac-89ca-9b329c9a11e4 | -3.98474 | -59.22148 | 2026-10-08 04:46:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README115.md)
