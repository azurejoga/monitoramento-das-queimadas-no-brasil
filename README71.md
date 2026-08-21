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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4291ec24-c828-35ee-8031-0f685e7ca463 | -11.19819 | -55.05048 | 2026-08-21 05:25:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a44ecee8-48a9-3f26-a704-87e7b2121e21 | -9.39585 | -60.56386 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2449c939-ccb3-3844-8b18-43e5cb058b9c | -10.80628 | -50.2771 | 2026-08-21 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cb130e42-6f74-3a21-8592-d351bf85b7da | -10.82306 | -50.99461 | 2026-08-21 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f6b0d32-5e87-3f42-acd0-221939a3b2fe | -20.27008 | -46.75478 | 2026-08-21 05:25:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 22a6de29-7452-36d5-8297-e60b3cbf4517 | -11.20863 | -55.05657 | 2026-08-21 05:25:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f41d06f2-ae6d-3c17-890c-2b8031487f80 | -11.16564 | -54.02645 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 631035ca-6d3e-37df-a780-38bd3f4280cf | -10.82237 | -50.99978 | 2026-08-21 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad8905e6-c5f1-36c4-97ef-772710412631 | -10.24382 | -54.36128 | 2026-08-21 05:25:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e7076a6d-a80b-39ae-9a0c-8de30374655e | -12.78755 | -48.45294 | 2026-08-21 05:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4c245c43-ac2f-3173-bfb5-2cfd6df31531 | -10.81207 | -50.27197 | 2026-08-21 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 21fd9643-53de-3529-9a2b-8576c91d7dca | -10.24556 | -54.37589 | 2026-08-21 05:25:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c62a6f3-12e9-3530-a37e-ffdbae7cdb84 | -12.74371 | -48.47392 | 2026-08-21 05:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fee3a7b4-edd0-329f-8867-de169cdeb703 | -12.47558 | -54.1775 | 2026-08-21 05:25:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b58a1fd-8c59-3a71-ae58-1e2da34e0e70 | -11.16243 | -54.0209 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e8c386ff-67a3-3e74-8d33-2f1a769795c5 | -9.4036 | -60.42998 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0b88da3c-1665-3a37-9c46-f3adc1214c89 | -12.78722 | -48.40318 | 2026-08-21 05:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c5fda78c-db86-3496-9e72-8ac69e031f17 | -10.38386 | -61.20732 | 2026-08-21 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 113b325e-269a-37da-8980-0d459563e652 | -20.28368 | -46.74141 | 2026-08-21 05:25:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 68d65b66-7a81-3f41-8f9d-2407f9ca28a8 | -10.80127 | -50.27643 | 2026-08-21 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 26fe02e1-e761-38f5-8d37-cd558d0a2ef7 | -11.20077 | -54.00241 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7697fdac-6190-3f95-beb6-0d28009367d5 | -9.41686 | -60.43612 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b82d4290-c4ab-3e32-aed6-82170d211419 | -11.20124 | -55.05547 | 2026-08-21 05:25:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 804f6fb5-e909-3df0-9f4c-1cbaf4674e9a | -9.40602 | -60.5456 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd008e26-7bb0-3b0b-bba0-cf58d0de1f12 | -11.17419 | -54.02261 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5145037d-2661-3487-80f9-7fedca258390 | -9.23606 | -60.39174 | 2026-08-21 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1aa7e905-55a5-3928-bc9c-25d19f4c9568 | -10.89773 | -50.27866 | 2026-08-21 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b976ed27-9678-325a-aaaf-29979b160a4a | -11.2047 | -54.00297 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e4aaa770-efe0-39e8-b248-3db4b3f92be5 | -9.39649 | -60.55997 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7183924-d9a0-3285-bd2a-c46b2e73ff93 | -19.66801 | -46.04181 | 2026-08-21 05:25:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7c063254-60f6-37aa-ad4f-07702635d02e | -12.01031 | -53.43968 | 2026-08-21 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a96a5c21-068f-3d40-84b5-4cfb55e6f70b | -9.40475 | -60.55338 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f9c5901-f6dd-3d9e-95fe-50d23bc4e675 | -9.21016 | -60.76809 | 2026-08-21 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 148402ba-b60d-31e5-8cdd-f346bef69fdc | -9.40487 | -60.42226 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 806ab09a-1103-37c8-96a2-c5f1d20bcaa8 | -11.20139 | -54.00086 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8dc9dcf-7f8b-3a96-bf7a-c275367b9761 | -9.41522 | -60.55512 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 724d7f6e-250b-30fa-be89-b89a2eca6625 | -19.73508 | -57.97092 | 2026-08-21 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 25abc528-e205-39d5-9b86-cdcfb8788c5a | -19.73746 | -57.95432 | 2026-08-21 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 2f8e7b0c-331d-3b1c-af4b-821c1749c1ed | -12.84761 | -48.44352 | 2026-08-21 05:25:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7af08b64-7e74-390f-bf42-bce8b3eed622 | -22.15919 | -46.65563 | 2026-08-21 05:25:00 | NPP-375D | SANTO ANTÔNIO DO JARDIM | SÃO PAULO | Brasil | 3548104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 152ebdcb-1178-3951-9ce8-d274c1092630 | -9.41055 | -60.43112 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 05ce6e05-f2c9-3424-910b-136799412d74 | -19.74859 | -57.97732 | 2026-08-21 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 216a34c2-3a1b-3737-ad63-0f5401e5f44e | -10.24691 | -54.36666 | 2026-08-21 05:25:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0fe07112-980d-3233-9e6b-6a40a2ff414a | -19.7392 | -57.96734 | 2026-08-21 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 9df54e59-904d-30c2-bee3-22c3a40e0eb8 | -18.03447 | -46.4688 | 2026-08-21 05:25:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6209bc2c-dfc1-381b-980f-05d2c587f0df | -12.78802 | -48.40063 | 2026-08-21 05:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| da791401-7c7e-3e4a-b74b-6fde8ccb6a03 | -19.75212 | -57.97788 | 2026-08-21 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 6395fdb7-be6f-36ae-ad35-8fa6c0a4f2bf | -9.40126 | -60.55278 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fa3d727a-aa81-3efb-8e77-81c8a8a371c0 | -22.29536 | -51.83875 | 2026-08-21 05:25:00 | NPP-375D | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f90046a6-3f03-3d9a-ae28-4bc3dde137dd | -9.42192 | -60.40534 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| baf36280-6790-3742-a18c-6b2419b34446 | -11.20558 | -55.05159 | 2026-08-21 05:25:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2e75a48c-5c95-3c36-9fae-503f8e1784f4 | -10.39874 | -61.20571 | 2026-08-21 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5eb555f6-af7f-3fec-9a75-491435a2fa97 | -12.71932 | -48.48077 | 2026-08-21 05:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 51afbe3d-6eb2-35f4-85c1-708ea5c154aa | -12.74091 | -48.44799 | 2026-08-21 05:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 06f08c5e-70bf-3c3f-b4d9-edbaa99f4502 | -10.76021 | -50.31778 | 2026-08-21 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1f471079-314c-3c76-b1d3-ccd51e44de17 | -9.40898 | -60.41898 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 2a00b774-dc27-322e-89f5-8bb39dfdad67 | -11.17277 | -54.0325 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8027a7f4-e7f0-3379-9498-bfca278c40f1 | -10.76237 | -50.30598 | 2026-08-21 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 56cc6790-6a66-3533-aca5-0c7a3bd5aedc | -11.68351 | -54.56303 | 2026-08-21 05:25:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17b89ea0-2a5a-317b-b871-a90c60222b5a | -19.67524 | -46.04263 | 2026-08-21 05:25:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 55ea287b-e5b9-30e0-bafd-ea1129168dc4 | -18.0404 | -46.47152 | 2026-08-21 05:25:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96b5834e-879d-34b5-bbc8-29275ce08600 | -9.11434 | -61.60622 | 2026-08-21 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3226adbf-ca38-34a5-9dcb-55c52be3c0aa | -19.75917 | -57.97902 | 2026-08-21 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.3 |
| 758bbe71-7440-30cd-9d70-626ef8f50365 | -9.41593 | -60.42013 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8e5654e9-ad07-3b3f-bae2-478ee0932d51 | -9.41435 | -60.40804 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 5d290fc0-a9b5-32d1-aab4-5e900f8b9c46 | -9.40204 | -60.41784 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 1cd93b09-b52c-3907-b3ef-442895bf2e4b | -12.50713 | -47.85293 | 2026-08-21 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c29c1847-165f-3ac9-ae8b-20b012059888 | -11.68418 | -54.5583 | 2026-08-21 05:25:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a51a148-e5cf-386a-a3a2-4c1e060b8373 | -19.73452 | -57.9496 | 2026-08-21 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 6cb937aa-a4d1-3772-a2b6-b7fedae191ed | -10.75799 | -50.33503 | 2026-08-21 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cbeb7855-4091-3172-a603-7eda145cdb9f | -17.96284 | -49.37346 | 2026-08-21 05:25:00 | NPP-375D | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e3b9758-4e9d-3c2e-96ba-272482e7e1c6 | -22.2957 | -51.83535 | 2026-08-21 05:25:00 | NPP-375D | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| cee1f8d7-cb90-3574-a1de-0d5244ee4751 | -10.90275 | -50.27934 | 2026-08-21 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 486932c2-7c97-361a-9498-9c7cfbc618fd | -11.84093 | -58.84734 | 2026-08-21 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b415b12f-10e2-3c17-86b9-dbd59c74c24d | -9.40888 | -60.55006 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f6e2392-6f24-36b8-80c7-8eb31197feb9 | -12.809 | -48.41954 | 2026-08-21 05:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f8c2d2cb-6dee-323b-8c98-cc6b2e41857b | -12.75126 | -48.4601 | 2026-08-21 05:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1790ccb7-d0aa-3134-8afe-5479dba47b0d | -9.39934 | -60.56445 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b2485d4-d260-377e-a98f-9ab833ed2172 | -9.41656 | -60.41629 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e2fa5bc6-1fcc-38ee-a403-4663d24b6a56 | -9.40741 | -60.40687 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| df732b83-114e-3fc1-90db-ac8755e47c76 | -9.4187 | -60.55572 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3074216d-50f1-3952-93fa-8007d22ae15e | -11.55503 | -46.94015 | 2026-08-21 05:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 015c6a24-ab27-376f-99d1-119e1ce9fe79 | -10.80705 | -50.27129 | 2026-08-21 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9ad561d6-e998-34a1-9bcc-70441b6d9740 | -9.41845 | -60.40477 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f6cb1c52-7723-3341-bea3-6d41d6c97e2e | -20.26882 | -46.75171 | 2026-08-21 05:25:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4aa60cd4-0847-3643-a07a-e336b08c8402 | -17.96245 | -49.3774 | 2026-08-21 05:25:00 | NPP-375D | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8bfca11c-7b7a-3806-a824-3d70911b088a | -22.17941 | -48.73793 | 2026-08-21 05:25:00 | NPP-375D | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| c38ec191-435f-360f-b842-086f79655c22 | -9.40835 | -60.42283 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2c3a09d7-cc54-3003-a962-80c8f440b62f | -12.78224 | -48.3994 | 2026-08-21 05:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7deb81cf-8780-31ce-975f-fc81e52605bb | -9.40267 | -60.41399 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| c46f8a20-6bcf-3bc1-a3ad-d38623654971 | -9.41498 | -60.40419 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d74b91c5-461d-3107-b074-452ffcce5c67 | -12.74664 | -48.44943 | 2026-08-21 05:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29637568-ebdf-370e-ac2d-343ff6732f0e | -10.77245 | -50.30187 | 2026-08-21 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b583ec99-0f84-3d08-b332-249cb8f2e7bc | -11.66487 | -48.3535 | 2026-08-21 05:25:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 27e9e5b0-7c68-3afd-9d02-ff844d116dc1 | -19.74039 | -57.95904 | 2026-08-21 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 7f382ec3-8653-3fcf-b206-091c823fa47e | -9.21655 | -60.77325 | 2026-08-21 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88242fb5-eec4-3fd7-b0a7-831a32a48239 | -9.41182 | -60.42341 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2f495256-2f5b-32cd-b0bf-0588deca5eef | -9.39777 | -60.55218 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea46bfef-517a-3e12-940b-d43879fc7d7a | -9.4076 | -60.55784 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e46cd9c-b421-3018-8580-27709a403a50 | -12.72597 | -48.47441 | 2026-08-21 05:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README72.md)
