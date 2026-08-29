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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8c59ff30-f0f6-3e82-8da2-234d9abe7c2e | -6.63103 | -43.74353 | 2026-08-29 04:51:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| e8fd2385-fb7a-3741-a154-670231359e89 | -3.87032 | -48.04673 | 2026-08-29 04:51:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 07057b34-5fbf-3312-9ed5-809ae04db7b7 | -5.98733 | -57.68097 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6cb028dc-accd-35ac-92f3-2940b5ef2674 | -8.6668 | -49.54593 | 2026-08-29 04:53:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 820dab2a-603b-34a4-a152-9c49d591bc93 | -6.18116 | -57.78739 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1fe82822-a02c-33b8-90f1-0e536113472f | -10.56757 | -59.61033 | 2026-08-29 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 624c08c9-b50f-390d-8eba-f2d60c9c3ce3 | -6.153 | -57.80421 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 96551df0-e088-3c1a-85c9-f8a1433dee73 | -7.21109 | -42.76129 | 2026-08-29 04:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5a8bab3a-0eb3-3cde-a0d5-497ff90a9833 | -8.53716 | -55.26818 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3c29eec7-9164-389d-a66f-7abe3d4969bf | -6.75729 | -55.65872 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c142af85-bd03-3e7e-a0cd-31dcf7a45235 | -7.57292 | -61.38605 | 2026-08-29 04:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 42ae4279-c7a2-3bfc-b79f-8d211e1f97f2 | -11.48476 | -45.0661 | 2026-08-29 04:53:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 042febe4-6c52-3027-b6ad-3cad046199a4 | -11.25992 | -54.01633 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e774bda-7cfb-3139-bda1-75bfc60fe8c2 | -6.74933 | -52.45274 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d483c576-3824-373d-bb76-c88d82cfe209 | -8.79765 | -49.9921 | 2026-08-29 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 629be114-d1af-3c69-ac1a-2e2661517afe | -8.04394 | -54.00719 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 62640c31-3ac0-373a-9437-291e348e0553 | -11.0427 | -57.21408 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 667aaf31-a15d-3542-afc5-88bffddc10c2 | -10.06125 | -48.68478 | 2026-08-29 04:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ab2d710a-6eed-309c-81e0-1bb41664556c | -12.79499 | -46.455 | 2026-08-29 04:53:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 08642785-3b73-3cdd-b1a8-8411bb02c2c2 | -9.25672 | -57.07201 | 2026-08-29 04:53:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ccebf0a3-c813-31d8-a5d7-6a509f116926 | -6.12183 | -57.68925 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9c15a5b-a012-3cda-91b9-fc4c57b1e979 | -11.71851 | -54.53093 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c87858c-31d1-352c-b457-35465fb776fc | -6.16776 | -57.78507 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8925b44d-0a8a-3b1e-ad64-1ba67b0e2891 | -6.91471 | -59.48514 | 2026-08-29 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f5b52c18-8535-316a-8f0b-1b14054496f0 | -11.23501 | -53.99319 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86dccdf4-23fb-38a4-8839-cc71f1a43019 | -9.13337 | -61.01133 | 2026-08-29 04:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ec2aa55-11e8-3a7d-84fc-55ce1a99e80b | -9.91289 | -60.43015 | 2026-08-29 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 038a596c-41fc-34ec-86f2-0da616ac0bc4 | -11.24179 | -53.99436 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62b7a202-cc18-34f8-9974-3b624666cd8e | -11.03518 | -57.23338 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf5d492f-ac1c-3e1f-9e21-e9e6cbcca9bf | -8.24203 | -54.96529 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e280276-2f5c-39b5-80c4-1b802e4c61bc | -11.27045 | -54.03709 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5cdf40ac-9cfe-310b-8dee-c83039f2410b | -8.58928 | -54.79185 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| becddff9-6072-310e-a546-df89acd42573 | -11.2815 | -54.01229 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02f9e7e0-5aff-3135-a72d-bcead0977945 | -6.78351 | -55.66776 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 316da79a-c54a-3cce-870c-ced2f98130cb | -8.8207 | -49.63484 | 2026-08-29 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0754106-a93b-3169-9778-4c150c47b085 | -12.19067 | -50.55538 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c33800ee-593e-3378-a78a-29df2926a3dd | -9.15363 | -49.97729 | 2026-08-29 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| baa696fd-ad0d-3514-9de3-15f8631b6590 | -11.03596 | -57.22896 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5f83157e-97ef-3ada-aa0c-6577c85d73f8 | -8.94201 | -63.27686 | 2026-08-29 04:53:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 237bcfab-7ae9-3282-9f88-a7e98ad4ed07 | -9.01891 | -57.54 | 2026-08-29 04:53:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fdf55aa0-4e4a-39ce-be26-ad1e0eb3cf17 | -6.82317 | -59.95026 | 2026-08-29 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ee845a70-549a-39b8-8ff3-976b4852a169 | -11.36065 | -45.15461 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 40db6b31-8330-35ea-9da5-a63af327dbbf | -10.4801 | -64.50057 | 2026-08-29 04:53:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 36d477d9-53b3-34f5-b1d3-a2f8e4ba5f00 | -9.31549 | -47.62809 | 2026-08-29 04:53:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b18e45f-cbb0-326a-8fb5-53d3b7052757 | -6.94543 | -52.79981 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11dd7dc6-a40e-3945-9c61-46f7cd35bc0f | -5.84795 | -57.75473 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 23673ca4-03e9-3e8d-b73e-7dc7d7f15f64 | -11.02586 | -57.21653 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23d1034c-749e-3d6b-9024-480b53a18f99 | -6.27673 | -53.13996 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c499dfc2-17ce-35f6-b4c1-df5a798def83 | -11.251 | -45.06568 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bfa41b76-f8f1-3a59-82a7-329bbe1564a5 | -8.77041 | -50.07854 | 2026-08-29 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2615ac06-006a-3151-9f98-ef1d7def20b0 | -10.31842 | -49.98117 | 2026-08-29 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b729f0c1-a037-38fa-9022-d9d9e08c0d30 | -7.34794 | -55.16351 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 03215c17-089e-3264-8332-c85a109ea064 | -8.95378 | -63.28315 | 2026-08-29 04:53:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb422720-fb4a-3dcb-89e8-feb1c5eeea28 | -10.40695 | -61.19666 | 2026-08-29 04:53:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2e61d99-c9bf-3930-943f-0ef9eb326573 | -9.93683 | -60.44093 | 2026-08-29 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d64f4e4-e19c-3f87-85fd-1f724590213e | -16.723 | -49.33809 | 2026-08-29 04:53:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da0a07ee-a147-3ba5-b967-8bfa5e8a77f7 | -6.77114 | -55.67066 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1e19fb65-43ed-3576-af56-09df667ecf6c | -9.4276 | -51.69971 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 00066f73-a8fe-354d-9ba6-c964199e7f84 | -11.26304 | -54.0397 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc1d0e54-ff07-3d42-9cae-d1cb082902fb | -6.24806 | -55.43333 | 2026-08-29 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a079f202-8166-370a-8a87-32216ff2785c | -9.15478 | -49.96983 | 2026-08-29 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11eb06e6-67d9-3018-a5d2-6dad05c5cadf | -5.93836 | -57.73807 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e1ebe58f-aa4f-3658-bd10-d6670b6c0fd2 | -8.79802 | -50.49216 | 2026-08-29 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ec4573af-d42b-3d3f-ba6f-e71ab5f49c8a | -11.48004 | -45.06569 | 2026-08-29 04:53:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf7cef2e-f2d7-3052-9a8f-714cf6c44a5a | -11.24427 | -45.08019 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 892a4238-5a65-3cfc-8411-bb06c25d597c | -15.56514 | -56.28357 | 2026-08-29 04:53:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9b81ccdd-63eb-3db0-99bc-1ca5bf98f255 | -7.5871 | -61.33862 | 2026-08-29 04:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2da3cef-bc13-3b83-8986-6374b74b6eee | -8.58093 | -54.8201 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 429ef760-49fb-394e-9f41-44e6699bd308 | -11.24518 | -53.99495 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 01321243-1643-3edd-ad43-a1966ad467f2 | -11.03114 | -57.22203 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| eb6f1119-4088-3123-a1b3-d011761c927d | -9.22983 | -51.57557 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6a596fc-e6a0-363a-9965-da150badc279 | -10.28285 | -62.82267 | 2026-08-29 04:53:00 | NOAA-20 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1da24ae3-eb09-32bd-abf7-d39e27a41f27 | -8.67026 | -49.54646 | 2026-08-29 04:53:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 985f4577-426a-37c7-bdf0-a9cedf2c106d | -11.36995 | -45.1418 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 758209da-3b25-3f8b-8548-e991b2be2e2f | -10.46199 | -64.491 | 2026-08-29 04:53:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7cca6cd8-fc78-31a2-ae87-948374e845d4 | -6.16176 | -57.79307 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e8b08de8-26c3-3183-b877-31191edbd5ef | -8.53348 | -55.26756 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a13f2a29-91c7-359b-b14d-e36e7e9378de | -15.56437 | -56.30918 | 2026-08-29 04:53:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a29f48bd-f554-3620-8197-5b4661b8c1cb | -13.6514 | -47.75287 | 2026-08-29 04:53:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d97ee5f2-8e09-3b5b-aa51-23ebff528b48 | -6.22497 | -55.61792 | 2026-08-29 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 29df38bc-f833-3537-9e2a-6e6f47beef73 | -8.95388 | -62.38005 | 2026-08-29 04:53:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ea823c05-5e77-3189-be7b-9207b84fb8be | -9.86451 | -65.03454 | 2026-08-29 04:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2833cf40-6efa-3a90-9526-5dbf5f237e0d | -9.92183 | -60.43789 | 2026-08-29 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6490d0de-cf23-3b2d-a130-8f13f2bca11d | -12.22161 | -50.53686 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84e42453-7628-320e-b64b-df25a8a73bb4 | -6.96697 | -55.70399 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e4bfe345-69b6-3324-878c-cf6d21c08ec0 | -8.58814 | -54.82116 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be835684-a91c-311d-bbd2-f9f011a3eab0 | -7.57231 | -61.3823 | 2026-08-29 04:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 95f55c4d-c107-331e-be56-f1fb49c0c9c3 | -7.51235 | -55.29848 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| c426e297-47d1-3914-902f-c8d5cb193335 | -18.3526 | -54.99306 | 2026-08-29 04:53:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f110e048-756f-30b8-a55c-c4a693be1694 | -11.36343 | -45.15556 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e9a064c1-ec88-35d5-8148-cbf5e075bf23 | -9.23092 | -51.56861 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 55cc486f-f85d-3082-abd5-5e68a0778c97 | -9.15136 | -49.9693 | 2026-08-29 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 453febf0-96c5-3272-82ed-b99e513413da | -7.1239 | -42.77061 | 2026-08-29 04:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f90f41a0-36f1-327d-abe4-8de637854fb4 | -7.61532 | -61.3671 | 2026-08-29 04:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3ce00c9-7600-3c34-a311-5d297117192b | -7.34929 | -55.16671 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 79ad82bf-7c36-347e-aa4c-2091a8a029bb | -8.95032 | -50.80076 | 2026-08-29 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83fd8a2a-f56c-38fc-bda4-b7028e3c7532 | -7.27619 | -49.84458 | 2026-08-29 04:53:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37f1fa24-7851-3126-9647-2ca501036235 | -9.40496 | -51.64965 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b25502f6-4e4d-31ee-a826-a4733029ba14 | -6.82725 | -59.95715 | 2026-08-29 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa023ded-ebfa-39b2-8fdd-b8cb720ad5d4 | -6.94738 | -58.95519 | 2026-08-29 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README44.md)
