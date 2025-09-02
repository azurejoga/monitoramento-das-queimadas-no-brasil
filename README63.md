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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e38883e-1bc3-3e49-9911-d6a34023443e | -12.90033 | -56.95203 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b9c2e2bb-cb86-3aad-91b7-7284fc90e7cd | -9.75723 | -54.76699 | 2025-09-02 05:06:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b8f8f5a-9a4e-3b41-a2e4-489f5b335513 | -14.75647 | -48.15625 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37c7b0e8-b02e-3520-8e0f-88b30d0cc5af | -11.31664 | -55.21084 | 2025-09-02 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54c1d962-e7ec-38dc-a660-dfa8f075b619 | -14.58895 | -54.57101 | 2025-09-02 05:06:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 530385b1-32b2-3fc4-817a-ee9057af4d9a | -11.42573 | -55.18478 | 2025-09-02 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1cd670b6-ec63-33c5-a79d-64428b2a3a42 | -9.08884 | -58.89087 | 2025-09-02 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1e68555c-7f5b-31ee-8c1b-8622ac4e8a13 | -12.93404 | -56.99729 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9a2f1d4-61c8-34ef-92cb-3deb25afa0e7 | -12.88355 | -48.17416 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1c540835-7563-3041-965f-b34ebd6bf724 | -13.10227 | -57.11874 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c8149b6-8961-3e82-a7f6-7d9d137139ba | -11.65442 | -52.1875 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 9252e00f-5fbf-3b45-bd31-fbf653893eec | -13.35549 | -51.73749 | 2025-09-02 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e25b7a71-01d8-3fdd-9a46-0bed491428ca | -9.75903 | -46.93052 | 2025-09-02 05:06:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fa32c653-ee77-3373-bcbc-46020b3694e5 | -14.59359 | -48.06445 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 438a44c1-c956-3066-8236-13d727824018 | -14.26667 | -45.25311 | 2025-09-02 05:06:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 982bdc65-94c7-3ff0-b6fb-ccde21b1b6ef | -11.66639 | -52.18936 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d6485c80-fb0e-3f97-99cf-99e48d1a4ef2 | -9.11606 | -61.48752 | 2025-09-02 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af1f0b59-a462-3eeb-b6a2-f9f52d05b3c3 | -10.89872 | -50.8364 | 2025-09-02 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6ea51ff9-b264-3087-8e44-d9d8f558b118 | -15.12243 | -48.18602 | 2025-09-02 05:06:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d85aa94-7ae1-3f83-9606-4eb5cea52099 | -8.75517 | -62.42374 | 2025-09-02 05:06:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5719c1f-75df-3b88-84a7-ab1f104519ff | -13.31946 | -46.8259 | 2025-09-02 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 56dc1c95-2f1f-3be3-b2c8-25e0e81ea923 | -11.66385 | -52.17825 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5e47d97e-ee25-3c85-b32f-573b931b4deb | -7.59854 | -61.63016 | 2025-09-02 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1098583-097a-3136-bf09-d4d6305fe5db | -14.3977 | -52.07022 | 2025-09-02 05:06:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 72a0a5a1-390f-35ae-b6d0-36bc240f785e | -12.6198 | -48.18615 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f17c2c2e-fd6d-3e89-a930-cfdec58f389c | -11.65734 | -52.16644 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 318da0f7-3d6c-37a7-ba4a-6187f122cf27 | -11.68293 | -52.21667 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 97088cc2-6b82-350a-81cb-3ff37b101733 | -7.67745 | -61.08425 | 2025-09-02 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7922710c-7447-3f42-93cf-8ed9880b6aa9 | -10.06444 | -48.09538 | 2025-09-02 05:06:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3220e05b-160c-369f-a550-effa1770fb76 | -7.5461 | -61.34299 | 2025-09-02 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e4ded0a8-f809-3795-b2f0-14baf816f577 | -14.27317 | -45.25408 | 2025-09-02 05:06:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5fbf7103-85b7-3d7e-9167-21ff51b273d6 | -12.87691 | -48.0523 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| db255f92-fbb7-3ea5-9efd-280cc4b7b0aa | -12.64908 | -48.25383 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1ed8e123-1739-3735-8b9d-f5937189a040 | -12.81122 | -48.05453 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d300e89c-c445-36e5-958b-391d557ef000 | -9.32985 | -56.27364 | 2025-09-02 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b23a6ddf-d56e-358e-bb47-80518ad15653 | -12.58168 | -44.80555 | 2025-09-02 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f7ea3abe-c8d4-3aca-892f-1a6c00dc9e85 | -14.58723 | -48.0658 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6b45d69f-4616-3039-a3b5-2ac0f54eabe8 | -14.27234 | -45.25904 | 2025-09-02 05:06:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| aa184c57-7d16-3e47-b409-61adff3c3fa6 | -10.82946 | -47.4476 | 2025-09-02 05:06:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f14fa4a-f517-38c6-bbc9-3154cc7806fd | -12.92515 | -56.94516 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2d2a96c7-4d05-3f53-84d4-4a0007ed25dd | -11.09708 | -44.6334 | 2025-09-02 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| a77ab7dd-cebf-301f-b54b-2d4d1ae32c1b | -14.60739 | -48.04034 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 00cdda8d-4d7b-34e9-8a8d-8f27f554726d | -9.837 | -48.61569 | 2025-09-02 05:06:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 544e7f6f-64cc-396d-9f0a-1afb41c114e7 | -10.04617 | -48.11507 | 2025-09-02 05:06:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c16c795f-27a2-3b4c-b6b7-d3669b702c43 | -11.65792 | -52.19163 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| acc798c6-640b-323e-b995-08e16eee5ac3 | -11.44156 | -46.8127 | 2025-09-02 05:06:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d728d1f6-258f-3f9b-b678-a2538fa5d27d | -14.81782 | -48.35806 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c390e9f3-9048-3d8f-a67b-f534ff51d0a3 | -12.9208 | -56.99515 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 35129b92-86b7-3574-8a39-ad9fde0d5808 | -12.88799 | -48.1688 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 37bec541-1a7c-37d2-a8cb-56b740aed516 | -14.59645 | -48.03848 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 40339a70-7aee-344c-874c-e0e3a918cbcf | -12.64857 | -48.25324 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d03ad3c2-35ee-332c-9659-fd66fcba846e | -12.93459 | -56.99376 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 04cc851f-a53c-3971-baa0-91ceb907a21d | -14.58259 | -48.05788 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 123fcbdf-8408-3547-9b61-00c1b560afe9 | -11.84062 | -51.52161 | 2025-09-02 05:06:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e3c889c-bc31-362c-8f16-33f4f8e7e842 | -11.65551 | -52.20903 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 3cccc7b9-6f74-33ee-b191-b48f259f7277 | -12.30431 | -56.89231 | 2025-09-02 05:06:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32f7b06c-e34f-301b-b32a-c391ba01da96 | -9.75397 | -46.92595 | 2025-09-02 05:06:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be6b2ccd-f4ec-3d1e-9577-7b3cf9d0fb08 | -10.29478 | -47.52042 | 2025-09-02 05:06:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b07be06-133e-3f9b-ae25-e11a43d45f26 | -7.55131 | -61.33662 | 2025-09-02 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ca18635f-a273-3ad4-995b-8b6e3d396558 | -14.59324 | -48.06768 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0fa37195-41d5-3157-96b0-3cf57c5dbd00 | -14.2664 | -45.25257 | 2025-09-02 05:06:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 96ed7f84-cced-38d7-b083-3a0e0d57a755 | -9.21177 | -59.53212 | 2025-09-02 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 83de578a-7d9f-39a9-9b6b-1a62d3dec76e | -8.75586 | -62.41973 | 2025-09-02 05:06:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 921bbb10-e90d-3b98-9a7d-73a03867b3eb | -12.60621 | -57.00599 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2fa1e6d1-59d6-3c24-95f2-e53e23241bea | -11.97548 | -45.87825 | 2025-09-02 05:06:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3ddc826a-ad27-374f-9b6d-7e01aac3aa5b | -14.76265 | -48.15075 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6c4ded36-cd61-3bcc-a965-4f6737d1101c | -14.31398 | -53.10305 | 2025-09-02 05:06:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3bbaf54f-504f-3902-a306-7c1559765b28 | -8.50124 | -63.91393 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f97ed299-53bf-3abd-867a-d559ada1c4f0 | -13.32415 | -46.83669 | 2025-09-02 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74565a69-718c-3f06-b5bc-48c5538812e2 | -8.50775 | -63.90458 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c664369c-3212-3388-be46-f1f4d2e69165 | -11.05899 | -45.40003 | 2025-09-02 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7835f11d-37ef-3b79-b733-a6715861d628 | -13.31871 | -46.83246 | 2025-09-02 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f66dcce7-6b28-3a9d-afa0-7f4ae6209485 | -10.05091 | -48.11886 | 2025-09-02 05:06:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b52f7e35-3264-3da3-94d9-6cf4d59cf4b4 | -13.34003 | -46.85303 | 2025-09-02 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 114b2c9a-3039-376f-852d-0807a2f44ad7 | -11.97527 | -45.8734 | 2025-09-02 05:06:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 40157181-5084-3257-9294-fab3fc40db48 | -7.66708 | -61.09748 | 2025-09-02 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d02da49f-44bd-3d7e-beec-02471283a8de | -11.90312 | -46.67047 | 2025-09-02 05:06:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 729c2002-287e-3265-9e6e-045ec5a4d287 | -9.46505 | -48.30419 | 2025-09-02 05:06:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1249751-5d43-3004-b14f-eabc35866339 | -12.76588 | -48.08615 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ca577aad-b89e-3cde-8a12-446fb4e12b1f | -10.03776 | -48.05813 | 2025-09-02 05:06:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8bbe9641-29af-36b6-b451-8c6e44697962 | -9.92118 | -51.61957 | 2025-09-02 05:06:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 483f9ada-b72c-3bfb-b94e-893f458a3ec7 | -14.60717 | -48.03842 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1ac7f6cc-8693-3bf5-bc75-4f4a8c733a90 | -11.65901 | -52.21312 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| bc6217e7-36e2-3c70-9fb2-06fea95c4891 | -7.7887 | -61.56677 | 2025-09-02 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 21b3ba64-63c1-369a-8314-7ecd7086c5ac | -12.87149 | -48.05205 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 134620f1-35f7-3c29-beb9-0a5171c7e262 | -11.67529 | -52.15469 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89ac95d9-10e4-3c6a-8aab-4fd9aace1fd3 | -7.69956 | -61.09848 | 2025-09-02 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7c6d2073-b24c-3ec2-8090-fdf8a9850f92 | -10.34281 | -48.14194 | 2025-09-02 05:06:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 471d8e39-5d6b-33d4-aa1a-d0c9560e0a19 | -8.72815 | -62.40268 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 907eb689-59cc-3860-8445-efb2b5811595 | -14.58236 | -54.53955 | 2025-09-02 05:06:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 458ac116-a12d-3c83-8ccb-e3241989af14 | -9.511 | -63.56538 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0cf20cf-31e6-3fc6-af4c-e48096698092 | -12.93289 | -56.96091 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b4b6f27-ad44-3c25-abea-2349a2b79290 | -13.33463 | -46.84857 | 2025-09-02 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48af429f-4231-3fba-9f14-0029252a3c71 | -13.27619 | -46.89377 | 2025-09-02 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd634cfe-689d-367b-a827-6c70f9af9a30 | -9.73966 | -48.96656 | 2025-09-02 05:06:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bead839c-c55e-3498-aac7-41b7f9409e50 | -12.43658 | -48.7193 | 2025-09-02 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8bd58f18-049f-3629-9055-968f5863b11e | -12.92627 | -56.95985 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d160843-ef74-3192-a917-2f05d1dc1c28 | -15.11733 | -48.18211 | 2025-09-02 05:06:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69cfe1a8-7345-3241-af46-aba9b4bba039 | -12.9318 | -56.96798 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2823dcb2-c118-36c6-80ca-fce5e92a94e6 | -14.58178 | -48.06479 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README64.md)
