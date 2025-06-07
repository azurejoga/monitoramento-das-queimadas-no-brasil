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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9865240b-196c-3bac-8b53-b0803c96310e | -6.96211 | -42.90598 | 2025-06-07 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 751bdd48-890f-3276-a5fd-ea788fb10299 | -9.06935 | -47.15085 | 2025-06-07 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1c58f0b8-4723-313d-8af6-e0d633a47ed3 | -5.63929 | -43.71566 | 2025-06-07 04:44:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 979f3afd-be5d-3511-8ef3-fb3958b6ac45 | -10.6314 | -49.43312 | 2025-06-07 04:44:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 54cb2ba6-441f-3a58-8683-917d6503489b | -7.8636 | -47.89861 | 2025-06-07 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18879996-8f9b-3215-8616-0696bf2391b9 | -7.21422 | -43.11342 | 2025-06-07 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f3c5b157-a75b-39f4-a090-21f975be6cc4 | -5.64322 | -43.72124 | 2025-06-07 04:44:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b258920-22e9-3e6c-9ee9-5fad6ec57710 | -6.95792 | -42.8994 | 2025-06-07 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| edc832ea-ce69-3868-9f2b-055ac48c230b | -6.3069 | -48.48663 | 2025-06-07 04:44:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ed12142-4195-34b5-8a73-b1ffa2e51cc4 | -6.9567 | -42.90805 | 2025-06-07 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 2fc432ca-da40-32a2-adf6-f650359e1311 | -10.46245 | -47.94714 | 2025-06-07 04:44:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31bcd8ea-d8d1-3a40-83f3-62ffe98fcf88 | -7.73044 | -44.17039 | 2025-06-07 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| e1256c9c-2214-3005-9598-33c50406e6f9 | -9.39974 | -48.44099 | 2025-06-07 04:44:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6c1bba20-615a-32e0-9a5c-91ccb40b979d | -9.5493 | -47.77366 | 2025-06-07 04:44:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 51af2fe1-4351-32de-877e-9cbe51b74914 | -7.18279 | -42.82593 | 2025-06-07 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d79f0975-5506-3fcd-841e-f62acbf79f69 | -10.46622 | -47.94772 | 2025-06-07 04:44:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fc5b24af-bc1a-34e6-8953-62722c508c94 | -6.94668 | -42.9065 | 2025-06-07 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a9740429-b0da-3b3b-8e34-59996dd8d12d | -7.73977 | -44.17146 | 2025-06-07 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 65930243-61cc-30f4-96a6-fd22c20ca78a | -10.69501 | -57.64322 | 2025-06-07 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bbc37afd-00a7-33a4-9ae5-eb1920243bad | -12.28446 | -50.09655 | 2025-06-07 04:46:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 29e52b05-2a1b-30f1-9ce0-f2bb24cd3e3a | -12.36378 | -54.17321 | 2025-06-07 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ab84d9d-79d8-3e3d-b2aa-ce3b73798ba6 | -11.13732 | -53.94813 | 2025-06-07 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 10dc0ab8-ed4a-3807-859e-22448eafc4b0 | -12.87813 | -52.2009 | 2025-06-07 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d7c6feb-5c8d-334a-adf7-76007df4722a | -11.37349 | -56.55103 | 2025-06-07 04:46:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b94ed808-a347-3da3-b00c-c93d4c8b273e | -10.67628 | -57.62766 | 2025-06-07 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbbb9225-a044-3033-9f80-95029d777d76 | -12.77699 | -48.71877 | 2025-06-07 04:46:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2d22335f-efc6-34c4-a44d-3fb60d4c858a | -14.74594 | -45.09546 | 2025-06-07 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7080f3b-f645-3ded-b6b8-43e99c546fe0 | -13.06714 | -49.24564 | 2025-06-07 04:46:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e5cbc29-01ef-3b44-8003-49408516294f | -12.53495 | -45.41844 | 2025-06-07 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f3b4a16d-1924-36d4-989c-df59f94d5425 | -11.56935 | -54.56379 | 2025-06-07 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19472fd0-ede6-3a5c-85d7-cad10e242f3a | -14.23261 | -45.49291 | 2025-06-07 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 224187d1-8426-3f79-8636-4f4c87dcea5e | -12.27854 | -49.52831 | 2025-06-07 04:46:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ddb1ed11-a35d-303a-8267-53a1ea07fca5 | -13.29035 | -57.93806 | 2025-06-07 04:46:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f647bdc-28e7-3ef2-9616-530a8e086303 | -12.33223 | -52.47723 | 2025-06-07 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07790fe7-6392-36b1-b286-ce206f0e6a9a | -12.2908 | -50.10149 | 2025-06-07 04:46:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2b33b68f-d5fd-3df1-89d0-de6c3d519761 | -17.26539 | -42.65505 | 2025-06-07 04:46:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4cf82bc4-b7e0-3d99-b3a1-fd8ac6fd07d3 | -12.95935 | -46.76397 | 2025-06-07 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cbd8b724-a24d-315d-a35a-eb7c856e3a19 | -10.2953 | -57.13721 | 2025-06-07 04:46:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 82a6e940-d815-3bf9-b509-c8f028bda7bf | -18.95556 | -45.37994 | 2025-06-07 04:46:00 | NOAA-20 | PAINEIRAS | MINAS GERAIS | Brasil | 3146404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3aa62ec-5f2d-384b-a50b-714dc37b9197 | -12.47393 | -46.33891 | 2025-06-07 04:46:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7959e65f-4880-3fb5-b149-6e9fd0eaf0ea | -13.29915 | -57.93585 | 2025-06-07 04:46:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2fe1f324-c69b-314f-9c45-9832be44ee20 | -11.2605 | -60.79517 | 2025-06-07 04:46:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 033d2d10-94fb-3ddf-aef0-35ec261a7b75 | -13.46483 | -56.8554 | 2025-06-07 04:46:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 6acf79c2-ffb1-33ab-9618-e08bfe33b5c9 | -11.77066 | -47.3945 | 2025-06-07 04:46:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96175528-23ba-3811-8956-0d3bb56e40d7 | -12.87482 | -52.20103 | 2025-06-07 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b977e0f4-a14c-36d5-ba15-80187b9b53bf | -12.88807 | -52.20251 | 2025-06-07 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f18ffd88-8bad-3db1-8f7b-2eeb9d5c5382 | -14.0315 | -55.12844 | 2025-06-07 04:46:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0664d264-5b9f-35e3-85c6-5e6aca2c5f29 | -14.73635 | -45.08477 | 2025-06-07 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ddb1319-ac35-3303-902a-643b124431ff | -12.2714 | -44.60835 | 2025-06-07 04:46:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6601a129-168e-3d1b-84d4-cf6e40333087 | -10.29998 | -57.1343 | 2025-06-07 04:46:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| abc19c65-037e-30ff-9913-970c5dfef39e | -14.7412 | -45.08526 | 2025-06-07 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8df65f84-65e7-308e-8779-9fe53aada106 | -11.78656 | -47.39671 | 2025-06-07 04:46:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a85718f2-413d-372a-83e6-1b7ad33b47ee | -10.6756 | -57.63151 | 2025-06-07 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39cda258-8c75-3fd6-abc2-f810adf7336f | -14.87934 | -48.11287 | 2025-06-07 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| af24f145-f6ba-30ce-a378-7a1f78d3c9fe | -10.87632 | -54.29984 | 2025-06-07 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6dfc5234-e382-3ff6-85aa-19d6ddbb460a | -10.87851 | -54.30814 | 2025-06-07 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c1872e7-6046-3ac4-a974-76cb154a564e | -11.83915 | -60.92202 | 2025-06-07 04:46:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0568654c-7c50-3fa7-b15a-1fbbde12dd96 | -9.41908 | -63.33402 | 2025-06-07 04:46:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| acb667c4-a309-31ef-bc5e-365a863fbe7b | -11.90451 | -63.3264 | 2025-06-07 04:46:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d272b735-fc1c-3e3e-9a46-6f6f1a9bcc78 | -13.71929 | -58.67673 | 2025-06-07 04:46:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b259eaef-e10c-3883-a8c0-6a6005c0e7ab | -13.09278 | -52.28296 | 2025-06-07 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 883209c0-225d-352f-96a7-83fb7f6e3da1 | -12.28792 | -50.09708 | 2025-06-07 04:46:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c0c8707c-a6c8-3cc7-83a4-72c03ac69c14 | -14.20336 | -45.49913 | 2025-06-07 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12e71dee-e443-3810-ad80-6bdcdac1105d | -11.77717 | -47.40597 | 2025-06-07 04:46:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c99d1b0-0024-3ec6-b8b1-b888fa78d4cf | -11.56523 | -54.56709 | 2025-06-07 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1249e6e2-f46b-3bef-a8f8-8e7eb09d3f03 | -11.14221 | -53.91817 | 2025-06-07 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb4ee16f-0168-3127-bce9-607906fd675b | -17.07946 | -50.63438 | 2025-06-07 04:46:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cfa92e91-bbbe-3028-ba25-0fd13b2ac84b | -11.13793 | -53.94439 | 2025-06-07 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 91a262bc-d5c9-3aee-9486-f1dfea96fcf8 | -10.87915 | -54.30428 | 2025-06-07 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be35b50b-1651-3ca9-860e-f24ec24f400a | -10.33455 | -57.48973 | 2025-06-07 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18bb3c1f-5275-38ed-b07f-48c9b4caee05 | -14.73695 | -45.08902 | 2025-06-07 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df48cb3e-430d-35c0-85f7-6fa7a3637bce | -12.32673 | -52.46911 | 2025-06-07 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7435feb6-390e-3966-8720-23551c0b564b | -11.1382 | -53.92134 | 2025-06-07 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0439e294-33af-3098-84f3-182c8599f36f | -10.54009 | -56.38528 | 2025-06-07 04:46:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e951e7f4-6f8f-3936-a29b-c3791752309b | -16.36106 | -49.38211 | 2025-06-07 04:46:00 | NOAA-20 | BRAZABRANTES | GOIÁS | Brasil | 5203609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9c283f6-00f4-3570-bdaf-49bc0f459202 | -12.70558 | -58.02547 | 2025-06-07 04:46:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 76f75ba6-90b9-3b58-8a49-00badac01766 | -12.27207 | -44.60308 | 2025-06-07 04:46:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 31ba30d5-7843-30bd-9045-d4c59b2c6c1b | -14.03397 | -55.12424 | 2025-06-07 04:46:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a87f9542-3226-3108-b2ea-8dbd397f644e | -13.34193 | -45.49122 | 2025-06-07 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5146acb0-6fdb-3cf4-a0bc-b7b898084862 | -16.68128 | -43.8852 | 2025-06-07 04:46:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e08929f3-15f3-3cf7-8144-bd81338e31ed | -12.33279 | -52.47371 | 2025-06-07 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3919d999-e128-3c12-b48c-4cacc192a8e0 | -13.37063 | -54.26049 | 2025-06-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba931a40-16b6-3049-af39-99250ed14aa7 | -11.26557 | -60.79626 | 2025-06-07 04:46:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aa90a177-035c-337d-a473-3bb5c1d99b36 | -13.64194 | -52.17945 | 2025-06-07 04:46:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 30551284-77df-360c-ad8f-970c112a6883 | -17.80832 | -51.00908 | 2025-06-07 04:46:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d9c05650-ea33-3fdc-bfd7-908499f65192 | -11.29932 | -54.70592 | 2025-06-07 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59d95922-21f9-3625-abeb-a3bbf5b4ce93 | -11.83348 | -60.92409 | 2025-06-07 04:46:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e114d38e-dedf-3c05-afc4-3848d181221d | -15.16794 | -52.97192 | 2025-06-07 04:46:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35cdf019-3edd-3af7-a91d-fb984080dd24 | -13.06413 | -49.24084 | 2025-06-07 04:46:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f002754d-a029-3808-a4aa-65e551390c6d | -11.89082 | -56.40796 | 2025-06-07 04:46:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64067779-267b-3fd7-be67-478746f5655e | -14.54133 | -53.64406 | 2025-06-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b23c6f9d-3dc5-3f76-ac2c-9a28b4c909b4 | -15.56718 | -47.85595 | 2025-06-07 04:46:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a22f53b-62e9-3cd5-a213-a9ddbf0a085e | -12.2833 | -50.10429 | 2025-06-07 04:46:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0d707447-f921-351d-abf6-1a2049232c90 | -13.0744 | -49.24673 | 2025-06-07 04:46:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ed79a5a-e676-3828-9e80-c0bace5776b3 | -12.38606 | -47.31672 | 2025-06-07 04:46:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 620a1ad4-417d-3273-85c0-a54a35bdc169 | -11.91487 | -54.82174 | 2025-06-07 04:46:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6652477d-9e5d-3c28-9939-50c4f950c09d | -11.1388 | -53.91761 | 2025-06-07 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| be95455f-12df-3818-bb10-d0520b94c766 | -17.25907 | -42.65868 | 2025-06-07 04:46:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6e4d5366-f500-3c4d-9b9b-9c931a7b931c | -14.7418 | -45.08948 | 2025-06-07 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76b76450-b158-3700-bae4-0980dc76e859 | -14.03958 | -55.1333 | 2025-06-07 04:46:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README21.md)
