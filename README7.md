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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1b0c8df-c74c-33c8-856f-721ca2dc40df | -11.08724 | -47.81368 | 2025-10-02 00:11:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| e2f70e83-a53b-3231-8a7c-5e462cc3db41 | -15.55623 | -48.19358 | 2025-10-02 00:11:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 16774949-1422-355e-b4c4-be54efe88747 | -16.87756 | -49.69067 | 2025-10-02 00:11:00 | TERRA_M-M | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 934d21fb-7d95-3f73-b5dc-cdff7e8db9cc | -15.26822 | -46.39971 | 2025-10-02 00:11:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| ddd39341-181c-3e24-b9f4-b7d73650f5b8 | -12.10929 | -43.43045 | 2025-10-02 00:11:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 9dec1841-47f0-3942-aa68-59d41c1a8eb7 | -11.60527 | -42.8588 | 2025-10-02 00:11:00 | TERRA_M-M | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| e7f7a3e2-cb34-3e16-b4ce-8ef7a8b03818 | -11.8317 | -44.99267 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 7aa7f48f-c755-34f9-b734-b61334442bd7 | -15.41452 | -47.04814 | 2025-10-02 00:11:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| b4fc097f-5ccf-36b7-bf6c-2f8036055e53 | -11.34995 | -44.97134 | 2025-10-02 00:11:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 70c4ac8b-b3a6-3695-b3c9-5f9f04d68949 | -13.32118 | -47.82227 | 2025-10-02 00:11:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 20.3 |
| f1acaba7-12f4-33ce-8567-a8dd448bd7b0 | -15.93634 | -43.34352 | 2025-10-02 00:11:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 03938995-8922-30b6-8561-e2b7acdec131 | -15.26353 | -49.31826 | 2025-10-02 00:11:00 | TERRA_M-M | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 56.4 |
| f4643be5-c49a-3b0a-a51a-bdcb475ada25 | -15.78781 | -43.67731 | 2025-10-02 00:11:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3697878d-9494-3685-b162-4827631d140a | -10.54356 | -43.64808 | 2025-10-02 00:11:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 67143fdd-86cb-3a78-8929-b7325e24b4c5 | -13.16335 | -47.83994 | 2025-10-02 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 18cbaad5-a5ac-346b-bd2d-d447b71853c9 | -14.48626 | -48.41713 | 2025-10-02 00:11:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 57f2f239-cf97-3838-acb5-44535a4d3dbc | -10.66007 | -48.52094 | 2025-10-02 00:11:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 3d15cea1-57ff-3304-93cf-2bf6b5b73fc2 | -11.79049 | -47.57459 | 2025-10-02 00:11:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 158fbe3b-291d-39b0-bde9-932649dac29b | -14.32428 | -44.50509 | 2025-10-02 00:11:00 | TERRA_M-M | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e4d35412-c8a7-354f-93d5-f64b9975b9df | -15.17413 | -43.62789 | 2025-10-02 00:11:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 58.8 |
| 40ecd5ff-6968-391f-928d-b946d9927796 | -14.26962 | -41.55081 | 2025-10-02 00:11:00 | TERRA_M-M | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 1b16bdd0-fe9b-356c-9251-07343980c53c | -15.29953 | -46.39462 | 2025-10-02 00:11:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 87a002c7-2007-324b-8dce-8b545f2464d8 | -11.98401 | -47.01567 | 2025-10-02 00:11:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 7b52399d-7c2b-393e-8019-7872550e7e45 | -14.41884 | -46.11608 | 2025-10-02 00:11:00 | TERRA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 42.1 |
| a6c594ff-ad3d-39e7-8add-233da8553f6b | -13.15388 | -47.85692 | 2025-10-02 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 67b075fd-430b-340b-8bd6-68f60a1880b0 | -13.53009 | -47.2697 | 2025-10-02 00:11:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 72624109-92a8-367d-8aa3-aa231b8bc049 | -14.47971 | -48.40596 | 2025-10-02 00:11:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 7db86cb8-b75b-3c79-9b2b-20c12096e5d5 | -13.21921 | -48.51387 | 2025-10-02 00:11:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 4dc8599c-fd47-343b-b26f-f8ed31360879 | -16.87113 | -40.59797 | 2025-10-02 00:11:00 | TERRA_M-M | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 81.6 |
| 797f3f8c-47c0-3ac7-bfca-70a44dedd19e | -11.43492 | -43.88884 | 2025-10-02 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 301337ec-6d19-35d5-a846-ba58e0293c42 | -11.80318 | -47.58752 | 2025-10-02 00:11:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 05253f49-96be-36e2-a8f3-5d11108c5df7 | -11.17942 | -47.26614 | 2025-10-02 00:11:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 76cebdb9-b72d-3f0e-bde0-1fd25f79730c | -15.43502 | -42.76236 | 2025-10-02 00:11:00 | TERRA_M-M | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 11d013b4-0967-371e-8b60-bc9bb124918e | -12.82116 | -47.02272 | 2025-10-02 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 406bc213-ab91-3ce2-b8b2-80e22a90577d | -13.86919 | -51.26316 | 2025-10-02 00:11:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 6c4a1bd5-de50-3aee-b03c-a3ff9366d02b | -11.84511 | -44.96479 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 288f18bb-2f3e-3aaa-ae29-dbc7781def08 | -13.95148 | -48.1152 | 2025-10-02 00:11:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| a25a1d5f-ebdf-3d01-bd87-73540deb1684 | -15.49952 | -42.56051 | 2025-10-02 00:11:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 39e3e3cd-bcc0-30ec-9f60-19f702ea4328 | -12.21682 | -43.75533 | 2025-10-02 00:11:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5263377e-acc6-3af0-b081-fb0d71540502 | -11.81588 | -47.60041 | 2025-10-02 00:11:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 1c50e4da-a775-3313-80e4-5cf44371b992 | -10.21376 | -43.05376 | 2025-10-02 00:11:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 3c3da02c-1b95-3fc7-8568-7630c86262e9 | -13.16524 | -47.85563 | 2025-10-02 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 3e766eb9-2517-307f-8904-57a86a9d9170 | -13.80386 | -48.04066 | 2025-10-02 00:11:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 764b6e06-4e4b-3300-a07d-d9bbf4bc8c7a | -16.13582 | -46.674 | 2025-10-02 00:11:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 218c07ce-7107-3903-af6e-fe4a2d05c08a | -14.3516 | -45.98431 | 2025-10-02 00:11:00 | TERRA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 45725783-ffce-316b-b6bb-5d80c153d20f | -11.98105 | -50.57933 | 2025-10-02 00:11:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 25716947-b732-3c4a-8053-a5109543b3b8 | -12.84955 | -46.94478 | 2025-10-02 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 20e8bce6-61a0-3827-9b5b-f75a6388da1e | -12.90037 | -46.92392 | 2025-10-02 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 76b8e5fa-9684-332d-9c35-8b47b5e8e74c | -13.31361 | -47.8559 | 2025-10-02 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 22.1 |
| e28a90ca-86f3-3c83-8db8-a3623021378d | -12.68366 | -46.91298 | 2025-10-02 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| fe21e919-68f8-35a3-9070-bc2f41712a55 | -11.81404 | -47.58607 | 2025-10-02 00:11:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 39.7 |
| beea3832-c462-3af7-afc9-0cfea70ccff0 | -16.28851 | -45.24171 | 2025-10-02 00:11:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 56660762-0dd0-3b47-b61f-46b65fe48c9d | -13.16003 | -47.81221 | 2025-10-02 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 39.2 |
| eea5458f-0142-3d25-80d9-1229234d0e28 | -10.35426 | -43.74204 | 2025-10-02 00:11:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 9d59f41b-c631-3d4b-bd07-71c860061934 | -10.82004 | -46.61057 | 2025-10-02 00:11:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 492eced4-7146-3134-a036-fb87ccc4964a | -13.96321 | -48.11378 | 2025-10-02 00:11:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 40848671-f6fd-3297-87c5-a04f0a04f469 | -16.54105 | -42.50521 | 2025-10-02 00:11:00 | TERRA_M-M | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a6994b7a-327c-3572-a39e-8ba4cb8b2c6b | -11.16892 | -47.2676 | 2025-10-02 00:11:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 218.9 |
| d8a1e40b-f096-3a68-a1a8-45762dc733bc | -12.87002 | -47.02435 | 2025-10-02 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 4c7c32f2-d3e9-3192-980e-2a2434b9a17c | -13.95364 | -48.13319 | 2025-10-02 00:11:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 2993cf24-8672-365c-8495-9929c2a31ee4 | -12.51285 | -46.84504 | 2025-10-02 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 472ce074-4e69-3508-b947-bec2e4f81d4f | -9.94983 | -43.74293 | 2025-10-02 00:11:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| c52634f3-dd87-320e-912f-fc0934f6cb5d | -12.09719 | -39.95549 | 2025-10-02 00:11:00 | TERRA_M-M | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 20.5 |
| 244ca396-9dd1-3ff6-9952-879775f00472 | -9.91086 | -43.67332 | 2025-10-02 00:11:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bc9fe753-c5eb-3b8b-96d7-8ab410bf90c2 | -14.90176 | -48.32058 | 2025-10-02 00:11:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| b3cedcb0-da81-35db-878b-9066f8a084f3 | -9.89626 | -45.946 | 2025-10-02 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 31ec5cfb-9fcd-3121-a64b-c49570ee417e | -12.75375 | -46.91087 | 2025-10-02 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| bec6bb27-90ba-337b-8847-d29d0fe11f22 | -14.2166 | -46.13086 | 2025-10-02 00:11:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 65d3e8f9-c13d-3f0d-a2f2-b96fffb4bea7 | -13.23973 | -47.34804 | 2025-10-02 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 2556e95a-671d-34b7-b086-affa4f9eabe0 | -15.41154 | -47.03957 | 2025-10-02 00:11:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e76e2b6d-3ef9-3755-b17d-879a973f1cbc | -11.42623 | -47.29672 | 2025-10-02 00:11:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| c701b2fd-54d0-3931-91ad-7326e32b12c0 | -11.80567 | -47.58111 | 2025-10-02 00:11:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 0a3f53a7-d3af-31d4-b0ca-07d6912ebd49 | -10.34545 | -43.74331 | 2025-10-02 00:11:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 1dd0c47e-0eb1-3e2b-9510-4ff2a772605a | -9.94102 | -43.74419 | 2025-10-02 00:11:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1603.5 |
| 7a4c977a-9df7-3527-bd17-b7337b0a552c | -11.81079 | -44.90622 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 2f887e41-2066-30a8-93c5-ea8914907ab6 | -12.65705 | -46.95638 | 2025-10-02 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 19d7b5db-2825-3216-9700-ddc7b7e95d3c | -9.94637 | -43.65277 | 2025-10-02 00:11:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 4b27d8af-8d15-3f55-99ab-21c24d6bf137 | -13.76098 | -47.9545 | 2025-10-02 00:11:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 1202689e-98d5-331f-915d-4a7e22676b86 | -5.99367 | -44.59262 | 2025-10-02 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| a6492e07-593d-3060-964c-d630406029f4 | -4.62807 | -49.37743 | 2025-10-02 00:13:00 | TERRA_M-M | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 68600ecd-3bbf-3ecc-8f92-edc491292a05 | -8.2136 | -43.59323 | 2025-10-02 00:13:00 | TERRA_M-M | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8e7c2a94-6a42-30b2-9cda-01cd5838f7f6 | -4.15174 | -41.52142 | 2025-10-02 00:13:00 | TERRA_M-M | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 3dd13d8d-f49f-324a-aa78-db4f781219a7 | -9.00364 | -46.69972 | 2025-10-02 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 008ea325-9bdf-387d-a89f-0060896e3154 | -7.55512 | -42.64553 | 2025-10-02 00:13:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 25.3 |
| d5c10809-fa64-360e-9fe4-cd01834c6752 | -4.83593 | -45.42732 | 2025-10-02 00:13:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3ef0ef9b-9a92-35b8-8f92-4e1928398015 | -5.95874 | -45.89225 | 2025-10-02 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 28557b58-7b22-3c5c-b1dd-d53d09fe41dc | -4.48462 | -47.67307 | 2025-10-02 00:13:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a37730d2-aec4-3694-9944-e37c2d37aa43 | -7.04521 | -43.34368 | 2025-10-02 00:13:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 02492037-3b35-30e5-9db5-7bb5a70e9101 | -6.82247 | -47.98034 | 2025-10-02 00:13:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 2fb9287d-7797-34e8-bf6a-97e247714d9b | -5.97571 | -44.61042 | 2025-10-02 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| a455ca4f-07c3-3119-bbed-766a669db15c | -5.96569 | -44.60286 | 2025-10-02 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 12cfd9a6-73e0-3a3f-8dec-f80792814368 | -5.09898 | -43.80255 | 2025-10-02 00:13:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| af8a17df-b880-3470-b9eb-e1ccb1fbab9f | -6.86135 | -48.65306 | 2025-10-02 00:13:00 | TERRA_M-M | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 26535625-09b7-3fab-8ee7-d5c4eb152047 | -5.85456 | -43.40118 | 2025-10-02 00:13:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 2529afec-0f2c-3d37-aab8-d1a4a8fd8a15 | -7.79364 | -42.506 | 2025-10-02 00:13:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| a7884dab-275e-332a-9e68-2fffda58ff1d | -6.04185 | -42.43933 | 2025-10-02 00:13:00 | TERRA_M-M | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 51a5e0e9-475b-395c-8658-c54e3f7c9e06 | -4.01042 | -43.27166 | 2025-10-02 00:13:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 72eb4dc8-d7a1-3c96-be13-e5c003f51e00 | -4.98922 | -45.26648 | 2025-10-02 00:13:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 81a637c3-408f-3170-91a2-377d0098ff26 | -6.46255 | -44.5859 | 2025-10-02 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 98d24773-8038-389d-b83b-a0c8a322c781 | -3.70042 | -49.56921 | 2025-10-02 00:13:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |


[Clique aqui para ver as próximas entradas](README8.md)
