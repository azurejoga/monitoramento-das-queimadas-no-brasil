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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f17aaa1-2b2d-3247-bda4-5635f09d8a60 | -11.48246 | -44.97575 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 796b46f4-77e1-3eb5-bfa4-1373a7a0beeb | -7.05612 | -43.21791 | 2025-10-05 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f5e31714-b10b-3d6a-bf39-3c6827776c30 | -10.94957 | -47.05561 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 543146cd-6fed-3517-ae83-4c1b0b7f0baf | -8.82213 | -47.27856 | 2025-10-05 04:46:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c2f10a1a-4285-308f-b8ef-c2d887577761 | -10.83517 | -57.16923 | 2025-10-05 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7acd3554-f630-3eb0-8d76-39c8e3abc944 | -10.6458 | -49.16024 | 2025-10-05 04:46:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6b03a622-9ca9-3779-bc4d-84f59c810b35 | -8.58184 | -46.32306 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 5700476a-9489-3c8c-a474-51506594ef17 | -11.53621 | -47.68032 | 2025-10-05 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 96eb7896-94d1-38b2-953c-d1a95ab0535b | -7.61802 | -45.46193 | 2025-10-05 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 22e1a80e-b43b-3b8f-a6f0-729b4b1a395f | -7.44354 | -46.52214 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 741d9e05-10d5-30d2-8444-732f31c46ffa | -10.45542 | -47.80822 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 785372aa-b869-3c02-a81b-040be2d1735c | -12.45336 | -45.52838 | 2025-10-05 04:46:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 42473509-bae3-3128-ba64-1b06a1dc90d6 | -10.46031 | -57.49823 | 2025-10-05 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f311bb58-9428-3e35-aa75-00d1fbb96eb3 | -11.05902 | -47.77334 | 2025-10-05 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 895972df-c69b-3f0b-8318-cdc9e394ae0f | -12.30673 | -55.15327 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d8d51af3-27b0-37d7-a02a-5142efd04c21 | -7.79156 | -44.54572 | 2025-10-05 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3a70ae25-4611-3889-a446-88f238e5b97c | -11.47566 | -51.45333 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ed29e0a-5423-374d-ab6c-776d38f53a5c | -7.7373 | -46.32306 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 11dc0e07-be8a-345e-9813-699fbe84860c | -7.02261 | -42.78689 | 2025-10-05 04:46:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| fc9b3d30-ea4e-3abd-bad8-e67e5b507192 | -11.06975 | -47.89254 | 2025-10-05 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 053bea6a-0c7e-3324-b67e-d7235a24db0e | -8.62608 | -54.62713 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e92a86c-3bc8-32b5-b5bf-18be0059323f | -9.7807 | -47.73818 | 2025-10-05 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3bed3c5c-0f6c-3a18-8948-07aac958ab93 | -6.70911 | -42.83678 | 2025-10-05 04:46:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8e02b953-0431-31ef-bc54-d08ac6cb0908 | -12.30947 | -55.1371 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ea8430e-8575-3fbe-a054-46fe78227a3a | -12.45761 | -44.64001 | 2025-10-05 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 890ac59f-0278-3618-a311-8552c0d62a87 | -11.45812 | -51.52292 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ec8426ce-0eed-3ab6-9912-e15ea6b6d037 | -13.32573 | -47.5693 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a915997c-9b03-3073-af35-5684506720bf | -11.10687 | -47.87833 | 2025-10-05 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5453ce11-871a-3473-a3ba-f226de354c13 | -9.45597 | -56.64871 | 2025-10-05 04:46:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f812c424-aba7-3619-928e-985f0dd055c4 | -8.55792 | -46.31567 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5e649396-74e4-3c2b-b41f-aa495cb59662 | -11.26116 | -47.66598 | 2025-10-05 04:46:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5ce22194-b10d-3eeb-9a39-0a99877a0c90 | -11.53989 | -49.80092 | 2025-10-05 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 15ef8bd0-e2a5-3ecb-af4c-db0ce766f7ac | -11.80425 | -46.85188 | 2025-10-05 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ff18e5a0-aecb-300c-a5fc-6307b5adeca4 | -9.88998 | -43.7048 | 2025-10-05 04:46:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3b788c9e-b5cc-388d-acd0-98e22ad32aab | -8.62821 | -55.00172 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8af8fa44-5453-307c-aa75-de3e2089528b | -8.93523 | -48.66489 | 2025-10-05 04:46:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 50748373-5287-3fd1-a75b-70fed54bf9c6 | -13.30991 | -47.80057 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23c0ffb3-885a-3c43-b4ec-8af11ccf0e9c | -12.59621 | -48.14658 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 27058927-726e-30e0-96f6-0172a373115a | -12.32079 | -55.15567 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e994d1f0-17ad-3d2f-aab2-968ccf93bd75 | -11.11862 | -47.17479 | 2025-10-05 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4091012-dd68-36b2-94cb-ec53c0899381 | -6.87739 | -47.23108 | 2025-10-05 04:46:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e6fa6691-66de-37f9-b6bd-253ceacd3c5d | -11.0268 | -45.57666 | 2025-10-05 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 552b3af3-2f45-3572-8c3a-f5fbc0eca1ce | -12.89042 | -47.29116 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5152e381-cf5d-3abd-95a3-f24c6ac450d5 | -13.139 | -50.88146 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 48c1a5c3-4ae8-37f2-848b-f4cadddac332 | -11.92603 | -55.90617 | 2025-10-05 04:46:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 113d3846-9a36-3f21-b891-e3cacd8aad76 | -9.15038 | -59.5325 | 2025-10-05 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1ac9b450-2af9-3ee3-83e8-10ba28d1a932 | -10.64844 | -46.34379 | 2025-10-05 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 974e740a-079b-3737-bc0b-17a6227056ae | -11.74217 | -46.81416 | 2025-10-05 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6a889827-f076-353b-a028-f6fe49cad75e | -8.87955 | -50.88928 | 2025-10-05 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01d047d1-c02e-3734-9120-e856ad7eab01 | -13.28379 | -47.17855 | 2025-10-05 04:46:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| abad4e39-2fe9-3b36-b087-4db4bf4509c6 | -9.27866 | -45.66842 | 2025-10-05 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 73aaeb5d-3db2-37d9-aa70-b60291197311 | -12.45852 | -45.52419 | 2025-10-05 04:46:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7dca6b8c-ed28-3250-85cf-96079ca75167 | -7.60841 | -45.46856 | 2025-10-05 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 61ce9c2c-9d1e-3665-a751-0eb35d97fd49 | -13.26392 | -47.60289 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 48f337e6-91e0-3724-8275-6e1232189a33 | -12.30811 | -55.14516 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 997515ad-9114-3a82-ba32-d785d1e5c352 | -13.08973 | -47.94198 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 75967fc4-de8d-36ab-9e2a-bd7125065055 | -13.1289 | -47.97877 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a87908e1-1d20-3900-8e35-23ce536a0bf3 | -10.17986 | -58.17876 | 2025-10-05 04:46:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca929bca-0276-3924-882d-2fddbf68710a | -11.43312 | -43.4825 | 2025-10-05 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 59f59ff9-f99f-3d3d-9f2d-49f409a13cc1 | -8.54163 | -46.31399 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 570c4228-f607-372c-9bd2-fd0cb04e0c09 | -12.45397 | -45.52362 | 2025-10-05 04:46:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 33c12a3e-73bf-3f6a-9aaa-4f96975a4a62 | -6.73854 | -48.17804 | 2025-10-05 04:46:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11c9a573-e873-3d15-8cad-42431ff620c6 | -9.04871 | -61.6392 | 2025-10-05 04:46:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 917c1015-eaf9-302f-9b7a-49252f81206a | -11.2361 | -47.7862 | 2025-10-05 04:46:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ae9a2755-aa88-3384-ba24-e9b72fdf36a8 | -9.38404 | -45.86765 | 2025-10-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 810690d4-6d90-3294-85db-92efe2eca016 | -13.85754 | -43.98661 | 2025-10-05 04:46:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7d9a5218-079a-3b38-babb-1c68f3d7f19c | -12.27273 | -55.13605 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6099a9a2-b166-3e99-8ea7-3ea97a7965fe | -11.95026 | -55.32482 | 2025-10-05 04:46:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6dda6ff-a39c-3a97-a522-76f8b0eefdf2 | -13.15581 | -47.95713 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a96fe8db-8a40-36b5-9a94-883da1e09c87 | -13.52224 | -47.28444 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9cfeacbf-62de-32d0-b7b3-0d10ca12f57a | -11.09773 | -47.74931 | 2025-10-05 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 60241759-0a6c-3df2-bed5-b20dc3a754b0 | -7.63024 | -45.46766 | 2025-10-05 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 14c59226-8136-3d67-8d01-365dce4e8791 | -9.2788 | -46.00396 | 2025-10-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8afe2d15-971f-3521-beb7-687ce909346e | -12.77945 | -48.82269 | 2025-10-05 04:46:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f077832e-29f5-39bf-8921-79870beaa9f0 | -11.12882 | -47.91555 | 2025-10-05 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b1f5b9fb-453b-33b3-956b-4288540930c1 | -9.64744 | -54.31572 | 2025-10-05 04:46:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d13d1636-eee5-312e-aaa4-0143d5c4874e | -7.79608 | -44.54655 | 2025-10-05 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7c5170da-1c32-3bd5-b967-3f366a23013f | -10.58125 | -51.60605 | 2025-10-05 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c006edec-8cf2-3fa5-ae4e-902e6230870a | -8.54216 | -46.31034 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1882babf-3736-3dc2-929e-89609f1d04db | -11.78956 | -47.92214 | 2025-10-05 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8dd23ee5-9cd4-3e4b-8f0e-48fe45248d64 | -13.29832 | -48.11767 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 111fa1ce-c023-39ae-87d7-2ac698a19442 | -11.56206 | -47.69422 | 2025-10-05 04:46:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0ff00407-3e28-3a60-8bd7-e2529f86f9df | -8.54694 | -46.27737 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6728a001-aacb-3462-b0ce-55edc663fb04 | -13.35452 | -47.20608 | 2025-10-05 04:46:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93695ee8-f5fd-343d-a280-0540de5c3c6d | -13.30656 | -47.61949 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 126d45be-8c2b-3878-838c-dd846663a5bc | -11.85686 | -44.94315 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2cadf39e-9d3b-363f-af51-9f6abab5872e | -8.55721 | -46.26414 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| a8c4572d-4ebd-37e0-bfb7-b940514528d7 | -11.86559 | -44.94933 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 155234af-e683-3df3-9264-91f90b1825f3 | -12.8159 | -46.85096 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| bfe05f9d-26ee-3f98-b7cf-68098e8c9f58 | -11.78254 | -48.89768 | 2025-10-05 04:46:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 045f8bbd-9baa-3356-8b84-e63bb5345341 | -7.25388 | -44.88227 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8e65b3c-98c7-3e45-98f0-b1439562d158 | -13.31472 | -48.08457 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b3aa9a2f-e7b7-3d24-b66b-0ef766060b00 | -13.67645 | -43.1831 | 2025-10-05 04:46:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d3ac9e4a-5cfe-3938-9476-132d991e600b | -11.67921 | -47.48667 | 2025-10-05 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5f97f966-039a-38b4-866f-b5d4506c649b | -13.34659 | -47.57783 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c4ddebd5-65b0-3823-9a83-0c08bcd35834 | -10.06884 | -48.18214 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08971985-7d56-33b1-ad14-b1fde521c8f7 | -13.26601 | -47.61769 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cc8e2bb7-67a6-327d-9eb1-b9ffd7717e47 | -11.06218 | -47.77884 | 2025-10-05 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a740cefd-52f3-38c4-87f9-e30c98db7f81 | -7.16269 | -46.21425 | 2025-10-05 04:46:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b25f134-2126-3760-b752-63215494a17b | -7.73327 | -46.32253 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README99.md)
