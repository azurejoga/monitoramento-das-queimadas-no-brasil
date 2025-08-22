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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ffab751-929e-3f73-98f1-e044c61dc7db | -8.55183 | -66.95387 | 2025-08-22 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e9f8d70-9655-3050-9dc5-fa51d3c7238a | -11.43997 | -47.31419 | 2025-08-22 05:12:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7f68f989-7963-3f12-b722-8308ab028fa1 | -9.66698 | -67.24708 | 2025-08-22 05:12:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6411f25-a253-3298-9c2b-3f8b9db23f32 | -9.27512 | -60.78004 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 625ce383-3132-324d-a587-f623f13ee730 | -12.96121 | -46.2902 | 2025-08-22 05:12:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 580c6783-6ba2-3901-aef9-32af024523d2 | -13.37543 | -47.49633 | 2025-08-22 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0b75d00f-9775-3c52-9b63-655cf5d7176d | -9.22599 | -59.75109 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 131b3b9f-f092-3880-94c4-2d9d0b16df5a | -10.8699 | -50.84732 | 2025-08-22 05:12:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 40fb24d7-0120-3aef-8b01-f46fab2bb39f | -7.29701 | -59.62746 | 2025-08-22 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5ef973f6-b2c6-313f-8418-112563edf0c3 | -10.85883 | -50.81857 | 2025-08-22 05:12:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 45358c04-d37e-35ec-a401-0f210ff8cf26 | -11.90204 | -55.89413 | 2025-08-22 05:12:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81c3791f-c2b1-3419-a9bc-5f89c4338cc2 | -7.5871 | -63.44263 | 2025-08-22 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e2e4bb39-16ca-3eff-aaa4-e6ca00164947 | -9.17778 | -59.70586 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40ee4b9b-d771-3a4e-a240-2b332eb4f95e | -9.93865 | -60.49675 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 35eaa217-8270-348e-86ad-9271698e1f30 | -13.13938 | -46.90023 | 2025-08-22 05:12:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| f833e92d-f58a-3bce-99d4-440dee79c446 | -13.14572 | -46.9018 | 2025-08-22 05:12:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 59fb8391-d110-37a3-af26-75e0d4c26e6b | -13.14534 | -46.89359 | 2025-08-22 05:12:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7b9ecb67-a8e1-3a25-abfc-63ce0b73ac57 | -12.92282 | -46.1713 | 2025-08-22 05:12:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| dcf4d8f8-eaeb-35ac-9003-1c60d4f5064f | -7.93965 | -63.041 | 2025-08-22 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 244f3c8c-aca2-3972-95de-129b270dbadc | -13.02847 | -45.20808 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6582ca2b-d38a-3004-a588-d28bf1be8e2a | -9.22646 | -59.76989 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe176f84-438d-380a-a592-bb2817c5e5b3 | -13.14491 | -46.90938 | 2025-08-22 05:12:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 78e20ac6-2b6e-3fc9-9417-a9cd3e585220 | -12.98897 | -56.89288 | 2025-08-22 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e38a5cd-090a-3fca-ba28-f9eeb2e5760d | -10.49961 | -53.577 | 2025-08-22 05:12:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74e56b50-bc94-3052-9742-cf1f8698ed30 | -10.73921 | -48.23836 | 2025-08-22 05:12:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 21b35b33-e48a-3ca7-a193-f9c61cf3244f | -13.49875 | -47.04787 | 2025-08-22 05:12:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| de0349ec-b701-3966-90fa-2298d9406cf0 | -9.09842 | -61.43393 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ebb36887-ac07-30b9-a764-1cc52c60f1e9 | -12.95651 | -46.2714 | 2025-08-22 05:12:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f66f99c3-dbdb-3911-815a-727d7fe007ea | -13.13896 | -46.90415 | 2025-08-22 05:12:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 486db4db-3933-3d81-bf5c-632847d9da44 | -13.02986 | -45.16979 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 79bdc211-f958-3786-aae3-c20b783a1415 | -7.05671 | -59.83088 | 2025-08-22 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 637dba79-d926-323e-8f06-03e8f34575b1 | -13.02775 | -45.19072 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| efdfb0e3-d337-319a-8d72-3c2728d972e5 | -9.20542 | -59.46933 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fcbb52df-bb6d-3ec4-9370-9b539cb7e381 | -8.55219 | -66.94676 | 2025-08-22 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26db0ef5-af64-31d3-b11b-7aeb46a2856e | -9.20888 | -59.4478 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f90c6dd-98d0-3508-ac09-fe4bfee6eff1 | -13.02514 | -45.17242 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e58e8527-5720-38a6-bdd9-6293e59a06f5 | -9.21164 | -60.79394 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7e9bd0db-018d-3775-a77a-b062ddd3f6b0 | -12.99413 | -56.88185 | 2025-08-22 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef3a1b95-7b5d-30a2-b8af-f195bd630726 | -9.18296 | -59.58766 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0fb9f93e-7767-348e-9f1b-18a64bf5c291 | -10.67866 | -51.56883 | 2025-08-22 05:12:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 40feb0d9-9302-346a-9aac-0b0aaccf8814 | -9.66119 | -67.24935 | 2025-08-22 05:12:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07c3f1bf-695a-3128-8a61-cb2acc8bb0c3 | -12.50206 | -53.80861 | 2025-08-22 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aeedfddb-c9cf-3875-bc59-08a676d48707 | -8.87669 | -62.40996 | 2025-08-22 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8544025d-3da4-37e7-983b-c8013739c50c | -9.21644 | -60.78664 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 90279fb6-f6a4-36a9-a5f1-42107ffb39ae | -9.82283 | -64.27261 | 2025-08-22 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90f4f1a9-382b-332f-b89c-a015a19f1042 | -10.28478 | -46.75877 | 2025-08-22 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 055bb679-48a1-3f79-8d93-1f6ca98f3e8a | -13.02633 | -45.2047 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ad8756f6-ed80-3743-af31-0df8b9746a2c | -12.99722 | -45.23258 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| f005c362-5268-3a72-8bb5-fc2e2fdf9748 | -6.87577 | -59.82151 | 2025-08-22 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 09e1a154-74ad-3f46-b619-be1791add925 | -12.98264 | -56.888 | 2025-08-22 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 74e235b9-f42e-3080-83dd-bdbb30b6ea30 | -9.22075 | -59.78395 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 060fde03-e810-30fa-9d66-038ba7b78814 | -9.21664 | -59.46378 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4fcc6d29-cba4-384f-9c68-1ab5ca1b694d | -13.14356 | -46.90934 | 2025-08-22 05:12:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4cbd91aa-9dc5-37e1-9d06-5c5c4447737f | -8.89044 | -62.42213 | 2025-08-22 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac1792ce-e461-36b5-bb8e-a7c6a128f2ee | -9.51021 | -60.5183 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8fbbc5c3-25cd-30ba-9d46-07626c6793e2 | -8.66127 | -70.04072 | 2025-08-22 05:12:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f3e200d6-4c17-3876-b361-62754c9f6fee | -12.93308 | -46.17455 | 2025-08-22 05:12:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b48a176b-7ad9-340c-8c59-e4637b10a466 | -12.98944 | -45.23851 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9a7c2247-1f67-3fd7-a90e-26f7e0023ebb | -9.09912 | -61.42971 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 946ad3af-45d9-3435-8ead-2d3cf821fe34 | -13.03447 | -46.33716 | 2025-08-22 05:12:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b4a866ac-7dab-33e5-b135-e54344e3f0b5 | -9.94774 | -60.18166 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51b2c68f-497d-3532-99f3-8283836454ce | -10.4629 | -59.13794 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08ed0f58-fd1b-36f9-92ad-63ce10965e0a | -7.62385 | -69.94916 | 2025-08-22 05:12:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fdc73bb0-c8ec-3e9c-b9b0-398b46cc09b0 | -13.16281 | -46.91164 | 2025-08-22 05:12:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4d4b16cd-ff83-344d-b5a0-441c960f71c1 | -9.10204 | -61.43453 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| af2083cf-f09f-3341-a091-e137b85b22d0 | -8.86663 | -62.42302 | 2025-08-22 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 057d1e8c-cf64-31e4-a3ae-f91ba9b2d68b | -12.49046 | -53.80321 | 2025-08-22 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ba25b03-e55b-38c7-8202-2b1023658f6e | -9.0955 | -61.4291 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 11763241-82af-3410-8b58-d95386dd6d5d | -9.17103 | -59.70476 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e12a08ae-88a3-3269-b16b-14733602932c | -9.22704 | -59.77419 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a791920-13b0-3183-b5a4-99ea406bcf56 | -12.93233 | -46.18167 | 2025-08-22 05:12:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4350e964-3fa6-3cfc-b371-dc66646a0c81 | -10.02191 | -64.83961 | 2025-08-22 05:12:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c0be99c-ea19-3a65-b909-4f1eeced6e59 | -13.38579 | -47.50779 | 2025-08-22 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 67995639-a348-3c94-a3b7-d4ffaf4ad890 | -13.37449 | -47.49574 | 2025-08-22 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3f389446-2797-3258-bcfe-5ce5217755c5 | -9.21108 | -59.45552 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e71af983-55c9-3974-a04b-9dba4c9deef8 | -12.98552 | -56.89237 | 2025-08-22 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21690a11-7e55-3e8e-970e-548cefbf7064 | -8.89238 | -62.42482 | 2025-08-22 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 93bf317b-0910-3dd8-84fd-307a2079bc3c | -9.2145 | -60.79848 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 00f00d52-1a99-3c99-b344-90287b9f4e9c | -9.50958 | -60.52215 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dae7892f-2256-3668-a171-63ed5ac0256d | -9.51083 | -60.51447 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 33252dba-fbd7-38d9-9d70-8d5f88aa2f9b | -9.19283 | -59.63379 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8f02f190-10e2-31b0-a8d2-9335a36d92ff | -6.6242 | -58.54173 | 2025-08-22 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9842ced8-849c-3b6a-b54f-4ec5c5191011 | -13.4865 | -47.04142 | 2025-08-22 05:12:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9662831c-78a8-32bb-be58-609e8120cf02 | -8.89349 | -62.42756 | 2025-08-22 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0ba6a44-8ad8-3dfc-bcdd-075f2cd8d8d6 | -11.0781 | -51.04936 | 2025-08-22 05:12:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d8aaf607-bfac-3f35-91d1-91c67c5ddd6c | -9.50454 | -60.50949 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c8027426-f61d-38f2-8fbb-743ab51a9e70 | -8.86679 | -62.3984 | 2025-08-22 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca074ba5-5080-3255-b853-159b9d79305f | -9.10635 | -61.43095 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48f3032b-f7e3-3669-abb2-c2e2c74e081c | -12.96383 | -46.26595 | 2025-08-22 05:12:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b242bf1f-e66f-34cf-a08e-7124a8acc304 | -9.94494 | -60.17739 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70c3988c-e222-3a74-9c5b-9744075a5b69 | -13.01731 | -45.17851 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 850acde0-bacf-3ed8-8327-5fc88359af55 | -9.206 | -59.46574 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1a42519a-ccec-3ccb-8f52-ef960898fe65 | -6.90217 | -59.89981 | 2025-08-22 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b91ed30e-1f6a-3f4a-ae06-20c68434e3e1 | -8.61371 | -62.61058 | 2025-08-22 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| defabffb-c6a0-30a6-8d9d-ec37f68dced0 | -10.85901 | -50.82205 | 2025-08-22 05:12:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 1ebb38b2-3cd2-302e-869b-0464e91385b8 | -9.21165 | -59.45193 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3126353b-8cb3-327f-9c92-e326da2f1a83 | -9.18725 | -59.62548 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dd9410f5-7fc9-32f2-a8ae-c9ab1c4183e6 | -9.22203 | -59.75418 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c43fea34-56ed-3b6c-bc44-c1377344deea | -6.56578 | -60.06058 | 2025-08-22 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39888217-73d1-38c9-ae9c-d79c0b36188a | -11.74106 | -58.31645 | 2025-08-22 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README49.md)
