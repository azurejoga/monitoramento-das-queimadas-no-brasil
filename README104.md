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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4692eed6-af71-3905-acb3-6f90d93c914b | -2.90804 | -54.19453 | 2026-09-21 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 20165707-49bf-3817-8eca-f0c6598b6a3b | -3.3973 | -61.29487 | 2026-09-21 05:59:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8023305-6da4-31e8-8b37-d8d506c79b53 | -5.76537 | -57.58415 | 2026-09-21 05:59:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9da5f5c5-967c-39ac-bea8-20eb34e5791a | -3.39858 | -59.58475 | 2026-09-21 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d931da5d-2d5c-3d94-ae46-e3588719b5bc | -3.19402 | -60.43274 | 2026-09-21 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2342122-630f-3afd-a4f9-8db19a3e856a | -3.48719 | -59.60709 | 2026-09-21 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 27e90d36-3752-3d6f-9584-28aae0da11f0 | -3.488 | -59.56766 | 2026-09-21 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2e75a664-2aaf-327f-b0e3-cdfa20692964 | -3.34771 | -59.85108 | 2026-09-21 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 26bb6d5d-72bd-3e5d-a8f1-ccd0c5ade5d3 | 0.01262 | -60.60692 | 2026-09-21 05:59:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7334ab5-0870-3516-b9ac-91e98ab5f151 | -2.86947 | -57.81055 | 2026-09-21 05:59:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 8dbbe3f3-3cb0-311a-a783-11a68fae8106 | -3.33411 | -59.83688 | 2026-09-21 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| edb1751c-b06e-3c68-b7f1-f69e6bb11a66 | -3.08314 | -61.17063 | 2026-09-21 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7bfb8d4-12b2-3e33-a7f5-87abdb522287 | -3.07192 | -61.2756 | 2026-09-21 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 430ed59e-ab98-3530-a2c1-90273573bf27 | -2.87006 | -57.80664 | 2026-09-21 05:59:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 79d9af9b-b887-3095-8c57-c97fbec766ad | -3.44575 | -58.39789 | 2026-09-21 05:59:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6f14f9a-2bc7-3da8-b7f6-fae5cfe1abbf | -3.10534 | -60.72153 | 2026-09-21 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7735c71b-32a4-3fd9-9ec9-b2943911f8ee | -3.39349 | -59.58402 | 2026-09-21 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4cdcbde-125a-3273-8aa7-84aee2710b12 | -3.49445 | -59.61518 | 2026-09-21 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 44071ca0-d1d5-3184-b97f-9fe25a356cd2 | -3.53636 | -58.68894 | 2026-09-21 05:59:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8cff8eeb-9ae8-3b41-a71d-b669bef7ff04 | -3.42669 | -59.26421 | 2026-09-21 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 610d07c1-74b7-3ae1-a8c7-9153ccae62b4 | -3.82413 | -59.33488 | 2026-09-21 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4a78d94-be5b-31a7-a6e0-dce4e31e8c33 | -3.07505 | -61.2853 | 2026-09-21 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc04e683-9631-3c25-a91d-3f4915812844 | -2.91348 | -57.78921 | 2026-09-21 05:59:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8cf028d5-3ea1-36bf-81ab-c5114116f166 | -3.75362 | -59.41705 | 2026-09-21 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f110ffe-5d9f-31d7-b292-9e0f879ccbc0 | -3.4319 | -59.26495 | 2026-09-21 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| acfc5b0d-b83e-3402-b184-b01fa92d3bba | 0.69076 | -59.55142 | 2026-09-21 05:59:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc41384d-171f-36b2-bacd-d25f5564c685 | -3.75317 | -59.42014 | 2026-09-21 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b44d64ca-b274-3988-9428-4e60152db586 | -3.06292 | -61.27423 | 2026-09-21 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc0b637c-e07f-3a7d-b8fb-72fa926fda08 | -3.39063 | -59.53474 | 2026-09-21 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6f795ee-52b7-39a6-b92b-10652be47acf | -4.34379 | -55.67111 | 2026-09-21 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f0524f0c-09ce-33d9-a35c-7d15039b783c | -3.05458 | -61.2684 | 2026-09-21 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ddf5434c-60c4-3730-8c94-5730b29de1a4 | -4.34527 | -55.66081 | 2026-09-21 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d008046c-cb29-3cd6-8577-d5d8d72ae1cf | -2.60306 | -59.76041 | 2026-09-21 05:59:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 73421b34-176e-3f93-981a-2b099b7ba47a | -3.49136 | -59.61384 | 2026-09-21 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aa8e1807-da03-3ba4-8bda-84833e455e29 | -3.82182 | -58.89128 | 2026-09-21 05:59:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fcc33dfd-d276-378b-ab23-cdcd4e29edb7 | -4.08839 | -62.08598 | 2026-09-21 05:59:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b097174-c32c-30ce-8446-eeb3465b043d | -2.86888 | -57.81444 | 2026-09-21 05:59:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d130822f-a6f4-3295-be02-797230d8e8d3 | -3.05841 | -61.27354 | 2026-09-21 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 453494d1-3dbf-3970-b096-d0fdd481581d | -3.11002 | -60.72226 | 2026-09-21 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4735a0a9-cb90-3959-b892-14e796e48277 | -3.53853 | -58.68824 | 2026-09-21 05:59:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07172f3c-997d-3894-95c4-7b7c8da62ec0 | -3.66011 | -54.2765 | 2026-09-21 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c0e09b15-3cf7-36a8-b029-e89c0195477f | -3.40182 | -61.29554 | 2026-09-21 05:59:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 287cc1bc-b370-32e2-b824-aae1653f49a1 | -3.06606 | -61.2839 | 2026-09-21 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6e76d171-e9c5-38d5-8cdc-61739d34202e | -3.39155 | -59.52872 | 2026-09-21 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de0f9336-69ec-33d3-982d-011b40b56ee9 | -3.82338 | -58.88105 | 2026-09-21 05:59:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79ee311d-f1de-3787-9851-598fd221b89e | -3.43861 | -58.02452 | 2026-09-21 05:59:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 55d184f4-71c8-329f-8b2d-e51bfbf93b9c | -3.42764 | -59.25793 | 2026-09-21 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0df8e8dc-1947-33c6-b40f-6bf4f06919b0 | -2.90977 | -57.78767 | 2026-09-21 05:59:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7e51d730-3dcf-3b37-9130-6b607d2984de | -2.9149 | -57.79242 | 2026-09-21 05:59:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0ced4723-66e4-33e7-9e48-0d33e7bdc351 | -4.56444 | -55.75134 | 2026-09-21 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 94fa47cb-d627-379f-aade-7e82981812e3 | -3.59804 | -59.01365 | 2026-09-21 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dfb0d3a6-3d25-3eb0-9598-b376b4ab8279 | -4.34606 | -55.6553 | 2026-09-21 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2142b044-1ac9-3579-aa88-eb5ede3b03b7 | -3.4829 | -59.56691 | 2026-09-21 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0df95b3e-abeb-3c31-9be7-8020f528837f | -3.18923 | -60.432 | 2026-09-21 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8bc151c8-ea52-3cee-bbda-27c63b86287f | -2.64528 | -54.69369 | 2026-09-21 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a3b3464a-9bd0-33bb-bc07-b2f36162821e | -5.77015 | -57.59388 | 2026-09-21 05:59:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7979c153-9632-37ac-9b6c-ed39d4a402fa | -2.90213 | -59.227 | 2026-09-21 05:59:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 33091975-b060-3fe2-9b62-1cd15c2c318c | -3.48845 | -59.56467 | 2026-09-21 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 04067992-7ff0-3115-8595-1ee13be3d690 | -3.39416 | -59.53218 | 2026-09-21 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 270c1365-8adb-32b4-941c-314cf271e4f6 | -4.35123 | -55.66654 | 2026-09-21 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 46bb1f7d-87df-3885-a3b8-587eb86aa6aa | -3.82366 | -59.33803 | 2026-09-21 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca418922-0102-3a94-9849-55d9ff3015d4 | -4.1595 | -59.93024 | 2026-09-21 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f78044d5-a355-326e-bcac-9872fecf0b5b | -3.33593 | -59.44627 | 2026-09-21 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 833eb7c1-d36a-30b4-8dc0-1c0c628ebe2a | -5.01114 | -56.10072 | 2026-09-21 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ba5051f0-3f10-378c-aa44-60b9a7dbec79 | -5.75333 | -57.58257 | 2026-09-21 05:59:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dab900e1-e9f2-380b-a72c-4c3058aee5a5 | -3.40332 | -61.34655 | 2026-09-21 05:59:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 885ad1b2-87ef-3ad0-b903-313c3b4796e1 | -3.47882 | -59.59369 | 2026-09-21 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed07a8fb-e4cb-3d9d-b1fe-f2105b624450 | -3.75834 | -59.42092 | 2026-09-21 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 138737db-9df6-378e-9be0-50cb4a52c75d | -4.34452 | -55.66602 | 2026-09-21 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fe8a24de-8ffb-32d4-88fa-82ef83592684 | -3.49489 | -59.61219 | 2026-09-21 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cc7ab510-68c5-3ff9-8aee-3d9a567bb783 | -3.39395 | -59.58103 | 2026-09-21 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9f34e9a-196a-381b-a60a-58b06c6adce7 | -3.45127 | -58.39869 | 2026-09-21 05:59:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9df7afa-a2f1-35d3-a818-6a6e342304ee | -3.40113 | -61.30009 | 2026-09-21 05:59:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b3a73d6d-5aa9-3c1c-be88-2b6514fa1cd4 | -3.33454 | -59.83404 | 2026-09-21 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ff012cb-8c90-3069-a409-cf225a3dec23 | -3.14764 | -61.39839 | 2026-09-21 05:59:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1eeb2c65-00b1-3280-8793-5b0c64b57f4f | -2.99909 | -60.80242 | 2026-09-21 05:59:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2888f814-31a0-356d-b8a8-2c1e75fc5cb4 | -3.75744 | -59.42713 | 2026-09-21 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8d61642-3794-3f51-9fd0-9d75cd5e37c5 | -3.07269 | -61.1785 | 2026-09-21 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 468d2395-df8a-317b-8580-c65da373d00a | -2.87123 | -57.79887 | 2026-09-21 05:59:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb62f2f0-3a45-3fd5-ae1d-37ab192ea93d | -5.75872 | -57.58786 | 2026-09-21 05:59:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 911ca9fd-9c35-359a-abcc-25539d6b0108 | -3.05008 | -61.26771 | 2026-09-21 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0c508edb-c92f-3a03-83e1-0d560c43a28f | -3.39666 | -59.52949 | 2026-09-21 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50250bb9-5d06-3afe-b6dd-0ec058aa85a9 | -4.35197 | -55.6614 | 2026-09-21 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5929035a-e353-34b5-a82f-0394e0549841 | -3.39373 | -61.06948 | 2026-09-21 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2aa666e1-b7e8-329b-b829-5ab4a02fa851 | -3.89858 | -60.59511 | 2026-09-21 05:59:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 915ae5c6-5186-30fb-b82f-048c6f2cc266 | -3.3962 | -59.53249 | 2026-09-21 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f844dbf-f4a5-321a-86b9-2a8ef045e0f9 | -2.9011 | -59.2247 | 2026-09-21 05:59:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 32ca582e-d5f0-34d3-aa9a-3c9a6094bc3b | -2.91515 | -54.19553 | 2026-09-21 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a04c5295-971a-3fb3-904c-321f2cbf8566 | -3.45107 | -58.39812 | 2026-09-21 05:59:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d287f12a-58d2-37c0-b19c-3f9e34f85322 | -3.23267 | -60.79865 | 2026-09-21 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 83c7cf6c-f290-3679-a52f-6ea6484ca6cf | -3.33638 | -59.44321 | 2026-09-21 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 06019ccf-b90e-36df-8440-e39f470eba6b | -3.04558 | -61.26703 | 2026-09-21 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca597179-6452-3232-95f2-4a1ccac75cf7 | -3.3946 | -59.52916 | 2026-09-21 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b45d219c-e46d-3458-a767-6a5e11f4b7be | -3.07791 | -61.17454 | 2026-09-21 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6175adf0-f916-3e7e-8c65-bbb9931512fe | -3.82286 | -58.88446 | 2026-09-21 05:59:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84d4d396-24bd-3b5f-b3fc-5ea9ff34a457 | -3.66372 | -54.2733 | 2026-09-21 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9f902894-1881-39cd-97d5-09298b4fa797 | -3.44218 | -58.23307 | 2026-09-21 05:59:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90fd61e5-6fb3-3b0f-b4c5-da16fd02bdd5 | -3.06224 | -61.27872 | 2026-09-21 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8783c91d-59b8-3d3f-bece-d5f3246e6420 | -3.66109 | -54.26996 | 2026-09-21 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e8cc6bb2-b389-3689-8426-399d0e900534 | -2.87457 | -57.81528 | 2026-09-21 05:59:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README105.md)
