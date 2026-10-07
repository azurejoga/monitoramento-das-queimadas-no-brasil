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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bdc36827-7928-3cb7-8420-497a490cf7d4 | -2.95623 | -54.10955 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1e65dc4c-aa4e-3f10-ba1b-9e21b9b06ea6 | -2.8753 | -54.14737 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b63eba8a-e11a-3eee-a392-c8550e4dd71d | -3.98165 | -56.2174 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8c3ba76a-a1cb-3673-8b7c-afa03e58486b | -3.49972 | -54.66126 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 60384309-fbf8-3d7a-b686-f5b3955cf43b | -6.69483 | -55.20405 | 2026-10-07 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c3fb3b8-c0f0-3024-804b-6d15d8907463 | -2.92912 | -54.15208 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99d0c82a-13d8-3472-bfd1-294fe78f34cb | -3.60912 | -54.59286 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 83424bca-48ef-3568-8c4b-abc0269f4d71 | -3.03313 | -53.89695 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87bee480-c5a4-3de2-ba74-bbd5391e0076 | -3.25004 | -53.87943 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a341c17d-152d-3212-85ec-59c1bf1f4e10 | -2.76625 | -54.10498 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 8beb5981-2397-3df0-9795-823d4fd90876 | -2.25391 | -51.93539 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c7cffd7-e094-31d1-a7d1-571ee5bb232b | -1.6267 | -55.13076 | 2026-10-07 05:04:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 200cb18b-1a76-3335-acba-14f029b9155e | -8.44198 | -46.41001 | 2026-10-07 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d9ce5cce-443f-31ef-906d-7a9e797add7c | -3.1824 | -50.55791 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 21427b9b-d746-3d9a-a9d1-9a4d62671db9 | -3.39284 | -59.59581 | 2026-10-07 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f6dde336-ba0c-3dcc-a602-4035ee197ef1 | -2.88025 | -54.13739 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b97094f7-9471-3b6b-bf05-5fe363d9c3d8 | -2.15366 | -51.9756 | 2026-10-07 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d02a173b-4258-3009-bc26-45522658f367 | -1.28634 | -56.9821 | 2026-10-07 05:04:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6f6a5068-f2d7-36fc-a850-ad9273a7ae1a | -5.73227 | -45.16783 | 2026-10-07 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 1fb88158-1f17-3ff4-a10a-e38f3a9db07f | -2.88676 | -54.09529 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34e2786f-84bf-30d8-aab3-5502bd6a1ced | -4.30453 | -50.78807 | 2026-10-07 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 98f6a730-9170-34e9-a6a7-885b62bd300a | -3.73395 | -59.45132 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2770e233-5baf-3f93-8ac7-bdfdd3f98224 | -1.1081 | -54.15763 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05e8f6db-21eb-3aff-9249-02ac5c9dc20c | -3.11515 | -53.76715 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b20c98ff-c5de-35fb-84af-11f7d9197d08 | -3.50857 | -54.66973 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cd770c41-a48f-3f9a-87ef-50c97e7802fb | -3.28152 | -54.18106 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86962863-df7f-3736-b3d8-4aaf5c3b80bc | -4.12 | -50.81363 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9630b0ec-9c74-3ea8-80c4-ee3d9619b6c5 | -2.5986 | -57.54609 | 2026-10-07 05:04:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0326e510-84eb-36f7-a22a-c4a9fc3a36fe | -3.73619 | -51.21193 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 400db3ab-8723-3d66-b32b-18c3462125d8 | -3.49741 | -54.63254 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e64ea42-837c-32d3-ab9b-71fa69059948 | -3.62453 | -55.27926 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e96d2a4-42bf-3ac0-aa83-9e5cdcbcdce5 | -3.21928 | -53.87835 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c45e4430-3da6-3797-b830-0ffc19e5673f | -3.06317 | -54.22992 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4bf5101-9d27-3bfa-b6f3-a083dcb9bb54 | -3.5068 | -54.63755 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1267ca01-843f-35fd-9e94-33354c6a0584 | -3.26961 | -50.40849 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3be9c37-1041-3025-b3c1-fecaf46c7412 | -3.73919 | -59.44269 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3d4ad7ae-06e8-3cc0-a7e7-9b55c0fdc5cd | -3.27307 | -50.41257 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 312be850-5897-33a2-8402-cbe1fd9aee0c | -3.29885 | -54.06844 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e1e0d035-4dea-306e-b5f2-de585548323c | 0.68652 | -60.07623 | 2026-10-07 05:04:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 707edfe5-25e8-3b46-9792-4fdfac2e809f | -3.52775 | -54.6337 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 65842304-f0aa-3d1d-9674-e674a357285a | -3.03368 | -53.89339 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9b2c5a3-f05e-30ba-8f22-32648b0a7b2a | -3.06029 | -54.20439 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c65d4295-f38a-3a30-8a1e-8bbbeb6b8627 | -3.06049 | -54.16134 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9b567dcc-2652-3bef-a053-a4b490c024bb | -1.28332 | -54.5617 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16b1e3dd-83f8-3d1b-877f-caab7633a564 | -4.26944 | -54.87662 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19d22de3-c9d9-3f13-935b-09cff6fd26c8 | -2.20968 | -56.91782 | 2026-10-07 05:04:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ccbec680-d7af-31dc-af4c-1f89955d6241 | -1.38092 | -56.89312 | 2026-10-07 05:04:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16c85aba-3b75-3c52-bbbe-e8a2c4dbef90 | -3.67094 | -54.54541 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4934bae-1d79-3010-bc79-eae735a62d55 | -3.38357 | -58.20367 | 2026-10-07 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e506d6de-4491-37b5-98f2-9f060305140d | -3.62729 | -55.2832 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b6ad24f-4a50-37f2-9d33-703b8ea90258 | -3.56557 | -54.47932 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 095c1e2c-1295-34ae-bd02-a1ca754a9147 | -3.27551 | -54.0252 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6d233206-acac-3883-a8ad-7c5d3cd907f2 | -4.92517 | -55.86432 | 2026-10-07 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ed62cfc-1a4b-3376-bdf8-2422ad156812 | -3.71517 | -59.69398 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ca5bc1a-8d90-3bbf-93b5-61872078667c | -3.0405 | -53.93806 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7d5a0f1-4a2d-38c7-acc7-2b2306b2bad1 | -2.97903 | -54.048 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d08181c2-9fa1-3ba6-8cdb-c51a14a920a8 | -4.45865 | -54.97021 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9b092f4-f417-362c-bc9b-276b4b3d74ab | -3.09452 | -54.15933 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31f71a74-a15c-3a38-b55e-b5ac2c32b40d | -3.09154 | -53.71947 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 966de8e2-4c18-3d08-b704-218f4c2d60d6 | -3.28058 | -50.14434 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 02674baf-0058-37cd-8ed3-c3c27889c3d4 | -3.2811 | -54.03331 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| b091f80a-9671-3fe4-ad95-02d9a59c08fe | -3.42419 | -59.56425 | 2026-10-07 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2fddeab6-26d2-38bc-a3aa-fddb279c3282 | -3.63059 | -55.28371 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 768dd652-a013-3cf0-85a1-d3aee6b1082f | -4.13473 | -54.90889 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4c7fb2c0-2954-3f52-9378-b609159b6632 | -3.07677 | -54.16381 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3484c52-c56a-3dce-9b09-3b0f956f7dec | -2.23891 | -55.06537 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92f0125f-97f5-3fb2-a9f8-4020a4868e2f | -3.02301 | -53.87355 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b1c2a8b7-0b42-322c-8287-11e3f8bb60b1 | -3.01415 | -57.73992 | 2026-10-07 05:04:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db41b31a-91dc-3390-ab58-b779f52176c0 | -3.2672 | -50.39747 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5da95dae-6f6c-3bd4-899b-8f90566dc0c0 | -1.80046 | -57.10656 | 2026-10-07 05:04:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 31caef3b-cb22-3cba-ac9e-a2597964cecd | -3.99999 | -56.27367 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ae83fda-10bc-35df-9130-0484f9ac40fe | -3.15837 | -50.82768 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e9a8f47-ab4e-3608-b143-8f885b413a2e | -3.52558 | -54.64756 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 17e94645-9eb3-35fd-bac4-5163e7ded139 | -4.16554 | -56.34651 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a32459b-5ea9-37d8-aea6-2c9c3d7a1a9d | -2.77345 | -54.1025 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 78739f87-243e-3337-b430-b423c8324d92 | -2.99402 | -54.03949 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 186b7240-000d-3926-ab6e-693520478d67 | -3.03819 | -53.90864 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 38a0bc44-94ac-3a7c-ab82-2040e21c72e0 | -3.09057 | -54.29496 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| f7e17caa-83b8-3b04-ad4c-c5798d17bfac | -2.87971 | -54.1409 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d12ee8f-c379-3c3f-a7d3-aaaccfe59ab5 | -3.29393 | -54.03889 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 02b6b102-d362-3c04-a694-ffeddcd04632 | -3.02643 | -53.89593 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0fef124c-c4af-307c-a692-bd8117b8ab52 | -4.75704 | -55.65461 | 2026-10-07 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4161456e-b580-3504-a626-5213325e0c4f | -3.58862 | -54.30763 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 23d0fed8-c0b2-3383-9665-b07ce6a308d4 | -3.38776 | -58.20021 | 2026-10-07 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 70395576-4ae2-3863-975c-854082862e91 | -4.77544 | -50.8098 | 2026-10-07 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9163351-ee03-3fff-b45d-e30ee0645e6c | -3.74693 | -51.21839 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 177e0b82-7a6c-37b0-91db-8e80bc5125e0 | -3.04649 | -53.87713 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 08fe6e74-1cd9-3701-bc1a-e323e86990ee | -3.085 | -54.28696 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ebb6c22f-35ce-3380-84bf-8c0a73b82d00 | -1.56694 | -47.74084 | 2026-10-07 05:04:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ca4ad80d-15b1-3001-935d-4586ff6ad386 | -3.00875 | -54.12103 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 16b73edf-f251-386b-b557-f899ad746184 | -2.94891 | -54.06886 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| f0d632d9-8233-33bc-b16b-d29049b5200c | -5.67917 | -53.50072 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 80047f67-a384-3d8c-97ba-5d088b9f8f4e | -3.19103 | -50.55407 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 84855b65-6db7-3aff-acec-cd6414fa0897 | -3.09335 | -54.29896 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8f776f11-193f-3c0a-ae23-30dd4020bff1 | -1.28279 | -54.56513 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 183d7431-f770-3d3c-a79d-8fd8d79bcfd1 | -3.48798 | -57.77925 | 2026-10-07 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 365de4dc-c432-3442-9cce-e6aa0d4f4994 | -3.47599 | -59.46169 | 2026-10-07 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2d60f47-7713-3785-af4a-0bdcd0cdf23e | -3.10954 | -53.75895 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8bcdf262-63c3-3ad9-9392-976837d24bb4 | -3.52451 | -54.32665 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1cf561d-902c-3f64-a2bc-2f5502d8c4e4 | -2.8052 | -54.13969 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README67.md)
