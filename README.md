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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 233cf1a3-ef51-3a08-821e-99a7e4c538a5 | -14.1779 | -54.4124 | 2026-08-05 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 6127c5a0-d330-36ba-9fbd-2a11c716984a | -6.5514 | -55.1569 | 2026-08-05 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 7433513d-4cb7-3873-bfcb-bf41700ac2ce | -6.5329 | -55.1578 | 2026-08-05 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 432ee7bf-c3dc-363a-9a20-ee13ae9562a3 | -4.3774 | -47.7627 | 2026-08-05 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| a79ada1f-e8b1-3441-8c3d-ecfc70054968 | -12.5947 | -46.9301 | 2026-08-05 00:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| bbc25572-96a1-37be-8a1a-740a36dbb562 | -6.5699 | -55.156 | 2026-08-05 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| d763056c-5f05-3193-8895-85d3327ea166 | -3.1882 | -52.8907 | 2026-08-05 00:00:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 91e6a6cd-1fc5-3728-a8a1-daaf9f5703ee | -3.1883 | -52.8703 | 2026-08-05 00:00:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 9788cbd6-10d1-3e77-8a5b-3595890b51be | -3.1883 | -52.8703 | 2026-08-05 00:10:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 71ba014b-d7db-3ff5-81c2-728ce6e9ef96 | -3.6639 | -49.4686 | 2026-08-05 00:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 0e892132-54fe-34dd-a9a4-b66d922c4a6c | -3.1882 | -52.8907 | 2026-08-05 00:10:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 3fdf261f-eeb2-3835-bd40-febc112f6eff | -12.6139 | -46.9273 | 2026-08-05 00:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 33a10cea-03ab-3286-b32e-49c32f4a1fd8 | -4.3774 | -47.7627 | 2026-08-05 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| b45c02d2-677d-3a7b-8300-efb57922049d | -12.5951 | -46.9075 | 2026-08-05 00:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 7267a819-92ac-3cd4-94a2-288be836e889 | -12.5942 | -46.9527 | 2026-08-05 00:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| ba2013c0-3198-32c8-9bd3-18a702f2ce5b | -12.5947 | -46.9301 | 2026-08-05 00:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 284.9 |
| cc11faf3-eabb-3132-95f9-67361f267737 | -6.5699 | -55.156 | 2026-08-05 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| bc92d910-ccea-350d-b471-ad76cb3b4817 | -6.5514 | -55.1569 | 2026-08-05 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 7165bdcc-5de1-3cb9-b941-85dc175ef435 | -11.19 | -54.89 | 2026-08-05 00:15:00 | MSG-03 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3554cc81-6608-3eea-8396-dafb47043559 | -11.19 | -54.95 | 2026-08-05 00:15:00 | MSG-03 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7abfda40-c421-3265-bee9-6cc075987ac8 | -11.16 | -54.88 | 2026-08-05 00:15:00 | MSG-03 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d5b49a09-8cdb-36e8-81a7-92cd5526d4c8 | -11.16 | -54.94 | 2026-08-05 00:15:00 | MSG-03 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8f46e8bc-9a9e-320f-8c0c-304caf58291c | -12.5947 | -46.9301 | 2026-08-05 00:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 382.0 |
| 60ac3f7c-bd11-3f7c-9df4-a22dba842c5c | -12.5951 | -46.9075 | 2026-08-05 00:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 126.8 |
| d4ee65af-da69-302e-8287-22db281ce6ba | -14.1779 | -54.4124 | 2026-08-05 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 31c79c73-9476-308f-b63f-164228a04fdd | -3.1882 | -52.8907 | 2026-08-05 00:20:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| fd11dfa0-2fa4-3c19-b55c-f69f0f630848 | -12.5942 | -46.9527 | 2026-08-05 00:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 9fda4922-185d-310d-8050-efc794fc6c4d | -6.5514 | -55.1569 | 2026-08-05 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 04cf3845-a91a-3403-aa7f-eb8665da42f1 | -6.5699 | -55.156 | 2026-08-05 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| da4c917f-60f2-3325-910e-41de4e7c37aa | -12.6139 | -46.9273 | 2026-08-05 00:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| afb0aecd-d913-309a-b5b1-795b00c860b3 | -4.3774 | -47.7627 | 2026-08-05 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 025b8400-3425-3602-be67-502055f9e63a | -12.5942 | -46.9527 | 2026-08-05 00:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 161.9 |
| 92b78532-925d-3a1e-88b8-af5ca84da88c | -12.5754 | -46.9329 | 2026-08-05 00:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 3eeba5bc-e9e5-3288-9393-8935f17022a1 | -12.5947 | -46.9301 | 2026-08-05 00:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 379.4 |
| 477a0fb0-56f1-3641-8f3a-5b8091815eaf | -6.5514 | -55.1569 | 2026-08-05 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 99389577-c8a8-3032-ac6a-7c922e8251ce | -6.5699 | -55.156 | 2026-08-05 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| f0ab9fa5-379d-3b31-a369-4745c37f53af | -12.575 | -46.9555 | 2026-08-05 00:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 26adf4df-8c11-3a5c-99c2-7896bd9a2bcf | -12.6139 | -46.9273 | 2026-08-05 00:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| ec2fdbdb-4120-30cf-a637-6b0ee9340b46 | -12.5951 | -46.9075 | 2026-08-05 00:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 35060c86-a4ec-3df2-9c4f-2e978d1cdb78 | -12.5942 | -46.9527 | 2026-08-05 00:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 209.5 |
| 5040088c-737a-3723-b85c-b44999e8ed34 | -12.575 | -46.9555 | 2026-08-05 00:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 6875d77f-9854-3aba-81c3-fddbf9711913 | -22.2171 | -42.5273 | 2026-08-05 00:40:00 | GOES-19 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 87.4 |
| f6fbc1bc-0def-39fb-88b7-ed8913d2f03f | -12.5947 | -46.9301 | 2026-08-05 00:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 374.0 |
| 9f79b65e-e659-31bc-8f81-9cb6f980126d | -6.5514 | -55.1569 | 2026-08-05 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| c77bfccd-2870-34fe-b074-6ec94b42b644 | -12.6139 | -46.9273 | 2026-08-05 00:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 0dd4b5d2-f197-384a-98a5-adb9a556c7f5 | -12.5754 | -46.9329 | 2026-08-05 00:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 158.8 |
| f7d56d0f-970b-3a7e-88b7-9bc49eb9005b | -12.5922 | -46.938599 | 2026-08-05 00:48:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6cf3c2ed-6028-3992-952c-020ee13b601a | -3.1813 | -52.879398 | 2026-08-05 00:48:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3cddbc3b-f5d2-3dc0-91a0-40973efcb48a | -11.1662 | -54.887501 | 2026-08-05 00:48:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 04179fde-0c37-3936-bdec-8e49668adfbd | -11.1817 | -54.865799 | 2026-08-05 00:48:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4915420d-1cd9-3d0e-aa7a-3144de65b428 | -11.1722 | -54.912998 | 2026-08-05 00:48:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ffa4faa4-789d-3685-9dae-a8b14496636d | -11.1604 | -54.906898 | 2026-08-05 00:48:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f79147e1-76c6-38a8-8114-ac22c37ec777 | -14.1611 | -54.405998 | 2026-08-05 00:48:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c1c3b188-ba80-3994-b638-59daba66be68 | -11.1992 | -54.8526 | 2026-08-05 00:48:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5eb7fc0e-3bba-38b4-9dd5-f0216e36361e | -11.1974 | -54.889 | 2026-08-05 00:48:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| efc979ce-981a-33d2-9553-a11f91ca42f4 | -11.2034 | -54.914501 | 2026-08-05 00:48:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fa791ee0-1b19-3e7f-b143-4f14653ff6c9 | -6.5551 | -55.150299 | 2026-08-05 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72a3c24d-9c01-3ed6-a3f5-0895ad65466d | -11.1759 | -54.885201 | 2026-08-05 00:48:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cf42b801-2f11-3d94-8b02-7c54830da6d8 | -12.443 | -50.512699 | 2026-08-05 00:48:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 66e735e9-0224-3d01-bf15-5db44d0b21fc | -13.2488 | -54.261501 | 2026-08-05 00:48:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7dce3db1-2ef9-38de-ab49-1cd6474da5cb | -6.567 | -55.157398 | 2026-08-05 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c8049be-de98-32db-a344-9641e4ce26ee | -6.7241 | -58.929001 | 2026-08-05 00:48:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 370d4f25-40b1-3d3e-910f-dcf22e3e13cd | -5.3755 | -55.880402 | 2026-08-05 00:48:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27ca9e6f-0067-393a-8597-0f2e18d5a931 | -11.3462 | -62.212601 | 2026-08-05 00:48:00 | METOP-B | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f838416c-0fda-3f4d-b84d-1ea81eb83cb6 | -11.1622 | -54.870499 | 2026-08-05 00:48:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0a2e5e7f-1313-3626-894a-017dcacc1ec6 | -14.1728 | -54.411999 | 2026-08-05 00:48:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f65fce24-fe0c-3063-b449-2e3b985e51b1 | -14.1982 | -54.432201 | 2026-08-05 00:48:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c8bb321e-a6f5-3ecc-b57c-ceedcb1b7eb1 | -6.7174 | -58.945 | 2026-08-05 00:48:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1cfa34b0-734e-339c-a5c6-f9ee1e0f1ea3 | -11.2014 | -54.905998 | 2026-08-05 00:48:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4c9457e6-b7cb-36df-abb3-6e91333c4209 | -6.5333 | -55.145599 | 2026-08-05 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac305262-3654-3196-b612-56ae1b86d560 | -6.4171 | -55.794601 | 2026-08-05 00:48:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64f181c2-b694-389c-ab40-d05c2e573721 | -11.1739 | -54.876701 | 2026-08-05 00:48:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 78245137-aae5-3436-bb32-48c38e46ed2a | -11.1719 | -54.868198 | 2026-08-05 00:48:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c4d7f605-ca78-329b-b2a5-a4405d36f9b8 | -12.4333 | -50.515202 | 2026-08-05 00:48:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 37375955-2b01-3f48-a636-24272da342bf | -11.1877 | -54.8913 | 2026-08-05 00:48:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d83d568d-8841-3895-847d-b35ce7476a74 | -11.205 | -54.833199 | 2026-08-05 00:48:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 19429036-8923-3b5f-9492-ae3aefe9e3bf | -9.2877 | -60.645901 | 2026-08-05 00:48:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a61a765e-f01e-30d9-bb67-12e69c075c25 | -11.2152 | -54.920601 | 2026-08-05 00:48:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5110111e-189e-3f43-ba07-b56a10d7e448 | -6.7226 | -58.922199 | 2026-08-05 00:48:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 316c9245-1f71-37dc-a84f-fca12e609199 | -12.1989 | -52.8587 | 2026-08-05 00:48:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 917bd338-e8a8-3049-b79a-b23bb76bde05 | -11.1742 | -54.921501 | 2026-08-05 00:48:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5e9b9fb2-de38-38fb-a063-7c49f07715e6 | -11.207 | -54.841702 | 2026-08-05 00:48:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bea3a335-8814-3f21-aa64-66352b56fd26 | -6.5474 | -55.1619 | 2026-08-05 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2bcde76b-4cc9-32a4-a869-618216fa377f | -6.5648 | -55.148102 | 2026-08-05 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06126e6d-2204-383e-a4bb-bee061bad186 | -12.4295 | -50.500301 | 2026-08-05 00:48:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1ce77d4e-ba22-3a3a-9a21-34d916a68c23 | -14.1591 | -54.397598 | 2026-08-05 00:48:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 914472d2-0fb1-3b01-a98c-9ddf5941d6df | -6.5691 | -55.166599 | 2026-08-05 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bfd313eb-f92d-3d4b-a6a4-e799c260d322 | -6.5794 | -56.5383 | 2026-08-05 00:48:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 909a4dd5-5d28-33d9-af6f-a1f0f6787f5c | -11.1837 | -54.874298 | 2026-08-05 00:48:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 421dd4dd-33ff-3806-8398-a434c0f94190 | -11.1917 | -54.908298 | 2026-08-05 00:48:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5e2f8910-3c6e-355b-991d-ad8d5e2e2236 | -11.1897 | -54.899799 | 2026-08-05 00:48:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 44c94355-c779-3960-9b58-df0084f5c5b2 | -6.5572 | -55.159599 | 2026-08-05 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdd6264f-fde3-3584-8cd8-e8b566e23161 | -11.2207 | -54.8564 | 2026-08-05 00:48:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c726d75f-9348-3e57-a70e-5ab1eaf74247 | -11.1859 | -54.9277 | 2026-08-05 00:48:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b797d7cf-11ef-301a-8372-6b0dc27877c9 | -12.5756 | -46.915401 | 2026-08-05 00:48:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ae61f727-4266-385e-8c07-75d7aeec4f40 | -11.1799 | -54.902199 | 2026-08-05 00:48:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9b72049c-05c1-3a47-994f-9918979ea500 | -11.1957 | -54.925301 | 2026-08-05 00:48:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 78408b42-33e3-3e05-afca-8f1cd117af89 | -11.9205 | -55.9081 | 2026-08-05 00:48:00 | METOP-B | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c3f7b9aa-44ba-3b7e-be2e-62eb3ecc81f6 | -11.1682 | -54.896 | 2026-08-05 00:48:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5c849521-d054-345f-9079-849ace229459 | -6.5529 | -55.140999 | 2026-08-05 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README2.md)
