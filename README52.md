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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1242a089-779d-32ba-99dc-2285b1a68aab | -9.96904 | -51.65781 | 2025-09-05 04:57:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4a06a68e-3662-36a2-9b69-a31c070edb60 | -12.18385 | -53.89411 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62e29085-3569-352b-9862-5c1efa3b7651 | -10.97647 | -45.95789 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 16788f98-6b6e-326a-afa7-bde5ccf5f8ba | -7.00081 | -55.11063 | 2025-09-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d97e9d59-4c12-3ac7-9966-77f4a96f22df | -12.97483 | -54.79592 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05227151-6a33-391e-acc2-48ca896bd9f7 | -12.96574 | -54.77263 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52248793-e84c-370b-9eca-8060122bb476 | -9.42383 | -46.77841 | 2025-09-05 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| afa02e1c-a6b7-309e-9916-23e401cb98ee | -12.52222 | -53.8075 | 2025-09-05 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f8e1e92-ef4b-3e32-b6d9-ccfebf87a6b8 | -12.50517 | -48.0789 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eccb085a-fc86-3641-8f48-95e56d57410c | -6.43372 | -51.8755 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ffb7f12f-c2c1-335e-961f-6d6886939313 | -7.86803 | -56.99549 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f74d6a1d-6354-3fd7-9995-c637af12a3e0 | -6.33348 | -58.17553 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| afeae8d5-a43e-35f2-af6d-4833c0ab7697 | -5.91347 | -57.73414 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4080f491-bbc7-3f1b-95b8-203a57e68a65 | -9.7075 | -48.98868 | 2025-09-05 04:57:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5838be70-c148-3678-b052-966691a5c0a0 | -11.86773 | -51.50026 | 2025-09-05 04:57:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 20301c5f-2adb-32ca-91ca-b2794a7a6043 | -8.93747 | -48.6473 | 2025-09-05 04:57:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ba5b93ae-e495-3808-8ac1-8efa97a7871d | -8.06396 | -52.38068 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 14b8cd9e-9d01-304a-a8a4-8f3f69261635 | -10.52696 | -57.77441 | 2025-09-05 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40a9fd7f-5ae0-3de4-9810-a4527d1c2fd0 | -12.3241 | -47.05114 | 2025-09-05 04:57:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 33378b39-2b99-3d3c-bedc-054fc1341d31 | -10.88021 | -55.38721 | 2025-09-05 04:57:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 672bf0a0-cb2c-3c3f-92a6-1345dc3715f8 | -10.46804 | -53.62508 | 2025-09-05 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 574f71c7-805b-363f-8d55-01116e040fe7 | -8.00491 | -45.44425 | 2025-09-05 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f239aab6-86f6-3b2b-b364-8496719d814b | -12.99658 | -54.83247 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ec13ecc9-d907-3dc2-8adf-8b92cccee292 | -12.98877 | -54.81654 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b01d382d-b535-371a-8843-7aeadbc40a6b | -13.55589 | -48.12748 | 2025-09-05 04:57:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11919704-a22e-314f-9879-3bdd6b119daa | -9.93144 | -60.1048 | 2025-09-05 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7901cc83-e686-377d-8588-32c0446dbf92 | -10.24172 | -50.55143 | 2025-09-05 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0dc2fe98-ca0c-3737-865e-ee1b24aeff24 | -9.76318 | -46.91595 | 2025-09-05 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f44f02e3-c91a-370e-b209-e44a9eb6b1a8 | -10.44886 | -53.61455 | 2025-09-05 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8372f91-f757-3153-ae23-bc7eb618c579 | -11.64876 | -54.53172 | 2025-09-05 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f50a15e8-bd54-31ae-8a09-47c90486441f | -9.5751 | -48.22917 | 2025-09-05 04:57:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df38a8b4-3553-33b2-9732-db8166a90fc6 | -10.97414 | -45.95403 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 12d0aeb4-5cbf-3faa-8db4-b9c1ffd60ef0 | -13.09378 | -57.11368 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da46832f-b2e0-3629-97d0-8d8dcfc246ea | -7.9769 | -44.52177 | 2025-09-05 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c1154604-8541-35ce-84fb-7e44d58245f4 | -12.5211 | -53.8381 | 2025-09-05 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e7162e1-18fb-3a25-b41f-eaebaca070a6 | -9.34192 | -55.21375 | 2025-09-05 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1ffbdf2-c2ed-30e1-87df-df197e114689 | -5.85445 | -57.76915 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1faec161-b652-360e-96a8-3164bb824757 | -6.84722 | -52.8021 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd094c92-ef7f-3f6c-9cca-1f9c3a3ddcde | -8.89586 | -45.76957 | 2025-09-05 04:57:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b22e1074-64f0-3378-b4c7-d8fc84909e82 | -7.95393 | -44.95053 | 2025-09-05 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4f36f1e-4322-3909-a14a-735daa6818a8 | -12.09178 | -44.72723 | 2025-09-05 04:57:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 39b6110e-bcf7-3f81-8a20-142776bff418 | -12.53246 | -53.80909 | 2025-09-05 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9a39cc0e-4101-3e72-8c87-20171f5a9d65 | -7.68231 | -50.26738 | 2025-09-05 04:57:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 472d4bfd-62e7-3ac5-ab58-5dee17f33c61 | -10.24255 | -50.54889 | 2025-09-05 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f5f627a9-7723-39f7-b560-228105cfa95a | -7.7106 | -45.16986 | 2025-09-05 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 623de649-6ac0-35a3-a7c7-d8fdea574002 | -12.90789 | -56.94027 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3c44565-1d91-3751-9feb-2c0174e99594 | -9.9795 | -51.63703 | 2025-09-05 04:57:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f4c19e38-e72b-3f93-98ff-93b2d9399cf6 | -7.51684 | -61.66813 | 2025-09-05 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 696d76c9-ff85-3dcd-9d8d-0873719b8d45 | -5.85509 | -57.77538 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bc0652b8-2e64-32e8-b9c3-3c0a5c5a3561 | -12.52223 | -53.8306 | 2025-09-05 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67d75a04-8953-3175-b614-822a7a1fe902 | -12.49498 | -53.84938 | 2025-09-05 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 995e0965-3420-3f3b-968b-038b48b4509f | -9.96949 | -51.65524 | 2025-09-05 04:57:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 94a470d7-8dbd-3dfb-b03f-c01185a0a39b | -10.50524 | -57.77484 | 2025-09-05 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0ae36d1-8f38-33dc-80c3-37551f31f69e | -5.48675 | -60.13979 | 2025-09-05 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 76f64f40-f4b3-3b9d-a143-c843a846e7ce | -7.9831 | -44.51851 | 2025-09-05 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0b20a39f-9420-341e-8a75-a3f041a45f53 | -12.88599 | -56.9478 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1163a071-6c26-3016-8537-5bf4d64f453f | -6.66364 | -57.63794 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3281647-c4a7-3137-9c60-1c0f6e0c2a73 | -5.90321 | -57.75034 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73c5ecc2-fb87-3a7c-bed2-3ba3ada2a3ec | -13.38144 | -45.73079 | 2025-09-05 04:57:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23026efd-7566-3e14-940b-b575f4031194 | -10.23147 | -50.53972 | 2025-09-05 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9517bfc2-d185-3a8c-969b-521b7c907d35 | -13.00453 | -45.22209 | 2025-09-05 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3b7c981e-8542-393a-b156-8695da711b42 | -13.27176 | -51.85628 | 2025-09-05 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e3ae82f-3ac6-3672-9f5c-d6a13d93801c | -9.63657 | -47.10602 | 2025-09-05 04:57:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0936e880-b45a-3959-a427-7eac4e31f7ad | -6.84666 | -52.80572 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 896d3246-eb9d-378f-b4f4-28942ba3a8bd | -11.0057 | -45.9204 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| debdae75-b44c-3d14-9953-1ab40977ca40 | -5.91564 | -57.72099 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d92fe907-54bc-386f-be20-9e04d91f81a8 | -9.61286 | -55.39022 | 2025-09-05 04:57:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bb938f9a-98e6-30fc-8da7-5cc3748f5dbb | -11.19912 | -55.02155 | 2025-09-05 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a105df94-2d1f-3714-9dac-ed043c2d97f4 | -12.97208 | -54.81385 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51880bd0-e82d-3db6-b461-5ec5c26bc1da | -10.09398 | -54.77301 | 2025-09-05 04:57:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 951fb067-c1bc-35b0-8c8e-e280228d52d7 | -7.61948 | -47.93886 | 2025-09-05 04:57:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b8872f1-579f-3d1b-a9f6-2bd6bb5d6f93 | -7.80109 | -52.13255 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e3936664-f7dc-3faf-bf00-13a4f5584eb9 | -10.95937 | -45.96328 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c727584a-b6ac-3a8c-bcf0-1de169d95250 | -11.31353 | -55.22358 | 2025-09-05 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 327c4e5e-7167-3630-a733-fb365f7d3437 | -10.66049 | -51.59795 | 2025-09-05 04:57:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e367e48-bd4f-3b0a-926d-1c51ff34a485 | -6.84104 | -52.84187 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0f73437-d0e5-341d-accc-8f773a7c0e48 | -8.02415 | -45.42305 | 2025-09-05 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 305a47d2-4503-38ba-8a6e-44b12a1a482d | -12.94158 | -48.05806 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5a62507c-a8ab-34a0-96fa-82f27aa73608 | -8.66287 | -68.74692 | 2025-09-05 04:57:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d7e88a9-0f9e-3a4c-932f-4a41d4a84ff6 | -12.90454 | -56.9397 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b02cf942-f2fd-3349-93bd-0c6cce925ff1 | -10.08471 | -45.26675 | 2025-09-05 04:57:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3858e2a3-df5c-3cfe-95d7-cf44c27ca5d0 | -10.09726 | -54.75204 | 2025-09-05 04:57:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88ab9654-bfd4-3689-b8ac-611babe4a82d | -6.83934 | -52.80828 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7282affb-d5ca-37b8-9f9b-16cfa8ac1d30 | -13.75496 | -49.10599 | 2025-09-05 04:57:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7972343b-3f5d-3275-a160-1e6c71efc5cf | -10.09395 | -54.75151 | 2025-09-05 04:57:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8bf9c20d-bd86-3972-beba-b402dc3d480c | -9.51046 | -57.78445 | 2025-09-05 04:57:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d800cd01-04e6-33b0-aeb4-aa204aed3046 | -9.96965 | -51.6536 | 2025-09-05 04:57:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 94a68e3c-0a99-373b-a331-6dd463178efb | -12.93197 | -48.05691 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3c745b44-94b7-391e-bf8c-b4958045c871 | -12.60732 | -56.99553 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e2f412c-a1cf-3e2d-a768-a8ffabf0835e | -10.76893 | -48.28606 | 2025-09-05 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9aa0395e-bcc0-3097-8d4e-a77abf7d16c7 | -10.46916 | -53.61775 | 2025-09-05 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3b8e2e30-bf66-3237-a73c-de55e7f40af1 | -7.59803 | -46.21196 | 2025-09-05 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 711b02ac-87b2-3d0f-b0f7-291a8a65adf2 | -8.00943 | -45.45096 | 2025-09-05 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc6b84af-f260-3dcd-b686-7209b4b29b8d | -11.26674 | -48.33381 | 2025-09-05 04:57:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 453f5bf7-35fb-3126-aa14-8fa470071f19 | -7.74384 | -48.79679 | 2025-09-05 04:57:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0d29de54-5a74-3713-854c-348f67da0bc9 | -8.51897 | -51.31437 | 2025-09-05 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c110d9a5-5ffa-3dfb-85eb-fbe8cd2b3fa2 | -5.50323 | -60.12128 | 2025-09-05 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab600137-32c1-3352-8843-cef061fea76e | -9.97218 | -51.63597 | 2025-09-05 04:57:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08b21e61-1fe8-3192-945d-dd72ce98c301 | -11.31629 | -55.22762 | 2025-09-05 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99c43de7-e1bd-3174-92ae-ed77e9e0ae98 | -11.09152 | -52.01905 | 2025-09-05 04:57:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README53.md)
