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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d02156a8-a765-3151-8de7-13f443d22f8d | -12.90908 | -56.99541 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3012a665-7be6-3011-a158-18e06dde1d93 | -14.56355 | -48.06758 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 10d8294d-9c7a-3691-a853-65ac0d0eaf49 | -12.8936 | -56.94981 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 225b207c-ecbc-3d8e-a12b-1aeeb224f9d8 | -15.30176 | -52.74508 | 2025-09-04 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6fb444bb-9775-3794-81c4-e611d6a89cfa | -12.63747 | -56.99157 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56123e4c-aac2-3016-896b-10bdc243088e | -12.91883 | -57.00591 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 64f86df3-43bf-315c-aa4e-bde610e5cab1 | -14.39303 | -51.6711 | 2025-09-04 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 01f289c8-033f-37b4-addb-96e9e6b258f9 | -13.85708 | -47.98209 | 2025-09-04 05:18:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 22123b16-3d81-3791-9e20-f189fc875072 | -14.55866 | -48.07517 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 88e7e103-5d22-3c54-a398-261ca25c3d27 | -10.25136 | -61.77885 | 2025-09-04 05:18:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dbeef20f-0838-342b-962d-d876ba2738a7 | -12.89424 | -56.94542 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5cad25c1-d1fd-3c91-8983-f29ada9cbf16 | -11.19854 | -55.01548 | 2025-09-04 05:18:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7914c550-5048-3342-bf57-368dc211528b | -15.78317 | -48.19758 | 2025-09-04 05:18:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 44322e63-ce34-39fb-b968-7e626a6b4716 | -11.61533 | -47.78253 | 2025-09-04 05:18:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 61d1e1b7-6931-3036-87b0-e4010d357125 | -11.63999 | -52.18808 | 2025-09-04 05:18:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78dbb692-aecd-381d-a0d9-3228247a3385 | -15.41229 | -55.94069 | 2025-09-04 05:18:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c3e46d66-5ca7-3227-bb8e-2b1b077def03 | -12.49895 | -53.8443 | 2025-09-04 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1752120a-9bb0-3cf1-8ff5-5e4688718884 | -14.77526 | -48.14164 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fc99000a-2f1d-3429-8ba4-a2e069f7f39d | -15.00211 | -50.03928 | 2025-09-04 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 316514ee-1be2-32a5-b1a9-4490d723aaef | -14.90395 | -49.62825 | 2025-09-04 05:18:00 | NOAA-20 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aed2ada4-4eac-333f-a17d-b86664b25cc7 | -14.55869 | -48.04905 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2a99cbb9-0e34-34c8-a273-297f797f861b | -12.63256 | -56.99974 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa2519d9-aaf3-3a83-9115-bf1b6d95a098 | -15.59875 | -52.89428 | 2025-09-04 05:18:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 47e093f4-2315-32da-94fa-a836d38a47a8 | -12.48374 | -53.83008 | 2025-09-04 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f140b45-afaa-35a6-a1b6-73cb23321ce2 | -12.18338 | -53.89478 | 2025-09-04 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 230f10cd-e060-3702-88e3-9dc38467e3ea | -10.06461 | -58.39502 | 2025-09-04 05:18:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e9677fd-f134-399b-a8e6-9a418241d254 | -12.95328 | -48.07042 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0b876d53-517f-3cae-a64c-e1787beda80b | -14.78719 | -48.13244 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 74b46172-dc0b-341a-9f55-3a3a78dcabdd | -11.6558 | -54.52325 | 2025-09-04 05:18:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 64b9a311-e26a-35cd-b61e-1025bb204375 | -14.29478 | -53.09108 | 2025-09-04 05:18:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b383742-a724-3a5a-b283-83dda0d93e38 | -12.64655 | -57.0062 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3fe4ed50-6fde-3f45-a02c-d742c0592e4c | -12.48697 | -53.83953 | 2025-09-04 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7e00523-bfe5-3880-9326-6da9db18669a | -13.74798 | -46.94316 | 2025-09-04 05:18:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8225ab9a-6502-3b5a-987e-2fb1b1031d9a | -13.73549 | -46.92599 | 2025-09-04 05:18:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 83b64b46-6fbc-3ed4-ade9-8e8f692f7663 | -12.90718 | -56.93396 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e66cf922-d629-3576-a004-56d6795f8fb1 | -11.19452 | -55.01486 | 2025-09-04 05:18:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 414cdf5b-caf1-3fcf-952f-9b6b07d1aa20 | -11.95319 | -51.34441 | 2025-09-04 05:18:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 14c7127b-9748-3d9e-8c4f-64b805f527c8 | -11.67168 | -57.35186 | 2025-09-04 05:18:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e928704-c438-3ee9-bafb-c895902e0c5f | -13.10402 | -57.11958 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da70fcf6-a5be-3661-9ed3-90b7cc55539d | -12.91274 | -56.99599 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a76801f-7907-3b54-a3a3-a0996d9d5efd | -11.65526 | -54.52719 | 2025-09-04 05:18:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8e1518df-714f-340f-b13a-a877d0a9baf7 | -11.84925 | -51.4544 | 2025-09-04 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5052c497-79f3-367c-9f40-99b3d1c344d7 | -14.20729 | -48.09464 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 04f90ec1-a34c-3c31-9551-d6004d63086d | -12.49451 | -53.84365 | 2025-09-04 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f84fc875-dcc7-3c08-aec7-7672d323119f | -12.96521 | -54.77324 | 2025-09-04 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0f369748-6551-3ca0-8ba5-ff24945e6571 | -10.87984 | -55.73641 | 2025-09-04 05:18:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18cb9385-f1d2-374f-9e2f-0e4467f0b01f | -13.08482 | -57.12258 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2333ce4-3189-3cd7-a711-ca378c1f3ad0 | -14.53735 | -48.06067 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| be43167e-5b18-3755-b05d-6b67183d5e03 | -12.87332 | -48.02315 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8dfa70d4-6fef-3feb-a8ac-64e4f1248f6d | -15.59498 | -52.89552 | 2025-09-04 05:18:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aaa0e62e-1be7-3277-8cf8-722c3b30ae6d | -14.8188 | -48.2154 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 62a42553-669a-306b-a5d2-fa50b5293c2f | -10.06517 | -58.39138 | 2025-09-04 05:18:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51246a52-7231-3ca5-b811-7d583a767976 | -11.53497 | -54.48801 | 2025-09-04 05:18:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04423a88-a71b-3462-b5e0-aad36efd5d6f | -12.64488 | -60.15982 | 2025-09-04 05:18:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74c7becb-8f5a-3eb2-b4e4-e6be99b100a8 | -12.90654 | -56.93836 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e56111a6-e789-302d-8a91-f375c4119cba | -12.49953 | -53.83987 | 2025-09-04 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 252d53a9-616f-3c56-8461-2b4258f9ad61 | -14.58111 | -53.01944 | 2025-09-04 05:18:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5a105975-939f-3999-ad8c-f1b50b4b7c52 | -15.04267 | -50.05225 | 2025-09-04 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 709ce999-cd21-3aa6-9bb4-af373ad85208 | -13.57229 | -48.12769 | 2025-09-04 05:18:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f11c0be4-a976-3de2-9880-f6beb2a6ce71 | -12.90286 | -56.9378 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f789d0c8-4661-391a-83f9-72ca708324b7 | -12.97049 | -54.76589 | 2025-09-04 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3416825b-e5f3-3861-a3db-48461855428f | -12.64479 | -56.9926 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 22a5bd73-51d1-3ea9-ac50-789bc35b4586 | -11.53597 | -54.48764 | 2025-09-04 05:18:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d410bd8-b97b-3182-a8dd-1c35d5d800b0 | -15.02713 | -50.08435 | 2025-09-04 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d862a13-ed8c-31b3-81c9-c11e0d94d8c4 | -15.59564 | -52.88985 | 2025-09-04 05:18:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54fea0b3-4311-38b9-aa3a-e7aef795aeab | -12.89552 | -56.93665 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bf32695c-8120-37a1-bdea-1c71df7450d0 | -13.0891 | -57.11882 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d06d40d-73d8-35e0-bc8a-b8f7cd28f4ba | -11.95261 | -58.73265 | 2025-09-04 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f072c518-9200-3bbb-bacf-fe51c43e4f08 | -13.572 | -48.12374 | 2025-09-04 05:18:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 588307a8-d0f0-347e-aa9e-0210b93d7c6e | -11.65054 | -54.53057 | 2025-09-04 05:18:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0c554ce7-91ca-34d4-8241-b8f6dab34d88 | -14.53792 | -48.05492 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d4597ad8-38ab-308a-9804-f87b5b247cb0 | -12.63861 | -57.00951 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06adf82c-82c4-3035-80d6-76080f4196f0 | -11.20508 | -55.02741 | 2025-09-04 05:18:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff60c3d9-f617-3a23-9b35-d7d7db2b9742 | -14.55655 | -48.0703 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d2576799-c007-3f8d-8ed5-c0ad2e5c361b | -14.29461 | -53.09185 | 2025-09-04 05:18:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d96d0bb-ffb9-3d29-93f9-b79f0c4c5533 | -11.7815 | -47.32631 | 2025-09-04 05:18:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 42c6ef13-da61-3d71-8d62-c53f88b1dffd | -14.55211 | -48.07355 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7f7cdeb6-8b14-34a6-8ede-76734056e25a | -14.57171 | -48.07878 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f9012dd0-a66a-3ad1-9b8d-e15f6a8ae11f | -12.89141 | -48.03188 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b5dfd2f-9a32-3322-b119-7b711aa1cb52 | -15.1419 | -52.33378 | 2025-09-04 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| deec054d-4e87-3300-983a-becfe811d48d | -13.09768 | -57.11119 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dc1233d9-7c30-38b7-8bb3-f57fcb16da61 | -15.00991 | -50.07771 | 2025-09-04 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4d57dbd-46d6-3f3a-873b-381828b43db9 | -13.80894 | -56.57477 | 2025-09-04 05:18:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9798fa8c-d049-3a54-b779-b0d014de5e76 | -14.78052 | -48.13195 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 68c409dc-00f8-3108-b1f1-f87568202d8d | -12.48291 | -53.82845 | 2025-09-04 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f08567c-461b-3d63-a7a7-7cbbf343a7da | -15.01492 | -50.03187 | 2025-09-04 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6c185605-50f0-3993-acda-c04a4e7609d4 | -11.58123 | -52.16152 | 2025-09-04 05:18:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2961dbbd-1648-3a27-a367-0e4423f454f1 | -8.88179 | -69.34529 | 2025-09-04 05:18:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4d27f8f7-78dd-3d57-a68f-2e907a45158f | -13.09704 | -57.11555 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2d86537b-c1c5-364a-9e25-5226393ee8ac | -14.77997 | -48.13745 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ecc771de-ae4e-3583-945e-57923d1b695c | -12.9092 | -56.99692 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19b8db96-5c5f-3583-91a7-42cd8990b5c2 | -11.31965 | -55.22559 | 2025-09-04 05:18:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a471921d-65b9-3c8d-9f24-821e73cfa25e | -15.30374 | -52.77557 | 2025-09-04 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89ab01a9-e9d2-3f3e-b6c2-c9e0112f7e68 | -14.56914 | -48.07865 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a66c8d10-651c-3cc6-a44b-0c888a31c69c | -12.89919 | -56.93723 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| edb672e1-2603-39e9-b5df-2d978cf47834 | -11.88174 | -51.53011 | 2025-09-04 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bcf49574-4ea1-3ae0-8f4f-4d309c3da2c3 | -15.04848 | -50.05394 | 2025-09-04 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 49a80166-b560-3184-8ef8-f1d0a1072f7a | -12.97525 | -54.76247 | 2025-09-04 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6694be02-d1eb-37ee-b2af-d1987f94a88b | -11.63578 | -52.20266 | 2025-09-04 05:18:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79da5cd2-b4a1-3717-a0c5-593cbf6b5d3a | -10.61123 | -55.40621 | 2025-09-04 05:18:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README87.md)
