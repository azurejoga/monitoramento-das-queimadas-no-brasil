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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f83c502-e706-367a-bacd-4a58742e776a | -17.31595 | -49.91414 | 2025-01-26 03:57:00 | NPP-375D | EDÉIA | GOIÁS | Brasil | 5207402 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1001199b-6406-3011-94b9-7897fe878d12 | -18.71209 | -40.57296 | 2025-01-26 03:57:00 | NPP-375D | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5ee3e2f7-6c6b-33d5-8cfa-43e29bbe73c9 | -15.04163 | -45.63768 | 2025-01-26 03:57:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c15c3686-decb-3a06-8213-2e1cbc21f3d4 | -20.34727 | -40.36133 | 2025-01-26 03:57:00 | NPP-375D | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bcc6477d-39fc-301a-aef3-b342c265c959 | -16.68191 | -43.88461 | 2025-01-26 03:57:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c3e7c4c7-c3f9-3fcf-856a-415d30c55453 | -15.03627 | -45.64427 | 2025-01-26 03:57:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ed3c309-94c7-37b0-898a-5037dbe3d5b9 | -13.22883 | -43.97672 | 2025-01-26 03:57:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7aa553c6-308d-3eae-811c-ed09fb5b0a8b | -16.55194 | -43.71146 | 2025-01-26 03:57:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 286ad449-1801-317c-88ec-c2cbcb3bf571 | -14.79609 | -44.29369 | 2025-01-26 03:57:00 | NPP-375D | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c8db955-2363-3c5b-b90d-8b446b9b8869 | -17.31321 | -49.91422 | 2025-01-26 03:57:00 | NPP-375D | EDÉIA | GOIÁS | Brasil | 5207402 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce9ada4c-fa3d-3a73-a7b5-7c1f351c4c64 | -17.75373 | -42.89688 | 2025-01-26 03:57:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d64d2e49-a595-3c96-93c4-bb396af3bca9 | -19.71795 | -40.3537 | 2025-01-26 03:57:00 | NPP-375D | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1b3f0711-91d3-38eb-ad0c-1a86d4128975 | -13.4772 | -44.01935 | 2025-01-26 03:57:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2d71eab4-8850-3b91-8067-485d089a7b74 | -15.03693 | -45.64064 | 2025-01-26 03:57:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fae4b23a-c8d7-323c-b1b3-2dec9dc729e5 | -13.22873 | -43.97907 | 2025-01-26 03:57:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3fb1d7ad-600b-337f-be5a-49b91c99eaa7 | -13.22508 | -43.97602 | 2025-01-26 03:57:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 58a19a32-56ab-3691-ae2d-94956690bbdd | -19.00587 | -40.50271 | 2025-01-26 03:57:00 | NPP-375D | SÃO GABRIEL DA PALHA | ESPÍRITO SANTO | Brasil | 3204708 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| af3466be-75c4-37f0-940b-7dc858e69c0b | -16.34893 | -43.69438 | 2025-01-26 03:57:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d3671575-b389-3c02-b192-94f60755bf02 | -16.55266 | -43.70731 | 2025-01-26 03:57:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 990bee8e-0aa1-3bf1-9de6-961a675e261a | -13.2243 | -43.98061 | 2025-01-26 03:57:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a64cdc8-32b9-3ceb-a495-86940f19f17d | -15.0403 | -45.64501 | 2025-01-26 03:57:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2138ab63-1a10-3010-9e7a-a87dda12ef7d | -20.12831 | -41.46864 | 2025-01-26 03:57:00 | NPP-375D | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 920ff9e7-123e-328e-a0b7-b56a753be1a6 | -19.83826 | -40.08327 | 2025-01-26 03:57:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| fb1d0652-2457-3d4c-9b9d-c5a1378b073d | -14.79528 | -44.29607 | 2025-01-26 03:57:00 | NPP-375D | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d2fa920-5c25-3525-b75f-7927e3937328 | -22.67811 | -42.85655 | 2025-01-26 03:59:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| ab3d17bb-cd5f-3715-8b21-cd7988006b46 | -20.4173 | -43.55321 | 2025-01-26 03:59:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 567c0423-1c86-3715-9f89-97a7203f1a92 | -21.51628 | -41.09407 | 2025-01-26 03:59:00 | NPP-375D | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 37a96d2c-8023-382a-8698-02b261dccb0d | -31.62639 | -52.36478 | 2025-01-26 04:01:00 | NPP-375D | PELOTAS | RIO GRANDE DO SUL | Brasil | 4314407 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| fa48ec3f-0a0d-31a0-9a72-da88dc3649b5 | -31.62335 | -52.36729 | 2025-01-26 04:01:00 | NPP-375D | PELOTAS | RIO GRANDE DO SUL | Brasil | 4314407 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| c8cef8e7-1b46-3674-968c-4269de870ff2 | -6.5631 | -51.1126 | 2025-01-26 04:10:00 | GOES-16 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| d0d646c6-a1cc-358e-bbd1-5d26da77aa34 | -5.68938 | -39.72207 | 2025-01-26 04:18:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 05b4ac17-6fa0-32c6-a15c-5873c349710f | -3.58932 | -53.81288 | 2025-01-26 04:18:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 70ae75eb-964a-3000-8d70-d26a638a7228 | -5.27283 | -45.77465 | 2025-01-26 04:18:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a170959-5355-3760-9782-6e435a9c57ce | -7.26962 | -39.66376 | 2025-01-26 04:18:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 390c26ce-1442-378c-bcac-26840c9274d6 | -7.59387 | -46.45524 | 2025-01-26 04:18:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ade3dca1-39ba-3fb4-aa01-5313449b1f10 | -5.2734 | -45.77108 | 2025-01-26 04:18:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 817f0695-cb56-313b-ae48-55a5a00d4f44 | -7.5933 | -46.45885 | 2025-01-26 04:18:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3db361b9-5d21-31c4-bf74-9f122ef41f8b | -7.2691 | -39.66741 | 2025-01-26 04:18:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7c3d444b-a84f-30b3-aa2e-10e8d8221eb3 | -3.61689 | -47.31675 | 2025-01-26 04:18:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76318be4-b98d-37f3-a0e2-eb8f2e4738c8 | -7.87934 | -44.19194 | 2025-01-26 04:18:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f79145cc-bf46-3be4-9139-309e2c6d7480 | -3.16701 | -47.72398 | 2025-01-26 04:18:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 546160e2-a663-36ea-9efc-44d1a0cd3798 | -7.87988 | -44.18842 | 2025-01-26 04:18:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fdc25599-794a-3b5f-b06e-2e1497292688 | -6.39699 | -46.33157 | 2025-01-26 04:18:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b4884053-b39a-3efb-9035-9e6339cb4342 | -3.17697 | -48.02977 | 2025-01-26 04:18:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3ce37d40-b8ca-37d8-8cd6-0cb369f57fcc | -5.34998 | -40.65773 | 2025-01-26 04:18:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 218b04f3-c061-3526-adb1-71c744c27ebf | -3.58869 | -53.81655 | 2025-01-26 04:18:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ea9479d-eee3-378f-9b29-2c36682445d3 | -5.35134 | -40.65617 | 2025-01-26 04:18:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2322f10c-c731-3a1a-899f-942197cc2b70 | -3.24673 | -48.07671 | 2025-01-26 04:18:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10b8862c-7c03-3fe9-8e03-b108f77f5bc7 | -7.88321 | -44.18894 | 2025-01-26 04:18:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d0ea908a-e1a3-3e4e-938a-d6fff4734fef | -3.24748 | -48.07209 | 2025-01-26 04:18:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee18a8cb-2a2f-3a6c-8d83-98ccba55cb10 | -7.88376 | -44.18542 | 2025-01-26 04:18:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 80d82ea6-7104-3759-b030-02bb542a2b37 | -15.57041 | -47.85574 | 2025-01-26 04:21:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e482ba82-3173-3c85-9b7c-1e73ec9e46be | -13.48394 | -52.94859 | 2025-01-26 04:21:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b648dfdc-f047-3652-b54e-65acaa629bd0 | -16.54948 | -43.70615 | 2025-01-26 04:21:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b87c4a1b-0d26-346f-a67f-829e79e0a92d | -16.68038 | -43.88438 | 2025-01-26 04:21:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a9afbe4f-6c60-3c80-b06d-420fd8f702a1 | -15.0381 | -45.6477 | 2025-01-26 04:21:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 383d178f-b963-3988-b5b5-18a9665d891d | -13.41337 | -44.42261 | 2025-01-26 04:21:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4ecfc0fd-0f0d-36be-886e-0bf9eed99ad6 | -15.0392 | -45.64044 | 2025-01-26 04:21:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f6b9014a-bc44-3ee7-a2a8-cb032d8bc09f | -9.52687 | -47.77827 | 2025-01-26 04:21:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 08de916f-a9ba-31ae-9903-e26a17d0834a | -13.22734 | -43.97807 | 2025-01-26 04:21:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8924e341-0876-38e1-90bb-a3746d7b2094 | -15.04805 | -45.16031 | 2025-01-26 04:21:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c96c1b8d-1389-379a-8660-1cccac1601af | -15.03586 | -45.63988 | 2025-01-26 04:21:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 52c2e796-609a-3d3e-b378-5aa2c5f54dc9 | -15.04199 | -45.64462 | 2025-01-26 04:21:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20a4e589-1ded-3546-85c9-c774a6558471 | -15.04254 | -45.64099 | 2025-01-26 04:21:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65c4d809-3fee-3560-9049-dc0dbbbe4a2a | -12.11438 | -43.63717 | 2025-01-26 04:21:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 23b1f6b9-881c-3244-927d-e3843d5b1bca | -10.80561 | -45.17456 | 2025-01-26 04:21:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ea012378-361d-3af5-b82b-6ceaa7fc6f99 | -16.68174 | -43.88281 | 2025-01-26 04:21:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e931f846-dcfe-3037-8ddc-7d94187322f2 | -11.17587 | -41.80316 | 2025-01-26 04:21:00 | NOAA-20 | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ef0b560e-8919-3b71-a029-233223cd1281 | -15.04748 | -45.16404 | 2025-01-26 04:21:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7195f771-a731-3352-affb-b59083ecab80 | -14.79501 | -44.29582 | 2025-01-26 04:21:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 898b8b6a-dde6-3ff8-a366-4a89a15dae5f | -15.03865 | -45.64407 | 2025-01-26 04:21:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c51339b7-b33a-307f-8106-a85b6ecd4a6c | -12.11089 | -43.63662 | 2025-01-26 04:21:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 21825e9b-25be-3c57-ab82-02ea0b5d6a72 | -15.0353 | -45.64352 | 2025-01-26 04:21:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 16ecd43e-d19c-354d-b2eb-818c06f596fb | -13.22386 | -43.97755 | 2025-01-26 04:21:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0ff00144-64f6-34df-93bd-8dfc1ae4d39c | -16.54886 | -43.71052 | 2025-01-26 04:21:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 077b0ba1-706e-3171-8f19-cf4fd760ae97 | -15.0431 | -45.63736 | 2025-01-26 04:21:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 85f6ccb7-e050-3b48-ad7e-bef279786ae3 | -10.77283 | -44.55079 | 2025-01-26 04:21:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d690d0d9-897f-3e70-9b22-d9f827ac4952 | -13.47641 | -44.02337 | 2025-01-26 04:21:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5eab768e-3b48-353d-8d6a-5764a694693c | -11.42797 | -38.40967 | 2025-01-26 04:21:00 | NOAA-20 | OLINDINA | BAHIA | Brasil | 2923100 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 84cc6fa0-3a9a-307f-bc1a-063a14560205 | -12.70596 | -54.92767 | 2025-01-26 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| feb0012d-49cc-38c7-a1b1-a4bf080cdf5e | -10.85089 | -44.31104 | 2025-01-26 04:21:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44cc3144-d343-3e5f-9129-51cf1519abbf | -13.47699 | -44.01945 | 2025-01-26 04:21:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 301cad93-a113-374a-8f2e-6644b94185a6 | -10.77227 | -44.55439 | 2025-01-26 04:21:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7980fa29-e26e-3f9d-9f9a-f779c80d7054 | -13.06118 | -39.77208 | 2025-01-26 04:21:00 | NOAA-20 | BREJÕES | BAHIA | Brasil | 2904308 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 38f08d21-6283-3c63-8389-b4c99eaf7aff | -12.70537 | -54.93077 | 2025-01-26 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 32bf7a48-628e-3bc2-896b-c918610fe786 | -20.41652 | -43.55537 | 2025-01-26 04:23:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| ffaea06e-3790-3ebb-9108-05fde70bb699 | -16.59905 | -46.7922 | 2025-01-26 04:23:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0761bb05-eccf-3e26-a5d8-4f4cb7a34cbf | -17.3131 | -49.9141 | 2025-01-26 04:23:00 | NOAA-20 | EDÉIA | GOIÁS | Brasil | 5207402 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70fae510-1cec-3df4-8965-43d3c6661110 | -20.12839 | -41.46556 | 2025-01-26 04:23:00 | NOAA-20 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 58d270b2-2c0e-33e3-9565-92042685ab19 | -19.00652 | -40.50293 | 2025-01-26 04:23:00 | NOAA-20 | SÃO GABRIEL DA PALHA | ESPÍRITO SANTO | Brasil | 3204708 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1bdc18de-c1a9-34d1-8897-b10416868589 | -22.67474 | -42.85239 | 2025-01-26 04:23:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f8ad1a35-9bba-37ca-986e-2458df8e1fb0 | -17.08543 | -49.39321 | 2025-01-26 04:23:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5436f203-adb6-32af-8360-b341f3533953 | -20.12712 | -41.46684 | 2025-01-26 04:23:00 | NOAA-20 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| cf238072-9ca2-3a02-854a-a3e2ed71054d | -23.98254 | -48.91822 | 2025-01-26 04:25:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b492ceb0-4872-381b-a742-0de13de516e2 | -24.62659 | -54.22342 | 2025-01-26 04:25:00 | NOAA-20 | PATO BRAGADO | PARANÁ | Brasil | 4118451 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 96fbd8ec-2c1e-3621-81da-d7147e3c5d7d | -2.90951 | -54.28905 | 2025-01-26 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 410f6a84-55f5-38d3-a1f3-c84e178c8d16 | -3.59114 | -53.81272 | 2025-01-26 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e55814f0-ba71-3e20-a2c1-b227157f841a | -3.71204 | -53.7104 | 2025-01-26 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78aebe0a-6cc0-3972-94f0-4ad2bb1fe659 | -7.88168 | -44.19109 | 2025-01-26 05:10:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6e9d4459-d608-35fe-ae57-bca205589e50 | -12.70738 | -54.93012 | 2025-01-26 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |


[Clique aqui para ver as próximas entradas](README3.md)
