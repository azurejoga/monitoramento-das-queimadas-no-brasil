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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0fecb4df-00c4-3505-ac7b-9ba7fcbc8631 | -13.41553 | -54.32478 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ea185e6-b090-3aa3-b2cf-abe29ae70759 | -15.38438 | -52.79354 | 2026-08-18 04:40:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75f3520b-30fb-3843-a45e-be1b979902dc | -8.9548 | -60.5298 | 2026-08-18 04:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5013fc8a-0df1-3e7d-9cba-85d836aa8e81 | -14.85669 | -46.6334 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1666a899-2922-3082-9547-408455247c19 | -11.32609 | -55.27094 | 2026-08-18 04:40:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2674def3-01f1-36cb-a168-a739cd916c0c | -11.30369 | -46.33282 | 2026-08-18 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f668ecf-5658-3014-951e-e69e21d271ef | -9.18118 | -56.99039 | 2026-08-18 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2d8f23f7-a30c-3678-ac03-ca49c98cb02f | -14.17742 | -52.9014 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 26.8 |
| c6133b9b-af98-39bf-9223-2922de599255 | -13.42185 | -54.38825 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54171334-d39e-348e-b428-18e0169042ef | -14.50291 | -45.6783 | 2026-08-18 04:40:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a1dce756-c0a5-31ce-bf77-7f424718b23c | -11.14029 | -47.2709 | 2026-08-18 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2c917252-973c-3ac7-b620-55a9a8e1c248 | -14.18042 | -52.90744 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 05b5c232-8b79-3a8e-af3b-1509eab7a80f | -10.54471 | -52.30614 | 2026-08-18 04:40:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e0b96da9-980f-3311-b7fa-650bf4adbd5e | -12.00852 | -46.42383 | 2026-08-18 04:40:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a1d38774-41e5-3279-addf-f62135baab1f | -14.1756 | -52.91184 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 88652542-39fd-3afe-9bea-b77673cba516 | -15.92458 | -55.54128 | 2026-08-18 04:40:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c45bd3b3-6540-329f-bd07-959192aa4d88 | -17.18521 | -53.40358 | 2026-08-18 04:40:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 08d45868-df03-3e30-92d8-f6f660ff07a1 | -13.41559 | -57.0459 | 2026-08-18 04:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4af5333-b0f5-3b8a-ae7d-9ec1332aaa66 | -17.98356 | -44.4352 | 2026-08-18 04:40:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6fcf872d-fa14-3637-9587-e3e2831b8a0c | -12.52472 | -47.88923 | 2026-08-18 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9614a49d-d6b9-33f7-b535-3ff669cfa58d | -14.82881 | -46.63295 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 49700ba2-d6c0-3681-871e-95885bbae9b0 | -15.38906 | -52.78937 | 2026-08-18 04:40:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80e2917c-f479-3dd5-bb4b-9fb94d98f58d | -11.10544 | -49.90186 | 2026-08-18 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f57cdbd9-0c05-354d-a6a3-575a6cf0d253 | -12.71621 | -48.49166 | 2026-08-18 04:40:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4c88aa53-5421-3726-ad12-010d897f4c88 | -12.76869 | -48.4341 | 2026-08-18 04:40:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| afb48ea7-b635-388b-a8ac-ac11870147c3 | -14.16297 | -52.91453 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| de4d1319-d89a-3da7-b7f8-9afe5aa91549 | -13.41496 | -57.04912 | 2026-08-18 04:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73aeaaa2-a1f8-31f2-a5fc-31e71c82bb41 | -17.10358 | -46.58468 | 2026-08-18 04:40:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 50845b19-eadb-3b2f-a4cd-58aa9e0bf600 | -14.35615 | -51.96339 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d80f9fa-24fe-3aa6-8545-a8d5f95d1fdf | -12.77044 | -48.42334 | 2026-08-18 04:40:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 88bedf5b-85b9-3946-b671-df3a8e983e4f | -12.22626 | -47.03582 | 2026-08-18 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6dbbc353-7c6b-3179-ab27-03745dc35c17 | -14.1726 | -52.90587 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 5ecd44e4-ee5a-38fd-a487-7dcc02d71d4c | -14.83161 | -46.63754 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26eb3617-bf2c-39e5-8005-d754d681ec12 | -14.86802 | -46.65076 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34b5a8f9-9283-34aa-b6fe-03d7c28a60a4 | -12.46853 | -54.19662 | 2026-08-18 04:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 39da380c-cae5-3955-b28a-8c3c67dfe999 | -14.35203 | -51.93618 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fe514f27-c9cb-3bd1-a980-01460d018fa4 | -14.83962 | -46.63078 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fdc10626-beab-3752-81a6-3fd65293d00e | -13.55802 | -51.69451 | 2026-08-18 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ca460ac2-6be1-37c2-88a3-72f0a8a3311f | -15.37844 | -52.78236 | 2026-08-18 04:40:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73201e59-6c33-3be8-8347-4399d0165c0a | -12.90829 | -52.82566 | 2026-08-18 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 739cab91-493a-3308-a7de-81a521e3d521 | -14.83501 | -46.63815 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5210a46-a5df-3e47-9c8d-c520b644d63a | -14.17508 | -52.93801 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 049c4612-b09b-3b2c-9062-8f61678e6a6c | -9.16712 | -59.70462 | 2026-08-18 04:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 671450d3-2080-3e80-8a38-85aa80bdbca2 | -11.14305 | -47.27494 | 2026-08-18 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ead3252-bcb0-37a1-927a-997636c0aa8f | -14.82822 | -46.6369 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3dce58c9-f976-3bd1-8853-a0e58f05fc8a | -14.16089 | -52.90329 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| adbf8ec9-1297-3cd3-b4bc-28c9df7449ae | -14.25414 | -51.92767 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 64cbdac9-bd29-350a-95b0-1e305c3e674a | -8.89879 | -60.59409 | 2026-08-18 04:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 151fef2c-ddb0-395d-a888-e6220ff62716 | -11.11326 | -46.49837 | 2026-08-18 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6d9f7134-427b-391e-b45f-647fd9c58f92 | -13.26707 | -51.65148 | 2026-08-18 04:40:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a04e92fe-0f6b-34d7-9cc1-5eb268d3471a | -12.70162 | -48.51852 | 2026-08-18 04:40:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 210b6c2c-1303-3ef9-bf0a-778146160102 | -12.51978 | -47.87758 | 2026-08-18 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6312bf18-aff7-350a-808b-ad6d11a90225 | -14.83281 | -46.6296 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f1a5e4c-dc86-3821-8c8d-b1911e8b65a4 | -11.62271 | -46.77934 | 2026-08-18 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3aaeb79a-cdfd-3ce8-8084-a6d3b40077f6 | -12.75428 | -48.4248 | 2026-08-18 04:40:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8d96543f-b9eb-37ef-88c2-1a5bd5c96630 | -10.27062 | -50.4149 | 2026-08-18 04:40:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bae2a3b9-7d7e-3cf0-ae71-6b07bcd65024 | -10.2677 | -50.40683 | 2026-08-18 04:40:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0e3b42b-91cc-3da8-9e03-bd964c0fef95 | -11.23851 | -54.01691 | 2026-08-18 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b9390c0-0f24-33ad-b51d-a66a47ecc17a | -9.42487 | -60.4496 | 2026-08-18 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f6c0615b-df6c-374e-9763-528c181d7eb6 | -14.17121 | -52.92936 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e67dc184-72f6-30df-b983-d5b389816735 | -9.18189 | -56.98656 | 2026-08-18 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| de55dd1d-0e38-3aa0-99f0-4fbb49ebb397 | -13.28274 | -48.69151 | 2026-08-18 04:40:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3e62ad7e-a7d0-32af-920b-5ed7d80d73aa | -14.36457 | -51.87242 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 50944967-205f-3406-9db6-7d01b1e184c8 | -11.11662 | -46.49886 | 2026-08-18 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ed3933e-22eb-32f0-98fb-4c7f086a423c | -13.79031 | -53.84377 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 08bf6d5d-ab17-39e3-a3c3-6cba9ef416ed | -14.805 | -46.65195 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| acfb59f1-f486-3ada-b6ba-e95dd02e8d51 | -12.47088 | -54.18377 | 2026-08-18 04:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b08c61a6-bbca-31cd-a367-5515158e4c3e | -12.9418 | -56.64175 | 2026-08-18 04:40:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0038f542-3945-3f6c-b0a0-85804e57687c | -14.17213 | -52.92432 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 22c39b55-85fa-3337-8afb-ca483b6f907b | -11.39002 | -46.40582 | 2026-08-18 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61db7592-a234-3237-bc5c-a8089d25eba5 | -14.17053 | -52.89453 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7402eb13-1a9d-3fb4-a5c6-d4d7085fe326 | -11.36426 | -46.39437 | 2026-08-18 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 37fcb6eb-2b32-3c92-8725-74cd377f9e2b | -14.17169 | -52.91105 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a3fc38eb-39b1-31a5-9c6d-5d33020bd504 | -16.22873 | -57.64459 | 2026-08-18 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 70780c36-23d1-35bd-9928-67554bb9a889 | -14.18181 | -52.91567 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 47bc894d-8caa-3ba9-8efd-7b1914724247 | -10.14436 | -54.2768 | 2026-08-18 04:40:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 82ed58bd-1181-34bb-9985-2f32416f4c1c | -13.40365 | -54.34036 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 52c448f7-df7d-311f-9a47-5c97419f7f16 | -11.13143 | -47.28384 | 2026-08-18 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 05b2e6a9-26a2-3f6b-a48b-8765be53b0dc | -12.76985 | -48.42694 | 2026-08-18 04:40:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3d48621-1c49-3a05-a82e-af93564ab30c | -11.53176 | -46.6445 | 2026-08-18 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e5ec0002-8a0c-32e6-ac19-d8e0daef8c47 | -9.42561 | -60.44608 | 2026-08-18 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7b432f2e-486c-3b2a-95e6-879d024b30a4 | -16.57261 | -51.62074 | 2026-08-18 04:40:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 59a5bdb8-8bdf-380a-bdbf-bf919c9d2f1a | -17.10416 | -46.58071 | 2026-08-18 04:40:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a9649f24-ec23-32af-aecf-54eff7cd39d9 | -11.19278 | -49.6843 | 2026-08-18 04:40:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8ce3e6b-e95c-3ad3-87a7-5196f5a63e43 | -11.46303 | -46.56799 | 2026-08-18 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 14238538-a2cb-327c-b752-e14acff5f6cf | -17.45876 | -47.86451 | 2026-08-18 04:40:00 | NPP-375D | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bc860648-616a-3133-b522-15e63b9e2824 | -15.29692 | -56.44587 | 2026-08-18 04:40:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0040f603-a7c1-3202-809e-452d9b371506 | -11.12535 | -47.27925 | 2026-08-18 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 320ab60a-33e3-3814-90a7-fb1e7c7b5d5e | -15.27258 | -56.49296 | 2026-08-18 04:40:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24558333-7d98-3774-b5e8-83eb4aa0cd22 | -13.5085 | -46.28504 | 2026-08-18 04:40:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c40cf9ac-3bea-316d-b5b3-450ea60441cd | -15.91239 | -55.55614 | 2026-08-18 04:40:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 33b4ae9f-ba5a-3767-bd53-fdcbe0441179 | -14.35801 | -51.93118 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e0968d6d-005a-3ff5-a711-8364092ac8f9 | -14.17697 | -52.92 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 25.9 |
| d923e3ff-e440-36c9-bab3-bb83b96b8d4a | -11.12213 | -46.49563 | 2026-08-18 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 84ee899d-d037-3d2e-808a-57b90493c4b4 | -11.14175 | -49.03959 | 2026-08-18 04:40:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1bee17f5-3868-36cc-abdf-f36626e6cdcb | -12.55191 | -47.88643 | 2026-08-18 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bb8afa80-3a0c-32b9-b39d-b120cbf532be | -14.80897 | -46.64874 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| eac41859-70d9-3a89-9f04-6dc8f0347ad9 | -14.18089 | -52.92075 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 2311a189-04c3-3e47-acaf-dfb8d0d52c1e | -13.3985 | -54.34383 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41c57dcc-4053-3a92-9b6f-37582b37ddcc | -14.48221 | -53.10021 | 2026-08-18 04:40:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README29.md)
