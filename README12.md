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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d4b2217-f432-392f-b9b8-e73a6f37b30c | -9.6953 | -54.3424 | 2026-09-13 01:05:00 | METOP-C | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e3a371dc-1f1b-3d5b-91f7-0d5ef07243f7 | -13.7559 | -42.5821 | 2026-09-13 01:05:00 | METOP-C | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 2cc53e10-1aff-308c-8096-4707b9993975 | -13.3941 | -48.0051 | 2026-09-13 01:05:00 | METOP-C | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| be669fdc-7e20-3e08-91a1-1a6f72295590 | -4.4621 | -50.153801 | 2026-09-13 01:05:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5b1cfed-541d-3dad-a6e0-4176f8198ccc | -14.8263 | -48.140999 | 2026-09-13 01:05:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 515310d9-0137-3b9c-bf49-bcb381b5e56c | -3.5648 | -52.9977 | 2026-09-13 01:05:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72156fd0-da1e-3635-bf03-503f59a856b9 | -4.5747 | -54.907799 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4cf438b5-7eb7-3737-8e20-e36e32900fcd | -9.6969 | -54.3493 | 2026-09-13 01:05:00 | METOP-C | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 61b30322-09eb-3db7-b835-b8665728afdc | -9.9009 | -47.600399 | 2026-09-13 01:05:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ca5bef6c-4c3a-3c4e-92f9-ef01eb53eb34 | -5.7885 | -53.820099 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7963ec79-0408-3b58-9f48-b648026f7d84 | -4.5352 | -54.960499 | 2026-09-13 01:05:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a8d9111-f365-3127-8089-24a1e01fad88 | -6.23 | -51.694401 | 2026-09-13 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11010942-822f-327a-af52-6595542a164a | -7.8739 | -54.720798 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53749953-9aba-30f4-8301-ccc57652b094 | -6.7558 | -58.9538 | 2026-09-13 01:05:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a5efd4ac-b289-3713-b762-11cdc168b4b7 | -12.8546 | -44.399601 | 2026-09-13 01:05:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 83d10166-2550-3756-a2bd-60d9fa816a93 | -5.8179 | -53.8134 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fe53158-c0f8-3ea0-b943-93baebd383ae | -2.9669 | -50.403198 | 2026-09-13 01:05:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ded608cb-d946-367a-a52f-6d1f97eee809 | -17.6134 | -46.6539 | 2026-09-13 01:05:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ab206a58-1a1f-30a8-99cb-e00d2c559bc8 | -17.616501 | -46.666199 | 2026-09-13 01:05:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e3308460-1290-34c7-96d0-f030b6315aea | -3.044 | -51.2556 | 2026-09-13 01:05:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e42718ce-42f0-3531-a001-649eb162dd9f | -13.3456 | -51.7785 | 2026-09-13 01:05:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1e0d2159-9aa5-31f7-9f33-4527ac2ea150 | -15.2542 | -42.798401 | 2026-09-13 01:05:00 | METOP-C | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b0d10133-1802-30bf-9b3c-d9e1643c23be | -10.693 | -54.150299 | 2026-09-13 01:05:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5ca3e62a-3e5f-35d2-b6be-1ea5e549dd2a | -15.5787 | -53.787701 | 2026-09-13 01:05:00 | METOP-C | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 05da2119-ee8b-344b-a0ce-35c10135e429 | -5.826 | -53.803902 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c06d0711-69f9-35bb-a61b-a5a7557638af | -3.4077 | -59.240799 | 2026-09-13 01:05:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dce67823-c6b6-3615-a26d-3587da2da7a6 | -6.6563 | -58.875401 | 2026-09-13 01:05:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2e9f2a11-7682-3c66-846f-1c8c107c08e5 | -12.8588 | -44.376099 | 2026-09-13 01:05:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ca3f2532-3df5-3f1f-838d-c72e9c71b858 | -10.2489 | -57.704601 | 2026-09-13 01:05:00 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eb2ffd50-be8d-31a9-b9fc-d5c2668d406f | -6.8205 | -58.643002 | 2026-09-13 01:05:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6aed3d7f-ef2c-3a14-ae6a-6e7234ed2aad | -7.8641 | -54.723099 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0dbd250f-a67c-30d3-89f7-baee4da9c2f5 | -8.0375 | -54.850101 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e3c8aaf-ec0c-3535-8e6d-2eecbe79ba46 | -2.9572 | -50.405499 | 2026-09-13 01:05:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db5074f6-b10e-3f5f-90d3-b36db8a12f00 | -10.4789 | -48.635601 | 2026-09-13 01:05:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ed12c7eb-5c42-35d8-8d01-b6d1137376a4 | -3.3882 | -50.749199 | 2026-09-13 01:05:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c294732-f9be-3eee-98d4-07f3fe90ab19 | -13.5522 | -49.482601 | 2026-09-13 01:05:00 | METOP-C | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 52f36e71-d47d-372a-954f-351b2ebe060d | -13.3119 | -51.722401 | 2026-09-13 01:05:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| da3e5024-a39b-32fb-8e9f-0994f8497ed7 | -15.5524 | -53.8088 | 2026-09-13 01:05:00 | METOP-C | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f8ca85f6-1790-349a-b3b2-102d1f85af07 | -7.8609 | -54.709301 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71650086-2bdd-3061-be7d-ec7f2fbcb43f | -9.5821 | -55.160301 | 2026-09-13 01:05:00 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 46290a98-9e04-3d7c-b551-426e1d30d42b | -3.8741 | -51.193699 | 2026-09-13 01:05:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58ba448f-355c-3fd5-9b42-2980f124da79 | -6.6759 | -58.871101 | 2026-09-13 01:05:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d8ad2e69-966c-361b-be56-b2ab0ae39b2b | -15.0195 | -48.5014 | 2026-09-13 01:05:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e51b515d-f9dd-32fc-9e12-cde4dc14734d | -6.1094 | -57.667099 | 2026-09-13 01:05:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95af1c16-e757-3bfc-b9c7-09e42919e885 | -2.9502 | -50.419399 | 2026-09-13 01:05:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a08e7049-eef7-3d53-908a-80f2bebfa158 | -2.6724 | -57.499199 | 2026-09-13 01:05:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8b757dec-a1db-32bf-b30a-a493c4618325 | -15.2667 | -42.7686 | 2026-09-13 01:05:00 | METOP-C | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4a3ec7ad-c40b-39ab-aea3-41323d082197 | -1.4642 | -52.962601 | 2026-09-13 01:05:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a164e7e-9523-3c37-8aa2-9e194ca59c98 | -5.9579 | -57.771702 | 2026-09-13 01:05:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8710ece6-7896-3f8f-bb58-6bf06b24fe2d | -11.3588 | -46.788601 | 2026-09-13 01:05:00 | METOP-C | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 59caa0fb-8b3a-309e-9564-1dd9ab8d2769 | -3.1612 | -58.651901 | 2026-09-13 01:05:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d70b749f-ec1a-394e-bae0-088cb2321e1d | -15.5591 | -53.792301 | 2026-09-13 01:05:00 | METOP-C | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 81c471c1-8600-34cd-bf3e-a95720787f32 | -15.5622 | -53.806599 | 2026-09-13 01:05:00 | METOP-C | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0a929698-7bb0-3ad7-942d-6adef94381d5 | -2.6658 | -57.515499 | 2026-09-13 01:05:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 409fad59-eb3d-395b-93a2-4ca49095fc1f | -5.1251 | -55.959099 | 2026-09-13 01:05:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ad94c5a-0e34-34e2-a338-bcb7749224cb | -2.6804 | -57.534401 | 2026-09-13 01:05:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1a824e03-8ce0-34f1-93c2-8d29afb27fea | -6.2378 | -51.683201 | 2026-09-13 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2200414f-42bd-3871-b0fe-8c4f6525f333 | -2.6788 | -57.527302 | 2026-09-13 01:05:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0d8a5205-8f9c-35ba-99c8-f399b7276acb | -6.7317 | -55.635101 | 2026-09-13 01:05:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7287e2d6-8f3f-3bdd-bc59-841f685ce831 | -15.2571 | -42.7714 | 2026-09-13 01:05:00 | METOP-C | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 080d1e19-35ea-3555-a333-c84c77408961 | -13.4519 | -48.486099 | 2026-09-13 01:05:00 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 49c4dbde-a319-3420-9a20-0ec0553a106a | -8.0473 | -54.8479 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20f57e90-1044-33f2-886b-354fdc7b0060 | -10.5281 | -51.355 | 2026-09-13 01:05:00 | METOP-C | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ad379a00-2b17-36a4-bf71-edcbdd11168e | -5.966 | -57.761902 | 2026-09-13 01:05:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e9fa751-c936-34f7-9719-903d3c447c77 | -5.8145 | -53.798901 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e886e4f3-ffed-33af-b92c-17f32993f740 | -5.0222 | -49.9977 | 2026-09-13 01:05:00 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1f86248-52bf-33ed-a0ec-df5d7d658a9a | -9.7114 | -54.367802 | 2026-09-13 01:05:00 | METOP-C | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 29b700cd-e487-3551-9946-a0e25fd7034f | -6.1284 | -57.5686 | 2026-09-13 01:05:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea9df886-5a69-378e-8542-17f3b727975f | -10.5399 | -51.361 | 2026-09-13 01:05:00 | METOP-C | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a0db939c-6ff0-3a40-b647-a8c79d9e8285 | -3.5974 | -59.078899 | 2026-09-13 01:05:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ea96d3ca-718e-3fa6-a2d0-3b99d0e46a46 | -16.290199 | -53.839901 | 2026-09-13 01:05:00 | METOP-C | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cfbd700c-5b3a-3f9e-8194-1dbd59879c23 | -6.0901 | -57.902401 | 2026-09-13 01:05:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95a1aaa1-3929-3ab6-8a3c-b192fe2c0ae2 | -11.5237 | -54.632099 | 2026-09-13 01:05:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4e7b2d64-c3fa-3070-8131-0f0c169d2cb5 | -8.5509 | -54.7047 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3bdd9a3-e56e-31e5-8328-9937fb47be37 | -10.688 | -54.173302 | 2026-09-13 01:05:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 601eafa6-28b8-3127-9000-f4988efaaca7 | -10.8211 | -50.5914 | 2026-09-13 01:05:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b8a0dbc3-6956-37ca-bf4c-1a38ac30165a | -7.8675 | -54.693298 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e44c375d-19f7-3797-9bb0-34833771a1ae | -10.9601 | -58.965801 | 2026-09-13 01:05:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a45a75b3-087a-3187-b50b-8f3db5cbf46c | -12.4909 | -48.0355 | 2026-09-13 01:05:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 645d59fc-2043-37f6-ac2d-2997737cc45c | -3.5938 | -59.062698 | 2026-09-13 01:05:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f336bfbf-07f0-31aa-aa03-9c167b65686f | -2.5376 | -54.662399 | 2026-09-13 01:05:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7625047-1686-3731-b286-7d63b2298f2f | -6.5959 | -58.834499 | 2026-09-13 01:05:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d55b7af7-0981-39b2-b2d1-d435e18059e7 | -6.8622 | -47.444698 | 2026-09-13 01:05:00 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 91ce2421-6c1a-3fce-bc4f-5b59b08b3415 | -5.1868 | -49.3535 | 2026-09-13 01:05:00 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bfa99785-71cf-3c3a-b962-f8ce42b5199d | -9.5903 | -55.1511 | 2026-09-13 01:05:00 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 24122463-acda-317e-a7c0-a51734de558d | -13.3474 | -51.785999 | 2026-09-13 01:05:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7a2138c2-2d94-3bf4-8583-bf4eff8cc118 | -2.9474 | -50.4077 | 2026-09-13 01:05:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab9ce313-8ad1-3b1c-86b1-7774a9f51c7d | -8.0179 | -54.854599 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 314a19b1-9247-3e2a-889c-180c66b513b0 | -6.0718 | -57.866299 | 2026-09-13 01:05:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f449cab-c465-3328-9f43-4d1ae3fd9009 | -2.6772 | -57.520302 | 2026-09-13 01:05:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f114a7d9-da75-3efe-8b3a-7cab592a1c39 | -8.0489 | -54.854801 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbbc29ac-fc4d-3467-bd4c-c69357acb4eb | -6.228 | -51.685501 | 2026-09-13 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61e49aac-ddf8-3f28-a4ab-070fa6f41e6a | -2.5359 | -54.6553 | 2026-09-13 01:05:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c047b249-7f66-381f-8c3b-12dfc8896873 | -13.6192 | -47.8708 | 2026-09-13 01:05:00 | METOP-C | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a9822a81-5b0c-3412-9755-d35a0ae015da | -13.3492 | -51.793598 | 2026-09-13 01:05:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 335dacc9-605d-3e7b-87e2-6177d5b37027 | -6.1621 | -57.7188 | 2026-09-13 01:05:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2216c092-f6b0-34db-bd2e-ea111e94a027 | -10.8233 | -50.600399 | 2026-09-13 01:05:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b8e9cf39-4e97-39b9-ae99-007e6c0e1590 | -6.0701 | -57.8587 | 2026-09-13 01:05:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee038707-dce6-349c-b750-78f01369bbff | -6.8629 | -55.5769 | 2026-09-13 01:05:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28b5e789-7613-3e02-89ad-0968126a5c39 | -10.9367 | -47.899799 | 2026-09-13 01:05:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README13.md)
