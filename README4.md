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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e17e030-9067-3606-ae73-f8e860007b34 | -10.7452 | -44.873199 | 2026-08-31 00:11:00 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6e7d91c3-c16e-34c9-9879-c7e0af7d09fd | -14.4301 | -52.5172 | 2026-08-31 00:11:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ed583de1-3340-3e0f-ad95-a5a389defc16 | -10.1465 | -45.7001 | 2026-08-31 00:11:00 | METOP-B | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bed104b8-db72-329f-b626-ef0a066d350a | -19.1479 | -57.377602 | 2026-08-31 00:11:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 942b7c3d-ad8b-328b-b7c6-15f713023403 | -3.4139 | -50.129002 | 2026-08-31 00:11:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b539762-ae1f-3c56-af09-387d8d0ed885 | -7.5212 | -55.326 | 2026-08-31 00:11:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 440f1fb5-c16b-3f47-addc-27702e4f5ab5 | -5.8785 | -57.760502 | 2026-08-31 00:11:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 765e6a21-c357-331e-affc-76fd01d5936d | -7.4921 | -55.285198 | 2026-08-31 00:11:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f7da486-147b-354b-8a59-4bdad84a3ef2 | -7.3373 | -60.575001 | 2026-08-31 00:11:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 96699309-fc09-3318-8996-9f190ad6f2be | -6.1218 | -57.660999 | 2026-08-31 00:11:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 224f85ae-d5ef-315c-8ae5-0ae0213866e4 | -5.9432 | -57.6824 | 2026-08-31 00:11:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65876e7e-a6b1-3b92-acf2-d26200371190 | -11.0261 | -57.235699 | 2026-08-31 00:11:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c99669a9-f351-3855-9f1d-c7e5aa47fcc8 | -18.2764 | -52.657799 | 2026-08-31 00:11:00 | METOP-B | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f062144e-a39d-333d-81e7-e8531532eff7 | -11.3461 | -45.1856 | 2026-08-31 00:11:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 078e562c-4969-391e-912c-8bbc51892dd4 | -1.7515 | -46.2799 | 2026-08-31 00:11:00 | METOP-B | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e9cec3c2-d295-37dc-9c39-89e5ea239c20 | -5.6109 | -44.007301 | 2026-08-31 00:11:00 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0fc24564-0737-33da-a9a8-9bc80caf32b9 | -6.1185 | -57.645599 | 2026-08-31 00:11:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54f2f384-02a7-3cca-bdcb-a4c79de26943 | -15.6562 | -45.9072 | 2026-08-31 00:11:00 | METOP-B | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 51a900f0-0bfb-3010-a82d-81a204a435f9 | -13.9325 | -54.399399 | 2026-08-31 00:11:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 368c40aa-3fb7-3b05-a347-e8b45f521ebf | 1.101 | -50.9818 | 2026-08-31 00:11:00 | METOP-B | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| d40f4a54-a0b2-3aa4-8f33-5dab24561ac6 | -6.1807 | -44.933399 | 2026-08-31 00:11:00 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eb79000a-1d85-3b75-8413-978c89e83eb5 | -4.8503 | -55.836201 | 2026-08-31 00:11:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4db54c3c-6a55-3db5-8eec-5e7c8ce5285f | -19.138201 | -57.3792 | 2026-08-31 00:11:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| fe9845d2-2c03-3681-a2ba-5f1eeaf3ab6e | -1.5989 | -54.408699 | 2026-08-31 00:11:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2e0439c-fb70-3813-bd6e-f790c70f2f73 | -7.9167 | -44.262199 | 2026-08-31 00:11:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 56eb22ba-3eb7-35d7-860a-85c5ea4eb939 | -16.277901 | -42.582199 | 2026-08-31 00:11:00 | METOP-B | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9e8d6fb8-c70d-3ea8-810d-1282fab3d2c0 | -5.2438 | -55.9049 | 2026-08-31 00:11:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed15ebde-71d8-3fad-9b2b-3ba6faabfcfe | -11.3299 | -45.160999 | 2026-08-31 00:11:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a3971c35-5354-349f-b66a-eb337d19594e | -10.7613 | -50.860401 | 2026-08-31 00:11:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 60bc79b9-0b26-3514-878d-91c161042f5b | -5.6078 | -43.994701 | 2026-08-31 00:11:00 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f620f8c1-ae47-3004-8e7f-4affd076fdf3 | -14.5971 | -54.111698 | 2026-08-31 00:11:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8a35b756-83e7-38c3-b60a-3926c11b7f8a | -15.7676 | -49.943401 | 2026-08-31 00:11:00 | METOP-B | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e834c41d-51f8-3e7d-a376-33356d864945 | -11.2216 | -45.1395 | 2026-08-31 00:11:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 149780d8-582f-3624-a2dd-13aa19d0a123 | -6.627 | -53.180099 | 2026-08-31 00:11:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f18abf3-2e7a-3384-b73c-47400e65589d | -11.198 | -43.369999 | 2026-08-31 00:11:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 78bbb8b5-9d75-388a-8d43-3bdacc1ecffe | -10.7344 | -50.643501 | 2026-08-31 00:11:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 79939721-6ee7-3532-86f9-e880d59b76bb | -15.2329 | -56.376499 | 2026-08-31 00:11:00 | METOP-B | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 74807055-9d09-3abb-b6eb-3b38279778a3 | -15.2401 | -53.868099 | 2026-08-31 00:11:00 | METOP-B | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| da4c0c67-7b1d-3dbe-abaf-5b79bd93342c | -10.326 | -49.956699 | 2026-08-31 00:11:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 64499b82-129e-3f4a-a366-4c673bb50d55 | -14.3025 | -52.892601 | 2026-08-31 00:11:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4a7078e7-67ce-3241-9a00-687a2f13c252 | -5.8764 | -52.153 | 2026-08-31 00:11:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3abb0396-2361-34f9-bfb6-b1545052505d | -5.8523 | -57.542801 | 2026-08-31 00:11:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ada8225e-5e7e-3f0e-9224-ea6120636414 | -10.7397 | -54.0257 | 2026-08-31 00:11:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8fb318e2-ad31-35fe-af2c-23c3e19d0a50 | -7.2837 | -49.8395 | 2026-08-31 00:11:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0089e65-615d-3f11-9200-55b11aa33e5c | -15.0716 | -48.014301 | 2026-08-31 00:11:00 | METOP-B | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1695dc28-5525-3803-b8d5-47a856db693c | -15.914 | -56.191502 | 2026-08-31 00:11:00 | METOP-B | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 50fa2b69-51b1-32ba-b11e-45575c469549 | -10.8427 | -45.3269 | 2026-08-31 00:11:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4a694ca0-2a7d-39d9-85e4-70a96c1b6f62 | -10.3503 | -49.973301 | 2026-08-31 00:11:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 310ce569-a21e-30c2-b1d7-b66d450a0c7a | -14.3969 | -52.554401 | 2026-08-31 00:11:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8ff27ece-dcc8-3a5e-b21c-345cb758a290 | -10.8012 | -50.667 | 2026-08-31 00:11:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 52a6eb7b-4f48-3aec-b98e-f27d35cce4ff | -10.5963 | -52.233299 | 2026-08-31 00:11:00 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2cb86579-fae7-310a-8f49-7cde660bb233 | -11.7878 | -47.6614 | 2026-08-31 00:11:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 15b27bed-1b9c-38a2-9649-6d7dc3587e45 | -9.1996 | -51.5639 | 2026-08-31 00:11:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 440a41cd-03ac-332f-b68d-e01a719592ee | -5.5656 | -60.2052 | 2026-08-31 00:11:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b48cb5e5-6d37-3a14-b947-1a695e33c4c7 | -14.3122 | -52.890499 | 2026-08-31 00:11:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 31710bed-ae89-3d82-8958-cfb1f28a3fab | -7.6131 | -57.5979 | 2026-08-31 00:11:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28d0511f-8edb-36d9-9d90-1ccb341f199f | -6.5269 | -51.424301 | 2026-08-31 00:11:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6faff0f-6900-319e-ba76-9e2f95e7f702 | -10.755 | -44.8708 | 2026-08-31 00:11:00 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 60be31a8-24fe-3991-a326-f09208609df1 | -11.2325 | -45.098499 | 2026-08-31 00:11:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cfce98f6-0883-33e6-bf78-b712dc19e89f | -18.2959 | -52.653702 | 2026-08-31 00:11:00 | METOP-B | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 98c4a81f-f854-3ab5-84ca-8acfd57df3b0 | -10.0653 | -48.699699 | 2026-08-31 00:11:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d58d1673-169a-31c7-a726-aa2dbc512ad2 | -14.1749 | -52.867199 | 2026-08-31 00:11:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 85634c73-be50-3676-9ec4-b148e164635b | -12.1391 | -47.258301 | 2026-08-31 00:11:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 06ccc503-29c6-3da3-95e8-4d953df1abd8 | -12.7234 | -49.0751 | 2026-08-31 00:11:00 | METOP-B | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3692b1bb-729b-30b6-bb22-69b45cfeee33 | -11.2628 | -45.052502 | 2026-08-31 00:11:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b324687a-11e2-33a2-9a36-38c3bb4818e1 | -14.4203 | -52.519299 | 2026-08-31 00:11:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 94d84200-5a3e-3966-bc4a-addc4795df3e | -14.2336 | -52.8549 | 2026-08-31 00:11:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 247ea405-43c6-3555-8ed8-c2480bd5ebfa | -15.4136 | -52.690498 | 2026-08-31 00:11:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5724d7fd-703d-370f-9a10-5856adc3bdf1 | -14.9921 | -48.166901 | 2026-08-31 00:11:00 | METOP-B | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fbc77197-2b46-306f-989c-f3d8ab6c2cee | -11.3245 | -45.181301 | 2026-08-31 00:11:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 806515ae-4390-39b8-9912-a69a4f69db90 | -4.9652 | -55.8466 | 2026-08-31 00:11:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8357ca45-3771-3901-af21-6f34d12597e0 | -4.1475 | -60.669399 | 2026-08-31 00:11:00 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 67449be8-6dcf-3bd8-a92a-65b3e7124a81 | -10.7354 | -44.875599 | 2026-08-31 00:11:00 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7b4086fa-9fba-3ad5-b79a-a4c964a76a08 | -12.9429 | -45.915298 | 2026-08-31 00:11:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 743655ca-045e-37d6-b4e1-f934012d43d4 | -8.5962 | -46.480701 | 2026-08-31 00:11:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 53006ced-18de-3bd0-9822-264185915613 | -7.5449 | -47.326302 | 2026-08-31 00:11:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9c290473-0b74-3d73-b441-772e2711e7d4 | -11.3363 | -45.188 | 2026-08-31 00:11:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| deb88d9e-1dac-3cf6-affb-dde4eda4116b | -15.4234 | -52.6884 | 2026-08-31 00:11:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b271741a-edfb-3a76-9082-67bb6eecd52c | -8.2354 | -49.0364 | 2026-08-31 00:11:00 | METOP-B | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 7fa15201-c968-3e04-9ff6-325ef4b84f75 | -11.3525 | -45.212502 | 2026-08-31 00:11:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 58fcf815-4393-3899-ad12-1f49fed4e18a | -5.7328 | -49.133202 | 2026-08-31 00:11:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| adb0fc16-15fe-3dd5-8f25-23cbcfb2ca54 | -10.7376 | -50.6581 | 2026-08-31 00:11:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 827a3ef7-f7c5-3025-b3e9-c793e9daa6cf | -5.1326 | -49.393799 | 2026-08-31 00:11:00 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99c2047c-a316-3b4b-a533-5b55e6b8c9d7 | -11.0856 | -51.503799 | 2026-08-31 00:11:00 | METOP-B | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cff167f3-38ab-326e-9560-0d9c7b9ad5e1 | -5.7115 | -52.290298 | 2026-08-31 00:11:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47715b5f-fa3e-36f2-bc12-538077a65847 | -10.149 | -45.754601 | 2026-08-31 00:11:00 | METOP-B | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7d402298-3505-32c4-a551-7ffa943dc41c | -12.0985 | -45.049099 | 2026-08-31 00:11:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2e20d357-c47e-3698-a100-5ab61ae8aaa6 | -14.6143 | -54.0956 | 2026-08-31 00:11:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f606be66-de42-3bee-9260-3125fb992f34 | -14.4105 | -52.5214 | 2026-08-31 00:11:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ede3daa7-3741-3f3a-8b0a-6bab2253d829 | -11.0741 | -51.498199 | 2026-08-31 00:11:00 | METOP-B | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| aa20faf1-c4a5-3a03-bde4-3169681e619d | -15.1955 | -46.2369 | 2026-08-31 00:11:00 | METOP-B | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1abbcbb7-196a-3e64-a1b4-2b0c0c9cab41 | -9.4387 | -45.674198 | 2026-08-31 00:11:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b41070c6-0e0b-3373-85bb-0b7f37a467b7 | -10.7996 | -50.659698 | 2026-08-31 00:11:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1dcad761-f656-3c03-9f4b-eb0d1d61de3c | -22.489401 | -48.571701 | 2026-08-31 00:11:00 | METOP-B | BARRA BONITA | SÃO PAULO | Brasil | 3505302 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 30d6a057-3084-3f94-b887-0122f346420a | -5.8708 | -51.7117 | 2026-08-31 00:11:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2713a258-97ec-3752-bf97-fc997d308bcb | -6.2097 | -53.569901 | 2026-08-31 00:11:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ce89018-c64f-3ad7-8c57-418a8b11a099 | -10.7527 | -44.861301 | 2026-08-31 00:11:00 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2491b605-9cbd-3072-b7ed-45e6868e074c | -1.605 | -54.3899 | 2026-08-31 00:11:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1d57bbd-1703-3eaf-afa1-fce52990b0ee | -12.7219 | -49.0681 | 2026-08-31 00:11:00 | METOP-B | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d14a322c-6641-38cd-b784-b664742e7dc2 | -4.0068 | -48.930401 | 2026-08-31 00:11:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README5.md)
