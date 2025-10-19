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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4c9e3a7-c610-3efe-8aaf-279c4b02063b | -12.3772 | -43.1651 | 2025-10-19 12:50:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 157.0 |
| 65fe49cf-d703-34c5-8866-f16007becbe3 | -14.4954 | -45.5716 | 2025-10-19 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 141.7 |
| 23a08de1-35e3-3c02-a622-dbcf62635072 | -13.9137 | -45.5344 | 2025-10-19 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 8f185262-e976-3443-a3a5-4a7362a18b55 | -14.4759 | -45.5751 | 2025-10-19 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 154.9 |
| 88291e1c-3626-30e5-961b-840e3a65bd23 | -12.3767 | -43.1891 | 2025-10-19 12:50:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 127.6 |
| fda9fbc5-a99e-35b4-8f5a-385f2641b500 | -14.4754 | -45.5984 | 2025-10-19 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 192.0 |
| e80725f4-671d-3eed-aaf3-934d0cfafb10 | -14.4949 | -45.5949 | 2025-10-19 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 247.0 |
| c3f7073c-e6ea-3c3f-9093-00495e75453d | -13.8947 | -45.5145 | 2025-10-19 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 138.8 |
| edc8dc58-b501-3f20-b592-908b86e6db29 | -12.3767 | -43.1891 | 2025-10-19 13:00:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 219.8 |
| 0a17a179-400a-3f19-af79-bdba8bd04f2f | -14.4944 | -45.6182 | 2025-10-19 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 297ba6fe-3ae2-32be-88c6-a83a07793be0 | -14.4954 | -45.5716 | 2025-10-19 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 169.9 |
| 9a9678a1-d485-3c92-bd48-781ee0441fea | -10.8671 | -43.9428 | 2025-10-19 13:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 166.0 |
| efa716f2-f8d9-3535-90d6-a41a23ebbcf2 | -13.9132 | -45.5576 | 2025-10-19 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 105.7 |
| e08edce4-dff1-352c-a786-eb57d2dde359 | -12.3772 | -43.1651 | 2025-10-19 13:00:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 315.0 |
| 8f72f75b-51d6-39e8-89da-b4e77b42d943 | -14.4949 | -45.5949 | 2025-10-19 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 275.5 |
| 0a2eb00c-adfe-31ef-86d2-413cf66cfda0 | 1.7852 | -55.7239 | 2025-10-19 13:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 43965bc6-3e9d-38c3-a312-2d80353e2a92 | -14.4754 | -45.5984 | 2025-10-19 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 264.8 |
| 07faedd9-ecdb-30db-b7c1-3f857484bc39 | -14.4949 | -45.5949 | 2025-10-19 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 543.5 |
| 444630ed-5cec-3152-be79-91bfd418ee06 | -10.848 | -43.9455 | 2025-10-19 13:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 150.7 |
| 6898206a-20c5-3714-84e8-dbd96a13a140 | -14.8162 | -41.8037 | 2025-10-19 13:10:00 | GOES-19 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 98.2 |
| 76dfeaf8-371a-3217-9e44-c14b6734f663 | -14.4954 | -45.5716 | 2025-10-19 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 192.9 |
| b73c8937-a11d-3a81-ae25-c20e0c06c60f | -14.4944 | -45.6182 | 2025-10-19 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 156.9 |
| b889ae59-4081-3111-ab54-74f668bd1bfc | -13.9132 | -45.5576 | 2025-10-19 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 9493a1ce-aa13-36eb-b8c6-7c39b20f9cb8 | -14.8359 | -41.7995 | 2025-10-19 13:10:00 | GOES-19 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 98.6 |
| 9fab5681-ebed-3c0f-8eb5-4843a8895794 | -14.4754 | -45.5984 | 2025-10-19 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 382.9 |
| dffced5f-4e76-3db9-8128-c8c1abceb9b9 | -10.848 | -43.9455 | 2025-10-19 13:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 435.0 |
| 92f3c756-e3a8-3ef6-b10d-b0d88b87bd06 | -10.6853 | -44.5506 | 2025-10-19 13:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 7770ffd6-c70c-3e37-a020-830bd1b85ba1 | -14.4754 | -45.5984 | 2025-10-19 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 319.6 |
| a23cb673-ab3a-3132-8316-5b32b513c50b | -11.4585 | -44.0204 | 2025-10-19 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 4e000911-699f-3702-90fb-4179e60f7c23 | -14.0677 | -44.6687 | 2025-10-19 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 2ad11733-ce4d-3fe3-b574-8d35d11e4412 | -14.4949 | -45.5949 | 2025-10-19 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 453.9 |
| 40a5165b-8b6b-3944-997b-7c391c828a20 | -14.0287 | -44.6757 | 2025-10-19 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 031942f0-2643-3b73-a56a-bc523cf7da6a | -14.4954 | -45.5716 | 2025-10-19 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 210.2 |
| e70b9cf4-b871-39fb-a2f8-803737e541e3 | -14.8162 | -41.8037 | 2025-10-19 13:20:00 | GOES-19 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 135.9 |
| 6b66c194-34b5-3272-8165-041157a6069c | -14.0482 | -44.6722 | 2025-10-19 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 2027c52c-8645-3aef-a6fe-be80988ab620 | -14.8359 | -41.7995 | 2025-10-19 13:20:00 | GOES-19 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 123.6 |
| f705461a-1b9e-3606-b0ed-9f6b2b35b51c | -11.4389 | -44.0468 | 2025-10-19 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 567528c3-ffda-3708-a6ba-2e2d2791efe0 | -14.4944 | -45.6182 | 2025-10-19 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 0707de9d-ac78-3111-8624-285b01c42cdb | -14.0292 | -44.6521 | 2025-10-19 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 92782bbb-9abb-3fbb-bb4b-5d00bc8825c8 | -10.8289 | -43.9482 | 2025-10-19 13:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| a3790a43-78f8-39cd-abb5-0eb4d01feece | -14.4888 | -41.5764 | 2025-10-19 13:20:00 | GOES-19 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 93.2 |
| 76674d0d-b3ec-3b79-9cbc-08fb597c82b2 | -14.4949 | -45.5949 | 2025-10-19 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 374.2 |
| d05b4d4a-271a-342d-9a83-2bbc363416d8 | -11.5062 | -43.4952 | 2025-10-19 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 7a54973e-21ed-3d58-953f-7cdd9e865a0c | -12.1383 | -46.7252 | 2025-10-19 13:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 126.9 |
| c201ea53-d889-3c86-94ba-03bf4d9d8589 | -14.0292 | -44.6521 | 2025-10-19 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 104.1 |
| c848aa9e-9ce7-3c23-b9c2-4c3eebc00d59 | -10.8293 | -43.9248 | 2025-10-19 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 1de6d4bb-2dbc-358b-a08d-95d990723bf0 | -14.4754 | -45.5984 | 2025-10-19 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 408.0 |
| 389202d9-59b7-3dc4-a745-b0072e232ffe | -14.8162 | -41.8037 | 2025-10-19 13:30:00 | GOES-19 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 192.2 |
| ae52b43d-379d-315b-9602-e30d2a51f8f5 | -14.4944 | -45.6182 | 2025-10-19 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 121.0 |
| dacae6cb-bb9b-3412-8ead-24ff4a00e6cd | -11.4389 | -44.0468 | 2025-10-19 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 32436142-6959-3aab-9945-8ae033961bc4 | -10.8484 | -43.9221 | 2025-10-19 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 273.7 |
| 33b73af6-1bef-36cb-8f3f-cc8ced1eabb8 | -11.4581 | -44.0439 | 2025-10-19 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 2062365c-14fc-3278-866a-ea8ebd3db9ee | -14.0287 | -44.6757 | 2025-10-19 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 6af7740e-1052-3593-8d6e-92ba8ca6ccc0 | -11.4193 | -44.0731 | 2025-10-19 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 125.3 |
| ef283367-cb41-35e9-9b36-6adeb5b55ec4 | -14.0477 | -44.6957 | 2025-10-19 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 92.7 |
| df23b678-6a32-37dd-8f2a-78d4bac9e5b0 | 1.7852 | -55.7239 | 2025-10-19 13:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 9515040b-f465-351a-a049-25820ff5af0e | -11.4576 | -44.0674 | 2025-10-19 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 6d0e3e1f-d602-3893-8744-0f423c4a9a37 | -10.9708 | -39.2706 | 2025-10-19 13:30:00 | GOES-19 | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | 99.0 |
| 0dec1a5e-9081-3a6b-90d4-4dc749d7195e | -11.4585 | -44.0204 | 2025-10-19 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 7ba5dc6e-3015-36a9-9610-dfa10e6410c3 | 1.7301 | -55.7641 | 2025-10-19 13:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 8ef27256-af7e-36e0-9dd7-d8af62df1a0b | 1.7668 | -55.7241 | 2025-10-19 13:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 03e4dad7-df2d-3a32-94be-23a49ac2059c | -14.8162 | -41.8037 | 2025-10-19 13:40:00 | GOES-19 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 168.5 |
| 787d39f8-3ac2-3f44-91b2-e926f6eb9d64 | 1.7485 | -55.7441 | 2025-10-19 13:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| c112bda8-e21e-3e02-b609-874bffc65a34 | -4.7895 | -42.1352 | 2025-10-19 13:40:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 94.6 |
| edf3aca6-ffd7-34d7-8600-52fb99b6f61f | -14.4944 | -45.6182 | 2025-10-19 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 120.4 |
| d064399b-7c47-3438-a078-00dcfd24eab2 | -11.4777 | -44.0175 | 2025-10-19 13:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 122.4 |
| af731d0e-ce83-3f9b-88dd-9f3ea7761b28 | -4.4059 | -43.4049 | 2025-10-19 13:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 4efaee6b-bbc0-300d-b7ae-08252bdd39b0 | -14.4949 | -45.5949 | 2025-10-19 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 345.6 |
| 3902bcb6-e958-3e46-a3ea-70622cfc84d4 | 1.7852 | -55.7239 | 2025-10-19 13:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| a9620599-21a6-3010-a2d7-3ce6296e7eec | -4.4445 | -43.2397 | 2025-10-19 13:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 8af2e6d0-82fc-38fe-8f7e-91bdb37ff84a | 1.7301 | -55.7641 | 2025-10-19 13:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 8c9d7a7f-9956-3203-bd28-a910cfd96707 | -3.8372 | -41.7644 | 2025-10-19 13:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 104.2 |
| 8737be00-074a-33e6-8d5e-2c267205a933 | -14.4754 | -45.5984 | 2025-10-19 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 362.0 |
| a848a94c-7520-3a0f-b2d2-8d5e6760b967 | -4.7708 | -42.1365 | 2025-10-19 13:40:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 89.6 |
| 4b3c5ae3-953a-3c52-87a8-880a174fc44e | -4.7999 | -43.2176 | 2025-10-19 13:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 53c0eb6a-c6c9-3763-98dc-4d953f53419a | -10.8097 | -43.951 | 2025-10-19 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 02c471e1-19dd-35ff-8b3e-04b804962013 | -14.4944 | -45.6182 | 2025-10-19 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 114.6 |
| cd4281f1-df6a-3bc3-a84e-2032753cb9d8 | -12.0058 | -41.4875 | 2025-10-19 13:50:00 | GOES-19 | MULUNGU DO MORRO | BAHIA | Brasil | 2922052 | 29 | 33 | nan | nan | nan | Caatinga | 109.7 |
| a84de242-81c6-391d-a6da-df99904f7d17 | -4.4066 | -43.3118 | 2025-10-19 13:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 53a5d885-9b61-3562-9a29-cd6130f2dc9d | -12.0256 | -41.4595 | 2025-10-19 13:50:00 | GOES-19 | MULUNGU DO MORRO | BAHIA | Brasil | 2922052 | 29 | 33 | nan | nan | nan | Caatinga | 305.5 |
| 264a8fef-238d-3d0e-85fd-49a2240a42c8 | -11.4777 | -44.0175 | 2025-10-19 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 132.8 |
| bc3c206d-45d2-3715-9fc5-2e722e95a730 | -10.8289 | -43.9482 | 2025-10-19 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 46f52ecf-d546-3a72-a22d-bc17adba7db0 | -14.8162 | -41.8037 | 2025-10-19 13:50:00 | GOES-19 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 117.5 |
| 2a6e46b8-f7db-3542-83eb-62a60e732972 | 1.7485 | -55.7441 | 2025-10-19 13:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 121.3 |
| 1f5df219-9c3f-3e71-88b8-08ea9a947802 | 1.7668 | -55.7241 | 2025-10-19 13:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 31f0b153-b4ba-3663-a3cf-ec9858b68ddd | 1.7668 | -55.7439 | 2025-10-19 13:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 93d0465a-eebf-352f-a443-e3f5eb37758b | -14.4754 | -45.5984 | 2025-10-19 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 254.2 |
| 796a2a19-a9e9-36a3-9ae1-893cd1d9d5a9 | -4.6509 | -43.1337 | 2025-10-19 13:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 72ffa532-d560-35ca-baee-d08966070eaf | 1.7301 | -55.7641 | 2025-10-19 13:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| ee725cf7-66b5-3b02-876e-fa896fab9f85 | -10.5136 | -43.4052 | 2025-10-19 13:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 89.2 |
| fe4734ae-f286-38d5-94b1-59140144cf4a | -14.4749 | -45.6217 | 2025-10-19 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 732d8226-f66e-326a-8ad3-0e6f3f35d469 | -3.8371 | -41.7883 | 2025-10-19 13:50:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 100.6 |
| 70f4f5c8-856d-33da-b191-21267cb12d6f | -10.9708 | -39.2706 | 2025-10-19 13:50:00 | GOES-19 | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | 108.9 |
| dfc24023-9d99-3101-b917-b2ce5fbdf367 | -4.4059 | -43.4049 | 2025-10-19 13:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 676d6443-6eee-33c9-a866-180512303bdb | -14.4888 | -41.5764 | 2025-10-19 13:50:00 | GOES-19 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 92.5 |
| 1eb25aa9-b700-36dc-b0e5-df02cc522dc1 | -4.7708 | -42.1365 | 2025-10-19 13:50:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 93.0 |
| 715e0830-0057-3da4-b9d2-15e64239690d | -4.3152 | -43.0138 | 2025-10-19 13:50:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 0507c219-28fa-3c1a-9397-8e9fca6224a1 | -4.6509 | -43.1337 | 2025-10-19 14:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 1521c1ef-d434-3dea-8f2a-1d4ee33c6d6b | -10.9708 | -39.2706 | 2025-10-19 14:00:00 | GOES-19 | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | 109.4 |
| df46f345-afe7-3313-8557-60757a5a97d8 | -10.5136 | -43.4052 | 2025-10-19 14:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 114.9 |


[Clique aqui para ver as próximas entradas](README65.md)
