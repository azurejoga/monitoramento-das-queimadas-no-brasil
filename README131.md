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

## Dados Diários - Página 131

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 41fadcf0-a3c6-364e-8a81-8643dc2bf75a | -7.90408 | -54.71841 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| faee9316-3f05-3db9-a882-398c889b3a6f | -11.38014 | -55.16264 | 2026-10-10 05:06:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fac06a05-ff19-332c-ab6b-c2a166b9dae0 | -7.4608 | -63.64134 | 2026-10-10 05:06:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f61ce84-a6b1-36c3-bd40-af1b4bf9e64d | -13.52074 | -47.42023 | 2026-10-10 05:06:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0da7d7b4-a92b-3a60-9ddd-ee7bf26ac048 | -8.26403 | -54.71959 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac7aea25-474a-3a4f-864c-42d990206c7d | -7.45673 | -63.63387 | 2026-10-10 05:06:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b07c0ef0-c8fe-33e4-b494-9bdd58ca3cec | -8.50247 | -54.60784 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 99bdab63-1b06-3af1-916e-fe0a3155f843 | -13.35661 | -43.90404 | 2026-10-10 05:06:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e09eef4c-2a89-3a7d-813b-9536d946dbf7 | -11.76212 | -43.53421 | 2026-10-10 05:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e0aff20-230f-3823-b5fd-b0ee7c61ac17 | -8.5763 | -53.10878 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8086ddcd-53ba-3ff9-b527-1a81afaf76d6 | -9.27684 | -47.3992 | 2026-10-10 05:06:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c45de2c2-c8cf-3d67-9b42-8b427177fae0 | -8.768 | -49.60556 | 2026-10-10 05:06:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3dee3033-c3ee-37b6-bd13-be002a125f68 | -12.26392 | -44.75984 | 2026-10-10 05:06:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3dcd1972-b28f-39b9-b80e-e70b2f479fff | -10.60999 | -60.48351 | 2026-10-10 05:06:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| dce6aa2f-3702-3692-8003-a5698445c472 | -13.50961 | -48.60882 | 2026-10-10 05:06:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d1d4496e-a68c-3740-ae1c-79974ffcced5 | -8.18575 | -54.72134 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1550e7d2-0b25-3720-9a3f-0fa266c0f69e | -11.83915 | -43.60955 | 2026-10-10 05:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad1fcf38-78f5-31f6-9882-b832c31c0671 | -13.14734 | -54.35389 | 2026-10-10 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad20bf07-8e7d-39d2-8c40-bc69031ac62e | -10.49771 | -51.9429 | 2026-10-10 05:06:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c76cfb56-7a9b-32af-a412-b142ffb16a7b | -12.41382 | -54.36439 | 2026-10-10 05:06:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 567b6fc9-14c1-3a7c-b925-4c03cc149ec4 | -10.24831 | -49.66549 | 2026-10-10 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 07a57465-edd2-3c5d-9e4e-97971aa65031 | -7.91935 | -63.7045 | 2026-10-10 05:06:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7c576d8-ff66-3b20-9fc3-7d3d2c77c15c | -12.15128 | -57.23673 | 2026-10-10 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fa526ce8-028a-30ae-a32b-535cb9b604f7 | -10.52679 | -49.46014 | 2026-10-10 05:06:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ecf57717-c3ee-3a63-9fd0-0335ac8fe0a8 | -11.8547 | -43.54884 | 2026-10-10 05:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60b143e6-07c6-34f7-80da-92d4879897d7 | -7.92116 | -54.71758 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c162499-0b61-37c3-b8a5-fc4de3cc4b4f | -7.95449 | -54.7659 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07082d98-c034-3623-80b4-63ecba215e14 | -9.09268 | -61.04908 | 2026-10-10 05:06:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a08d5638-17b8-3dc9-bc98-ae069a1fc1d7 | -11.98287 | -43.45481 | 2026-10-10 05:06:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9dd48ea6-2950-3fa0-a2bc-efb965648f82 | -9.4476 | -48.92495 | 2026-10-10 05:06:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43d20f67-7c13-3363-bf47-cd0a80233081 | -8.77567 | -49.61044 | 2026-10-10 05:06:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b8137f2-2417-385e-91e5-32195db0f5f9 | -10.0435 | -50.93424 | 2026-10-10 05:06:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 999b281a-8730-3f9f-8c59-a222f5be0fa2 | -9.28645 | -47.40053 | 2026-10-10 05:06:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 3b8f5dda-e3bb-307d-b300-40a94add2c51 | -11.86462 | -48.02641 | 2026-10-10 05:06:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 27f781b1-e59c-3b2f-9ff0-b92e6a595947 | -9.27949 | -47.41576 | 2026-10-10 05:06:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 43d95a7b-89c4-3cad-8a02-a4d1738ad15d | -7.45614 | -63.63711 | 2026-10-10 05:06:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 332c0a06-355c-31cc-8058-e024d5c2e1fd | -8.26252 | -55.68774 | 2026-10-10 05:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab00bf6e-fcfe-3d88-abad-b36602032f30 | -14.45302 | -43.9423 | 2026-10-10 05:06:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fdc98e5d-b6bb-3b67-977d-869fb2599670 | -11.97668 | -57.61309 | 2026-10-10 05:06:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b8755993-1ec6-3ce8-8eac-2c06a90fefd5 | -12.02595 | -43.48448 | 2026-10-10 05:06:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a78dc061-d0a1-3aa0-a139-9007e150d1a7 | -14.45827 | -43.94717 | 2026-10-10 05:06:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3cb82d39-52f3-32b6-b299-ba4e67627241 | -7.90848 | -54.712 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f499fc1-de3a-3a26-819a-9d0c09effb7b | -12.36295 | -46.61042 | 2026-10-10 05:06:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d20b6de-1900-3032-91f4-4c6657f98078 | -8.18299 | -54.71735 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2d1a75cb-eb72-3acf-a89d-05d9fa7889f0 | -11.82826 | -43.59215 | 2026-10-10 05:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d8bb2d36-6e22-3ea9-b92d-dea6f6ab1b21 | -7.5698 | -61.54784 | 2026-10-10 05:06:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f280a7e7-5e88-3a96-918e-572b786e12a8 | -14.53169 | -48.0391 | 2026-10-10 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6bbba968-09d7-3194-b316-7e5eca10b8fe | -9.88139 | -50.51294 | 2026-10-10 05:06:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e5a6557f-8031-35b6-99ed-86425498291a | -9.35296 | -46.57094 | 2026-10-10 05:06:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e80178cb-2d00-31e8-8840-b1b66b82b7b4 | -11.08048 | -44.11797 | 2026-10-10 05:06:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46cf2139-1639-3469-8422-e37962e2a06f | -7.88494 | -63.77527 | 2026-10-10 05:06:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8e126e7-8489-30fb-9903-ba3d37610b67 | -11.60211 | -43.71679 | 2026-10-10 05:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d042f920-3e8b-381f-9da6-4e2158781315 | -8.48869 | -54.6092 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2fd3d5d9-32e3-3fd5-bbf7-19348abec6a5 | -8.98436 | -47.53665 | 2026-10-10 05:06:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e83cfab6-bb7c-300c-81e1-0f786a866280 | -7.90353 | -54.72187 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b67af65-f5b0-3ca1-9de5-6798c1b164aa | -7.91345 | -54.72345 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b142bdac-4f34-3508-98f4-1bd41c6f35b4 | -9.20819 | -57.72789 | 2026-10-10 05:06:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6bd9e30e-69c5-31a6-8268-349da5838a37 | -8.70466 | -62.38488 | 2026-10-10 05:06:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5dc67117-cce1-3df1-8b62-4254b0caa1df | -10.44942 | -47.8499 | 2026-10-10 05:06:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 25771640-98be-3b44-830f-dffca3a566e9 | -11.38345 | -55.16318 | 2026-10-10 05:06:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c19b373c-75d3-3cc8-929b-6e3c9d5142c6 | -8.58763 | -53.10307 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2823e331-f6ca-3181-9e09-9bde9bff3e8d | -9.21897 | -45.66421 | 2026-10-10 05:06:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce6006dd-482c-3cc2-bd76-fe4a6a7d199b | -7.00038 | -59.10014 | 2026-10-10 05:06:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c44c87ad-24c1-33e6-99b0-2bfb599dbf56 | -10.67439 | -54.70309 | 2026-10-10 05:06:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7d471b3-244d-368d-ab9f-d5fd0e9a2635 | -9.85236 | -48.01114 | 2026-10-10 05:06:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fe4d9da7-08b4-3f66-abc0-9ea00c43d27b | -7.92392 | -54.72157 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5f5a928-5ee1-3297-b2c5-f69541a50cf7 | -8.2497 | -54.72442 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d4aa9c7-dc8f-3a20-8d90-82580c7d1342 | -11.72814 | -46.73917 | 2026-10-10 05:06:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5ce65e7-2bc8-3f82-ab3c-9af52846f835 | -12.97716 | -51.55117 | 2026-10-10 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44ca0963-cfa0-3f9b-ab2e-c177edc4cfc1 | -12.06903 | -47.38221 | 2026-10-10 05:06:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 008c088a-7a3d-3f8a-b9f3-51af77fb70c2 | -12.15339 | -55.42762 | 2026-10-10 05:06:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa0a5e74-80e8-303a-b533-d2b15bf7c69a | -8.11328 | -55.32612 | 2026-10-10 05:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d581625b-810a-3011-a009-df5f26fe78f6 | -13.72811 | -49.12294 | 2026-10-10 05:06:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 432236b0-cd2c-3a04-97e3-7e20ec55f877 | -13.15073 | -54.35442 | 2026-10-10 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de39109f-c2d1-3f6a-b160-6e485fc65673 | -11.08757 | -44.11143 | 2026-10-10 05:06:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c99a496a-89d4-3116-a1d9-c76775c3c76a | -13.25522 | -42.25897 | 2026-10-10 05:06:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| aecbfa00-288c-3c57-aa6b-0b5893fc844f | -14.43789 | -43.9626 | 2026-10-10 05:06:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 80a9e627-947a-306b-b442-5518093d1d19 | -7.93275 | -54.73008 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0abffee8-aa72-31ee-9f2c-ae00d0117a5b | -7.45379 | -63.65009 | 2026-10-10 05:06:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b82ee8ce-fe95-336c-8013-255ca9fcb48e | -13.91387 | -47.85099 | 2026-10-10 05:06:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 68a13444-586b-34f8-9650-886aceef1267 | -9.12403 | -45.82091 | 2026-10-10 05:06:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99d117ed-7578-3aa6-8918-8bd3e72f195a | -14.04774 | -47.00594 | 2026-10-10 05:06:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6472ae5-1711-34b8-b1c9-587f78024e3f | -7.92944 | -54.72956 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8fc2611e-eda5-3822-a6aa-a48bc0c233ba | -6.94793 | -59.36732 | 2026-10-10 05:06:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 584110b3-c194-3b33-8a62-d0a324ab0fc5 | -11.05547 | -49.56231 | 2026-10-10 05:06:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b0008c4e-6ab6-368f-a7a8-4e0d7a336f95 | -8.95251 | -47.38006 | 2026-10-10 05:06:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 84ef43ac-1ece-3519-bfbf-964f7a0e1cb6 | -13.77841 | -48.13138 | 2026-10-10 05:06:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 22604b2a-d0c2-39e4-a6cf-7b3c258a02fd | -7.44414 | -63.5546 | 2026-10-10 05:06:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f4581473-06b7-3c23-ab15-f12d9790821a | -13.35424 | -43.9253 | 2026-10-10 05:06:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b88a3b35-382b-37a6-860f-1c04b5b287da | -15.02049 | -46.25402 | 2026-10-10 05:06:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a636976-8a05-339f-a3f9-ceabf031a342 | -11.77689 | -45.48464 | 2026-10-10 05:06:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 35557ae4-3cf2-3bc3-bdc3-1c257bf6a4b4 | -12.22648 | -44.6947 | 2026-10-10 05:06:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2d1b75f5-4ab9-3ecc-844f-b1bc25dcb875 | -11.17646 | -45.31818 | 2026-10-10 05:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 66931c25-72e7-3570-9f96-b16ed16357ae | -14.45777 | -43.95942 | 2026-10-10 05:06:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 05fb3e8b-4910-379b-b50c-fc95e8dd575c | -8.64985 | -54.53534 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e47c9cce-1864-3e4e-8be9-1e7ac157733a | -12.07941 | -47.3807 | 2026-10-10 05:06:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e7fe7149-25b8-33d2-be7a-b874701ed162 | -11.45787 | -59.13266 | 2026-10-10 05:06:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 09fa077a-bbe0-3450-909f-1011e3bec54a | -12.09446 | -57.15178 | 2026-10-10 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76fbe6a8-2786-3ad9-8fe4-741723c83086 | -10.4604 | -47.84026 | 2026-10-10 05:06:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5c01136e-578e-31a3-83db-9f9387d718db | -7.45555 | -63.64035 | 2026-10-10 05:06:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README132.md)
