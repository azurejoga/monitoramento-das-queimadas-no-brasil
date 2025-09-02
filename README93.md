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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c3740ba-20de-3679-bfc5-60b4626ee469 | -11.56434 | -47.61805 | 2025-09-02 12:36:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 120.3 |
| bc6fdf25-ae21-3511-8b67-a9d204e11885 | -12.85135 | -48.05376 | 2025-09-02 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 38.1 |
| fe6cb4d6-efeb-3545-8bf3-8152013b5da6 | -11.05563 | -52.06422 | 2025-09-02 12:36:00 | TERRA_M-T | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6930f27c-47c1-33de-a7b6-1b0580687827 | -14.82432 | -49.29006 | 2025-09-02 12:36:00 | TERRA_M-T | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2ea2260c-adec-3d9d-bd22-8cf27016eb1b | -13.68868 | -46.93092 | 2025-09-02 12:36:00 | TERRA_M-T | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 70eccee2-b333-3fde-a602-89d3086ac100 | -13.50854 | -51.80104 | 2025-09-02 12:36:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e311a927-3fce-3e7e-9b7b-5b06833b01ba | -14.48045 | -52.99795 | 2025-09-02 12:36:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2da66c1c-5958-3c14-8bed-896be4f35900 | -10.84004 | -47.46129 | 2025-09-02 12:36:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 8b6cd65b-156a-37db-9fdb-53671e32f579 | -11.81731 | -51.51936 | 2025-09-02 12:36:00 | TERRA_M-T | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 15.0 |
| be5dd07f-2802-395b-9bb9-7312792ffb37 | -11.9521 | -50.62112 | 2025-09-02 12:36:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 59dcb1d1-abaf-3eaa-9ca4-4f64598c1548 | -11.80784 | -51.4471 | 2025-09-02 12:36:00 | TERRA_M-T | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f270d3d0-2039-30fe-ace4-d95fd9736da0 | -11.0002 | -46.83458 | 2025-09-02 12:36:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| f20a60d5-219e-3414-9a9f-4e8e3e259d21 | -15.72431 | -49.03297 | 2025-09-02 12:36:00 | TERRA_M-T | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 42.4 |
| c1e04cd0-4859-31f6-bfb4-47b35c9c505f | -12.17736 | -50.1289 | 2025-09-02 12:36:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 169c9717-6ec5-3499-8721-ba40f00cc148 | -13.31823 | -51.77957 | 2025-09-02 12:36:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 903001b6-406b-35b2-830e-c499127a1fd4 | -13.70194 | -51.94019 | 2025-09-02 12:36:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 949b3df5-2d6a-3a33-99b4-6edb7d121292 | -10.72099 | -49.59737 | 2025-09-02 12:36:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 3585a245-e29e-35d2-9c56-a51cbdd6981c | -10.29336 | -47.51639 | 2025-09-02 12:36:00 | TERRA_M-T | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 0b98a965-0f37-3612-b231-16925b52a552 | -11.9508 | -50.63053 | 2025-09-02 12:36:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 50.7 |
| abdd35d6-31e6-3896-b7a4-058f95a5a4c2 | -11.43581 | -46.8267 | 2025-09-02 12:36:00 | TERRA_M-T | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 97d16357-42ba-3c89-81ee-1f8415dfd40b | -13.71941 | -46.94157 | 2025-09-02 12:36:00 | TERRA_M-T | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 49641eb3-4337-3f86-96bb-43e515c476d6 | -10.24738 | -51.14672 | 2025-09-02 12:36:00 | TERRA_M-T | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| df3cdfb8-9c76-3bb0-ae58-42cefd1e86c9 | -11.09912 | -44.63343 | 2025-09-02 12:36:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 9126ce42-260f-37b5-8986-b51eeba8c3af | -11.80317 | -48.36403 | 2025-09-02 12:36:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b95e3a43-65fd-30ec-bedb-22d3db5b156f | -15.96796 | -52.20296 | 2025-09-02 12:36:00 | TERRA_M-T | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 201f72f9-25f8-3406-8656-6a5a413bccf4 | -11.66278 | -52.20523 | 2025-09-02 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 85355be7-7dc4-3cf0-bb4e-ea914a649c2e | -12.63317 | -57.00134 | 2025-09-02 12:36:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| b579eecb-b1c3-3f4f-a1af-fa8d39ed3aac | -18.03501 | -44.41284 | 2025-09-02 12:36:00 | TERRA_M-T | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 4e904aa9-e7c1-3cf9-856a-5911025bb971 | -16.59562 | -48.97334 | 2025-09-02 12:36:00 | TERRA_M-T | BONFINÓPOLIS | GOIÁS | Brasil | 5203559 | 52 | 33 | nan | nan | nan | Cerrado | 18.2 |
| deaae65f-d05d-3bf1-abbb-f9941846c2b1 | -14.21071 | -51.66279 | 2025-09-02 12:36:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 0662bec8-639f-3a3f-9409-4ba113fd50e2 | -11.99671 | -47.1031 | 2025-09-02 12:36:00 | TERRA_M-T | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 57378f4a-2176-3953-be9f-ce62f6955f74 | -17.85243 | -44.73345 | 2025-09-02 12:36:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 938089fc-4aad-398e-b643-7b4b9bbc1ab4 | -11.85019 | -51.5425 | 2025-09-02 12:36:00 | TERRA_M-T | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 61.3 |
| aa359bd5-65b3-3c09-84b0-9d5e397ec3cd | -12.94072 | -48.07271 | 2025-09-02 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 8a3ce1fe-4cf9-32f6-b509-bacd119c53fd | -11.83385 | -51.46654 | 2025-09-02 12:36:00 | TERRA_M-T | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 2afd8432-9670-3cd5-ad33-f6dad6c5d1ce | -11.43764 | -46.8209 | 2025-09-02 12:36:00 | TERRA_M-T | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 1d4de30f-bd63-317a-b922-652ddee2817d | -14.82281 | -49.30177 | 2025-09-02 12:36:00 | TERRA_M-T | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 157.0 |
| d3d4e3e8-d409-31ac-b092-fcc5f6feebb0 | -11.85159 | -51.4691 | 2025-09-02 12:36:00 | TERRA_M-T | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 8e069e92-1b0b-3c97-8d2a-dd2daea5f2f4 | -14.8075 | -48.2323 | 2025-09-02 12:36:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 8290330b-bf2f-3c63-81b1-e11a4559ca62 | -11.80474 | -48.35188 | 2025-09-02 12:36:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 4c54da56-6da4-3b04-b343-21954d9f8811 | -14.3083 | -53.09982 | 2025-09-02 12:36:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 59462784-60fc-3208-90a0-0e19468e7951 | -11.42439 | -46.82546 | 2025-09-02 12:36:00 | TERRA_M-T | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 25.4 |
| f4c8a546-be33-31d5-aee1-893596367d5d | -18.69915 | -49.91123 | 2025-09-02 12:38:00 | TERRA_M-T | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 6744bf9d-1467-3b56-a617-6c73094c64d6 | -22.70704 | -44.98121 | 2025-09-02 12:38:00 | TERRA_M-T | CACHOEIRA PAULISTA | SÃO PAULO | Brasil | 3508603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 31.1 |
| 01f82003-8e5e-380f-9d16-95b69ef15931 | -18.70221 | -49.88667 | 2025-09-02 12:38:00 | TERRA_M-T | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 29.1 |
| dfe18e06-1611-38b2-9c36-3b117494d933 | -18.78041 | -44.17608 | 2025-09-02 12:38:00 | TERRA_M-T | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 1ac1e16f-aeb5-397f-9238-31f552fc9e37 | -19.12407 | -49.7764 | 2025-09-02 12:38:00 | TERRA_M-T | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 7a6f10d5-c766-3a25-af82-190d67c7e80f | -19.65045 | -46.09874 | 2025-09-02 12:38:00 | TERRA_M-T | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 32.8 |
| d7101500-ef61-3a04-aa5f-f046e57ca876 | -18.56458 | -47.43741 | 2025-09-02 12:38:00 | TERRA_M-T | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 16feb897-61b2-3e1d-8f11-bf21e9dec7ca | -19.64379 | -46.09138 | 2025-09-02 12:38:00 | TERRA_M-T | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 0636e74f-161a-3145-8b4d-eec207ca3d11 | -19.27796 | -46.05837 | 2025-09-02 12:38:00 | TERRA_M-T | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 4a6f3d70-8059-3a8a-b61b-72b8b91e39cc | -18.79086 | -44.18224 | 2025-09-02 12:38:00 | TERRA_M-T | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 19f70c72-30ed-30f3-8d74-e9de4aea309e | -18.70068 | -49.89893 | 2025-09-02 12:38:00 | TERRA_M-T | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 212.7 |
| 5f5b0ce0-563e-3473-8406-70de80594d2f | -19.1257 | -49.76346 | 2025-09-02 12:38:00 | TERRA_M-T | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 18.2 |
| b7ab2590-7ac4-33f0-ac34-01b4f42bcaa8 | -18.83958 | -47.03873 | 2025-09-02 12:38:00 | TERRA_M-T | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 6cea2aed-c749-3a1b-8a10-f75cc9bbbd9c | -20.05394 | -47.81934 | 2025-09-02 12:38:00 | TERRA_M-T | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 651dd259-5255-3134-af66-8bca33c07dcc | -20.06604 | -47.82046 | 2025-09-02 12:38:00 | TERRA_M-T | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 148.5 |
| ab00e95d-ad66-35c3-b420-78d1694380ab | -19.12264 | -49.76901 | 2025-09-02 12:38:00 | TERRA_M-T | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 6892c460-a811-3fad-8e66-03c4ff850926 | -22.19887 | -54.69308 | 2025-09-02 12:38:00 | TERRA_M-T | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 6b2bea31-6f63-3678-af53-0583d381ec03 | -22.95779 | -47.38093 | 2025-09-02 12:38:00 | TERRA_M-T | MONTE MOR | SÃO PAULO | Brasil | 3531803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| 3c58fdb4-72fc-3ace-8348-5845f924335a | -18.55835 | -47.44808 | 2025-09-02 12:38:00 | TERRA_M-T | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| bd0a8952-3cf7-344e-8828-56894024ee15 | -20.06401 | -47.83857 | 2025-09-02 12:38:00 | TERRA_M-T | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 103.3 |
| ffc02533-5aa2-33c1-a89e-83c29b294e44 | -20.07098 | -47.82668 | 2025-09-02 12:38:00 | TERRA_M-T | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 76.6 |
| ad7b87de-b8d5-3b46-9e8a-1cc3ffbe3693 | -10.062 | -48.1197 | 2025-09-02 12:40:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 91339bc4-8bcb-32df-b340-a6d0e6c9d3a4 | -5.9698 | -44.2923 | 2025-09-02 12:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 3b24c36f-80ad-3ca9-b8d2-e5b23ad22c2f | -8.847 | -45.7808 | 2025-09-02 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 56675b19-c670-3d27-9a74-5e4e94660df0 | -4.9124 | -43.187 | 2025-09-02 12:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 70b84ee8-4a5c-3982-a466-02441ef3a2a1 | -8.02 | -44.084 | 2025-09-02 12:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 834d2cf6-6062-3056-8e92-a05853e1a7e9 | -5.9513 | -44.2707 | 2025-09-02 12:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| ec2dbea2-c324-3035-bc8c-a0df7e261182 | -11.853 | -51.453 | 2025-09-02 12:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 82.8 |
| af680143-7561-324e-968c-1da5492b2a76 | -9.7297 | -48.9617 | 2025-09-02 12:40:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| bd7429c5-f1ff-334c-8364-e3c8ae9a5557 | -6.9942 | -43.2308 | 2025-09-02 12:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.1 |
| d56e2615-a52a-3756-8e52-831af1eec7ce | -6.8724 | -45.8554 | 2025-09-02 12:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 8f787168-6072-3c6b-bc94-5b3a18d3591b | -6.9754 | -43.2326 | 2025-09-02 12:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.7 |
| d87664f2-70fb-3404-9daf-5137de5ba046 | -5.8694 | -43.0003 | 2025-09-02 12:40:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 74.4 |
| f9d813ea-a472-3aa0-8a65-428f99b481c1 | -7.9165 | -46.4354 | 2025-09-02 12:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| fe5011c6-4763-398c-92e0-cf7867d0795f | -10.2976 | -47.5201 | 2025-09-02 12:40:00 | GOES-19 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 45986b4f-3965-3c15-8844-2ecc05ee2469 | -11.1033 | -44.6548 | 2025-09-02 12:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 136.8 |
| d2712a32-3d51-3fec-bc64-66085fe64a78 | -8.8638 | -50.5847 | 2025-09-02 12:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 861a1820-d250-310d-9bbb-5277cb91a3e8 | -9.7485 | -48.9598 | 2025-09-02 12:40:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 494dbd8a-662e-38da-8942-2f76561808cc | -5.9511 | -44.2937 | 2025-09-02 12:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 0dcb2fa1-cb7e-359d-8b8c-567ac1e7f0ac | -11.6527 | -52.191 | 2025-09-02 12:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 118.8 |
| c679d8ee-b735-3029-aeee-e3242519a3eb | -11.6717 | -52.189 | 2025-09-02 12:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 136.4 |
| 56589f92-f673-3feb-8125-081801004ce6 | -5.8882 | -42.9988 | 2025-09-02 12:40:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 152.0 |
| 43d47f81-cc5a-3a5e-89e1-78951990a532 | -8.8467 | -45.8034 | 2025-09-02 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 245.1 |
| 56d316ae-7dab-32e0-bfb6-ed93303bdbcd | -10.0623 | -48.0978 | 2025-09-02 12:40:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| b6886336-3457-3f24-84a8-7805f84dbded | -12.8817 | -48.0518 | 2025-09-02 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 182976ea-4216-39d1-865f-087b19f2b204 | -7.9163 | -46.4577 | 2025-09-02 12:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 232.3 |
| f29f3150-84fb-3ca3-a2f6-0d1a17078351 | -11.8527 | -51.4742 | 2025-09-02 12:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 3115d13e-365d-33e9-93f2-f4f8c0c7cad2 | -11.672 | -52.168 | 2025-09-02 12:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| a28e348c-c31c-3c7c-9e28-aa5ba03e87c9 | -7.1089 | -44.7703 | 2025-09-02 12:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 937d05f7-ef14-3fd1-9d58-c9caa38b7afc | -6.8911 | -45.8538 | 2025-09-02 12:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 334.7 |
| 54700f26-a2e8-37a2-958d-02afbf65dd92 | -8.8281 | -45.7828 | 2025-09-02 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 19b8ab9f-7007-318d-af49-b6272ded98d9 | -8.8656 | -45.8014 | 2025-09-02 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 262.6 |
| 8ea3041b-b74a-30da-8824-372893b55d3e | -12.8625 | -48.0545 | 2025-09-02 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| ca5a9c64-2290-3864-916c-02c6b6447737 | -11.1037 | -44.6315 | 2025-09-02 12:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 01cefd07-9061-3ecf-b9f6-a1b70a400dcd | -11.6715 | -52.21 | 2025-09-02 12:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 123.6 |
| 245821e1-ce59-30bc-96b9-a8209d2e4c20 | -11.9415 | -50.6131 | 2025-09-02 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 94b937ef-e41e-3f46-85a6-104d97028a52 | -9.4794 | -46.4994 | 2025-09-02 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| ab22cf14-3edc-3729-b467-b262823860ed | -11.653 | -52.17 | 2025-09-02 12:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 93.9 |


[Clique aqui para ver as próximas entradas](README94.md)
