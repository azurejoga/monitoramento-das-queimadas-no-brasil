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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02201f78-c8fe-375c-848d-ef5e0088dbdb | -10.3131 | -50.5128 | 2026-09-23 02:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 297.6 |
| 834607ec-d3da-3fce-bf7f-8795ac6a0e75 | -6.3293 | -43.9411 | 2026-09-23 02:00:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 53d02473-ac9f-3135-9682-0f72a7158f98 | -11.9063 | -45.7595 | 2026-09-23 02:00:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 69ef409e-18fc-3b8d-b374-f2df2accbd5f | -8.9351 | -61.4759 | 2026-09-23 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| d00029ba-c6b9-3065-8210-e1361a048341 | -12.4216 | -46.9551 | 2026-09-23 02:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 34e37f8e-1ceb-3fdf-a45e-c4811a2f611d | -12.3484 | -50.1779 | 2026-09-23 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 1ffb1342-dcad-3b3f-9ab6-efdf917222d4 | -3.8648 | -58.8211 | 2026-09-23 02:00:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 5c96e9bb-97f0-35e6-8576-fe021e28abcd | -6.633 | -59.9457 | 2026-09-23 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 3e1e6b05-f227-3481-b641-699f507a52bc | -3.6763 | -60.5839 | 2026-09-23 02:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 4ebc506c-87df-3a9a-9aea-ec3510677d00 | -12.387 | -50.1515 | 2026-09-23 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 173.8 |
| b3e574b2-69aa-34d7-a404-fb2d9fef546a | -12.3679 | -50.1539 | 2026-09-23 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 413.2 |
| c70d5246-2214-37d3-aa39-a6b98cf20d98 | -10.3129 | -50.5341 | 2026-09-23 02:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 127.3 |
| 93e38034-03e5-3f38-a2f4-6dca73ce6e1a | -8.4726 | -48.6927 | 2026-09-23 02:00:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 69.4 |
| bd495473-1034-3f62-b0ad-bdababc474d8 | -4.0925 | -62.0874 | 2026-09-23 02:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 0162fdef-51a2-3d9c-9755-812a36875e28 | -1.9271 | -58.2587 | 2026-09-23 02:00:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| aa152e1a-272c-34e9-952d-81daf5e4562f | -12.3676 | -50.1755 | 2026-09-23 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 232.1 |
| a0f44f3c-3d6c-3f3e-8b20-f26d38c14fb1 | -8.9164 | -61.4958 | 2026-09-23 02:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 793314d7-9814-37c0-bccd-cc2158139cbb | -6.1109 | -57.684 | 2026-09-23 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 6e0eec0f-8ca1-35f5-b5a0-e96375c138fd | -9.0839 | -61.4308 | 2026-09-23 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 1c2e2d0a-9e69-39f2-939b-9e0e6e90dd5a | -6.6515 | -59.9258 | 2026-09-23 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 68f65e05-6489-3102-956f-9c358cf84292 | -11.8871 | -45.7623 | 2026-09-23 02:00:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 89d64f3b-55a9-359c-bab5-bb0a7594adb9 | -3.6946 | -60.5835 | 2026-09-23 02:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 1621edbd-982e-3cdf-92bb-0c57a5ee4d52 | -11.5311 | -45.3323 | 2026-09-23 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 369a4768-a4a2-3b4a-8f27-8d1fb442d710 | -8.2616 | -54.7776 | 2026-09-23 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 5e144c81-b3c5-3519-ab0b-81986758278d | -6.6146 | -59.9272 | 2026-09-23 02:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 219.1 |
| 46e90e22-05bb-3a5f-84cd-d839457a815d | -6.6145 | -59.9464 | 2026-09-23 02:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| a6eff2b3-628b-3b42-9d4a-cc99903210d9 | -6.6331 | -59.9265 | 2026-09-23 02:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 173.6 |
| a2d6c424-f27a-3161-8ec0-e8d4c34de9bd | -8.9165 | -61.4767 | 2026-09-23 02:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 6e112d92-d43c-3dea-93cb-9c56c95506f5 | -5.7567 | -45.1067 | 2026-09-23 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| e9e3be3e-0d94-3eb2-a801-ae07397e088f | -3.6947 | -60.5645 | 2026-09-23 02:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 4f473242-7c93-3964-9699-38f62c9fe322 | -6.0925 | -57.6847 | 2026-09-23 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 38386a71-78e7-3290-9a54-a6cfefdd522a | -7.8811 | -61.1779 | 2026-09-23 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 4a4df36d-bd36-39d0-8d3b-1462d3ac7f2a | -11.8867 | -45.7852 | 2026-09-23 02:00:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 57.0 |
| ee9c2c34-bbfb-37ac-a39c-739550624a5a | -3.2313 | -46.9596 | 2026-09-23 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 03496ab2-ba26-317e-b513-5b0a66906b6a | -12.1192 | -45.6368 | 2026-09-23 02:00:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 2604b086-dd0b-36be-af41-51b4d2c06e9c | -10.2604 | -50.2196 | 2026-09-23 02:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 4cbfa1f4-5706-3c52-97bf-bdfd18936c13 | -8.8105 | -44.2757 | 2026-09-23 02:00:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 9fda6c37-c65f-3730-8601-aff32cd3f7b5 | -8.4538 | -48.6944 | 2026-09-23 02:00:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 81.6 |
| d559078e-75ea-355c-9654-e57b8f1685f7 | -12.3488 | -50.1563 | 2026-09-23 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 198.6 |
| 16da67d1-912c-3b11-b13f-a07ba306b955 | -9.1025 | -61.4299 | 2026-09-23 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| fbdcc638-16c9-3d06-84d5-3b89b8f03457 | -5.7754 | -45.1053 | 2026-09-23 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| bac424dc-efcf-3d55-a015-735b7d36c2e8 | -14.6302 | -45.6403 | 2026-09-23 02:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 0cfbda94-863c-361c-a4f3-2751804c846b | -6.6148 | -59.908 | 2026-09-23 02:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 84.5 |
| f6240775-a640-3be1-9348-eaab29bf91d9 | -3.2129 | -46.9383 | 2026-09-23 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 0932e683-e441-331a-b913-64979b4d91f8 | -8.935 | -61.495 | 2026-09-23 02:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 52.7 |
| c2f80658-fc61-3f2f-ae2b-28f268e44e00 | -10.294 | -50.536 | 2026-09-23 02:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 917b1cd4-a813-3578-9eba-e37e01f5f6a3 | -4.2951 | -49.1234 | 2026-09-23 02:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| c22679ea-6310-3e7c-ada6-7157302e1082 | -5.6246 | -45.2518 | 2026-09-23 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 906ca317-8234-3577-af1b-a66e71d9ec5c | -11.8867 | -45.7852 | 2026-09-23 02:10:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 72171439-1a80-3c96-a0cb-5307c0b4d219 | -10.3131 | -50.5128 | 2026-09-23 02:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 18fe88a2-40cd-31bf-88d9-1a7bc8d20bfa | -1.9271 | -58.2587 | 2026-09-23 02:10:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 62c915af-573e-3241-9249-039dff836392 | -6.6129 | -43.7317 | 2026-09-23 02:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 7253ce98-d47a-3aa2-a619-952951b0288b | -3.6764 | -60.5649 | 2026-09-23 02:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 54853f1e-0b60-306c-ad20-699d079fd393 | -11.9063 | -45.7595 | 2026-09-23 02:10:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| e64b74f3-4ab9-306e-b929-69f39d675b5a | -8.4538 | -48.6944 | 2026-09-23 02:10:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 91.8 |
| ef61d731-b79d-3162-a366-7705a6289ad6 | -3.8648 | -58.8211 | 2026-09-23 02:10:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| c0ef69ac-a038-3972-87b3-762864f8f01b | -11.4009 | -44.029 | 2026-09-23 02:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 9fb69cf2-2ca7-3484-87c5-54bea9ec63d7 | -6.6146 | -59.9272 | 2026-09-23 02:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 222.2 |
| 765ff4bb-47af-328e-b8b1-c641637002c5 | -8.8297 | -44.2503 | 2026-09-23 02:10:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 52cbe055-83b0-3a5f-ae83-abd7d80b36ab | -9.1024 | -61.4491 | 2026-09-23 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| db11163f-c7e6-3368-8792-ff5627109497 | -8.8108 | -44.2525 | 2026-09-23 02:10:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 91.4 |
| a368e830-d3ae-33dc-8c26-156d38b67eb6 | -6.6315 | -43.7533 | 2026-09-23 02:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| fd11fb55-1400-3b19-a3fd-01dabc340418 | -6.0926 | -57.6652 | 2026-09-23 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 84708ef3-f9a8-3b8d-bf1e-519520471418 | -10.2942 | -50.5147 | 2026-09-23 02:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| d7d56bcd-67ce-3852-9ed8-19d6738b0987 | -12.4212 | -46.9777 | 2026-09-23 02:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 61eb0997-3fc9-35c5-b626-3761aeb45965 | -4.0925 | -62.0874 | 2026-09-23 02:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 4a2d35ab-fdb9-3d7e-b9c4-8dd363691134 | -15.6382 | -43.507 | 2026-09-23 02:10:00 | GOES-19 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 145.7 |
| 8eeac4d3-4edd-3b04-b72f-edce1fe91f70 | -6.6148 | -59.908 | 2026-09-23 02:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 6c59c35c-e719-39c1-8ac5-3437f757f53c | -6.6145 | -59.9464 | 2026-09-23 02:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 60ca0e19-f1c7-3c87-a147-80c2be7c0fe0 | -8.9165 | -61.4767 | 2026-09-23 02:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 50.5 |
| cc2a686d-782f-347a-ac15-e6173be99068 | -3.6946 | -60.5835 | 2026-09-23 02:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| a7d96c29-58d3-3547-9575-0f4715477cd7 | -6.6127 | -43.7549 | 2026-09-23 02:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 80ebd9ed-3b02-38a0-9947-78619b0d4a7b | -8.4985 | -57.6075 | 2026-09-23 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| a5c84ac3-9937-35a3-a89f-f91f236a2ff6 | -8.7916 | -44.2778 | 2026-09-23 02:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 6edf392d-d9a3-3535-9d5a-9095465036ce | -3.6763 | -60.5839 | 2026-09-23 02:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 9ec78f30-1737-3981-9e3b-e38143fa6c2e | -8.2616 | -54.7776 | 2026-09-23 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 73689493-bb66-3495-993e-80edf7277683 | -15.6185 | -43.5111 | 2026-09-23 02:10:00 | GOES-19 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 75.3 |
| df993c7a-5525-3135-8d70-14385b2d16c2 | -3.2314 | -46.9376 | 2026-09-23 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 129.0 |
| 7d1162ac-3afb-31bd-8d12-3fc7fbf2790a | -5.6246 | -45.2518 | 2026-09-23 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 4a007fd1-2d42-33cb-9419-d4105c440d12 | -8.8102 | -44.2988 | 2026-09-23 02:10:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 7d171390-24d6-3ce8-918f-2d1fc717fb40 | -8.8105 | -44.2757 | 2026-09-23 02:10:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 252.5 |
| a263f66f-3817-343d-bb9b-9b5a6329882a | -6.633 | -59.9457 | 2026-09-23 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 704a4009-13d3-3a23-9d35-209a362b17ec | -5.7754 | -45.1053 | 2026-09-23 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| c9eae126-7db2-3d0c-a32e-12268a1fa58e | -8.4726 | -48.6927 | 2026-09-23 02:10:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 24455c20-e753-3146-a331-5d5c37797d0e | -6.1289 | -57.7613 | 2026-09-23 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 3aae5f4b-0a24-362b-bc24-48678b1c1b22 | -6.6331 | -59.9265 | 2026-09-23 02:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 144.8 |
| 05fb35d6-ea4f-3cff-a66d-a64ce5561602 | -3.2313 | -46.9596 | 2026-09-23 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 0bfc816e-0a7e-3d32-9490-3d84fdcff61e | -6.0925 | -57.6847 | 2026-09-23 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| bbecb99e-b9ac-3572-8e1d-ab62a0268e3d | -5.7567 | -45.1067 | 2026-09-23 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 0b93dffd-6846-33a0-84ec-16b7fc039eb9 | -3.2129 | -46.9383 | 2026-09-23 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 4ee8bdd3-4307-35fb-8562-2435c4018d42 | -6.3293 | -43.9411 | 2026-09-23 02:10:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| eafc596f-f9fe-3789-a9e2-7b79de60d32e | -9.1025 | -61.4299 | 2026-09-23 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| a04cb50a-b2cc-3fce-b95b-78abbbc68bc8 | -5.7565 | -45.1293 | 2026-09-23 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| b6533451-070f-32d4-b987-bd7a4536379b | -3.2128 | -46.9602 | 2026-09-23 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 33fe6e79-fdfc-348a-ada7-f7a939a4a2b8 | -12.4216 | -46.9551 | 2026-09-23 02:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 0b4c87af-8f3e-34fa-97c9-c0c4f6879742 | -10.294 | -50.536 | 2026-09-23 02:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 49e0be83-80e8-3f55-a94e-753865ccfb38 | -8.9164 | -61.4958 | 2026-09-23 02:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 51.5 |
| df64c2c7-7bdc-3a46-8010-1543633982f2 | -15.6179 | -43.5353 | 2026-09-23 02:10:00 | GOES-19 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 89.5 |
| ad06954c-3a20-353c-b662-92364738bff4 | -11.8871 | -45.7623 | 2026-09-23 02:10:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 133.8 |
| c6534539-ded7-3e18-87e1-e23ceb1389d2 | -15.6376 | -43.5312 | 2026-09-23 02:10:00 | GOES-19 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 188.7 |


[Clique aqui para ver as próximas entradas](README36.md)
