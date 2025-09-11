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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0bc254b-c2dd-30d6-9314-4d317afb45db | -11.20694 | -54.98456 | 2025-09-11 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a52db2a-6e25-309c-96bf-60282184c863 | -11.77595 | -46.51527 | 2025-09-11 04:46:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dc80f35a-c1f4-3521-880a-25320742a5e6 | -16.0507 | -49.98285 | 2025-09-11 04:46:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 26ff4d1a-c7da-3e36-8848-10eb02f35939 | -9.67527 | -47.52229 | 2025-09-11 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9279d494-3f9e-31ec-b538-af4db2b56058 | -12.10221 | -51.01117 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 31fa1545-7174-3984-963e-7ea3cac31dfc | -10.57469 | -51.5022 | 2025-09-11 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 99fe7cfa-aeb9-3a13-bb63-ad6a2c6f045c | -9.90386 | -49.90677 | 2025-09-11 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e8d06925-aa87-3715-a441-3ada6b6d534f | -9.58785 | -48.0687 | 2025-09-11 04:46:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db789c85-ef02-3b17-86a8-f14ba50c4b86 | -12.01058 | -47.57893 | 2025-09-11 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 7c20b686-20ea-32be-bef3-27ba023d6c23 | -14.56453 | -48.77322 | 2025-09-11 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a48b10c7-d901-3de6-ae09-9f3220d14f4b | -12.13257 | -44.8721 | 2025-09-11 04:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b0f3498c-f9b4-3608-b82b-1084690a0b6f | -11.48055 | -49.26354 | 2025-09-11 04:46:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62e13f39-798a-345b-bce6-bbb480bf3fee | -15.10181 | -50.06934 | 2025-09-11 04:46:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2c1e14bd-4591-3053-a9cb-0d27d8165855 | -10.0482 | -59.36083 | 2025-09-11 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 171614e1-0278-391d-8966-9e7a03d396b4 | -11.94716 | -46.6459 | 2025-09-11 04:46:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c0a9f78-fca8-3872-abea-2e95f0ad35ed | -10.01574 | -51.73238 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0eecf3d6-6995-3b32-a94a-3dc3c5ddbc58 | -10.02622 | -51.73048 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00b6e45d-0093-39e2-b731-daedad4dbf8b | -12.84158 | -52.95414 | 2025-09-11 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d75b21f5-9f42-30af-8442-e482979c8003 | -15.59656 | -49.39427 | 2025-09-11 04:46:00 | NOAA-20 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05117bf2-103d-332a-88e8-24ec06d7d0c6 | -14.40192 | -47.31794 | 2025-09-11 04:46:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9c575ad1-83b3-3cb7-9922-9a48c9f19cac | -14.88386 | -55.87334 | 2025-09-11 04:46:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d5fc0b50-4fad-3bd5-9bb2-0a9af9948205 | -9.72312 | -48.33652 | 2025-09-11 04:46:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2527de8a-6d05-39f5-8016-9ec331b175ec | -9.98524 | -48.37905 | 2025-09-11 04:46:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9c735026-7f07-39a7-9cc3-b09b4bd0e5cf | -9.00683 | -49.52323 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c7b9609a-5047-381a-af80-3c9d03f16788 | -11.48664 | -43.66569 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4e961a22-1bc8-31fd-8c65-2b8b1b30d89a | -10.00181 | -51.71199 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d60f7a5-c6fe-3926-894f-bb6f3fe489eb | -15.60179 | -52.74167 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ec37bbdd-8562-3fd5-9649-e6fdc9226601 | -10.25716 | -48.81995 | 2025-09-11 04:46:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 55e8e397-af21-3442-bc9d-df8add6a7286 | -12.38681 | -54.167 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5cafc541-68a2-3b84-b57b-c89e56907621 | -16.27939 | -45.68111 | 2025-09-11 04:46:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2fc82a00-1086-3e97-b6ad-38ef56f41c3f | -9.80811 | -47.75721 | 2025-09-11 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 64832c9c-a23a-3b6c-8a8e-ac3f7ad1967e | -12.86461 | -47.95958 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a59c6e1-3ce0-3dbd-adff-ff4a4b3457f9 | -11.14496 | -48.46573 | 2025-09-11 04:46:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cef0cc95-0e55-3623-b5c4-959c3c1e096b | -11.3897 | -45.58552 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d4f8c66-c8c6-3f0f-8784-d8e7b03951c5 | -11.34744 | -46.49982 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3731ac40-db81-3bc0-ae26-f51f947aa052 | -11.44316 | -43.57613 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09c5b2ad-0e55-38a1-9d1c-31fc48ff26c2 | -11.12912 | -52.05836 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96c4334d-9bf8-3ebd-bc67-059cb21424be | -13.9026 | -47.99614 | 2025-09-11 04:46:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 861fa60b-b81b-3b44-ad99-b88567f6ce77 | -13.05361 | -47.15168 | 2025-09-11 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 28e7f978-492c-306f-8108-5c12ae1ba4ca | -10.57105 | -52.02203 | 2025-09-11 04:46:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1bf6d553-2844-34b2-90a1-44f6a0b24740 | -11.34167 | -46.47929 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 21ab9109-7679-393e-ab98-40ab4907cc00 | -15.12488 | -47.0287 | 2025-09-11 04:46:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f7e03ec5-0d19-39e8-a410-11569c918ab3 | -9.90728 | -49.9073 | 2025-09-11 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f4bcd751-28a9-385b-8625-8ddce07592a6 | -11.65722 | -52.24062 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e63e01ff-1f05-33d6-a1c2-0be8d331fae2 | -12.16279 | -48.48516 | 2025-09-11 04:46:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f2f9b52-07cc-3d65-be55-75db99272937 | -11.95919 | -46.65141 | 2025-09-11 04:46:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc571b65-ddcf-3695-b677-a41ddbe550c7 | -11.37532 | -43.51492 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 140b6108-d2ca-3744-b348-4e816542ede8 | -14.50881 | -53.9337 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 21ecd938-9af9-3b48-aafa-9c484b80742c | -11.08601 | -51.33357 | 2025-09-11 04:46:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9238eacf-8766-360b-9ac6-0cd7dc52a27b | -12.45977 | -57.19794 | 2025-09-11 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 633188ed-cfdc-361c-a3c6-d33485ecbebb | -11.78222 | -47.32141 | 2025-09-11 04:46:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69e7b519-72bb-3c22-89b6-42174d3e06aa | -10.02181 | -51.73693 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5624761c-d93c-3fb1-ab34-fcc1782c0923 | -11.15196 | -45.29777 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f95ec60-ae8b-35f2-96de-8de6f9a27cfe | -11.19291 | -48.41149 | 2025-09-11 04:46:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6bf6e85c-5f4d-3d14-b4ca-659f7d4364b6 | -10.17864 | -44.76734 | 2025-09-11 04:46:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f46fb06a-b97d-379e-a3d7-d7b055b72c94 | -14.88239 | -55.86035 | 2025-09-11 04:46:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0fb00931-f1d6-3c01-b6c7-8502ff851554 | -11.12055 | -48.39949 | 2025-09-11 04:46:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3a9da74b-fd49-3b42-8c1f-437f68d24251 | -15.08696 | -50.07115 | 2025-09-11 04:46:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a3232efe-fa90-3bb3-aace-1a54b9616695 | -12.39343 | -63.81586 | 2025-09-11 04:46:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 01da3f32-b5e4-322d-824d-d3faee7aa938 | -11.17407 | -55.05041 | 2025-09-11 04:46:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eff23239-a937-3b6b-9abe-cb4d06e264d4 | -11.20626 | -54.98864 | 2025-09-11 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d5dd24fe-9a1d-3340-950c-cfadedfa5283 | -9.20493 | -51.81286 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 618213fa-5185-326a-9628-3930d1e35dee | -15.12173 | -52.40227 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 81c1d173-9825-3eef-b106-b78a500e1dcc | -11.7332 | -50.6282 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5214a035-ab59-37f1-bb6f-78f3d4a53f33 | -13.65514 | -45.71517 | 2025-09-11 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aeb2cd40-7b49-39fc-8918-6b2936ad87ac | -12.84443 | -47.96186 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2dc44044-3d67-37b3-b7b5-7c109897acf4 | -11.46328 | -43.70158 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 99329df1-5aff-359b-8e1d-23f01985bdb2 | -11.44748 | -43.58302 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d3636912-8837-3666-bb78-8008ab588075 | -11.47661 | -43.63922 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5639e5bf-57fb-36d4-a843-51b3f439a875 | -9.08544 | -49.81144 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5578d7c2-ae4e-3fea-9baa-1e7dc5c631de | -11.71794 | -48.24789 | 2025-09-11 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7bcf45b-1dec-317a-a848-ff35906754b3 | -9.76954 | -51.11496 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2bc5c29f-6c1a-3405-85c6-2dd5d2e515e4 | -9.81436 | -46.82294 | 2025-09-11 04:46:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc6b86fe-d77b-3097-914d-7a2e54db7db2 | -12.92762 | -54.80036 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46dea6ca-5397-33e0-955f-15be2a427ca6 | -14.30114 | -45.03945 | 2025-09-11 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b5081437-7d5d-34ae-88c8-3e553e6f42db | -13.29371 | -43.75704 | 2025-09-11 04:46:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4117894c-888b-3fe9-8c73-dc6164540051 | -11.3427 | -46.47163 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 84357c95-1c02-32b5-8c5a-20a0b7f282b2 | -13.34012 | -54.38788 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df01a1ff-fe10-3ecd-b9f2-428da960bab2 | -11.12691 | -52.05081 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6faba83f-f67f-3a15-a8cb-ab4bedfcd8c4 | -12.48131 | -53.82232 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 93f98567-c5a1-33c2-94ad-1f23d21f198b | -12.91897 | -54.76692 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ca0fbd8a-c3df-3914-b644-bf9d691400e3 | -11.43843 | -43.57231 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 08754961-794d-327c-a3a2-c2d87eede190 | -15.55513 | -54.74622 | 2025-09-11 04:46:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a60de360-58b1-36b7-9021-cb6d18ab5637 | -10.06314 | -50.37726 | 2025-09-11 04:46:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 230ba3cc-61ce-3e87-8206-29b683c4cc32 | -11.39384 | -43.53315 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 498293cc-a3f2-342b-8281-ddec33242695 | -11.16484 | -45.30488 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e59d41f1-fd9c-349c-a4ef-0311d1c5ac92 | -11.05386 | -51.34299 | 2025-09-11 04:46:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f365cf8c-3de8-3cff-be8d-7b0ea6fdbf23 | -12.84715 | -52.94054 | 2025-09-11 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4be60565-dd57-3ba3-a1ba-e1c9a55e1c00 | -12.07074 | -47.57399 | 2025-09-11 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 22f99d54-b6c3-3ccc-8103-f6e461659d0d | -8.81068 | -52.00682 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 842f30d8-a839-3b41-b094-27a4a6ee8c7e | -16.08414 | -47.35148 | 2025-09-11 04:46:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 85e749c6-7637-3ec0-a7ac-c0bf1f0a2abd | -10.39225 | -48.58308 | 2025-09-11 04:46:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b81e35b-48b2-3080-8616-78c68d83d4a7 | -11.74298 | -48.12377 | 2025-09-11 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0d6c0a97-cd81-35dd-8c51-c495d5553586 | -9.80231 | -47.77052 | 2025-09-11 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2da54e43-055f-31cd-baf1-a0b5b3dd77de | -12.91691 | -47.98361 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aed96c74-aa8d-31e0-ad7c-3a0f6769a4ae | -8.57238 | -51.30165 | 2025-09-11 04:46:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bbd7f1f7-a835-39b6-ab19-9fae15a2e10c | -14.30539 | -54.7478 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f5c54dc8-aeac-3b1c-bb05-1c72674966e1 | -11.15726 | -52.03056 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ed30651d-a92c-3d2f-aecf-60b695077624 | -10.56806 | -51.50114 | 2025-09-11 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e44d00c-fd40-3f5e-9901-3eea2beb0c54 | -9.44735 | -46.42586 | 2025-09-11 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |


[Clique aqui para ver as próximas entradas](README114.md)
