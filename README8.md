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
| a7d175d2-fb5d-3acc-9d54-999d2e9420c5 | -1.98463 | -47.34352 | 2025-11-16 00:15:00 | TERRA_M-M | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| aa39eea1-f078-3492-b946-d75a79753824 | -2.52938 | -47.82346 | 2025-11-16 00:15:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| c642e289-7541-3c71-b710-188142702a6d | -2.14176 | -45.35441 | 2025-11-16 00:15:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 01d69cfc-cc99-3045-89fe-79892addb6dc | -3.06232 | -44.7495 | 2025-11-16 00:15:00 | TERRA_M-M | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| dad38174-9061-346a-bdf7-ff85793d036d | -3.35397 | -46.92275 | 2025-11-16 00:15:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 003b9b5e-e06a-38d5-a216-b0927b2c0300 | -2.41226 | -46.30409 | 2025-11-16 00:15:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 0b7d1185-4181-355f-a84c-1ad07c35e5c3 | -2.78826 | -43.34396 | 2025-11-16 00:15:00 | TERRA_M-M | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 41da7592-a7ec-3de1-b2c8-855ce3fd7e53 | -2.51891 | -47.81521 | 2025-11-16 00:15:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 360.8 |
| 78beef85-a7c2-3456-b5e5-16cef6033cd7 | -3.30932 | -45.80357 | 2025-11-16 00:15:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1e862b76-dfbd-3efe-b93d-d509b212c97e | -2.54295 | -47.45306 | 2025-11-16 00:15:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3de5df0e-95a3-3504-bc3b-e145375da04e | -3.38139 | -47.18782 | 2025-11-16 00:15:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 568518bc-c5be-3119-84b6-9d4716821ad5 | -2.91124 | -49.79276 | 2025-11-16 00:15:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 0df49692-af4b-38c5-aad4-0e5fa4e3413b | -3.29927 | -45.79601 | 2025-11-16 00:15:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 183877eb-dff8-3569-895a-4a8fc23599b7 | -3.3219 | -44.56252 | 2025-11-16 00:15:00 | TERRA_M-M | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4b3a963f-e589-3fee-bde6-eb0f358f11be | -2.79667 | -52.97226 | 2025-11-16 00:15:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| f381971c-301e-301e-abe6-70efdc5826f1 | -1.9936 | -47.3423 | 2025-11-16 00:15:00 | TERRA_M-M | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 8319faf5-4f63-3d06-8711-23f73e934c01 | -3.28036 | -45.45042 | 2025-11-16 00:15:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 9214d5f4-ed7d-3e33-bef2-36e7eb163c15 | -3.3267 | -45.84864 | 2025-11-16 00:15:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 9b3cd1f1-8f5e-3c86-ac8a-a07c501a6722 | -3.72312 | -49.52677 | 2025-11-16 00:15:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 51cd6f58-c564-3ed5-b65c-7e4b056d6e7a | -3.63653 | -49.42764 | 2025-11-16 00:15:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6b65d50f-ecac-3160-817f-8aa7144c4376 | -3.2715 | -45.45167 | 2025-11-16 00:15:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 0fa10f16-5df5-3d2c-8234-defcd31025de | -3.40195 | -50.18098 | 2025-11-16 00:15:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 8c623c06-e66f-3132-a471-014dd14f2060 | -3.78815 | -47.46717 | 2025-11-16 00:15:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b06037a6-1510-34ec-b018-fad1821e8be6 | -3.26027 | -45.77458 | 2025-11-16 00:15:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 4f8a01f3-ccdd-3fd7-aa83-b026bcbb7ce0 | -2.80535 | -52.96399 | 2025-11-16 00:15:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 4f1dd208-63eb-3e85-8f00-f76c3d729128 | -1.1641 | -49.20449 | 2025-11-16 00:15:00 | TERRA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| bc5e0855-ee42-31e0-84b8-e0d737c76f76 | -3.16984 | -45.72143 | 2025-11-16 00:15:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 06b7fb65-3191-3192-8246-669f73f32dbc | -2.88702 | -53.27063 | 2025-11-16 00:15:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| f0354672-0e43-340c-8789-f4ed93ec6eaf | -3.2114 | -51.58332 | 2025-11-16 00:15:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 2c9bdb33-9d50-3d68-b702-bdeb718efdf2 | -3.17321 | -45.81073 | 2025-11-16 00:15:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7cf39fd6-63ea-305b-bf22-771415ef99af | -3.06104 | -44.74029 | 2025-11-16 00:15:00 | TERRA_M-M | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| e82bb322-b734-38d4-851b-3229f077dc38 | -2.78664 | -45.21458 | 2025-11-16 00:15:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 14.4 |
| be7c7df6-a691-3e27-b958-c2c65592933a | -1.11927 | -47.74875 | 2025-11-16 00:15:00 | TERRA_M-M | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c1f275d3-fade-3299-90f9-cea88eceb3af | -2.88445 | -51.43007 | 2025-11-16 00:15:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 3598cbcc-dbc7-3b0d-889b-7c7688ed4c7e | -2.89009 | -53.29377 | 2025-11-16 00:15:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 5cffca58-5dd6-3da2-9009-6cccbe26277e | -2.14053 | -45.34543 | 2025-11-16 00:15:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 35.1 |
| bf6ee022-b85a-33d8-a818-27dc1792bff1 | -3.22187 | -49.22811 | 2025-11-16 00:15:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 31.5 |
| af83f06e-df13-3483-84dc-3495352929b0 | -3.60252 | -47.52407 | 2025-11-16 00:15:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 44065ed3-57f4-3d5b-8fce-b0a6bd26929f | -1.98712 | -47.36172 | 2025-11-16 00:15:00 | TERRA_M-M | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a4aaf5cf-53d8-31d1-b99a-dac3c24a32b1 | -3.14536 | -45.54488 | 2025-11-16 00:15:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b231908b-8532-342c-ba8d-9edcab9e4df9 | -3.24112 | -43.38445 | 2025-11-16 00:15:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1bb9fb7d-1e44-380f-afc1-548a9ecffe6c | -1.01912 | -48.1567 | 2025-11-16 00:15:00 | TERRA_M-M | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c3d4665a-b293-3ddd-8c7e-60fb92c35068 | -2.52021 | -47.82473 | 2025-11-16 00:15:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| a72b5fe5-8422-3899-a6c5-b8954d2f0de9 | -3.07701 | -52.91533 | 2025-11-16 00:15:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| f2860c8b-79e1-3123-86c8-3521d4c315f9 | -2.58205 | -46.93244 | 2025-11-16 00:15:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 358fecd7-349f-33fd-b436-7e84400b943d | -2.5795 | -51.87577 | 2025-11-16 00:15:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 283f2c2b-5645-3b26-b697-ca0d962efca5 | -3.25266 | -45.78463 | 2025-11-16 00:15:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 3a29c1eb-bfd0-30e7-a5b0-43638accef6c | -3.45758 | -46.12927 | 2025-11-16 00:15:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 988de693-ed4f-3003-9135-bb92db5ae510 | -3.24352 | -46.12355 | 2025-11-16 00:15:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 99adc7fb-9c3a-3858-b242-b4409425618c | -2.82112 | -48.32911 | 2025-11-16 00:15:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 661f9fca-0b64-34ed-84f3-89037d2a7984 | -3.34146 | -45.16349 | 2025-11-16 00:15:00 | TERRA_M-M | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 16.3 |
| bc69fa22-4aec-32d4-8693-7808c9e9a379 | -3.41014 | -52.19619 | 2025-11-16 00:15:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| b7d46f22-c43b-370c-9a3d-bbec2ac48c7f | -3.26271 | -45.79219 | 2025-11-16 00:15:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 13.6 |
| a9a45016-0361-3394-9aa6-290af25b121d | -2.82175 | -45.401 | 2025-11-16 00:15:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 085a6d8b-d73f-3ae6-b607-4cb6b2ac03db | -2.58432 | -51.82175 | 2025-11-16 00:15:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| b61537f8-9546-3fe8-8e12-3a6ea1266423 | -2.42296 | -44.78896 | 2025-11-16 00:15:00 | TERRA_M-M | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d8bd8387-60d5-3ce5-b489-c27c7ecb22ba | -3.35522 | -46.93179 | 2025-11-16 00:15:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e9b98329-90e5-3000-bc06-5bddec3e8ccf | -2.90333 | -49.13949 | 2025-11-16 00:15:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 508a73a8-0196-3e05-bc64-658540c1310a | -2.58349 | -51.86967 | 2025-11-16 00:15:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| ddbd760e-5a11-3302-aab6-c199aab6b2f9 | -3.18044 | -44.40713 | 2025-11-16 00:15:00 | TERRA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7926938b-41b3-340c-9b2b-3d15d3be6e65 | -2.94047 | -48.73909 | 2025-11-16 00:15:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 50c43b7d-0666-3530-8505-1d09c5072801 | -3.22028 | -49.21668 | 2025-11-16 00:15:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 83f6b435-2ad5-33d5-a4a8-784a4f1ebdb1 | -2.91812 | -45.23545 | 2025-11-16 00:15:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 93abfb22-6b24-3ab4-8b69-44640ce78e7b | -3.45637 | -46.12047 | 2025-11-16 00:15:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 6dac6eb9-e99d-32e8-aad3-f08f4e19e054 | -2.72566 | -45.04508 | 2025-11-16 00:15:00 | TERRA_M-M | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e461924f-6a5a-309f-bfb9-b2af9840353e | -2.59096 | -46.9312 | 2025-11-16 00:15:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 491cb0e9-c99a-3cba-be08-f32db7b471b7 | -3.161 | -45.72267 | 2025-11-16 00:15:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fc88a355-c272-34c0-a919-7ae2252d0b61 | -3.24796 | -51.35096 | 2025-11-16 00:15:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 294bdf99-4af9-3049-a9e0-610820ec3e82 | -2.46697 | -48.85627 | 2025-11-16 00:15:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 0b1cda92-d25b-352b-84f1-ecaf060ae25a | -3.13026 | -50.29134 | 2025-11-16 00:15:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 6277d512-f345-38ad-85e3-fe05f8c0a288 | -1.11801 | -47.73952 | 2025-11-16 00:15:00 | TERRA_M-M | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| fcf31e58-7393-3dc3-859f-927643e77bde | -1.49653 | -47.81368 | 2025-11-16 00:15:00 | TERRA_M-M | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d39fa0dc-4f10-314a-9c96-28624c1d0e35 | -2.93149 | -51.76837 | 2025-11-16 00:15:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 9fc71e35-6dfa-38e3-9156-feabcf32af33 | -1.99485 | -47.35136 | 2025-11-16 00:15:00 | TERRA_M-M | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 115.0 |
| 97228adb-37db-359d-9275-307e4df130ca | -2.82299 | -45.40989 | 2025-11-16 00:15:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5bf57b12-c8e0-3538-a4e3-437ec6c0151d | -2.25877 | -47.19444 | 2025-11-16 00:15:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 43cd4ee7-250e-3f20-abf4-3908196000c8 | -3.45784 | -51.01762 | 2025-11-16 00:15:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| d426607b-df30-3cad-8131-e5ebb191d7bb | -3.10404 | -45.78185 | 2025-11-16 00:15:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 21b4d2d3-b4bb-3a04-81f9-81e47e4077fb | -3.25144 | -45.77582 | 2025-11-16 00:15:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e59b5a7e-0bca-36b5-aab1-eb548bdf79c6 | -2.93898 | -45.4507 | 2025-11-16 00:15:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 9e983752-a7c3-39db-bbff-d592f1ad697b | -3.34036 | -45.62225 | 2025-11-16 00:15:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8358b9c6-c4f5-3973-b136-d2c4469b31b1 | -3.78945 | -47.4766 | 2025-11-16 00:15:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| f8869f32-2e1e-3455-bf8f-ec6087478bc3 | -3.21747 | -43.35564 | 2025-11-16 00:15:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 96da347d-f877-359c-8216-246475bf46c0 | -2.25753 | -47.18542 | 2025-11-16 00:15:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fc56f48a-9026-347d-ad7c-687d1d25ddac | -3.42586 | -50.35841 | 2025-11-16 00:15:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| f2ecfa1c-7576-37ce-9cdc-4e114c17b993 | -3.41492 | -50.35981 | 2025-11-16 00:15:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| ac98f9c4-7f89-3fe0-b41f-7ed9dc135c0f | -2.52808 | -47.81397 | 2025-11-16 00:15:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 6f4fa323-08e5-3e79-a73d-241f37b42fa2 | -3.39527 | -49.76641 | 2025-11-16 00:15:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| ec896998-ea78-3d16-97d5-3eb7f30eab98 | -3.73168 | -49.53222 | 2025-11-16 00:15:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e251b566-f721-341c-84fb-65c69e44c304 | -2.58678 | -51.83925 | 2025-11-16 00:15:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 8b2b7e71-408c-3dea-af90-ed2ef80b9707 | -3.37997 | -46.03835 | 2025-11-16 00:15:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 745dc8f6-5464-3d48-826e-718a2633300f | -1.99402 | -46.54532 | 2025-11-16 00:15:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d2d12792-de6f-3f9c-94b9-474a2fcdd5d7 | -3.08544 | -45.71261 | 2025-11-16 00:15:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 38.7 |
| c6eed891-8fb3-31fe-8660-ba7d3ad9d2cd | -3.4644 | -50.12575 | 2025-11-16 00:15:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| df98f938-b1c6-3cba-9992-e5ddbd16a24f | -2.50975 | -47.81652 | 2025-11-16 00:15:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 5a77aaaa-f69a-39ab-b275-d3181df9049d | -3.83279 | -49.81158 | 2025-11-16 00:15:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| dc6b8864-9019-3666-a785-9252a1f861ef | -3.33676 | -45.85619 | 2025-11-16 00:15:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 246cc3a1-29f4-339e-a09b-580981b625bd | -2.69099 | -49.07872 | 2025-11-16 00:15:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 118501b9-e347-3e1a-be7d-3fd9575a0c2e | -3.25073 | -43.38308 | 2025-11-16 00:15:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 85799f99-30a6-365f-9f88-7ba0297a52d0 | -2.59219 | -46.94015 | 2025-11-16 00:15:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |


[Clique aqui para ver as próximas entradas](README9.md)
