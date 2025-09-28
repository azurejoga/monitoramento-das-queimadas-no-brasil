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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aaa7b7be-8215-3772-87c5-b5f02b328b09 | -13.00755 | -49.45385 | 2025-09-28 05:18:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f9c273e4-64c9-30a7-be0a-04097b14a45e | -13.60496 | -48.10285 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9166c7ff-9494-3df6-b449-2cf115bc7413 | -13.59305 | -47.31981 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 72d1cb67-92a3-302d-95c5-27bde6e5fa2a | -13.01872 | -49.46288 | 2025-09-28 05:18:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| dc1bb91c-3283-37df-b2f0-4987cdb17d61 | -12.65867 | -51.66704 | 2025-09-28 05:18:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89411e2c-ce5f-3042-8f6f-fcb35b77700e | -13.58644 | -47.31634 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a9459d9e-d2d3-3762-b1b9-48d01b9c81c3 | -12.66048 | -51.667 | 2025-09-28 05:18:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| febb39c8-5652-3dc9-aa6a-0214c8f4c60b | -13.61381 | -47.32092 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f4d19a8b-04b9-3e3b-86f5-a3f08aedda0c | -13.79542 | -47.92667 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 294ee71f-2681-386f-815c-f21a8eeb02ad | -8.94616 | -65.92242 | 2025-09-28 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 479f32b3-32cf-357b-9f76-ffd9560f3d65 | -12.6505 | -51.66261 | 2025-09-28 05:18:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| adb6bf44-7ddf-3a7d-b1e1-530ddf59fdfa | -11.62221 | -52.85155 | 2025-09-28 05:18:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 237a2581-8ce6-3093-b5cf-40158103b2ac | -13.25047 | -48.45016 | 2025-09-28 05:18:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 263e3a4f-dfa1-3bcd-b2da-fbf2e05b1e6d | -8.48484 | -47.80352 | 2025-09-28 05:18:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf586a05-743a-3674-b121-2fe49d1e4a07 | -9.26533 | -64.50486 | 2025-09-28 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44aa1c57-0809-3b5a-9d96-7b16607a7f19 | -13.62275 | -48.06953 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ce377de0-b6df-312a-a032-fb9601aa0246 | -10.85457 | -47.79812 | 2025-09-28 05:18:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f8645339-e579-3c8d-8fc7-47e37a2db800 | -13.79722 | -47.90968 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4cb8a94e-9c91-3687-ad6e-4b3bfa3531b5 | -9.65245 | -62.83907 | 2025-09-28 05:18:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b0ae8754-8658-3152-b060-0145fb8fa498 | -13.59926 | -47.32713 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ff7161b8-0e41-3877-adfa-65d50c0fc4e6 | -13.60709 | -48.09084 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e9cc7985-6b9d-378e-9278-cd5d6e8893cd | -8.86538 | -46.60077 | 2025-09-28 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f7c39d5e-0f84-3547-9507-18d9bd698b6c | -12.99304 | -49.4505 | 2025-09-28 05:18:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| aefc37af-0b62-3da9-94ca-6dafbd0547da | -12.00366 | -47.03604 | 2025-09-28 05:18:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b32ee0fb-b31e-3ca6-9cc8-5434ada15c2c | -11.94321 | -47.9233 | 2025-09-28 05:18:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a17d5b62-2d86-3f58-9172-e48c967770ea | -11.98856 | -47.04682 | 2025-09-28 05:18:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2d8ba325-46ba-3b3f-9394-504d891ddd1c | -9.86691 | -65.16968 | 2025-09-28 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9397d6f9-b626-33eb-a9e7-6e81a5bf9cc7 | -12.6942 | -46.87891 | 2025-09-28 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0bde3a3c-4d8e-3d38-b1b3-4eeab3be64c2 | -12.69327 | -46.87923 | 2025-09-28 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b474b16d-e4cd-3729-9966-a97d488dd317 | -9.73482 | -62.36435 | 2025-09-28 05:18:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3044a4d-a579-353f-8e60-4e5336d1f50f | -11.52441 | -54.31431 | 2025-09-28 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 71806521-87f7-37f0-abb5-4d9d900a1e77 | -9.57214 | -63.207 | 2025-09-28 05:18:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3162754-e201-302e-a43f-0c8e21e2d31b | -13.40211 | -48.15482 | 2025-09-28 05:18:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1a1ba9bc-999b-3047-a3fd-f9091eb59827 | -9.94035 | -65.20485 | 2025-09-28 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6477d4e4-f648-3e42-84bc-3b6240fe2164 | -13.5883 | -47.29796 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 81c8f879-c29f-3b47-91f9-4b455f555181 | -9.83235 | -58.04665 | 2025-09-28 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0189895-7331-3a60-9a16-eca968e14e92 | -10.84792 | -51.89958 | 2025-09-28 05:18:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 22260f44-6590-3777-a3ea-0bd07d05446a | -9.92781 | -55.22582 | 2025-09-28 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2e38b14-e82c-30bc-9f29-223a2d555d12 | -13.59904 | -47.32371 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ec621e22-8503-342c-93d2-30f9ce1c64ae | -11.94842 | -47.93513 | 2025-09-28 05:18:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ef3a2c19-2481-3450-8731-a30c63b7af47 | -9.0476 | -46.72482 | 2025-09-28 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bd4e63b2-77af-3f4f-9081-7757bc7cc2f9 | -9.73962 | -62.35705 | 2025-09-28 05:18:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6866d1f5-c7f8-3d83-9c9b-2611fdaf90ab | -13.62745 | -47.32355 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3949ead5-28af-328b-9b9f-e086b4e6d874 | -13.62531 | -48.09887 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e5d3844f-a9a2-30b0-abe6-adf140346790 | -10.94209 | -47.78679 | 2025-09-28 05:18:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4b9fc2b7-5fbd-36f6-8611-6544136339c9 | -11.37327 | -55.14277 | 2025-09-28 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 328fbfdd-8e3e-3653-a18d-156cfd8271c4 | -11.14511 | -54.31241 | 2025-09-28 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| edb456a3-cfcd-3bea-95b2-fe2638feba1f | -9.68638 | -63.17598 | 2025-09-28 05:18:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 27f0ec65-511c-340c-b9cd-9274fa2ee4b4 | -11.99641 | -47.04842 | 2025-09-28 05:18:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ee19bc9c-65f5-31e8-9017-c289820e7214 | -8.82906 | -46.20821 | 2025-09-28 05:18:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4069ea1c-1e45-3cb7-9574-a0597794e701 | -9.56132 | -63.20227 | 2025-09-28 05:18:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 00bbd3a5-04d6-38fe-bc8f-ed46e353a498 | -11.58735 | -54.48776 | 2025-09-28 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 206d5b17-3c7b-35c9-8572-37baf727b63e | -9.51514 | -54.66138 | 2025-09-28 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d872edfe-3723-3bc9-a104-6f47b94eb378 | -9.96019 | -64.75575 | 2025-09-28 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df1c2d5b-1c57-3c89-9442-34950b16900f | -11.97035 | -63.1682 | 2025-09-28 05:18:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6bbabbbe-6d00-336d-92a4-f9f6ff444751 | -12.68053 | -46.87467 | 2025-09-28 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 992b1ec8-6655-3bda-bda0-3592e7ea1c79 | -13.60728 | -48.08037 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 9c0ff45a-9e2d-3ce2-80e0-145afff9d892 | -13.78114 | -47.87011 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 951d900f-e3ca-3d7b-9c19-41b2065ba14e | -13.5726 | -48.28459 | 2025-09-28 05:18:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 74109edb-e068-3e5f-a670-570e6b336ac6 | -11.15461 | -54.30571 | 2025-09-28 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7662fe47-6fbd-325a-9d0a-4be5c8fa7676 | -9.49516 | -48.51405 | 2025-09-28 05:18:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d46f4925-45b7-3b85-aa6b-98653cdb3d58 | -12.88081 | -47.09301 | 2025-09-28 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 06803a67-f00f-32c6-bcf5-6dd9320eaf61 | -9.56049 | -63.20943 | 2025-09-28 05:18:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4e9de59-5430-3ff9-a7b1-3231d32d8340 | -13.60668 | -48.08619 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 365c4419-7a56-3e5f-8210-389ed5fa3575 | -13.5857 | -47.31834 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 02990d76-02cf-385f-a3bb-fb37fc2fb230 | -13.75255 | -47.88575 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0012ff14-5cc7-3a9c-a5bd-1bc57a987844 | -13.61252 | -48.10194 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 787fddc5-e079-3f4f-9c97-9d806180fce4 | -10.94268 | -47.7818 | 2025-09-28 05:18:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 366fc238-b282-3cc5-9ab5-70efdcff3deb | -12.98757 | -49.44505 | 2025-09-28 05:18:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 28dfb853-99d9-38e3-ad3b-d54a7dc098cf | -11.94911 | -47.93119 | 2025-09-28 05:18:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b8318c41-6306-36ac-b967-fbad6d095db1 | -11.99877 | -47.90063 | 2025-09-28 05:18:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3a00a661-2100-397c-8192-9ca77cd5709f | -10.20282 | -58.21917 | 2025-09-28 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 212962a8-7884-3cee-a68d-fdd2fb1e63ad | -11.62289 | -52.84642 | 2025-09-28 05:18:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4ce0b59b-5e55-31c1-9ece-31eceefb2c0c | -13.58726 | -47.30384 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a4bfcb53-fc07-3b80-bb6b-c86c522adb88 | -11.99469 | -47.0542 | 2025-09-28 05:18:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0b247f2e-3282-3414-9fc2-ebdff1dae193 | -12.64394 | -51.70062 | 2025-09-28 05:18:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84fc0b9d-d5f4-3e33-91dc-c9f881046eb3 | -9.21783 | -46.77958 | 2025-09-28 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| bef0c446-b018-3878-baef-e16db7d2be57 | -13.40149 | -48.16079 | 2025-09-28 05:18:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 837e3ea1-7f53-331d-85fb-950947ef3d24 | -6.59785 | -62.93323 | 2025-09-28 05:18:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c729897-de0f-3c63-91be-9c68fac750ee | -13.61437 | -48.0761 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fcd8b44c-9f30-3522-9412-a34fae87a3bb | -12.32493 | -51.51568 | 2025-09-28 05:18:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ca60d0a-a1ff-3e30-a237-27765ede9576 | -12.67877 | -46.88285 | 2025-09-28 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5bc822e2-67bd-3be7-b9d4-28b3cca04993 | -11.6509 | -52.86828 | 2025-09-28 05:18:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 85f2328e-8d48-3cc6-90ac-a16b24fd75bf | -11.58788 | -54.48383 | 2025-09-28 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6de2ce22-97b4-3e02-bf48-402a4e7e4a48 | -13.01643 | -49.45874 | 2025-09-28 05:18:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4711de5e-0f9d-3e0d-a59f-912adbc2dde1 | -13.00448 | -49.45681 | 2025-09-28 05:18:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1c984420-df40-3a95-9809-c840ca158c8c | -9.64888 | -62.83844 | 2025-09-28 05:18:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5fe010b2-abc9-3d13-ad78-72790270de42 | -10.04751 | -62.45088 | 2025-09-28 05:18:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1caf679d-bbeb-3322-968c-89e55b168a09 | -8.86465 | -46.60669 | 2025-09-28 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8719af3a-0098-3f95-a320-70e64e923d40 | -13.78562 | -47.89188 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a78ff6ad-4be7-3120-b0af-b9d9fd232b6c | -12.88772 | -47.0969 | 2025-09-28 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bdd8b772-9ed3-3a10-b91b-cf339711a0a2 | -13.61556 | -48.07431 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eb89959b-9321-3142-988b-781c3a6e27f4 | -9.79637 | -61.49115 | 2025-09-28 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c5a7f1f-d782-3562-a3a7-8e082926e804 | -12.65389 | -51.6633 | 2025-09-28 05:18:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc2747b2-ad54-372b-b7b1-a6795ca09671 | -12.6796 | -46.87473 | 2025-09-28 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d43d1b3d-7b3d-3374-96b2-6846d8b34f90 | -9.7466 | -62.35818 | 2025-09-28 05:18:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c5798e7-fdd2-3808-9b0a-9f1df84bdbc5 | -13.58773 | -47.29943 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 640c3251-7e12-3263-87e1-6b6c36881a7c | -13.01001 | -49.46157 | 2025-09-28 05:18:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d55e6062-7963-3a1e-8a9a-0ae69834213d | -9.88637 | -58.29104 | 2025-09-28 05:18:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53057646-bb9d-3176-a351-1729dbd114f8 | -12.00459 | -47.0367 | 2025-09-28 05:18:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |


[Clique aqui para ver as próximas entradas](README86.md)
