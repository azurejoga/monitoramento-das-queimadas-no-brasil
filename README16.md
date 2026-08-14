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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 565ac11a-87f7-35bd-bced-881f48a531dd | -14.71529 | -52.89612 | 2026-08-14 04:17:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7f9e9f9c-7852-3f36-806f-4d413d378321 | -15.09701 | -50.43999 | 2026-08-14 04:17:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a45469af-7909-361e-8df3-d773938f7eeb | -16.25312 | -53.70871 | 2026-08-14 04:17:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 18e1c53c-d243-361b-b10b-df2f6f36ccf1 | -16.90986 | -54.14054 | 2026-08-14 04:17:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d52248be-f9b2-389e-a919-a08cf0397ac2 | -14.72361 | -52.88516 | 2026-08-14 04:17:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a36f6333-b9ad-38d2-a011-1a4d1682b668 | -20.26545 | -46.70984 | 2026-08-14 04:17:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 58c1327c-7053-31bf-94fa-c1a47b847981 | -18.49198 | -43.39918 | 2026-08-14 04:17:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 066a8bb7-f899-3bb7-9e7d-3cd7164e0d88 | -14.44757 | -51.86061 | 2026-08-14 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d822eeb9-1211-3ea0-a65b-2ba59cd8142e | -15.16436 | -52.81036 | 2026-08-14 04:17:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c265f4a-a932-388b-861e-1448576d34cb | -13.8146 | -53.81567 | 2026-08-14 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3bddca9d-ec40-332b-84ee-fb4b5a651808 | -20.32018 | -42.0173 | 2026-08-14 04:17:00 | NPP-375D | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| fb4fdf18-a341-35a8-b182-ff22bc6cd462 | -13.93128 | -53.96009 | 2026-08-14 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cfda7b0c-2c66-39b6-a813-fd1c0274102e | -18.16332 | -43.98047 | 2026-08-14 04:17:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3423c0b4-7399-34e6-8fa1-c841762d8995 | -16.90773 | -54.15033 | 2026-08-14 04:17:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 750683a2-4cbf-3978-b85b-e09f015269c9 | -17.12294 | -51.68708 | 2026-08-14 04:17:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 221790d4-0087-30ad-a764-c65ab8520af4 | -19.9521 | -44.70648 | 2026-08-14 04:17:00 | NPP-375D | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cc7bc337-b1ee-3ed1-b46b-9f18ce709bbc | -13.91746 | -53.96322 | 2026-08-14 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cd25778a-ed4a-3636-8a58-1a3582812127 | -14.45381 | -51.85805 | 2026-08-14 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2ed1877c-4c6c-38ea-a8fd-064660e0245e | -20.11955 | -40.2 | 2026-08-14 04:17:00 | NPP-375D | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e8f0a9bb-613f-3b76-9e81-15d1692ec2df | -13.81349 | -53.8209 | 2026-08-14 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41bcc514-185a-3546-88d8-29ac6ed620a9 | -14.06056 | -53.60956 | 2026-08-14 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7325ba7-9da4-36dd-a348-03c4bcd2e3af | -15.63358 | -48.89442 | 2026-08-14 04:17:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5556a0bf-3f67-32e2-a805-38ea7116c50c | -13.88046 | -53.76811 | 2026-08-14 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8afd6ba-5d2b-3cf1-a13a-a0bcc37a7d6b | -15.16009 | -52.80341 | 2026-08-14 04:17:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8468ebab-7bb6-34bc-915d-6a6aa38dd2b0 | -14.0514 | -53.59216 | 2026-08-14 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 81f363b1-a596-3f4a-bd99-94c1e9d6ec3c | -18.41752 | -45.19643 | 2026-08-14 04:17:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 13ad3dfe-d60d-3359-a970-cd388dd15d34 | -16.34324 | -50.45357 | 2026-08-14 04:17:00 | NPP-375D | SANCLERLÂNDIA | GOIÁS | Brasil | 5219001 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 33ec1e11-d0c1-3014-8a3e-83fbee159045 | -21.78022 | -44.04739 | 2026-08-14 04:17:00 | NPP-375D | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| c4b4bcaa-ab18-3eee-8082-c1978832dbdb | -19.95236 | -45.55149 | 2026-08-14 04:17:00 | NPP-375D | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 08cb83bb-68d0-3f70-b162-c72a1fc21f46 | -19.68015 | -45.0583 | 2026-08-14 04:17:00 | NPP-375D | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a9277fd8-cc3a-356f-b52c-866c518330c6 | -20.31562 | -42.22977 | 2026-08-14 04:17:00 | NPP-375D | MATIPÓ | MINAS GERAIS | Brasil | 3140902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e535847d-8517-3203-8b35-55ac05cbef39 | -17.6667 | -44.48344 | 2026-08-14 04:17:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fb350754-06fb-30b0-8c57-395ad91f046f | -18.28987 | -46.08505 | 2026-08-14 04:17:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5b70945c-206a-3e4e-a188-05cb1ac69312 | -19.95652 | -45.54806 | 2026-08-14 04:17:00 | NPP-375D | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6c04952a-e185-328f-ad34-91f60bcf56a1 | -20.26082 | -46.71627 | 2026-08-14 04:17:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95f16fe4-4fc5-3d6e-84d0-df1570b19bf9 | -15.15627 | -50.0552 | 2026-08-14 04:17:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1574d7e7-4b22-35d3-9c37-6a6fb49b76b9 | -15.1649 | -52.80905 | 2026-08-14 04:17:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf037355-6f84-3bcc-9c61-c316816d7e84 | -15.05238 | -52.68649 | 2026-08-14 04:17:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e77768b9-aae7-3717-b2db-b3854a35dfd0 | -19.77554 | -43.65015 | 2026-08-14 04:17:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 06e53e73-801a-39e7-b55c-a84e7220f6ef | -21.81193 | -42.08408 | 2026-08-14 04:17:00 | NPP-375D | SÃO SEBASTIÃO DO ALTO | RIO DE JANEIRO | Brasil | 3305307 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bd03e3b3-0a41-3452-8336-618b59d8218e | -14.05764 | -53.65364 | 2026-08-14 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce1c3c7a-4fce-3392-972d-8e10ebef972e | -15.70161 | -48.31924 | 2026-08-14 04:17:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d77d142-f597-3d31-a552-b0156f640fac | -16.91931 | -54.15528 | 2026-08-14 04:17:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 43a97538-43f3-3f6a-b9da-f6b9d3838939 | -21.40376 | -41.15739 | 2026-08-14 04:17:00 | NPP-375D | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f64b2bba-1101-3d13-a976-0d8ea5d87c11 | -20.89943 | -50.50905 | 2026-08-14 04:17:00 | NPP-375D | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3699d449-f36a-3c78-ba6e-f7fe4d7ccc3f | -20.36226 | -41.49911 | 2026-08-14 04:17:00 | NPP-375D | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| f5cbed0c-84d0-3ca1-aaa6-a72da9861dee | -21.76361 | -44.04433 | 2026-08-14 04:17:00 | NPP-375D | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7274bc32-1855-327d-9cbf-f0ab16059642 | -15.16609 | -50.05619 | 2026-08-14 04:17:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 5d11c403-4b5f-37a2-b6bc-fec716474fa4 | -14.44132 | -51.86322 | 2026-08-14 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 395c48c6-76ba-33d2-831a-13e5344def19 | -15.05326 | -52.68222 | 2026-08-14 04:17:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d0fc031-10ef-39fa-aeb0-9c1d872d31be | -20.26466 | -46.71433 | 2026-08-14 04:17:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0843b058-4c47-3751-a2a6-0b137055788d | -20.89406 | -50.5126 | 2026-08-14 04:17:00 | NPP-375D | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 4689dc00-0712-3bd3-8dd0-2849d8e7257e | -14.05383 | -53.58925 | 2026-08-14 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1be99a8b-e45b-3374-abba-14bf5763c960 | -18.174 | -43.97861 | 2026-08-14 04:17:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75dc655b-64db-36f4-82d8-77b398567da6 | -14.07491 | -53.63293 | 2026-08-14 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77420d5a-a1e3-3183-8f37-ee6dbf33e5cc | -19.94262 | -44.14738 | 2026-08-14 04:17:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b69a29c4-e864-358f-9655-2f5960594300 | -20.26164 | -46.71175 | 2026-08-14 04:17:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35d44ce3-acd8-30b2-a2f8-d424a25ebf5c | -21.78082 | -44.04367 | 2026-08-14 04:17:00 | NPP-375D | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| a9b5d54c-071b-328a-839a-e0ceb610bc48 | -14.30638 | -51.96879 | 2026-08-14 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7276222c-3622-3cce-bf56-301ac0f79a00 | -20.33509 | -46.7409 | 2026-08-14 04:17:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7bf960a0-d05b-3b9e-92a9-f3834ae8e817 | -13.88156 | -53.76303 | 2026-08-14 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 000e6da7-1039-3fdc-8150-dc8cf45b079a | -13.82642 | -53.79062 | 2026-08-14 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52dccb87-ec83-3567-a094-8681c7cbce47 | -19.95928 | -45.5528 | 2026-08-14 04:17:00 | NPP-375D | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd6e661b-df0d-39d6-9919-5b11ae25766d | -14.43507 | -51.86584 | 2026-08-14 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 405a0431-1dcd-3b12-8605-c31b02e73dbe | -18.41541 | -45.18784 | 2026-08-14 04:17:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ae77447-858e-3814-8adf-d5100d45e821 | -17.56741 | -47.50372 | 2026-08-14 04:17:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 556cdd26-a92b-3109-88d4-a00bf2cbb702 | -18.42721 | -45.20255 | 2026-08-14 04:17:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 194abf71-cd07-34fc-a522-daa6eaae4fb4 | -21.59812 | -43.70148 | 2026-08-14 04:17:00 | NPP-375D | BIAS FORTES | MINAS GERAIS | Brasil | 3106804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 6fbe55dd-3c94-3878-ba3e-b64199ed46f1 | -20.44947 | -46.47663 | 2026-08-14 04:17:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9bc2df48-3142-3c3a-b96b-a2784cac2c00 | -18.10759 | -47.92812 | 2026-08-14 04:17:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e14d142b-ae96-30af-ab1e-b05f9be4c200 | -14.0417 | -53.58582 | 2026-08-14 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d2c57593-0a9c-37f6-8746-7408a453f260 | -19.94873 | -44.70582 | 2026-08-14 04:17:00 | NPP-375D | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 85d67874-1688-3682-ae5f-8dc61afbf49f | -15.04765 | -52.6805 | 2026-08-14 04:17:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b7f4b79-cf6c-324f-8d7b-9df20e607974 | -20.26526 | -46.71241 | 2026-08-14 04:17:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8606ef7a-0354-372f-916d-bad3b6a27849 | -18.50542 | -47.0167 | 2026-08-14 04:17:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db348370-efa9-36b5-9547-2284645bd3db | -21.54191 | -45.67798 | 2026-08-14 04:17:00 | NPP-375D | PARAGUAÇU | MINAS GERAIS | Brasil | 3147204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a81bbe73-f58b-30f3-b333-f29e0a3d8816 | -13.93226 | -53.95543 | 2026-08-14 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f024f738-4d25-3957-832c-66bbf3e4e286 | -18.42376 | -45.20181 | 2026-08-14 04:17:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03c32470-cd86-3120-bbe2-3d52f1190d38 | -14.7203 | -52.8954 | 2026-08-14 04:17:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 29f76e0c-24f0-3be0-8cf1-d28a1c4aee74 | -21.27828 | -45.96596 | 2026-08-14 04:17:00 | NPP-375D | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0a1d6ab7-621b-3716-8dfe-a33f089af0a5 | -19.95998 | -45.54873 | 2026-08-14 04:17:00 | NPP-375D | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29bf143d-51e0-3a30-94d5-3c9e23c7149a | -15.12322 | -48.6559 | 2026-08-14 04:17:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dc742a38-d7d8-3cf3-8523-a186218e4dbe | -21.74486 | -44.03323 | 2026-08-14 04:17:00 | NPP-375D | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 4f035be2-d35f-3f66-bf25-06ab194c4532 | -15.15952 | -52.80471 | 2026-08-14 04:17:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6929961d-bb2d-39ee-9a25-dedd4773be6d | -16.60383 | -43.36469 | 2026-08-14 04:17:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5bd716a0-b85c-3eca-86d3-e34ed0571dfe | -16.90054 | -54.15434 | 2026-08-14 04:17:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 416ddedc-3ca2-3a80-96d6-49dcb4e2425d | -13.92492 | -53.95906 | 2026-08-14 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 79330f5d-a5b1-354d-8fde-957bdbd5177f | -19.95306 | -45.5474 | 2026-08-14 04:17:00 | NPP-375D | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 81593d49-2915-36e8-bee0-0ed41798bd91 | -14.07279 | -53.61249 | 2026-08-14 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93880082-b176-3ef0-87bc-c5f84e3f79e6 | -14.43034 | -51.86097 | 2026-08-14 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cadb4270-59e4-36ea-b9d1-80a0332dfadc | -14.0478 | -53.58738 | 2026-08-14 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 61fbd358-0d71-3478-9bb9-62e9d3e72170 | -20.25909 | -46.61848 | 2026-08-14 04:17:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44a91b5c-661a-33f0-a805-0198e2997bd7 | -15.16125 | -50.05532 | 2026-08-14 04:17:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2e79615a-e287-3b92-9d04-073aa1df6c25 | -18.4914 | -43.40281 | 2026-08-14 04:17:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e1880012-73b7-3a46-a6fc-fffd368ff344 | -16.92048 | -54.1515 | 2026-08-14 04:17:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cea08383-a175-3d1d-8f37-710aafd96123 | -19.95582 | -45.55215 | 2026-08-14 04:17:00 | NPP-375D | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 37077c72-528a-3f27-8f0b-467ecb3aef17 | -14.08102 | -53.63446 | 2026-08-14 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| df6e6f81-8385-319a-9f99-43995ca3dde1 | -18.42654 | -45.20649 | 2026-08-14 04:17:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f853dc4-aab5-363b-8bcd-4467d5085be1 | -20.96736 | -47.41336 | 2026-08-14 04:17:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 20d8ea0f-5d28-3bbd-b3ac-92403196e530 | -20.84697 | -45.79453 | 2026-08-14 04:17:00 | NPP-375D | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README17.md)
