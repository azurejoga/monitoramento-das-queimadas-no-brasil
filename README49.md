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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d1846f4-4825-350c-9163-7661db1c5503 | -4.62824 | -45.5714 | 2024-11-21 04:31:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63c73b66-b054-351b-93b7-4bf8e9a05ee6 | -3.77407 | -54.2226 | 2024-11-21 04:31:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27f8dd5b-7778-3105-8b23-95fbc82c3eb3 | -4.75522 | -44.34375 | 2024-11-21 04:31:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f18b002e-4577-391c-9189-fe5cea8b660a | -3.75025 | -51.07484 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7fc7c18d-7359-3dea-8670-07f91ac3dc0a | -3.28758 | -53.85929 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3f6f7cf-40b0-3764-ae20-921986d80017 | -4.68991 | -48.97618 | 2024-11-21 04:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9615e52e-7833-3cb8-b499-4caa43ce213e | -3.46686 | -54.56306 | 2024-11-21 04:31:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7a5610b1-bdf9-3b3b-9034-c9a3febef250 | -11.84892 | -52.33953 | 2024-11-21 04:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73a7b8f8-efc3-326f-9b29-6028f4ed47af | -12.60383 | -48.52224 | 2024-11-21 04:33:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6874ad6-788d-3275-b197-c758eb6d992b | -18.43016 | -40.5515 | 2024-11-21 04:33:00 | NPP-375D | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| aeb83574-1553-36cc-93a5-11834c4cdb76 | -12.01159 | -47.46793 | 2024-11-21 04:33:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15aff08a-cfe5-3290-a632-bd9d8dbaa5ca | -18.43056 | -40.54772 | 2024-11-21 04:33:00 | NPP-375D | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| bb5ad032-6454-387e-93ef-06060a6c7548 | -12.69215 | -43.37408 | 2024-11-21 04:33:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc243c5e-1f57-3e70-b67a-131f758c1bf0 | -17.59233 | -43.28465 | 2024-11-21 04:33:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d7d647a-e6f2-3cfa-b4dd-0457ff9c4b0e | -12.59661 | -48.52472 | 2024-11-21 04:33:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b209318-0217-3584-a1d1-b238a75170d8 | -18.42463 | -40.55084 | 2024-11-21 04:33:00 | NPP-375D | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a59b117f-a4a4-3eb3-984c-99fbf26c722b | -12.85589 | -43.82114 | 2024-11-21 04:33:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2cb604b-a441-3e9c-94e6-13243a3b7d6a | -12.33816 | -49.99615 | 2024-11-21 04:33:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 753632af-e6cd-3213-a1f0-f11057eddf9a | -12.85639 | -43.81738 | 2024-11-21 04:33:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2391ddb5-7143-3852-b00d-cc17ae16ddad | -11.84527 | -52.33887 | 2024-11-21 04:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bdf909ad-fa64-31e0-8f64-18803b2b4ead | -17.56615 | -52.39645 | 2024-11-21 04:33:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e58c7c0b-c5f9-3b71-9146-26428c651675 | -12.80294 | -51.49159 | 2024-11-21 04:33:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05ddbbdb-d940-344a-8e49-d222690d85d3 | -12.78944 | -43.86201 | 2024-11-21 04:33:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| faa2f03f-0324-314c-bccf-456abef2db7d | -12.69277 | -43.37566 | 2024-11-21 04:33:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f60e4dc3-1f57-3589-a1fd-a893201e3f2d | -12.58188 | -52.49282 | 2024-11-21 04:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f34b2669-a098-39e1-8bc8-83859986f8fc | -17.58776 | -43.28407 | 2024-11-21 04:33:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c005817-1c50-3607-bb84-b0b967af4bed | -18.42503 | -40.54707 | 2024-11-21 04:33:00 | NPP-375D | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 00dd92a2-eeaa-358a-a418-97bdbe090164 | -12.85421 | -43.8181 | 2024-11-21 04:33:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 36c13ae0-e223-36b3-a413-c12a15a9cf77 | -13.53365 | -42.97568 | 2024-11-21 04:33:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7da6e76c-d54d-369b-99e6-dd81634bb34a | -24.24249 | -50.74095 | 2024-11-21 04:36:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a9b09045-6a43-32e5-8634-16bde2627f16 | -24.01459 | -54.22597 | 2024-11-21 04:36:00 | NPP-375D | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 13c9d1da-79f6-3347-bd97-39fd33299079 | -20.0568 | -50.45415 | 2024-11-21 04:36:00 | NPP-375D | TURMALINA | SÃO PAULO | Brasil | 3555307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 72b43887-982a-372d-b9c9-763b8a4a1a22 | -22.54158 | -48.81153 | 2024-11-21 04:36:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a926dae-0a2a-35f7-8f41-ca469f5aff6b | -22.22001 | -49.74845 | 2024-11-21 04:36:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 063ec106-0246-31d0-b2f1-21eb629b6347 | -3.2768 | -53.8199 | 2024-11-21 04:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| b2fc5735-e67c-3880-9871-111a81305e1f | -4.2575 | -46.1188 | 2024-11-21 04:40:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 5e69d3c1-298a-3462-8a46-3cd47ebe84a3 | -3.2767 | -53.84 | 2024-11-21 04:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 6e569ff7-8b08-3c4c-a3cf-7a47edaa81da | -4.2388 | -46.1197 | 2024-11-21 04:40:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 5c124251-2e49-328a-ad70-47f76a302f70 | -2.0259 | -54.5289 | 2024-11-21 04:40:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 4f6a6c8a-9e36-3cba-b839-09ec98ff6d9f | -3.2951 | -53.8395 | 2024-11-21 04:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 0ebbb2da-9fa9-33a4-a0bb-39fc71b4b66b | -3.295 | -53.8597 | 2024-11-21 04:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 37b7e1e9-b8e2-391e-8c90-cf153802d37d | -3.2951 | -53.8395 | 2024-11-21 04:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 16f8edc8-36ad-3fd1-b8c3-dbef1a3d06b3 | -4.2388 | -46.1197 | 2024-11-21 04:50:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 5aaf80bd-c7b7-323f-b308-e6ca1af55bfc | -3.2767 | -53.84 | 2024-11-21 04:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| c091b517-d5f9-35b0-82f7-1e31f2c6ce78 | -2.0259 | -54.5289 | 2024-11-21 04:50:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 3868ca71-4b15-32cc-bbec-c5ca731a5a4c | -3.2768 | -53.8199 | 2024-11-21 04:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 339bf26b-26e1-3fae-b144-1f15403e2e0c | -4.2575 | -46.1188 | 2024-11-21 04:50:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 55.5 |
| aeda8e32-ace2-3974-bd6c-878838b7b0cc | -6.1182 | -42.5086 | 2024-11-21 04:50:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 61.8 |
| 17c79ee8-2510-312d-892c-837bc735d196 | -3.295 | -53.8597 | 2024-11-21 04:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| e8369516-ca2c-337a-b2ff-2ce89271c1f5 | -1.46027 | -52.67083 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05f2b042-3df3-33f7-b79d-c3c111cc0cef | -1.06179 | -51.75075 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f48200b-37ec-36e0-9784-a31884143ebf | -2.17758 | -52.12832 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 64300a56-f5f9-333b-b823-26d5a794f942 | -2.45793 | -47.03317 | 2024-11-21 04:53:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a1b1c845-afe8-365f-bda4-2742b4977c89 | -3.12662 | -45.44807 | 2024-11-21 04:53:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d89c46d-d0cd-3550-9afe-24bce54e03c7 | -1.22166 | -54.19022 | 2024-11-21 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9658b4b8-d0ad-3a3f-bc42-1085c9492504 | -2.21155 | -53.70702 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fce292ef-63a8-3313-9418-b4d0928ced44 | -1.23471 | -54.01977 | 2024-11-21 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 19237a4c-6feb-3031-801c-38e456a07051 | -1.20936 | -51.75863 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19c0e14c-0fef-3e69-a228-0a9d21bfb375 | 0.75246 | -52.07142 | 2024-11-21 04:53:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dfbbb5e9-f29d-3609-b175-143bcdd889bb | -1.70107 | -50.20352 | 2024-11-21 04:53:00 | NOAA-20 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab85cde5-a955-3bf7-aa1c-e540ece8f91e | -2.21039 | -50.69397 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e590d01-6d6c-348d-a5dc-22d9cd21af49 | -0.30539 | -51.56859 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf77fdda-8e9d-34c8-8325-e1b27e9cd8e0 | -1.10882 | -53.15698 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13e3b402-3789-3aa8-8144-a79f94c956a5 | -1.59086 | -50.44379 | 2024-11-21 04:53:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3646d55b-8c2c-356a-b47d-cc59616709c2 | -0.04424 | -51.24469 | 2024-11-21 04:53:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ff01028-219c-3836-99a8-14c64259102b | -2.1492 | -48.92012 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 12c9f121-eb02-3857-bee3-209f3a0692e0 | -1.92823 | -49.51458 | 2024-11-21 04:53:00 | NOAA-20 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ab7bb2b-482b-31fd-8022-0b5b6fef5b3e | -1.69591 | -51.08799 | 2024-11-21 04:53:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e39172f-43fd-32c3-a502-5ea4fe4f434e | -1.64113 | -52.68819 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 463613bd-a325-3a71-aaf9-7acd267007dd | -1.63432 | -52.62365 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 58bbe8fd-d952-37f6-a66a-5b7970d1f03b | -1.40553 | -54.27283 | 2024-11-21 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3efcbc4-e4ba-3df2-b615-fffcf159fa8e | -1.51527 | -52.36483 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a71ed2ae-aa92-3918-ab38-1f8b1bb4467f | -0.9775 | -51.71963 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 36d42f02-315c-3dae-9b4f-48746d9b251e | -2.6321 | -48.06817 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 75a2a7b3-791e-3f22-b433-b6444a1b1db4 | -1.47027 | -51.11836 | 2024-11-21 04:53:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e667a9d-0329-3e3e-9979-77ce4634773c | -1.59326 | -47.49548 | 2024-11-21 04:53:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4083de65-9196-3fe2-b4e5-a95ac8cd8392 | -2.60971 | -48.24473 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0696501e-4e7a-34b2-bdb5-31cf91823a84 | -1.78482 | -53.61201 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 498cc23b-64af-3984-82e2-792fd9d17433 | -0.17474 | -51.62135 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 03cd82e5-71c8-3967-b88e-5719c0212c2f | -1.78206 | -53.60804 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ad20270-e953-31d6-8126-ff477595b08b | -2.94309 | -48.07239 | 2024-11-21 04:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06bff763-f42f-3b8f-864f-bdfa14c62fd7 | -0.42107 | -51.56863 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f394ab84-233c-31a3-b562-92ef628e1049 | -0.93719 | -51.72041 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a45e09bc-de16-3b81-be03-41f6c7a9888e | -1.4979 | -49.68327 | 2024-11-21 04:53:00 | NOAA-20 | SÃO SEBASTIÃO DA BOA VISTA | PARÁ | Brasil | 1507706 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91df9af2-0bd3-37b8-ba64-6071b8d9fc03 | -1.65733 | -45.44411 | 2024-11-21 04:53:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ffa30c37-316c-3c95-b8bc-c29855f2b625 | -0.98318 | -51.77113 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da0c8c6a-c45f-362e-ac71-679d9706b908 | -1.97872 | -53.3288 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b3e722b3-69bb-3aec-8c32-8316571a3baa | -1.4473 | -54.5018 | 2024-11-21 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5e7baef1-c050-3c42-a609-7936a67b8b22 | -1.78097 | -53.61494 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93a5e2ee-b2d0-31be-9311-33236ead5ca2 | -1.46033 | -52.69197 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c45ab84-d71e-3eb3-90db-2058e96b3206 | -1.20601 | -51.75811 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c554c9a6-e374-3f79-9546-e71bcf3a441f | -1.74094 | -50.48147 | 2024-11-21 04:53:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5c07ecf-8bdb-301d-9e1c-d4bcbc8fd7e7 | -1.20325 | -51.77578 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 82e87592-5d04-39c8-b9e1-fef409a9b15d | -1.39171 | -52.43783 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c9165e9-5294-3173-a45d-4497535caf0c | -1.71263 | -52.38454 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b4f3b32b-1127-3a18-8e57-d2b99fd4687e | -2.65865 | -48.4873 | 2024-11-21 04:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0334761b-7c51-3db2-8344-8bd98bce763a | -1.24836 | -51.61919 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e830e2a-5ec7-344c-b3e3-4862ab4a1096 | -1.64907 | -52.76689 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50fe8abe-4cea-3cb7-a818-fb0d45e85e3b | -1.58672 | -50.44717 | 2024-11-21 04:53:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61cbbfdf-a559-3c99-b9dd-8e14d00b7d07 | 0.75546 | -50.24387 | 2024-11-21 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README50.md)
