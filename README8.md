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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 16aa4c0e-b1b9-3553-97bd-e5ccae8d0700 | -4.1092 | -48.4981 | 2024-11-07 00:31:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecac6fbb-8201-328b-ab4d-c2527b4e817e | -5.5923 | -45.207199 | 2024-11-07 00:31:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| be09f595-f516-3d3a-ae43-6bbb29f53257 | -2.436 | -53.650398 | 2024-11-07 00:31:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98256f84-e95f-365d-83bf-4bfc91b00969 | -2.7291 | -54.133202 | 2024-11-07 00:31:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d81d191-e1e8-3d2b-8922-fc3daa5129b3 | -3.971 | -48.389 | 2024-11-07 00:31:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 001c9936-f833-368e-a32e-8aa34a2f101f | -4.2147 | -48.689999 | 2024-11-07 00:31:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26e8a517-f884-3093-8c5f-8e4c9db90c59 | -5.7121 | -45.948101 | 2024-11-07 00:31:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 36cf5184-e789-39ca-800e-5a23e753cb5a | -4.7366 | -44.412399 | 2024-11-07 00:31:00 | METOP-C | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a78b2109-e96a-3989-b1a0-65f8b8cd2f2d | -3.0814 | -53.877998 | 2024-11-07 00:31:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4127a64e-c91e-35c2-b1b7-a8e110f49df4 | -2.7565 | -53.2075 | 2024-11-07 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39e060b5-55e3-3c50-b8a3-2791951eba94 | -3.5722 | -50.5369 | 2024-11-07 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffdb3d57-1fc8-35eb-aa68-a81ce5eff233 | -2.1086 | -49.083 | 2024-11-07 00:31:00 | METOP-C | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23a64145-7782-30ff-a94d-022e68cbc90d | -2.6136 | -51.756199 | 2024-11-07 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec614753-6eb0-385a-a18e-9d480ada0471 | -1.9223 | -46.471901 | 2024-11-07 00:31:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e93575a-5088-3d60-a07b-e783286b0546 | -4.7482 | -44.4179 | 2024-11-07 00:31:00 | METOP-C | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b2148df9-5152-3610-9b10-18eaa970a03b | -6.5543 | -39.671501 | 2024-11-07 00:31:00 | METOP-C | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 65dd71fe-11aa-38f6-88b6-9d6b4977c94b | -2.174 | -46.444901 | 2024-11-07 00:31:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85ec8835-76ab-3119-91df-9c930d7ae034 | -2.3145 | -48.134899 | 2024-11-07 00:31:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1295740-7602-32ed-957b-46f91eb502ca | -4.3439 | -48.624001 | 2024-11-07 00:31:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da867658-741c-35a4-8e35-c37787e77c45 | -5.0444 | -46.8582 | 2024-11-07 00:31:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1de60fc5-120b-3efd-8651-bb630ea06271 | -5.9597 | -46.306499 | 2024-11-07 00:31:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 46180071-093c-3462-ac8b-5749a79d075c | -3.7173 | -48.995499 | 2024-11-07 00:31:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05f5fc5f-0cab-3926-9b05-c5f4f5b1bf71 | -3.2403 | -53.398701 | 2024-11-07 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 835a32b6-714e-31a8-98c8-09ae19f4a73b | -7.8536 | -48.201801 | 2024-11-07 00:31:00 | METOP-C | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a0731095-d470-3e9e-947d-8f17215dadda | -2.54 | -45.661701 | 2024-11-07 00:31:00 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ac5eeae0-81b4-3fa3-989b-a89bef6109a3 | -3.5866 | -50.236 | 2024-11-07 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d37bb96-47e4-3395-8767-f2514d3eb3f3 | -2.1981 | -48.797798 | 2024-11-07 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcf0147b-f6ca-354c-85d2-81df7e24e76f | -5.6189 | -43.9491 | 2024-11-07 00:31:00 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 738a87db-33f9-388a-8dfa-4092549c1ffa | -2.9375 | -52.690201 | 2024-11-07 00:31:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25c941ac-0881-3853-9644-26ba5d28c639 | -2.4332 | -53.638302 | 2024-11-07 00:31:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa77ac80-80bb-39ea-a6fb-309694b0e444 | -2.4262 | -53.652599 | 2024-11-07 00:31:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87981829-5a22-3010-afd1-22122fdc5586 | -3.6354 | -50.133598 | 2024-11-07 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b43d6c6d-af6c-3c1f-a0b0-5b026a773e89 | -5.5514 | -43.705399 | 2024-11-07 00:31:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4f634b1f-8b1d-31eb-9251-b2f1c219100e | -5.1421 | -47.691601 | 2024-11-07 00:31:00 | METOP-C | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 37ca7428-0047-3846-8d88-95783f250a4c | -4.5879 | -48.473202 | 2024-11-07 00:31:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c231b937-efda-38fa-87b0-36d244c0d272 | -2.3161 | -48.141701 | 2024-11-07 00:31:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7af34729-6d14-33b2-b492-677e37df9bd9 | -3.971 | -48.1628 | 2024-11-07 00:31:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d247801f-ebbc-3c25-a490-f032cda3000f | -3.9726 | -48.396 | 2024-11-07 00:31:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d40d7e3e-e7aa-3d74-8300-1c69cc677e0a | -7.6726 | -41.342499 | 2024-11-07 00:31:00 | METOP-C | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c8efa162-eeb6-3cdd-8160-d46967039269 | -2.3895 | -48.5075 | 2024-11-07 00:31:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b8eb1e9-4bf4-3dfe-9e8b-f9712dbca6e1 | -8.6823 | -47.9491 | 2024-11-07 00:31:00 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 35676770-4361-3afd-8b43-5c2f42c980b5 | -2.1965 | -48.790901 | 2024-11-07 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb168f33-80fe-3693-849e-a9618c8e8303 | -1.8022 | -46.981098 | 2024-11-07 00:31:00 | METOP-C | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7106967-daf8-3fe9-a2bc-a7415de6ead8 | -5.0283 | -46.833199 | 2024-11-07 00:31:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e4064af2-5662-3e31-99aa-ba55e16fbe93 | -2.8398 | -52.894001 | 2024-11-07 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7be55532-8303-37d8-aa58-b047544f5ff2 | -5.3562 | -49.228199 | 2024-11-07 00:31:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 681236fa-1959-35f6-bafa-e05f34386c05 | -5.8395 | -46.232399 | 2024-11-07 00:31:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2713fe8f-b9ed-3815-a007-de9cf3e4de50 | -3.6186 | -50.195599 | 2024-11-07 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e5f2cbb-db05-3b5e-a8a5-28c7c80fbc15 | -3.2333 | -50.4487 | 2024-11-07 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c92ed56e-ec57-3e82-9810-930affb9d16f | -4.3953 | -49.760899 | 2024-11-07 00:31:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7f5cb99-77df-3cde-8217-a62d4b9b55f6 | -2.0493 | -52.078499 | 2024-11-07 00:31:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5669a42-262e-3ee1-8ea0-3d26bee53c61 | -6.6882 | -43.054699 | 2024-11-07 00:31:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2bb0fd7b-a73b-3d2a-8d92-b65148433fc3 | -5.9889 | -45.3591 | 2024-11-07 00:31:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 65ac27ad-a128-3a60-adf5-62bc33aa2ecb | -5.594 | -45.2145 | 2024-11-07 00:31:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fdf5b700-536e-3e1d-ba14-264bc74b4dee | -4.2429 | -48.5424 | 2024-11-07 00:31:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81bd36eb-ce6b-37c6-af1e-c6b447ad758d | -3.2314 | -50.440601 | 2024-11-07 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10ce6ee0-4e51-315a-9878-63136d2c0960 | -3.4533 | -50.374802 | 2024-11-07 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9fdb917c-882d-33a2-8b18-d5d440802751 | -2.7311 | -51.7304 | 2024-11-07 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1cc1b276-a30a-365a-a98c-50db279c0263 | -5.9581 | -46.299599 | 2024-11-07 00:31:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e1ab38c4-b84f-3d58-9866-62bff520a80b | -2.8998 | -48.619801 | 2024-11-07 00:31:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc90ac1e-330a-3ae7-8e5f-9aa80e969078 | -4.9993 | -49.883598 | 2024-11-07 00:31:00 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c46dcd1-4113-3ebd-83d3-90794d0908da | -7.417 | -44.7966 | 2024-11-07 00:31:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cd29b0fb-f7c3-3d87-b9c4-bb279a79a11b | -3.9564 | -48.144299 | 2024-11-07 00:31:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 606462db-febe-3186-bf4a-e450b5017f2a | -4.3521 | -48.614799 | 2024-11-07 00:31:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf61d072-f1c9-3ac1-9af8-15bada1bf2b3 | -2.8458 | -48.653801 | 2024-11-07 00:31:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2965959e-889f-33b7-83dc-abbf1eb67659 | -4.5191 | -42.870499 | 2024-11-07 00:31:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e342dcc2-1223-3b10-bc1a-bc8484aa9005 | -4.4194 | -44.468399 | 2024-11-07 00:31:00 | METOP-C | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4f061869-401d-306e-8eb0-52ed80c79722 | -3.9725 | -48.169701 | 2024-11-07 00:31:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d0cec79-9454-3894-980a-4bf919788e39 | -2.8982 | -48.612801 | 2024-11-07 00:31:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58011ee0-3060-348c-80ce-77bf3fdba06e | -3.0128 | -53.4356 | 2024-11-07 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a95a40db-c54f-3e68-90e2-9171c63da776 | -3.0419 | -48.022999 | 2024-11-07 00:31:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8234759e-9814-3867-9ed1-a2bc811a999e | -2.4289 | -53.664799 | 2024-11-07 00:31:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e42e046c-be71-317a-b9fc-ee1e3367482f | -5.3579 | -49.235802 | 2024-11-07 00:31:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16217b7c-4e9b-3cf6-91a6-fb17da571c90 | -2.7591 | -53.219101 | 2024-11-07 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36a35106-1881-3c19-9f18-ad5b123ebd1f | -3.6676 | -52.3312 | 2024-11-07 00:31:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14bb06d8-ff14-32f8-b014-c6e919a92771 | -6.5412 | -39.659599 | 2024-11-07 00:31:00 | METOP-C | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| fe303ca8-56be-338e-bd7f-fd6f4e6be6d8 | -6.9624 | -39.823299 | 2024-11-07 00:31:00 | METOP-C | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| b11e9551-dbb8-33f5-bea5-9ae505812120 | -4.5116 | -42.882301 | 2024-11-07 00:31:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 083242ec-f50c-34b5-831a-5447fd4cf224 | -5.9922 | -45.373299 | 2024-11-07 00:31:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cd4a266f-82e6-3fc5-bdac-056f13cd2a23 | -2.7775 | -45.127602 | 2024-11-07 00:31:00 | METOP-C | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9d65c713-2cf8-3f23-9f39-7d33da24e25f | -2.4387 | -53.662601 | 2024-11-07 00:31:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e4f3d93-d959-3fff-b1ac-02abda7a10f5 | -2.5383 | -45.654301 | 2024-11-07 00:31:00 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 50c563a1-7ffa-3f1e-92dd-24f89f6136fc | -1.4211 | -46.8046 | 2024-11-07 00:31:00 | METOP-C | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a90526e8-cbb0-3b77-b0eb-b475ed3dbc59 | -1.5362 | -47.3503 | 2024-11-07 00:31:00 | METOP-C | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3e19b5d-9865-332e-836b-74b5b037a807 | -2.6698 | -51.822498 | 2024-11-07 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c54ee4f-ed44-3230-922b-3d3b1da4c885 | -4.4974 | -42.865601 | 2024-11-07 00:31:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7a96dffc-d26d-3cb8-ba9c-c92e6b805e85 | -15.8678 | -43.794899 | 2024-11-07 00:31:00 | METOP-C | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 8ec08811-65c3-3a38-9ab1-61b0029c9dee | -5.3708 | -46.258499 | 2024-11-07 00:31:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5abd7e20-bce6-3710-8601-bcd27a41a811 | -1.9239 | -46.478901 | 2024-11-07 00:31:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 728d9680-1835-3c33-b3de-909c352279bc | -1.8038 | -46.9879 | 2024-11-07 00:31:00 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47b892f9-f3e7-3ef2-b30a-1b16bb4f163f | -4.3423 | -48.617001 | 2024-11-07 00:31:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 675afe1d-c484-39f8-a6c0-1c30aaef5655 | -0.9968 | -47.606899 | 2024-11-07 00:31:00 | METOP-C | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0439e431-f4f5-39bf-87e2-d23629c28430 | -5.374 | -46.272301 | 2024-11-07 00:31:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 910e992a-4a71-39c5-8059-52e86cc92906 | -2.0797 | -52.031799 | 2024-11-07 00:31:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0a88a3a-d0a7-38b3-9d9e-2ea4151b0907 | -5.4683 | -47.0429 | 2024-11-07 00:31:00 | METOP-C | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e12da713-d3f0-3eb9-94a4-3eceb6864867 | -5.2246 | -44.912399 | 2024-11-07 00:31:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aac04b5a-cb41-3885-a9ef-a887afc5e9fc | -14.0702 | -44.1483 | 2024-11-07 00:31:00 | METOP-C | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 013d6701-99fc-3e6f-a7b3-20aa47ae537a | -3.2121 | -49.221199 | 2024-11-07 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43bb7013-71da-3e38-882f-9136e78636ba | -4.2131 | -48.682899 | 2024-11-07 00:31:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75ea612f-1579-31a6-b34e-26155e94b307 | -2.4015 | -46.1786 | 2024-11-07 00:31:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README9.md)
