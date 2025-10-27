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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| caac07a1-9a42-38eb-9327-4513e49cbc98 | -9.45283 | -47.72838 | 2025-10-27 00:13:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 6a52b14f-4b55-34aa-bab3-d36ceb57f116 | -5.3638 | -45.04538 | 2025-10-27 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f9075b51-e0a9-3a85-b1cb-2ee62152ae9e | -9.56423 | -44.70988 | 2025-10-27 00:13:00 | TERRA_M-M | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 9f687a1a-19a4-3b77-887e-cfc76d5fe8ae | -5.41209 | -46.34011 | 2025-10-27 00:13:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 9c53dcab-57e8-3d62-9a40-0700feef5f4f | -4.8768 | -43.28431 | 2025-10-27 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3d152f32-185b-337b-8c5d-11f5aad5e7b9 | -9.42593 | -46.20763 | 2025-10-27 00:13:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 94af9531-4c81-3208-a681-724ad021c731 | -3.55386 | -49.49083 | 2025-10-27 00:16:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 659f1455-da2e-31b9-8b77-a10dd399d45e | -3.40795 | -43.84563 | 2025-10-27 00:16:00 | TERRA_M-M | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 572705e0-6a14-3dec-90ed-6dbcba998dfe | -3.87639 | -43.24214 | 2025-10-27 00:16:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3cb953c4-29cd-3cd2-b246-cc7259af4b60 | -3.42316 | -52.43261 | 2025-10-27 00:16:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| ca99c326-9ebb-33a8-b92e-ed3d36ee457f | -3.58044 | -49.01767 | 2025-10-27 00:16:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 212032d8-ff50-3bb3-954d-db70925c383b | -4.04561 | -44.0575 | 2025-10-27 00:16:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5b712cdf-e387-34e1-ae62-3f9401071d44 | -4.37152 | -46.81157 | 2025-10-27 00:16:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 20cbba13-c3e6-3d1a-b993-587579367d41 | -4.76864 | -46.41622 | 2025-10-27 00:16:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5321d264-43d8-3c4c-912f-5689d5e7e4f5 | -3.25156 | -50.04394 | 2025-10-27 00:16:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| d48dec80-849d-39d7-a612-be3002624bc2 | -3.63273 | -46.00026 | 2025-10-27 00:16:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| b6a816f2-ed87-333a-b775-48e7aa3899a7 | -4.76092 | -46.42657 | 2025-10-27 00:16:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 2d124377-72f9-31de-9fd1-76775f81d965 | -3.05271 | -53.01078 | 2025-10-27 00:16:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 3cfccf9d-ca36-3c5c-a95d-bfd03c268d27 | -2.31003 | -46.09114 | 2025-10-27 00:16:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6e876c1e-7b24-32a9-a053-8dd841460753 | -3.21341 | -44.43405 | 2025-10-27 00:16:00 | TERRA_M-M | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 2eb0ca72-d140-3724-8c00-77df8dce7911 | -4.23381 | -43.2991 | 2025-10-27 00:16:00 | TERRA_M-M | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 12b045d0-6418-3673-bbad-767fac3b7f0c | -4.4408 | -45.97694 | 2025-10-27 00:16:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 24.4 |
| e38d0dc8-da71-32e2-b623-e8179a60279c | -4.3234 | -48.08915 | 2025-10-27 00:16:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 6e7651de-6677-3af2-9531-4be0429b5d8f | -2.27719 | -47.86099 | 2025-10-27 00:16:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 91ea97ea-a289-35a0-addf-66fefd09446b | -3.31168 | -44.54417 | 2025-10-27 00:16:00 | TERRA_M-M | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 55f4e820-2736-3f74-b375-c7db79a125bf | -2.8107 | -49.14777 | 2025-10-27 00:16:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a5a038b5-b100-32c0-8af3-70d0cb73a647 | -4.48031 | -44.59282 | 2025-10-27 00:16:00 | TERRA_M-M | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 7c3b3e53-8050-3a22-b2d0-8bf95290a1f5 | -4.76989 | -46.42532 | 2025-10-27 00:16:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| eab5e954-9172-3fc6-afb6-793b057bb3b1 | -3.57855 | -43.6123 | 2025-10-27 00:16:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| c8bbfa6d-93f3-35f7-a779-94f402f5568b | -4.23533 | -45.69349 | 2025-10-27 00:16:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0dd29e1a-8c4b-3d17-963a-690dcefe5c76 | -3.5772 | -43.60257 | 2025-10-27 00:16:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c0ebd1d2-2f13-38a3-a9e0-5a0f428d7c17 | -4.49074 | -46.53858 | 2025-10-27 00:16:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f962222c-460b-31b6-963c-9a81dc4cb53e | -3.20772 | -45.788 | 2025-10-27 00:16:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| cbc84a2c-1cf7-39ca-8e30-a27365b97a4f | -3.80129 | -49.28521 | 2025-10-27 00:16:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 62524a20-d257-3b34-98f3-fd1630749491 | -3.24965 | -50.03005 | 2025-10-27 00:16:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 53b07198-c915-3463-9078-c156b2139cd3 | -4.12464 | -48.81642 | 2025-10-27 00:16:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 59a23986-3cb6-31ea-b2b5-76443d7428f2 | -4.2058 | -48.35986 | 2025-10-27 00:16:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| c55783be-9257-342a-9d11-fd3ea87b87c5 | -3.24261 | -50.64628 | 2025-10-27 00:16:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| e1deb8f6-0d84-3fcd-9e5f-cc3f0a08c32b | -3.56876 | -44.53553 | 2025-10-27 00:16:00 | TERRA_M-M | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 55b3cfb6-7782-3e6b-a8f1-f174725039e5 | -3.22838 | -45.93745 | 2025-10-27 00:16:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 3948c546-5640-3855-a6e1-11795f1f82a9 | -2.87605 | -46.78936 | 2025-10-27 00:16:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 87f6cab3-8a36-3953-a408-2337b511c523 | -2.7859 | -54.41376 | 2025-10-27 00:16:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| e0aa51d9-c381-3358-afeb-6a0727421bda | -4.33452 | -48.09862 | 2025-10-27 00:16:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| f408c755-53a4-346b-a416-f540322acaae | -4.45448 | -45.47372 | 2025-10-27 00:16:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 25603a51-4958-3f1c-8bcf-0b2c3da6b8ff | -4.32484 | -48.09982 | 2025-10-27 00:16:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 45eef15d-e672-326f-9384-8db7fa850363 | -3.39221 | -50.39863 | 2025-10-27 00:16:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| d856e08b-4c2e-38f1-af83-760949834946 | -2.32327 | -48.58075 | 2025-10-27 00:16:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 58c01079-8f8d-3485-8c77-9e16979dc06d | -2.27585 | -47.85117 | 2025-10-27 00:16:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| ee3a5307-a758-3d10-85a7-c3c952c71bb1 | -3.15471 | -50.3383 | 2025-10-27 00:16:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| c388387f-efe7-3bfb-a6c8-2f9099322863 | -4.42306 | -45.9794 | 2025-10-27 00:16:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e8a59ccb-33cf-38b1-8651-762dab6535ff | -3.14659 | -45.07283 | 2025-10-27 00:16:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| db9a3a7b-b6f8-371a-a4e2-b817320216a7 | -4.25611 | -48.12591 | 2025-10-27 00:16:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 6cce956b-cc29-3d51-9ffa-0f1ea89f7b77 | -3.31041 | -44.53509 | 2025-10-27 00:16:00 | TERRA_M-M | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 560bdbf7-05ae-3894-886a-490acedc835b | -4.34617 | -49.88843 | 2025-10-27 00:16:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| dea6bbeb-57d4-3a59-aec4-a9d306ee24cd | -3.12291 | -49.11055 | 2025-10-27 00:16:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 86d631da-a7a7-3952-87ee-bb16dcfdcc03 | -4.37025 | -46.80228 | 2025-10-27 00:16:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 3e110c6a-d662-3e18-9b76-6ca139e74457 | -3.72201 | -47.6541 | 2025-10-27 00:16:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 122.2 |
| 6cc8e2ed-da19-31db-ba6b-067509e33e8d | -4.2156 | -48.35854 | 2025-10-27 00:16:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8b156e3e-eb48-37c5-b737-8196f4657415 | -2.44764 | -49.03229 | 2025-10-27 00:16:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 315c4d97-0ad7-3578-8c40-0b6ae3cda08e | -4.45205 | -45.45614 | 2025-10-27 00:16:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 75ce7096-14ac-35dd-b759-9c720bbb543d | -4.57906 | -46.51058 | 2025-10-27 00:16:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f98723aa-1e53-374b-8330-2c6e4ae5c291 | -4.10139 | -48.02436 | 2025-10-27 00:16:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| d266529d-0a3f-3f58-8f79-b6bfc780c649 | -4.15329 | -43.24525 | 2025-10-27 00:16:00 | TERRA_M-M | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 542ec41a-66f2-3909-b600-c7ccbc7bcdd0 | -4.21828 | -43.18916 | 2025-10-27 00:16:00 | TERRA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c67b2494-64ab-369c-bc75-94bd24c2bfb4 | -4.25757 | -48.13667 | 2025-10-27 00:16:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 74cb0bb4-9545-3b1e-abe3-92b1bd3b0a69 | -3.60698 | -43.56215 | 2025-10-27 00:16:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 3993e6f7-4d28-3ec4-ab2f-457fe954a90d | -3.81268 | -44.96304 | 2025-10-27 00:16:00 | TERRA_M-M | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 164ddae7-24dc-377b-ae54-d8249f0db763 | -3.2404 | -48.77517 | 2025-10-27 00:16:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 8c13b1bb-df0d-306b-85df-f1994b29993e | -3.5675 | -44.52647 | 2025-10-27 00:16:00 | TERRA_M-M | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 52.2 |
| e2dcff4f-806e-3465-9a3e-4b983b2ec71c | -3.41904 | -52.42785 | 2025-10-27 00:16:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 0ab5d8dc-6310-3a45-9907-ba7d58807bc7 | -4.0736 | -46.05261 | 2025-10-27 00:16:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b50cd29b-0e1c-381b-9597-6c8f790286a7 | -3.71876 | -45.41992 | 2025-10-27 00:16:00 | TERRA_M-M | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 77251f6c-3813-38ad-ba50-b5476308c0db | -3.36173 | -44.04168 | 2025-10-27 00:16:00 | TERRA_M-M | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 18effc00-5d73-3a03-b85b-d6632d4c1117 | -3.12978 | -50.15232 | 2025-10-27 00:16:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| fb0a62a2-bf98-336b-89b6-8b1bee30bc9e | -4.31298 | -48.23293 | 2025-10-27 00:16:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 39bde487-cd0f-30e5-aa2e-10e9ca44bb35 | -3.4723 | -49.96765 | 2025-10-27 00:16:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 0cc0aefc-14d0-3994-9425-e6d3383fc9f0 | -2.22543 | -48.36818 | 2025-10-27 00:16:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 14e1de66-b5c2-303b-8163-a55b3f0a2930 | -3.41079 | -42.47681 | 2025-10-27 00:16:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 69451b4f-7a4a-37ca-bdc3-68f282e238af | -4.24175 | -43.28777 | 2025-10-27 00:16:00 | TERRA_M-M | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 102ac51d-e6a7-3a71-aaed-a2e4afb7372f | -4.35986 | -48.66525 | 2025-10-27 00:16:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 62c74d22-bfb3-323c-b4a9-67723620553d | -3.94577 | -48.09007 | 2025-10-27 00:16:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| d488ca4e-38ef-3774-a370-874738a493cb | -3.72337 | -47.66403 | 2025-10-27 00:16:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 3df9250b-c3f6-3116-a860-b91bfbe73c6b | -3.04724 | -53.01794 | 2025-10-27 00:16:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| e19186ce-d455-38fa-b4bc-0219bd50e597 | -4.26723 | -50.51425 | 2025-10-27 00:16:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| b2369afb-6125-3377-b266-c2ee0d5bc190 | -3.24242 | -44.64297 | 2025-10-27 00:16:00 | TERRA_M-M | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 86ab7c3f-64d3-3b59-9c76-80c7ccbec6ae | -3.71131 | -47.64539 | 2025-10-27 00:16:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 200.8 |
| 71ff8bc4-6e78-303b-9d41-14c4ade34e73 | -3.24474 | -50.66173 | 2025-10-27 00:16:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| a9cf9ac6-3308-3bb4-8bae-fdac0db080c0 | -4.33309 | -48.08805 | 2025-10-27 00:16:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 1a97fd51-20c6-355f-9037-ec73ffe4fdd0 | -3.97548 | -46.00894 | 2025-10-27 00:16:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 653cac60-fd5a-3fca-bda4-311a8f0f7c30 | -3.80301 | -49.29765 | 2025-10-27 00:16:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| a5207fa8-4656-35cd-879c-a7ab9b240eab | -3.98533 | -49.28608 | 2025-10-27 00:16:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 6823bad7-f18a-35f0-b7be-8cda30af128d | -3.58471 | -43.60512 | 2025-10-27 00:16:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| ab3add75-8271-3df3-91be-910906d0affc | -4.75968 | -46.41752 | 2025-10-27 00:16:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 65edc813-91c8-3523-8f93-c4c1f023144d | -3.80926 | -49.29049 | 2025-10-27 00:16:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| dd594445-3075-3983-a1da-76c890ae0eb0 | -3.0875 | -49.52059 | 2025-10-27 00:16:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6bb25707-ede8-3087-9145-7e1fbbf24eae | -4.43193 | -45.97817 | 2025-10-27 00:16:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| a031fad3-0f5c-3d85-8dc0-3303635d49eb | -2.83614 | -45.49154 | 2025-10-27 00:16:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7cc503d0-e407-32c0-8895-85474213daeb | -3.23721 | -45.93621 | 2025-10-27 00:16:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 0bb4bd93-9700-3cd5-8628-b4a6b6d26aee | -4.48156 | -44.60175 | 2025-10-27 00:16:00 | TERRA_M-M | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 95a526a9-b0eb-39ef-8d34-1332377eddf8 | -3.61639 | -42.77193 | 2025-10-27 00:16:00 | TERRA_M-M | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |


[Clique aqui para ver as próximas entradas](README7.md)
