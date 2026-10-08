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

## Dados Diários - Página 157

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb1cb961-3890-37de-9763-39dac8d598d9 | -3.30251 | -54.05095 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9c44fdf2-1f71-3b8d-b8bc-ce4414263984 | -3.59191 | -54.66737 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 05445a59-a1fd-3787-bb0b-b128c0fa2a86 | -3.00339 | -54.07439 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| e648c342-6e3b-3887-ba82-9dc7fb5957f0 | -1.0873 | -54.10808 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f77bd6d2-29a6-3bfd-965e-d6d886bf3e67 | -3.09262 | -53.73289 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a19bcd30-3869-332a-8c17-e51e23132486 | -3.29917 | -54.02635 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4b845fc9-eeca-353c-b295-32837a103333 | -3.08262 | -54.28252 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a1d6923e-edeb-3fca-93a1-aac05421fa2d | -3.07566 | -54.2814 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7a1a5670-f935-3702-b48f-cb870f25bed5 | -5.22394 | -60.24389 | 2026-10-08 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51249803-e21d-3fc7-8710-2e736f7db467 | -3.16381 | -54.72828 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07b324ac-fc30-37cc-b5ce-f7919d0365b0 | -2.7718 | -54.07623 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3650a521-9582-3d97-af12-ec07c450634c | -1.0531 | -53.59222 | 2026-10-08 05:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a87b8f36-4e76-3491-a505-df25a814ec3d | -3.16097 | -54.72404 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8493c0b-98e7-3582-acbf-57a3864f1654 | -3.01041 | -54.07548 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| fd0d7f95-4bc2-377f-baeb-f59efaa126bb | -3.60079 | -54.56514 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 77eff664-ad4a-3bfa-9476-375f816fd9ed | -3.09096 | -58.02853 | 2026-10-08 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ddd07234-fd3e-3536-a678-8387d46422a7 | -3.58276 | -61.62646 | 2026-10-08 05:23:00 | NPP-375D | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7b582d0-8f80-3798-a1ff-56a526119ef3 | -2.70372 | -56.52856 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 723ede68-ef62-31e6-aa9a-696316b581e2 | -4.27135 | -54.86892 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bdbcb60c-429a-3e64-b313-dad79d209c48 | -2.48183 | -56.08973 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8790b2e9-9139-30fe-b779-7a42b210acd9 | -2.55107 | -56.29162 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1b1e2f5-0a86-3afb-b0bf-84707c5c15c4 | -3.73422 | -54.6506 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e76df4a1-3bf8-37d0-8c3a-dd7c10585bd4 | -3.55504 | -59.47393 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a1d5b8d2-5d0a-3864-8380-487e14c04d98 | -3.44871 | -59.82927 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 232b2195-0401-3ead-979e-660f74e511bd | -1.10718 | -54.16063 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e139d77-e277-3709-aa87-e1e95a4309fa | -2.48629 | -56.1046 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 726aa6b9-52ff-3257-9a4e-a3b2f61a2e31 | -3.11654 | -53.78981 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b9a04354-fcbd-31a5-9875-078fc9a74507 | -8.61253 | -67.02558 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| afa0170f-1803-3aa9-9acc-fb90c3368290 | -3.53717 | -59.47107 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1e45629-3924-38cb-b653-b9ccc84d640b | -3.16207 | -54.73935 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 05b2c57b-921a-3499-973b-4f7df76e9a3d | -3.13041 | -53.70169 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1d25406-b3c3-3077-8a5d-2dea05986648 | -3.84591 | -55.91535 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 694dfd8c-0f6c-3c2b-ba56-cd001848d692 | -2.49025 | -56.14419 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 25b3909c-053a-3126-9b4b-f05b3e6fe02a | -2.75992 | -54.1059 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a3055a0-9b1e-3e0a-844a-3446fdf70589 | -2.98934 | -51.04743 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 630eb5f9-726c-34f4-8b81-f755375e89ae | -3.47974 | -54.62369 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eeee4059-4670-3ab3-ace8-4fb26ca41e95 | -3.04739 | -53.9534 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 5536fb8b-e301-3a8b-8e65-6e51690d3dc9 | -4.26769 | -59.88639 | 2026-10-08 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d1d6d44-14a2-3405-83cd-f31b53b7ee94 | -3.84654 | -55.97638 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d7ef6591-b1d3-3b1d-bd4e-018dc91b6a63 | -1.52162 | -54.51639 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 281369b0-7d12-3b75-8650-1f494391d679 | -6.89841 | -48.71389 | 2026-10-08 05:23:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f9562b3f-b093-31ee-9145-d119a3485ead | -3.53436 | -59.4094 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35a7fd8b-e93c-35ba-b2e4-fa2277ea43c2 | -3.05172 | -54.39012 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc72f0ad-20e1-3421-9f0a-2cb86ef61e4a | -3.30789 | -54.03977 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8d0fc25e-f47a-38f1-b144-94dfd0200bda | -1.29166 | -54.55922 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de454b65-a638-3c7c-b241-44de73d9673c | -9.53897 | -64.81689 | 2026-10-08 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96ec41c0-d755-3930-9863-8751038f7017 | -3.02633 | -53.92597 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 6259935e-f265-3570-bbd5-52324952c948 | -3.54399 | -54.66432 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56967d0d-34fc-37b0-8246-21dc508e4445 | -3.28322 | -54.03597 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84d56156-d125-3254-9e16-6fce22b02160 | -2.94056 | -48.86518 | 2026-10-08 05:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 921c89c4-9fbc-3792-9609-ee4906ea89b1 | -3.70227 | -55.96468 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63938a20-7230-32c6-98f3-7417e353d03d | -3.08745 | -53.95151 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| df99fef3-0d45-36a2-a704-9d96594615ed | -6.72279 | -55.05934 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eeb55949-ae8e-3f68-8a32-82bc11db44bf | -5.29838 | -60.08762 | 2026-10-08 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ffa91f09-6a6d-3f0a-b6fc-58d7d2d50731 | -3.0649 | -54.25333 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 14053409-aa30-3ce6-98fa-eb49cc46dd80 | -6.23391 | -52.84921 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 257ebc13-34b0-31a9-8f2f-b70562c990f2 | -3.4749 | -59.5742 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 04b68fd0-4f78-3bc7-9e48-9612f8ca087d | -3.07519 | -54.23832 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6078c013-8be1-36ce-a11a-b336a403ad44 | -0.42073 | -51.73339 | 2026-10-08 05:23:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ec795d6c-de35-3cdd-88dd-06e752cbb5c2 | -3.65575 | -54.28114 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f683c0c5-7a0b-332c-9e10-b7cc528f4969 | -2.78493 | -54.08922 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 800ac283-b9bb-3065-a978-bc4b0e76a88c | -3.52488 | -59.35454 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c6f0811b-cbf4-3c61-ab79-02262e514025 | -3.2777 | -54.07108 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ccd8eb1-4bda-3b41-aa8d-ed39468dfe47 | -2.76677 | -54.11397 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 266d5a16-765b-36aa-b867-3caf26875c1e | -5.6992 | -53.48927 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 157112c1-bc9e-3127-958a-143f85abb044 | -11.81003 | -47.34495 | 2026-10-08 05:23:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05584cbb-96f6-315f-8c1c-25f6dbc73697 | -3.77533 | -59.25503 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df4135df-8a63-38e8-ac7e-146625df3b55 | -3.84926 | -51.92784 | 2026-10-08 05:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88de3fa5-6b5f-3ce8-b8ed-a3a45ccc883e | -4.07147 | -51.03989 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| eb67099a-7720-3ab5-a342-c45a5d1d8468 | -3.53877 | -54.67502 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 81a9c093-640b-3df1-b33d-2099b623888e | -3.49412 | -54.62211 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 219b4681-5483-345a-a649-1f9968fdbadf | -2.94156 | -58.00132 | 2026-10-08 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e815e9ee-6b74-3584-8d48-a31986f1536e | -5.89698 | -53.50664 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c95d8d9-cda8-3a8e-8deb-f48f1baf645f | -1.97521 | -56.0632 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| afdba687-9138-3928-aa05-50c4435981be | -2.98682 | -54.13514 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c0f926f2-c172-3c84-abfa-c68824f8649a | -1.99854 | -56.95644 | 2026-10-08 05:23:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a8cb99c3-f1b8-3664-b9a9-129fbf276530 | -8.72189 | -45.17066 | 2026-10-08 05:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0dc11524-23d9-34c7-82b8-3eb8625ff07f | -3.03086 | -54.08262 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fe1f4cd0-5461-32f1-940a-66de200ade37 | -3.97175 | -59.3573 | 2026-10-08 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a5a302b-a3a4-3b83-a7fb-15944f2f96e3 | -2.76114 | -54.09822 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9981d066-f69f-3361-ac73-26d703607158 | -3.45135 | -58.04779 | 2026-10-08 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0acd1d7-192c-349a-95e3-d532d86d54b3 | -3.11216 | -54.1613 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 46fa85ac-212d-3495-a0fa-b8d880d2b6dd | -2.92119 | -54.13697 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae33cf46-be67-321f-abb3-10f3b8e8a8f9 | -2.98816 | -54.07995 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 77cb95af-cb74-3678-a711-143948dd4651 | -3.73012 | -55.98337 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae6bc5e1-f8bd-38d9-bfcf-fba477fa562c | -2.99705 | -54.04557 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 936cf102-6724-33b9-b5df-10af731fd91e | -1.0218 | -53.72289 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b4913f50-2e83-34f7-820c-ee6f0a423c27 | -3.00821 | -54.76104 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d75fc104-f439-32f2-8ecf-c688006f7071 | -2.82254 | -57.60816 | 2026-10-08 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a0fc7c0-9965-316d-9613-2598a0b502df | -4.1393 | -54.2534 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db6cb5ec-0ee5-39c2-b6b6-b85f4806bde1 | -2.96899 | -56.623 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9eb1191e-4799-3aac-b7bc-84571db43093 | -3.58048 | -55.60369 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 58c01505-df5a-37a2-bb6e-2af45f82dae0 | -3.70561 | -55.96521 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 672430bb-76c3-34d0-ae55-4f46458a5c97 | -3.30913 | -54.03193 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 59532345-d36f-3e4c-a771-0a876d9772e1 | -3.10697 | -54.14852 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba8d6d73-ff34-30c5-9379-39a1a11a7c32 | -2.95956 | -59.32235 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1b0ccce-7334-36e2-9546-545398403b2d | -4.15967 | -55.14205 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d0ce556b-76ae-38af-8517-dce17153d88e | -2.50121 | -56.07504 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| eb153e64-fff1-3ef0-8d44-67188b91a13e | -3.69998 | -50.65583 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08343655-01bf-3b12-bc00-d100ab116db6 | -3.65012 | -58.89032 | 2026-10-08 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README158.md)
