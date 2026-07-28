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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 21769106-d1e7-3e41-8610-24877dcbdb5d | -20.62393 | -57.26738 | 2026-07-28 04:53:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 466199d3-917f-3716-a072-943ce016c6e8 | -22.06306 | -56.53273 | 2026-07-28 04:53:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d805efc-2088-3883-b5bc-de5df5a77f4a | -15.24278 | -48.57619 | 2026-07-28 04:53:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 45941a9b-8d80-35ba-974b-d688d848250e | -10.88855 | -50.36835 | 2026-07-28 04:53:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7fb558cb-9e0b-30a2-b8a9-08946c457759 | -12.33149 | -47.16412 | 2026-07-28 04:53:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 28488e89-2ceb-3720-926c-fdfcfb205836 | -9.77719 | -49.19357 | 2026-07-28 04:53:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6abe8d8-5398-3ab6-8863-dd8e0f4d5e2f | -10.94004 | -43.04793 | 2026-07-28 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |
| ec47cace-8403-36b7-bb69-086e91aaf949 | -11.89204 | -43.82946 | 2026-07-28 04:53:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 18961ce8-12e5-3e0f-9501-0d2c27b139fc | -22.06098 | -56.52431 | 2026-07-28 04:53:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 758e9f86-7a8a-3750-976d-ca1a47db5035 | -17.30734 | -42.67191 | 2026-07-28 04:53:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b8959f4c-9e9e-31f9-ab85-4647a7572d3b | -16.5634 | -51.62411 | 2026-07-28 04:53:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f73d6c96-fb8b-39d1-9adb-bc6a1fe3cd24 | -13.29657 | -45.11076 | 2026-07-28 04:53:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 14fde63b-dff5-377f-a90e-4592c8207606 | -10.93471 | -43.04724 | 2026-07-28 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 702d6dad-bbb0-30ef-a45d-0e4a20b3f47f | -13.30137 | -45.11128 | 2026-07-28 04:53:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6c8042a2-741d-3e33-85c3-963747c4b841 | -10.67217 | -49.66239 | 2026-07-28 04:53:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d1a19c82-0b4f-3ab0-9811-d1683d417c66 | -12.49407 | -43.76814 | 2026-07-28 04:53:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 51343538-9544-3752-9191-ab5514808b34 | -14.27552 | -58.9917 | 2026-07-28 04:53:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f3e68fce-5c8b-39fb-9c4c-d459b3561d13 | -9.60813 | -47.76069 | 2026-07-28 04:53:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1a0881e-caf7-34a9-803b-1e6b850160f8 | -10.9392 | -43.05465 | 2026-07-28 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 5ba62110-7dee-3342-a911-91a5a23c1911 | -13.29384 | -45.0941 | 2026-07-28 04:53:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 49a97556-9173-3c16-bb52-02f662c7247c | -10.93878 | -43.05801 | 2026-07-28 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 24cd53b5-ac1a-30a4-b44a-87aa5dd367d3 | -13.30069 | -45.1166 | 2026-07-28 04:53:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bd67ee7e-fba0-3739-abeb-18256f58da8d | -20.55921 | -57.28494 | 2026-07-28 04:53:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b2ba708-ec96-3455-8507-dae22dbc4413 | -20.63305 | -57.34098 | 2026-07-28 04:53:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c559552e-bdef-32ed-831f-bc7cf7d94018 | -13.33792 | -54.30887 | 2026-07-28 04:53:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ef38e6b-5c82-388b-a703-2b2c77e0116d | -13.70449 | -51.9018 | 2026-07-28 04:53:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7737722a-0b7e-3252-a6e4-a2f3d01a7954 | -12.33971 | -48.23104 | 2026-07-28 04:53:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2746e93-d383-340c-8f80-34ee6fdec498 | -17.334 | -43.63029 | 2026-07-28 04:53:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 95806b6e-aa4a-35f0-947b-7264b3e79558 | -13.35505 | -54.28906 | 2026-07-28 04:53:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3460d239-df86-3a89-a289-e3441bf3b970 | -19.06957 | -53.46402 | 2026-07-28 04:53:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c5126b9f-3964-33bf-8e09-60382bd843f8 | -20.61413 | -57.26117 | 2026-07-28 04:53:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 46e4fe8a-e22c-3403-8cf4-a146a7f35ce1 | -13.29246 | -45.10482 | 2026-07-28 04:53:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| d70f60a5-f9de-337c-89cd-4ff7d48ed671 | -13.70504 | -51.89819 | 2026-07-28 04:53:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3785e5cc-c8b6-329e-b580-6a0d16fcfbd0 | -11.78333 | -47.08528 | 2026-07-28 04:53:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0b2a9fc9-0b91-37a4-a087-a278c213cdaa | -11.98828 | -45.55252 | 2026-07-28 04:53:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5c95250-d3f0-3577-9243-5e224e2fd471 | -12.31863 | -54.10089 | 2026-07-28 04:53:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7ebe72f3-4a52-307a-9521-2637ebbca8ee | -13.29795 | -45.10001 | 2026-07-28 04:53:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 781b2432-12a8-3962-83ab-27f4443d551a | -20.60443 | -57.23353 | 2026-07-28 04:53:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c0712ed2-b2ff-31ef-b1cc-4ddba14f23d0 | -8.88467 | -65.01308 | 2026-07-28 04:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4de90334-8b29-3c37-b14d-7c475c4ec898 | -14.41078 | -52.11722 | 2026-07-28 04:53:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c17af72a-8da0-32bb-9143-1ea5f43983ba | -10.74984 | -42.09719 | 2026-07-28 04:53:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f403fdbe-59b5-3856-9904-64e695683718 | -9.92818 | -47.89636 | 2026-07-28 04:53:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3edb8db-67c7-3524-9327-ab477a1d7d7f | -12.45306 | -46.51821 | 2026-07-28 04:53:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bb0476f9-cdb6-3824-ae5a-7ece39d33b61 | -11.97524 | -45.54602 | 2026-07-28 04:53:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9ae05cbe-1bdc-3289-a4c3-cb8dc3f7694f | -20.62321 | -57.27153 | 2026-07-28 04:53:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3a8e244-a9e3-3bce-a3dd-95d386fd60f5 | -15.41046 | -55.92761 | 2026-07-28 04:53:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ec318171-3164-367f-a937-f1a640d5725d | -20.58523 | -57.28143 | 2026-07-28 04:53:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0bcb7538-11b4-32a7-b6ca-fadc12f8a458 | -13.30205 | -45.10597 | 2026-07-28 04:53:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 616bc856-35f7-3f1e-a1b3-1f54a1fd62f1 | -11.83622 | -50.23471 | 2026-07-28 04:53:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dad267bc-8801-3826-acb1-af8d7e577188 | -10.93962 | -43.05129 | 2026-07-28 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |
| c7f4b7e4-ea00-3d89-a714-5089482cb084 | -11.52556 | -47.56707 | 2026-07-28 04:53:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6e0e9f0d-0653-3824-9da4-cbf84fafa187 | -10.37779 | -49.57623 | 2026-07-28 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2a0e5568-d860-34da-bd56-2bb5c4a1edea | -20.58874 | -57.28211 | 2026-07-28 04:53:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 417787e6-fc16-3040-9ca5-65419aff9bf0 | -12.32358 | -46.74355 | 2026-07-28 04:53:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e95c2e6b-0062-353f-a21b-0b75a0156d85 | -10.94108 | -43.05307 | 2026-07-28 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 56c55fd4-9c5b-310e-ad4c-76bf8ecf19f4 | -22.06033 | -56.52819 | 2026-07-28 04:53:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7f8f6334-c3fc-320d-b937-ffd687a8600b | -10.93575 | -43.05239 | 2026-07-28 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 27.0 |
| b9b4ac81-3216-3f3f-baee-390d291ac2c8 | -11.55179 | -50.17335 | 2026-07-28 04:53:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 00256756-2b04-3db1-b26e-02f5f1b17d90 | -11.97981 | -45.54657 | 2026-07-28 04:53:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e2efaffa-1bc1-3ab2-90b8-e4b38f32a3b5 | -15.24205 | -48.57907 | 2026-07-28 04:53:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c689c68f-5153-3ded-9f8e-cb292a0daaed | -9.78072 | -49.19412 | 2026-07-28 04:53:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| eaadda1a-7fd2-3414-b41c-6de784256043 | -10.38537 | -49.57339 | 2026-07-28 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c60e0701-71a2-3aab-8254-2a5cf8e33a36 | -11.65788 | -61.22159 | 2026-07-28 04:53:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a2995d3d-69b5-353f-bf50-acea276fefbc | -11.19868 | -54.04045 | 2026-07-28 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a09f6cb-2de9-3402-b595-e8f86c7f4b41 | -20.61134 | -57.25634 | 2026-07-28 04:53:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 54757908-b732-3d85-b0c1-80f7a12b2465 | -15.81589 | -41.89545 | 2026-07-28 04:53:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c1260c5c-3fc1-3475-b5c2-78cc4786b087 | -14.2252 | -58.98262 | 2026-07-28 04:53:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 253f904d-9247-3f2a-9d75-7cea1cf08d60 | -20.55202 | -57.30518 | 2026-07-28 04:53:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 474b598c-8723-34f7-8c4d-ea620885fc7b | -20.30132 | -46.35473 | 2026-07-28 04:53:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f663d68b-501f-3fcd-a36b-fca1fb953790 | -9.9275 | -47.90101 | 2026-07-28 04:53:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6606ac60-4cf3-36b3-996d-d5a52d061a62 | -8.64075 | -64.9081 | 2026-07-28 04:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7dd9ae4a-007e-338f-b421-0ae4d666e0fd | -10.38129 | -49.57678 | 2026-07-28 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 7e40b6c0-3bcc-36a1-a1ea-29c10381c443 | -20.59649 | -57.27929 | 2026-07-28 04:53:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c694cd72-be87-3309-9c6a-670350641371 | -17.72729 | -48.60399 | 2026-07-28 04:55:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 166f416a-9dc0-3921-89c9-0ed3f84f2095 | -18.374 | -50.67683 | 2026-07-28 04:55:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 9b895186-c61a-3b7c-a96c-ee65a22d2b27 | -18.85987 | -43.45525 | 2026-07-28 04:55:00 | NOAA-20 | ALVORADA DE MINAS | MINAS GERAIS | Brasil | 3102407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ccc8dbc7-dc69-373f-988e-7c48563f7338 | -18.36677 | -50.67572 | 2026-07-28 04:55:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 91a4ecfe-2d47-3f6d-a999-2ebad1eddb52 | -18.37701 | -50.6817 | 2026-07-28 04:55:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 53.7 |
| e203d3a0-f2f0-320f-8fa3-0a2db312f0be | -19.17057 | -42.99593 | 2026-07-28 04:55:00 | NOAA-20 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 90ef76dc-63a9-3edd-9f0d-a49a6b486ada | -17.3985 | -47.33181 | 2026-07-28 04:55:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e74ebef7-d4a6-337c-94aa-7e77aba3e25e | -18.37278 | -50.68544 | 2026-07-28 04:55:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 5480a64a-cd1c-3f3b-95d6-edd23349c6b8 | -27.34673 | -50.73138 | 2026-07-28 04:55:00 | NOAA-20 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d51eecb3-a926-31a1-8385-7abd924da90f | -18.37949 | -50.66411 | 2026-07-28 04:55:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b51a81e2-ab93-3a20-ad82-15fb2be9a4d9 | -18.36977 | -50.6806 | 2026-07-28 04:55:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 1d8ede87-eecb-3034-aa6a-3142f7a00a87 | -18.36862 | -50.66259 | 2026-07-28 04:55:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| e37edba8-bed7-3513-92d6-c3fa9d7e60eb | -18.37762 | -50.67737 | 2026-07-28 04:55:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 9d9862da-6539-3e27-9486-69f91b8f2917 | -18.37587 | -50.6636 | 2026-07-28 04:55:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 956eedbd-a3df-3122-acfb-1ee008e28071 | -18.3764 | -50.68599 | 2026-07-28 04:55:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 4e400849-0e9b-39bc-a568-ec6a65fb5001 | -17.39904 | -47.32751 | 2026-07-28 04:55:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8bc7375b-da98-3863-9bc0-7b1453b1f50e | -18.368 | -50.66699 | 2026-07-28 04:55:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 091e7236-3de8-39c2-873c-6776f61a6c6d | -18.37339 | -50.68116 | 2026-07-28 04:55:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 22.7 |
| c2810dbd-bd32-34e1-afc2-14980ea24065 | -18.85563 | -43.45403 | 2026-07-28 04:55:00 | NOAA-20 | ALVORADA DE MINAS | MINAS GERAIS | Brasil | 3102407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| d4e5410e-5d67-36e5-bede-b067d1a5b997 | -18.91515 | -50.64638 | 2026-07-28 04:55:00 | NOAA-20 | PARANAIGUARA | GOIÁS | Brasil | 5216304 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 13560735-33c9-385e-9e08-06d9209c1044 | -18.37462 | -50.67245 | 2026-07-28 04:55:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 57dc6383-52eb-38ba-8aab-4944b4a5c48c | -17.08867 | -51.73618 | 2026-07-28 04:55:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8872b135-b1b2-3ae7-94ee-0a87f1ea811b | -18.37099 | -50.67193 | 2026-07-28 04:55:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 9742ee46-a7a2-391f-bebf-8216d83a8074 | -23.98011 | -48.52618 | 2026-07-28 04:55:00 | NOAA-20 | CAPÃO BONITO | SÃO PAULO | Brasil | 3510203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| db13c74c-0850-349f-9d6e-9f9ddac8943a | -18.36917 | -50.6849 | 2026-07-28 04:55:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 51092965-ce0a-3b5a-bca6-84ec07e40cad | -17.72397 | -48.60297 | 2026-07-28 04:55:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 49d0a501-84c2-3458-8c8c-aea599db5380 | -18.36924 | -50.65815 | 2026-07-28 04:55:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |


[Clique aqui para ver as próximas entradas](README20.md)
