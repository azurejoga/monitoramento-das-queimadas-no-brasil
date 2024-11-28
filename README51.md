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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 93284836-baa3-36a2-9615-a942e2d594e2 | -5.71644 | -46.80403 | 2024-11-28 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ce1c0fe1-3cfa-30f1-b550-673c1525fa49 | -8.09029 | -47.06743 | 2024-11-28 04:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 67ff15fa-e2ab-3a55-89f5-bfca5fa21d20 | -8.12747 | -47.98351 | 2024-11-28 04:23:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eb0bf32e-2e20-3473-9460-9b638b976d58 | -1.64184 | -52.7318 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cbfaf38c-4c3d-3ba7-bb13-f43754c6174e | -1.28493 | -52.11064 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 297beb36-398f-39a2-b46b-05dfc0d6b703 | -2.71346 | -46.2205 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 902db27d-349c-3cd6-9041-440ed8cadcf9 | -8.13278 | -44.47436 | 2024-11-28 04:23:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 070f7b00-5999-3576-9622-55422137a8e6 | -0.6744 | -52.37128 | 2024-11-28 04:23:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11ce9b22-0e54-3410-adb6-708c04a340f3 | -1.6619 | -52.72972 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 39563cba-0c8c-3e0f-8647-a9ae814dc72b | -7.79703 | -50.00528 | 2024-11-28 04:23:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1576f162-cfb3-321e-a52c-b5ed19155fd7 | -4.15151 | -54.81386 | 2024-11-28 04:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0db8309b-396e-3898-b1e6-212794d1d6aa | -2.70779 | -46.21606 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29f7986c-97ab-334a-a96d-28e2fd228662 | -2.55429 | -47.32692 | 2024-11-28 04:23:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7b913d60-9d74-37aa-ae11-27520e2ea86a | -8.08753 | -47.06343 | 2024-11-28 04:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 69ca46cc-6575-393d-8d49-5e7e0eea01d4 | -1.34628 | -51.98975 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 94139391-d514-3c2b-97c3-9119803ccff6 | -0.86403 | -47.4245 | 2024-11-28 04:23:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b3be836-13e5-398e-9c32-4f65967c8f02 | -1.32663 | -51.93758 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| cb837b0a-4482-344c-af70-a3b8a9522cb6 | 0.94809 | -50.73632 | 2024-11-28 04:23:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5588596b-b570-398e-a150-27217ac2f32f | -1.28938 | -54.55807 | 2024-11-28 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 048b0a4e-2a34-348c-a60c-2de523cc1a36 | -6.93528 | -39.25764 | 2024-11-28 04:23:00 | NOAA-20 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b56de72f-59fa-3201-b3f6-c13c43a892e0 | -2.60339 | -46.83724 | 2024-11-28 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 18e72a22-be52-32da-bd4c-87d5d761cd87 | -0.23981 | -51.59715 | 2024-11-28 04:23:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 50801657-da77-3fee-a1c7-e262b7ecd35a | -2.09423 | -46.55276 | 2024-11-28 04:23:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29993f69-00cc-3fe3-8a6a-943fab7588b7 | -7.54555 | -46.60347 | 2024-11-28 04:23:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e5bde33-b87f-35df-8321-2f7038253a94 | -2.59525 | -46.25918 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 880c2a97-6461-3f3a-8172-09445138bd01 | -6.0994 | -43.9702 | 2024-11-28 04:23:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 8fe7094a-59ef-391b-be21-f132e7c37229 | -7.39468 | -47.80717 | 2024-11-28 04:23:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d545f81-6bc7-3e83-8dd2-0d8d0cc243fe | -2.72402 | -46.28293 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e45f6bb9-4adb-3c90-8001-ded82be2af3e | -6.12123 | -46.58669 | 2024-11-28 04:23:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 132780f3-3ec0-383e-9c10-e3509bec4eec | -1.3506 | -54.63284 | 2024-11-28 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d850c12-c1ae-3fbb-bba1-3a183f0637b6 | -1.08942 | -48.20907 | 2024-11-28 04:23:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f30839d5-06ac-3bca-bd14-fae93fdf90f2 | -0.26795 | -51.62533 | 2024-11-28 04:23:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a286280-a505-3bed-a591-7294d54c8c17 | -1.55315 | -52.2789 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b44d55cc-3380-3af7-8f20-ffe3b822afb8 | -1.44232 | -52.59903 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 996dc565-7625-383a-aa59-58a54178b7b5 | -6.86784 | -44.75815 | 2024-11-28 04:23:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9704cf4e-e884-332b-badd-bd10973d4af8 | -5.51314 | -46.26345 | 2024-11-28 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58813934-0976-3b17-b3b0-e074ce608359 | -2.71457 | -46.23496 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48c6a866-829a-312f-b0f7-daad648918d8 | -2.84052 | -45.3285 | 2024-11-28 04:23:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ed56df8f-02ea-3be2-8dfb-faa350e70cf1 | -0.58312 | -51.71021 | 2024-11-28 04:23:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad21d41a-fb4a-3dba-8e80-6e8c0ccef776 | -6.67074 | -47.87764 | 2024-11-28 04:23:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 51d3964b-5497-3ccf-b27b-6e8584d9ba8e | -1.31023 | -47.81173 | 2024-11-28 04:23:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 678b861c-71a3-32f5-b432-3244045437c9 | -2.54696 | -46.39499 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29651c1a-029e-34bb-93c2-37155966a42c | -8.08974 | -47.0709 | 2024-11-28 04:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| acb3ebdb-91c9-35f1-b2b5-07b4ef0ece59 | -9.17266 | -44.72469 | 2024-11-28 04:23:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f241a8ec-931d-3473-8464-5f85a592887d | -5.82897 | -44.10986 | 2024-11-28 04:23:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 968a7701-980d-37e5-a938-cc7b5504989e | -6.34955 | -47.3079 | 2024-11-28 04:23:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a9a82aa8-7e67-37b1-91bd-176f0e4751df | -1.70815 | -46.24277 | 2024-11-28 04:23:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab3ff82f-ad52-3b81-b2c5-4011aab9f630 | -6.09112 | -48.03922 | 2024-11-28 04:23:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 1bb71b3d-2cc8-37c5-93a8-481aa9c2f2db | -1.57882 | -52.26804 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 288f7ade-5960-328e-b90e-5705128b6f78 | -7.48494 | -47.17846 | 2024-11-28 04:23:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1d40ed4-b586-3fc7-9a90-46df34d7ec8a | -0.02519 | -49.63364 | 2024-11-28 04:23:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7e21ce1-89a4-3458-a334-6f0c029ce9f6 | -0.94347 | -51.6577 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b1fe9b1-48de-3067-8a0b-3c7105ff3a65 | -2.02216 | -45.69276 | 2024-11-28 04:23:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9713911a-bc4f-3c82-b956-c15153544c6c | -2.53102 | -44.18341 | 2024-11-28 04:23:00 | NOAA-20 | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42827322-3751-31a2-a393-617a0e5cc1bc | -1.86766 | -47.85807 | 2024-11-28 04:23:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1a4b2f84-b5f2-3a7e-bd8f-978e75b29268 | -2.68738 | -46.28081 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f91759ac-aae3-32db-9d6c-79b648494126 | -1.65876 | -52.71473 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7006cdfe-8440-3a6f-80bb-38e23a764f29 | -2.27801 | -46.37442 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8e808862-d536-3824-b648-36e2427a5729 | -2.54362 | -46.39446 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 39a613a9-0c57-3330-b3dc-a829466b4809 | -2.70168 | -46.21152 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d5c9233-0345-3622-b122-0f719de9ef38 | 0.70434 | -51.44848 | 2024-11-28 04:23:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9f6106e3-6fdc-34cd-ba46-b41ce0fb162a | -3.09885 | -53.82142 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| badd6c9d-7ec2-39b1-b92d-ee576679eb1e | -2.96008 | -51.00486 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d2c2dbde-9e18-33be-a143-561aef662e88 | -3.9805 | -46.65178 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ffe17ec8-6ee9-3762-8b92-c18a285468e9 | -3.61974 | -51.36854 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39b05766-8575-3fc5-ae1e-da1858569889 | -3.48879 | -50.44762 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 12af93ad-de5c-31ba-af62-6d39019b5341 | -2.71998 | -48.67216 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 993012f8-cfe0-3d33-a974-25e24201faca | -4.14549 | -40.75708 | 2024-11-28 04:25:00 | NOAA-20 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ddc45cce-5d22-3df2-b4e2-5e88df72f053 | -16.19843 | -43.38668 | 2024-11-28 04:25:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07a379d1-1471-3d36-9905-3ee5b9ae9d5f | -2.83458 | -54.12347 | 2024-11-28 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7852383e-17cb-3741-b16b-c93850cd027f | -3.3076 | -50.27792 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 0a1c6b68-5045-3e64-9c8b-3a7a5f27b41b | -4.65806 | -46.92467 | 2024-11-28 04:25:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17a1f5ec-b82f-3004-8ab9-bf031ca2be1a | -2.31796 | -51.96343 | 2024-11-28 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2fc4663-3d12-3e3b-9d5a-ef678d5baee9 | -4.17866 | -48.62402 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84fe466d-a11f-3d65-aa5c-8d5664746f22 | -3.10258 | -54.98232 | 2024-11-28 04:25:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7ec2cee-0604-3eea-81ff-737128d505ea | -2.30967 | -51.95738 | 2024-11-28 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9589c10c-d91d-3eb2-80eb-d1d1039aaf68 | -4.11832 | -48.52807 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3360308c-51de-34fb-bbe5-8b3fd9df8666 | -2.18146 | -53.77723 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be2fe259-ec6e-38bd-ba6e-a77c8bbcc44d | -3.77586 | -47.4734 | 2024-11-28 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c3c4f004-5e6d-3bf2-be69-60bf6d7b3ee4 | -3.34247 | -53.74183 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bb36a951-21a0-36da-bb74-49e66ff4ddf5 | -3.8095 | -46.59595 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c68688d5-0099-3eb9-967a-b54a3571a518 | -3.24014 | -46.43561 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d00762e-58ee-360f-b70b-c0a7755593de | -3.34602 | -50.19053 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5b05b42-9494-3450-bcb5-332bccd04bdc | -4.6614 | -46.92521 | 2024-11-28 04:25:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c05c18fd-8f05-35c5-97f3-df372f1be776 | -3.77169 | -46.68359 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e9db323-6404-34b2-b1ac-86dbddf1e611 | -3.29846 | -50.35958 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 025ee88e-778d-31d4-8bfe-17f836f3f628 | -6.24929 | -37.21051 | 2024-11-28 04:25:00 | NOAA-20 | SÃO FERNANDO | RIO GRANDE DO NORTE | Brasil | 2411809 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 260781d0-cc49-3961-9343-801ad43fe7c6 | -2.60108 | -51.79366 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ad7b7454-21c9-3167-b410-18cb1f9ca47d | -3.11869 | -53.76286 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9aec17d-5b9a-3f0d-b581-7fef8f1150b8 | -3.37238 | -46.65381 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79318a85-19bd-3302-8907-0e5879f1cd6b | -3.93776 | -46.51598 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c9ccd85-a8d5-38f0-addd-9a78c6358a18 | -3.9392 | -48.15717 | 2024-11-28 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0dab83d8-1a57-3cd3-9e13-b2e890416ba6 | -2.43416 | -50.41829 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| def7e7c4-6ae0-3a10-a821-7378ad26d286 | -3.96571 | -48.08179 | 2024-11-28 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d55920f2-05d7-3446-ac26-a30dd5fa90f9 | -2.58727 | -47.47402 | 2024-11-28 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fc983d44-4f5e-38b1-a8f7-041b839bea26 | -4.80774 | -43.29787 | 2024-11-28 04:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 74b01b8c-91e6-31dc-ac4a-dd586b71965e | -4.0458 | -46.83923 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a911d563-aedc-3676-8c6f-8ce4b3b1b53f | -2.8784 | -46.85374 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2fb2600-de73-32a1-b6fc-fec912df9bb5 | -3.77116 | -46.51468 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e977b297-c577-3a5c-b84a-edacda6a7dce | -2.85761 | -46.85413 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README52.md)
